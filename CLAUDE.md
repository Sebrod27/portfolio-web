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

## Cómo agregar una nueva empresa / caso de estudio
Checklist completo — toca 4 lugares en `template.html` más `build.py`. Usa el caso de
MOLT (`id="molt"`) como plantilla más simple para copiar/pegar.

1. **Logo.** Si el logo del cliente trae fondo blanco/sólido, quítaselo antes de usarlo
   (fondo transparente se ve mucho mejor en `.plate` y en la barra de confianza). Script
   rápido con PIL: abrir la imagen, calcular distancia de color al fondo, y convertir esa
   distancia en canal alfa (ver commits de `molt_logo_t.png` / `alta_logo_t.png` para el
   patrón exacto). Si el logo ya es un PNG transparente (como el de Moraich o el de
   LoreFlorez), no hace falta tocarlo.
2. **Screenshots de evidencia.** Comprimir a JPG (~80-90 quality, max ~1400px de ancho)
   antes de meterlos — los PNG crudos de captura de pantalla pesan cientos de KB a veces
   más de 1MB. **Antes de usar cualquier screenshot de un cliente, revisar la imagen
   completa por datos sensibles** (nombres reales de personas, en particular si el
   cliente maneja datos de salud/terapia — ver el caso de LoreFlorez/Obsidian: una
   captura de grafo de Obsidian traía nombres reales de pacientes y tuvo que difuminarse
   antes de publicarse). Ante la duda, preguntar antes de subir.
3. **`build.py`** — agregar una entrada en `TOKEN_FILES` por cada imagen nueva:
   ```python
   "nuevaempresa_logo": "nuevaempresa_logo_t.png",
   "nuevaempresa_evidencia1": "nuevaempresa_evidencia1.jpg",
   ```
4. **Barra de confianza** (`.trust-track`, cerca del `<header class="hero">`) — el logo
   aparece **dos veces** (el set normal + el set duplicado con `aria-hidden="true"` que
   permite el loop infinito del marquee). Agregar el `<img>` en ambos sets:
   ```html
   <img src="{{nuevaempresa_logo}}" alt="Nueva Empresa">
   ...
   <img src="{{nuevaempresa_logo}}" alt="" aria-hidden="true">
   ```
5. **Índice de proyectos** (`.index-list`, sección `id="proyectos"`) — agregar una fila:
   ```html
   <a class="index-item reveal" href="#nuevaempresa"><span class="ref">AT/XXXX</span><span class="name">Nueva Empresa</span><span class="desc">Descripción corta del proyecto</span></a>
   ```
6. **Sección del caso** — copiar un `<section class="case reveal" id="...">` completo
   (MOLT es el más simple) y adaptar. Estructura exacta, con el patrón de evidencia
   plegable para mobile (**obligatorio** — sin esto las fotos se ven apretadas y
   diminutas en celular):
   ```html
   <section class="case reveal" id="nuevaempresa" data-label="Nueva Empresa">
     <div class="wrap case-grid">
       <div class="case-meta">
         <div class="plate"><img src="{{nuevaempresa_logo}}" alt="Nueva Empresa"></div>
         <div class="meta-list">
           <div><b>Cliente</b><br>Nueva Empresa</div>
           <div><b>Sector</b><br>...</div>
           <div><b>Rol</b><br>...</div>
           <div class="status"><span class="dot"></span><b>Activo</b> — ...</div>
         </div>
         <div class="tags"><span class="tag">...</span></div>
       </div>
       <div class="case-body">
         <h2>Titular del caso (la frase gancho).</h2>
         <p>Párrafo largo explicando el problema y la solución.</p>
         <button class="evidence-toggle" type="button" data-target="ev-nuevaempresa" aria-expanded="false"><span class="label">Ver evidencia</span><span class="chev">⌄</span></button>
         <div class="evidence-group" id="ev-nuevaempresa">
           <div class="evidence-row cols-2">
             <figure class="spec"><img src="{{nuevaempresa_evidencia1}}" alt="..."><figcaption>Pie de foto</figcaption></figure>
           </div>
         </div>
       </div>
     </div>
   </section>
   ```
   - El botón `.evidence-toggle` + wrapper `.evidence-group` son los que activan el
     acordeón "Ver evidencia (N fotos)" en mobile (el JS cuenta las `<img>` dentro del
     grupo solo). En desktop el botón queda oculto (`display:none`) y el grupo se ve
     siempre expandido — no se necesita nada adicional para que funcione en ambos.
   - `.evidence-row` puede llevar `cols-2`, `cols-3`, `cols-lg-sm` (2fr/1fr, para
     destacar una imagen grande junto a una chica), o `style="grid-template-columns: 1fr;"`
     para una sola imagen a todo ancho.
   - Si hay carruseles estilo Instagram (como en Alta Studio), van dentro del mismo
     `.evidence-group` usando `.carousel-block` — copiar ese patrón de la sección de
     Alta Studio, cambiando los IDs (`carousel-1`, `carousel-2`, etc. deben ser únicos
     en toda la página).
   - Si el caso no tiene suficientes fotos como para justificar el acordeón (ej. una
     sola imagen), igual se recomienda envolverla en `.evidence-toggle`/`.evidence-group`
     por consistencia visual entre casos — es lo que se hizo hasta con Acelera Talent.
7. **Rol de fundador vs. cliente:** si es un proyecto propio (como Acelera Talent, sin
   logo de cliente externo), usar `<section class="venture reveal" ...>` en vez de
   `class="case reveal"`, y en el `.plate` usar `<span class="initials">Nombre</span>`
   en vez de una imagen (mismo patrón que LoreFlorez usaba antes de tener logo).
8. **Compilar y verificar:**
   ```
   python build.py
   cd dist && python -m http.server 5500
   ```
   Revisar tanto en ventana ancha (desktop) como angosta (<390px, o achicando la ventana)
   — el sitio no tiene breakpoints intermedios raros, pero el acordeón de evidencia solo
   se activa por debajo de 720px, así que hay que probar ahí específicamente.
9. **Deploy:** el dueño hace `git add -A && git commit` y deploy manual a Vercel — no
   hacerlo automáticamente sin que lo pida explícitamente.

### Gotchas de flexbox que ya mordieron una vez (no repetir)
- El sitio tiene una regla global `* { min-width: 0; }` para permitir que los elementos
  flex se encojan (necesario para que texto largo haga wrap y las imágenes no rompan el
  ancho de la página en Safari/iOS). Como efecto secundario, **cualquier imagen dentro de
  un contenedor `display:flex` necesita `flex-shrink: 0` si tiene una dimensión fija**
  (como `.trust-logos img { height: 22px; flex-shrink: 0; }`) — si no, Safari puede
  comprimir el ancho de la imagen mientras la altura queda fija, distorsionando el logo.
- Si un elemento hijo de un flex container necesita competir por espacio con otro
  (como pasó con `.trust-label` vs `.trust-logos`), cuidado con darle `flex-grow` — eso
  le quita espacio al otro. Casi siempre se quiere `flex-grow: 0` en el elemento de texto
  y dejar que el contenido "importante" (logos, imágenes) tenga el `flex: 1` que absorbe
  el espacio sobrante.

## Contacto usado en el footer
sebasrod27@gmail.com · +57 321 405 6649 (WhatsApp). Sin link a LinkedIn (el cliente
pidió quitarlo).
