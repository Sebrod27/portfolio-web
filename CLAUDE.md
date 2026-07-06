# CLAUDE.md — Portfolio Web (Sebastián Rodríguez)

Portafolio de una sola página para mostrar a clientes/prospectos. Dueño: **Sebastián
Rodríguez**. Comunicar en **español**.

## Qué es
Sitio autocontenido (imágenes en base64, sin dependencias externas) con 5 casos de
estudio: MOLT, Moraich, LoreFlorez, Alta Studio (+ Luciano Parra), y Acelera Talent
(mención sin logo). Incluye secciones de Servicios y Habilidades (logos de tecnologías).
Marca personal: monograma "SR" + wordmark, tomados de
`C:\Sebas_AI\Cotizaciones_Sebastian\Assets\Logos`.

## Estructura
- `template.html` — fuente editable, con tokens `{{nombre}}` donde van las imágenes.
- `assets/` — imágenes ya recortadas/comprimidas.
- `build.py` — inyecta cada imagen de `assets/` en su token → genera `dist/index.html`.
- `dist/index.html` — archivo final, autocontenido, listo para servir o desplegar.
- `vercel.json` — apunta a `dist/` como output para despliegue estático.

## Flujo de trabajo
1. Editar `template.html` (texto/estructura) o reemplazar el archivo en `assets/`.
2. Correr `python build.py` desde esta carpeta.
3. Ver en local: `cd dist && python -m http.server 5500` → http://localhost:5500
4. Desplegar: `vercel --prod` desde esta carpeta (usa `vercel.json`).

## Diseño (tokens, en `template.html`)
Tema **claro único** (sin modo oscuro) — papel cálido casi blanco, tinta casi negra y un
acento índigo vivo (`--accent: #3242E0`), con un bloque de contacto a todo color en ese
mismo acento como único punto de alto contraste (nunca oscuro). Tipografía self-hosted
(woff2 embebido en base64, sin llamadas externas): **IBM Plex Sans** en bold para
titulares y cuerpo (`--font-display` y `--font-body` apuntan a la misma familia — el
cliente pidió tipografía plana sans-serif, sin serif editorial), **IBM Plex Mono** para
cifras/etiquetas (`--font-mono`). Nav superior sticky con scrollspy. Motivo recurrente:
marcas de esquina tipo plano técnico (`.spec`) en cada imagen de evidencia, y "plates"
(`.plate`) para los logos de cliente — logos de MOLT y Alta Studio ya vienen con fondo
recortado a transparente (`*_t.png`), igual que el monograma y el wordmark.

## Pendiente
- Nada bloqueante por ahora. Moraich ya tiene link a `mei-moraich.com` y screenshots
  reales (landing + chat de MEI + dashboard). LoreFlorez ya tiene capturas reales del
  chat interno y el dashboard (solo interfaz y cifras agregadas, sin datos puntuales de
  clientes, por tratarse de salud mental).
- Si llegan más assets a futuro: guardarlos en `assets/`, añadir su token en
  `build.py` (`TOKEN_FILES`), referenciarlo en `template.html`, y volver a correr
  `python build.py`.

## Contacto usado en el footer
sebasrod27@gmail.com · +57 321 405 6649 (WhatsApp). Sin link a LinkedIn (el cliente
pidió quitarlo).
