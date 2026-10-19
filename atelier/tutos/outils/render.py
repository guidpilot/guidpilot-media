"""Rend une capture HTML de GuidPilot (prise dans le navigateur intégré) en PNG haute définition.

Usage : python3 render.py <snap.html> <sortie.png> [--scale 2]
La page est rendue avec son vrai contenu et son vrai CSS ; seules les polices sont remplacées par
les mêmes familles (Inter, Manrope, Sora) installées localement, car le bac à sable n'accède pas à guidpilot.fr.
render() peut aussi renvoyer la position d'éléments (sélecteurs Playwright) pour les zooms du montage.
"""
import json, pathlib, re, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FS = HERE / "node_modules" / "@fontsource"
EXT = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,"
       "U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")


def font_faces():
    css = []
    for fam, key in (("Inter", "inter"), ("Manrope", "manrope"), ("Sora", "sora")):
        for w in (300, 400, 500, 600, 700, 800):
            f = FS / key / "files" / f"{key}-latin-{w}-normal.woff2"
            if f.exists():
                css.append(f"@font-face{{font-family:{fam};font-weight:{w};font-style:normal;src:url('file://{f}') format('woff2')}}")
            fe = FS / key / "files" / f"{key}-latin-ext-{w}-normal.woff2"
            if fe.exists():
                css.append(f"@font-face{{font-family:{fam};font-weight:{w};font-style:normal;src:url('file://{fe}') format('woff2');unicode-range:{EXT}}}")
    return "\n".join(css)


def prepare(html):
    html = re.sub(r"@font-face\s*\{[^}]*\}", "", html)
    html = html.replace('loading="lazy"', '')
    # Champs date / heure : affichage français (le Chromium de rendu est en anglais)
    def _fr(m):
        tag = m.group(0)
        t = re.search(r'type="(date|time)"', tag).group(1)
        v = re.search(r'value="([^"]*)"', tag)
        val = v.group(1) if v else ""
        if t == "date":
            shown = "/".join(reversed(val.split("-"))) if val else "jj/mm/aaaa"
        else:
            shown = val[:5] if val else "--:--"
        tag = re.sub(r'type="(date|time)"', 'type="text"', tag)
        tag = re.sub(r'\svalue="[^"]*"', "", tag)
        return tag[:-1] + f' value="{shown}">' if tag.endswith(">") else tag
    html = re.sub(r'<input[^>]*type="(?:date|time)"[^>]*>', _fr, html)
    return html.replace("</head>", f"<style id='gpfonts'>{font_faces()}</style>"
                        "<style>*{transition:none!important;animation:none!important;caret-color:transparent}"
                        "[data-sonner-toaster]{display:none}</style></head>", 1)


def meta_of(src):
    html = pathlib.Path(src).read_text()
    return json.loads(re.search(r"<!--GPSNAP (\{.*?\})-->", html).group(1))


def render(src, out, scale=2.0, rects=None):
    src = pathlib.Path(src).resolve()
    html = src.read_text()
    meta = json.loads(re.search(r"<!--GPSNAP (\{.*?\})-->", html).group(1))
    tmp = src.with_name(src.stem + ".prep.html")
    tmp.write_text(prepare(html))
    found = {}
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--lang=fr-FR"])
        pg = b.new_page(viewport={"width": meta["w"], "height": meta["h"]}, device_scale_factor=scale, locale="fr-FR", timezone_id="Europe/Paris")
        pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith(("file:", "data:")) else r.abort())
        pg.goto(f"file://{tmp}")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        if meta.get("scrollY"):
            pg.evaluate(f"window.scrollTo(0,{meta['scrollY']})")
        if meta.get("dlgTop"):
            pg.evaluate(f"(()=>{{const d=document.querySelector('[role=dialog]'); if(d) d.scrollTop={meta['dlgTop']};}})()")
        pg.wait_for_timeout(150)
        for key, sel in (rects or {}).items():
            try:
                found[key] = pg.locator(sel).first.bounding_box(timeout=1500)
            except Exception:
                found[key] = None
        if out:
            pg.screenshot(path=str(out))
        b.close()
    meta["rects"] = found
    return meta


if __name__ == "__main__":
    a = sys.argv[1:]
    scale = float(a[a.index("--scale") + 1]) if "--scale" in a else 2.0
    print(render(a[0], a[1], scale=scale))
