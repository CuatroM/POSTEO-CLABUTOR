"""Historias — Compresores, de chico a grande (solo con stock en BaseLinker al 05/11).
Precio = costo informado por la sincronización (INVENTARIO COMPLETO FEMA 2026 MATIAS, grupo 65271)
+ 40 %, redondeado al peso. Envío gratis a todo el país. Historias de producto sin barras."""

import importlib.util
from pathlib import Path

ID = "historia-compresores"
FORMATO = "historia"
CINTA = None
RUBRO = ""
TEXTO = ""
MARGEN = 1.40
NARANJA = "#FF6A00"

_spec = importlib.util.spec_from_file_location("cyber_c", Path(__file__).with_name("historia-cyber-c.py"))
_c = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c)

# sku, nombre, costo BaseLinker, título comercial
COMPRESORES = [
    ("69370100", "Compresor Duca Silen 3/4 HP 6 L", 186700.8, "Silencioso<br><em>y portátil</em>"),
    ("69370106", "Compresor Duca Silen 1 HP 24 L con ruedas", 193065.6, "Silencioso<br><em>para tu casa</em>"),
    ("69370208-10", "Compresor Fema 2,5 HP 50 L + kit 10 piezas", 211679.72, "Con kit,<br><em>listo para usar</em>"),
    ("69370024", "Compresor Duca W 3 HP 100 L axial", 378705.6, "Más aire<br><em>para tu taller</em>"),
    ("69370211", "Compresor Fema 2,5 HP 120 L con ruedas", 328962.92, "El compresor<br><em>que rinde todo</em>"),
    ("69370029", "Compresor Duca Pro 3 HP 180 L 220 V", 723465.6, "Aire de sobra<br><em>para trabajar</em>"),
    ("69370310", "Compresor Fema 5532 a nafta 5,5 HP 32 L", 754679.64, "Aire donde<br><em>no llega la luz</em>"),
    ("69370225", "Compresor Fema a correa 5,5 HP 330 L 380 V", 1357470.4, "Potencia<br><em>industrial</em>"),
    ("69370226", "Compresor Fema a correa 5,5 HP 500 L 380 V", 1829880, "Gran reserva<br><em>de aire</em>"),
    ("69370245", "Compresor Fema a correa 10 HP 500 L 380 V", 2081996.8, "El más grande<br><em>para tu industria</em>"),
]

GUIA = [
    ("Inflar, soplar y pintar en casa", "6 a 50 L"),
    ("Taller y herramientas neumáticas", "100 a 180 L"),
    ("Obra sin luz eléctrica", "a nafta"),
    ("Uso profesional e industrial", "330 a 500 L"),
]


def camion(tam=60):
    return (f'<svg width="{tam}" height="{int(tam*.7)}" viewBox="0 0 100 70"><path d="M4 8h54v40H4ZM58 22h20l16 16v10H58Z" fill="none" '
            f'stroke="#fff" stroke-width="8" stroke-linejoin="round"/><circle cx="22" cy="56" r="9" fill="#fff"/><circle cx="76" cy="56" r="9" fill="#fff"/></svg>')


def placas(g):
    filas = "".join(
        f'<div style="display:flex;align-items:center;justify-content:space-between;gap:20px;padding:24px 0;border-bottom:3px solid #23406B">'
        f'<span style="font-family:Titular;font-weight:700;font-size:40px;line-height:1.1">{uso}</span>'
        f'<span style="font-family:Titular;font-weight:900;font-size:44px;color:{NARANJA};white-space:nowrap">{rango}</span></div>'
        for uso, rango in GUIA)
    info = f'''
<div class="pildora"><i></i>COMPRESORES</div>
<h1 style="font-size:124px;margin-top:26px">¿Qué compresor<br><em>necesitás?</em></h1>
<p class="bajada" style="font-size:42px">Elegí según el trabajo que hacés.<br><b>Tenemos desde 6 hasta 500 litros.</b></p>
<div style="margin-top:40px">{filas}</div>
<div style="display:flex;align-items:center;gap:22px;background:{NARANJA};color:#fff;padding:24px 30px;margin-top:50px">
  {camion(76)}<span style="font-family:Titular;font-weight:900;font-size:44px;letter-spacing:2px">ENVÍO GRATIS A TODO EL PAÍS</span>
</div>
'''
    salida = [("azul", info)]
    for sku, nombre, costo, titulo in COMPRESORES:
        if not (g.AQUI / "productos" / "recortes" / f"{sku}.png").exists():
            print(f"Sin foto: {sku}")
            continue
        html = _c.placa_oferta(g, sku, nombre, None, round(costo * MARGEN), titulo, True)
        salida.append(("azul", html.replace("OFERTA CYBER", "COMPRESORES")))
    return salida
