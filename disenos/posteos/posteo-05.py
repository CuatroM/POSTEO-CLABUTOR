"""Posteo 5 — Agro: electrobombas de combustible y cuenta litros FEMA (muro, carrusel).
Solo productos con stock (export BaseLinker 11/11). Precio = costo + 35 % + envío (10 % del costo, mín. $20.000).
Los tanques de combustible quedaron afuera: sin stock."""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("gen", Path(__file__).parents[1] / "generar.py")
_g = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_g)
precio = _g.precio_envio_gratis

ID = "posteo-05-agro-electrobombas"
RUBRO = "Agro · Combustible"
ROJO = "#E10600"

# sku, volanta, título, nombre, costo, datos técnicos
PRODUCTOS = [
    ("69359811", "Kit surtidor 12 V", "Tu surtidor<br><em>en el campo</em>",
     "Electrobomba FEMA 12 V kit surtidor completo", 341578,
     ["60 L/min", "12 V a batería", "Con cuenta litros", "Manguera y pistola"]),
    ("69359918", "Kit surtidor 220 V", "Surtidor fijo<br><em>a 220 V</em>",
     "Electrobomba diésel 220 V kit surtidor completo", 470448,
     ["60 L/min", "220 V · 350 W", "Conexión 1\"", "Con cuenta litros"]),
    ("69359805", "Electrobomba 12 V", "80 litros<br><em>por minuto</em>",
     "Electrobomba FEMA 12 V para gasoil", 389809,
     ["80 L/min", "12 V a batería", "Conexión 1\"", "Uso continuo"]),
    ("69359806", "Kit para nafta 12 V", "Para nafta,<br><em>con pistola</em>",
     "Electrobomba FEMA 12 V para nafta, kit completo", 552922,
     ["57 L/min", "12 V a batería", "Caudalímetro", "Pistola automática"]),
    ("69359687", "Cuenta litros", "Controlá<br><em>cada litro</em>",
     "Cuenta litros FEMA de aluminio", 82799,
     ["Display 4/8 dígitos", "Conexión 1\"", "Cuerpo de aluminio", "Parcial y total"]),
]


def pesos(n):
    return "$" + f"{round(n):,}".replace(",", ".")


TEXTO = """
Abastecé tractores, camionetas, generadores y maquinaria sin ir a la estación de servicio. ⛽🚜

Electrobombas FEMA para combustible, a 12 V o 220 V, con o sin cuenta litros:

""" + "\n".join(f"• {n}: {pesos(precio(c))}" for _, _, _, n, c, _ in PRODUCTOS) + """

Envío gratis a todo el país.

Comprá en clabutor.com.ar o escribinos por WhatsApp:
Casa central: 351 227 2419 · Domingo F. Sarmiento 365 - Córdoba
Sucursal: 351 227 2420 · Blvd. de los Alemanes 5310 - Córdoba

#clabutor #agro #campo #combustible #gasoil #fema #cordoba
"""


def chips(datos):
    return "".join(
        f'<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:2px solid #E6E6E6">'
        f'<span style="width:12px;height:12px;background:{ROJO};flex:none"></span>'
        f'<span style="font-family:Titular;font-weight:700;font-size:28px;white-space:nowrap">{d}</span></div>' for d in datos)


def placa_producto(g, sku, volanta, titulo, nombre, costo, datos):
    foto = f'<img src="../../productos/recortes/{sku}.png" style="max-width:100%;max-height:440px;object-fit:contain">'
    return f'''
<div class="volanta">{volanta}</div>
<h1 style="font-size:92px;white-space:nowrap">{titulo}</h1>
<div style="display:grid;grid-template-columns:1fr 330px;gap:26px;margin-top:24px;height:470px;border-top:2px solid #111;padding-top:14px">
  <div style="display:flex;align-items:center;justify-content:center;min-height:0">{foto}</div>
  <div style="display:flex;flex-direction:column;justify-content:center">
    <div style="font-weight:700;font-size:18px;letter-spacing:3px;color:#8A8A8A;margin-bottom:4px">DATOS TÉCNICOS</div>
    {chips(datos)}
  </div>
</div>
<div style="font-family:Titular;font-weight:700;font-size:30px;margin-top:10px">{g.e(nombre)}</div>
<div style="font-weight:600;font-size:18px;color:#8A8A8A;letter-spacing:2px;margin-top:4px">COD. {sku}</div>
<div style="display:flex;align-items:center;gap:26px;margin-top:6px">
  <span style="font-family:Titular;font-weight:900;font-size:112px;line-height:.95;letter-spacing:-4px;color:{ROJO}">{pesos(precio(costo))}</span>
  <span style="background:#111;color:#fff;padding:12px 18px;font-family:Titular;font-weight:900;font-size:22px;letter-spacing:2px;line-height:1.15">ENVÍO<br>GRATIS</span>
</div>
'''


def placas(g):
    puntos = "".join(
        f'<div style="display:flex;align-items:center;gap:20px;padding:18px 0;border-bottom:2px solid #333">'
        f'<span style="width:14px;height:14px;background:{ROJO};flex:none"></span>'
        f'<span style="font-family:Titular;font-weight:700;font-size:36px">{t}</span></div>'
        for t in ["A 12 V (batería) o 220 V", "Hasta 80 litros por minuto", "Con o sin cuenta litros"])
    portada = f'''
<div class="volanta">Para el agro</div>
<h1 style="font-size:116px">Tu propio<br><em>surtidor</em></h1>
<p class="bajada" style="font-size:36px"><b>Abastecé tractores, camionetas, generadores<br>y maquinaria sin ir a la estación de servicio.</b></p>
<div style="margin-top:26px">{puntos}</div>
<div style="position:absolute;left:80px;right:80px;bottom:150px;background:{ROJO};color:#fff;padding:22px 30px;display:flex;justify-content:space-between;align-items:center">
  <span style="font-family:Titular;font-weight:900;font-size:40px;letter-spacing:1px">ENVÍO GRATIS A TODO EL PAÍS</span>
  <span style="font-family:Titular;font-weight:900;font-size:40px">&rarr;</span>
</div>
'''
    return [("oscura", portada)] + [("", placa_producto(g, *p)) for p in PRODUCTOS]
