"""Historias — Bulonería y fijaciones para la industria (contenido tal cual MARKETING PRODUCTOS CONTENIDO).
4 historias informativas, colores Clabutor (blanco, negro y rojo). Mix de productos para mostrar variedad:
fotos reales (taco Fischer SX 8, autoperforante Tel alas, caja Tel x 10.000) + ilustraciones de bulón,
tuerca, arandela y varilla roscada (en la web no tienen foto)."""

ID = "historia-fijaciones"
FORMATO = "historia"
CINTA = None
RUBRO = ""
TEXTO = ""
ROJO = "#E10600"
NEGRO = "#111111"
METAL = "#9AA0A6"


# ---------- Ilustraciones (vista lateral, acero zincado) ----------
def _grad(id_):
    return (f'<defs><linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="#E9ECEF"/><stop offset=".45" stop-color="#B9BEC4"/>'
            f'<stop offset="1" stop-color="#7D838A"/></linearGradient></defs>')


def bulon(w=300, ang=0):
    rosca = "".join(f'<path d="M{210+i*13} 30 l7 40" stroke="#6B7177" stroke-width="3"/>' for i in range(15))
    return (f'<svg width="{w}" viewBox="0 0 420 100" style="transform:rotate({ang}deg)">{_grad("gb")}'
            f'<rect x="10" y="10" width="80" height="80" rx="4" fill="url(#gb)" stroke="#5E646A" stroke-width="3"/>'
            f'<path d="M10 36h80M10 64h80" stroke="#5E646A" stroke-width="2"/>'
            f'<rect x="90" y="30" width="320" height="40" fill="url(#gb)" stroke="#5E646A" stroke-width="3"/>{rosca}</svg>')


def tuerca(w=200):
    return (f'<svg width="{w}" viewBox="0 0 120 120">{_grad("gt")}'
            f'<polygon points="60,6 107,33 107,87 60,114 13,87 13,33" fill="url(#gt)" stroke="#5E646A" stroke-width="4"/>'
            f'<circle cx="60" cy="60" r="27" fill="#fff" stroke="#5E646A" stroke-width="4"/>'
            f'<circle cx="60" cy="60" r="21" fill="none" stroke="#9AA0A6" stroke-width="3" stroke-dasharray="4 4"/></svg>')


def arandela(w=200):
    return (f'<svg width="{w}" viewBox="0 0 120 120">{_grad("ga")}'
            f'<circle cx="60" cy="60" r="54" fill="url(#ga)" stroke="#5E646A" stroke-width="4"/>'
            f'<circle cx="60" cy="60" r="22" fill="#fff" stroke="#5E646A" stroke-width="4"/></svg>')


def varilla(w=360, ang=0):
    rosca = "".join(f'<path d="M{14+i*14} 6 l8 26" stroke="#6B7177" stroke-width="3"/>' for i in range(28))
    return (f'<svg width="{w}" viewBox="0 0 420 38" style="transform:rotate({ang}deg)">{_grad("gv")}'
            f'<rect x="6" y="5" width="408" height="28" rx="3" fill="url(#gv)" stroke="#5E646A" stroke-width="3"/>{rosca}</svg>')


def foto(sku, estilo):
    return f'<img src="../../productos/recortes/{sku}.png" style="{estilo};object-fit:contain">'


def banda(texto, fondo=ROJO, tam=46):
    return (f'<div style="background:{fondo};color:#fff;padding:28px 34px;font-family:Titular;font-weight:900;'
            f'font-size:{tam}px;line-height:1.08;letter-spacing:-.5px">{texto}</div>')


def wa(tam=40):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 32 32"><circle cx="16" cy="16" r="16" fill="#25D366"/>'
            f'<path d="M9 23l1.2-3.6A7.5 7.5 0 1 1 13 22Z" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg>')


def placas(g):
    # ---------- Historia 1: pregunta ----------
    h1 = f'''
<div class="pildora"><i></i>INDUSTRIA</div>
<h1 style="font-size:94px;margin-top:26px">¿Tu producción<br>necesita bulones,<br>tornillos y fijaciones<br><em>en cantidad?</em></h1>
<p class="bajada" style="font-size:42px">Sabemos que <b>un faltante frena<br>toda la línea.</b></p>
<div style="position:absolute;left:0;right:0;top:770px;height:360px">
  <div style="position:absolute;left:0;top:10px">{bulon(470)}</div>
  <div style="position:absolute;left:0;top:150px">{varilla(470)}</div>
  <div style="position:absolute;left:10px;top:215px;display:flex;gap:30px;align-items:center">{tuerca(110)}{arandela(100)}{foto("104070008", "width:190px")}</div>
  <div style="position:absolute;right:0;top:0;bottom:0;display:flex;align-items:center">{foto("14108012TEL", "height:320px")}</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0">{banda("Lo que buscás, lo tenemos.", tam=54)}</div>
'''

    # ---------- Historia 2: mix de productos ----------
    def tile(visual, nombre):
        return (f'<div style="border:3px solid #E4E4E4;display:flex;flex-direction:column">'
                f'<div style="flex:1;min-height:0;display:flex;align-items:center;justify-content:center;padding:14px">{visual}</div>'
                f'<div style="background:{NEGRO};color:#fff;font-family:Titular;font-weight:900;font-size:30px;letter-spacing:1px;'
                f'padding:14px 18px">{nombre}</div></div>')
    grilla = "".join([
        tile(bulon(270), "Bulones"),
        tile(foto("15108032TELEST", "max-height:230px;max-width:100%"), "Tornillos"),
        tile(tuerca(170), "Tuercas"),
        tile(arandela(170), "Arandelas"),
        tile(varilla(280, -20), "Varillas roscadas"),
        tile(foto("104070008", "max-width:100%;max-height:120px"), "Fijaciones"),
    ])
    h2 = f'''
<div class="pildora"><i></i>BULONERÍA</div>
<h1 style="font-size:96px;margin-top:26px">Elementos de fijación<br><em>para tu industria</em></h1>
<p class="bajada" style="font-size:36px"><b>Bulones, tornillos, tuercas, arandelas, varillas roscadas y fijaciones,</b> en todas las medidas y terminaciones.</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:16px;height:600px;margin-top:34px">{grilla}</div>
<p style="font-weight:600;font-size:32px;line-height:1.3;color:#555;margin-top:30px;border-left:10px solid {ROJO};padding-left:22px">
Para <b style="color:{NEGRO}">fábricas, metalúrgicas, constructoras,<br>talleres y montajes.</b></p>
'''

    # ---------- Historia 3: proveedor ----------
    puntos = [("Venta por cantidad", "y precios mayoristas"),
              ("Stock permanente", "para entregas continuas"),
              ("Te ayudamos a armar el pedido", "de tu obra o producción"),
              ("Envíos a todo el país", "")]
    filas = "".join(
        f'<div style="display:flex;gap:26px;align-items:baseline;padding:26px 0;border-bottom:3px solid {NEGRO}">'
        f'<span style="font-family:Titular;font-weight:900;font-size:46px;color:{ROJO};width:70px;flex:none">0{i}</span>'
        f'<span style="font-family:Titular;font-weight:700;font-size:44px;line-height:1.1">{a}'
        f'{"<br><span style=&quot;font-weight:600;color:#555;font-size:38px&quot;>" + b + "</span>" if b else ""}</span></div>'
        for i, (a, b) in enumerate(puntos, 1)).replace("&quot;", '"')
    h3 = f'''
<div class="pildora"><i></i>POR MAYOR</div>
<h1 style="font-size:96px;margin-top:26px">Tu proveedor<br>de fijaciones<br><em>para cada proyecto</em></h1>
<div style="display:flex;gap:20px;margin-top:20px">
  <div style="flex:1">{filas}</div>
</div>
<div style="position:absolute;right:0;top:250px">{foto("15108032TELEST", "height:210px")}</div>
<div style="position:absolute;left:0;right:0;bottom:0">{banda("Ahorrá tiempo, compralo<br>todo en un solo lugar.", NEGRO, 52)}</div>
'''

    # ---------- Historia 4: cotización + contacto ----------
    def sede(nombre, tel, dir_):
        return (f'<div style="padding:16px 0;border-top:3px solid #E4E4E4">'
                f'<div style="font-weight:700;font-size:24px;letter-spacing:3px;color:#777">{nombre}</div>'
                f'<div style="display:flex;align-items:center;gap:16px;margin-top:8px">{wa(52)}'
                f'<span style="font-family:Titular;font-weight:900;font-size:64px;letter-spacing:-1px;color:{ROJO}">{tel}</span></div>'
                f'<div style="font-weight:500;font-size:30px;color:#444;margin-top:6px">{dir_}</div></div>')
    h4 = f'''
<div class="pildora"><i></i>COTIZACIÓN</div>
<h1 style="font-size:116px;margin-top:22px">Cotizá tu<br><em>pedido hoy</em></h1>
<p class="bajada" style="font-size:40px">Mandanos tu <b>listado de medidas y cantidades,</b> y te respondemos con la cotización.</p>
<div style="display:flex;gap:30px;align-items:flex-start;margin-top:26px">
  <div style="flex:1">
    <div style="font-family:Titular;font-weight:900;font-size:42px">Escribinos por WhatsApp</div>
    <div style="display:flex;align-items:center;gap:18px;margin-top:14px">{wa(70)}<span style="font-family:Titular;font-weight:900;font-size:88px;letter-spacing:-2px;color:{ROJO}">351 227 2419</span></div>
    <div style="margin-top:22px;border-top:3px solid #E4E4E4">
      <div style="padding:14px 0;border-bottom:3px solid #E4E4E4"><span style="font-weight:700;font-size:24px;letter-spacing:3px;color:#777">CASA CENTRAL</span><br><span style="font-weight:600;font-size:32px">Domingo F. Sarmiento 365 - Córdoba</span></div>
      <div style="padding:14px 0"><span style="font-weight:700;font-size:24px;letter-spacing:3px;color:#777">SUCURSAL</span><br><span style="font-weight:600;font-size:32px">Blvd. de los Alemanes 5310 - Córdoba</span></div>
    </div>
  </div>
</div>
<div style="position:absolute;left:0;right:0;bottom:180px;display:flex;align-items:center;justify-content:space-between;padding-top:14px;border-top:3px solid #E4E4E4">{bulon(250)}{tuerca(100)}{arandela(90)}{foto("15108032TELEST", "height:130px")}{foto("104070008", "width:170px")}</div>
<div style="position:absolute;left:0;right:0;bottom:0">{banda("Atención exclusiva para<br>empresas y fabricantes.", ROJO, 50)}</div>
'''
    return [("blanca colores-marca", h1), ("blanca colores-marca", h2),
            ("blanca colores-marca", h3), ("blanca colores-marca", h4)]
