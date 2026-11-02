"""Posteo 3 — "Comprá tranquilo" (contenido tal cual MARKETING PRODUCTOS CONTENIDO).
Colores llevados a la paleta fija del muro de Clabutor: naranja -> rojo #E10600, fondo azul -> negro."""

ID = "posteo-03-compra-tranquilo"
RUBRO = "Bulonería · Herramientas"

TEXTO = """
Comprá tranquilo en Clabutor: hasta 12 cuotas con tarjeta o precio especial en efectivo o transferencia, envío express en 48 hs y asesoramiento para elegir bien. La maquinaria FEMA tiene 6 meses de garantía del fabricante.

Comprá en clabutor.com.ar o escribinos por WhatsApp:
Casa central: 351 227 2419 · Domingo F. Sarmiento 365
Sucursal: 354 344 1711 · Blvd. de los Alemanes 5310

#clabutor #cordoba #herramientas #ferreteria #fema
"""

ROJO = "#E10600"


def escudo(tam=420, fondo="#111"):
    return f'''<svg viewBox="0 0 200 230" width="{tam}" xmlns="http://www.w3.org/2000/svg">
  <path d="M100 8 L184 40 V110 C184 165 148 204 100 222 C52 204 16 165 16 110 V40 Z" fill="{ROJO}"/>
  <path d="M100 30 L164 54 V110 C164 153 137 184 100 199 C63 184 36 153 36 110 V54 Z" fill="none" stroke="#fff" stroke-width="5" opacity=".35"/>
  <path d="M62 114 L90 142 L142 88" fill="none" stroke="#fff" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''


def camion(tam=150, color="#111"):
    return f'''<svg viewBox="0 0 120 80" width="{tam}" xmlns="http://www.w3.org/2000/svg">
  <path d="M6 10h66v46H6ZM72 26h24l18 18v12H72Z" fill="none" stroke="{color}" stroke-width="7" stroke-linejoin="round"/>
  <circle cx="26" cy="64" r="10" fill="#fff" stroke="{color}" stroke-width="7"/><circle cx="92" cy="64" r="10" fill="#fff" stroke="{color}" stroke-width="7"/>
  <path d="M-18 22h16M-24 36h22M-14 50h12" stroke="{ROJO}" stroke-width="6" stroke-linecap="round"/>
</svg>'''


def caja():
    """Caja de envío con la cinta de Clabutor, saliendo en camino (líneas de velocidad)."""
    return f'''<svg viewBox="0 0 640 470" width="560" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="350" cy="440" rx="230" ry="20" fill="#000" opacity=".08"/>
  <path d="M30 150h90M0 210h120M40 270h80" stroke="{ROJO}" stroke-width="12" stroke-linecap="round"/>
  <polygon points="160,140 360,70 560,140 360,210" fill="#E9C99A"/>
  <polygon points="160,140 360,210 360,430 160,360" fill="#D9AE73"/>
  <polygon points="560,140 360,210 360,430 560,360" fill="#C79A5E"/>
  <polygon points="240,112 440,182 440,212 240,142" fill="{ROJO}" opacity=".0"/>
  <polygon points="250,108 280,98 480,168 450,178" fill="{ROJO}"/>
  <polygon points="450,178 480,168 480,388 450,398" fill="#B00500"/>
  <g transform="translate(192 248) skewY(19)">
    <rect x="0" y="0" width="150" height="40" fill="#111"/>
    <rect x="10" y="12" width="14" height="14" fill="{ROJO}"/>
    <text x="34" y="27" font-family="Titular" font-weight="900" font-size="20" letter-spacing="1" fill="#fff">CLABUTOR</text>
  </g>
  <g transform="translate(380 230) skewY(-19)">
    <rect x="0" y="0" width="140" height="64" fill="#fff" opacity=".9"/>
    <rect x="14" y="14" width="80" height="8" fill="#BDBDBD"/><rect x="14" y="30" width="110" height="8" fill="#BDBDBD"/><rect x="14" y="46" width="60" height="8" fill="#BDBDBD"/>
  </g>
</svg>'''


def placas(g):
    razones = "".join(
        f'<div style="display:flex;align-items:center;gap:26px;padding:20px 0;border-bottom:2px solid #333">'
        f'<span style="font-family:Titular;font-weight:900;font-size:40px;color:{ROJO};width:62px">{n}</span>'
        f'<span style="font-family:Titular;font-weight:700;font-size:34px;letter-spacing:-.5px;white-space:nowrap">{t}</span></div>'
        for n, t in [("01", "Cuotas o precio especial"), ("02", "Envío express en 48 hs"), ("03", "Asesoramiento y garantía")])
    p1 = f'''
<div class="volanta">Comprá tranquilo</div>
<h1 style="font-size:116px">¿Por qué<br>comprar en<br><em>Clabutor?</em></h1>
<p class="bajada" style="font-size:36px"><b>3 razones para comprar tranquilo.</b></p>
<div style="display:flex;align-items:center;gap:46px;margin-top:36px">
  <div style="width:560px">{razones}</div>
  <div style="flex:1;display:flex;justify-content:center">{escudo(270)}</div>
</div>
'''

    rec = g.AQUI / "productos" / "recortes" / "G1910KAR.png"
    foto = f'<img src="../../productos/recortes/G1910KAR.png" style="max-width:84%;max-height:84%;object-fit:contain">' if rec.exists() else ""
    p2 = f'''
<div class="volanta">Razón 01</div>
<h1 style="font-size:104px">Pagá como<br>te quede <em>mejor</em></h1>
<p class="bajada" style="font-size:32px">Hasta <b>12 cuotas con tarjeta,</b><br>o <b>precio especial</b> en efectivo o transferencia.</p>
<div style="position:relative;background:#fff;margin-top:34px;height:540px;display:flex;flex-direction:column;border-top:2px solid #111">
  <div style="flex:1;min-height:0;display:flex;align-items:center;justify-content:center">{foto}</div>
  <div style="position:absolute;top:-26px;right:-20px;width:260px;height:260px;border-radius:50%;background:{ROJO};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg);box-shadow:0 10px 0 rgba(0,0,0,.12)">
    <span style="font-family:Titular;font-weight:900;font-size:26px;letter-spacing:4px">PRECIO</span>
    <b style="font-family:Titular;font-weight:900;font-size:56px;letter-spacing:-2px;line-height:1;margin-top:4px">$85.500</b>
    <span style="font-family:Titular;font-weight:700;font-size:19px;letter-spacing:1px;margin-top:6px;text-align:center;line-height:1.1">EFECTIVO O<br>TRANSFERENCIA</span>
  </div>
  <div style="padding:0 0 22px">
    <div style="font-family:Titular;font-weight:700;font-size:28px">Amoladora angular en kit 750 W Gamma</div>
    <div style="font-weight:600;font-size:18px;color:#8A8A8A;letter-spacing:1px;margin-top:4px">COD. G1910KAR</div>
  </div>
</div>
'''

    p3 = f'''
<div class="volanta">Razón 02</div>
<h1 style="font-size:116px">Envío express<br><em>en 48 hs</em></h1>
<p class="bajada" style="font-size:34px">Pedí en <b>clabutor.com.ar</b> con compra segura<br>y <b>recibilo rápido.</b></p>
<div style="position:absolute;left:80px;right:80px;top:560px;bottom:140px;display:flex;flex-direction:column">
  <div style="flex:1;min-height:0;display:flex;align-items:center;justify-content:center">{caja()}</div>
  <div style="align-self:flex-start;display:flex;align-items:center;gap:18px;background:#111;color:#fff;padding:16px 26px;margin-bottom:24px">
    {camion(70, "#fff")}<span style="font-family:Titular;font-weight:900;font-size:30px;letter-spacing:3px">ENVÍOS A TODO EL PAÍS</span>
  </div>
</div>
'''

    rec4 = g.AQUI / "productos" / "recortes" / "69510215.png"
    foto4 = (f'<img src="../../productos/recortes/69510215.png" style="max-width:80%;max-height:360px;object-fit:contain">'
             if rec4.exists() else '<div style="color:#9A9A9A;font-weight:700;font-size:22px;letter-spacing:2px">FOTO 69510215</div>')
    p4 = f'''
<div class="volanta">Razón 03</div>
<h1 style="font-size:104px">Asesoramiento<br><em>y garantía</em></h1>
<p class="bajada" style="font-size:32px"><b>Te ayudamos a elegir.</b> La maquinaria FEMA tiene<br>6 meses de garantía del fabricante.</p>
<div style="display:grid;grid-template-columns:360px 1fr;gap:24px;margin-top:30px;height:470px;overflow:hidden">
  <div style="position:relative;background:#fff;display:flex;flex-direction:column">
    <div style="flex:1;min-height:0;display:flex;align-items:center;justify-content:center;padding-top:14px">{foto4}</div>
    <div style="padding:0 18px 14px;color:#111">
      <div style="font-family:Titular;font-weight:700;font-size:24px">Pisonador FEMA F-66 3 HP</div>
      <div style="font-weight:600;font-size:16px;color:#8A8A8A;letter-spacing:1px;margin-top:2px">COD. 69510215</div>
    </div>
    <div style="position:absolute;top:16px;right:16px;background:{ROJO};color:#fff;padding:10px 16px;font-family:Titular;font-weight:900;font-size:22px;letter-spacing:2px;line-height:1.05;text-align:center">6 MESES<br>DE GARANTÍA</div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center">
    <div style="position:relative;background:#fff;color:#111;padding:26px 28px;border-radius:28px 28px 28px 4px">
      <div style="font-weight:600;font-size:24px;color:#555">¿Dudas con tu equipo?</div>
      <div style="font-family:Titular;font-weight:900;font-size:36px;line-height:1.05;margin-top:6px">Escribinos por WhatsApp</div>
      <div style="margin-top:18px;padding-top:16px;border-top:2px solid #E6E6E6">
        <div style="font-weight:700;font-size:18px;letter-spacing:2px;color:#777">CASA CENTRAL</div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:4px"><svg width="34" height="34" viewBox="0 0 32 32"><circle cx="16" cy="16" r="16" fill="#25D366"/><path d="M9 23l1.2-3.6A7.5 7.5 0 1 1 13 22Z" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg><span style="font-family:Titular;font-weight:900;font-size:38px;letter-spacing:-.5px;color:{ROJO}">351 227 2419</span></div>
        <div style="font-weight:500;font-size:20px;color:#555;margin-top:2px">Domingo F. Sarmiento 365</div>
      </div>
      <div style="margin-top:14px;padding-top:14px;border-top:2px solid #E6E6E6">
        <div style="font-weight:700;font-size:18px;letter-spacing:2px;color:#777">SUCURSAL</div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:4px"><svg width="34" height="34" viewBox="0 0 32 32"><circle cx="16" cy="16" r="16" fill="#25D366"/><path d="M9 23l1.2-3.6A7.5 7.5 0 1 1 13 22Z" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg><span style="font-family:Titular;font-weight:900;font-size:38px;letter-spacing:-.5px;color:{ROJO}">354 344 1711</span></div>
        <div style="font-weight:500;font-size:20px;color:#555;margin-top:2px">Blvd. de los Alemanes 5310</div>
      </div>
      <svg width="40" height="30" viewBox="0 0 40 30" style="position:absolute;left:0;bottom:-28px"><path d="M0 0h40L0 30Z" fill="#fff"/></svg>
    </div>
  </div>
</div>
'''
    return [("oscura", p1), ("", p2), ("", p3), ("oscura", p4)]
