"""Historias CyberMonday — "Arrancó el CyberMonday": lanzamiento con precios.
Una oferta por placa: producto recortado y grande sobre fondo liso, precio anterior tachado
(el de la web) y precio cyber grande en naranja. Sin cuotas (pedido del 2/11)."""

ID = "historia-cyber-c-arranco-el-cybermonday"
FORMATO = "historia"
CINTA = "cyber"
RUBRO = ""
TEXTO = ""

NARANJA = "#FF6A00"

# Placas 5 a 7: precio = costo informado por la sincronización (BaseLinker, grupo 65271,
# INVENTARIO COMPLETO FEMA 2026 MATIAS) + 35 %, redondeado al peso.
COSTO = {"69502706": 344318, "69370216": 723465.6, "69372106": 298014.08}
MARGEN = 1.35

# sku, nombre, antes (web), ahora, título comercial, envío gratis
OFERTAS = [
    ("G1910KAR", "Amoladora angular en kit 750 W Gamma", 196119, 85500,
     "Tu amoladora<br><em>con kit completo</em>", False),
    ("G3469ARA", "Soldadora inverter ARC130 Gamma", 418194, 97500,
     "Soldá como<br><em>un profesional</em>", False),
    ("601.IE.6200.7", "Soldadora inverter 220 A Salkor", 376490, 260000,
     "Más potencia<br><em>para soldar</em>", False),
    ("69502706", "Mesa plataforma elevadora hidráulica 150 kg", None, round(COSTO["69502706"] * MARGEN),
     "Levantá cargas<br><em>sin esfuerzo</em>", True),
    ("69370216", "Compresor a correa 3 HP 180 L", None, round(COSTO["69370216"] * MARGEN),
     "Aire de sobra<br><em>para tu taller</em>", True),
    ("69372106", "Desmalezadora Stiga SB 520 D 52 cc", None, round(COSTO["69372106"] * MARGEN),
     "Tu jardín,<br><em>impecable</em>", True),
]


def pesos(n):
    return "$" + f"{round(n):,}".replace(",", ".")


def placa_oferta(g, sku, nombre, antes, ahora, titulo, envio):
    rec = g.AQUI / "productos" / "recortes" / f"{sku}.png"
    foto = (f'<img src="../../productos/recortes/{sku}.png">' if rec.exists()
            else '<div style="color:#9AA6B8;font-weight:700;font-size:26px;letter-spacing:3px">FOTO PRODUCTO</div>')
    badge = ""
    if antes and ahora and antes > ahora:
        pct = round((1 - ahora / antes) * 100)
        badge = f'<div class="descuento"><b>-{pct}%</b><span>OFF</span></div>'
    gratis = ('<div class="envio-gratis"><svg width="44" height="30" viewBox="0 0 100 70"><path d="M4 8h54v40H4ZM58 22h20l16 16v10H58Z" fill="none" stroke="#fff" stroke-width="8" stroke-linejoin="round"/>'
              '<circle cx="22" cy="56" r="9" fill="#fff"/><circle cx="76" cy="56" r="9" fill="#fff"/></svg>ENVÍO GRATIS A TODO EL PAÍS</div>') if envio else ""
    tachado = f'<div class="precio-antes">{pesos(antes)}</div>' if antes else ""
    precio = pesos(ahora) if ahora else "$ —"
    return f'''
<div class="pildora"><i></i>OFERTA CYBER</div>
<h1 style="font-size:92px;margin-top:24px;white-space:nowrap">{titulo}</h1>
<div class="panel-oferta">{badge}{foto}{gratis}</div>
<div class="ficha">
  <div class="nombre-o">{g.e(nombre)}</div>
  <div class="sku-o">COD. {g.e(sku)}</div>
  <div class="precios"><div class="precio-cyber">{precio}</div>{tachado}</div>
</div>
'''


def placas(g):
    maximo = max(round((1 - a / b) * 100) for _, _, b, a, _, _ in OFERTAS if a and b)
    h1 = f'''
<h1 style="font-size:140px;margin-top:0">¡<em>Arrancó</em><br>el Cyber<br>Monday!</h1>
<p class="bajada" style="font-size:46px">Envío a todo el país.<br><b>Solo hasta el miércoles 4.</b></p>
<div style="display:flex;align-items:center;gap:30px;margin-top:36px">
  <div style="background:{NARANJA};color:#fff;padding:22px 30px;transform:rotate(-3deg)">
    <div style="font-family:Titular;font-weight:900;font-size:40px;letter-spacing:4px">HASTA</div>
    <div style="font-family:Titular;font-weight:900;font-size:150px;line-height:.85;letter-spacing:-6px">{maximo}%</div>
    <div style="font-family:Titular;font-weight:900;font-size:40px;letter-spacing:6px">OFF</div>
  </div>
</div>
<div style="margin-top:40px;border-left:12px solid {NARANJA};padding:6px 0 6px 34px">
  <div style="font-family:Titular;font-weight:900;font-size:64px;line-height:1.02;letter-spacing:-1px">Los mejores precios<br>se van primero.</div>
  <div style="font-weight:700;font-size:40px;color:#C9D3E3;margin-top:18px">Pasá y elegí el tuyo antes que otro &rarr;</div>
</div>
'''
    return [("azul", h1)] + [("azul", placa_oferta(g, *o)) for o in OFERTAS]
