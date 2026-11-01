"""Historias CyberMonday — Posteo A "Se viene el CyberMonday"
(contenido tal cual MARKETING PRODUCTOS CONTENIDO). 3 historias 1080x1920."""

ID = "historia-cyber-a-se-viene-el-cybermonday"
FORMATO = "historia"
CINTA = "cyber"
RUBRO = ""

TEXTO = """
Historias CyberMonday 2, 3 y 4 de noviembre — Posteo A "Se viene el CyberMonday".
"""

NARANJA = "#FF6A00"
AZUL = "#0B1F3A"


def calendario():
    """Noviembre 2026 (empieza domingo): primeras dos semanas, con 2, 3 y 4 marcados."""
    dias = ["L", "M", "M", "J", "V", "S", "D"]
    filas = [[None] * 6 + [1], [2, 3, 4, 5, 6, 7, 8]]
    cab = "".join(f'<div style="text-align:center;font-weight:700;font-size:30px;color:#8FA3C2">{d}</div>' for d in dias)
    celdas = ""
    for fila in filas:
        for d in fila:
            if d is None:
                celdas += "<div></div>"
            elif d in (2, 3, 4):
                celdas += (f'<div style="background:{NARANJA};color:#fff;display:flex;align-items:center;justify-content:center;'
                           f'font-family:Titular;font-weight:900;font-size:130px;letter-spacing:-4px;height:190px">{d}</div>')
            else:
                celdas += (f'<div style="display:flex;align-items:center;justify-content:center;font-family:Titular;font-weight:700;'
                           f'font-size:48px;color:#5C7398;height:190px">{d}</div>')
    return f'''
<div style="background:#16325C;padding:34px 30px 30px;margin-top:60px">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:26px">
    <div style="font-family:Titular;font-weight:900;font-size:44px;letter-spacing:4px">NOVIEMBRE</div>
    <div style="display:flex;gap:16px"><span style="width:22px;height:22px;border-radius:50%;background:{NARANJA}"></span><span style="width:22px;height:22px;border-radius:50%;background:{NARANJA}"></span></div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:10px;margin-bottom:12px">{cab}</div>
  <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:10px">{celdas}</div>
</div>'''


IC = f'fill="none" stroke="{NARANJA}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"'
ICONOS = {
    "etiqueta": f'<path {IC} d="M14 50 50 14h34v34L48 84Z"/><circle cx="68" cy="30" r="7" fill="{NARANJA}"/>',
    "estrella": f'<path {IC} d="M50 10l11.8 24 26.4 3.8-19.1 18.6 4.5 26.3L50 70.3 26.4 82.7l4.5-26.3L11.8 37.8l26.4-3.8Z"/>',
    "tarjeta": f'<rect {IC} x="8" y="22" width="84" height="56" rx="8"/><path {IC} d="M8 40h84M20 64h22"/>',
    "camion": f'<path {IC} d="M6 26h52v40H6ZM58 40h20l14 14v12H58Z"/><circle cx="24" cy="72" r="9" fill="#fff" stroke="{NARANJA}" stroke-width="7"/><circle cx="76" cy="72" r="9" fill="#fff" stroke="{NARANJA}" stroke-width="7"/>',
}


def icono(n, tam=120):
    return f'<svg viewBox="0 0 100 100" width="{tam}" height="{tam}" xmlns="http://www.w3.org/2000/svg">{ICONOS[n]}</svg>'


def beneficio(n, texto):
    return (f'<div style="display:flex;align-items:center;gap:40px;padding:28px 0;border-bottom:3px solid #E3E8F0">'
            f'<div style="width:170px;height:170px;background:#FFF1E6;display:flex;align-items:center;justify-content:center">{icono(n)}</div>'
            f'<div style="font-family:Titular;font-weight:900;font-size:60px;line-height:1;letter-spacing:-1px">{texto}</div></div>')


def celular():
    """Celular con la campanita de notificaciones y una mano tocándola."""
    return f'''<svg viewBox="0 0 760 980" width="560" xmlns="http://www.w3.org/2000/svg">
  <rect x="150" y="20" width="400" height="740" rx="56" fill="#16325C" stroke="#fff" stroke-width="10"/>
  <rect x="285" y="44" width="130" height="18" rx="9" fill="#0B1F3A"/>
  <g transform="translate(350 330)">
    <circle r="150" fill="{NARANJA}" opacity=".16"/>
    <circle r="108" fill="{NARANJA}" opacity=".28"/>
    <path d="M-62 40v-50a62 62 0 0 1 124 0v50l18 22h-160Z" fill="{NARANJA}"/>
    <path d="M-22 74a22 22 0 0 0 44 0Z" fill="{NARANJA}"/>
    <rect x="-9" y="-92" width="18" height="24" rx="9" fill="{NARANJA}"/>
    <circle cx="56" cy="-58" r="26" fill="#fff"/>
    <text x="56" y="-47" text-anchor="middle" font-family="Titular" font-weight="900" font-size="32" fill="{AZUL}">1</text>
  </g>
  <rect x="210" y="560" width="280" height="20" rx="10" fill="#2A4C80"/>
  <rect x="210" y="600" width="200" height="20" rx="10" fill="#2A4C80"/>
  <!-- mano -->
  <g transform="translate(372 400) rotate(-18)">
    <rect x="-34" y="0" width="68" height="250" rx="34" fill="#F1F4F9" stroke="{AZUL}" stroke-width="6"/>
    <path d="M-34 170 L-34 420 Q-34 470 16 470 L170 470 Q220 470 220 420 L220 250 Q220 200 175 200 Q150 200 140 220 Q130 180 95 180 Q70 180 60 205 Q50 170 20 170 Q0 170 0 190" fill="#F1F4F9" stroke="{AZUL}" stroke-width="6" stroke-linejoin="round"/>
    <rect x="-34" y="0" width="68" height="250" rx="34" fill="#F1F4F9"/>
    <path d="M-34 34 A34 34 0 0 1 34 34 L34 240 M-34 34 L-34 240" fill="none" stroke="{AZUL}" stroke-width="6"/>
    <path d="M-16 26 q16 -10 32 0" fill="none" stroke="#C9D3E3" stroke-width="6" stroke-linecap="round"/>
  </g>
</svg>'''


def placas(g):
    h1 = f'''
<h1 style="font-size:112px">Se viene el<br><em>CyberMonday</em></h1>
<p class="bajada"><b>2, 3 y 4 de noviembre.</b><br>Agendalo.</p>
{calendario()}
'''

    h2 = f'''
<h1 style="font-size:112px">3 beneficios,<br><em>3 días</em></h1>
<div style="margin-top:46px">
  {beneficio("etiqueta", "Descuentos especiales")}
  {beneficio("estrella", "Productos únicos")}
  {beneficio("tarjeta", "12 cuotas")}
</div>
<div style="display:flex;align-items:center;gap:30px;margin-top:44px">
  {icono("camion", 130)}
  <div style="font-weight:700;font-size:44px;color:#42526B">Y envío a todo el país.</div>
</div>
'''

    h3 = f'''
<h1 style="font-size:150px">No te<br>lo <em>pierdas</em></h1>
<p class="bajada">Activá las notificaciones<br>y <b>enterate primero de cada oferta.</b></p>
<div style="display:flex;justify-content:center;margin-top:40px">{celular()}</div>
'''
    return [("azul", h1), ("blanca", h2), ("azul", h3)]
