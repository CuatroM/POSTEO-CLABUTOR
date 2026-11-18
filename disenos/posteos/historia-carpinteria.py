"""Historias — Carpinterías y fábricas de muebles (contenido tal cual MARKETING PRODUCTOS CONTENIDO, v2).
5 historias informativas, colores Clabutor. Fotos de ambiente provistas por el cliente (taller y tornillos en madera).
Productos con foto real y stock:
- clabutor.com.ar: autoperforante Tel alas (15108032TELEST), taco Fischer SX 8 (104070008), caja Tel x 10.000 (14108012TEL)
- FEMA (Drive): taladro de banco 13 mm (69330110), compresor FEMA 2 HP 25 L (69370206), compresor DUCA silencioso
  (69370100), clavadora neumática DUCA (800050), engrampadora neumática DUCA (800040)
Historia 4 (sin repetir productos de las otras): Bosch GSB 183-LI, GBH 2-28 D, GSR 7-14 E, GST 75 E y GSB 450 RE
(fotos de bosch-professional.com/ar), compresor DUCA a correa 180 L (69370029), clavadora de bobina DUCA (800060),
engrampadora DUCA (800416), martillo bolita y destornillador Vanguard. Sin sierras circulares, ingletadoras ni lijadoras
(FEMA no las tiene con stock).
Historia 3: los bulones de clabutor.com.ar no tienen foto -> va la foto del taller, sin productos."""

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


def foto(sku, estilo):
    return f'<img src="../../productos/recortes/{sku}.png" style="{estilo};object-fit:contain">'


def ambiente(nombre, alto, pos="center"):
    return (f'<div style="height:{alto}px;overflow:hidden;margin-top:30px">'
            f'<img src="../../fotos/{nombre}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};display:block"></div>')


def fila(*imgs, alto=300):
    return (f'<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:16px;height:{alto}px;margin-top:24px">'
            + "".join(imgs) + '</div>')


def placas(g):
    p1 = f'''
<div class="pildora"><i></i>CARPINTERÍAS</div>
<h1 style="font-size:84px;margin-top:26px;white-space:nowrap">¿Tenés una<br>carpintería o una<br><em>fábrica de muebles?</em></h1>
<p class="bajada" style="font-size:40px">Somos tu proveedor de insumos<br><b>para producir sin frenar.</b></p>
{ambiente("taller-a.jpg", 400)}
{fila(foto("14614050PC", "max-width:24%;max-height:200px"), foto("69330110", "max-width:16%;max-height:280px"),
      foto("69370206", "max-width:26%;max-height:220px"), foto("69440103", "max-width:26%;max-height:220px"), alto=280)}
'''

    p2 = f'''
<div class="pildora"><i></i>FIJACIONES</div>
<h1 style="font-size:86px;margin-top:26px;white-space:nowrap">Fijaciones<br><em>para tu producción</em></h1>
<p class="bajada" style="font-size:36px"><b>Tornillos para madera y aglomerado, autoperforantes, tirafondos, tarugos y clavos,</b> en todas las medidas y por cantidad.</p>
{ambiente("tornillos-a.jpg", 420, "center 40%")}
{fila(foto("14706025TEL", "max-width:24%;max-height:220px"), foto("15108032TELEST", "max-width:24%;max-height:260px"),
      foto("104070006", "max-width:22%;max-height:200px"), foto("14110025TELEST", "max-width:24%;max-height:260px"), alto=280)}
'''

    p3 = f'''
<div class="pildora"><i></i>BULONERÍA</div>
<h1 style="font-size:82px;margin-top:26px;white-space:nowrap">Bulones y<br><em>elementos de unión</em></h1>
<p class="bajada" style="font-size:38px"><b>Bulones, tuercas, arandelas y varillas roscadas</b><br>para estructuras, muebles y montajes.</p>
{ambiente("taller-b.jpg", 700, "center")}
'''

    p4 = f'''
<div class="pildora"><i></i>HERRAMIENTAS</div>
<h1 style="font-size:82px;margin-top:26px;white-space:nowrap">Herramientas FEMA<br><em>para el taller</em></h1>
<p class="bajada" style="font-size:36px"><b>Taladros, perforadoras, atornilladores, caladoras,</b> compresores, clavadoras neumáticas y herramientas manuales.</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:repeat(3,215px);gap:14px;margin-top:30px">
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("06019K91E6-000", "max-height:100%;max-width:100%")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("06112673H0-000", "max-height:100%;max-width:100%")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("06014470H0-000", "max-height:100%;max-width:100%")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("060158H0H0-000", "max-height:100%;max-width:100%")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("06011B50H0-000", "max-height:100%;max-width:100%")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("69370029", "max-height:100%;max-width:100%")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("800060", "max-height:100%;max-width:100%")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("800416", "max-height:100%;max-width:100%")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:6px;border:3px solid #E4E4E4;padding:12px;min-height:0">{foto("69411150", "max-height:100%;max-width:55%")}{foto("69435565", "max-height:100%;max-width:40%")}</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;gap:26px;background:{ROJO};color:#fff;padding:22px 34px">
  <span style="font-family:Titular;font-weight:900;font-size:104px;line-height:.85;letter-spacing:-4px">6</span>
  <span style="font-family:Titular;font-weight:900;font-size:46px;line-height:1.05">meses de<br>garantía</span>
</div>
'''

    p5 = f'''
<div class="pildora"><i></i>CONTACTO</div>
<h1 style="font-size:92px;margin-top:26px;white-space:nowrap">Abastecemos<br><em>a tu carpintería</em></h1>
<p class="bajada" style="font-size:38px">Precios por cantidad para <b>carpinterías<br>y fabricantes de muebles.</b></p>
<div style="margin-top:34px">
  <div style="font-family:Titular;font-weight:900;font-size:40px">Escribinos por WhatsApp</div>
  <div style="display:flex;align-items:center;gap:18px;margin-top:10px">{f.wa(66)}<span style="font-family:Titular;font-weight:900;font-size:84px;letter-spacing:-2px;color:{ROJO}">351 227 2419</span></div>
  <div style="margin-top:18px;border-top:3px solid #E4E4E4">
    <div style="padding:12px 0;border-bottom:3px solid #E4E4E4"><span style="font-weight:700;font-size:22px;letter-spacing:3px;color:#777">CASA CENTRAL</span><br><span style="font-weight:600;font-size:30px">Domingo F. Sarmiento 365 - Córdoba</span></div>
    <div style="padding:12px 0"><span style="font-weight:700;font-size:22px;letter-spacing:3px;color:#777">SUCURSAL</span><br><span style="font-weight:600;font-size:30px">Blvd. de los Alemanes 5310 - Córdoba</span></div>
  </div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:400px;overflow:hidden"><img src="../../fotos/tornillos-b.jpg" style="width:100%;height:100%;object-fit:cover;object-position:center 70%;display:block"></div>
'''
    return [("blanca colores-marca", p) for p in (p1, p2, p3, p4, p5)]
