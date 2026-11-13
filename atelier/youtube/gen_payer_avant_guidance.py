"""Vidéo YouTube 1920x1080 : « Comment se faire payer avant une consultation de voyance ou de tarot, sans gêne »
(CONSEIL · public guidance, vendredi 13/11/2026).
Usage : python3 gen_payer_avant_guidance.py <voix.wav> [DUR]  -> build/yt-payer-avant/
Voix : 9 paragraphes générés un par un (voix/2026-11-13_yt-payer-avant-p1..p9.mp3), assemblés dans l'ordre p1..p9
avec assembler_voix.py (p3 = CTA oral d'abonnement après le réflexe 1, ~30 %). Total 163,1 s.
Temps T = début des phrases (silencedetect -30 dB / 0,15 s et 0,28 s sur le wav assemblé + découpage des phrases).
Structure « 4 réflexes sur une frise » (nouvelle) : chaque réflexe s'ouvre sur une carte plein écran à fond changeant
avec une frise en 4 étapes (Avant · Réservation · La question · Conditions) qui avance -> problème illustré ->
phrase prête à copier. GuidPilot seulement à la fin (~15 s + fin).
Aucune personne, aucun prix GuidPilot, aucun superlatif, aucune promesse de résultat, aucun conseil juridique.
Réutilise CSS et helpers de gen_trouver_clientes_therapeutes.py (lui-même basé sur gen_logiciel_reiki.py).
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_trouver_clientes_therapeutes.py").read_text()
ns = {"__file__": str(HERE / "gen_trouver_clientes_therapeutes.py")}
_argv = sys.argv[:]
sys.argv = sys.argv[:2]
exec(src.split("\nT = dict(")[0], ns)
sys.argv = _argv
CSS, EXTRA, EXTRA4, EXTRA5, EXTRA7, EXTRA8, EXTRA9, ATELIER, KIT = (ns[k] for k in ("CSS", "EXTRA", "EXTRA4", "EXTRA5", "EXTRA7", "EXTRA8", "EXTRA9", "ATELIER", "KIT"))
pop, fin, phone, LOGO, LOGOW, E = (ns[k] for k in ("pop", "fin", "phone", "LOGO", "LOGOW", "E"))

DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 166.0
r2 = lambda x: round(x, 2)

EXTRA10 = """
.fz{position:absolute;left:150px;top:0;bottom:0;width:1620px;display:flex;flex-direction:column;justify-content:center}
.fz .n{display:inline-flex;align-items:center;gap:22px;font-weight:800;font-size:32px;letter-spacing:.14em;text-transform:uppercase}
.fz .n b{display:inline-flex;width:84px;height:84px;border-radius:50%;align-items:center;justify-content:center;font-size:44px;letter-spacing:0}
.fz .t{font-weight:800;font-size:112px;line-height:1.04;letter-spacing:-.035em;margin-top:36px;max-width:1600px}
.fz .w{font-weight:700;font-size:34px;margin-top:30px;opacity:.85}
.fz .fr{position:relative;display:flex;justify-content:space-between;width:1500px;margin-top:80px}
.fz .fr .ln{position:absolute;left:30px;right:30px;top:28px;height:6px;border-radius:3px;opacity:.25}
.fz .fr .st{position:relative;display:flex;flex-direction:column;align-items:center;gap:16px;width:260px;font-weight:700;font-size:26px;opacity:.45}
.fz .fr .st i{font-style:normal;width:62px;height:62px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px}
.fz .fr .st.on{opacity:1}
.fz .fr .st.on i{transform:scale(1.25)}
.cream .fz .n{color:#B7791F}.cream .fz .n b{background:#0F172A;color:#E9C46A}.cream .fz .t{color:#0F172A}.cream .fz .t span{color:#2563EB}.cream .fz .w{color:#6B4E16}
.cream .fz .fr .ln{background:#0F172A}.cream .fz .fr .st{color:#0F172A}.cream .fz .fr .st i{background:#fff;border:3px solid #0F172A;color:#0F172A}.cream .fz .fr .st.on i{background:#0F172A;color:#E9C46A}
.navy .fz .n{color:#93C5FD}.navy .fz .n b{background:#E9C46A;color:#0F172A}.navy .fz .t{color:#fff}.navy .fz .t span{color:#E9C46A}.navy .fz .w{color:#CBD5E1}
.navy .fz .fr .ln{background:#E9C46A}.navy .fz .fr .st{color:#fff}.navy .fz .fr .st i{background:#1E293B;border:3px solid #E9C46A;color:#E9C46A}.navy .fz .fr .st.on i{background:#E9C46A;color:#0F172A}
.blue .fz .n{color:#BFDBFE}.blue .fz .n b{background:#fff;color:#1D4ED8}.blue .fz .t{color:#fff}.blue .fz .t span{color:#E9C46A}.blue .fz .w{color:#DBEAFE}
.blue .fz .fr .ln{background:#fff}.blue .fz .fr .st{color:#fff}.blue .fz .fr .st i{background:#1D4ED8;border:3px solid #fff;color:#fff}.blue .fz .fr .st.on i{background:#fff;color:#1D4ED8}
.blue{background:#2563EB;color:#fff}
.st10{display:inline-flex;align-items:center;gap:14px;margin:6px 20px 0 auto;padding:10px 20px;border-radius:999px;background:#FEE2E2;color:#B91C1C;font-weight:800;font-size:22px}
.day10{text-align:center;margin:16px 0 4px;font-weight:700;font-size:20px;color:#94A3B8}
.pend10{position:absolute;left:110px;top:930px;display:flex;gap:22px}
.pend10 div{padding:18px 32px;border-radius:999px;font-weight:800;font-size:36px}
.pend10 .a{background:#1E293B;border:2px solid #475569;color:#F1F5F9}
.pend10 .b{background:#7F1D1D;color:#FECACA}
.qbig{align-self:flex-start;padding:44px 64px;border-radius:56px;border-bottom-left-radius:14px;font-weight:800;font-size:96px;line-height:1.06;letter-spacing:-.035em;background:#0F172A;color:#fff}
.nolist{display:flex;gap:30px;margin-top:60px}
.nolist div{display:flex;align-items:center;gap:18px;padding:22px 34px;border-radius:24px;background:rgba(255,255,255,.14);border:2px solid rgba(255,255,255,.35);font-weight:800;font-size:40px;color:#fff}
.nolist div i{font-style:normal;width:56px;height:56px;border-radius:50%;background:#DC2626;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px}
.cp10{display:flex;width:fit-content;align-items:center;gap:12px;margin:14px 22px 0 auto;padding:10px 22px;border-radius:999px;background:#0F172A;color:#E9C46A;font-weight:800;font-size:22px}
.b8.lg{max-width:360px;font-size:24px}
.cond{position:absolute;left:990px;top:250px;width:820px;border-radius:30px;padding:46px;background:#fff;border:3px solid #2563EB;box-shadow:0 30px 80px rgba(37,99,235,.15)}
.cond .k{font-weight:800;font-size:28px;letter-spacing:.12em;color:#2563EB}
.cond .row{display:flex;align-items:center;gap:20px;margin-top:30px;font-weight:700;font-size:34px;color:#334155}
.cond .row i{font-style:normal;flex:none;width:56px;height:56px;border-radius:16px;background:#EFF6FF;color:#2563EB;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800}
.qq{display:flex;flex-direction:column;gap:26px;margin-top:40px;background:none!important;border:0!important;box-shadow:none!important;padding:0!important}
.qq div{align-self:flex-start;padding:24px 36px;border-radius:30px;border-bottom-left-radius:10px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07);font-weight:800;font-size:42px;color:#0F172A}
.nop{display:flex;gap:20px;margin-top:34px}
.nop div{padding:16px 30px;border-radius:999px;background:#7F1D1D;color:#FECACA;font-weight:800;font-size:32px;text-decoration:line-through;text-decoration-thickness:3px}
"""

T = dict(
    pai=1.72, rien=2.48, heure=3.45, ecrit=7.33, vir=8.96, douze=10.49, rel=12.28, pourt=13.70, vid=16.09, quatre=17.6, phr=21.26,
    r1=24.03, gene=26.59, avant=29.12, i1=32.34, i2=33.21, i3=34.07, i4=37.28, ecr=38.39, meme=40.50, fil=41.51, clair=42.89, disc=44.74, etape=46.56,
    cta=48.76, abo=50.40, deux=51.22, lien=55.0,
    r2=60.43, r2b=61.57, gv=63.70, trav=65.47, apres=67.82, av=68.83, regle=70.61, pas=72.19, douc=74.12, msg=75.86, rec=77.52,
    r3=81.58, r3b=82.91, q=85.49, just=87.46, baiss=89.15, calme=90.62, comp=92.2, toutes=93.61, perm=97.28, lienq=99.24, chal=101.82, meme3=103.34,
    r4=106.11, r4b=108.32, ann=111.49, depl=113.17, ecr4=115.47, manq=118.36, rap=121.87, repr=123.78, raf=124.68,
    rs=126.77, s1=127.97, s2=132.85, s3=137.32,
    g=141.19, gres=146.94, gfac=150.12, grap=151.90, gclic=153.67,
    z=156.26, url=159.17, zabo=161.80)

body, js = "", ""
STEPS = ["Avant", "Réservation", "La question", "Conditions"]


def fcard(id_, start, end, num, title, cls, logo, lead):
    st = "".join(f'<div class="st{" on" if i == num - 1 else ""}"><i>{"✓" if i < num - 1 else i + 1}</i>{s}</div>' for i, s in enumerate(STEPS))
    h = f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(start)}" data-duration="{r2(end - start)}" data-track-index="1">
  {logo}
  <div class="fz"><div class="n hid" id="{id_}n"><b>{num}</b>Réflexe {num} sur 4</div>
    <div class="t hid" id="{id_}t">{title}</div><div class="w hid" id="{id_}w">{lead}</div>
    <div class="fr"><div class="ln"></div>{st}</div></div>
</div>'''
    j = pop(f"#{id_}n", start + .05, E) + pop(f"#{id_}t", start + .2, "back.out(1.3)", 50) + pop(f"#{id_}w", start + .9)
    return h, j


# ---------- A : accroche (0 -> vid) — lisible dès l'image 0
conv = ('<div class="phead"><div class="av">É</div>Émilie R.</div>'
        '<div style="position:absolute;left:0;right:0;top:150px">'
        '<div class="day10">Il y a 12 jours</div>'
        '<div class="b8 me">Voici votre guidance audio, comme promis.</div>'
        '<div class="b8 me au"><b>▶</b><span></span></div>'
        '<div class="b8 hid" id="am1">Merci&nbsp;! Je vous fais le virement ce soir 🙏</div>'
        '<div class="day10 hid" id="am2">Aujourd\'hui</div>'
        '<div class="st10 hid" id="am3">● Règlement en attente</div></div>')
body += f'''
<div id="a" class="clip navy" data-start="0" data-duration="{r2(T["vid"])}" data-track-index="1">
  <div class="hk9" style="top:250px;width:960px"><div class="q">Guidance envoyée.<br/><span>Paiement&nbsp;: toujours rien.</span></div>
    <div class="s hid" id="as1">Une heure sur son tirage.<br/><b>Un audio enregistré avec soin.</b></div></div>
  <div class="pend10"><div class="a hid" id="ap1">Relancer&nbsp;? Mal à l'aise…</div><div class="b hid" id="ap2">Votre temps, déjà donné</div></div>
  {phone("aph", conv, 1290, 100)}
</div>'''
js += fin("#aph", .05) + pop("#as1", T["heure"] + .1, E) + pop("#am1", T["vir"]) + pop("#am2", T["douze"]) + pop("#am3", T["douze"] + .5, "back.out(2)")
js += pop("#ap1", T["rel"]) + pop("#ap2", T["pourt"] + .4, "back.out(2)")

# ---------- B : promesse (vid -> r1)
tl4 = [("1", "Tout annoncer", "avant", ""), ("2", "Régler", "à la réservation", "g"), ("3", "Une réponse", "prête", ""), ("4", "Des conditions", "écrites", "g")]
th = "".join(f'<div class="c {g} hid" id="bt{k}"><i>{n}</i><div><b>{a}</b><small>{s}</small></div></div>' for k, (n, a, s, g) in enumerate(tl4))
body += f'''
<div id="b" class="clip light" data-start="{r2(T["vid"])}" data-duration="{r2(T["r1"] - T["vid"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="bc"><b>4</b>Réflexes</div>
    <div class="h hid" id="bh" style="font-size:72px">Être payée <span>avant la consultation</span></div></div>
  <div class="t4" style="top:390px">{th}</div>
  <div class="both hid" id="bs" style="top:880px"><div>Sans paraître insistante · <span>phrases à copier</span></div></div>
</div>'''
js += pop("#bc", T["vid"] + .05, E) + pop("#bh", T["vid"] + .25, E, 40)
js += "".join(pop(f"#bt{k}", T["quatre"] + .2 + k * .6, y=50) for k in range(4)) + pop("#bs", T["phr"], "back.out(2)")

# ---------- Réflexe 1
h, j = fcard("f1", T["r1"], T["gene"], 1, "Annoncez tout, <span>avant</span>", "cream", LOGO, "Avant même qu'elle réserve")
body += h; js += j

# R1 : la surprise (gene -> avant)
sur = ('<div class="phead"><div class="av">S</div>Sophie L.</div>'
       '<div style="position:absolute;left:0;right:0;top:170px">'
       '<div class="b8 me">Votre guidance est prête. Voici le règlement à effectuer.</div>'
       '<div class="b8 hid" id="g1b">Ah… c\'est ce prix-là&nbsp;? Je pensais que c\'était moins 😕</div></div>')
body += f'''
<div id="g1" class="clip eve" data-start="{r2(T["gene"])}" data-duration="{r2(T["avant"] - T["gene"])}" data-track-index="1">
  {LOGOW}
  <div class="hk9" style="top:330px;width:980px"><div class="q" style="font-size:96px">La gêne vient souvent <span>d'une surprise.</span></div></div>
  {phone("g1ph", sur, 1290, 100)}
</div>'''
js += fin("#g1ph", T["gene"] + .2) + pop("#g1b", T["gene"] + 1.0, "back.out(2)")

# R1 : les 4 infos (avant -> ecr)
inf = [("€", "Le tarif", "Affiché clairement", ""), ("⏱", "La durée", "Ou la longueur", "g"),
       ("✎", "Le format", "Écrit, vocal ou visio", ""), ("↦", "Le délai", "De livraison", "g")]
ih = "".join(f'<div class="c {g} hid" id="i1t{k}"><i>{ic}</i><div><b>{a}</b><small>{s}</small></div></div>' for k, (ic, a, s, g) in enumerate(inf))
body += f'''
<div id="i1" class="clip light" data-start="{r2(T["avant"])}" data-duration="{r2(T["ecr"] - T["avant"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="i1c"><b>1</b>Les 4 infos</div>
    <div class="h hid" id="i1h" style="font-size:66px">Ce qu'elle doit savoir <span>avant de réserver</span></div></div>
  <div class="t4">{ih}</div>
</div>'''
js += pop("#i1c", T["avant"] + .05, E) + pop("#i1h", T["avant"] + .25, E, 40)
js += "".join(pop(f"#i1t{k}", T[f"i{k + 1}"], y=50) for k in range(4))

# R1 : une fiche par prestation (ecr -> cta)
body += f'''
<div id="p1" class="clip light" data-start="{r2(T["ecr"])}" data-duration="{r2(T["cta"] - T["ecr"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:800px;top:-90px"><div class="chap hid" id="p1c"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="p1h" style="font-size:70px">Sur chaque prestation,<br/><span>au même endroit</span></div>
    <div class="ok8 hid" id="p1o" style="color:#B91C1C"><i style="background:#DC2626">✕</i>Pas au fil des messages</div></div>
  <div class="pres hid" id="p1p" style="left:990px;height:600px;top:170px"><span class="illus" style="right:24px;top:24px">Exemple</span>
    <div class="ic" style="background:#FBF3DC;color:#B7791F;font-size:52px;font-weight:800">✎</div><div class="tt">Guidance écrite · Tarot</div>
    <div class="row"><i>€</i>Votre tarif, affiché</div><div class="row"><i>⏱</i>Tirage complet en 10 cartes</div>
    <div class="row"><i>✎</i>Format : écrit</div><div class="row"><i>↦</i>Livrée sous 48 h</div></div>
  <div class="both hid" id="p1b" style="top:880px"><div>Le paiement devient <span>l'étape suivante</span></div></div>
</div>'''
js += pop("#p1c", T["ecr"] + .05, E) + pop("#p1h", T["ecr"] + .25, E, 40) + fin("#p1p", T["ecr"] + .5)
js += pop("#p1o", T["fil"]) + pop("#p1b", T["disc"], "back.out(2)")

# ---------- CTA oral abonnement (cta -> r2)
body += f'''
<div id="cta" class="clip navy" data-start="{r2(T["cta"])}" data-duration="{r2(T["r2"] - T["cta"])}" data-track-index="1">
  {LOGOW}
  <div class="ctaC"><div class="k hid" id="ck">CES CONSEILS VOUS SONT UTILES&nbsp;?</div>
    <div class="b hid" id="cb">2 vidéos par semaine<br/><span>pour organiser votre activité</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="dsc hid" id="cd">↓ <span><b>Essai gratuit&nbsp;:</b> le lien est dans la description</span></div>
</div>'''
js += pop("#ck", T["cta"] + .1, E) + pop("#cy", T["abo"], "back.out(2)") + pop("#cb", T["deux"], E, 40)
js += f'tl.to("#cy",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(T["abo"] + 1.4)});\n' + pop("#cd", T["lien"] + .2)

# ---------- Réflexe 2
h, j = fcard("f2", T["r2"], T["gv"], 2, "Le règlement fait partie <span>de la réservation</span>", "navy", LOGOW, "Pas une étape à part, après coup")
body += h; js += j

# R2 : payer après = avancer son temps (gv -> regle)
body += f'''
<div id="c2" class="clip cream" data-start="{r2(T["gv"])}" data-duration="{r2(T["regle"] - T["gv"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="c2c" style="color:#B7791F"><b style="background:#0F172A;color:#E9C46A">✎</b>Guidance écrite ou vocale</div>
    <div class="h hid" id="c2h" style="font-size:66px;color:#0F172A">Votre travail commence <span>dès qu'elle réserve</span></div></div>
  <div class="chain" style="top:390px;width:820px"><div class="st hid" id="c2s0"><b>1</b>Elle réserve</div>
    <div class="st hid" id="c2s1"><b>2</b>Vous tirez les cartes, vous écrivez</div><div class="st hid" id="c2s2"><b>3</b>Vous livrez</div>
    <div class="st hid" id="c2s3" style="border-color:#FCA5A5;background:#FEF2F2;color:#B91C1C"><b style="background:#DC2626">?</b>Elle paie… plus tard&nbsp;?</div></div>
  <div class="eff9 hid" id="c2e" style="left:1030px;top:520px;font-size:44px">Payer après =<br/>avancer votre temps</div>
</div>'''
js += pop("#c2c", T["gv"] + .05, E) + pop("#c2h", T["gv"] + .25, E, 40)
js += pop("#c2s0", T["trav"]) + pop("#c2s1", T["trav"] + .7) + pop("#c2s2", T["trav"] + 1.4) + pop("#c2s3", T["apres"], "back.out(2)") + pop("#c2e", T["av"] + .2, "back.out(1.6)")

# R2 : la règle (regle -> douc)
body += f'''
<div id="c2r" class="clip navy" data-start="{r2(T["regle"])}" data-duration="{r2(T["douc"] - T["regle"])}" data-track-index="1">
  {LOGOW}
  <div class="ctaC" style="top:280px"><div class="k hid" id="c2rk">LA RÈGLE LA PLUS SIMPLE</div>
    <div class="b hid" id="c2rb">Pas de créneau confirmé<br/><span>sans règlement</span></div></div>
</div>'''
js += pop("#c2rk", T["regle"] + .1, E) + pop("#c2rb", T["pas"] - .2, "back.out(1.4)", 50)

# R2 : phrase à copier (douc -> r3)
m2 = ('<div class="phead"><div class="av">C</div>Claire D.</div>'
      '<div style="position:absolute;left:0;right:0;top:170px">'
      '<div class="b8">Bonjour, je viens de réserver une guidance écrite&nbsp;!</div>'
      '<div class="b8 me lg hid" id="c2m1">Merci&nbsp;! Dès réception de votre règlement, je prépare votre guidance. Vous la recevrez sous 48&nbsp;h.</div>'
      '<div class="cp10 hid" id="c2m2">⧉ À copier</div></div>')
body += f'''
<div id="c2c2" class="clip light" data-start="{r2(T["douc"])}" data-duration="{r2(T["r3"] - T["douc"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px"><div class="chap hid" id="c2pc"><b>✓</b>Prêt à copier</div>
    <div class="h hid" id="c2ph1" style="font-size:76px">Dites-le<br/><span>avec douceur</span></div>
    <div class="ok8 hid" id="c2po1"><i>✓</i>Ce que vous faites</div><div class="ok8 hid" id="c2po2"><i>✓</i>Quand elle la reçoit</div></div>
  {phone("c2ph", m2, 1240, 100)}
</div>'''
js += pop("#c2pc", T["douc"] + .05, E) + pop("#c2ph1", T["douc"] + .25, E, 40) + fin("#c2ph", T["douc"] + .4)
js += pop("#c2m1", T["msg"]) + pop("#c2m2", T["msg"] + 1.2, "back.out(2)") + pop("#c2po1", T["msg"] + .6) + pop("#c2po2", T["rec"] + .2)

# ---------- Réflexe 3
h, j = fcard("f3x", T["r3"], T["q"], 3, "Préparez la réponse <span>à la question qui gêne</span>", "blue", LOGOW, "Celle qui revient toujours")
body += h; js += j

# R3 : la question (q -> calme)
body += f'''
<div id="c3q" class="clip blue" data-start="{r2(T["q"])}" data-duration="{r2(T["calme"] - T["q"])}" data-track-index="1">
  {LOGOW}
  <div class="qb"><div class="qbig hid" id="c3qb">«&nbsp;Je peux payer après&nbsp;?&nbsp;»</div>
    <div class="nolist"><div class="hid" id="c3n0"><i>✕</i>Vous justifier longuement</div><div class="hid" id="c3n1"><i>✕</i>Baisser votre prix</div></div></div>
</div>'''
js += pop("#c3qb", T["q"] + .05, "back.out(1.4)", 50) + pop("#c3n0", T["just"] + .2) + pop("#c3n1", T["baiss"] + .1)

# R3 : la réponse calme (calme -> chal)
m3 = ('<div class="phead"><div class="av">M</div>Marion B.</div>'
      '<div style="position:absolute;left:0;right:0;top:150px">'
      '<div class="b8">Je peux payer après la séance&nbsp;?</div>'
      '<div class="b8 me lg hid" id="c3m1" style="max-width:380px">Je comprends. Pour toutes mes consultations, le règlement se fait à la réservation&nbsp;: c\'est ce qui me permet de vous réserver ce temps.</div>'
      '<div class="b8 me lg hid" id="c3m2">Le lien est ici, quand vous êtes prête&nbsp;:</div>'
      '<div class="lnk9 hid" id="c3m3"><div class="a">🔗 Réserver et régler</div><div class="b">Lien direct</div></div></div>')
body += f'''
<div id="c3r" class="clip light" data-start="{r2(T["calme"])}" data-duration="{r2(T["chal"] - T["calme"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px"><div class="chap hid" id="c3rc"><b>✓</b>Prêt à copier</div>
    <div class="h hid" id="c3rh" style="font-size:76px">Une réponse<br/><span>calme suffit</span></div>
    <div class="ok8 hid" id="c3ro1"><i>✓</i>Elle se sent comprise</div><div class="ok8 hid" id="c3ro2"><i>✓</i>La règle est claire</div></div>
  {phone("c3ph", m3, 1240, 90)}
</div>'''
js += pop("#c3rc", T["calme"] + .05, E) + pop("#c3rh", T["calme"] + .25, E, 40) + fin("#c3ph", T["calme"] + .4)
js += pop("#c3m1", T["comp"]) + pop("#c3ro1", T["comp"] + .6) + pop("#c3ro2", T["toutes"] + 1.5) + pop("#c3m2", T["lienq"]) + pop("#c3m3", T["lienq"] + .9, "back.out(2)")

# R3 : chaleureuse et la même règle (chal -> r4)
body += f'''
<div id="c3s" class="clip cream" data-start="{r2(T["chal"])}" data-duration="{r2(T["r4"] - T["chal"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:1500px"><div class="h hid" id="c3sh" style="font-size:76px;color:#0F172A">Douce dans le ton,<br/><span>ferme sur la règle</span></div>
    <div class="lc9"><div class="hid" id="c3s0"><i>♡</i>Vous restez chaleureuse</div>
      <div class="hid" id="c3s1"><i>=</i>La même règle pour toutes</div></div></div>
</div>'''
js += pop("#c3sh", T["chal"] + .05, E, 40) + pop("#c3s0", T["chal"] + .5, y=40) + pop("#c3s1", T["meme3"], y=40)

# ---------- Réflexe 4
h, j = fcard("f4", T["r4"], T["ann"], 4, "Écrivez vos conditions <span>avant un souci</span>", "cream", LOGO, "Le dernier réflexe… celui qu'on oublie")
body += h; js += j

# R4 : les questions + conditions (ann -> manq)
body += f'''
<div id="c4" class="clip light" data-start="{r2(T["ann"])}" data-duration="{r2(T["manq"] - T["ann"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px"><div class="chap hid" id="c4c"><b>?</b>À prévoir</div>
    <div class="qq"><div class="hid" id="c4q0">Et si elle annule&nbsp;?</div><div class="hid" id="c4q1">Jusqu'à quand<br/>peut-elle déplacer&nbsp;?</div></div></div>
  <div class="cond hid" id="c4d"><span class="illus" style="right:24px;top:24px">Exemple</span><div class="k">MES CONDITIONS</div>
    <div class="row"><i>↻</i>Report possible jusqu'à 24 h avant</div>
    <div class="row"><i>✕</i>Annulation : vos règles, écrites</div>
    <div class="row"><i>✎</i>Délai de livraison rappelé</div>
    <div class="row hid" id="c4v" style="color:#2563EB"><i style="background:#2563EB;color:#fff">👁</i>Visibles avant le paiement</div></div>
</div>'''
js += pop("#c4c", T["ann"] + .05, E) + pop("#c4q0", T["ann"] + .2) + pop("#c4q1", T["depl"]) + fin("#c4d", T["ecr4"]) + pop("#c4v", T["ecr4"] + 1.4, "back.out(2)")

# R4 : un seul rappel (manq -> rs)
m4 = ('<div class="phead"><div class="av">CE</div>Cabinet Exemple</div>'
      '<div style="position:absolute;left:0;right:0;top:200px">'
      '<div class="b8 me lg hid" id="c4m1">Bonjour, petit rappel&nbsp;: le règlement de votre guidance du 3 novembre est en attente. Voici le lien&nbsp;:</div>'
      '<div class="lnk9 hid" id="c4m2"><div class="a">🔗 Régler ma guidance</div><div class="b">Lien direct</div></div></div>')
body += f'''
<div id="c4r" class="clip eve" data-start="{r2(T["manq"])}" data-duration="{r2(T["rs"] - T["manq"])}" data-track-index="1">
  {LOGOW}
  <div class="hk9" style="top:250px;width:900px"><div class="q" style="font-size:96px">Un règlement manque&nbsp;?<br/><span>Un seul rappel.</span></div>
    <div class="s hid" id="c4rs"><b>Court · factuel · avec le lien</b></div>
    <div class="nop"><div class="hid" id="c4n0">Reproche</div><div class="hid" id="c4n1">Rafale de messages</div></div></div>
  {phone("c4ph", m4, 1290, 100)}
</div>'''
js += fin("#c4ph", T["manq"] + .3) + pop("#c4m1", T["rap"] - .4) + pop("#c4m2", T["rap"] + .8, "back.out(2)") + pop("#c4rs", T["rap"])
js += pop("#c4n0", T["repr"]) + pop("#c4n1", T["raf"] + .2)

# ---------- récap (rs -> g)
rc = [("Annoncez <span>tarif, durée,</span><br/>format et délai", T["s1"], ""), ("Le règlement,<br/><span>à la réservation</span>", T["s2"], " g"),
      ("Des conditions<br/><span>écrites avant</span>", T["s3"], "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += f'''
<div id="r" class="clip light" data-start="{r2(T["rs"])}" data-duration="{r2(T["g"] - T["rs"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>
</div>'''
js += pop("#rk", T["rs"] + .05, E) + "".join(pop(f"#rc{i}", t, y=50) for i, (_, t, _) in enumerate(rc))

# ---------- GuidPilot (g -> z)
gc = [("Tarif et durée affichés", "g"), ("Réservation + règlement", "gres"), ("Facture automatique", "gfac"), ("Rappel en un clic", "gclic")]
gch = "".join(f'<div class="hid" id="gc{i}">{a}</div>' for i, (a, _) in enumerate(gc))
body += f'''
<div id="g" class="clip light" data-start="{r2(T["g"])}" data-duration="{r2(T["z"] - T["g"])}" data-track-index="1">
  <div class="col" style="width:820px;justify-content:flex-start;top:130px"><img class="hid" id="gl" src="assets/logo_couleur.png" alt="GuidPilot" style="width:400px" />
    <div class="h hid" id="gb" style="font-size:60px">Un outil conçu<br/><span>pour la guidance</span></div>
    <div class="chips8" style="margin-top:34px;max-width:820px">{gch}</div></div>
  <div class="pp8 hid" id="gpp" style="left:980px;top:120px;width:840px;height:540px"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="tp" style="height:130px;padding:28px 44px"><div class="k">VOTRE PAGE</div><div class="n" style="font-size:38px">Cabinet Exemple · Tarot</div></div>
    <div class="it">Guidance écrite · sous 48 h<span>Réserver</span></div>
    <div class="it">Guidance en visio · 45 min<span>Réserver</span></div>
    <div class="it">Guidance vocale · sous 48 h<span>Réserver</span></div></div>
  <div class="pp8 hid" id="gz1" style="left:980px;top:690px;width:840px;height:310px"><span class="illus" style="right:24px;top:14px">Illustration</span>
    <div class="it" style="margin-top:44px">Facture créée automatiquement<span style="background:#16A34A">✓</span></div>
    <div class="it hid" id="gz2">Règlement en attente<span>Envoyer un rappel</span></div></div>
</div>'''
js += f'tl.fromTo("#gl",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"}},{r2(T["g"] + .1)});\n' + pop("#gb", T["g"] + .7, E, 40)
js += "".join(pop(f"#gc{i}", T[k] + (.9 if k == "g" else .2)) for i, (_, k) in enumerate(gc)) + fin("#gpp", T["g"] + 1.2) + fin("#gz1", T["gfac"]) + pop("#gz2", T["grap"] + .3)

# ---------- fin marine (z -> DUR)
t = T["z"]
body += f'''
<div id="z" class="clip navy" data-start="{r2(t)}" data-duration="{r2(DUR - t)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard hid" id="z7">✓ Sans carte bancaire</div>
    <div class="url hid" id="z8">guidpilot.fr</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += f'tl.fromTo("#z6",{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"}},{r2(t + .1)});\n'
js += pop("#z7", t + 1.6) + pop("#z8", T["url"]) + pop("#z9", T["zabo"])
js += f'tl.to("#z9",{{scale:1.06,duration:.45,yoyo:true,repeat:2,ease:"sine.inOut"}},{r2(T["zabo"] + .6)});\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA4}{EXTRA5}{EXTRA7}{EXTRA8}{EXTRA9}{EXTRA10}</style></head><body>
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

d = ATELIER / "build" / "yt-payer-avant"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, DUR)
