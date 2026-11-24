"""Vidéo YouTube 1920x1080 : « Logiciel de gestion pour sophrologue, Reiki, hypnose : 1 an pour 99 €, ce que cela comprend »
(OFFRE DE NOËL · public thérapeutes, mardi 24/11/2026 — programme du 17/11 au 31/12/2026).
Usage : python3 gen_offre_noel_therapeutes.py <voix.wav> [DUR]  -> build/yt-offre-noel-therapeutes/
Voix : 10 paragraphes générés un par un (voix/2026-11-24_yt-offre-therapeutes-p1..p10.mp3), assemblés dans l'ordre
avec assembler_voix.py (p4 = CTA oral d'abonnement + lien de l'offre, ~32 %). Total 157,0 s.
Temps T = début des mots-clés (silencedetect -32 dB / 0,16 s sur le wav assemblé, ancrage sur la ponctuation,
interpolation par nombre de caractères entre deux ancres).
Structure NOUVELLE « le coffret de l'année + 3 questions » : accroche-question « Combien coûte une de vos séances ? »
(lisible dès l'image 0) + étiquettes « votre séance : ? € » / « 1 an : 99 € » -> barres comparées 348 € / 99 € ->
question 1/3 (carte plein écran) -> coffret « Compris dans l'année » qui se remplit en 3 compartiments (avant la séance,
pendant et après, gestion), compteur x / 12, captures démo finance.png et avis.png -> question 2/3 -> 3 étapes + bande
des 12 mois -> question 3/3 -> 3 choix de fin d'année -> pourquoi cette offre (mot de l'équipe) -> récap -> offre -> fin.
Offre de Noël (exception validée par Normane jusqu'au 31/12/2026) : 99 € payés une fois, 29 €/mois et 348 € en comparaison.
Aucune personne, aucun superlatif, aucun vocabulaire médical, aucune promesse de rentabilité.
Réutilise CSS et helpers de gen_gagner_temps_therapeutes.py (et sa chaîne).
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_gagner_temps_therapeutes.py").read_text()
ns = {"__file__": str(HERE / "gen_gagner_temps_therapeutes.py")}
_argv = sys.argv[:]
sys.argv = sys.argv[:2]
exec(src.split("\nT = dict(")[0], ns)
sys.argv = _argv
CSS, ATELIER, KIT, LOGO, LOGOW, E, LOCK = (ns[k] for k in ("CSS", "ATELIER", "KIT", "LOGO", "LOGOW", "E", "LOCK"))
EXTRAS = "".join(ns[k] for k in ("EXTRA", "EXTRA4", "EXTRA5", "EXTRA7", "EXTRA8", "EXTRA9", "EXTRA10", "EXTRA11"))

DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 160.0
r2 = lambda x: round(x, 2)


def pop(sel, t, ease="back.out(1.6)", y=30):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{r2(t)});\n'


def fin(sel, t, x=120):
    return f'tl.fromTo("{sel}",{{opacity:0,x:{x},scale:.95}},{{opacity:1,x:0,scale:1,duration:.7,ease:"{E}"}},{r2(t)});\n'


def setv(sel, t, v=1):
    return f'tl.set("{sel}",{{opacity:{v}}},{r2(t)});\n'


EXTRA13 = """
.hk13{position:absolute;left:0;right:0;top:120px;text-align:center}
.hk13 .tg{display:inline-block;padding:12px 32px;border-radius:999px;background:#1E293B;border:2px solid #475569;color:#E2E8F0;font-weight:800;font-size:32px}
.hk13 .q{font-weight:800;font-size:104px;line-height:1.04;letter-spacing:-.035em;color:#fff;margin-top:30px}
.hk13 .q span{color:#E9C46A}
.tags13{position:absolute;left:0;right:0;top:500px;display:flex;justify-content:center;align-items:center;gap:50px}
.tag13{width:620px;height:250px;border-radius:34px;padding:34px 44px;display:flex;flex-direction:column;justify-content:space-between}
.tag13 small{font-weight:800;font-size:30px;letter-spacing:.08em;text-transform:uppercase}
.tag13 b{font-weight:800;font-size:110px;letter-spacing:-.04em;line-height:1}
.tag13 em{font-style:normal;font-weight:700;font-size:28px}
.tag13.t1{background:#1E293B;border:3px dashed #64748B;color:#fff}.tag13.t1 small{color:#94A3B8}.tag13.t1 b{color:#93C5FD}
.tag13.t2{background:#FBF3DC;border:3px solid #E9C46A;color:#0F172A}.tag13.t2 small{color:#6B4E16}.tag13.t2 em{color:#6B4E16}
.vs13{font-weight:800;font-size:60px;color:#64748B}
.car{display:inline-block;width:6px;height:90px;background:#93C5FD;margin-left:8px;vertical-align:-6px}
.chips13{position:absolute;left:0;right:0;top:840px;display:flex;justify-content:center;gap:26px}
.chips13 div{display:flex;align-items:center;gap:16px;padding:20px 36px;border-radius:999px;background:#fff;color:#0F172A;font-weight:800;font-size:36px}
.chips13 div i{font-style:normal;display:flex;width:50px;height:50px;border-radius:50%;background:#0F172A;color:#E9C46A;align-items:center;justify-content:center;font-size:28px}
.bars13{position:absolute;left:150px;right:150px;top:370px;display:flex;flex-direction:column;gap:56px}
.bar13 .lb{display:flex;justify-content:space-between;align-items:baseline;font-weight:800;font-size:40px;color:#0F172A}
.bar13 .lb small{font-weight:700;font-size:30px;color:#64748B;margin-left:16px}
.bar13 .tr{position:relative;height:110px;margin-top:18px;border-radius:24px;background:#EDE6D6}
.bar13 .tr b{position:absolute;left:0;top:0;bottom:0;border-radius:24px;transform-origin:left center;display:flex;align-items:center;justify-content:flex-end;padding-right:30px;font-weight:800;font-size:56px}
.bar13.a .tr b{width:100%;background:#334155;color:#fff}
.bar13.n .tr b{width:28.45%;background:#E9C46A;color:#0F172A}
.calc13{position:absolute;left:0;right:0;top:860px;text-align:center}
.calc13 div{display:inline-block;padding:24px 50px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:42px}
.calc13 div span{color:#E9C46A}
.allf{position:absolute;left:150px;bottom:150px;display:inline-flex;align-items:center;gap:18px;padding:22px 40px;border-radius:999px;background:rgba(255,255,255,.16);border:2px solid rgba(255,255,255,.4);color:#fff;font-weight:800;font-size:38px}
.box13L{position:absolute;left:100px;top:140px;width:600px}
.box13L .h{font-size:88px;color:#0F172A}
.box13L .h span{color:#2563EB}
.cnt13{margin-top:46px;width:420px;border-radius:30px;background:#0F172A;padding:30px 36px;color:#fff}
.cnt13 small{display:block;font-weight:700;font-size:24px;letter-spacing:.1em;color:#94A3B8;text-transform:uppercase}
.cnt13 .nn{position:relative;height:110px;margin-top:8px}
.cnt13 .nn b{position:absolute;left:0;top:0;font-weight:800;font-size:96px;letter-spacing:-.03em;color:#E9C46A;opacity:0}
.cnt13 .nn em{position:absolute;left:190px;top:34px;font-style:normal;font-weight:800;font-size:52px;color:#64748B}
.secs{display:flex;gap:10px;margin-top:20px}
.secs i{display:block;flex:1;height:12px;border-radius:6px;background:#334155}
.secs i.on{background:#E9C46A}
.box13{position:absolute;left:760px;right:80px;top:120px;bottom:60px;border-radius:40px;background:#fff;border:3px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.10);overflow:hidden}
.box13 .lid{height:96px;background:#0F172A;display:flex;align-items:center;justify-content:center;gap:16px;color:#E9C46A;font-weight:800;font-size:34px;letter-spacing:.06em;position:relative}
.box13 .lid:after{content:"";position:absolute;left:50%;top:0;bottom:0;width:40px;margin-left:-20px;background:#E9C46A;opacity:.25}
.grid13{display:grid;grid-template-columns:1fr 1fr;gap:26px;padding:34px}
.tile13{height:330px;border-radius:28px;background:#F6F8FC;border:2px solid #E2E8F0;padding:34px 34px;display:flex;flex-direction:column}
.tile13 i{font-style:normal;display:flex;width:86px;height:86px;border-radius:24px;background:#EFF6FF;color:#2563EB;align-items:center;justify-content:center;font-size:44px}
.tile13.g i{background:#FBF3DC;color:#B7791F}
.tile13 b{font-weight:800;font-size:40px;line-height:1.12;color:#0F172A;margin-top:26px}
.tile13 small{font-weight:600;font-size:27px;line-height:1.3;color:#64748B;margin-top:10px}
.sm13 .tile13{height:200px;padding:24px 30px;flex-direction:row;align-items:center;gap:24px}
.sm13 .tile13 b{margin-top:0;font-size:36px}
.sm13 .tile13 small{font-size:24px}
.sm13 .tile13 b,.sm13 .tile13 small{display:block}
.sm13 .tile13 i{flex:none}
.shot13{position:absolute;left:34px;right:34px;bottom:30px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 18px 50px rgba(15,23,42,.14);overflow:hidden}
.shot13 img{display:block;width:100%}
.shot13 .dm{position:absolute;right:14px;top:10px;font-size:18px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:3px 14px}
.steps13{position:absolute;left:100px;right:100px;top:290px;display:flex;align-items:stretch;gap:24px}
.steps13 .st{flex:1;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.08);padding:36px 40px}
.steps13 .st i{font-style:normal;display:flex;width:80px;height:80px;border-radius:50%;background:#2563EB;color:#fff;align-items:center;justify-content:center;font-size:40px;font-weight:800}
.steps13 .st.g{border:3px solid #E9C46A;background:#FFFBEF}.steps13 .st.g i{background:#E9C46A;color:#0F172A}
.steps13 .st b{display:block;font-weight:800;font-size:46px;line-height:1.1;color:#0F172A;margin-top:26px}
.steps13 .st small{display:block;font-weight:700;font-size:28px;color:#64748B;margin-top:14px}
.steps13 .ar{align-self:center;font-weight:800;font-size:60px;color:#2563EB}
.mon13{position:absolute;left:100px;right:100px;top:730px;display:grid;grid-template-columns:repeat(12,1fr);gap:12px}
.mon13 div{height:110px;border-radius:18px;background:#fff;border:2px solid #BFDBFE;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:800;font-size:30px;color:#1D4ED8}
.mon13 div small{font-weight:700;font-size:18px;color:#64748B;margin-bottom:6px}
.mon13 div.g{background:#E9C46A;border-color:#E9C46A;color:#0F172A}.mon13 div.g small{color:#6B4E16}
.np13{position:absolute;left:0;right:0;top:900px;display:flex;justify-content:center;gap:24px}
.np13 div{padding:20px 40px;border-radius:999px;font-weight:800;font-size:38px}
.np13 .a{background:#DCFCE7;color:#15803D;border:2px solid #86EFAC}
.np13 .b{background:#0F172A;color:#fff}
.ch13{position:absolute;left:110px;right:110px;top:360px;display:flex;gap:34px}
.ch13 .c{flex:1;height:440px;border-radius:34px;background:#1E293B;border:3px solid #475569;padding:44px 40px;display:flex;flex-direction:column}
.ch13 .c i{font-style:normal;display:flex;width:100px;height:100px;border-radius:28px;background:#0F172A;color:#E9C46A;align-items:center;justify-content:center;font-size:52px}
.ch13 .c b{font-weight:800;font-size:54px;line-height:1.08;color:#fff;margin-top:40px}
.ch13 .c small{font-weight:600;font-size:30px;line-height:1.3;color:#CBD5E1;margin-top:16px}
.ch13 .c.k{border-color:#E9C46A}
.hd13{position:absolute;left:0;right:0;top:130px;text-align:center}
.hd13 .h{font-size:80px;color:#fff}
.hd13 .h span{color:#E9C46A}
.why13{position:absolute;left:260px;right:260px;top:300px;border-radius:40px;background:#fff;border:3px solid #E7DFC9;box-shadow:0 30px 80px rgba(15,23,42,.08);padding:56px 70px}
.why13 .ln{display:flex;align-items:center;gap:26px;font-weight:800;font-size:46px;line-height:1.15;color:#0F172A;margin-bottom:34px}
.why13 .ln i{font-style:normal;flex:none;display:flex;width:64px;height:64px;border-radius:50%;background:#FBF3DC;color:#B7791F;align-items:center;justify-content:center;font-size:32px}
.why13 .ln span{color:#2563EB}
.why13 .sg{font-weight:700;font-size:30px;color:#6B4E16;text-align:right}
"""

T = {'gard': 4.28, 'jus': 5.84, 'e99': 8.18, 'une': 8.65, 'dans': 9.95, 'q1': 11.96, 'q2': 13.25, 'q3': 14.61,
     'b': 17.26, 'm29': 19.6, 'm348': 21.84, 'noel': 23.55, 'b99': 24.63, 'beau': 26.62,
     'c1': 30.55, 'tout': 33.2, 'opt': 35.84, 'av': 37.55, 'page': 39.15, 'cab': 40.96, 'cli': 42.44, 'regl': 44.85, 'agd': 46.11, 'rap': 48.44,
     'cta': 50.52, 'abo': 53.13, 'lien': 55.92,
     'g2': 60.23, 'meet': 62.82, 'notes': 64.77, 'hist': 67.59, 'cr': 70.63, 'esp': 73.28, 'msg': 75.34,
     'g3': 77.04, 'fac': 78.15, 'tab': 80.59, 'enc': 82.98, 'avis': 85.8, 'page6': 87.13, 'com': 89.25,
     'qq2': 93.21, 'un': 96.36, 'deux': 100.65, 'd99': 102.36, 'd31': 104.33, 'trois': 105.69, 'pre': 108.0, 'rien': 109.66,
     'qq3': 111.83, 'choi': 113.86, 'ren': 115.14, 'mois': 115.95, 'arr': 116.95, 'lect': 118.24,
     'pq': 121.82, 'jeune': 122.86, 'concu': 124.46, 'pref': 127.58, 'simple': 131.01, 'amel': 131.79, 'sem': 133.41,
     'rs': 136.92, 'r1': 137.85, 'r2': 141.03, 'r3': 144.98, 'o': 147.21, 'olien': 150.72, 'o31': 152.47, 'z': 154.64}

body, js = "", ""


def clip(id_, cls, a, b, inner, logo=None):
    lg = logo if logo is not None else (LOGOW if cls in ("navy", "eve", "blue") else LOGO)
    return f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(a)}" data-duration="{r2(b - a)}" data-track-index="1">
  {lg}
{inner}
</div>'''


def qcard(id_, cls, a, b, num, q, extra=""):
    bars = "".join(f'<i class="{"on" if k < num else ""}"></i>' for k in range(3))
    return clip(id_, cls, a, b, f'''
  <div class="qz"><div class="n hid" id="{id_}n"><b>{num}</b>Question {num} sur 3</div>
    <div class="q hid" id="{id_}q">{q}</div>
    <div class="bar5" style="gap:16px">{bars.replace("<i", '<i style="width:200px"')}</div></div>{extra}''')


# ---------- A : accroche (0 -> b) — question lisible dès l'image 0
body += clip("a", "navy", 0, T["b"], '''
  <div class="hk13"><div class="tg">Sophrologie · Reiki · Hypnose</div>
    <div class="q">Combien coûte <span>une de vos séances&nbsp;?</span></div></div>
  <div class="tags13"><div class="tag13 t1" id="at1"><small>Votre séance</small><b>?<span class="car" id="acar"></span> €</b><em style="color:#94A3B8">Gardez ce chiffre en tête</em></div>
    <div class="vs13 hid" id="avs">·</div>
    <div class="tag13 t2 hid" id="at2"><small>🎁 1 an de GuidPilot</small><b id="a99" class="hid">99&nbsp;€</b><em class="hid" id="aun">payés une fois · jusqu'au 31 décembre</em></div></div>
  <div class="chips13"><div class="hid" id="ac1"><i>1</i>Ce que cela comprend</div><div class="hid" id="ac2"><i>2</i>Comment ça se passe</div>
    <div class="hid" id="ac3"><i>3</i>Au bout d'un an</div></div>''')
js += f'tl.to("#acar",{{opacity:0,duration:.25,yoyo:true,repeat:9}},{r2(T["gard"] + .5)});\n'
js += pop("#avs", T["jus"]) + pop("#at2", T["jus"] + .1, "back.out(1.8)") + pop("#a99", T["e99"], "back.out(2)", 40) + pop("#aun", T["une"])
js += pop("#ac1", T["q1"]) + pop("#ac2", T["q2"]) + pop("#ac3", T["q3"])

# ---------- B : comparaison (b -> c1)
body += clip("b", "cream", T["b"], T["c1"], '''
  <div class="hdr" style="top:120px"><div class="chap hid" id="bc" style="color:#B7791F"><b style="background:#0F172A;color:#E9C46A">€</b>La comparaison</div>
    <div class="h hid" id="bh" style="font-size:80px;color:#0F172A">Faites-la <span style="color:#2563EB">avec votre propre tarif</span></div></div>
  <div class="bars13">
    <div class="bar13 a hid" id="bA"><div class="lb"><span>Au mois<small>29&nbsp;€ par mois × 12</small></span></div><div class="tr"><b id="bAb">348&nbsp;€</b></div></div>
    <div class="bar13 n hid" id="bN"><div class="lb"><span>🎁 Offre de Noël<small>payée une seule fois · 12 mois</small></span></div><div class="tr"><b id="bNb">99&nbsp;€</b></div></div></div>
  <div class="calc13 hid" id="bq"><div>99&nbsp;€ = <span>une ou deux de vos séances&nbsp;?</span></div></div>''')
js += pop("#bc", T["b"] + .05, E) + pop("#bh", T["b"] + .25, E, 40)
js += pop("#bA", T["m29"]) + f'tl.fromTo("#bAb",{{scaleX:0}},{{scaleX:1,duration:1.6,ease:"power2.out"}},{r2(T["m29"] + .3)});\n'
js += pop("#bN", T["noel"]) + f'tl.fromTo("#bNb",{{scaleX:0}},{{scaleX:1,duration:1.0,ease:"power2.out"}},{r2(T["b99"] - .2)});\n'
js += pop("#bq", T["beau"], "back.out(2)")

# ---------- Q1 (c1 -> av)
body += qcard("q1", "blue", T["c1"], T["av"], 1, "Qu'est-ce qui est <span>compris&nbsp;?</span>",
              '<div class="allf hid" id="q1a">✓ Toutes les fonctions de l\'abonnement · aucune option à ajouter</div>')
js += pop("#q1n", T["c1"] + .05, E) + pop("#q1q", T["c1"] + .3, E, 40) + pop("#q1a", T["tout"], "back.out(2)")


# ---------- coffret : 3 compartiments
def coffret(id_, a, b, sec, title, tiles, n0, small=False, extra=""):
    nums = "".join(f'<b id="{id_}k{n}">{n}</b>' for n in range(n0, n0 + 5))
    secs = "".join(f'<i class="{"on" if k < sec else ""}"></i>' for k in range(3))
    tl_ = "".join(f'<div class="tile13{" g" if k % 3 == 1 else ""} hid" id="{id_}t{k}"><i>{ic}</i><div><b>{tt}</b><small>{sm}</small></div></div>'
                  if small else
                  f'<div class="tile13{" g" if k % 3 == 1 else ""} hid" id="{id_}t{k}"><i>{ic}</i><b>{tt}</b><small>{sm}</small></div>'
                  for k, (ic, tt, sm, _) in enumerate(tiles))
    h = clip(id_, "light", a, b, f'''
  <div class="box13L"><div class="chap hid" id="{id_}c"><b>🎁</b>Compris · {sec}/3</div>
    <div class="h hid" id="{id_}h">{title}</div>
    <div class="cnt13"><small>Fonctions dévoilées</small><div class="nn">{nums}<em>/ 12</em></div><div class="secs">{secs}</div></div></div>
  <div class="box13"><div class="lid">🎁 COMPRIS DANS L'ANNÉE</div><div class="grid13{" sm13" if small else ""}">{tl_}</div>{extra}</div>''')
    j = pop(f"#{id_}c", a + .05, E) + pop(f"#{id_}h", a + .25, E, 40) + setv(f"#{id_}k{n0}", a)
    for k, (_, _, _, t) in enumerate(tiles):
        j += f'tl.fromTo("#{id_}t{k}",{{opacity:0,scale:.85}},{{opacity:1,scale:1,duration:.5,ease:"back.out(1.8)"}},{r2(t)});\n'
        j += setv(f"#{id_}k{n0 + k}", t, 0) + setv(f"#{id_}k{n0 + k + 1}", t)
        j += f'tl.fromTo("#{id_}k{n0 + k + 1}",{{scale:1.25}},{{scale:1,duration:.4}},{r2(t)});\n'
    return h, j


h, j = coffret("g1", T["av"], T["cta"], 1, "Avant <span>la séance</span>", [
    ("🔗", "Votre page de praticienne", "Vos prestations, au cabinet ou en visio", T["page"]),
    ("📅", "Réservation en ligne", "Votre cliente choisit son créneau", T["cli"]),
    ("💳", "Paiement en ligne", "Réglé dès la réservation", T["regl"]),
    ("✉", "Agenda et rappel e&#8209;mail", "Le rendez-vous arrive tout seul", T["agd"])], 0)
body += h; js += j

# ---------- CTA oral abonnement + offre (cta -> g2)
body += clip("cta", "navy", T["cta"], T["g2"], '''
  <div class="ctaC" style="top:110px"><div class="k hid" id="ck">CES VIDÉOS VOUS AIDENT&nbsp;?</div>
    <div class="b hid" id="cb2">2 vidéos par semaine<br/><span>pour votre cabinet</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="gift hid" id="cg"><div>🎁 Jusqu'au 31 décembre&nbsp;: 1 an pour 99&nbsp;€, payé une fois</div></div>
  <div class="dsc hid" id="cd" style="top:820px">↓ <span><b>Le lien</b> est en 1re ligne de la description</span></div>''')
js += pop("#ck", T["cta"] + .1, E) + pop("#cb2", T["cta"] + .6, E, 40) + pop("#cy", T["abo"], "back.out(2)")
js += f'tl.to("#cy",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(T["abo"] + .8)});\n'
js += pop("#cg", T["lien"] - .3, "back.out(1.8)") + pop("#cd", T["lien"] + .6)

h, j = coffret("g2", T["g2"], T["g3"], 2, "Pendant <span>et après</span>", [
    ("🎥", "Lien Google Meet", "Prêt pour vos séances à distance", T["meet"]),
    (LOCK.format(s=44, c="#B7791F"), "Fiche et notes privées", "Tout l'historique de votre cliente", T["notes"]),
    ("🎙", "Compte rendu écrit ou audio", "Envoyé après la séance", T["cr"]),
    (LOCK.format(s=44, c="#2563EB"), "Espace client sécurisé", "Avec la messagerie", T["esp"])], 4)
body += h; js += j

# groupe 3 : tuiles compactes + captures démo en bas
fs = 1 - 0.0  # finance.png 1270x240 ; avis.png 1270x330
h, j = coffret("g3", T["g3"], T["qq2"], 3, "Côté <span>gestion</span>", [
    ("🧾", "Factures numérotées", "Créées automatiquement", T["fac"]),
    ("📊", "Tableau de bord", "Encaissé et reste à encaisser", T["tab"]),
    ("★", "Demandes d'avis", "L'avis peut s'afficher sur votre page", T["avis"]),
    ("0 %", "Aucune commission", "Hors frais du moyen de paiement", T["com"])], 8, small=True,
    extra='''<div class="shot13 hid" id="g3f"><img src="assets/finance.png" alt="" /><span class="dm">Compte de démonstration</span></div>
  <div class="shot13 hid" id="g3a"><img src="assets/avis.png" alt="" /><span class="dm">Compte de démonstration</span></div>''')
body += h; js += j
js += pop("#g3f", T["tab"] + .4, E, 60) + f'tl.to("#g3f",{{opacity:0,duration:.4}},{r2(T["avis"] + .3)});\n' + pop("#g3a", T["avis"] + .5, E, 60)

# ---------- Q2 (qq2 -> un) puis 3 étapes (un -> qq3)
body += qcard("q2", "navy", T["qq2"], T["un"], 2, "Comment ça se passe, <span>concrètement&nbsp;?</span>")
js += pop("#q2n", T["qq2"] + .05, E) + pop("#q2q", T["qq2"] + .3, E, 40)
mons = '<div class="g hid" id="m0"><small>Mois 1</small>99&nbsp;€</div>' + "".join(
    f'<div class="hid" id="m{k}"><small>Mois {k + 1}</small>✓</div>' for k in range(1, 12))
body += clip("s", "light", T["un"], T["qq3"], f'''
  <div class="hdr" style="top:110px"><div class="chap"><b>▶</b>En 3 étapes</div></div>
  <div class="steps13"><div class="st hid" id="s1"><i>1</i><b>Créez votre compte</b><small>14 jours gratuits · sans carte bancaire</small></div>
    <div class="ar hid" id="sa1">→</div>
    <div class="st g hid" id="s2"><i>2</i><b>Un seul paiement&nbsp;: 99&nbsp;€</b><small id="s2d" class="hid">Avant le 31 décembre</small></div>
    <div class="ar hid" id="sa2">→</div>
    <div class="st hid" id="s3"><i>3</i><b>12 mois d'accès complet</b><small>Toutes les fonctions</small></div></div>
  <div class="mon13">{mons}</div>
  <div class="np13"><div class="a hid" id="sn">✓ Aucun prélèvement automatique</div><div class="b hid" id="sr">Rien ne repart sans vous</div></div>''')
js += pop("#s1", T["un"] + .1, "back.out(1.8)", 40) + pop("#sa1", T["deux"]) + pop("#s2", T["deux"] + .1, "back.out(1.8)", 40)
js += pop("#s2d", T["d31"]) + pop("#sa2", T["trois"]) + pop("#s3", T["trois"] + .1, "back.out(1.8)", 40)
js += pop("#m0", T["d99"], "back.out(2)")
js += "".join(pop(f"#m{k}", T["trois"] + .5 + k * .12, "back.out(2)", 20) for k in range(1, 12))
js += pop("#sn", T["pre"], "back.out(2)") + pop("#sr", T["rien"], "back.out(2)")

# ---------- Q3 (qq3 -> choi) puis 3 choix (choi -> pq)
body += qcard("q3", "blue", T["qq3"], T["choi"], 3, "Et au bout <span>d'un an&nbsp;?</span>")
js += pop("#q3n", T["qq3"] + .02, E) + pop("#q3q", T["qq3"] + .15, E, 40)
body += clip("f", "navy", T["choi"], T["pq"], f'''
  <div class="hd13"><div class="h hid" id="fh">Au bout d'un an, <span>c'est vous qui choisissez</span></div></div>
  <div class="ch13"><div class="c hid" id="f1"><i>↻</i><b>Renouveler</b><small>Pour une nouvelle année</small></div>
    <div class="c hid" id="f2"><i>📅</i><b>Passer au mois</b><small>Sans engagement</small></div>
    <div class="c hid" id="f3"><i>⏸</i><b>Arrêter</b><small id="f3s" class="hid">Vos données restent accessibles, en lecture</small></div></div>''')
js += pop("#fh", T["choi"] + .05, E, 40) + pop("#f1", T["ren"], "back.out(1.8)", 40) + pop("#f2", T["mois"], "back.out(1.8)", 40)
js += pop("#f3", T["arr"], "back.out(1.8)", 40) + pop("#f3s", T["lect"])
js += f'tl.to("#f3",{{borderColor:"#E9C46A",duration:.4}},{r2(T["lect"])});\n'

# ---------- pourquoi cette offre (pq -> rs)
body += clip("w", "cream", T["pq"], T["rs"], '''
  <div class="eqT" style="top:110px"><div class="h hid" id="wh" style="font-weight:800;letter-spacing:-.02em">Pourquoi <span style="color:#2563EB">cette offre&nbsp;?</span></div></div>
  <div class="why13 hid" id="wc">
    <div class="ln hid" id="w1"><i>1</i><div>Un outil jeune, <span>conçu pour les thérapeutes</span> et les praticiennes en guidance</div></div>
    <div class="ln hid" id="w2"><i>2</i><div>S'équiper pour l'année entière, <span>à un prix simple</span></div></div>
    <div class="ln hid" id="w3"><i>3</i><div>Amélioré chaque semaine <span>grâce à vos retours</span></div></div>
    <div class="sg hid" id="ws">— L'équipe GuidPilot</div></div>''')
js += pop("#wh", T["pq"] + .05, E, 40) + pop("#wc", T["jeune"] - .3, E, 40) + pop("#w1", T["jeune"])
js += pop("#w2", T["pref"] + .6) + pop("#w3", T["sem"]) + pop("#ws", T["sem"] + 1.2)

# ---------- récap (rs -> o)
rc = [("Toutes les fonctions,<br/><span>de la réservation à la facture</span>", "r1", ""),
      ("Un seul paiement&nbsp;:<br/><span>99&nbsp;€, sans prélèvement</span>", "r2", " g"),
      ("Au bout d'un an,<br/><span>vous décidez</span>", "r3", "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += clip("r", "light", T["rs"], T["o"], f'''
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>''')
js += pop("#rk", T["rs"] + .05, E) + "".join(pop(f"#rc{i}", T[k] + .2, y=50) for i, (_, k, _) in enumerate(rc))

# ---------- offre de Noël (o -> z)
body += clip("o", "navy", T["o"], T["z"], '''
  <img src="assets/logo_blanc.png" alt="GuidPilot" style="position:absolute;left:50%;top:40px;width:280px;margin-left:-140px" />
  <div class="top14 hid" id="o14" style="top:140px"><div>Pour commencer&nbsp;: 14 jours gratuits · sans carte bancaire</div></div>
  <div class="xm" style="top:250px"><div class="k">🎁 OFFRE DE NOËL · JUSQU'AU 31 DÉCEMBRE</div>
    <div class="p">1 an pour <span>99&nbsp;€</span></div>
    <div class="s">payé une seule fois</div>
    <div class="c">au lieu de 29&nbsp;€/mois, soit 348&nbsp;€ sur un an</div>
    <div class="np">✓ Aucun prélèvement automatique</div></div>
  <div class="dsc hid" id="od" style="top:900px">↓ <span><b>Le lien</b> est dans la description</span></div>''', logo="")
js += pop("#o14", T["o"] + .1, "back.out(2)") + pop("#od", T["olien"], "back.out(2)")

# ---------- écran de fin (z -> DUR)
t = T["z"]
body += f'''
<div id="z" class="clip navy" data-start="{r2(t)}" data-duration="{r2(DUR - t)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:220px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="endo">🎁 1 an pour 99&nbsp;€</div>
    <div class="endd">Jusqu'au 31 décembre · payé une fois</div>
    <div class="url" style="font-size:44px">guidpilot.fr/offre-fondatrice</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += f'tl.fromTo("#z6",{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.5)"}},{r2(t + .05)});\n'
js += pop("#z9", t + .5) + f'tl.to("#z9",{{scale:1.06,duration:.45,yoyo:true,repeat:2,ease:"sine.inOut"}},{r2(t + 1.1)});\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRAS}{EXTRA13}</style></head><body>
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

d = ATELIER / "build" / "yt-offre-noel-therapeutes"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "finance.png", "avis.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, DUR)
