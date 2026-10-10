"""Vidéo YouTube / site 1920x1080 (~3 min) : présentation complète de GuidPilot, même style que gen_visibilite.py.
Usage : python3 gen_presentation_complete.py <voix.wav>  -> build/yt-presentation-complete/
Voix : voix/2026-10-10_yt-presentation-complete.mp3 + 0,8 s de silence ajoutés avant chaque paragraphe (11 paragraphes),
voir la fonction ajouter_pauses() ci-dessous. Temps ci-dessous = temps après ajout des pauses.
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_visibilite.py").read_text().split("def phone(")[0]
ns = {"__file__": str(HERE / "gen_visibilite.py")}
exec(src, ns)
CSS, EXTRA, frame, section, ATELIER, KIT = ns["CSS"], ns["EXTRA"], ns["frame"], ns["section"], ns["ATELIER"], ns["KIT"]
DUR = 180.0
T = dict(b=18.3, c=32.9, d=51.8, e=70.9, f=85.0, g=101.2, h=115.7, i=124.2, j=134.7, k=145.0, l=161.3)

EXTRA2 = """
.toolchip{position:absolute;padding:24px 42px;border-radius:22px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:700;font-size:44px;white-space:nowrap}
.kick{font-weight:700;font-size:30px;letter-spacing:.16em;text-transform:uppercase;color:#E9C46A}
.evt{display:flex;align-items:center;gap:26px;margin:16px 0;padding:22px 34px;border-radius:20px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:600;font-size:36px;width:760px}
.evt b{color:#F87171;font-weight:800;width:110px}
.hl{position:absolute;border:5px solid #2563EB;border-radius:18px;box-shadow:0 0 0 8px rgba(37,99,235,.18)}
.fiche{position:absolute;left:900px;top:270px;width:840px;padding:40px 46px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.fiche .who{display:flex;align-items:center;gap:22px}
.fiche .av{width:84px;height:84px;border-radius:50%;background:#EFF6FF;color:#2563EB;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center}
.fiche h4{font-weight:800;font-size:38px}
.hist{margin-top:26px}
.hist div{display:flex;justify-content:space-between;align-items:center;padding:18px 0;border-top:2px solid #F1F5F9;font-weight:600;font-size:28px;color:#334155}
.hist em{font-style:normal;font-size:22px;font-weight:700;padding:6px 16px;border-radius:999px;background:#DCFCE7;color:#166534}
.hist em.b{background:#EFF6FF;color:#2563EB}
.clock{font-weight:800;font-size:120px;color:#fff;letter-spacing:-.03em;line-height:1}
.clock span{color:#E9C46A}
.tl{display:flex;align-items:center;gap:24px;margin:18px 0;padding:22px 32px;border-radius:20px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:700;font-size:36px;width:900px}
.tl i{font-style:normal;flex:none;width:56px;height:56px;border-radius:50%;background:#14532D;color:#4ADE80;display:flex;align-items:center;justify-content:center;font-size:28px}
.tl small{font-weight:600;font-size:24px;color:#94A3B8;margin-left:auto}
.privc{position:absolute;top:320px;width:500px;padding:44px 40px;border-radius:28px;border:2px solid #E2E8F0;background:#fff;box-shadow:0 20px 60px rgba(15,23,42,.08)}
.privc h5{font-weight:800;font-size:38px}
.privc li{list-style:none;font-weight:600;font-size:30px;color:#334155;margin-top:18px;display:flex;gap:14px;align-items:center}
.privc li b{flex:none;width:40px;height:40px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:22px;background:#DCFCE7;color:#16A34A}
.privc li.no b{background:#FEE2E2;color:#DC2626}
.steps3{display:flex;gap:18px;margin-top:30px}
.steps3 div{padding:14px 26px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:700;font-size:28px}
.steps3 b{color:#60A5FA;margin-right:8px}
"""

# --- A : accroche (0 -> 18.3)
tools = [("Agenda", 200, 60), ("WhatsApp", 980, 30), ("Tableur clientes", 480, 210), ("Virements", 1260, 230), ("Factures le soir", 260, 380)]
tool_html = "".join(f'<div class="toolchip" id="t{i}" style="left:{x}px;top:{y}px">{n}</div>' for i, (n, x, y) in enumerate(tools))

hl = lambda id_, x, y, w, h: f'<div class="hl" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>'
dash_frame = frame("ef", "dash.png", 1000, 760, 150).replace(
    'style="width:1000px" /></div></div>',
    'style="width:1000px" />' + hl("h1", 12, 116, 232, 144) + hl("h2", 256, 116, 230, 144) + hl("h3", 497, 116, 231, 144) + hl("h4", 740, 116, 231, 144) + '</div></div>')

body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="{T['b']}" data-track-index="1">
  <div class="center" style="top:150px"><div class="big" id="a1">Tarologue, voyante, médium, <span>énergéticienne</span></div></div>
  <div style="position:absolute;left:110px;right:110px;top:420px;height:520px">{tool_html}</div>
  <div class="center" id="a2" style="top:380px"><div class="big" style="font-size:92px">Et si tout tenait <span>dans un seul espace ?</span></div></div>
  <div class="center" id="a3" style="top:330px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:660px;display:block" />
    <div class="big" style="margin-top:46px;font-size:60px;font-weight:700;color:#CBD5E1">Le logiciel tout-en-un des <span>praticiennes indépendantes</span></div></div>
</div>
<div id="b" class="clip navy" data-start="{T['b']}" data-duration="{round(T['c']-T['b'],2)}" data-track-index="1">
  <div style="position:absolute;left:150px;top:150px;width:860px">
    <div class="kick" id="bk">Pourquoi GuidPilot</div>
    <div class="big" id="b1" style="width:860px;font-size:66px;margin-top:26px;text-align:left">Né en observant le quotidien <span>d'une praticienne en guidance</span></div>
  </div>
  <div style="position:absolute;left:150px;top:560px">
    <div class="evt" id="e1"><b>21 h</b>Répondre aux messages</div>
    <div class="evt" id="e2"><b>22 h</b>Vérifier un virement</div>
    <div class="evt" id="e3"><b>23 h</b>Préparer une facture</div>
  </div>
  <div style="position:absolute;left:1080px;top:380px;width:700px;text-align:center" id="b2">
    <div style="font-weight:800;font-size:58px;color:#fff;line-height:1.15">L'outil s'occupe <span style="color:#60A5FA">de l'organisation.</span></div>
    <div style="font-weight:700;font-size:44px;color:#E9C46A;margin-top:34px">Vous, de vos clientes.</div>
  </div>
</div>
{section("c", T['c'], T['d'], 1, "Votre vitrine", "Votre <span>page praticienne</span>",
  '<div class="p" id="cp">Activité, prestations, tarifs et avis, avec un bouton « Prendre rendez-vous ».</div>'
  '<div class="pill" id="c1"><i>✓</i>Un lien pour votre bio Instagram ou TikTok</div>'
  '<div class="pill" id="c2"><i>✓</i>Visible dans l\'annuaire GuidPilot</div>',
  frame("cf", "page.png", 1000, 760, 150) + frame("cg", "annuaire.png", 1000, 425, 300))}
{section("d", T['d'], T['e'], 2, "Réservation", "Réservation et <span>paiement en ligne</span>",
  '<div style="margin-top:30px">'
  '<div class="step" id="s1"><i>1</i>Elle choisit sa séance</div>'
  '<div class="step" id="s2"><i>2</i>Elle choisit un créneau libre</div>'
  '<div class="step" id="s3"><i>3</i>Elle paie en ligne</div></div>'
  '<div class="tag" id="dt">Selon vos disponibilités</div>',
  '<div class="mock" id="dm"><span class="illus">Illustration</span><h4>Tirage de tarot · Visio</h4><div class="sm">Choisissez un créneau</div>'
  '<div class="slots"><div class="slot off">10:00</div><div class="slot" id="sl">14:00</div><div class="slot">16:30</div>'
  '<div class="slot">18:00</div><div class="slot off">19:00</div><div class="slot">20:30</div></div>'
  '<div class="payb" id="pb">Payer en ligne</div><div class="okpay" id="po">✓ Paiement reçu · Rendez-vous confirmé</div></div>'
  '<div class="msgcount" id="mc">Fini les 10 messages pour fixer une date</div>'
  + frame("df", "dash.png", 1000, 760, 150) +
  '<div class="mock" id="dg" style="top:250px"><span class="illus">Illustration</span><h4>Jeudi · 14:00 – 14:45</h4><div class="sm">Tirage de tarot · Visio</div>'
  '<div class="row"><span>Cliente</span><b>Julie M.</b></div><div class="row"><span>Paiement</span><b style="color:#16A34A">Reçu</b></div>'
  '<div class="meet" id="mb">▶ Rejoindre la visio Google Meet</div></div>')}
{section("e", T['e'], T['f'], 3, "Votre journée", "Tableau de bord <span>et fiches clientes</span>",
  '<div class="p" id="ep">Rendez-vous du jour, guidances à livrer, revenus du mois et note moyenne : l\'essentiel, chaque matin.</div>'
  '<div class="tag" id="et">Une fiche par cliente, avec tout l\'historique</div>',
  dash_frame +
  '<div class="fiche" id="ek"><span class="illus">Illustration</span><div class="who"><div class="av">JM</div><div><h4>Julie M.</h4><div class="sm">Cliente depuis septembre</div></div></div>'
  '<div class="hist"><div>Tirage de tarot · Visio<em>Payé</em></div><div>Guidance écrite et vocale<em class="b">Livrée</em></div>'
  '<div>Facture<em>Envoyée</em></div><div>Messages échangés<em class="b">4</em></div></div></div>')}
<div id="f" class="clip navy" data-start="{T['f']}" data-duration="{round(T['g']-T['f'],2)}" data-track-index="1">
  <div style="position:absolute;left:150px;top:150px">
    <div class="kick" id="fk">Prenons un exemple</div>
    <div class="clock" id="f1" style="margin-top:24px">Mardi <span>23:00</span></div>
  </div>
  <div style="position:absolute;left:150px;top:420px">
    <div class="tl" id="f2"><i>✓</i>Elle réserve un tirage pour jeudi</div>
    <div class="tl" id="f3"><i>✓</i>Elle paie en ligne et reçoit sa confirmation</div>
  </div>
  <div style="position:absolute;left:1120px;top:150px" id="f4">
    <div class="kick">Le lendemain matin</div>
    <div class="tl" id="f5" style="width:650px;margin-top:40px"><i>✓</i>Rendez-vous dans l'agenda</div>
    <div class="tl" id="f6" style="width:650px"><i>✓</i>Fiche cliente créée</div>
    <div class="tl" id="f7" style="width:650px"><i>✓</i>Facture prête</div>
  </div>
  <div class="center" id="f8" style="top:800px"><div class="big" style="font-size:64px">Vous n'avez <span>rien eu à faire.</span></div></div>
</div>
{section("g", T['g'], T['h'], 4, "Guidances", "Guidances <span>écrites et vocales</span>",
  '<div class="pill" id="g1"><i>✓</i>Écrite, vocale, ou les deux</div>'
  '<div class="pill" id="g2"><i>✓</i>Dans l\'espace client sécurisé</div>'
  '<div class="pill" id="g3"><i>✓</i>Rendez-vous, documents, messagerie</div>'
  '<div class="tag" id="gt">Fini les vocaux perdus dans WhatsApp</div>',
  frame("gf", "guid.png", 1000, 442, 300))}
{section("h", T['h'], T['i'], 5, "Confidentialité", "Des données <span>qui restent privées</span>",
  '<div class="p" id="hp">Chaque praticienne a son propre espace.</div>',
  '<div class="privc" id="hc1" style="left:820px"><h5>Ce que vous voyez</h5><ul><li><b>✓</b>Toutes vos clientes</li><li><b>✓</b>Vos notes personnelles</li><li><b>✓</b>Vos revenus et factures</li></ul></div>'
  '<div class="privc" id="hc2" style="left:1350px"><h5>Ce que voit la cliente</h5><ul><li><b>✓</b>Ses rendez-vous</li><li><b>✓</b>Ses guidances</li><li class="no"><b>✕</b>Vos notes personnelles</li></ul></div>')}
{section("i", T['i'], T['j'], 6, "Gestion", "Factures <span>automatiques</span>",
  '<div class="p" id="ip">Chaque paiement génère sa facture. Vos règlements sont suivis au même endroit.</div>',
  frame("if", "finance.png", 1000, 189, 240) +
  '<div id="ib" style="position:absolute;left:820px;width:1000px;top:520px;text-align:center">'
  '<div class="stat">0 %</div><div style="font-weight:800;font-size:46px;margin-top:10px">de commission sur vos séances</div>'
  '<div style="font-weight:500;font-size:26px;color:#64748B;margin-top:12px">hors frais du moyen de paiement</div></div>')}
{section("j", T['j'], T['k'], 7, "Réputation", "Avis clients <span>en un clic</span>",
  '<div class="pill" id="j1"><i>✓</i>Demande en un clic après la séance</div>'
  '<div class="pill" id="j2"><i>✓</i>Relance si besoin</div>'
  '<div class="tag" id="jt">Affichés sur votre page praticienne</div>',
  frame("jf", "avis.png", 1000, 260, 400))}
<div id="k" class="clip navy" data-start="{T['k']}" data-duration="{round(T['l']-T['k'],2)}" data-track-index="1">
  <div style="position:absolute;left:0;right:0;top:100px;text-align:center"><div class="big" style="width:auto;font-size:72px" id="kh">En résumé</div></div>
  <div style="position:absolute;left:500px;top:250px">
    <div class="rec" id="r_1"><i>✓</i>Une page pour être trouvée</div>
    <div class="rec" id="r_2"><i>✓</i>Réservation et paiement en ligne</div>
    <div class="rec" id="r_3"><i>✓</i>Un agenda toujours à jour</div>
    <div class="rec" id="r_4"><i>✓</i>Guidances livrées proprement</div>
    <div class="rec" id="r_5"><i>✓</i>Factures automatiques</div>
    <div class="rec" id="r_6"><i>✓</i>Des avis qui renforcent votre image</div>
  </div>
  <div class="center" id="k7" style="top:880px"><div class="offer" style="font-size:34px">Un seul espace · sur ordinateur comme sur téléphone</div></div>
</div>
<div id="l" class="clip navy" data-start="{T['l']}" data-duration="{round(DUR-T['l'],2)}" data-track-index="1">
  <div class="center" id="l0" style="top:90px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:340px;display:block" />
    <div class="offer" style="margin-top:36px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard" id="l1">✓ Sans carte bancaire</div>
    <div class="url" id="l2" style="margin-top:28px">guidpilot.fr</div>
    <div class="steps3" id="l3"><div><b>1</b>Créez votre page</div><div><b>2</b>Ajoutez vos prestations</div><div><b>3</b>Partagez votre lien</div></div>
    <div class="sub" id="l4" style="margin-top:30px"><i></i>Abonnez-vous à la chaîne GuidPilot</div>
  </div>
</div>'''

E = "power3.out"
def pop(sel, t, ease="back.out(1.6)", y=30):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{t});\n'
def out(sels, t, x=-60):
    s = ",".join(f'"{x_}"' for x_ in sels)
    return f'tl.to([{s}],{{opacity:0,x:{x},duration:.4,ease:"power2.in"}},{t});\n'
def fin(sel, t):
    return f'tl.fromTo("{sel}",{{opacity:0,x:120,scale:.95}},{{opacity:1,x:0,scale:1,duration:.7,ease:"{E}"}},{t});\n'
def head(i, t):
    return pop(f"#{i}c", t + .1, E) + pop(f"#{i}h", t + .25, E, 40)
def light(sel, t):
    return (f'tl.to("{sel}",{{color:"#0F172A",duration:.3}},{t});\n'
            f'tl.to("{sel} i",{{backgroundColor:"#2563EB",color:"#fff",duration:.3}},{t});\n')
def ring(sel, t, d=1.3):
    return (f'tl.fromTo("{sel}",{{opacity:0,scale:1.08}},{{opacity:1,scale:1,duration:.3,ease:"power2.out"}},{t});\n'
            f'tl.to("{sel}",{{opacity:0,duration:.3}},{t+d});\n')

# A
js = pop("#a1", 0.4, E, 50)
js += "".join(f'tl.fromTo("#t{i}",{{opacity:0,y:-80,rotation:{-10 if i%2 else 10}}},{{opacity:1,y:0,rotation:{-3 if i%2 else 3},duration:.5,ease:"back.out(2)"}},{t});\n'
              for i, t in enumerate([6.4, 7.7, 8.8, 10.4, 11.6]))
js += 'tl.to(["#t0","#t2","#t4"],{y:-14,duration:.6,yoyo:true,repeat:1,ease:"sine.inOut"},12.0);\n'
js += 'tl.to(["#t0","#t1","#t2","#t3","#t4","#a1"],{opacity:0,scale:.9,duration:.5,ease:"power2.in"},13.2);\n'
js += 'tl.fromTo("#a2",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.6,ease:"back.out(1.6)"},13.6);\n'
js += 'tl.to("#a2",{opacity:0,y:-30,duration:.4,ease:"power2.in"},15.6);\n'
js += 'tl.fromTo("#a3",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.8,ease:"back.out(1.5)"},16.0);\n'
# B
js += pop("#bk", 18.5) + pop("#b1", 18.8, E)
js += "".join(f'tl.fromTo("#e{i+1}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"}},{t});\n' for i, t in enumerate([22.4, 23.6, 24.8]))
js += 'tl.to(["#e1","#e2","#e3"],{opacity:.35,duration:.5},27.0);\n'
js += 'tl.fromTo("#b2",{opacity:0,x:80},{opacity:1,x:0,duration:.7,ease:"power3.out"},27.2);\n'
# C : page praticienne
js += head("c", T['c']) + fin("#cf", 33.4) + pop("#cp", 35.4, E)
js += 'tl.fromTo("#cfi",{y:0},{y:-200,duration:6,ease:"sine.inOut"},36.0);\n'
js += pop("#c1", 42.7) + out(["#cf"], 45.6) + fin("#cg", 45.9) + pop("#c2", 46.6)
# D : réservation
js += head("d", T['d']) + fin("#dm", 52.2)
js += "".join(light(f"#s{i+1}", t) for i, t in enumerate([52.3, 53.5, 54.9]))
js += 'tl.to("#sl",{backgroundColor:"#2563EB",color:"#fff",borderColor:"#2563EB",scale:1.08,duration:.35},53.7);\n'
js += 'tl.fromTo("#pb",{scale:1},{scale:.95,duration:.15,yoyo:true,repeat:1},55.0);\n'
js += pop("#po", 55.4) + pop("#mc", 56.2, y=20)
js += out(["#dm", "#mc"], 58.7) + fin("#df", 59.1) + pop("#dt", 60.6)
js += 'tl.fromTo("#dfi",{y:0},{y:-123,duration:3,ease:"sine.inOut"},60.0);\n'
js += out(["#df"], 65.2) + fin("#dg", 65.5)
js += 'tl.fromTo("#mb",{scale:1},{scale:1.06,duration:.35,yoyo:true,repeat:5,ease:"sine.inOut"},67.0);\n'
# E : tableau de bord + fiche
js += head("e", T['e']) + fin("#ef", 71.3) + pop("#ep", 72.0, E)
js += ring("#h1", 73.4, 1.2) + ring("#h2", 74.7, 1.2) + ring("#h3", 76.0, .8) + ring("#h4", 76.9, 1.4)
js += out(["#ef"], 79.2) + fin("#ek", 79.5) + pop("#et", 80.0)
js += "".join(pop(f"#ek .hist div:nth-child({n})", 80.4 + n * .5, y=16) for n in range(1, 5))
# F : exemple
js += pop("#fk", 85.3) + 'tl.fromTo("#f1",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.6,ease:"back.out(1.7)"},85.6);\n'
js += pop("#f2", 86.9) + pop("#f3", 91.2)
js += 'tl.fromTo("#f4",{opacity:0,x:60},{opacity:1,x:0,duration:.5,ease:"power3.out"},93.5);\n'
js += pop("#f5", 95.0) + pop("#f6", 96.6) + pop("#f7", 97.9)
js += 'tl.fromTo("#f8",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.6,ease:"back.out(1.6)"},99.4);\n'
# G : guidances
js += head("g", T['g']) + fin("#gf", 101.6) + pop("#g1", 102.4) + pop("#g2", 105.0) + pop("#g3", 108.1) + pop("#gt", 113.2)
# H : confidentialité
js += head("h", T['h']) + pop("#hp", 117.4, E)
js += 'tl.fromTo("#hc1",{opacity:0,y:60},{opacity:1,y:0,duration:.6,ease:"back.out(1.5)"},116.8);\n'
js += 'tl.fromTo("#hc2",{opacity:0,y:60},{opacity:1,y:0,duration:.6,ease:"back.out(1.5)"},119.6);\n'
js += 'tl.fromTo("#hc2 li.no",{scale:1},{scale:1.08,duration:.35,yoyo:true,repeat:3,ease:"sine.inOut"},121.5);\n'
# I : factures
js += head("i", T['i']) + fin("#if", 124.6) + pop("#ip", 125.2, E)
js += 'tl.fromTo("#ib",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.7,ease:"back.out(1.7)"},129.7);\n'
# J : avis
js += head("j", T['j']) + fin("#jf", 135.1) + pop("#j1", 135.6) + pop("#j2", 137.6) + pop("#jt", 139.1)
# K : résumé
js += pop("#kh", 145.2, E)
js += "".join(f'tl.fromTo("#r_{i+1}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"}},{t});\n'
              for i, t in enumerate([146.0, 147.3, 149.3, 150.5, 152.1, 153.0]))
js += pop("#k7", 155.5)
# L : fin
js += 'tl.fromTo("#l0",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},161.4);\n'
js += pop("#l1", 164.6) + pop("#l2", 165.8) + pop("#l3", 167.4) + pop("#l4", 172.1)
js += 'tl.to("#l4",{scale:1.06,duration:.45,yoyo:true,repeat:7,ease:"sine.inOut"},172.8);\n'

hidden = ["#a2", "#a3", "#b2", "#cp", "#c1", "#c2", "#dt", "#po", "#mc", "#ep", "#et", "#f4", "#f5", "#f6", "#f7", "#f8", "#g1", "#g2", "#g3", "#gt",
          "#hp", "#ip", "#ib", "#j1", "#j2", "#jt", "#k7", "#l1", "#l2", "#l3", "#l4", "#h1", "#h2", "#h3", "#h4"]
html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA2}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1920" data-height="1080">
<div class="aibadge">Voix off générée par IA</div>
<audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
{body}
</div>
<script>
const tl=gsap.timeline({{paused:true}});
tl.set({hidden!r},{{opacity:0}},0);
{js}
window.__timelines["main"]=tl;
</script></body></html>'''


def ajouter_pauses(src_wav, dst_wav, cuts=(17.81, 31.62, 49.67, 67.95, 81.26, 96.70, 110.42, 118.04, 127.82, 137.24, 152.75), gap=0.8):
    """Insère `gap` s de silence juste avant chaque début de paragraphe (temps mesurés sur la voix brute)."""
    import wave, numpy as np
    w = wave.open(str(src_wav)); sr = w.getframerate(); ch = w.getnchannels()
    a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, ch)
    z = np.zeros((int(gap * sr), ch), dtype=np.int16); parts = []; prev = 0
    for c in cuts:
        i = int((c - 0.08) * sr); parts += [a[prev:i], z]; prev = i
    parts.append(a[prev:])
    o = wave.open(str(dst_wav), "wb"); o.setnchannels(ch); o.setsampwidth(2); o.setframerate(sr)
    o.writeframes(np.concatenate(parts).tobytes()); o.close()


if __name__ == "__main__":
    d = ATELIER / "build" / "yt-presentation-complete"
    if d.exists(): shutil.rmtree(d)
    (d / "assets").mkdir(parents=True)
    for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
    for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
    for a in ("page.png", "dash.png", "annuaire.png", "guid.png", "finance.png", "avis.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
    shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
    shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
    (d / "index.html").write_text(html)
    print("ok", d)
