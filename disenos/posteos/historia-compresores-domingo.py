"""Historias — Domingo para equiparte: compresores con precio especial (contenido tal cual MARKETING PRODUCTOS CONTENIDO).
Portada informativa (con barras, compresor FEMA a correa 500 L 69370226) + 3 historias de producto (sin barras), 2 compresores por historia.
Compresores con stock en BaseLinker (INVENTARIO COMPLETO FEMA 2026 MATIAS, grupo 65271) al 22/11 y foto del Drive.
Precio = costo BaseLinker + 35 % (no lleva envío gratis: el contenido dice "Envíos a todo el país")."""

ID = "historia-compresores-domingo"
FORMATO = "historia"
CINTA = None
RUBRO = ""
TEXTO = ""
ROJO = "#E10600"
NEGRO = "#111111"
MARGEN = 1.35

# sku, nombre, característica, costo BaseLinker
GRUPOS = [
    ("Chicos y<br><em>silenciosos</em>", "Para el hogar y trabajos livianos.", [
        ("69370100", "Compresor DUCA Silen<br>3/4 HP 6 L", "Silencioso, cárter seco y 2 manómetros", 186700.8),
        ("69370102", "Compresor DUCA Silen<br>3/4 HP 12 L", "Silencioso, cárter seco y acople rápido", 181927.2),
    ]),
    ("Aire para<br><em>tu taller</em>", "Para herramientas neumáticas y pintura.", [
        ("69370024", "Compresor DUCA W<br>3 HP 100 L", "2 cilindros en V, 360 L/min y 220 V", 378705.6),
        ("69370026", "Compresor DUCA PRO<br>3 HP 120 L", "Con manómetro, llave esférica y 220 V", 630115.2),
    ]),
    ("Uso<br><em>profesional</em>", "Para talleres grandes e industria.", [
        ("69370221", "Compresor FEMA a correa<br>3 HP 280 L", "Monofásico, con manómetro y patas", 1003516.8),
        ("69370052", "Compresor DUCA PRO<br>5,5 HP 330 L", "Trifásico 380 V, con manómetro", 1357470.4),
    ]),
]


def pesos(n):
    return "$" + f"{round(n):,}".replace(",", ".")


def foto(sku, estilo):
    return f'<img src="../../productos/recortes/{sku}.png" style="{estilo};object-fit:contain">'


def camion(tam=70):
    return (f'<svg width="{tam}" height="{int(tam*.7)}" viewBox="0 0 100 70"><path d="M4 8h54v40H4ZM58 22h20l16 16v10H58Z" fill="none" '
            f'stroke="#fff" stroke-width="8" stroke-linejoin="round"/><circle cx="22" cy="56" r="9" fill="#fff"/><circle cx="76" cy="56" r="9" fill="#fff"/></svg>')


def tarjeta(sku, nombre, rasgo, costo):
    return f'''<div style="display:flex;flex-direction:column;height:430px;border-top:3px solid {NEGRO};padding-top:14px">
  <div style="flex:1;min-height:0;display:flex;align-items:center;justify-content:center">{foto(sku, "max-width:92%;max-height:100%")}</div>
  <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin-top:8px">
    <div>
      <div style="font-family:Titular;font-weight:900;font-size:36px;line-height:1.05;letter-spacing:-.5px">{nombre}</div>
      <div style="font-weight:600;font-size:24px;color:#555;margin-top:6px">{rasgo}</div>
    </div>
    <div style="font-family:Titular;font-weight:900;font-size:64px;letter-spacing:-2px;line-height:1;color:{ROJO};white-space:nowrap">{pesos(costo * MARGEN)}</div>
  </div>
</div>'''


def placas(g):
    portada = f'''
<div class="pildora"><i></i>DOMINGO</div>
<h1 style="font-size:116px;margin-top:26px;white-space:nowrap">Domingo para<br><em>equiparte</em></h1>
<p class="bajada" style="font-size:42px">Compresores con <b>precio especial.</b></p>
<div style="height:560px;margin-top:20px;display:flex;align-items:center;justify-content:center">{foto("69370226", "max-width:100%;max-height:100%")}</div>
<div style="position:absolute;left:0;right:0;bottom:0">
  <div style="background:{NEGRO};color:#fff;padding:24px 32px;font-family:Titular;font-weight:900;font-size:44px;line-height:1.08">Tu taller, siempre<br>con aire a presión.</div>
  <div style="display:flex;align-items:center;gap:22px;background:{ROJO};color:#fff;padding:20px 32px">{camion(70)}
    <span style="font-family:Titular;font-weight:900;font-size:40px;letter-spacing:2px">ENVÍOS A TODO EL PAÍS</span></div>
</div>
'''
    salida = [("blanca colores-marca", portada)]
    for titulo, bajada, prods in GRUPOS:
        html = g.MARCA_PRODUCTO + f'''
<div class="pildora"><i></i>PRECIO ESPECIAL</div>
<h1 style="font-size:92px;margin-top:18px;white-space:nowrap">{titulo}</h1>
<p class="bajada" style="font-size:34px;margin-top:12px">{bajada}</p>
<div style="display:flex;flex-direction:column;gap:18px;margin-top:18px">{"".join(tarjeta(*p) for p in prods)}</div>
'''
        salida.append(("blanca colores-marca", html))
    return salida
