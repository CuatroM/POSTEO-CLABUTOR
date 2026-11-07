"""Historia — Feriados 9 y 10 de noviembre por la visita del Papa León XIV: locales cerrados.
Colores Clabutor (no es campaña): fondo negro, blanco y rojo."""

ID = "historia-feriado-papa"
FORMATO = "historia"
CINTA = None
RUBRO = ""
TEXTO = ""
ROJO = "#E10600"


def hoja(dia, nombre):
    return f'''<div style="background:#fff;color:#111;width:290px;border:3px solid #111;box-shadow:0 12px 0 #111">
  <div style="background:{ROJO};color:#fff;font-family:Titular;font-weight:900;font-size:34px;letter-spacing:6px;text-align:center;padding:16px 0">{nombre}</div>
  <div style="font-family:Titular;font-weight:900;font-size:180px;line-height:1;letter-spacing:-8px;text-align:center;padding:22px 0 6px">{dia}</div>
  <div style="font-weight:700;font-size:28px;letter-spacing:5px;text-align:center;color:#777;padding-bottom:26px">NOVIEMBRE</div>
</div>'''


def placas(g):
    info = f'''
<div class="pildora"><i></i>FERIADOS</div>
<h1 style="font-size:124px;margin-top:26px">Lunes 9 y<br>martes 10<br><em>cerrado</em></h1>
<p class="bajada" style="font-size:38px">Por la visita de <b>Su Santidad el Papa León XIV,</b><br>nuestros locales permanecen cerrados.</p>
<div style="display:flex;justify-content:center;gap:40px;margin-top:44px">
  <div style="transform:rotate(-4deg)">{hoja(9, "LUNES")}</div>
  <div style="transform:rotate(3deg);margin-top:30px">{hoja(10, "MARTES")}</div>
</div>
<div style="margin-top:56px;border-left:12px solid {ROJO};padding:4px 0 4px 30px">
  <div style="font-family:Titular;font-weight:900;font-size:42px;line-height:1.08">Mientras tanto, seguí comprando<br>online en <span style="color:{ROJO}">clabutor.com.ar</span></div>
</div>
'''
    return [("blanca colores-marca", info)]
