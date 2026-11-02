"""
Recorta el fondo blanco de las fotos de producto (para mostrarlas "recortadas" sobre un fondo liso).
Uso: python disenos/recortar.py SKU [SKU ...]  -> disenos/productos/recortes/<SKU>.png
Quita solo el blanco conectado con los bordes, así no se borran partes blancas del producto.
"""
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

PRODUCTOS = Path(__file__).parent / "productos"
SALIDA = PRODUCTOS / "recortes"


def recortar(sku, tol=232):
    f = next((PRODUCTOS / f"{sku}{e}" for e in (".png", ".jpg", ".jpeg", ".webp") if (PRODUCTOS / f"{sku}{e}").exists()), None)
    if not f:
        print(f"{sku}: sin foto")
        return
    im = Image.open(f).convert("RGBA")
    fondo = Image.new("RGBA", im.size, (255, 255, 255, 255))
    fondo.paste(im, mask=im.split()[3])           # transparencias -> blanco
    rgb = fondo.convert("RGB")
    claro = rgb.convert("L").point(lambda p: 255 if p >= tol else 0)
    # también exige poca saturación (blanco/gris muy claro)
    sat = ImageChops.subtract(rgb.convert("HSV").split()[1], Image.new("L", rgb.size, 18)).point(lambda p: 255 if p == 0 else 0)
    candidato = ImageChops.multiply(claro, sat)
    marca = candidato.copy()
    w, h = marca.size
    for x in range(0, w, 4):
        for y in (0, h - 1):
            if marca.getpixel((x, y)) == 255:
                ImageDraw.floodfill(marca, (x, y), 128)
    for y in range(0, h, 4):
        for x in (0, w - 1):
            if marca.getpixel((x, y)) == 255:
                ImageDraw.floodfill(marca, (x, y), 128)
    alfa = marca.point(lambda p: 0 if p == 128 else 255).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    out = rgb.convert("RGBA")
    out.putalpha(alfa)
    out = out.crop(alfa.point(lambda p: 255 if p > 20 else 0).getbbox())
    SALIDA.mkdir(exist_ok=True)
    out.save(SALIDA / f"{sku}.png")
    print(f"{sku}: {out.size}")


if __name__ == "__main__":
    for s in sys.argv[1:]:
        recortar(s)
