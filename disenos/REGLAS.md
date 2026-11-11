# Reglas de diseño y redacción — Clabutor (@clabutor.cba)

## Contenido
- Los contenidos se sacan siempre tal cual indica MARKETING PRODUCTOS CONTENIDO para la cuenta de Clabutor.

## Diseño (siempre constante)
- **Logo:** en el encabezado de posteos e historias va el logo oficial (`disenos/marca/clabutor-logo.png`), no la palabra CLABUTOR escrita.
- Mismo sistema para todos los posteos: `estilo.css` (fondo blanco, negro y rojo #E10600, tipografía Inter), placas JPG 1080×1350.
- Encabezado: marca CLABUTOR a la izquierda y rubro a la derecha.
- Pie: **www.clabutor.com.ar abajo a la izquierda** (no poner @clabutor.cba). Progreso de placas a la derecha.
- Fotos de producto en `productos/<SKU>.jpg`, recortadas al producto (sin margen blanco). Se descargan solas listando los SKU en `productos/pedido.txt`.

- Placas claras: **fondo blanco siempre**, nunca grises (vale para posteos e historias). Los fondos oscuros siguen igual.

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

## Historias (1080×1920)
- **Colores:** fuera de una campaña, las historias van con los colores de Clabutor (blanco, negro y rojo #E10600), igual que el muro: `fondo = "blanca colores-marca"` (o `"azul colores-marca"` para fondo negro), sin cinta. El azul oscuro y el naranja son SOLO para la campaña CyberMonday.
- Se arman con `FORMATO = "historia"` en el archivo de `posteos/`; el marco está en `generar.py` y el estilo en `historia.css` (misma tipografía Inter).
- Campaña CyberMonday: azul oscuro #0B1F3A + naranja #FF6A00, y cinta fija "CYBERMONDAY · 2·3·4 NOV" arriba en todas las piezas.
- La cinta va debajo de la barra de perfil de Instagram y el pie (www.clabutor.com.ar abajo a la izquierda) por encima de la zona de respuesta, para que nada quede tapado.
- Ofertas: una sola por placa, producto recortado, grande y sobre fondo liso; precio anterior tachado en gris y chico; precio cyber grande en naranja; debajo "12 cuotas" (clases `.precio-antes`, `.precio-cyber`, `.cuotas`).

- Historias de **producto**: sin la fila de barras de progreso (se pueden publicar en cualquier orden).
  Historias **informativas**: con barras, contando solo las informativas del set.

## Contacto (WhatsApp)
- Siempre los dos números, sin guiones y separados por espacios, con la dirección si hay lugar:
  - Casa central: 351 227 2419 · Domingo F. Sarmiento 365 - Córdoba
  - Sucursal: 351 227 2420 · Blvd. de los Alemanes 5310 - Córdoba
- En las placas, el producto tiene prioridad de tamaño sobre el bloque de contacto.

## Precios (productos FEMA con envío gratis)
- Precio = **costo + 35 % + envío**, donde envío = **10 % del costo, con un mínimo de $20.000**. Redondeado al peso.
  - Costo = el que informa la sincronización en BaseLinker (INVENTARIO COMPLETO FEMA 2026 MATIAS, grupo de precios 65271).
  - Se aplica en **todas** las piezas con envío gratis (historias y posteos), salvo que el contenido indique otro precio.
- Solo productos **con stock** y **con foto**. Para tener stock y costo al día, correr antes el export de BaseLinker (`bl_exportar.yml`, buscar "COMPLETO FEMA").
- Función lista para usar: `precio_envio_gratis(costo)` en `disenos/generar.py`.
