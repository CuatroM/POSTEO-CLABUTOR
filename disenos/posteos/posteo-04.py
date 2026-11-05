"""Posteo 4 — "Seguimos con precios promocionales" (muro).
Portada + 5 productos de "Arrancó el CyberMonday" (sin la mesa elevadora). Sin fechas.
Precios: los mismos de la promo (Gamma y Salkor: precio fijado; FEMA: costo BaseLinker + 35 %).
El precio tachado es el que figuraba en clabutor.com.ar."""

ID = "posteo-04-seguimos-con-precios-promo"
RUBRO = "Bulonería · Herramientas"
ROJO = "#E10600"

TEXTO = """
¡Seguimos con precios promocionales! 🔥 Mantenemos las ofertas en herramientas y maquinaria para obra, taller y jardín.

• Amoladora angular en kit 750 W Gamma: $85.500
• Soldadora inverter ARC130 Gamma: $97.500
• Soldadora inverter 220 A Salkor: $260.000
• Compresor a correa 3 HP 180 L: $976.679, con envío gratis
• Desmalezadora Stiga SB 520 D 52 cc: $402.319, con envío gratis

Comprá en clabutor.com.ar o escribinos por WhatsApp:
Casa central: 351 227 2419 · Domingo F. Sarmiento 365 - Córdoba
Sucursal: 351 227 2420 · Blvd. de los Alemanes 5310 - Córdoba

#clabutor #cordoba #herramientas #ofertas #fema #gamma
"""

# sku, nombre, antes (web), ahora, título comercial, envío gratis
PRODUCTOS = [
    ("G1910KAR", "Amoladora angular en kit 750 W Gamma", 196119, 85500,
     "Tu amoladora<br><em>con kit completo</em>", False),
    ("G3469ARA", "Soldadora inverter ARC130 Gamma", 418194, 97500,
     "Soldá como<br><em>un profesional</em>", False),
    ("601.IE.6200.7", "Soldadora inverter 220 A Salkor", 376490, 260000,
     "Más potencia<br><em>para soldar</em>", False),
    ("69370216", "Compresor a correa 3 HP 180 L", None, round(723465.6 * 1.35),
     "Aire de sobra<br><em>para tu taller</em>", True),
    ("69372106", "Desmalezadora Stiga SB 520 D 52 cc", None, round(298014.08 * 1.35),
     "Tu jardín,<br><em>impecable</em>", True),
]


def pesos(n):
    return "$" + f"{round(n):,}".replace(",", ".")


def placa_producto(g, sku, nombre, antes, ahora, titulo, envio):
    rec = g.AQUI / "productos" / "recortes" / f"{sku}.png"
    foto = f'<img src="../../productos/recortes/{sku}.png" style="max-width:88%;max-height:470px;object-fit:contain">' if rec.exists() else ""
    badge = ""
    if antes and antes > ahora:
        pct = round((1 - ahora / antes) * 100)
        badge = (f'<div style="position:absolute;top:18px;right:0;width:200px;height:200px;border-radius:50%;background:{ROJO};color:#fff;'
                 f'display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg)">'
                 f'<b style="font-family:Titular;font-weight:900;font-size:70px;letter-spacing:-3px;line-height:.9">-{pct}%</b>'
                 f'<span style="font-family:Titular;font-weight:900;font-size:28px;letter-spacing:4px">OFF</span></div>')
    gratis = ('<div style="position:absolute;left:0;bottom:16px;background:#111;color:#fff;padding:12px 20px;font-family:Titular;'
              'font-weight:900;font-size:24px;letter-spacing:3px">ENVÍO GRATIS A TODO EL PAÍS</div>') if envio else ""
    tachado = (f'<span style="font-weight:600;font-size:36px;color:#9A9A9A;text-decoration:line-through;margin-bottom:16px">{pesos(antes)}</span>'
               if antes else "")
    return f'''
<div class="volanta">Precio promocional</div>
<h1 style="font-size:96px;white-space:nowrap">{titulo}</h1>
<div style="position:relative;height:520px;margin-top:22px;display:flex;align-items:center;justify-content:center;border-top:2px solid #111">
  {foto}{badge}{gratis}
</div>
<div style="font-family:Titular;font-weight:700;font-size:30px;margin-top:6px">{g.e(nombre)}</div>
<div style="font-weight:600;font-size:18px;color:#8A8A8A;letter-spacing:2px;margin-top:4px">COD. {g.e(sku)}</div>
<div style="display:flex;align-items:flex-end;gap:26px;margin-top:6px">
  <span style="font-family:Titular;font-weight:900;font-size:118px;line-height:.95;letter-spacing:-4px;color:{ROJO}">{pesos(ahora)}</span>{tachado}
</div>
'''


def placas(g):
    maximo = max(round((1 - a / b) * 100) for _, _, b, a, _, _ in PRODUCTOS if b)
    portada = f'''
<div class="volanta">Ofertas que siguen</div>
<h1 style="font-size:106px">Seguimos con<br><em>precios</em><br><em>promocionales</em></h1>
<p class="bajada" style="font-size:34px;white-space:nowrap">Mantenemos las ofertas en herramientas y maquinaria.<br><b>Deslizá y elegí la tuya &rarr;</b></p>
<div style="position:absolute;left:80px;right:80px;top:740px;bottom:160px;display:flex;align-items:center;justify-content:center">
  <div style="background:{ROJO};color:#fff;padding:26px 60px 30px;transform:rotate(-4deg);text-align:center">
    <div style="font-family:Titular;font-weight:900;font-size:48px;letter-spacing:8px">HASTA</div>
    <div style="font-family:Titular;font-weight:900;font-size:250px;line-height:.8;letter-spacing:-10px">{maximo}%</div>
    <div style="font-family:Titular;font-weight:900;font-size:56px;letter-spacing:12px;margin-top:6px">OFF</div>
  </div>
</div>
'''
    return [("oscura", portada)] + [("", placa_producto(g, *p)) for p in PRODUCTOS]
