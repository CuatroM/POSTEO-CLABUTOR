"""Historias CyberMonday — Posteo B "Armá tu lista"
(contenido tal cual MARKETING PRODUCTOS CONTENIDO). 4 historias 1080x1920, sin precios."""

ID = "historia-cyber-b-arma-tu-lista"
FORMATO = "historia"
CINTA = "cyber"
RUBRO = ""

TEXTO = """
Historias CyberMonday — Posteo B "Armá tu lista".
"""

NARANJA = "#FF6A00"
AZUL = "#0B1F3A"


def tarjeta(g, sku, nombre, marca="proximamente"):
    foto = g.foto_producto(sku).replace("<img ", '<img style="max-width:100%;max-height:100%;object-fit:contain" ')
    if marca == "proximamente":
        pie = ('<div class="precio-tapado"><span class="falso">$ ?.???</span>'
               '<div class="franja">PRÓXIMAMENTE</div></div>')
        sello = ""
    else:
        pie = ""
        sello = '<div class="sello-cyber">CYBER</div>'
    return (f'<div class="adelanto" style="position:relative">{sello}<div class="foto-a">{foto}</div>'
            f'<div class="datos-a"><div class="nombre-a">{g.e(nombre)}</div><div class="sku-a">COD. {g.e(sku)}</div></div>{pie}</div>')


def libreta():
    """Libreta de obra con lista tildada y lápiz de carpintero."""
    items = ["Herramientas", "Jardín", "Generadores", "Bulonería"]
    filas = ""
    for i, t in enumerate(items):
        y = 190 + i * 96
        filas += (f'<rect x="92" y="{y-34}" width="44" height="44" rx="6" fill="none" stroke="{AZUL}" stroke-width="5"/>'
                  f'<path d="M100 {y-12} l12 13 l26 -32" fill="none" stroke="{NARANJA}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
                  f'<text x="166" y="{y}" font-family="Titular" font-weight="700" font-size="44" fill="{AZUL}">{t}</text>'
                  f'<line x1="92" y1="{y+30}" x2="560" y2="{y+30}" stroke="#D5DCE6" stroke-width="3"/>')
    anillos = "".join(f'<rect x="{110 + i*60}" y="36" width="18" height="60" rx="9" fill="#9AA6B8"/>' for i in range(8))
    return f'''<svg viewBox="0 0 780 660" width="600" xmlns="http://www.w3.org/2000/svg">
  <rect x="58" y="70" width="560" height="560" rx="14" fill="#C9D2DE"/>
  <rect x="44" y="60" width="560" height="560" rx="14" fill="#FFFFFF" stroke="{AZUL}" stroke-width="5"/>
  <rect x="44" y="60" width="560" height="64" rx="14" fill="{AZUL}"/>
  <rect x="44" y="100" width="560" height="24" fill="{AZUL}"/>
  {anillos}
  {filas}
  <g transform="translate(650 120) rotate(28)">
    <rect x="-26" y="0" width="52" height="420" fill="{NARANJA}"/>
    <rect x="-26" y="0" width="16" height="420" fill="#FF8F40"/>
    <polygon points="-26,420 26,420 14,500 -14,500" fill="#E8C9A0"/>
    <rect x="-10" y="482" width="20" height="18" fill="#2B2B2B"/>
    <rect x="-26" y="0" width="52" height="34" fill="{AZUL}"/>
  </g>
</svg>'''


def placas(g):
    h1 = f'''
<h1 style="font-size:120px;color:{AZUL}">¿Qué te<br>falta?<br><em>Armá<br>tu lista</em></h1>
<p class="bajada">En 4 días arranca el CyberMonday.<br><b>Mirá lo que viene.</b></p>
<div style="display:flex;justify-content:center;margin-top:40px">{libreta()}</div>
'''

    def placa_productos(titulo, bajada, a, b, marca="proximamente", tam=112):
        return f'''
<h1 style="font-size:{tam}px">{titulo}</h1>
<p class="bajada" style="font-size:42px">{bajada}</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:46px;flex:1;min-height:0;max-height:640px">
  {tarjeta(g, *a, marca=marca)}{tarjeta(g, *b, marca=marca)}
</div>
'''

    h2 = placa_productos("Para la obra<br><em>y el taller</em>",
                         "Herramientas eléctricas, neumáticas<br>y de mano <b>de primeras marcas.</b>",
                         ("KHE2445", "Martillo combinado Metabo"), ("7132", "Llave de impacto Bremen"))
    h3 = placa_productos("Para el jardín<br><em>y la casa</em>",
                         "Jardín, generadores<br><b>y todo para la temporada.</b>",
                         ("KLDDE52", "Desmalezadora KLD"), ("GE3460", "Generador Gamma 2500"))
    h4 = placa_productos("Y lo que todo<br>el mundo<br><em>necesita</em>",
                         "Bulonería, tornillos y fijaciones<br><b>por caja.</b>",
                         ("14108012TEL", "Tel Dry x 10.000"), ("104070008", "Fischer SX 8×40"), marca="cyber", tam=104)
    return [("gris", h1), ("azul", h2), ("verde", h3), ("blanca", h4)]
