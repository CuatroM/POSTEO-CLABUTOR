"""
Publica en Instagram el próximo post pendiente de la carpeta posts/.

Cada post es una carpeta dentro de posts/ con:
  - una o varias imágenes .jpg  (1 = post simple, 2 a 10 = carrusel)
  - o un video .mp4             (se publica como Reel)
  - texto.txt                   (el texto del post, con hashtags)

Las carpetas se publican en orden alfabético. Las que empiezan con "_" se ignoran.
Si el nombre empieza con una fecha (AAAA-MM-DD), no se publica antes de ese día.
Las ya publicadas quedan anotadas en publicados.txt.
"""

import os
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import quote

import requests

API = "https://graph.instagram.com/v25.0"
TOKEN = os.environ.get("IG_TOKEN", "").strip()
IG_USER_ID = os.environ.get("IG_USER_ID", "").strip()
if not TOKEN:
    sys.exit("ERROR: falta el secreto IG_TOKEN (o está vacío).")
if not IG_USER_ID.isdigit():
    sys.exit(f"ERROR: el secreto IG_USER_ID tiene que ser solo números (tiene {len(IG_USER_ID)} caracteres).")
REPO = os.environ.get("GITHUB_REPOSITORY", "CuatroM/POSTEO-CLABUTOR")
RAMA = os.environ.get("GITHUB_REF_NAME", "main")
CARPETA_FORZADA = os.environ.get("CARPETA", "").strip()

RAIZ = Path(__file__).parent
POSTS = RAIZ / "posts"
PUBLICADOS = RAIZ / "publicados.txt"
HOY = datetime.now(timezone(timedelta(hours=-3))).date()  # hora de Argentina


def api(metodo, ruta, **params):
    params["access_token"] = TOKEN
    try:
        r = requests.request(metodo, f"{API}/{ruta}", params=params, timeout=60)
        datos = r.json()
    except Exception as e:
        sys.exit(f"ERROR: no se pudo conectar con Instagram ({e}).")
    if "error" in datos:
        err = datos["error"]
        sys.exit(f"ERROR de Instagram: {err.get('message')} (código {err.get('code')})")
    return datos


def url_publica(archivo: Path) -> str:
    ruta = archivo.relative_to(RAIZ).as_posix()
    return f"https://raw.githubusercontent.com/{REPO}/{RAMA}/{quote(ruta)}"


def esperar_listo(contenedor_id, intentos=60):
    for _ in range(intentos):
        estado = api("GET", contenedor_id, fields="status_code,status").get("status_code")
        if estado == "FINISHED":
            return
        if estado in ("ERROR", "EXPIRED"):
            sys.exit(f"Instagram no pudo procesar el contenido ({estado}).")
        time.sleep(10)
    sys.exit("Instagram tardó demasiado en procesar el contenido.")


def elegir_post():
    ya = set(PUBLICADOS.read_text(encoding="utf-8").split()) if PUBLICADOS.exists() else set()
    if CARPETA_FORZADA:
        carpeta = POSTS / CARPETA_FORZADA
        if not carpeta.is_dir():
            sys.exit(f"No existe la carpeta posts/{CARPETA_FORZADA}")
        return carpeta
    for carpeta in sorted(p for p in POSTS.iterdir() if p.is_dir()):
        if carpeta.name.startswith("_") or carpeta.name in ya:
            continue
        fecha = re.match(r"(\d{4}-\d{2}-\d{2})", carpeta.name)
        if fecha and datetime.strptime(fecha.group(1), "%Y-%m-%d").date() > HOY:
            continue
        return carpeta
    return None


def main():
    cuenta = api("GET", "me", fields="username")
    print(f"Conectado a Instagram como @{cuenta.get('username')}")

    carpeta = elegir_post()
    if not carpeta:
        print("No hay posts pendientes para hoy.")
        return

    texto_archivo = carpeta / "texto.txt"
    texto = texto_archivo.read_text(encoding="utf-8").strip() if texto_archivo.exists() else ""
    if len(texto) > 2200:
        sys.exit("El texto supera los 2200 caracteres que permite Instagram.")

    imagenes = sorted(f for f in carpeta.iterdir() if f.suffix.lower() in (".jpg", ".jpeg"))
    videos = sorted(f for f in carpeta.iterdir() if f.suffix.lower() == ".mp4")
    print(f"Publicando: {carpeta.name}")

    if videos:
        c = api("POST", f"{IG_USER_ID}/media", media_type="REELS",
                video_url=url_publica(videos[0]), caption=texto)
        esperar_listo(c["id"])
    elif len(imagenes) == 1:
        c = api("POST", f"{IG_USER_ID}/media", image_url=url_publica(imagenes[0]), caption=texto)
        esperar_listo(c["id"])
    elif 2 <= len(imagenes) <= 10:
        hijos = []
        for img in imagenes:
            h = api("POST", f"{IG_USER_ID}/media", image_url=url_publica(img), is_carousel_item="true")
            esperar_listo(h["id"])
            hijos.append(h["id"])
        c = api("POST", f"{IG_USER_ID}/media", media_type="CAROUSEL",
                children=",".join(hijos), caption=texto)
        esperar_listo(c["id"])
    else:
        sys.exit(f"posts/{carpeta.name} necesita entre 1 y 10 imágenes .jpg, o un video .mp4.")

    pub = api("POST", f"{IG_USER_ID}/media_publish", creation_id=c["id"])
    print(f"Publicado. ID de Instagram: {pub['id']}")

    with PUBLICADOS.open("a", encoding="utf-8") as f:
        f.write(carpeta.name + "\n")


if __name__ == "__main__":
    main()
