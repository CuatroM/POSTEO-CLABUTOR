"""Posteo 1 — "Al mundo le falta un tornillo" (contenido tal cual MARKETING PRODUCTOS CONTENIDO)."""

ID = "posteo-01-al-mundo-le-falta-un-tornillo"
RUBRO = "Bulonería · Herramientas"

TEXTO = """
Desde un tornillo hasta una hormigonera: más de 10.000 productos para obra, taller, industria y hogar. Comprá en (WEB), escribinos al (WHATSAPP) o visitanos en (DIRECCIÓN). #bulonería #ferreteria #cordoba #herramientas #construccion
"""

P2 = [
    {"sku": "15108032TELEST", "nombre": "Autoperforante Tel alas 8×1¼\""},
    {"sku": "104070008", "nombre": "Taco Fischer SX 8×40"},
]
P3 = [
    {"sku": "69510063", "nombre": "Hormigonera FEMA 400 L"},
    {"sku": "KHE2445", "nombre": "Martillo combinado Metabo"},
    {"sku": "GE3460", "nombre": "Generador Gamma 2500"},
]


def placas(g):
    p1 = f'''
<h1 style="font-size:140px;margin-top:60px">Al mundo<br>le falta<br>un <em>tornillo…</em></h1>
<div style="position:absolute;right:40px;bottom:140px;width:450px;height:450px;border-radius:50%;background:#E10600"></div>
<div style="position:absolute;right:150px;bottom:70px;transform:rotate(32deg);transform-origin:center">{g.svg_tornillo(600)}</div>
<div style="position:absolute;left:80px;bottom:160px;font-family:Titular;font-weight:900;font-size:74px;line-height:.95;letter-spacing:-2px">…y <span style="color:#E10600">Clabutor</span><br>lo tiene.</div>
'''

    iconos = "".join(
        f'<div style="background:#F2F2F2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px">'
        f'{g.svg_icono(n, 74)}<span style="font-weight:700;font-size:19px;letter-spacing:1px;text-transform:uppercase">{n}</span></div>'
        for n in g.ICONOS)
    p2 = f'''
<div class="volanta">Bulonería</div>
<h1 style="font-size:112px">Desde el<br>tornillo<br><em>más chico</em></h1>
<p class="bajada" style="font-size:32px">Bulones, tornillos, tuercas, arandelas, tacos y varillas. <b>Métricos, pulgadas, inoxidable y grado 8.8.</b></p>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:10px;height:150px;margin-top:34px">{iconos}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;height:300px;margin-top:20px">{g.tarjeta(P2[0])}{g.tarjeta(P2[1])}</div>
'''

    p3 = f'''
<div class="volanta">Herramientas y maquinaria</div>
<h1 style="font-size:112px">Hasta la<br>máquina<br><em>más grande</em></h1>
<p class="bajada" style="font-size:32px">Herramientas eléctricas, neumáticas, jardín, generadores y <b>maquinaria FEMA.</b></p>
<div style="position:relative;display:grid;grid-template-columns:1.15fr 1fr;grid-template-rows:1fr 1fr;gap:20px;height:520px;margin-top:36px">
  {g.tarjeta(P3[0], "grid-row:1 / span 2")}{g.tarjeta(P3[1])}{g.tarjeta(P3[2])}
  <div class="etiqueta" style="position:absolute;top:-22px;left:-14px">EN STOCK</div>
</div>
'''

    p4 = f'''
<div class="volanta">Todo el país</div>
<h1 style="font-size:124px">Más de<br><em>10.000</em><br>productos</h1>
<div style="display:flex;justify-content:space-between;margin-top:34px">
  <div style="width:470px">
    <p class="bajada" style="font-size:32px;margin-top:0"><b>Casa central y sucursal en Córdoba.</b> Envíos a todo el país.</p>
    <div style="background:#111;color:#fff;padding:36px 34px;margin-top:44px">
      <div style="font-family:Titular;font-weight:900;font-size:46px;line-height:1.02;letter-spacing:-1px">Al mundo le falta un tornillo y <span style="color:#E10600">Clabutor</span> lo tiene.</div>
    </div>
    <div style="margin-top:30px;font-weight:700;font-size:28px">clabutor.com.ar</div>
  </div>
  <div style="margin-top:-10px;margin-right:-60px">{g.svg_mapa(300, [(-64.18, -31.42, "Córdoba")])}</div>
</div>
'''
    return [p1, p2, p3, p4]
