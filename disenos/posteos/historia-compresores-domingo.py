"""Historias — Domingo para equiparte: compresores con precio especial (contenido tal cual MARKETING PRODUCTOS CONTENIDO).
Portada informativa (con barras, compresor FEMA a correa 500 L 69370226) + 6 historias de producto (sin barras), un compresor por historia, con SKU.
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

# sku, nombre, característica, costo BaseLinker, título, uso
PRODUCTOS = [
    ("69370100", "Compresor DUCA Silen 3/4 HP 6 L", "Silencioso, cárter seco y 2 manómetros", 186700.8,
     "Silencioso<br><em>y portátil</em>", "Para el hogar y trabajos livianos."),
    ("69370102", "Compresor DUCA Silen 3/4 HP 12 L", "Silencioso, cárter seco y acople rápido", 181927.2,
     "Silencioso,<br><em>con más aire</em>", "Para inflar, soplar y pintar."),
    ("69370024", "Compresor DUCA W 3 HP 100 L", "2 cilindros en V, 360 L/min y 220 V", 378705.6,
     "Aire para<br><em>tu taller</em>", "Para herramientas neumáticas y pintura."),
    ("69370026", "Compresor DUCA PRO 3 HP 120 L", "Con manómetro, llave esférica y 220 V", 630115.2,
     "Más reserva<br><em>de aire</em>", "Para trabajar todo el día en el taller."),
    ("69370221", "Compresor FEMA a correa 3 HP 280 L", "Monofásico, con manómetro y patas", 1003516.8,
     "Potencia<br><em>a correa</em>", "Para talleres grandes, sin conexión trifásica."),
    ("69370052", "Compresor DUCA PRO 5,5 HP 330 L", "Trifásico 380 V, con manómetro", 1357470.4,
     "Uso<br><em>profesional</em>", "Para la industria y el trabajo continuo."),
]


def pesos(n):
    return "$" + f"{round(n):,}".replace(",", ".")


def foto(sku, estilo):
    return f'<img src="../../productos/recortes/{sku}.png" style="{estilo};object-fit:contain">'


def camion(tam=70):
    return (f'<svg width="{tam}" height="{int(tam*.7)}" viewBox="0 0 100 70"><path d="M4 8h54v40H4ZM58 22h20l16 16v10H58Z" fill="none" '
            f'stroke="#fff" stroke-width="8" stroke-linejoin="round"/><circle cx="22" cy="56" r="9" fill="#fff"/><circle cx="76" cy="56" r="9" fill="#fff"/></svg>')


def placa_producto(g, sku, nombre, rasgo, costo, titulo, uso):
    return g.MARCA_PRODUCTO + f'''
<div class="pildora"><i></i>PRECIO ESPECIAL</div>
<h1 style="font-size:108px;margin-top:22px;white-space:nowrap">{titulo}</h1>
<p class="bajada" style="font-size:38px;margin-top:16px">{uso}</p>
<div style="height:640px;margin-top:20px;border-top:3px solid {NEGRO};display:flex;align-items:center;justify-content:center">{foto(sku, "max-width:96%;max-height:600px")}</div>
<div style="font-family:Titular;font-weight:900;font-size:44px;line-height:1.05;letter-spacing:-.5px;margin-top:10px">{nombre}</div>
<div style="font-weight:600;font-size:28px;color:#555;margin-top:8px">{rasgo}</div>
<div style="font-weight:700;font-size:24px;letter-spacing:2px;color:#8A8A8A;margin-top:6px">SKU {sku}</div>
<div style="font-family:Titular;font-weight:900;font-size:130px;letter-spacing:-5px;line-height:1;color:{ROJO};margin-top:10px">{pesos(costo * MARGEN)}</div>
'''


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
    salida += [("blanca colores-marca", placa_producto(g, *p)) for p in PRODUCTOS]
    return salida
