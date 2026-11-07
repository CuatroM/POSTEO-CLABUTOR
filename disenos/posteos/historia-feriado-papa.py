"""Historia — Feriados 9 y 10 de noviembre por la visita del Papa León XIV: locales cerrados.
Colores Clabutor (blanco, negro y rojo) + toque argentino (celeste y blanco, Sol de Mayo)
EXCLUSIVO de esta historia. Foto provista por el cliente."""

import math

ID = "historia-feriado-papa"
FORMATO = "historia"
CINTA = None
RUBRO = ""
TEXTO = ""
ROJO = "#E10600"
CELESTE = "#74ACDF"
SOL = "#F6B40E"


def sol(tam=120):
    rayos = ""
    for i in range(16):
        a = math.radians(i * 22.5)
        largo = 46 if i % 2 == 0 else 38
        x1, y1 = 50 + 22 * math.cos(a), 50 + 22 * math.sin(a)
        x2, y2 = 50 + largo * math.cos(a), 50 + largo * math.sin(a)
        rayos += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{SOL}" stroke-width="{5 if i % 2 == 0 else 3}" stroke-linecap="round"/>'
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 100 100">{rayos}'
            f'<circle cx="50" cy="50" r="19" fill="{SOL}"/><circle cx="50" cy="50" r="19" fill="none" stroke="#C98E00" stroke-width="2"/></svg>')


def franja_argentina():
    """Bandera como cinta superior: celeste - blanco (con sol) - celeste."""
    return f'''<div style="position:fixed;left:0;right:0;top:118px;height:84px;display:flex;flex-direction:column">
  <div style="flex:1;background:{CELESTE}"></div>
  <div style="flex:1;background:#fff;position:relative">
    <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)">{sol(56)}</div>
  </div>
  <div style="flex:1;background:{CELESTE}"></div>
</div>'''


def placas(g):
    foto = g.AQUI / "fotos" / "papa-leon-xiv.jpg"
    if not foto.exists():
        foto = g.AQUI / "fotos" / "papa-leon-xiv-original.png"
    info = f'''
{franja_argentina()}
<div class="pildora" style="margin-top:20px"><i></i>FERIADOS</div>
<h1 style="font-size:110px;margin-top:22px">Lunes 9 y<br>martes 10<br><em>cerrado</em></h1>
<p class="bajada" style="font-size:36px">Por la visita de <b>Su Santidad el Papa León XIV,</b><br>nuestros locales permanecen cerrados.</p>
<div style="display:flex;gap:30px;margin-top:34px;height:660px">
  <div style="flex:1;display:flex;flex-direction:column;justify-content:space-between;padding:6px 0">
    <div>
      {sol(110)}
      <div style="font-family:Titular;font-weight:900;font-size:62px;line-height:.98;letter-spacing:-1px;margin-top:14px">¡Bienvenido<br>a la<br><span style="color:{CELESTE}">Argentina!</span></div>
    </div>
    <div style="border-left:10px solid {ROJO};padding:4px 0 4px 22px">
      <div style="font-family:Titular;font-weight:900;font-size:32px;line-height:1.1">Seguí comprando<br>online en<br><span style="color:{ROJO}">clabutor.com.ar</span></div>
    </div>
  </div>
  <div style="width:440px;position:relative;border:6px solid {CELESTE};overflow:hidden;flex:none">
    <img src="../../fotos/{foto.name}" style="width:100%;height:100%;object-fit:cover;object-position:center top;display:block">
    <div style="position:absolute;left:0;right:0;bottom:0;height:16px;display:flex"><div style="flex:1;background:{CELESTE}"></div><div style="flex:1;background:#fff"></div><div style="flex:1;background:{CELESTE}"></div></div>
  </div>
</div>
'''
    return [("blanca colores-marca", info)]
