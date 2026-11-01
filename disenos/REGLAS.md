# Reglas de diseño y redacción — Clabutor (@clabutor.cba)

## Contenido
- Los contenidos se sacan siempre tal cual indica MARKETING PRODUCTOS CONTENIDO para la cuenta de Clabutor.

## Diseño (siempre constante)
- Mismo sistema para todos los posteos: `estilo.css` (fondo blanco, negro y rojo #E10600, tipografía Inter), placas JPG 1080×1350.
- Encabezado: marca CLABUTOR a la izquierda y rubro a la derecha.
- Pie: **www.clabutor.com.ar abajo a la izquierda** (no poner @clabutor.cba). Progreso de placas a la derecha.
- Fotos de producto en `productos/<SKU>.jpg`, recortadas al producto (sin margen blanco). Se descargan solas listando los SKU en `productos/pedido.txt`.

## Redacción
- No repetir el mismo tema en una placa: si la volanta dice "Todo el país", la bajada no repite "envíos a todo el país" (usar otra cosa, p. ej. "Retiro en sucursal o entrega a domicilio").
- No repetir el link de la web dentro de la placa, porque ya está en el pie. Solo va en el cuerpo si es el título principal o una referencia tipo "Visitá nuestra web" / "Mirá lo que tenemos para vos en la web".
- Nada de palabras solas en un renglón. Cortar por frase u oración completa, con `<br>` donde haga falta:

      Casa central y sucursal en Córdoba.
      Envíos a todo el país.

  y no:

      Casa central y sucursal en
      Córdoba. Envíos a todo el
      país.

- Revisar siempre el render antes de publicar para confirmar que ningún renglón quede con una palabra suelta ni que nada se superponga.
