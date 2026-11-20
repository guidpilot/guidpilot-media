"""Vidéo YouTube 1920x1080 : « Tarologue, voyante, médium : comment gagner du temps dans la gestion de vos consultations »
(PRÉSENTATION + offre de Noël · public guidance, vendredi 20/11/2026 — programme du 17/11 au 31/12/2026).
Usage : python3 gen_consultation_guidance.py <voix.wav> [DUR]  -> build/yt-consultation-guidance/
Voix : 10 paragraphes générés un par un (voix/2026-11-20_yt-consultation-guidance-p1..p10.mp3), assemblés dans l'ordre
avec assembler_voix.py (p4 = CTA oral d'abonnement + rappel de l'offre de Noël, ~30 %). Total 178,1 s.
Structure NOUVELLE « une seule consultation suivie de bout en bout, en écran partagé » : accroche-notification 23:04
(lisible dès l'image 0) -> chemin en 4 étapes -> pour chaque étape, un écran partagé « Habituellement » (gauche, sombre,
compteur de messages qui monte) / « Avec GuidPilot » (droite, claire, qui s'allume quand la voix le dit), barre d'étapes
en haut -> gros plans sur les captures démo finance.png, guid.png, avis.png -> récap 3 cartes -> « combien de messages ? »
-> offre de Noël (20 s) -> écran de fin.
Offre de Noël (exception validée par Normane jusqu'au 31/12/2026) : 99 € payés une fois, 29 €/mois et 348 € en comparaison.
Aucune personne, aucun superlatif, aucune promesse de prédiction ni de gain de temps chiffré.
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

DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 180.2
r2 = lambda x: round(x, 2)


def pop(sel, t, ease="back.out(1.6)", y=30):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{r2(t)});\n'


def fin(sel, t, x=120):
    return f'tl.fromTo("{sel}",{{opacity:0,x:{x},scale:.95}},{{opacity:1,x:0,scale:1,duration:.7,ease:"{E}"}},{r2(t)});\n'


def setv(sel, t, v=1):
    return f'tl.set("{sel}",{{opacity:{v}}},{r2(t)});\n'


EXTRA12 = """
.nt12{position:absolute;left:50%;top:170px;width:1180px;margin-left:-590px;border-radius:36px;background:#fff;box-shadow:0 40px 100px rgba(0,0,0,.45);padding:40px 50px}
.nt12 .ap{display:flex;align-items:center;gap:18px;font-weight:700;font-size:30px;color:#64748B}
.nt12 .ap i{font-style:normal;width:56px;height:56px;border-radius:16px;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px}
.nt12 .ap span{margin-left:auto;font-weight:800;color:#0F172A}
.nt12 .m{font-weight:800;font-size:78px;line-height:1.1;letter-spacing:-.02em;color:#0F172A;margin-top:24px}
.hk12{position:absolute;left:0;right:0;top:590px;text-align:center;font-weight:800;font-size:58px;color:#fff}
.hk12 span{color:#E9C46A}
.chips12{position:absolute;left:0;right:0;top:720px;display:flex;justify-content:center;gap:28px}
.chips12 div{display:flex;align-items:center;gap:16px;padding:22px 38px;border-radius:999px;background:#1E293B;border:2px solid #475569;color:#F1F5F9;font-weight:800;font-size:38px}
.chips12 div i{font-style:normal;color:#E9C46A}
.path12{position:absolute;left:150px;right:150px;top:470px;display:flex;align-items:flex-start;justify-content:space-between}
.path12 .ln{position:absolute;left:90px;right:90px;top:88px;height:8px;border-radius:4px;background:#CBD5E1}
.path12 .ln b{position:absolute;left:0;top:0;bottom:0;width:100%;border-radius:4px;background:#2563EB;transform-origin:left center}
.path12 .s{position:relative;width:340px;text-align:center}
.path12 .s i{font-style:normal;display:flex;margin:0 auto;width:184px;height:184px;border-radius:50%;background:#fff;border:6px solid #2563EB;color:#2563EB;align-items:center;justify-content:center;font-size:84px;font-weight:800;box-shadow:0 20px 50px rgba(15,23,42,.12)}
.path12 .s.g i{border-color:#E9C46A;color:#B7791F}
.path12 .s b{display:block;margin-top:30px;font-weight:800;font-size:44px;color:#0F172A;line-height:1.1}
.ttl12{position:absolute;left:0;right:0;top:150px;text-align:center}
.ttl12 .h{font-weight:800;font-size:76px;letter-spacing:-.02em;color:#0F172A;margin-top:24px}
.ttl12 .h span{color:#2563EB}
.lr12{position:absolute;left:0;right:0;top:840px;display:flex;justify-content:center;gap:40px}
.lr12 div{padding:22px 44px;border-radius:24px;font-weight:800;font-size:40px}
.lr12 .l{background:#1E293B;color:#F1F5F9}.lr12 .r{background:#fff;border:3px solid #2563EB;color:#1D4ED8}
.stp{position:absolute;left:0;right:0;top:0;height:150px;background:#0F172A;display:flex;align-items:center;justify-content:center;gap:16px;z-index:5}
.stp div{display:flex;align-items:center;gap:14px;padding:12px 26px;border-radius:999px;font-weight:800;font-size:28px;color:#64748B;border:2px solid #334155}
.stp div i{font-style:normal;width:42px;height:42px;border-radius:50%;background:#1E293B;color:#94A3B8;display:flex;align-items:center;justify-content:center;font-size:24px}
.stp div.dn{color:#CBD5E1}.stp div.dn i{background:#16A34A;color:#fff}
.stp div.on{background:#E9C46A;border-color:#E9C46A;color:#0F172A}.stp div.on i{background:#0F172A;color:#E9C46A}
.stp .ar{border:0;padding:0;color:#475569;font-size:28px}
.half{position:absolute;top:150px;bottom:0;width:960px;overflow:hidden}
.half.L{left:0;background:#1E293B}
.half.R{left:960px;background:#F6F8FC}
.half .tg{position:absolute;left:70px;top:46px;display:inline-flex;align-items:center;gap:14px;font-weight:800;font-size:30px;letter-spacing:.1em;text-transform:uppercase}
.half.L .tg{color:#FCA5A5}.half.R .tg{color:#2563EB}
.half .tg b{display:flex;width:50px;height:50px;border-radius:50%;align-items:center;justify-content:center;font-size:28px;letter-spacing:0}
.half.L .tg b{background:#7F1D1D;color:#FECACA}.half.R .tg b{background:#2563EB;color:#fff}
.half .hh{position:absolute;left:70px;right:60px;top:120px;font-weight:800;font-size:56px;line-height:1.08;letter-spacing:-.02em}
.half.L .hh{color:#fff;right:270px;font-size:48px}.half.L .hh span{color:#FCA5A5}
.half.R .hh{color:#0F172A}.half.R .hh span{color:#2563EB}
.veil{position:absolute;inset:0;background:#E2E8F0;z-index:4;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:44px;color:#94A3B8}
.cnt12{position:absolute;right:50px;top:36px;width:200px;height:120px;border-radius:24px;background:#0F172A;border:2px solid #475569;text-align:center;z-index:3}
.cnt12 small{display:block;margin-top:12px;font-weight:700;font-size:20px;letter-spacing:.08em;color:#94A3B8}
.cnt12 b{position:absolute;left:0;right:0;top:38px;font-weight:800;font-size:60px;color:#FCA5A5;opacity:0}
.chat{position:absolute;left:70px;right:70px;top:280px}
.bb{display:table;max-width:720px;margin:0 0 12px;padding:12px 26px;border-radius:24px;background:#334155;color:#F1F5F9;font-weight:600;font-size:29px;line-height:1.28}
.bb small{display:block;font-size:20px;font-weight:700;color:#94A3B8;margin-top:6px}
.bb.me{margin-left:auto;background:#2563EB;color:#fff}.bb.me small{color:#BFDBFE}
.bb.vo{display:flex;align-items:center;gap:20px;width:620px}
.bb.vo .pl{flex:none;width:64px;height:64px;border-radius:50%;background:#fff;color:#2563EB;display:flex;align-items:center;justify-content:center;font-size:30px}
.bb.vo .wv{flex:1;height:44px;background:repeating-linear-gradient(90deg,#BFDBFE 0 6px,transparent 6px 12px);border-radius:6px;opacity:.85}
.bb.vo .du{font-weight:800;font-size:28px}
.tag3{display:inline-block;margin:10px 0 24px;padding:10px 24px;border-radius:999px;background:#0F172A;color:#E9C46A;font-weight:800;font-size:28px}
.capL{position:absolute;left:70px;right:70px;bottom:32px;padding:22px 30px;border-radius:22px;background:#7F1D1D;color:#FECACA;font-weight:800;font-size:36px;text-align:center}
.bk12{position:absolute;left:80px;right:80px;top:235px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 26px 70px rgba(15,23,42,.12);padding:34px 40px}
.bk12 .lk{display:inline-flex;align-items:center;gap:12px;padding:10px 22px;border-radius:999px;background:#EFF6FF;color:#1D4ED8;font-weight:800;font-size:24px}
.bk12 .t{font-weight:800;font-size:40px;color:#0F172A;margin-top:20px}
.bk12 .f{display:flex;gap:12px;margin-top:16px}
.bk12 .f span{padding:8px 20px;border-radius:999px;background:#F1F5F9;color:#334155;font-weight:700;font-size:24px}
.bk12 .g{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:24px}
.bk12 .g div{height:70px;border-radius:16px;background:#EFF6FF;border:2px solid #BFDBFE;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:24px;color:#1D4ED8}
.bk12 .g div.x{background:#F1F5F9;border-color:#E2E8F0;color:#94A3B8;text-decoration:line-through}
.bk12 .bt{margin-top:24px;height:78px;border-radius:18px;background:#0F172A;color:#fff;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center}
.okR{position:absolute;left:80px;right:80px;bottom:28px;padding:24px 30px;border-radius:22px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:36px;text-align:center;border:2px solid #86EFAC}
.bnk{position:absolute;left:70px;right:70px;top:430px;border-radius:26px;background:#fff;overflow:hidden}
.bnk .hd{padding:22px 30px;background:#F1F5F9;font-weight:800;font-size:28px;color:#0F172A}
.bnk .rw{display:flex;justify-content:space-between;padding:22px 30px;border-top:2px solid #E2E8F0;font-weight:700;font-size:28px;color:#334155}
.bnk .rw.q{background:#FEF3C7;color:#92400E}
.meet{position:absolute;left:50%;top:520px;margin-left:-380px;width:760px;font-size:36px !important;padding:24px 34px !important;z-index:6;display:flex;align-items:center;justify-content:center;gap:16px;padding:16px 30px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:30px;box-shadow:0 16px 40px rgba(15,23,42,.35)}
.meet i{font-style:normal;color:#E9C46A}
.cap12{position:absolute;left:60px;right:60px;top:280px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 26px 70px rgba(15,23,42,.12);overflow:hidden}
.cap12 img{display:block;width:100%}
.cap12 .dm{position:absolute;right:16px;bottom:12px;font-size:18px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:3px 14px}
.esp{position:absolute;left:80px;right:80px;top:700px;display:flex;align-items:center;gap:24px;padding:26px 32px;border-radius:24px;background:#0F172A;color:#fff;font-weight:800;font-size:34px}
.esp i{font-style:normal;flex:none;width:70px;height:70px;border-radius:20px;background:#1E293B;display:flex;align-items:center;justify-content:center}
.esp small{display:block;font-weight:600;font-size:24px;color:#CBD5E1;margin-top:6px}
.prv{position:absolute;left:80px;bottom:46px;display:inline-flex;align-items:center;gap:14px;padding:16px 30px;border-radius:999px;background:#FBF3DC;border:2px solid #E9C46A;color:#6B4E16;font-weight:800;font-size:30px}
.lst12{position:absolute;left:70px;right:70px;top:300px;display:flex;flex-direction:column;gap:26px}
.lst12 div{display:flex;align-items:center;gap:22px;padding:26px 32px;border-radius:24px;background:#334155;color:#F1F5F9;font-weight:800;font-size:38px}
.lst12 div i{font-style:normal;flex:none;width:60px;height:60px;border-radius:50%;background:#7F1D1D;color:#FECACA;display:flex;align-items:center;justify-content:center;font-size:30px}
.lst12 div small{margin-left:auto;font-weight:700;font-size:24px;color:#FCA5A5}
.inv12{position:absolute;left:80px;right:80px;top:270px;border-radius:28px;padding:36px 40px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 26px 70px rgba(15,23,42,.12)}
.inv12 .k{display:flex;justify-content:space-between;font-weight:800;font-size:28px;letter-spacing:.1em;color:#2563EB}
.inv12 .rw{display:flex;justify-content:space-between;margin-top:26px;font-weight:700;font-size:30px;color:#334155}
.inv12 .ok{display:inline-flex;margin-top:26px;padding:12px 24px;border-radius:999px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:26px}
.ml12{position:absolute;left:80px;right:80px;top:640px;border-radius:24px;padding:28px 34px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.10)}
.ml12 .f{font-weight:700;font-size:22px;color:#64748B}
.ml12 .s{font-weight:800;font-size:32px;color:#0F172A;margin-top:8px}
.ml12 .st{margin-top:12px;font-size:40px;color:#E9C46A;letter-spacing:6px}
.big12{position:absolute;left:0;right:0;top:330px;display:flex;justify-content:center;align-items:center;gap:60px}
.big12 .msg{width:520px;height:340px;border-radius:40px;background:#fff;border:3px solid #E7DFC9;box-shadow:0 24px 60px rgba(15,23,42,.08);display:flex;flex-direction:column;align-items:center;justify-content:center}
.big12 .msg b{font-weight:800;font-size:160px;line-height:1;color:#0F172A}
.big12 .msg small{font-weight:700;font-size:36px;color:#6B4E16;margin-top:14px}
"""

T = dict(
    il=3.05, av=5.83, c1=7.43, c2=8.81, c3=10.19, dans=12.29, suiv=13.42, prem=15.49, verr=17.52,
    q=20.25, dem=21.27, pai=22.15, gui=22.98, fac=23.94, gau=25.61, dro=27.84,
    s1=31.24, hab1=33.16, rep1=35.65, aut1=36.98, plus1=38.44, avec1=40.27, lien1=41.42, page1=42.95, voit1=44.31, form1=45.65,
    cren1=47.92, chois1=50.35, agd1=51.13,
    cta=54.19, abo=57.15, xmas=59.59, x99=61.09, lien=65.24,
    s2=67.52, sans2=69.17, vir2=70.28, bnk2=71.98, rel2=75.72, avec2=76.84, paie2=81.67, tab2=83.16, enc2=84.79,
    s3=86.93, visio3=89.07, hab3=92.20, sem3=95.72, avec3=99.03, aud3=101.83, deux3=103.56, livr3=104.35, ret3=106.69, not3=108.98,
    s4=112.43, fac4=114.99, auto4=116.75, ret4=118.53, avis4=121.76, son4=124.59, lu4=127.24,
    rs=130.40, r1=131.30, r2=135.29, r3=139.68, comb=144.01, compt=145.96,
    o=148.98, onoel=150.49, o99=151.68, opaye=154.06, olieu=155.31, o348=156.83, opre=158.93, oess=160.52, ofin=163.87,
    oren=165.51, omois=166.18, oarr=167.00, oval=168.94,
    z=173.37, zabo=174.2)

body, js = "", ""
STEPS = ["Demande", "Paiement", "Guidance", "Facture et avis"]


def clip(id_, cls, a, b, inner, logo=None):
    lg = logo if logo is not None else (LOGOW if cls in ("navy", "eve", "blue") else LOGO)
    return f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(a)}" data-duration="{r2(b - a)}" data-track-index="1">
  {lg}
{inner}
</div>'''


def stepbar(num):
    out = []
    for i, s in enumerate(STEPS):
        c = "on" if i == num - 1 else ("dn" if i < num - 1 else "")
        out.append(f'<div class="{c}"><i>{"✓" if i < num - 1 else i + 1}</i>{s}</div>')
    return '<div class="stp">' + '<div class="ar">→</div>'.join(out) + '</div>'


def counter(id_, a, b, times):
    """compteur de messages : chiffres a..b, chacun affiché à son temps"""
    h = f'<div class="cnt12"><small>MESSAGES</small>' + "".join(f'<b id="{id_}{n}">{n}</b>' for n in range(a, b + 1)) + '</div>'
    j = setv(f"#{id_}{a}", 0.0 if times[0] is None else times[0])
    for k, n in enumerate(range(a + 1, b + 1)):
        j += setv(f"#{id_}{n - 1}", times[k + 1], 0) + setv(f"#{id_}{n}", times[k + 1])
    return h, j


def split(id_, start, end, num, left, right, avec_t, extra="", logo=""):
    h = f'''
<div id="{id_}" class="clip light" data-start="{r2(start)}" data-duration="{r2(end - start)}" data-track-index="1">
  {stepbar(num)}{logo}
  <div class="half L"><div class="tg"><b>✕</b>Habituellement</div>{left}</div>
  <div class="half R"><div class="tg hid" id="{id_}rt"><b>✓</b>Avec GuidPilot</div>{right}
    <div class="veil" id="{id_}vl">Avec GuidPilot…</div></div>
  {extra}
</div>'''
    j = f'tl.to("#{id_}vl",{{opacity:0,duration:.5}},{r2(avec_t)});\n' + pop(f"#{id_}rt", avec_t + .1, E)
    return h, j


# ---------- A : accroche (0 -> dans) — lisible dès l'image 0
body += clip("a", "navy", 0, T["dans"], '''
  <div class="nt12"><div class="ap"><i>✉</i>Message privé<span>23:04</span></div>
    <div class="m">« Vous êtes dispo pour un tirage ce soir&nbsp;? »</div></div>
  <div class="hk12 hid" id="ah">Et avant le moindre tirage… <span>tout le reste.</span></div>
  <div class="chips12"><div class="hid" id="ac1"><i>1</i>Fixer l'heure</div><div class="hid" id="ac2"><i>2</i>Vérifier le virement</div>
    <div class="hid" id="ac3"><i>3</i>Envoyer la guidance</div></div>''')
js += pop("#ah", T["av"] - .2, E) + pop("#ac1", T["c1"]) + pop("#ac2", T["c2"]) + pop("#ac3", T["c3"])

# ---------- B : une consultation en 4 étapes (dans -> s1)
ps = "".join(f'<div class="s{" g" if k % 2 else ""} hid" id="bp{k}"><i>{k + 1}</i><b>{s}</b></div>' for k, s in enumerate(STEPS))
body += clip("b", "light", T["dans"], T["s1"], f'''
  <div class="ttl12"><div class="chap hid" id="bc"><b>▶</b>Tarologue · voyante · médium</div>
    <div class="h hid" id="bh">Une consultation, <span>du premier message<br/>à la guidance livrée</span></div></div>
  <div class="path12"><div class="ln"><b id="bl"></b></div>{ps}</div>
  <div class="lr12"><div class="l hid" id="bL">◀ Habituellement</div><div class="r hid" id="bR">Avec GuidPilot ▶</div></div>''')
js += pop("#bc", T["dans"] + .05, E) + pop("#bh", T["dans"] + .25, E, 40)
js += f'tl.fromTo("#bl",{{scaleX:0}},{{scaleX:1,duration:4.5,ease:"power1.inOut"}},{r2(T["prem"])});\n'
js += "".join(pop(f"#bp{k}", T[t], "back.out(1.8)", 40) for k, t in enumerate(("q", "pai", "gui", "fac")))
js += pop("#bL", T["gau"], "back.out(2)") + pop("#bR", T["dro"], "back.out(2)")

# ---------- Étape 1 : la demande (s1 -> cta)
ch1, cj1 = counter("k1n", 1, 5, [T["hab1"] + .3, T["rep1"], T["aut1"], T["plus1"] - .6, T["plus1"] - .1])
L1 = ch1 + '''<div class="hh hid" id="e1lh">Fixer une date <span>par messages</span></div>
  <div class="chat" style="top:235px"><div class="bb hid" id="e1b1">Vous êtes dispo pour un tirage ce soir&nbsp;?<small>23:04</small></div>
    <div class="bb me hid" id="e1b2">Ce soir non… demain 18&nbsp;h&nbsp;?<small>Le lendemain · 9:12</small></div>
    <div class="bb hid" id="e1b3">Demain je travaille. Jeudi&nbsp;?<small>12:40</small></div>
    <div class="bb me hid" id="e1b4">Jeudi 19&nbsp;h, ça vous va&nbsp;?<small>14:05</small></div>
    <div class="bb hid" id="e1b5">Parfait&nbsp;!<small>18:31</small></div></div>
  <div class="capL hid" id="e1cap">Plusieurs messages pour une seule date</div>'''
R1 = '''<div class="hh hid" id="e1rh">Un seul lien&nbsp;: <span>votre page</span></div>
  <div class="bk12 hid" id="e1bk"><span class="illus" style="right:20px;top:20px">Illustration</span>
    <div class="lk hid" id="e1lk">🔗 Votre lien de réservation</div>
    <div class="t">Tirage de tarot · 45 min</div>
    <div class="f hid" id="e1f"><span>Visio</span><span>Écrite</span><span>Vocale</span></div>
    <div class="g hid" id="e1g"><div class="x">Mer 18:00</div><div id="e1v">Jeu 19:00</div><div>Ven 10:00</div><div>Sam 9:30</div><div class="x">Sam 14:00</div><div>Lun 18:30</div></div>
    <div class="bt hid" id="e1bt">Réserver</div></div>
  <div class="okR hid" id="e1ok">✓ Rendez-vous ajouté à votre agenda</div>'''
h, j = split("e1", T["s1"], T["cta"], 1, L1, R1, T["avec1"])
body += h; js += j + cj1
js += pop("#e1lh", T["s1"] + .4, E) + pop("#e1b1", T["hab1"] + .3) + pop("#e1b2", T["rep1"]) + pop("#e1b3", T["aut1"])
js += pop("#e1b4", T["plus1"] - .6) + pop("#e1b5", T["plus1"] - .1) + pop("#e1cap", T["plus1"] + .3, "back.out(2)")
js += pop("#e1rh", T["avec1"] + .3, E) + fin("#e1bk", T["lien1"]) + pop("#e1lk", T["page1"], "back.out(2)")
js += pop("#e1f", T["form1"]) + pop("#e1g", T["cren1"] - .3)
js += f'tl.to("#e1v",{{backgroundColor:"#2563EB",borderColor:"#2563EB",color:"#FFFFFF",duration:.3}},{r2(T["chois1"])});\n'
js += pop("#e1bt", T["chois1"] + .3) + pop("#e1ok", T["agd1"] + .4, "back.out(2)")

# ---------- CTA oral abonnement + offre (cta -> s2)
body += clip("cta", "navy", T["cta"], T["s2"], '''
  <div class="ctaC" style="top:110px"><div class="k hid" id="ck">CES VIDÉOS VOUS AIDENT&nbsp;?</div>
    <div class="b hid" id="cb2">2 vidéos par semaine<br/><span>pour votre activité</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="gift hid" id="cg"><div>🎁 Jusqu'au 31 décembre&nbsp;: 1 an pour 99&nbsp;€, payé une fois</div></div>
  <div class="dsc hid" id="cd" style="top:820px">↓ <span><b>Le lien</b> est dans la description</span></div>''')
js += pop("#ck", T["cta"] + .1, E) + pop("#cb2", T["cta"] + .6, E, 40) + pop("#cy", T["abo"], "back.out(2)")
js += f'tl.to("#cy",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(T["abo"] + .8)});\n'
js += pop("#cg", T["xmas"] + .2, "back.out(1.8)") + pop("#cd", T["lien"])

# ---------- Étape 2 : le paiement (s2 -> tab2) puis capture finance (tab2 -> s3)
ch2, cj2 = counter("k2n", 5, 7, [T["s2"] + .2, T["vir2"], T["rel2"]])
L2 = ch2 + '''<div class="hh hid" id="e2lh">« Je vous fais <span>le virement ce soir »</span></div>
  <div class="chat" style="top:280px"><div class="bb hid" id="e2b1">Je vous fais le virement ce soir&nbsp;!<small>Jeudi · 20:15</small></div></div>
  <div class="bnk hid" id="e2bk"><span class="illus" style="right:20px;top:18px">Illustration</span><div class="hd">Relevé de compte</div>
    <div class="rw"><span>Carte · Librairie</span><span>—</span></div>
    <div class="rw q"><span>Virement de… ?</span><span>🔍</span></div>
    <div class="rw"><span>Prélèvement · Téléphone</span><span>—</span></div></div>
  <div class="capL hid" id="e2cap">Et parfois… une relance à écrire</div>'''
R2 = '''<div class="hh hid" id="e2rh">Le règlement fait partie <span>de la réservation</span></div>
  <div class="bk12 hid" id="e2bk2" style="top:330px"><span class="illus" style="right:20px;top:20px">Illustration</span>
    <div class="t">Tirage de tarot · 45 min</div><div class="f"><span>Jeudi · 19:00</span><span>Visio</span></div>
    <div class="bt" style="background:#2563EB">💳 Régler et réserver</div></div>
  <div class="okR hid" id="e2ok">✓ Règlement reçu · réservation confirmée</div>'''
h, j = split("e2", T["s2"], T["tab2"], 2, L2, R2, T["avec2"])
body += h; js += j + cj2
js += pop("#e2lh", T["s2"] + .4, E) + pop("#e2b1", T["vir2"]) + fin("#e2bk", T["bnk2"], -120) + pop("#e2cap", T["rel2"] + .2, "back.out(2)")
js += pop("#e2rh", T["avec2"] + .3, E) + fin("#e2bk2", T["avec2"] + 1.4) + pop("#e2ok", T["paie2"], "back.out(2)")
# finance.png 1270x240 -> 1600x302 ; « À encaisser » x 340-617, y 95-185
sc = 1600 / 1270
body += clip("e2d", "light", T["tab2"], T["s3"], f'''
  <div class="hdr" style="top:120px"><div class="chap hid" id="e2dc"><b>✓</b>Tableau de bord</div>
    <div class="h hid" id="e2dh" style="font-size:70px">Encaissé, <span>et reste à encaisser</span></div></div>
  <div class="capf hid" id="e2cap2" style="left:160px;top:420px;width:1600px"><img src="assets/finance.png" alt="" /><span class="dm">Compte de démonstration</span></div>
  <div class="ring hid" id="e2r" style="left:{r2(160 + 340 * sc - 14)}px;top:{r2(420 + 95 * sc - 14)}px;width:{r2(277 * sc + 28)}px;height:{r2(90 * sc + 28)}px"></div>
  <div class="both hid" id="e2b" style="top:840px"><div>Plus de relevé <span>à fouiller</span></div></div>''')
js += pop("#e2dc", T["tab2"] + .05, E) + pop("#e2dh", T["tab2"] + .25, E, 40) + fin("#e2cap2", T["tab2"] + .5, 0)
js += pop("#e2r", T["enc2"] + .2, "back.out(2)") + pop("#e2b", T["enc2"] + .7, "back.out(2)")

# ---------- Étape 3 : la guidance (s3 -> s4)
ch3, cj3 = counter("k3n", 7, 9, [T["s3"] + .2, T["hab3"] + .4, T["sem3"] + .3])
L3 = ch3 + '''<div class="hh hid" id="e3lh">Un vocal <span>dans une messagerie</span></div>
  <div class="chat" style="top:300px"><div class="bb me vo hid" id="e3b1"><div class="pl">▶</div><div class="wv"></div><div class="du">14:32</div></div>
    <div class="tag3 hid" id="e3t">3 semaines plus tard…</div>
    <div class="bb hid" id="e3b2">Vous pouvez me renvoyer le vocal&nbsp;? Je ne le retrouve plus 😕<small>21:47</small></div></div>
  <div class="capL hid" id="e3cap">La guidance se perd dans le fil</div>'''
# guid.png 1270x561 -> largeur 840 ; badge « Audio » x 217-296, y 253-279
gs = 840 / 1270
R3 = f'''<div class="hh hid" id="e3rh">Écrite, audio, <span>ou les deux</span></div>
  <div class="cap12 hid" id="e3cap2"><img src="assets/guid.png" alt="" /><span class="dm">Compte de démonstration</span></div>
  <div class="ring hid" id="e3r" style="left:{r2(60 + 2 + 210 * gs - 10)}px;top:{r2(280 + 2 + 248 * gs - 10)}px;width:{r2(92 * gs + 20)}px;height:{r2(36 * gs + 20)}px;border-width:5px;border-radius:14px"></div>
  <div class="esp hid" id="e3e"><i>{LOCK.format(s=40, c="#E9C46A")}</i><div>Livrée dans l'espace client sécurisé<small>Votre cliente la retrouve quand elle veut</small></div></div>
  <div class="prv hid" id="e3p">{LOCK.format(s=26, c="#6B4E16")}Vos notes personnelles restent privées</div>'''
h, j = split("e3", T["s3"], T["s4"], 3, L3, R3, T["avec3"], extra='<div class="meet hid" id="e3m"><i>🎥</i>En visio&nbsp;: lien Google Meet prêt</div>')
body += h; js += j + cj3
js += pop("#e3m", T["visio3"], "back.out(2)") + f'tl.to("#e3m",{{opacity:0,duration:.4}},{r2(T["hab3"] + .2)});\n'
js += pop("#e3lh", T["hab3"], E) + pop("#e3b1", T["hab3"] + .4) + pop("#e3t", T["sem3"]) + pop("#e3b2", T["sem3"] + .3)
js += pop("#e3cap", T["sem3"] + 1.4, "back.out(2)")
js += pop("#e3rh", T["avec3"] + .3, E) + fin("#e3cap2", T["avec3"] + 1.0) + pop("#e3r", T["aud3"] + .3, "back.out(2)")
js += pop("#e3e", T["livr3"] + .2, "back.out(1.6)") + pop("#e3p", T["not3"], "back.out(2)")

# ---------- Étape 4 : facture et avis (s4 -> son4) puis capture avis (son4 -> rs)
L4 = '''<div class="hh hid" id="e4lh">Le soir, <span>encore deux tâches</span></div>
  <div class="lst12"><div class="hid" id="e4l1"><i>✕</i>Faire la facture<small>à la main</small></div>
    <div class="hid" id="e4l2"><i>✕</i>Demander un avis<small>souvent oublié</small></div></div>'''
R4 = '''<div class="inv12 hid" id="e4i"><span class="illus" style="right:20px;top:-40px">Illustration</span>
    <div class="k"><span>FACTURE</span><span>N° 2026-112</span></div>
    <div class="rw"><span>Tirage de tarot · 45 min</span><span>Réglée</span></div>
    <div class="ok hid" id="e4ok">✓ Créée automatiquement · dans son espace</div></div>
  <div class="ml12 hid" id="e4m"><span class="illus" style="right:20px;top:-40px">Illustration</span>
    <div class="f">Quelques jours plus tard · e-mail automatique</div><div class="s">Votre avis sur votre consultation&nbsp;?</div>
    <div class="st">★★★★★</div></div>'''
h, j = split("e4", T["s4"], T["son4"], 4, L4, R4, T["fac4"])
body += h; js += j
js += pop("#e4lh", T["s4"] + .5, E) + pop("#e4l1", T["s4"] + 1.2) + pop("#e4l2", T["s4"] + 1.8)
js += f'tl.to("#e4l1",{{opacity:.35,duration:.4}},{r2(T["fac4"] + .2)});\n' + f'tl.to("#e4l2",{{opacity:.35,duration:.4}},{r2(T["avis4"])});\n'
js += fin("#e4i", T["fac4"] + .4) + pop("#e4ok", T["ret4"], "back.out(2)") + fin("#e4m", T["avis4"] + .2)
body += clip("e4d", "light", T["son4"], T["rs"], '''
  <div class="hdr" style="top:110px"><div class="chap hid" id="e4dc"><b>★</b>Avis</div>
    <div class="h hid" id="e4dh" style="font-size:70px">Son avis peut s'afficher <span>sur votre page</span></div></div>
  <div class="capf hid" id="e4cap" style="left:235px;top:360px;width:1450px"><img src="assets/avis.png" alt="" /><span class="dm">Compte de démonstration</span></div>
  <div class="both hid" id="e4b" style="top:840px"><div>Lu par vos futures clientes · <span>avant de réserver</span></div></div>''')
js += pop("#e4dc", T["son4"] + .05, E) + pop("#e4dh", T["son4"] + .25, E, 40) + fin("#e4cap", T["son4"] + .6, 0) + pop("#e4b", T["lu4"], "back.out(2)")

# ---------- récap (rs -> comb)
rc = [("Un seul lien&nbsp;:<br/><span>elle réserve et règle</span>", "r1", ""), ("La guidance,<br/><span>rangée dans son espace</span>", "r2", " g"),
      ("Facture et avis&nbsp;:<br/><span>sans vous</span>", "r3", "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += clip("r", "light", T["rs"], T["comb"], f'''
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>''')
js += pop("#rk", T["rs"] + .05, E) + "".join(pop(f"#rc{i}", T[k] + .2, y=50) for i, (_, k, _) in enumerate(rc))

# ---------- combien de messages ? (comb -> o)
body += clip("c2", "cream", T["comb"], T["o"], '''
  <div class="eqT"><div class="chap hid" id="c2c" style="color:#B7791F"><b style="background:#0F172A;color:#E9C46A">✎</b>Votre dernière consultation</div></div>
  <div class="big12"><div class="msg hid" id="c2m"><b>?</b><small>messages envoyés</small></div></div>
  <div class="eqB hid" id="c2b"><div>Comptez-les&nbsp;: <span>c'est là que se cache votre temps</span></div></div>''')
js += pop("#c2c", T["comb"] + .05, E) + pop("#c2m", T["comb"] + .4, "back.out(2)")
js += f'tl.to("#c2m",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(T["comb"] + 1.2)});\n' + pop("#c2b", T["compt"], "back.out(2)")

# ---------- offre de Noël (o -> z)
body += clip("o", "navy", T["o"], T["z"], '''
  <img src="assets/logo_blanc.png" alt="GuidPilot" style="position:absolute;left:50%;top:50px;width:300px;margin-left:-150px" />
  <div class="top14 hid" id="o14"><div>Essai&nbsp;: 14 jours gratuits · sans carte bancaire</div></div>
  <div class="xm hid" id="oxm"><div class="k">🎁 OFFRE DE NOËL · JUSQU'AU 31 DÉCEMBRE</div>
    <div class="p hid" id="op">1 an pour <span>99&nbsp;€</span></div>
    <div class="s hid" id="os">payé une seule fois</div>
    <div class="c hid" id="oc">au lieu de 29&nbsp;€/mois, soit 348&nbsp;€ sur un an</div>
    <div class="np hid" id="on">✓ Aucun prélèvement automatique</div>
    <div class="ch hid" id="och">À la fin de l'année, vous choisissez&nbsp;:</div>
    <div class="cs"><div class="hid" id="oc0">Renouveler</div><div class="hid" id="oc1">Passer au mois</div><div class="hid" id="oc2">Arrêter · données en lecture</div></div></div>''', logo="")
js += pop("#oxm", T["onoel"], E, 40) + pop("#op", T["o99"] + .4, "back.out(1.6)", 40) + pop("#os", T["opaye"])
js += pop("#oc", T["olieu"]) + pop("#on", T["opre"], "back.out(2)") + pop("#o14", T["oess"], "back.out(2)")
js += pop("#och", T["ofin"]) + pop("#oc0", T["oren"]) + pop("#oc1", T["omois"]) + pop("#oc2", T["oarr"])

# ---------- écran de fin (z -> DUR)
t = T["z"]
body += f'''
<div id="z" class="clip navy" data-start="{r2(t)}" data-duration="{r2(DUR - t)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:230px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="endo">🎁 1 an pour 99&nbsp;€</div>
    <div class="endd">Jusqu'au 31 décembre · payé une fois</div>
    <div class="url" style="font-size:44px">guidpilot.fr/offre-fondatrice</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += f'tl.fromTo("#z6",{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"}},{r2(t + .1)});\n'
js += pop("#z9", T["zabo"]) + f'tl.to("#z9",{{scale:1.06,duration:.45,yoyo:true,repeat:2,ease:"sine.inOut"}},{r2(T["zabo"] + .6)});\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRAS}{EXTRA12}</style></head><body>
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

d = ATELIER / "build" / "yt-consultation-guidance"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "finance.png", "avis.png", "guid.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, DUR)
