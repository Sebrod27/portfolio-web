import base64
import mimetypes
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
TEMPLATE = os.path.join(ROOT, "template.html")
DIST = os.path.join(ROOT, "dist")
OUT = os.path.join(DIST, "index.html")

MIME_OVERRIDES = {
    ".woff2": "font/woff2",
}

TOKEN_FILES = {
    "mark": "mark_light_t.png",
    "favicon": "favicon.png",
    "molt_logo": "molt_logo_t.png",
    "molt_before": "molt_before.jpg",
    "molt_after": "molt_after.jpg",
    "moraich_logo": "moraich_logo.png",
    "loreflorez_logo": "loreflorez_logo.png",
    "landing_moraich": "landing_moraich.jpg",
    "mei_chat": "MEI1.jpg",
    "mei_dashboard": "MEI_dashboard.jpg",
    "alta_logo": "alta_logo_t.png",
    "alta_hero": "alta_hero.jpg",
    "foto_sebastian": "foto_sebastian_crop.jpg",
    "carousel1_1": "carousel1_1.jpg",
    "carousel1_2": "carousel1_2.jpg",
    "carousel1_3": "carousel1_3.jpg",
    "carousel1_4": "carousel1_4.jpg",
    "carousel2_1": "carousel2_1.jpg",
    "carousel2_2": "carousel2_2.jpg",
    "carousel2_3": "carousel2_3.jpg",
    "loreflorez_chat": "Loreflorez_pagina1.jpg",
    "loreflorez_dashboard": "loreflorez_dashboard.jpg",
    "n8n_altastudio": "n8n_altastudio.jpg",
    "manychat_altastudio": "manychat_altastudio.jpg",
    "obsidian_acelera": "obsidian_acelera_crm.jpg",
    "obsidian_loreflorez": "obsidian_loreflorez_final.jpg",
    "font_plexsans": "fonts/plexsans.woff2",
    "font_plexmono400": "fonts/plexmono400.woff2",
    "font_plexmono500": "fonts/plexmono500.woff2",
}


def data_uri(path):
    ext = os.path.splitext(path)[1].lower()
    mime = MIME_OVERRIDES.get(ext) or mimetypes.guess_type(path)[0]
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def main():
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        html = f.read()

    total = 0
    for token, filename in TOKEN_FILES.items():
        path = os.path.join(ASSETS, filename)
        if not os.path.exists(path):
            print(f"WARNING: missing asset for token {{{{{token}}}}}: {path}")
            continue
        uri = data_uri(path)
        total += len(uri)
        pattern = "{{" + token + "}}"
        count = html.count(pattern)
        if count == 0:
            print(f"NOTE: token {token} not used in template")
        html = html.replace(pattern, uri)

    leftover = re.findall(r"\{\{[a-zA-Z0-9_]+\}\}", html)
    if leftover:
        print("WARNING: unresolved tokens remain:", set(leftover))

    os.makedirs(DIST, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Built {OUT} ({os.path.getsize(OUT)/1024:.0f} KB, images+fonts ~{total/1024:.0f} KB base64)")


if __name__ == "__main__":
    main()
