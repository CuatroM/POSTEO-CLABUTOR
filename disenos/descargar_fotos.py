"""
Descarga las fotos de productos por SKU desde clabutor.com.ar o femacba.com.ar
(API pública de WooCommerce) y las guarda en disenos/productos/<SKU>.<ext>.

Uso: python disenos/descargar_fotos.py            -> usa disenos/productos/pedido.txt
     python disenos/descargar_fotos.py SKU1 SKU2  -> esos SKU

pedido.txt: un SKU por línea; opcionalmente "SKU | texto de búsqueda" para cuando
el buscador no encuentra el código.
"""
import re
import sys
from pathlib import Path

import requests

AQUI = Path(__file__).parent
PRODUCTOS = AQUI / "productos"
SITIOS = ["https://clabutor.com.ar", "https://femacba.com.ar"]
UA = {"User-Agent": "Mozilla/5.0 (posteo-clabutor)"}


def buscar(sitio, termino):
    r = requests.get(f"{sitio}/wp-json/wc/store/v1/products",
                     params={"search": termino, "per_page": 50}, headers=UA, timeout=40)
    r.raise_for_status()
    return r.json()


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def encontrar(sku, consulta):
    if consulta.strip().lower() == "drive":     # "SKU | drive" = buscar directo en Drive
        return encontrar_drive(sku)
    for sitio in SITIOS:
        for termino in [sku] + ([consulta] if consulta else []):
            try:
                res = buscar(sitio, termino)
            except Exception as ex:  # noqa: BLE001
                print(f"  {sitio} '{termino}': error {ex}")
                continue
            exactos = [p for p in res if norm(p.get("sku")) == norm(sku)]
            elegido = exactos[0] if exactos else None
            if not elegido:
                print(f"  {sitio} '{termino}': {len(res)} resultados, ninguno con SKU {sku} "
                      f"({', '.join((p.get('sku') or '?') + ' ' + p['name'] for p in res[:5])})")
                continue
            imgs = elegido.get("images") or []
            if not imgs:
                print(f"  {sitio}: {elegido['name']} sin imagen")
                continue
            return sitio, elegido, imgs[0]["src"]
    return encontrar_html(sku, consulta) or encontrar_drive(sku)


# Último recurso: la carpeta pública de fotos FEMA en Google Drive (la misma que usa la
# publicación en Mercado Libre). Las fotos se llaman <SKU>.jpg (o <SKU>-1.jpg, etc.).
DRIVE_FOTOS = "1n-pnG6JIS5q1TBEWn3jS0BYY9I36xlra"
_DRIVE = None


def _drive_listar(fid, profundidad=4):
    import html as _h
    r = requests.get(f"https://drive.google.com/embeddedfolderview?id={fid}", headers=UA, timeout=60)
    r.raise_for_status()
    out = []
    for m in re.finditer(r'<div class="flip-entry" id="entry-([A-Za-z0-9_-]+)".*?'
                         r'<div class="flip-entry-title">(.*?)</div>', r.text, re.S):
        eid, nombre = m.group(1), _h.unescape(m.group(2)).strip()
        bloque = r.text[m.start():m.end() + 400]
        if "/folders/" in bloque or "drive/folders" in bloque:
            if profundidad > 0:
                out += _drive_listar(eid, profundidad - 1)
        else:
            out.append((nombre, eid))
    return out


def encontrar_drive(sku):
    global _DRIVE
    if _DRIVE is None:
        try:
            _DRIVE = _drive_listar(DRIVE_FOTOS)
            print(f"  Drive: {len(_DRIVE)} archivos en la carpeta de fotos")
        except Exception as ex:  # noqa: BLE001
            print(f"  Drive: error al listar ({ex})")
            _DRIVE = []
    base = sku.split("-")[0]
    candidatos = sorted(n for n in _DRIVE if re.match(re.escape(sku) + r"([ ._-]|$)", n[0], re.I)) or \
        sorted(n for n in _DRIVE if re.match(re.escape(base) + r"([ ._-]|$)", n[0], re.I))
    candidatos = [c for c in candidatos if c[0].lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
    if not candidatos:
        print(f"  Drive: no hay foto para {sku}")
        parecidos = [n for n, _ in _DRIVE if n[:6] == base[:6]][:15]
        if parecidos:
            print(f"  Drive: nombres parecidos: {', '.join(parecidos)}")
        return None
    print(f"  Drive: candidatos {[c[0] for c in candidatos]}")
    # Preferir la foto del equipo: SKU.jpg, luego SKU-1.jpg..., y al final las de accesorios (ARNES, KIT...)
    def orden(c):
        resto = Path(c[0]).stem[len(sku):].lstrip(" ._-").upper()
        if resto == "":
            return (0, c[0])
        if resto.isdigit():
            return (1, c[0])
        return (2, c[0])
    candidatos.sort(key=orden)
    nombre, fid = candidatos[0]
    print(f"  Drive: {nombre}")
    ext = Path(nombre).suffix.lower()
    return "drive", {"name": nombre}, f"https://drive.usercontent.google.com/download?id={fid}&export=download#{ext}"


# Respaldo para tiendas sin API (femacba.com.ar corre en TiendaQuick):
# busca en el HTML las páginas de producto y toma la que muestre el SKU.
PAGINAS_HTML = [
    "https://www.femacba.com.ar/?s={q}",
    "https://www.femacba.com.ar/construccion/hormigoneras-carretillas-baldes",
    "https://www.femacba.com.ar/compresores/compresores-1",
    "https://www.femacba.com.ar/compresores",
    "https://www.femacba.com.ar/motores/motores-a-explosion",
    "https://www.femacba.com.ar/electrobombas/electrobombas-centrifugas-y-perifericas",
    "https://www.femacba.com.ar/jardineria/canos-mangueras-de-riego",
    "https://www.femacba.com.ar/listado-productos.htm",
] + [f"https://www.femacba.com.ar/compresores/compresores-1?{k}={n}" for k in ("page", "pagina", "p") for n in range(2, 6)]


def _get(url):
    r = requests.get(url, headers=UA, timeout=40)
    r.raise_for_status()
    return r.text


def _og_image(html_txt):
    m = (re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', html_txt)
         or re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', html_txt))
    return m.group(1) if m else None


def _abs(u):
    if u.startswith("//"):
        return "https:" + u
    if u.startswith("/"):
        return "https://www.femacba.com.ar" + u
    return u


def _desde_listado(sku, txt):
    """En un listado que muestra el SKU, toma la foto y el link más cercanos al código."""
    # 0) una imagen cuyo nombre lleva el SKU (en TiendaQuick: .../thumb_03_<SKU>-1.jpg.webp -> versión grande)
    directas = re.findall(r'["\'(]([^"\'()\s]*?' + re.escape(sku) + r'[^"\'()\s]*?\.(?:jpe?g|png|webp))', txt, re.I)
    if directas:
        img = _abs(re.sub(r"thumb_\d+_", "", directas[0]))
        print(f"  imagen con el SKU en el nombre -> {img}")
        return "femacba (listado)", {"name": sku}, img
    i = txt.find(sku)
    ventana_antes, ventana_despues = txt[max(0, i - 4000):i], txt[i:i + 1500]
    imgs = [m for m in re.findall(r'<img[^>]+(?:data-src|src)=["\']([^"\']+)', ventana_antes)
            if "logo" not in m.lower() and not m.endswith(".svg")]
    hrefs = [m for m in re.findall(r'href=["\']([^"\'#]+)', ventana_antes + ventana_despues)
             if m.count("/") >= 2]
    print(f"  listado: imgs cerca={imgs[-3:]} links cerca={hrefs[-4:]}")
    # 1) página del producto (link más cercano antes del código)
    for h in reversed(hrefs[:len(re.findall(r'href=', ventana_antes))]):
        h = _abs(h)
        if h in PAGINAS_HTML or "?" in h:
            continue
        try:
            img = _og_image(_get(h))
        except Exception:  # noqa: BLE001
            continue
        if img and "logo" not in img.lower():
            print(f"  producto {h} -> {img}")
            return "femacba (html)", {"name": h}, _abs(img)
        break
    # 2) la imagen del listado, en tamaño grande si la URL lo permite
    if imgs:
        img = _abs(imgs[-1])
        print(f"  imagen del listado -> {img}")
        return "femacba (listado)", {"name": sku}, img
    return None


def encontrar_html(sku, consulta):
    vistos, listados = set(), set()
    for plantilla in PAGINAS_HTML:
        for q in [sku] + ([consulta] if consulta else []):
            url = plantilla.format(q=requests.utils.quote(q))
            if url in listados:
                continue
            listados.add(url)
            try:
                txt = _get(url)
            except Exception as ex:  # noqa: BLE001
                print(f"  {url}: error {ex}")
                continue
            links = []
            for href in re.findall(r'href=["\']([^"\'#]+)', txt):
                if href.startswith("/"):
                    href = "https://www.femacba.com.ar" + href
                if "femacba.com.ar" in href and href.count("/") >= 4 and href not in links:
                    links.append(href)
            # primero los links que mencionan el término
            palabras = [norm(w) for w in (consulta or "").split() if len(w) >= 4]
            links.sort(key=lambda h: -(10 * (sku in h) + sum(w[:6] in norm(h) for w in palabras)))
            print(f"  {url}: {len(links)} links; SKU en la página: {sku in txt}")
            for pag_url in re.findall(r'href=["\']([^"\']*(?:[?&](?:page|pagina|pag|p)=\d+)[^"\']*)', txt)[:8]:
                pag_url = _abs(pag_url.replace("&amp;", "&"))
                if pag_url not in listados and pag_url.startswith("https://www.femacba.com.ar"):
                    listados.add(pag_url)
                    try:
                        ptxt = _get(pag_url)
                    except Exception:  # noqa: BLE001
                        continue
                    if sku in ptxt:
                        print(f"  encontrado en {pag_url}")
                        hallado = _desde_listado(sku, ptxt)
                        if hallado:
                            return hallado
            if sku in txt:
                hallado = _desde_listado(sku, txt)
                if hallado:
                    return hallado
            for h in links[:120]:
                if h in vistos:
                    continue
                vistos.add(h)
                try:
                    pag = _get(h)
                except Exception:  # noqa: BLE001
                    continue
                if sku in pag and h not in PAGINAS_HTML:
                    img = _og_image(pag)
                    if img and "logo" in img.lower():
                        hallado = _desde_listado(sku, pag)
                        if hallado:
                            return hallado
                        continue
                    print(f"  coincide {h} -> {img}")
                    if img:
                        return "femacba (html)", {"name": h}, img
    return None


LOG = []
_print = print


def print(*a):  # noqa: A001
    LOG.append(" ".join(str(x) for x in a))
    _print(*a)


def main():
    if len(sys.argv) > 1:
        pedido = [(s, "") for s in sys.argv[1:]]
    else:
        pedido = []
        for linea in (PRODUCTOS / "pedido.txt").read_text(encoding="utf-8").splitlines():
            linea = linea.strip()
            if linea and not linea.startswith("#"):
                sku, _, q = linea.partition("|")
                pedido.append((sku.strip(), q.strip()))
    faltan = []
    for sku, q in pedido:
        print(f"{sku}:")
        hallado = encontrar(sku, q)
        if not hallado:
            faltan.append(sku)
            print("  NO ENCONTRADO")
            continue
        sitio, prod, url = hallado
        ext = (url.split("#")[1] if "#" in url else Path(url.split("?")[0]).suffix.lower()) or ".jpg"
        destino = PRODUCTOS / f"{sku}{ext}"
        img = requests.get(url.split("#")[0], headers=UA, timeout=120)
        img.raise_for_status()
        for viejo in PRODUCTOS.glob(f"{sku}.*"):
            viejo.unlink()
        destino.write_bytes(img.content)
        print(f"  OK {prod['name']} ({sitio}) -> {destino.name} [{len(img.content)//1024} KB]")
        pr = prod.get("prices") or {}
        if pr:
            div = 10 ** int(pr.get("currency_minor_unit", 0) or 0)
            val = lambda k: (int(pr[k]) / div) if pr.get(k) else None  # noqa: E731
            print(f"  PRECIOS {sku}: precio={val('price')} lista={val('regular_price')} oferta={val('sale_price')} "
                  f"link={prod.get('permalink', '')}")
    if faltan:
        print("Sin foto:", ", ".join(faltan))
    (PRODUCTOS / "descarga.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
