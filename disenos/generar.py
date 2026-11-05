"""
Arma las placas de un posteo de Clabutor como HTML (estilo fijo en estilo.css).
Uso: python3 disenos/generar.py disenos/posteos/posteo-01.py   -> crea disenos/salida/<id>/placa-N.html
Después render.js las convierte en JPG 1080x1350.
"""
import html
import importlib.util
import sys
from pathlib import Path

AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI / "assets"))
import mapa  # noqa: E402

PRODUCTOS = AQUI / "productos"


def e(t):
    return html.escape(t)


# ---------- Ilustraciones ----------
def svg_tornillo(alto=820):
    """Tornillo de cabeza hexagonal, negro con brillos, vista lateral."""
    w_vara, y0, y1 = 120, 150, 700
    hilos = []
    izq, der = [], []
    paso = 26
    y = y0
    i = 0
    while y < y1:
        izq.append((-w_vara / 2 - (16 if i % 2 == 0 else 0), y))
        der.append((w_vara / 2 + (16 if i % 2 == 1 else 0), y))
        if i % 2 == 0:
            hilos.append(f'<line x1="{-w_vara/2-10}" y1="{y}" x2="{w_vara/2+10}" y2="{y+paso}" stroke="#4a4a4a" stroke-width="5"/>')
        y += paso / 2
        i += 1
    contorno = [(-w_vara / 2, y0)] + izq + [(0, y1 + 70)] + list(reversed(der)) + [(w_vara / 2, y0)]
    pts = " ".join(f"{x:.0f},{yy:.0f}" for x, yy in contorno)
    return f'''<svg viewBox="-160 -10 320 800" height="{alto}" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#050505"/><stop offset=".45" stop-color="#3a3a3a"/><stop offset=".6" stop-color="#1a1a1a"/><stop offset="1" stop-color="#000"/></linearGradient></defs>
  <rect x="-130" y="118" width="260" height="22" rx="4" fill="#1d1d1d"/>
  <path d="M-115 20 L115 20 L125 40 L125 110 L115 120 L-115 120 L-125 110 L-125 40 Z" fill="url(#g)"/>
  <rect x="-38" y="20" width="76" height="100" fill="#4a4a4a" opacity=".55"/>
  <line x1="-38" y1="20" x2="-38" y2="120" stroke="#000" stroke-width="3"/><line x1="38" y1="20" x2="38" y2="120" stroke="#000" stroke-width="3"/>
  <polygon points="{pts}" fill="url(#g)"/>
  {"".join(hilos)}
  <rect x="-14" y="150" width="12" height="540" fill="#fff" opacity=".18"/>
</svg>'''


ICONOS = {
    "Bulones": '<rect x="30" y="8" width="40" height="20" fill="none"/><rect x="40" y="28" width="20" height="64"/><path d="M38 44h24M38 56h24M38 68h24M38 80h24" class="r"/>',
    "Tornillos": '<path d="M24 12h52L58 30H42Z"/><path d="M42 30h16v46L50 94l-8-18Z"/><path d="M40 42l20 6M40 54l20 6M40 66l20 6" class="r"/>',
    "Tuercas": '<path d="M50 10l35 20v40L50 90 15 70V30Z"/><circle cx="50" cy="50" r="17" class="r"/>',
    "Arandelas": '<circle cx="50" cy="50" r="38"/><circle cx="50" cy="50" r="16" class="r"/>',
    "Tacos": '<path d="M36 10h28v66L50 92 36 76Z"/><path d="M36 26h28M36 40h28M36 54h28M36 68h28" class="r"/>',
    "Varillas": '<rect x="44" y="6" width="12" height="88"/><path d="M40 18l20 6M40 34l20 6M40 50l20 6M40 66l20 6M40 82l20 6" class="r"/>',
}


def svg_icono(nombre, tam=86):
    return (f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" xmlns="http://www.w3.org/2000/svg">'
            f'<style>*{{fill:none;stroke:#111;stroke-width:6;stroke-linejoin:round}}.r{{stroke:#E10600}}</style>'
            f'{ICONOS[nombre]}</svg>')


def svg_mapa(ancho, marcas):
    w, h = mapa.tamano(ancho)
    pts = ""
    for lon, lat, txt in marcas:
        x, y = mapa.proyectar(lon, lat, ancho)
        pts += (f'<circle cx="{x:.0f}" cy="{y:.0f}" r="44" fill="#E10600" opacity=".18"/>'
                f'<circle cx="{x:.0f}" cy="{y:.0f}" r="18" fill="#E10600"/>'
                f'<text x="{x+34:.0f}" y="{y+12:.0f}" font-family="Titular" font-weight="900" font-size="36" fill="#111">{e(txt)}</text>')
    return (f'<svg viewBox="-10 -10 {w+180:.0f} {h+20:.0f}" width="{w+190:.0f}" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="{mapa.path(ancho)}" fill="#F2F2F2" stroke="#111" stroke-width="4" stroke-linejoin="round"/>{pts}</svg>')


# ---------- Piezas ----------
FOTOS = AQUI / "fotos"


def foto_lugar(nombre, estilo="", filtro="", falta="FOTO"):
    """Foto de disenos/fotos/<nombre>.jpg; si no está, un recuadro que avisa qué foto falta."""
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        f = FOTOS / f"{nombre}{ext}"
        if f.exists():
            return f'<div class="foto-lugar" style="{estilo}"><img src="../../fotos/{f.name}" style="filter:{filtro}"></div>'
    return f'<div class="foto-lugar" style="{estilo}"><div class="falta">{e(falta)}</div></div>'


def pin(texto, estilo=""):
    icono = ('<svg width="30" height="40" viewBox="0 0 30 40"><path d="M15 0C6.7 0 0 6.7 0 15c0 11 15 25 15 25s15-14 15-25C30 6.7 23.3 0 15 0z" fill="#E10600"/>'
             '<circle cx="15" cy="15" r="6" fill="#fff"/></svg>')
    return f'<div class="pin" style="{estilo}">{icono}{e(texto)}</div>'
def foto_producto(sku):
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        f = PRODUCTOS / f"{sku}{ext}"
        if f.exists():
            return f'<img src="../../productos/{f.name}">'
    return f'<div class="sinfoto">FOTO PRODUCTO<span>{e(sku)}</span></div>'


def tarjeta(p, estilo=""):
    return (f'<div class="producto" style="{estilo}"><div class="foto">{foto_producto(p["sku"])}</div>'
            f'<div class="datos"><div class="nombre">{e(p["nombre"])}</div><div class="sku">COD. {e(p["sku"])}</div></div></div>')


def marco(cuerpo, n, total, rubro, fondo=""):
    # Historias de producto (marcadas con MARCA_PRODUCTO) van sin barras de progreso:
    # se pueden publicar en cualquier orden. Las informativas sí las llevan.
    barras = "" if not n else "".join(f'<span class="{"activa" if i <= n else ""}"></span>' for i in range(1, total + 1))
    return f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../estilo.css"></head>
<body><div class="placa {fondo}">
<div class="encabezado"><div class="marca"><i></i>CLABUTOR</div><div class="rubro">{e(rubro)}</div></div>
{cuerpo}
<div class="pie"><div class="usuario">www.clabutor.com.ar</div><div class="progreso"><div class="barras">{barras}</div>{n:02d} / {total:02d}</div></div>
</div></body></html>'''


MARCA_PRODUCTO = "<!--producto-->"
CINTAS = {"cyber": 'CYBERMONDAY <b>·</b> 2·3·4 NOV'}


def marco_historia(cuerpo, n, total, fondo="azul", cinta="cyber"):
    """Historia 1080x1920: cinta de campaña arriba, marca, cuerpo y web abajo a la izquierda."""
    # Historias de producto (marcadas con MARCA_PRODUCTO) van sin barras de progreso:
    # se pueden publicar en cualquier orden. Las informativas sí las llevan.
    barras = "" if not n else "".join(f'<span class="{"activa" if i <= n else ""}"></span>' for i in range(1, total + 1))
    tira = f'<div class="cinta">{CINTAS[cinta]}</div>' if cinta else ""
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="tamano" content="1080x1920">
<link rel="stylesheet" href="../../historia.css"></head>
<body><div class="historia {fondo}{"" if cinta else " sin-cinta"}">
{tira}
<div class="marca-h"><i></i>CLABUTOR</div>
<div class="cuerpo" style="overflow:hidden">{cuerpo}</div>
<div class="pie-h"><div class="web">www.clabutor.com.ar</div><div class="barras">{barras}</div></div>
</div></body></html>'''


def generar(modulo):
    spec = importlib.util.spec_from_file_location("posteo", modulo)
    post = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(post)
    salida = AQUI / "salida" / post.ID
    salida.mkdir(parents=True, exist_ok=True)
    placas = post.placas(sys.modules[__name__])
    historia = getattr(post, "FORMATO", "posteo") == "historia"
    informativas = [c for c in placas if historia and MARCA_PRODUCTO not in c[1]]
    k = 0
    for i, cuerpo in enumerate(placas, 1):
        if historia:  # cada placa es (fondo, html)
            fondo, html_cuerpo = cuerpo
            if MARCA_PRODUCTO in html_cuerpo:
                n = 0
            else:
                k += 1
                n = k
            pagina = marco_historia(html_cuerpo, n, len(informativas), fondo, getattr(post, "CINTA", "cyber"))
        else:
            fondo, cuerpo = cuerpo if isinstance(cuerpo, tuple) else ("", cuerpo)
            pagina = marco(cuerpo, i, len(placas), post.RUBRO, fondo)
        (salida / f"placa-{i}.html").write_text(pagina, encoding="utf-8")
    (salida / "texto.txt").write_text(post.TEXTO.strip() + "\n", encoding="utf-8")
    print(salida)


if __name__ == "__main__":
    generar(sys.argv[1])
