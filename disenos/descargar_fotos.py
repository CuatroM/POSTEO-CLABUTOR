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
        ext = Path(url.split("?")[0]).suffix.lower() or ".jpg"
        destino = PRODUCTOS / f"{sku}{ext}"
        img = requests.get(url, headers=UA, timeout=60)
        img.raise_for_status()
        for viejo in PRODUCTOS.glob(f"{sku}.*"):
            viejo.unlink()
        destino.write_bytes(img.content)
        print(f"  OK {prod['name']} ({sitio}) -> {destino.name} [{len(img.content)//1024} KB]")
    if faltan:
        print("Sin foto:", ", ".join(faltan))
    (PRODUCTOS / "descarga.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
