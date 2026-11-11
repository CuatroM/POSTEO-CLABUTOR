"""Historia — Ya estamos abiertos (vuelta del feriado). Colores Clabutor, fondo blanco.
Fotos de los dos locales + WhatsApp y dirección de cada uno (regla de contacto)."""

ID = "historia-abiertos"
FORMATO = "historia"
CINTA = None
RUBRO = ""
TEXTO = ""
ROJO = "#E10600"

WA = ('<svg width="40" height="40" viewBox="0 0 32 32"><circle cx="16" cy="16" r="16" fill="#25D366"/>'
      '<path d="M9 23l1.2-3.6A7.5 7.5 0 1 1 13 22Z" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg>')

LOCALES = [
    ("casa-central", "CASA CENTRAL", "Domingo F. Sarmiento 365 - Córdoba", "351 227 2419"),
    ("sucursal", "SUCURSAL", "Blvd. de los Alemanes 5310 - Córdoba", "351 227 2420"),
]


def local(foto, nombre, direccion, wa):
    return f'''<div style="display:flex;gap:26px;padding:22px 0;border-bottom:3px solid #111">
  <div style="width:320px;height:210px;flex:none;overflow:hidden;border-top:6px solid {ROJO}">
    <img src="../../fotos/{foto}.jpg" style="width:100%;height:100%;object-fit:cover;display:block">
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;gap:10px">
    <div style="font-family:Titular;font-weight:900;font-size:30px;letter-spacing:4px;color:{ROJO}">{nombre}</div>
    <div style="font-weight:600;font-size:26px;color:#555;white-space:nowrap">{direccion}</div>
    <div style="display:flex;align-items:center;gap:12px;margin-top:6px">{WA}
      <span style="font-family:Titular;font-weight:900;font-size:44px;letter-spacing:-.5px">{wa}</span></div>
  </div>
</div>'''


def placas(g):
    info = f'''
<div class="pildora"><i></i>HORARIO HABITUAL</div>
<h1 style="font-size:122px;margin-top:24px;white-space:nowrap">¡Ya estamos<br><em>abiertos!</em></h1>
<p class="bajada" style="font-size:38px">Volvimos a nuestro horario habitual.<br><b>¡Los esperamos en nuestras sucursales!</b></p>
<div style="margin-top:28px;border-top:3px solid #111">{"".join(local(*l) for l in LOCALES)}</div>
<div style="display:flex;align-items:center;gap:22px;background:{ROJO};color:#fff;padding:22px 28px;margin-top:32px">
  {WA.replace('width="40" height="40"', 'width="64" height="64"')}
  <div>
    <div style="font-family:Titular;font-weight:900;font-size:42px;line-height:1.05">¿Tenés una consulta?</div>
    <div style="font-weight:600;font-size:30px;margin-top:4px">Escribinos por WhatsApp y te ayudamos.</div>
  </div>
</div>
'''
    return [("blanca colores-marca", info)]
