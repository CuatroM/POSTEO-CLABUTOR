"""Historias — Todo para tu carpintería (contenido tal cual MARKETING PRODUCTOS CONTENIDO).
5 historias informativas, colores Clabutor. Fotos reales con stock: clavadora y engrampadora neumáticas DUCA
(800050, 800040), compresor DUCA silencioso 24 L (69370106), autoperforante Tel alas, taco Fischer SX 8,
caja Tel x 10.000. Bulones/tuercas/arandelas/varillas: ilustración (en la web no tienen foto).
Taller de carpintería: ilustración de tablas de madera (no hay foto del taller)."""

import importlib.util
from pathlib import Path

ID = "historia-carpinteria"
FORMATO = "historia"
CINTA = None
RUBRO = ""
TEXTO = ""
ROJO = "#E10600"
NEGRO = "#111111"

_spec = importlib.util.spec_from_file_location("fij", Path(__file__).with_name("historia-fijaciones.py"))
f = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(f)


def tablas(w=900, h=330):
    """Pila de tablas de madera con veta (el taller)."""
    colores = [("#C8955A", "#A9743F"), ("#D9A86C", "#B9844B"), ("#BE8A50", "#9C6B36"), ("#D4A064", "#B07C43")]
    filas = ""
    alto = h / 4
    for i, (c1, c2) in enumerate(colores):
        y = i * alto
        dx = [0, 40, 12, 60][i]
        vetas = "".join(
            f'<path d="M{dx+20} {y+alto*(.25+.17*k):.0f} C {w*.3:.0f} {y+alto*(.12+.2*k):.0f}, {w*.55:.0f} {y+alto*(.4+.15*k):.0f}, {w-20} {y+alto*(.22+.18*k):.0f}" '
            f'stroke="{c2}" stroke-width="3" fill="none" opacity=".7"/>' for k in range(4))
        nudo = f'<ellipse cx="{w*(.3+.15*i):.0f}" cy="{y+alto*.5:.0f}" rx="22" ry="9" fill="none" stroke="{c2}" stroke-width="4"/>'
        filas += (f'<rect x="{dx}" y="{y+3:.0f}" width="{w-dx-[30,0,50,10][i]}" height="{alto-6:.0f}" rx="4" fill="{c1}"/>'
                  f'{vetas}{nudo}<rect x="{dx}" y="{y+alto-10:.0f}" width="{w-dx-[30,0,50,10][i]}" height="5" fill="{c2}"/>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{filas}</svg>'


def foto(sku, estilo):
    return f'<img src="../../productos/recortes/{sku}.png" style="{estilo};object-fit:contain">'


def lista(items, tam=42):
    return "".join(
        f'<div style="display:flex;gap:22px;align-items:center;padding:20px 0;border-bottom:3px solid {NEGRO}">'
        f'<span style="width:18px;height:18px;background:{ROJO};flex:none"></span>'
        f'<span style="font-family:Titular;font-weight:700;font-size:{tam}px;line-height:1.1">{t}</span></div>' for t in items)


def placas(g):
    # 1 — Portada
    p1 = f'''
<div class="pildora"><i></i>CARPINTERÍA</div>
<h1 style="font-size:94px;margin-top:26px;white-space:nowrap">Todo para tu<br>carpintería,<br><em>en un solo lugar</em></h1>
<p class="bajada" style="font-size:40px"><b>Fijaciones, bulones y herramientas FEMA</b><br>para cada proyecto.</p>
<div style="position:absolute;left:0;right:0;bottom:0;height:560px">
  <div style="position:absolute;left:0;bottom:0">{tablas(900, 300)}</div>
  <div style="position:absolute;left:10px;bottom:250px">{foto("800050", "height:300px")}</div>
  <div style="position:absolute;right:0;bottom:240px">{foto("69370106", "height:330px")}</div>
</div>
'''

    # 2 — Fijaciones
    p2 = f'''
<div class="pildora"><i></i>FIJACIONES</div>
<h1 style="font-size:112px;margin-top:26px">Fijaciones<br><em>para madera</em></h1>
<div style="margin-top:20px">{lista(["Tornillos para madera y aglomerado", "Tornillos autoperforantes y tirafondos", "Tarugos y anclajes", "Clavos y grampas"], 40)}</div>
<div style="display:flex;align-items:flex-end;justify-content:space-between;height:330px;margin-top:20px">
  {foto("15108032TELEST", "height:300px")}{foto("104070008", "width:300px;margin-bottom:40px")}{foto("14108012TEL", "height:240px")}
</div>
<div style="position:absolute;left:0;right:0;bottom:0">{f.banda("Todas las medidas, por unidad<br>o por cantidad.", NEGRO, 48)}</div>
'''

    # 3 — Bulones
    p3 = f'''
<div class="pildora"><i></i>BULONERÍA</div>
<h1 style="font-size:104px;margin-top:26px">Bulones y<br><em>elementos<br>de unión</em></h1>
<div style="margin-top:20px">{lista(["Bulones, tuercas y arandelas", "Varillas roscadas", "Bulones para estructuras, decks y pérgolas"], 40)}</div>
<div style="position:relative;height:360px;margin-top:30px">
  <div style="position:absolute;left:0;top:20px">{f.bulon(560)}</div>
  <div style="position:absolute;left:0;top:170px">{f.varilla(560)}</div>
  <div style="position:absolute;right:10px;top:0">{f.tuerca(170)}</div>
  <div style="position:absolute;right:30px;top:200px">{f.arandela(140)}</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0">{f.banda("Stock para tu taller<br>y tus obras.", ROJO, 52)}</div>
'''

    # 4 — Herramientas FEMA
    p4 = f'''
<div class="pildora"><i></i>HERRAMIENTAS</div>
<h1 style="font-size:84px;margin-top:26px;white-space:nowrap">Herramientas FEMA<br><em>para carpinteros</em></h1>
<div style="margin-top:14px">{lista(["Sierras circulares e ingletadoras", "Taladros y atornilladores", "Caladoras, lijadoras y routers", "Compresores y clavadoras neumáticas"], 38)}</div>
<div style="display:flex;align-items:flex-end;justify-content:space-between;height:340px;margin-top:24px">
  {foto("800040", "max-width:29%;max-height:270px")}{foto("69370106", "max-width:38%;max-height:330px")}{foto("800050", "max-width:29%;max-height:270px")}
</div>
<div style="position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;gap:26px;background:{ROJO};color:#fff;padding:26px 34px">
  <span style="font-family:Titular;font-weight:900;font-size:110px;line-height:.85;letter-spacing:-4px">6</span>
  <span style="font-family:Titular;font-weight:900;font-size:46px;line-height:1.05">meses de<br>garantía FEMA</span>
</div>
'''

    # 5 — Cierre
    p5 = f'''
<div class="pildora"><i></i>CONTACTO</div>
<h1 style="font-size:84px;margin-top:26px;white-space:nowrap">Tu proveedor<br><em>para cada trabajo</em></h1>
<p class="bajada" style="font-size:40px">Precios para <b>carpinterías, mueblerías<br>y profesionales.</b></p>
<div style="margin-top:44px">
  <div style="font-family:Titular;font-weight:900;font-size:42px">Escribinos por WhatsApp</div>
  <div style="display:flex;align-items:center;gap:18px;margin-top:14px">{f.wa(70)}<span style="font-family:Titular;font-weight:900;font-size:88px;letter-spacing:-2px;color:{ROJO}">351 227 2419</span></div>
  <div style="margin-top:22px;border-top:3px solid #E4E4E4">
    <div style="padding:14px 0;border-bottom:3px solid #E4E4E4"><span style="font-weight:700;font-size:24px;letter-spacing:3px;color:#777">CASA CENTRAL</span><br><span style="font-weight:600;font-size:32px">Domingo F. Sarmiento 365 - Córdoba</span></div>
    <div style="padding:14px 0"><span style="font-weight:700;font-size:24px;letter-spacing:3px;color:#777">SUCURSAL</span><br><span style="font-weight:600;font-size:32px">Blvd. de los Alemanes 5310 - Córdoba</span></div>
  </div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0">{tablas(900, 230)}</div>
'''
    return [("blanca colores-marca", p) for p in (p1, p2, p3, p4, p5)]
