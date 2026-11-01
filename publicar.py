"""
Publica en Instagram el próximo post pendiente de la carpeta posts/.

Cada post es una carpeta dentro de posts/ con:
  - una o varias imágenes .jpg  (1 = post simple, 2 a 10 = carrusel)
  - o un video .mp4             (se publica como Reel)
  - texto.txt                   (el texto del post, con hashtags)

Historias: si el nombre de la carpeta contiene "historia", cada imagen .jpg
(1080x1920) se publica como una historia, en orden alfabético (no lleva texto).

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

TOKEN = os.environ.get("IG_TOKEN", "").strip()
# Token de "inicio de sesión con Instagram" (IGAA...) o de "inicio de sesión con Facebook" (EAA...)
ES_FACEBOOK = TOKEN.startswith("EA")
API = "https://graph.facebook.com/v25.0" if ES_FACEBOOK else "https://graph.instagram.com/v25.0"
IG_USER_ID = os.environ.get("IG_USER_ID", "").strip()
if not TOKEN:
    sys.exit("ERROR: falta el secreto IG_TOKEN (o está vacío).")
print(f"Token: {len(TOKEN)} caracteres, empieza con '{TOKEN[:2]}'"
      + (" (TIENE ESPACIOS O COMILLAS)" if any(c in TOKEN for c in " \"'=") else ""))
if not IG_USER_ID.isdigit():
    sys.exit(f"ERROR: el secreto IG_USER_ID tiene que ser solo números (tiene {len(IG_USER_ID)} caracteres).")
REPO = os.environ.get("GITHUB_REPOSITORY", "CuatroM/POSTEO-CLABUTOR")
RAMA = os.environ.get("GITHUB_REF_NAME", "main")
CARPETA_FORZADA = os.environ.get("CARPETA", "").strip()

RAIZ = Path(__file__).parent
POSTS = RAIZ / "posts"
PUBLICADOS = RAIZ / "publicados.txt"
HOY = datetime.now(timezone(timedelta(hours=-3))).date()  # hora de Argentina


def api(metodo, ruta, salir=True, **params):
    params["access_token"] = TOKEN
    try:
        r = requests.request(metodo, f"{API}/{ruta}", params=params, timeout=60)
        datos = r.json()
    except Exception as e:
        sys.exit(f"ERROR: no se pudo conectar con Instagram ({e}).")
    if "error" in datos and not salir:
        return datos
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


def aviso(msg):
    # Se ve en el log y como anotación del workflow
    print(msg)
    print(f"::notice::{msg}")


def diagnostico_facebook():
    """Revisa el token de Facebook y devuelve los IDs de Instagram que puede usar."""
    candidatos = {}
    info = api("GET", "debug_token", salir=False, input_token=TOKEN).get("data", {})
    if info:
        aviso(f"Diag: tipo={info.get('type')} valido={info.get('is_valid')} "
              f"app={info.get('application')} vence={info.get('expires_at')} "
              f"permisos={','.join(info.get('scopes', []))}")
        for g in info.get("granular_scopes", []):
            if g.get("scope", "").startswith("instagram"):
                for t in g.get("target_ids", []):
                    candidatos.setdefault(t, "permiso " + g["scope"])
    else:
        aviso("Diag: no se pudo leer la información del token")
    yo = api("GET", "me", salir=False, fields="id,name")
    aviso(f"Diag: el token pertenece a: {yo.get('name')} ({yo.get('id')})" if "error" not in yo
          else f"Diag: me -> {yo['error'].get('message')}")
    pag = api("GET", "me", salir=False, fields="instagram_business_account{id,username}")
    if "instagram_business_account" in pag:
        ig = pag["instagram_business_account"]
        candidatos[ig["id"]] = f"@{ig.get('username')} (token de página)"
    for p in api("GET", "me/accounts", salir=False,
                 fields="name,instagram_business_account{id,username}").get("data", []):
        ig = p.get("instagram_business_account")
        aviso(f"Diag: página '{p.get('name')}' -> Instagram: {ig.get('username') if ig else 'NO VINCULADO'}")
        if ig:
            candidatos[ig["id"]] = f"@{ig.get('username')} (página {p.get('name')})"
    for i, origen in candidatos.items():
        aviso(f"Diag: cuenta de Instagram disponible: IG_USER_ID={i} -> {origen}")
    return list(candidatos)


def main():
    global IG_USER_ID
    candidatos = diagnostico_facebook() if ES_FACEBOOK else []
    cuenta = api("GET", IG_USER_ID, salir=False, fields="username")
    if "error" in cuenta and len(candidatos) == 1:
        aviso(f"El IG_USER_ID cargado no sirve; uso el que encontré: {candidatos[0]}")
        IG_USER_ID = candidatos[0]
        cuenta = api("GET", IG_USER_ID, salir=False, fields="username")
    if "error" in cuenta:
        aviso(f"ERROR: el IG_USER_ID no corresponde a una cuenta accesible: {cuenta['error'].get('message')}")
        sys.exit(1)
    aviso(f"Conectado a Instagram como @{cuenta.get('username')}")

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

    if "historia" in carpeta.name.lower():
        if not imagenes:
            sys.exit(f"posts/{carpeta.name} no tiene imágenes .jpg para las historias.")
        for img in imagenes:
            h = api("POST", f"{IG_USER_ID}/media", media_type="STORIES", image_url=url_publica(img))
            esperar_listo(h["id"])
            pub = api("POST", f"{IG_USER_ID}/media_publish", creation_id=h["id"])
            print(f"Historia {img.name} publicada. ID de Instagram: {pub['id']}")
            time.sleep(5)
        with PUBLICADOS.open("a", encoding="utf-8") as f:
            f.write(carpeta.name + "\n")
        return

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
