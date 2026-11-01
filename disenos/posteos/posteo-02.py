"""Posteo 2 — "Desde 1957" (contenido tal cual MARKETING PRODUCTOS CONTENIDO).
Colores llevados a la paleta fija de Clabutor: naranja -> rojo #E10600, fondo azul -> negro."""

ID = "posteo-02-desde-1957"
RUBRO = "Bulonería · Herramientas"

TEXTO = """
Lo que empezó como una bulonería familiar hoy es una ferretería industrial con miles de productos. Gracias a cada cliente que nos eligió desde 1957.

Casa central: Domingo F. Sarmiento 365 · Sucursal: Blvd. de los Alemanes 5310 · clabutor.com.ar

#clabutor #desde1957 #cordoba #comerciolocal
"""

SEPIA = "sepia(.45) saturate(.85) contrast(1.05) brightness(1.02)"


def placas(g):
    p1 = f'''
<div class="volanta">Nuestra historia</div>
<h1 style="font-size:96px;margin-top:22px">Desde</h1>
<div style="font-family:Titular;font-weight:900;font-size:300px;line-height:.8;letter-spacing:-12px;color:#E10600;margin-top:4px">1957</div>
<p class="bajada" style="font-size:34px;margin-top:30px">Una empresa familiar que empezó vendiendo bulones<br><b>en pleno centro de Córdoba.</b></p>
{g.foto_lugar("casa-central", "position:absolute;left:80px;right:80px;bottom:140px;height:470px", SEPIA, "FOTO CASA CENTRAL")}
'''

    p2 = f'''
<div class="volanta">Nuestros locales</div>
<h1 style="font-size:124px">Crecimos<br>con <em>Córdoba</em></h1>
<p class="bajada" style="font-size:32px">Casa central en <b>Domingo F. Sarmiento 365</b><br>y sucursal en <b>Blvd. de los Alemanes 5310.</b></p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;position:absolute;left:80px;right:80px;bottom:150px;height:520px">
  <div style="position:relative">{g.foto_lugar("casa-central", "height:100%", "", "FOTO CASA CENTRAL")}{g.pin("CASA CENTRAL", "left:16px;bottom:16px")}</div>
  <div style="position:relative">{g.foto_lugar("sucursal", "height:100%", "", "FOTO SUCURSAL")}{g.pin("SUCURSAL", "left:16px;bottom:16px")}</div>
</div>
'''

    valores = "".join(
        f'<div style="display:flex;align-items:center;gap:20px;padding:16px 0;border-bottom:2px solid #D6D6D6">'
        f'<span style="width:14px;height:44px;background:#E10600;flex:none"></span>'
        f'<span style="font-family:Titular;font-weight:900;font-size:50px;letter-spacing:-1px;text-transform:uppercase">{v}</span></div>'
        for v in ["Integridad", "Solidez", "Compromiso", "Calidad"])
    p3 = f'''
<div class="volanta">Nuestros valores</div>
<h1 style="font-size:124px">Lo que<br><em>no cambió</em></h1>
<p class="bajada" style="font-size:32px">Los mismos valores,<br><b>ahora también online.</b></p>
<div style="display:grid;grid-template-columns:440px 1fr;gap:34px;margin-top:34px;height:380px">
  <div>{valores}</div>
  {g.foto_lugar("mostrador", "height:100%", "", "FOTO MOSTRADOR")}
</div>
<div style="position:absolute;left:80px;right:80px;bottom:140px;background:#111;color:#fff;padding:30px 36px">
  <div style="font-family:Titular;font-weight:900;font-size:42px;line-height:1.05;letter-spacing:-1px">Casi 70 años después,<br>seguimos atendiendo <span style="color:#E10600">como el primer día.</span></div>
</div>
'''
    return [("", p1), ("oscura", p2), ("gris", p3)]
