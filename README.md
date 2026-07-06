# Portfolio Web — Sebastián Rodríguez

Sitio de una sola página, autocontenido (imágenes en base64, sin dependencias externas).

## Estructura
- `template.html` — código fuente editable (con tokens `{{nombre}}` donde van las imágenes)
- `assets/` — imágenes ya recortadas/comprimidas para el sitio
- `build.py` — arma `dist/index.html` inyectando cada imagen de `assets/` en su token
- `dist/index.html` — archivo final, listo para desplegar

## Editar contenido o imágenes
1. Edita `template.html` (texto) o reemplaza el archivo correspondiente en `assets/`.
2. Corre `python build.py` desde esta carpeta.
3. Vuelve a desplegar `dist/`.

## Desplegar en Vercel
Opción CLI, desde esta carpeta:
```
vercel --prod
```
(usa `vercel.json`, que apunta a `dist/` como carpeta de salida — no requiere build ni framework)

Opción dashboard: arrastra la carpeta `dist/` a vercel.com/new, o conecta este repo y define
"Output Directory" = `dist` con "Framework Preset" = *Other*.
