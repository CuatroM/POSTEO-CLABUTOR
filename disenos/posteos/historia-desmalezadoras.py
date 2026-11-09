"""Historias — Bordeadoras y desmalezadoras FEMA con stock (export BaseLinker 09/11).
Precio = costo informado por la sincronización (INVENTARIO COMPLETO FEMA 2026 MATIAS, grupo 65271)
+ 35 % + envío (10 % del costo, mínimo $20.000), redondeado al peso. Envío gratis a todo el país. Colores Clabutor (no es campaña).
Historias de producto sin barras; cada una indica el uso: hogar o profesional."""

import importlib.util
from pathlib import Path

ID = "historia-desmalezadoras"
FORMATO = "historia"
CINTA = None
RUBRO = ""
TEXTO = ""
MARGEN = 1.35          # 35 % sobre el costo
ENVIO_PCT = 0.10       # envío: 10 % del costo...
ENVIO_MIN = 20000      # ...con un mínimo de $20.000


def precio(costo):
    return round(costo * MARGEN + max(costo * ENVIO_PCT, ENVIO_MIN))
ROJO = "#E10600"

_spec = importlib.util.spec_from_file_location("cyber_c", Path(__file__).with_name("historia-cyber-c.py"))
_c = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c)

# sku, nombre, costo BaseLinker, uso, título comercial
EQUIPOS = [
    ("69382600", "Bordeadora Castel Garden 500 W 30 cm", 71496.07, "PARA EL HOGAR",
     "Bordes prolijos<br><em>sin esfuerzo</em>"),
    ("69382620", "Bordeadora Castel Garden 700 W 28 cm", 74900.67, "PARA EL HOGAR",
     "Más potencia<br><em>para tu patio</em>"),
    ("69372050", "Desmalezadora Fema BC260 26 cc curva", 114920, "HOGAR Y QUINTAS",
     "Liviana<br><em>y a nafta</em>"),
    ("69372070", "Desmalezadora Fema 415 43 cc", 147097.6, "USO PROFESIONAL",
     "Para terrenos<br><em>grandes</em>"),
    ("69372075", "Desmalezadora Fema 520 52 cc", 137904, "USO PROFESIONAL",
     "Máxima fuerza<br><em>contra la maleza</em>"),
]

GUIA = [
    ("¿Querés emprolijar el césped del patio?", "Bordeadora eléctrica", "HOGAR"),
    ("¿Pasto alto en la quinta o en un terreno chico?", "Desmalezadora 26 cc", "HOGAR"),
    ("¿Malezas, terrenos grandes o campo?", "Desmalezadora 43 a 52 cc", "PROFESIONAL"),
]


def camion(tam=60):
    return (f'<svg width="{tam}" height="{int(tam*.7)}" viewBox="0 0 100 70"><path d="M4 8h54v40H4ZM58 22h20l16 16v10H58Z" fill="none" '
            f'stroke="#fff" stroke-width="8" stroke-linejoin="round"/><circle cx="22" cy="56" r="9" fill="#fff"/><circle cx="76" cy="56" r="9" fill="#fff"/></svg>')


def placas(g):
    filas = "".join(
        f'<div style="padding:34px 0;border-bottom:3px solid #111">'
        f'<div style="display:flex;justify-content:space-between;align-items:center;gap:16px">'
        f'<span style="font-family:Titular;font-weight:700;font-size:36px;line-height:1.12">{uso}</span>'
        f'<span style="font-family:Titular;font-weight:900;font-size:22px;letter-spacing:3px;color:#fff;background:{"#111" if tag == "HOGAR" else ROJO};padding:6px 12px;white-space:nowrap">{tag}</span></div>'
        f'<div style="font-weight:600;font-size:34px;color:#555;margin-top:10px">&rarr; Te sirve: <b style="font-family:Titular;font-weight:900;font-size:40px;color:{ROJO}">{equipo}</b></div></div>'
        for uso, equipo, tag in GUIA)
    info = f'''
<div class="pildora"><i></i>JARDÍN</div>
<h1 style="font-size:116px;margin-top:26px">¿Qué estás<br><em>necesitando?</em></h1>
<p class="bajada" style="font-size:40px">Cada jardín pide su herramienta.<br><b>Encontrá la tuya según tu situación.</b></p>
<div style="margin-top:40px">{filas}</div>
<div style="display:flex;align-items:center;gap:22px;background:{ROJO};color:#fff;padding:26px 30px;margin-top:60px">
  {camion(76)}<span style="font-family:Titular;font-weight:900;font-size:44px;letter-spacing:2px">ENVÍO GRATIS A TODO EL PAÍS</span>
</div>
'''
    salida = [("blanca colores-marca", info)]
    for sku, nombre, costo, uso, titulo in EQUIPOS:
        if not (g.AQUI / "productos" / "recortes" / f"{sku}.png").exists():
            print(f"Sin foto: {sku}")
            continue
        html = _c.placa_oferta(g, sku, nombre, None, precio(costo), titulo, True)
        salida.append(("blanca colores-marca", html.replace("OFERTA CYBER", uso)))
    return salida
