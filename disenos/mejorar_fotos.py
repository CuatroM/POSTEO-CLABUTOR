"""
Mejora la calidad de las fotos (Real-ESRGAN x4) que se suben a disenos/fotos/ con el
nombre <nombre>-original.<ext>. Deja disenos/fotos/<nombre>.jpg (ancho máx. 2400 px).
Uso: python disenos/mejorar_fotos.py   (lo corre GitHub al subir una foto nueva)
"""
import sys
from pathlib import Path

import numpy as np
import torch
from PIL import Image, ImageFilter
from spandrel import ModelLoader

FOTOS = Path(__file__).parent / "fotos"
MODELO = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("RealESRGAN_x4plus.pth")


def tiles(modelo, img, tam=256, borde=16):
    """Procesa por partes para no agotar memoria."""
    _, _, h, w = img.shape
    esc = modelo.scale
    salida = torch.zeros((1, 3, h * esc, w * esc))
    for y in range(0, h, tam):
        for x in range(0, w, tam):
            y0, x0 = max(0, y - borde), max(0, x - borde)
            y1, x1 = min(h, y + tam + borde), min(w, x + tam + borde)
            with torch.no_grad():
                out = modelo(img[:, :, y0:y1, x0:x1])
            yy, xx = (y - y0) * esc, (x - x0) * esc
            hh, ww = (min(h, y + tam) - y) * esc, (min(w, x + tam) - x) * esc
            salida[:, :, y * esc:y * esc + hh, x * esc:x * esc + ww] = out[:, :, yy:yy + hh, xx:xx + ww]
    return salida


def main():
    modelo = ModelLoader().load_from_file(str(MODELO)).eval()
    for f in sorted(FOTOS.glob("*-original.*")):
        destino = FOTOS / (f.stem.replace("-original", "") + ".jpg")
        if destino.exists() and destino.stat().st_mtime > f.stat().st_mtime:
            continue
        im = Image.open(f).convert("RGB")
        t = torch.from_numpy(np.asarray(im)).permute(2, 0, 1).float().div(255).unsqueeze(0)
        out = tiles(modelo, t).clamp(0, 1)[0].permute(1, 2, 0).mul(255).round().byte().numpy()
        res = Image.fromarray(out)
        if res.width > 2400:
            res = res.resize((2400, round(res.height * 2400 / res.width)), Image.LANCZOS)
        res = res.filter(ImageFilter.UnsharpMask(radius=1.2, percent=40, threshold=2))
        res.save(destino, quality=94)
        print(f"{f.name} {im.size} -> {destino.name} {res.size}")


if __name__ == "__main__":
    main()
