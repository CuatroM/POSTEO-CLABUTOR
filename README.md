# Posteo automático en Instagram

Publica en Instagram, por la API oficial de Meta, los posts que se cargan en la carpeta `posts/`.

## Cómo cargar un post

1. Dentro de `posts/` creá una carpeta por post. Empezá el nombre con la fecha a partir de la cual se puede publicar, por ejemplo `2026-11-03-amoladora`.
2. Adentro poné:
   - **Post simple:** una imagen `.jpg`.
   - **Carrusel:** de 2 a 10 imágenes `.jpg`, que se publican en orden alfabético (`1.jpg`, `2.jpg`, ...).
   - **Reel:** un video `.mp4`.
   - **Historias:** si el nombre de la carpeta contiene `historia`, cada `.jpg` (1080×1920) se publica como historia, en orden (no lleva `texto.txt`).
   - **`texto.txt`:** el texto del post con los hashtags (máximo 2200 caracteres).
3. Hacé commit. Listo.

Las carpetas que empiezan con `_` se ignoran (ahí está el ejemplo). Las ya publicadas quedan anotadas en `publicados.txt`.

Las imágenes tienen que ser **JPG**. Instagram acepta formatos de 4:5 (vertical, el recomendado: 1080×1350), 1:1 (1080×1080) o 1.91:1 (horizontal).

## Cuándo publica

- **Automático:** lunes, miércoles y viernes a las 10:00 (Argentina), un post por vez. GitHub puede demorarlo unos minutos.
- **A mano:** en la pestaña *Actions* → *Publicar en Instagram* → *Run workflow*. Si escribís el nombre de una carpeta, publica esa; si lo dejás vacío, publica la próxima pendiente.

## Secretos necesarios

En *Settings → Secrets and variables → Actions*:

| Nombre | Valor |
| --- | --- |
| `IG_TOKEN` | Token de Instagram generado en la app de Meta |
| `IG_USER_ID` | Número de la cuenta de Instagram |
| `GH_PAT` | Token de GitHub con permiso *Secrets: Read and write* sobre este repo (para renovar `IG_TOKEN`) |

El token de Instagram vence a los 60 días. El proceso *Renovar token de Instagram* lo renueva solo el día 1 de cada mes.
