"""Vidéo YouTube 1920x1080 : « Devenir partenaire GuidPilot » (recrutement de partenaires, 21/10/2026).
Règles : aucun tarif ni montant, jamais le mot « affiliation », vouvoiement, aucune personne représentée
(captures du compte de démonstration recadrées sans la photo de profil), logo officiel uniquement.
Voix : 6 paragraphes Claire générés séparément puis assemblés (temps exacts dans starts.json).
Usage : python3 gen_partenaires.py <voix.wav> <starts.json>  -> build/yt-partenaires/
"""
import json, pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
base = (HERE / "gen_presentation.py").read_text().split("def frame(")[0]
ns = {"__file__": str(HERE / "gen_presentation.py")}
exec(base, ns)
CSS, ATELIER, KIT = ns["CSS"], ns["ATELIER"], ns["KIT"]

S = json.loads(pathlib.Path(sys.argv[2]).read_text())  # {"starts":[...6], "ends":[...6], "total": x}
st, en = S["starts"], S["ends"]
DUR = round(S["total"] + 4.5, 2)
E = "power3.out"

EXTRA = """
.hid{opacity:0}
.kick{font-weight:700;font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:#E9C46A}
.mega{font-weight:800;font-size:120px;line-height:1.02;letter-spacing:-.03em;color:#fff;margin-top:26px}
.mega span{color:#E9C46A}
.prow{display:flex;gap:22px;margin-top:60px;justify-content:center}
.pp{padding:20px 38px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:700;font-size:38px}
.ttl{position:absolute;left:110px;top:120px;width:1700px;font-weight:800;font-size:66px;line-height:1.1;letter-spacing:-.02em;color:#0F172A}
.ttl span{color:#2563EB}
.ttl.w{color:#fff}.ttl.w span{color:#E9C46A}
.qcol{position:absolute;left:110px;top:330px;width:900px}
.qc{display:flex;align-items:center;gap:24px;margin-top:26px;padding:28px 34px;border-radius:26px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 16px 40px rgba(15,23,42,.07);font-weight:700;font-size:40px;color:#0F172A}
.qc i{font-style:normal;flex:none;width:64px;height:64px;border-radius:50%;background:#FEF3C7;color:#92400E;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:36px}
.tools{position:absolute;left:1100px;top:340px;width:700px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.tl5{padding:30px 20px;border-radius:24px;background:#fff;border:2px dashed #CBD5E1;text-align:center;font-weight:800;font-size:34px;color:#475569}
.tl5 b{display:block;font-size:56px;margin-bottom:10px}
.night{position:absolute;left:1100px;top:880px;width:700px;padding:24px 30px;border-radius:22px;background:#0F172A;color:#fff;font-weight:800;font-size:36px;text-align:center}
.lst{position:absolute;left:110px;top:330px;width:760px}
.li{display:flex;align-items:center;gap:22px;margin-top:24px;padding:26px 30px;border-radius:22px;background:#EEF2F7;border:2px solid transparent;font-weight:700;font-size:38px;color:#94A3B8}
.li i{font-style:normal;flex:none;width:58px;height:58px;border-radius:50%;background:#CBD5E1;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px}
.cards{position:absolute;left:110px;right:110px;top:360px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px}
.cd{padding:50px 40px;border-radius:30px;background:#1E293B;border:2px solid #334155;min-height:430px}
.cd b{display:block;font-size:80px}
.cd h3{font-weight:800;font-size:46px;line-height:1.15;color:#fff;margin-top:26px}
.cd p{font-weight:600;font-size:32px;line-height:1.4;color:#CBD5E1;margin-top:20px}
.steps{position:absolute;left:110px;right:110px;top:420px;display:grid;grid-template-columns:repeat(3,1fr);gap:50px}
.sp{position:relative;padding:60px 44px 50px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.08);min-height:380px}
.sp .n{position:absolute;top:-48px;left:44px;width:96px;height:96px;border-radius:50%;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:50px}
.sp h3{font-weight:800;font-size:44px;line-height:1.15;color:#0F172A;margin-top:20px}
.sp p{font-weight:600;font-size:30px;line-height:1.4;color:#64748B;margin-top:18px}
.endc{position:absolute;left:0;right:0;top:120px;display:flex;flex-direction:column;align-items:center;text-align:center}
.endc .t{font-weight:800;font-size:96px;color:#fff;margin-top:50px;letter-spacing:-.02em}
.endc .d{font-weight:700;font-size:42px;color:#CBD5E1;margin-top:26px}
.endc .d span{color:#E9C46A}
"""

def pop(sel, t, y=30, ease="back.out(1.6)"):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{round(t, 2)});\n'
def lion(sel, t):
    return (f'tl.to("{sel}",{{color:"#0F172A",backgroundColor:"#FFFFFF",borderColor:"#BFDBFE",duration:.35}},{round(t, 2)});\n'
            f'tl.to("{sel} i",{{backgroundColor:"#2563EB",duration:.35}},{round(t, 2)});\n')
def at(i, f):  # instant situé à la fraction f du paragraphe i
    return st[i] + (en[i] - st[i]) * f
def clip(id_, i, cls, inner, logo=True):
    end = st[i + 1] if i + 1 < len(st) else DUR
    s0 = 0 if i == 0 else st[i] - .25
    lg = '<img class="logo-corner" src="assets/logo_couleur.png" alt="GuidPilot" />' if (logo and cls == "light") else ""
    return f'<div id="{id_}" class="clip {cls}" data-start="{round(s0, 2)}" data-duration="{round(end - .25 - s0 if i + 1 < len(st) else end - s0, 2)}" data-track-index="1">{lg}{inner}</div>'

def shot(id_, img, W, box, left, top, w):
    x0, y0, x1, y1 = box; s = w / (x1 - x0); h = round((y1 - y0) * s)
    return (f'<div class="frame hid" id="{id_}" style="left:{left}px;top:{top}px;width:{w}px"><div class="bar"><span class="dot"></span><span class="dot"></span>'
            f'<span class="dot"></span><span class="demo">Compte de démonstration</span></div><div class="vp" style="height:{h}px">'
            f'<img class="shot" src="assets/{img}" alt="" style="width:{round(W * s)}px;left:{-round(x0 * s)}px;top:{-round(y0 * s)}px" /></div></div>')

body, js = "", ""
# A — accroche (navy)
body += clip("a", 0, "navy", '''<div class="center" style="top:250px"><div class="kick hid" id="ak">Praticiens · Thérapeutes · Formateurs</div>
<div class="mega" id="at">GuidPilot cherche<br/>des <span>partenaires</span></div>
<div class="prow"><div class="pp hid" id="ap0">Vous les formez</div><div class="pp hid" id="ap1">Vous les conseillez</div><div class="pp hid" id="ap2">Ils vous suivent</div></div></div>''')
js += 'tl.fromTo("#at",{scale:1.04},{scale:1,duration:1.2,ease:"power2.out"},0);\n' + pop("#ak", .3)
for k, f in enumerate((.25, .42, .6)): js += pop(f"#ap{k}", at(0, f))

# B — le problème (light)
qs = ["Comment recevoir mes premiers clients&nbsp;?", "Comment me faire payer sans relancer&nbsp;?", "Comment faire des factures correctes&nbsp;?"]
tools = [("📅", "Agenda"), ("💳", "Paiement"), ("🧾", "Factures"), ("💬", "Messages")]
body += clip("b", 1, "light", '<div class="ttl hid" id="bt">Quand un praticien se lance,<br/><span>les mêmes questions reviennent</span></div>'
             + '<div class="qcol">' + "".join(f'<div class="qc hid" id="bq{k}"><i>?</i>{q}</div>' for k, q in enumerate(qs)) + '</div>'
             + '<div class="tools">' + "".join(f'<div class="tl5 hid" id="bo{k}"><b>{e}</b>{n}</div>' for k, (e, n) in enumerate(tools)) + '</div>'
             + '<div class="night hid" id="bn">🌙 21&nbsp;h&nbsp;: encore de l\'administratif</div>')
js += pop("#bt", st[1] + .1, 40, E)
for k, f in enumerate((.2, .38, .55)): js += pop(f"#bq{k}", at(1, f))
for k in range(4): js += pop(f"#bo{k}", at(1, .7) + k * .25)
js += pop("#bn", at(1, .88))

# C — GuidPilot (light)
items = ["Réservation et paiement en ligne", "Rappels envoyés automatiquement", "Factures créées toutes seules", "Un espace privé pour chaque client"]
body += clip("c", 2, "light", '<div class="ttl hid" id="ct">Le seul outil conçu <span>pour leur métier</span></div>'
             + '<div class="lst">' + "".join(f'<div class="li hid" id="cl{k}"><i>✓</i>{x}</div>' for k, x in enumerate(items)) + '</div>'
             + shot("cs0", "page_np.png", 1100, (310, 90, 960, 590), 960, 300, 860)
             + shot("cs1", "dash_np.png", 1270, (20, 585, 805, 845), 960, 330, 860)
             + shot("cs2", "guid.png", 1270, (430, 150, 1235, 480), 960, 330, 860))
js += pop("#ct", st[2] + .1, 40, E)
for k in range(4): js += pop(f"#cl{k}", st[2] + .5 + k * .15, 20, E)
for k, f in enumerate((.3, .52, .72, .88)): js += lion(f"#cl{k}", at(2, f))
cs = [(.05, .45), (.45, .7), (.7, 1.0)]
for k, (a, b) in enumerate(cs):
    js += f'tl.fromTo("#cs{k}",{{opacity:0,x:80}},{{opacity:1,x:0,duration:.6,ease:"{E}"}},{round(at(2, a) + .3, 2)});\n'
    if k < 2: js += f'tl.to("#cs{k}",{{opacity:0,duration:.3}},{round(at(2, b), 2)});\n'

# D — qui nous cherchons (navy)
cards = [("🎓", "Vous formez des praticiens", "Reiki, tarot, sophrologie, magnétisme…"),
         ("💬", "Vous partagez vos conseils", "À une communauté de praticiens ou de thérapeutes"),
         ("🧰", "Vous recommandez des outils", "Aux indépendants qui vous font confiance")]
body += clip("d", 3, "navy", '<div class="ttl w hid" id="dt">Nous cherchons des partenaires <span>qui connaissent ce public</span></div><div class="cards">'
             + "".join(f'<div class="cd hid" id="dc{k}"><b>{e}</b><h3>{h}</h3><p>{p}</p></div>' for k, (e, h, p) in enumerate(cards)) + '</div>')
js += pop("#dt", st[3] + .1, 40, E)
for k, f in enumerate((.3, .6, .82)): js += pop(f"#dc{k}", at(3, f), 60)

# E — comment ça marche (light)
steps = [("Candidatez", "Le formulaire est sur guidpilot.fr"), ("Nous étudions", "Chaque candidature, personnellement"),
         ("Vous présentez GuidPilot", "Avec votre lien personnel et tout le nécessaire")]
body += clip("e", 4, "light", '<div class="ttl hid" id="et">Le fonctionnement <span>est simple</span></div><div class="steps">'
             + "".join(f'<div class="sp hid" id="es{k}"><div class="n">{k + 1}</div><h3>{h}</h3><p>{p}</p></div>' for k, (h, p) in enumerate(steps)) + '</div>')
js += pop("#et", st[4] + .1, 40, E)
for k, f in enumerate((.18, .45, .7)): js += pop(f"#es{k}", at(4, f), 60)

# F — appel à l'action (navy, jusqu'à la fin)
body += clip("f", 5, "navy", '''<div class="endc"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:420px;display:block" class="hid" id="fl" />
<div class="t hid" id="ft">Devenez partenaire</div>
<div class="d hid" id="fd">Le lien pour candidater est <span>dans la description</span></div>
<div class="url hid" id="fu">guidpilot.fr</div>
<div class="sub hid" id="fs"><i></i>Abonnez-vous à la chaîne</div></div>''')
js += 'tl.fromTo("#fl",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},' + str(round(st[5], 2)) + ');\n'
js += pop("#ft", st[5] + .4) + pop("#fd", at(5, .1)) + pop("#fu", at(5, .35)) + pop("#fs", at(5, .75))
js += f'tl.to("#fs",{{scale:1.06,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"}},{round(at(5, .75) + .6, 2)});\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1920" data-height="1080">
<div class="aibadge">Voix off générée par IA</div>
<audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
{body}
</div>
<script>
const tl=gsap.timeline({{paused:true}});
gsap.set(".hid",{{opacity:0}});
{js}
window.__timelines["main"]=tl;
</script></body></html>'''

d = ATELIER / "build" / "yt-partenaires"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for a in ("page_np.png", "dash_np.png", "guid.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, "durée", DUR)
