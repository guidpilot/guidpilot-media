"""Reels ManyChat (Instagram uniquement) : appel à commenter un mot-clé, reçu en message privé via ManyChat.
Usage : python3 reels/gen_manychat.py <slug> <voix.wav>
Réutilise les scènes de gen_conseils.py / gen_promos.py avec des temps fixés à la main (silencedetect),
ajoute deux scènes marine « prize » (lots du jeu-concours) et « steps » (étapes numérotées),
et remplace l'écran final par un CTA « Commentez <MOT> … » (variante "concours" : « Commentez GuidPilot pour participer »).
Sortie : build/<slug>/
"""
import pathlib, shutil, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import gen_promos as gp
gc = gp.gc

SPECS = {
 # 13/10/2026 — thérapeutes — voix/2026-10-13_manychat-therapeute.mp3 (22,4 s) — musique pilote
 "m1-therapeute": {"mot": "THÉRAPEUTE", "dur": 25.8, "cta": 18.4, "scenes": [
  ({"k": "x", "tag": "THÉRAPEUTES", "title": "Votre cabinet, <span>éparpillé</span>", "ext": 0.1, "extop": 720,
    "ex": ("list", ["!Rendez-vous : un agenda", "!Paiements : une appli", "!Factures : un tableur", "!Notes de séance : un carnet"], 1.5)}, 0.0),
  ({"k": "hook", "kicker": "SOPHROLOGIE · HYPNOSE · REIKI", "title": "4 outils pour <span>un seul cabinet</span>&nbsp;?", "size": 100}, 6.4),
  ({"k": "shot", "tag": "AVEC GUIDPILOT", "title": "Tout dans <span>un seul espace</span>", "img": "dash_np.png", "W": 1270, "box": (15, 145, 620, 550)}, 8.1),
  ({"k": "x", "title": "Tout est <span>réuni</span>", "size": 84, "ext": 0.1, "extop": 600,
    "ex": ("list", ["Réservation et paiement en ligne", "Fiches clientes et historique", "Notes privées, jamais visibles par la cliente", "Factures automatiques"], 1.85)}, 11.05),
 ]},
 # 14/10/2026 — jeu-concours n°1 — voix/2026-10-14_manychat-concours.mp3 (25,9 s) — musique elan
 "m2-concours": {"mot": "GuidPilot", "concours": True, "dur": 27.4, "cta": 20.0, "scenes": [
  ({"k": "hook", "kicker": "🎁 JEU-CONCOURS", "title": "Le jeu-concours de lancement <span>GuidPilot</span>", "size": 104}, 0.0),
  ({"k": "prize", "t2": 2.85}, 2.35),
  ({"k": "x", "tag": "GUIDPILOT", "title": "Tout dans <span>un seul espace</span>", "ext": 0.25, "extop": 640,
    "ex": ("list", ["Agenda", "Réservations", "Paiements", "Factures", "Espace client"], 1.15)}, 6.7),
  ({"k": "steps", "title": "Pour <span>participer</span>", "items": ["Abonnez-vous à <span>@guidpilot.fr</span>", "Aimez <span>cette publication</span>", "Commentez <span>« GuidPilot »</span>"],
    "at": [1.6, 3.8, 5.1]}, 13.6),
 ]},
 # 15/10/2026 — guidance — voix/2026-10-15_manychat-guidance.mp3 (24,0 s) — musique cocon
 "m3-guidance": {"mot": "GUIDANCE", "dur": 25.6, "cta": 18.05, "scenes": [
  ({"k": "x", "tag": "TAROT · VOYANCE · MÉDIUMNITÉ", "title": "Votre guidance vocale, <span>perdue</span>", "ext": 0.6, "extop": 760,
    "ex": ("chat", [("out", "🎙️ Message vocal · 12 min<small>Envoyé sur WhatsApp</small>"),
                    ("in", "Bonjour, pourriez-vous me la renvoyer ? Je ne la retrouve plus…<small>3 semaines plus tard</small>")], 1.9)}, 0.0),
  ({"k": "x", "tag": "AVEC GUIDPILOT", "title": "Écrite <span>ou vocale</span>", "ext": 0.6, "extop": 760,
    "ex": ("audio", "GUIDANCE VOCALE", "Votre guidance du mois")}, 5.75),
  ({"k": "phone", "title": "Dans son <span>espace client</span>", "size": 76,
    "items": [("📝", "Guidance écrite"), ("🎧", "Guidance vocale"), ("📅", "Prochain rendez-vous"), ("💬", "Messages")]}, 8.75),
  ({"k": "x", "title": "Et pour <span>vous</span>", "size": 84, "ext": 0.15, "extop": 600,
    "ex": ("list", ["Réservation et paiement en ligne", "Agenda", "Fiches clientes et historique"], 1.25)}, 13.1),
 ]},
 # 16/10/2026 — thérapeutes — voix/2026-10-16_manychat-therapeute.mp3 (22,4 s) — musique lofi
 "m4-therapeute": {"mot": "THÉRAPEUTE", "dur": 24.0, "cta": 16.5, "scenes": [
  ({"k": "x", "tag": "THÉRAPEUTES", "title": "6 messages pour <span>1 séance</span>", "ext": 0.15, "extop": 720,
    "ex": ("chat", [("in", "Mardi 18 h ?"), ("out", "Plutôt jeudi ?"), ("in", "Ah non, finalement samedi…")], 1.1)}, 0.0),
  ({"k": "x", "tag": "AVEC GUIDPILOT", "title": "Elle choisit <span>un créneau libre</span>", "ext": 0.5, "extop": 760,
    "ex": ("button", "RÉSERVATION EN LIGNE", "Réserver et payer", "✓ Séance réservée")}, 6.05),
  ({"k": "shot", "tag": "VOTRE AGENDA", "title": "La séance <span>est planifiée</span>", "img": "dash_np.png", "W": 1270, "box": (20, 585, 805, 1000)}, 9.75),
  ({"k": "phone", "title": "Le compte rendu, <span>dans son espace</span>", "size": 72,
    "items": [("📝", "Compte rendu de séance"), ("📅", "Prochaine séance"), ("💬", "Messages")]}, 11.5),
  ({"k": "x", "title": "La facture <span>se crée toute seule</span>", "size": 80, "ext": 0.35, "extop": 760,
    "ex": ("card", "FACTURE", "✓ Créée automatiquement après le paiement")}, 14.85),
 ]},
 # 17/10/2026 — jeu-concours n°2 — voix/2026-10-17_manychat-concours.mp3 (23,1 s) — musique pilote
 "m5-concours": {"mot": "GuidPilot", "concours": True, "dur": 24.6, "cta": 19.7, "scenes": [
  ({"k": "hook", "kicker": "🎁 JEU-CONCOURS GUIDPILOT", "title": "Plus que <span>9 jours</span>", "size": 150, "sub": "pour participer", "subt": 1.4}, 0.0),
  ({"k": "prize", "t2": 1.6}, 3.9),
  ({"k": "steps", "title": "3 étapes, <span>moins d'une minute</span>", "items": ["Abonnez-vous à <span>@guidpilot.fr</span>", "Aimez <span>cette publication</span>", "Commentez <span>« GuidPilot »</span>"],
    "at": [1.75, 4.6, 6.8]}, 7.95),
  ({"k": "x", "tag": "ET ENSUITE", "title": "Confirmation <span>en message privé</span>", "size": 80, "ext": 0.7, "extop": 820,
    "ex": ("chat", [("in", "✓ Votre participation au jeu-concours est bien enregistrée.<small>Message privé automatique · Illustration</small>")], 1)}, 15.3),
 ]},
 # 18/10/2026 — guidance — voix/2026-10-18_manychat-guidance.mp3 (21,3 s) — musique aube
 "m6-guidance": {"mot": "GUIDANCE", "dur": 22.9, "cta": 15.45, "scenes": [
  ({"k": "x", "tag": "TAROT · VOYANCE · ÉNERGÉTIQUE", "title": "Le paiement <span>qui n'arrive pas</span>", "ext": 0.3, "extop": 760,
    "ex": ("chat", [("in", "Je vous fais le virement ce soir&nbsp;!<small>Lundi, 20 h 14</small>"),
                    ("out", "Bonjour, je me permets de revenir vers vous…<small>Jeudi · brouillon jamais envoyé</small>")], 1.9)}, 0.0),
  ({"k": "shot", "tag": "AVEC GUIDPILOT", "title": "Elle réserve <span>sur votre page</span>", "img": "page_np.png", "W": 1100, "box": (80, 80, 1020, 600)}, 5.1),
  ({"k": "x", "tag": "PAIEMENT EN LIGNE", "title": "Payé <span>dès la réservation</span>", "ext": 0.2, "extop": 760,
    "ex": ("button", "RÉSERVATION", "Réserver et payer", "✓ Paiement reçu")}, 8.4),
  ({"k": "x", "title": "Et ensuite, <span>tout suit</span>", "size": 84, "ext": 0.1, "extop": 620,
    "ex": ("list", ["Chaque règlement suivi", "Facture créée toute seule", "Avis demandé en un clic"], 1.5)}, 10.65),
 ]},
}

GOLD = "#E9C46A"
MC_CSS = """
.pz-k{font-weight:800;font-size:46px;letter-spacing:.16em;color:#E9C46A}
.pz-big{margin-top:40px;font-weight:800;font-size:250px;line-height:.9;color:#fff;letter-spacing:-.04em}
.pz-big small{display:block;font-size:76px;line-height:1.1;color:#E9C46A;margin-top:24px;letter-spacing:-.01em;width:920px}
.pz-plus{margin-top:70px;display:inline-block;padding:28px 52px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:58px}
.st-t{font-weight:800;font-size:84px;line-height:1.08;color:#fff;width:920px;letter-spacing:-.02em}
.st-t span{color:#E9C46A}
.st{display:flex;align-items:center;gap:30px;margin:28px 0;padding:36px 42px;width:940px;border-radius:32px;background:#1E293B;border:3px solid #334155;text-align:left;font-weight:800;font-size:54px;line-height:1.15;color:#fff}
.st b{flex:none;display:flex;align-items:center;justify-content:center;width:100px;height:100px;border-radius:50%;background:#E9C46A;color:#0F172A;font-size:56px}
.st span{color:#E9C46A}
"""

def mc_scene(i, sc, t0, t1):
    k = sc["k"]; sid = f"s{i}"; d = round(t1 - t0, 2); js = []
    def a(sel, frm, to, at, ease="E"):
        js.append(f'tl.fromTo("{sel}",{frm},{{...{to},ease:{ease}}},{round(at,2)});')
    if k == "prize":
        body = (f'<div class="center" style="top:420px"><div class="pz-k" id="{sid}k">À GAGNER</div>'
                f'<div class="pz-big" id="{sid}b">1&nbsp;an<small>d\'abonnement GuidPilot offert</small></div>'
                f'<div class="pz-plus" id="{sid}p">+ 2 abonnements de 3&nbsp;mois</div></div>')
        a(f"#{sid}k", "{opacity:0,y:-30}", "{opacity:1,y:0,duration:.4}", t0 + .05)
        a(f"#{sid}b", "{opacity:0,scale:.6}", "{opacity:1,scale:1,duration:.6}", t0 + .2, '"back.out(1.7)"')
        a(f"#{sid}p", "{opacity:0,y:60}", "{opacity:1,y:0,duration:.5}", t0 + sc["t2"], '"back.out(1.6)"')
    elif k == "steps":
        items = "".join(f'<div class="st" id="{sid}i{j}"><b>{j+1}</b><div>{tx}</div></div>' for j, tx in enumerate(sc["items"]))
        body = (f'<div class="center" style="top:330px"><div class="st-t" id="{sid}t">{sc["title"]}</div></div>'
                f'<div class="center" style="top:700px">{items}</div>')
        a(f"#{sid}t", "{opacity:0,y:40}", "{opacity:1,y:0,duration:.45}", t0 + .1)
        for j, at in enumerate(sc["at"]):
            a(f"#{sid}i{j}", "{opacity:0,x:-90}", "{opacity:1,x:0,duration:.45}", t0 + at, '"back.out(1.6)"')
    else:
        return gp.scene(i, sc, t0, t1)
    body = gp._nbsp(body)
    return f'<div id="{sid}" class="clip navy" data-start="{round(t0,2)}" data-duration="{d}" data-track-index="1">{body}</div>', "\n".join(js)

CTA_CSS = """
.mc-lead{font-weight:800;font-size:76px;color:#fff;letter-spacing:-.01em}
.mc-box{margin-top:34px;display:flex;align-items:center;gap:26px;background:#fff;border-radius:36px;padding:34px 44px;box-shadow:0 30px 80px rgba(0,0,0,.35)}
.mc-box i{font-style:normal;flex:none;width:96px;height:96px;border-radius:50%;background:#E0E7FF;display:flex;align-items:center;justify-content:center;font-size:52px}
.mc-word{font-weight:800;font-size:104px;color:#0F172A;letter-spacing:.02em}
.mc-sub{margin-top:44px;font-weight:700;font-size:56px;line-height:1.25;color:#fff;width:900px}
.mc-sub span{color:#E9C46A}
.mc-offer{margin-top:56px;display:inline-block;background:#FBF3DC;color:#6B4E16;font-weight:700;font-size:40px;padding:18px 40px;border-radius:999px}
.mc-site{margin-top:40px;font-weight:800;font-size:52px;color:#60A5FA}
.mc-conf{font-size:46px;color:#E2E8F0}
"""

def cta_html(t, d, mot, concours=False):
    if concours:
        sub, offer, site = "pour <span>participer</span>", "Tirage au sort · lundi 26 octobre", "Confirmation en message privé"
    else:
        sub, offer, site = "et recevez la présentation <span>en message privé</span>", "14 jours gratuits · sans carte bancaire", "guidpilot.fr"
    return f'''<div id="cta" class="clip navy" data-start="{t}" data-duration="{d}" data-track-index="1">
  <div class="center" style="top:200px"><img id="cl" src="assets/logo_blanc.png" alt="GuidPilot" style="width:480px;display:block" /></div>
  <div class="center" style="top:520px"><div class="mc-lead" id="c1">Commentez</div>
  <div class="mc-box" id="c2"><i>💬</i><span class="mc-word">{mot}</span></div>
  <div class="mc-sub" id="c3">{sub}</div>
  <div class="mc-offer" id="c4">{offer}</div>
  <div class="mc-site{' mc-conf' if concours else ''}" id="c5">{site}</div></div>
</div>'''

def cta_js(t):
    return f'''tl.fromTo("#cl",{{opacity:0,y:-30}},{{opacity:1,y:0,duration:.5,ease:E}},{t+.05});
tl.fromTo("#c1",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.4,ease:E}},{t+.15});
tl.fromTo("#c2",{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.8)"}},{t+.4});
tl.fromTo("#c3",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},{t+1.4});
tl.fromTo("#c4",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},{t+2.6});
tl.fromTo("#c5",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},{t+3.0});
tl.to("#c2",{{scale:1.06,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"}},{t+1.2});'''

def build(slug, voix):
    spec = SPECS[slug]; SCENES, CTA_T, DUR = spec["scenes"], spec["cta"], spec["dur"]
    gp.IMGS.clear()
    bodies, jss = [], []
    for i, (sc, t0) in enumerate(SCENES):
        t1 = SCENES[i + 1][1] if i + 1 < len(SCENES) else CTA_T
        h, j = mc_scene(i, sc, t0, t1)
        bodies.append(h); jss.append(j)
    bodies.append(cta_html(CTA_T, round(DUR - CTA_T, 2), spec["mot"], spec.get("concours", False)))
    js = "\n".join(jss) + "\n" + cta_js(CTA_T)
    d = gc.BASE / "build" / slug
    if d.exists(): shutil.rmtree(d)
    (d / "assets").mkdir(parents=True)
    for sub in ("fonts", "vendor"): shutil.copytree(gc.SRC / sub, d / sub)
    for f in ("hyperframes.json", "meta.json"): shutil.copy(gc.SRC / f, d / f)
    for im in gp.IMGS | {"logo_blanc.png"}: shutil.copy(gc.SRC / "assets" / im, d / "assets" / im)
    shutil.copy(voix, d / "assets" / "voix.wav")
    shutil.copy(gc.BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
    html = gc.page(DUR, "\n".join(bodies), js, "voix.wav").replace("</style>", gc.EXTRA + gp.PCSS + CTA_CSS + MC_CSS + "</style>", 1)
    (d / "index.html").write_text(html)
    print("ok", d)

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
