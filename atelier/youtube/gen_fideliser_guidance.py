"""Vidéo YouTube 1920x1080 : « Fidéliser ses clientes en guidance : 5 habitudes pour qu'elles reviennent »
(conseil · public guidance, mercredi 14/10/2026).
Usage : python3 gen_fideliser_guidance.py <voix.wav>  -> build/yt-fideliser-guidance/
Temps calés sur voix/2026-10-14_yt-fideliser-clientes-guidance.mp3 (118,5 s) : silencedetect -32 dB / 0,14 s
+ estimation par syllabes (script d'alignement), vérifiés aux pauses.
Scènes : conversation téléphone « Merci ! » + frise des mois vides, titre en chemin de 5 étapes, message du lendemain
qui s'écrit dans un téléphone, avant / après écran partagé (éparpillé vs rangé), carnet de séance ouvert avec cadenas,
« À éviter » barré vs « Préférez », demande d'avis avec étoiles qui se remplissent, GuidPilot (liste qui s'allume +
téléphone espace client, fiche cliente, capture avis.png avec cercle, bouton « Prendre un nouveau rendez-vous »), citation, fin marine.
Réutilise CSS et helpers de gen_therapeutes_soir.py.
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_therapeutes_soir.py").read_text()
ns = {"__file__": str(HERE / "gen_therapeutes_soir.py")}
exec(src.split("# ---------- A :")[0], ns)
CSS, EXTRA, ATELIER, KIT = ns["CSS"], ns["EXTRA"], ns["ATELIER"], ns["KIT"]
pop, fin, out, lion, chap, phone, LOGO, E = (ns[k] for k in ("pop", "fin", "out", "lion", "chap", "phone", "LOGO", "E"))

DUR = 119.4
T = dict(t=12.45, s1=17.15, s2=33.55, s3=49.2, s4=61.45, s5=78.45, g0=86.55, g1=89.55, q=107.5, end=110.2)

EXTRA2 = """
.hk2{position:absolute;left:110px;top:130px;width:820px}
.hk2 .k{font-weight:700;font-size:28px;letter-spacing:.14em;color:#2563EB}
.hk2 .b{font-weight:800;font-size:84px;line-height:1.06;letter-spacing:-.03em;color:#0F172A;margin-top:22px}
.hk2 .b span{color:#2563EB}
.months{position:absolute;left:110px;top:560px;width:800px;display:flex;gap:18px}
.mo{flex:1;height:150px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px}
.mo b{font-weight:800;font-size:28px;color:#0F172A}
.mo i{display:block;width:34px;height:34px;border-radius:50%;background:#2563EB}
.mo.e{border-style:dashed;background:#F8FAFC}.mo.e b{color:#94A3B8}
.mo.e i{background:none;border:4px dashed #CBD5E1;width:34px;height:34px}
.chips{position:absolute;left:110px;top:780px;width:820px;display:flex;flex-wrap:wrap;gap:16px}
.chips div{padding:14px 28px;border-radius:999px;background:#0F172A;font-weight:700;font-size:30px;color:#fff}
.qmark{position:absolute;left:1500px;top:640px;font-weight:800;font-size:150px;color:#CBD5E1}
.path{position:absolute;left:160px;top:560px;width:1600px;height:300px}
.pl{position:absolute;left:0;top:70px;width:1600px;height:10px;border-radius:5px;background:#CBD5E1;transform-origin:left center}
.st5{position:absolute;top:0;width:150px;height:150px;margin-left:-75px;border-radius:50%;background:#fff;border:10px solid #2563EB;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:58px;color:#0F172A;box-shadow:0 16px 40px rgba(15,23,42,.1)}
.st5.g{border-color:#E9C46A}
.sl5{position:absolute;top:180px;width:300px;margin-left:-150px;text-align:center;font-weight:800;font-size:32px;color:#0F172A;line-height:1.2}
.ts{position:absolute;left:0;right:0;top:150px;text-align:center;font-weight:600;font-size:22px;color:#94A3B8}
.bub.lg{max-width:370px;font-size:27px;line-height:1.32}
.typing{position:absolute;right:24px;width:110px;height:58px;border-radius:26px;background:#DBEAFE;display:flex;align-items:center;justify-content:center;gap:10px}
.typing i{width:12px;height:12px;border-radius:50%;background:#2563EB}
.split{position:absolute;top:290px;width:820px;height:700px;border-radius:30px;padding:40px}
.split.l{left:110px;background:#FEF2F2;border:2px solid #FECACA}
.split.r{left:990px;background:#F0FDF4;border:2px solid #BBF7D0}
.split .lb{display:inline-flex;align-items:center;gap:12px;padding:10px 24px;border-radius:999px;font-weight:800;font-size:28px}
.split.l .lb{background:#FEE2E2;color:#B91C1C}.split.r .lb{background:#DCFCE7;color:#15803D}
.it{position:absolute;padding:22px 26px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.08);font-weight:700;font-size:28px;color:#0F172A}
.it small{display:block;font-weight:600;font-size:21px;color:#64748B;margin-top:6px}
.wave{display:flex;align-items:center;gap:5px;margin-top:10px}
.wave i{display:block;width:7px;border-radius:4px;background:#2563EB}
.lost{position:absolute;left:40px;right:40px;bottom:40px;text-align:center;font-weight:800;font-size:40px;color:#B91C1C}
.fold{position:absolute;left:40px;right:40px;top:120px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 18px 44px rgba(15,23,42,.08);overflow:hidden}
.fold .fh{display:flex;align-items:center;gap:18px;padding:24px 28px;border-bottom:2px solid #E2E8F0;font-weight:800;font-size:30px;color:#0F172A}
.fold .fh i{width:54px;height:42px;border-radius:8px;background:#2563EB;position:relative}
.fold .fh i:before{content:"";position:absolute;left:0;top:-8px;width:24px;height:12px;border-radius:5px 5px 0 0;background:#2563EB}
.fr{display:flex;align-items:center;gap:18px;padding:20px 28px;border-bottom:2px solid #F1F5F9;font-weight:700;font-size:27px;color:#0F172A}
.fr .tg{margin-left:auto;padding:6px 16px;border-radius:999px;font-weight:800;font-size:20px;background:#EFF6FF;color:#2563EB}
.fr .tg.a{background:#F5F3FF;color:#7C3AED}
.relire{position:absolute;left:40px;right:40px;bottom:40px;text-align:center;font-weight:800;font-size:36px;color:#15803D}
.nb{position:absolute;left:880px;top:170px;width:960px;height:760px;display:flex;filter:drop-shadow(0 30px 60px rgba(15,23,42,.16))}
.pg{flex:1;background:#FFFDF7;padding:50px 44px;position:relative}
.pg.a{border-radius:24px 0 0 24px;border-right:3px solid #E7DFC8}
.pg.b{border-radius:0 24px 24px 0}
.pg .t1{font-weight:800;font-size:34px;color:#0F172A}
.pg .t2{font-weight:600;font-size:22px;color:#64748B;margin-top:6px}
.pr{display:flex;align-items:center;gap:16px;margin-top:34px;font-weight:700;font-size:25px;color:#0F172A}
.pr i{flex:none;width:22px;height:22px;border-radius:50%;border:5px solid #2563EB}
.pr small{display:block;font-weight:600;font-size:19px;color:#64748B}
.hl{font-weight:800;font-size:24px;letter-spacing:.08em;color:#B7791F;margin-top:30px}
.hw{font-weight:600;font-size:27px;color:#1E293B;margin-top:10px;line-height:1.35}
.lockt{position:absolute;left:44px;right:44px;bottom:44px;display:flex;align-items:center;gap:14px;padding:18px 22px;border-radius:18px;background:#0F172A;color:#fff;font-weight:800;font-size:26px}
.vs{position:absolute;left:110px;width:1700px;padding:40px 50px;border-radius:30px;display:flex;align-items:center;gap:40px}
.vs .ic{flex:none;width:96px;height:96px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:52px;color:#fff}
.vs .lb{font-weight:800;font-size:26px;letter-spacing:.14em}
.vs .tx{font-weight:700;font-size:44px;line-height:1.25;color:#0F172A;margin-top:8px}
.vs.no{top:300px;background:#FEF2F2;border:2px solid #FECACA}.vs.no .ic{background:#DC2626}.vs.no .lb{color:#B91C1C}
.vs.yes{top:560px;background:#F0FDF4;border:2px solid #BBF7D0}.vs.yes .ic{background:#16A34A}.vs.yes .lb{color:#15803D}
.strike{position:absolute;left:180px;top:58%;height:6px;width:0;background:#DC2626;border-radius:3px}
.rythm{position:absolute;left:0;right:0;top:850px;text-align:center}
.rythm div{display:inline-block;padding:20px 44px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:38px}
.rythm span{color:#E9C46A}
.stars{display:flex;gap:10px;margin:22px 24px 0}
.stars svg{width:62px;height:62px}
.stars path{fill:#E2E8F0}
.zf2{position:absolute;left:10px;top:270px;width:864px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.zf2 .vp{position:relative;width:860px;height:224px;overflow:hidden}
.zf2 .vp img{position:absolute;left:0;top:0;width:860px}
.ring2{position:absolute;border:6px solid #E9C46A;border-radius:22px;box-shadow:0 0 0 9999px rgba(15,23,42,.14)}
"""

STAR = '<svg viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
LOCK = ('<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#E9C46A" stroke-width="2.2" stroke-linecap="round">'
        '<rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>')
body, js = "", ""

# ---------- A : une première guidance… puis plus de nouvelles (0 -> 12.45)
months = [("Sept.", ""), ("Oct.", " e"), ("Nov.", " e"), ("Déc.", " e")]
mh = "".join(f'<div class="mo{c} hid" id="am{i}"><b>{m}</b><i></i></div>' for i, (m, c) in enumerate(months))
inner = ('<div class="phead"><div class="av">CR</div>Camille R.</div><div class="ts">Hier · 19:40</div>'
         '<div class="bub her lg hid" id="ab0" style="top:200px">Merci beaucoup pour la guidance&nbsp;!</div>'
         '<div class="bub her hid" id="ab1" style="top:345px">Je me sens plus sereine.</div>'
         '<div class="bub me hid" id="ab2" style="top:480px">Avec plaisir, belle soirée à vous.</div>')
body += f'''
<div id="a" class="clip light" data-start="0" data-duration="{T['t']}" data-track-index="1">
  {LOGO}
  <div class="hk2"><div class="k hid" id="ak">PRATICIENNES EN GUIDANCE</div>
    <div class="b hid" id="ah">Une première séance…<br/><span>puis plus de nouvelles ?</span></div></div>
  <div class="months">{mh}</div>
  <div class="chips"><div class="hid" id="ac0">Tarologue</div><div class="hid" id="ac1">Voyante</div>
    <div class="hid" id="ac2">Médium</div><div class="hid" id="ac3">Énergéticienne</div></div>
  {phone("ap", inner, 1060, 100)}
</div>'''
js += pop("#ak", 0.1, E) + fin("#ap", 0.3) + pop("#ab0", 0.9, y=20)
js += pop("#ah", 2.0, E, 40) + pop("#ab1", 2.4, y=20) + pop("#ab2", 3.5, y=20)
js += pop("#am0", 4.2) + "".join(pop(f"#am{i}", 5.1 + (i - 1) * .35) for i in range(1, 4))
js += 'tl.to(".mo.e",{opacity:.55,duration:.3,stagger:.1},6.6);\n'
js += pop("#ac0", 9.6) + pop("#ac1", 10.39) + pop("#ac2", 10.9) + pop("#ac3", 11.4)

# ---------- T : titre en chemin (12.45 -> 17.15)
steps = ["Le suivi", "La guidance<br/>bien rangée", "Son histoire", "Une suite,<br/>sans forcer", "Son avis"]
xs = [0, 400, 800, 1200, 1600]
ph = "".join(f'<div class="st5{" g" if i == 4 else ""} hid" id="tp{i}" style="left:{x}px">{i + 1}</div>'
             f'<div class="sl5 hid" id="tl{i}" style="left:{x}px">{s}</div>' for i, (s, x) in enumerate(zip(steps, xs)))
body += f'''
<div id="t" class="clip light" data-start="{T['t']}" data-duration="{round(T['s1'] - T['t'], 2)}" data-track-index="1">
  {LOGO}
  <div class="titleT hid" id="tt" style="top:150px"><div class="k">FIDÉLISER SES CLIENTES EN GUIDANCE</div>
    <div class="b">5 habitudes pour qu'elles<br/><span>aient envie de revenir</span></div></div>
  <div class="path"><div class="pl hid" id="tpl"></div>{ph}</div>
</div>'''
js += 'tl.fromTo("#tt",{opacity:0,y:40},{opacity:1,y:0,duration:.7,ease:"back.out(1.4)"},12.55);\n'
js += 'tl.fromTo("#tpl",{opacity:1,scaleX:0},{opacity:1,scaleX:1,duration:2.2,ease:"power1.inOut"},13.3);\n'
js += "".join(pop(f"#tp{i}", 13.3 + i * .5) + pop(f"#tl{i}", 13.45 + i * .5) for i in range(5))

# ---------- 1 : le suivi après la séance (17.15 -> 33.55)
h1, j1 = chap("s1", 1, "Le suivi", "Le lendemain,<br/><span>un message court</span>", T['s1'])
msg = [("Bonjour Camille,", 23.21), ("merci pour votre confiance hier.", 24.14),
       ("Prenez le temps de relire votre guidance,", 26.02), ("je reste disponible si une question se pose.", 28.16)]
mtx = " ".join(f'<span class="hid" id="m{i}">{t}</span>' for i, (t, _) in enumerate(msg))
inner = ('<div class="phead"><div class="av">CR</div>Camille R.</div><div class="ts">Aujourd\'hui · 10:12</div>'
         '<div class="typing hid" id="s1ty" style="top:200px"><i></i><i></i><i></i></div>'
         f'<div class="bub me lg hid" id="s1b" style="top:200px">{mtx}</div>'
         '<div class="bub her hid" id="s1r" style="top:560px">Merci, c\'est très gentil !</div>')
body += f'''
<div id="s1" class="clip light" data-start="{T['s1']}" data-duration="{round(T['s2'] - T['s1'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:780px">{h1}
    <div class="cons hid" id="s1k"><div class="l">LE CONSEIL</div><div class="t">Un mot sincère, sans rien lui proposer d'autre.</div></div>
    <div class="ok hid" id="s1o1"><i>✓</i>Pas de vente</div>
    <div class="ok hid" id="s1o2"><i>✓</i>Juste de l'attention</div></div>
  {phone("s1p", inner, 1180, 100)}
</div>'''
js += j1 + fin("#s1p", 17.6) + pop("#s1ty", 20.1, y=10)
js += pop("#s1k", 20.9, E) + out("#s1ty", 23.0, .2) + pop("#s1b", 23.1, y=10)
js += "".join(f'tl.fromTo("#m{i}",{{opacity:0}},{{opacity:1,duration:.4}},{t});\n' for i, (_, t) in enumerate(msg))
js += pop("#s1o1", 31.27) + pop("#s1o2", 32.44) + pop("#s1r", 32.0, y=20)

# ---------- 2 : la guidance bien rangée, avant / après (33.55 -> 49.2)
wave = lambda n: '<div class="wave">' + "".join(f'<i style="height:{h}px"></i>' for h in [14, 30, 22, 40, 18, 34, 26, 12, 30, 20][:n]) + '</div>'
body += f'''
<div id="s2" class="clip light" data-start="{T['s2']}" data-duration="{round(T['s3'] - T['s2'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:100px"><div class="chap hid" id="s2c"><b>2</b>La guidance bien rangée</div>
    <div class="h hid" id="s2h" style="font-size:60px">Livrez-la dans <span>un endroit qu'elle retrouve</span></div></div>
  <div class="split l hid" id="s2l"><div class="lb">✕ Éparpillée</div>
    <div class="it hid" id="i0" style="left:60px;top:130px;transform:rotate(-4deg)">Message vocal · 3:42{wave(10)}<small>perdu au milieu des conversations</small></div>
    <div class="it hid" id="i1" style="left:300px;top:330px;transform:rotate(3deg)">Re : Re : votre guidance<small>noyé dans les e-mails</small></div>
    <div class="it hid" id="i2" style="left:80px;top:470px;transform:rotate(-2deg)">Capture d'écran.png<small>dans la galerie photos</small></div>
    <div class="lost hid" id="s2x">Votre travail disparaît.</div></div>
  <div class="split r hid" id="s2r"><div class="lb">✓ Rangée</div>
    <div class="fold"><div class="fh"><i></i>Les guidances de Camille</div>
      <div class="fr hid" id="f0">Guidance écrite<span class="tg">13 oct.</span></div>
      <div class="fr hid" id="f1">Guidance vocale · 3:42<span class="tg a">Audio</span></div>
      <div class="fr hid" id="f2" style="border:0">Guidance écrite<span class="tg">2 sept.</span></div></div>
    <div class="relire hid" id="s2o">Elle la relit quand elle veut.</div>
    <span class="illus" style="right:24px;top:30px">Illustration</span></div>
</div>'''
js += pop("#s2c", 33.65, E) + pop("#s2h", 33.9, E, 40)
js += 'tl.fromTo("#s2l",{opacity:0,x:-60},{opacity:1,x:0,duration:.6,ease:"power3.out"},35.0);\n'
js += pop("#i0", 37.17) + pop("#i1", 38.7) + pop("#i2", 39.6)
js += 'tl.to(["#i0","#i1","#i2"],{opacity:.25,filter:"blur(3px)",duration:.8},40.63);\n' + pop("#s2x", 40.9)
js += 'tl.fromTo("#s2r",{opacity:0,x:60},{opacity:1,x:0,duration:.6,ease:"power3.out"},42.14);\n'
js += pop("#f0", 43.0) + pop("#f1", 44.0) + pop("#f2", 45.0) + pop("#s2o", 46.4)

# ---------- 3 : son histoire, le carnet (49.2 -> 61.45)
h3, j3 = chap("s3", 3, "Son histoire", "Elle n'a pas à<br/><span>tout réexpliquer</span>", T['s3'])
rows = [("Séance découverte", "2 septembre", 55.0), ("Guidance de suivi", "23 septembre", 55.5), ("Tirage du mois", "13 octobre", 56.0)]
prs = "".join(f'<div class="pr hid" id="nr{i}"><i></i><div>{a}<small>{b}</small></div></div>' for i, (a, b, _) in enumerate(rows))
body += f'''
<div id="s3" class="clip warm" data-start="{T['s3']}" data-duration="{round(T['s4'] - T['s3'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:700px">{h3}
    <div class="cons hid" id="s3k"><div class="l">LE CONSEIL</div><div class="t">Après chaque séance, notez les thèmes abordés et ce qu'elle souhaite suivre.</div></div></div>
  <div class="nb hid" id="s3nb"><span class="illus" style="left:30px;top:-46px">Illustration</span>
    <div class="pg a"><div class="t1">Camille R.</div><div class="t2">Cliente depuis septembre</div>{prs}</div>
    <div class="pg b"><div class="hl hid" id="nh0" style="margin-top:0">THÈMES ABORDÉS</div>
      <div class="hw hid" id="nw0">Projet professionnel, choix entre deux offres.</div>
      <div class="hl hid" id="nh1">À SUIVRE</div>
      <div class="hw hid" id="nw1">Sa décision de janvier, et comment elle la vit.</div>
      <div class="lockt hid" id="s3l">{LOCK}Notes privées · pour vous seule</div></div></div>
</div>'''
js += j3 + 'tl.fromTo("#s3nb",{opacity:0,y:60,rotation:2},{opacity:1,y:0,rotation:0,duration:.7,ease:"power3.out"},50.2);\n'
js += "".join(pop(f"#nr{i}", t) for i, (_, _, t) in enumerate(rows))
js += pop("#s3k", 56.61, E) + pop("#nh0", 57.2) + pop("#nw0", 57.6) + pop("#nh1", 58.5) + pop("#nw1", 58.9)
js += 'tl.fromTo("#s3l",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.45,ease:"back.out(2)"},60.12);\n'

# ---------- 4 : une suite, sans forcer (61.45 -> 78.45)
body += f'''
<div id="s4" class="clip light" data-start="{T['s4']}" data-duration="{round(T['s5'] - T['s4'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:100px"><div class="chap hid" id="s4c"><b>4</b>Une suite, sans forcer</div>
    <div class="h hid" id="s4h" style="font-size:60px">Proposez, <span>elle décide</span></div></div>
  <div class="vs no hid" id="s4n"><div class="ic">✕</div><div style="position:relative"><div class="lb">À ÉVITER</div>
    <div class="tx">« Il faut absolument refaire un tirage la semaine prochaine. »</div><div class="strike" id="s4s" style="left:0"></div></div></div>
  <div class="vs yes hid" id="s4y"><div class="ic">✓</div><div><div class="lb">PRÉFÉREZ</div>
    <div class="tx">« Si vous souhaitez faire le point dans quelques semaines, mes disponibilités sont en ligne. »</div></div></div>
  <div class="rythm hid" id="s4r"><div>Elle décide, <span>à son rythme.</span></div></div>
</div>'''
js += pop("#s4c", 61.55, E) + pop("#s4h", 61.8, E, 40)
js += 'tl.fromTo("#s4n",{opacity:0,x:-80},{opacity:1,x:0,duration:.6,ease:"power3.out"},65.23);\n'
js += 'tl.to("#s4s",{width:"100%",duration:.6,ease:"power2.inOut"},70.3);\n'
js += 'tl.to("#s4n",{opacity:.6,duration:.4},70.9);\n'
js += 'tl.fromTo("#s4y",{opacity:0,x:80},{opacity:1,x:0,duration:.6,ease:"power3.out"},71.22);\n'
js += 'tl.fromTo("#s4r",{opacity:0,y:30},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},76.28);\n'

# ---------- 5 : son avis (78.45 -> 86.55)
h5, j5 = chap("s5", 5, "Son avis", "Quelques jours après,<br/><span>demandez-le simplement</span>", T['s5'])
stars = "".join(f'<span id="sx{i}">{STAR}</span>' for i in range(5))
inner = ('<div class="phead"><div class="av">CR</div>Camille R.</div><div class="ts">Vendredi · 11:00</div>'
         '<div class="bub me lg hid" id="s5b" style="top:200px">Bonjour Camille, si vous le souhaitez, votre avis sur notre séance me serait précieux.</div>'
         f'<div class="hid" id="s5st" style="position:absolute;left:0;right:0;top:500px"><div class="stars" style="justify-content:center">{stars}</div></div>')
body += f'''
<div id="s5" class="clip light" data-start="{T['s5']}" data-duration="{round(T['g0'] - T['s5'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px">{h5}
    <div class="ok hid" id="s5o1"><i>✓</i>Vous progressez grâce à son retour</div>
    <div class="ok hid" id="s5o2"><i>✓</i>Vos prochaines clientes sont rassurées</div></div>
  {phone("s5p", inner, 1180, 100)}
</div>'''
js += j5 + fin("#s5p", 78.8) + pop("#s5b", 79.96, y=20) + pop("#s5st", 81.4, y=20)
js += 'tl.to("#s5st path",{fill:"#E9C46A",duration:.2,stagger:.18},81.9);\n'
js += pop("#s5o1", 83.5) + pop("#s5o2", 84.61)

# ---------- 6 : GuidPilot (86.55 -> 107.5)
items = ["Son espace client sécurisé", "Sa fiche et vos notes privées", "La demande d'avis en un clic", "Elle reprend rendez-vous elle-même"]
lis = "".join(f'<div class="li" id="l{i}"><i>{i + 1}</i>{t}</div>' for i, t in enumerate(items))
v1 = phone("v1", '<div class="phead">Mon espace</div>'
              '<div class="cr hid" id="v1a"><div class="a">Ma guidance écrite</div><div class="b">13 octobre</div><div class="nw">Nouveau</div></div>'
              '<div class="cr hid" id="v1b"><div class="a">Ma guidance vocale</div><div class="b">3 min 42</div></div>'
              '<div class="cr hid" id="v1c"><div class="a">Mes factures</div><div class="b">3 documents</div></div>'
              '<div class="cr hid" id="v1d"><div class="a">Messagerie</div><div class="b">Échanger avec votre praticienne</div></div>', 210, 0)
v2 = (f'<div class="hid" id="v2" style="position:absolute;inset:0"><div class="mini"><span class="illus" style="right:24px;top:20px">Illustration</span>'
      f'<div class="ch"><div class="av">CR</div><div><div style="font-weight:800;font-size:36px">Camille R.</div><div style="font-weight:600;font-size:22px;color:#64748B">3 séances</div></div></div>'
      f'<div class="r"><i></i>Historique des séances</div><div class="r"><i></i>Guidances livrées</div><div class="r"><i></i>Paiements et factures</div>'
      f'<div class="note" style="bottom:30px"><div class="nh">Notes privées</div><div class="ns" style="margin:8px 0 0">Jamais visibles par votre cliente</div>'
      f'<div class="nl" style="width:85%"></div></div></div></div>')
v3 = ('<div class="hid" id="v3" style="position:absolute;inset:0"><div class="zf2"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>'
      '<span class="demo">Compte de démonstration</span></div><div class="vp"><img src="assets/avis.png" alt="" />'
      '<div class="ring2 hid" id="v3r" style="left:4px;top:52px;width:540px;height:42px"></div></div></div>'
      '<div class="cap" style="top:580px">Demandez un avis,<br/><span>relancez si besoin</span></div></div>')
v4 = phone("v4", '<div class="phead">Mon espace</div>'
              '<div class="cr"><div class="a">Ma dernière séance</div><div class="b">Tirage du mois · 13 octobre</div></div>'
              '<div class="cr"><div class="a">Ma guidance écrite</div><div class="b">À relire quand vous voulez</div></div>'
              '<div class="btn" id="v4b" style="margin-top:40px;height:auto;padding:18px 20px;text-align:center;line-height:1.25">Prendre un nouveau rendez-vous</div>'
              '<div class="noted hid" id="v4n" style="margin:24px 22px 0">✓ Rendez-vous réservé</div>', 210, 0)
body += f'''
<div id="g0" class="clip navy" data-start="{T['g0']}" data-duration="{round(T['g1'] - T['g0'], 2)}" data-track-index="1">
  <div class="gp hid" id="gpi"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:440px" />
    <div class="b">Avec GuidPilot,<br/><span>ces habitudes deviennent faciles</span></div></div>
</div>
<div id="g1" class="clip light" data-start="{T['g1']}" data-duration="{round(T['q'] - T['g1'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:800px"><div class="chap"><b>✓</b>Avec GuidPilot</div><div class="lst">{lis}</div></div>
  <div class="vis">{v1}{v2}{v3}{v4}</div>
</div>'''
js += 'tl.fromTo("#gpi",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},86.65);\n'
vt = [89.65, 96.94, 100.97, 102.7]
for i, t in enumerate(vt):
    js += lion(f"#l{i}", t)
    js += f'tl.fromTo("#v{i + 1}",{{opacity:0,x:80}},{{opacity:1,x:0,duration:.5,ease:"{E}"}},{t});\n'
    if i < 3:
        js += out(f"#v{i + 1}", vt[i + 1] - .35, .3)
js += pop("#v1a", 90.6) + pop("#v1b", 91.6) + pop("#v1c", 93.42) + pop("#v1d", 94.6)
js += pop("#v3r", 101.5) + 'tl.to("#v3r",{scale:1.03,duration:.3,yoyo:true,repeat:1},101.9);\n'
js += 'tl.to("#v4b",{scale:.94,duration:.15,yoyo:true,repeat:1},104.9);\n' + pop("#v4n", 105.4)

# ---------- citation (107.5 -> 110.2) puis fin (110.2 -> DUR)
body += f'''
<div id="q" class="clip light" data-start="{T['q']}" data-duration="{round(T['end'] - T['q'], 2)}" data-track-index="1">
  {LOGO}
  <div class="quote"><div class="qm hid" id="qm">“</div>
    <div class="q hid" id="qq">Une cliente qui se sent suivie<br/><span>a envie de revenir.</span></div></div>
</div>
<div id="z" class="clip navy" data-start="{T['end']}" data-duration="{round(DUR - T['end'], 2)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard hid" id="z7">✓ Sans carte bancaire</div>
    <div class="url hid" id="z8">guidpilot.fr</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : une vidéo par jour</div>
  </div>
</div>'''
js += pop("#qm", 107.55, E) + 'tl.fromTo("#qq",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},107.65);\n'
js += 'tl.fromTo("#z6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},110.3);\n'
js += pop("#z7", 113.42) + pop("#z8", 114.57) + pop("#z9", 116.05)
js += 'tl.to("#z9",{scale:1.06,duration:.45,yoyo:true,repeat:3,ease:"sine.inOut"},117.0);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA2}</style></head><body>
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

d = ATELIER / "build" / "yt-fideliser-guidance"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for a in ("avis.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
