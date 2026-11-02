"""Historias CyberMonday — ofertas FEMA (mismo diseño que las placas 5 a 7 de "Arrancó el CyberMonday").
Precio = costo informado por la sincronización (BaseLinker, INVENTARIO COMPLETO FEMA 2026 MATIAS,
grupo 65271) + 35 %, redondeado al peso. Envío gratis a todo el país. Solo productos con stock y con foto
(el motor B&S 69367162 quedó afuera: no hay foto en las webs ni en Drive)."""

import importlib.util
from pathlib import Path

ID = "historia-cyber-d-ofertas-fema"
FORMATO = "historia"
CINTA = "cyber"
RUBRO = ""
TEXTO = ""
MARGEN = 1.35

_spec = importlib.util.spec_from_file_location("cyber_c", Path(__file__).with_name("historia-cyber-c.py"))
_c = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c)

# sku de la foto, sku que se muestra, nombre, costo BaseLinker, título comercial
OFERTAS = [
    ("69439916", "69439916", "Tablero de herramientas 34 piezas Vanguard", 45999.36,
     "Tu taller,<br><em>siempre en orden</em>"),
    ("69381380", "69381380", "Cargador de baterías Duca 12/24 V 0,3 kW", 105705.6,
     "Batería a full,<br><em>siempre lista</em>"),
    ("69370029", "69370029", "Compresor Duca Pro 180 L 3 HP 220 V", 723465.6,
     "Aire de sobra<br><em>para trabajar</em>"),
    ("69510412", "69510412", "Alisadora de cemento 900 mm motor 7 HP", 1009757.84,
     "Pisos perfectos<br><em>a otro nivel</em>"),
    ("69370211", "69370211", "Compresor Fema 120 L 2,5 HP 220 V", 328962.92,
     "El compresor<br><em>que rinde todo</em>"),
    ("69502230-1", "69502230-1", "Carretilla Fema doble rueda 65 L 150 kg", 73540.74,
     "Cargá más,<br><em>cansate menos</em>"),
    ("69500950", "69500950", "Escalera dieléctrica doble 12 peldaños 3,66 m", 433253.37,
     "Llegá alto<br><em>con seguridad</em>"),
    ("57071804", "57071804", "Manguera de riego 1/2\" 25 m", 9614.18,
     "Tu jardín,<br><em>siempre verde</em>"),
    ("69360062", "69360062", "Electrobomba centrífuga Fema DFC158 1 HP", 108416,
     "Agua con presión<br><em>en toda la casa</em>"),
    ("69501210", "69501210 + 69501232", "Andamio galvanizado 1219 × 1700 + plataforma", 128114.8 + 68017.49,
     "Andamio listo<br><em>con plataforma</em>"),
    ("69510058", "69510058", "Hormigonera Fema 200 L 800 W volteo", 573362.4,
     "Mezclá más<br><em>en menos tiempo</em>"),
    ("69501490", "69501490", "Set 2 rampas de acero 680 kg", 237256.8,
     "Subí la moto<br><em>sin esfuerzo</em>"),
]


def placas(g):
    salida = []
    for foto, sku, nombre, costo, titulo in OFERTAS:
        # Solo los que ya tienen foto recortada; los demás se suman cuando llegue la foto.
        if not (g.AQUI / "productos" / "recortes" / f"{foto}.png").exists():
            print(f"Sin foto todavía: {sku} {nombre}")
            continue
        html = _c.placa_oferta(g, foto, nombre, None, round(costo * MARGEN), titulo, True)
        html = html.replace(f"COD. {g.e(foto)}", f"COD. {g.e(sku)}")
        salida.append(("azul", html))
    return salida
