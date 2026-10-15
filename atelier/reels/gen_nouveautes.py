"""Reel ANNONCE nouveautés (15/10/2026) : cartes cadeaux, forfaits, chèque/espèces, livre des recettes, logo.
Ligne V2 : accroche lisible dès la frame 0, 20–30 s, fin courte. Réutilise gen_v2.py + une scène « gift » (carte cadeau dessinée).
Usage : python3 reels/gen_nouveautes.py <voix.wav> → build/nouveautes-cartes-cadeaux/
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_v2 as g

GIFT_CSS = """
.gcard{width:900px;height:540px;border-radius:40px;background:#0F172A;border:4px solid #E9C46A;position:relative;text-align:left;padding:56px 60px;box-shadow:0 30px 80px rgba(15,23,42,.25)}
.gcard .lg{width:120px;height:120px;border-radius:50%;border:3px dashed #E9C46A;color:#E9C46A;font-weight:700;font-size:24px;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.1}
.gcard .k{position:absolute;top:70px;right:60px;font-weight:800;font-size:30px;letter-spacing:.14em;color:#E9C46A}
.gcard .for{margin-top:46px;font-weight:600;font-size:38px;color:#94A3B8}
.gcard .nm{font-weight:800;font-size:76px;color:#fff;margin-top:6px}
.gcard .msg{margin-top:18px;font-weight:600;font-size:38px;color:#CBD5E1;font-style:italic}
.gcard .code{position:absolute;bottom:50px;right:60px;font-weight:700;font-size:30px;color:#64748B;letter-spacing:.1em}
.gsub{margin-top:50px;font-weight:700;font-size:46px;color:#0F172A;width:900px;line-height:1.3}
.illu2{margin-top:24px;font-weight:600;font-size:28px;color:#94A3B8;letter-spacing:.06em}
"""

_scene = g.scene

def scene(i, sc, t0, t1):
    if sc["k"] != "gift":
        return _scene(i, sc, t0, t1)
    sid = f"s{i}"; d = round(t1 - t0, 2)
    body = f'''<div class="center" style="top:300px"><div class="tag" id="{sid}n">🎁 NOUVEAU</div>
<div class="stitle" id="{sid}t" style="margin-top:30px;font-size:88px">Les <span>cartes cadeaux</span></div></div>
<div class="center" style="top:720px"><div class="gcard" id="{sid}c"><div class="lg">Votre<br>logo</div><div class="k">CARTE CADEAU</div>
<div class="for">Pour</div><div class="nm">Sophie</div><div class="msg">« Un moment rien que pour vous »</div><div class="code">CODE · ••••-••••</div></div>
<div class="gsub" id="{sid}s">Sur votre page ou vendue au cabinet</div><div class="illu2">ILLUSTRATION</div></div>'''
    js = "\n".join([
        f'tl.fromTo("#{sid}n",{{opacity:0,y:-30}},{{opacity:1,y:0,duration:.4,ease:E}},{round(t0+.05,2)});',
        f'tl.fromTo("#{sid}t",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.45,ease:E}},{round(t0+.18,2)});',
        f'tl.fromTo("#{sid}c",{{opacity:0,y:80,rotation:-4,scale:.9}},{{opacity:1,y:0,rotation:0,scale:1,duration:.6,ease:"back.out(1.5)"}},{round(t0+.5,2)});',
        f'tl.fromTo("#{sid}s",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.4,ease:E}},{round(t0+1.6,2)});',
    ])
    html = f'<div id="{sid}" class="clip light" data-start="{round(t0,2)}" data-duration="{d}" data-track-index="1">{body}</div>'
    return html.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»"), js

g.scene = scene
g.EXTRA_V2 = g.EXTRA_V2 + GIFT_CSS

SPEC = {"slug": "nouveautes-cartes-cadeaux", "scenes": [
  {"k": "hook2", "title": "Noël approche. Vos clientes cherchent <span>quoi offrir</span>.", "sub": "Nouveau sur GuidPilot 🎁", "subt": 1.6,
   "say": "Noël approche… et vos clientes cherchent quoi offrir."},
  {"k": "gift",
   "say": "Nouveau sur GuidPilot : les cartes cadeaux à votre logo, achetées sur votre page ou vendues au cabinet."},
  {"k": "list", "tag": "NOUVEAU", "top": 380, "extop": 820, "size": 88, "title": "Les <span>forfaits</span> de séances",
   "ex": ("card", "FORFAIT · 5 SÉANCES", "Plus que 3 séances : décomptées automatiquement"), "ext": 0.8,
   "say": "Les forfaits de séances, décomptés automatiquement."},
  {"k": "list", "tag": "NOUVEAU", "top": 330, "extop": 720, "size": 84, "title": "Encaissé au cabinet&nbsp;? <span>Un clic.</span>",
   "ex": ("list", ["Chèque", "Espèces", "Carte sur votre terminal"], 0.35), "ext": 0.7,
   "say": "Le chèque et les espèces, enregistrés en un clic."},
  {"k": "list", "tag": "NOUVEAU", "top": 380, "extop": 820, "size": 88, "title": "Votre <span>livre des recettes</span>",
   "ex": ("card", "EXPORT · PÉRIODE AU CHOIX", "À transmettre à votre comptable"), "ext": 0.8,
   "say": "Et votre livre des recettes, à transmettre à votre comptable."},
  {"k": "quote", "title": "GuidPilot <span>évolue</span> avec vous.",
   "say": "GuidPilot évolue avec vous."},
  {"k": "save", "kw": "GUIDANCE<br>ou THÉRAPEUTE", "q": "Ou rendez-vous sur guidpilot.fr",
   "say": "Commentez GUIDANCE ou THÉRAPEUTE, ou rendez-vous sur guidpilot.fr."},
]}

if __name__ == "__main__":
    g.build(SPEC, sys.argv[1])
