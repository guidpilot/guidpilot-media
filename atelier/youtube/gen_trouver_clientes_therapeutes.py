"""Vidéo YouTube 1920x1080 : « Comment trouver des clients en sophrologie, Reiki ou hypnose : les 5 questions à régler »
(CONSEIL · public thérapeutes, mardi 10/11/2026).
Usage : python3 gen_trouver_clientes_therapeutes.py <voix.wav> [DUR]  -> build/yt-trouver-clientes/
Voix : 9 paragraphes générés un par un (voix/2026-11-10_yt-trouver-clientes-p1..p9.mp3), assemblés dans l'ordre
p1..p9 avec assembler_voix.py (p3 = CTA oral d'abonnement après la question 1, ~30 %). Total 163,9 s.
Temps T = début des phrases (silencedetect -30 dB / 0,15 s sur le wav assemblé + découpage des phrases).
Structure « les 5 questions d'une future cliente » (nouvelle) : chaque question = grande bulle de la future cliente
sur fond changeant + barre 5 segments -> problème illustré -> bon réflexe. GuidPilot seulement à la fin (~11 s + fin).
Aucune personne, aucun prix GuidPilot, aucun superlatif, aucun vocabulaire médical, aucune promesse de résultat.
Réutilise CSS et helpers de gen_logiciel_reiki.py + EXTRA7 (sophro) + EXTRA8 (médium).
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_logiciel_reiki.py").read_text()
ns = {"__file__": str(HERE / "gen_logiciel_reiki.py")}
exec(src.split("\n# ---------- A :")[0], ns)
CSS, EXTRA, EXTRA4, EXTRA5, ATELIER, KIT = (ns[k] for k in ("CSS", "EXTRA", "EXTRA4", "EXTRA5", "ATELIER", "KIT"))
pop, fin, out, phone, LOGO, LOGOW, E, LOCK = (ns[k] for k in ("pop", "fin", "out", "phone", "LOGO", "LOGOW", "E", "LOCK"))
EXTRA7 = (HERE / "gen_logiciel_sophro_hypno.py").read_text().split('EXTRA7 = """')[1].split('"""')[0]
EXTRA8 = (HERE / "gen_logiciel_medium_energeticienne.py").read_text().split('EXTRA8 = """')[1].split('"""')[0]

DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 167.0
r2 = lambda x: round(x, 2)

EXTRA9 = """
.hk9{position:absolute;left:110px;top:300px;width:900px}
.hk9 .q{font-weight:800;font-size:112px;line-height:1.02;letter-spacing:-.035em;color:#fff}
.hk9 .q span{color:#E9C46A}
.hk9 .s{font-weight:700;font-size:46px;line-height:1.25;color:#CBD5E1;margin-top:46px}
.hk9 .s b{color:#fff}
.wk{position:absolute;left:1080px;top:230px;width:740px;border-radius:30px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.35);overflow:hidden}
.wk .hd{height:96px;padding:0 36px;display:flex;align-items:center;justify-content:space-between;background:#F1F5F9;font-weight:800;font-size:32px;color:#0F172A}
.wk .hd small{font-weight:600;font-size:22px;color:#64748B}
.wk .d{display:flex;align-items:center;gap:24px;padding:24px 36px;border-top:2px solid #E2E8F0}
.wk .d b{flex:none;width:120px;font-weight:800;font-size:28px;color:#0F172A}
.wk .d span{flex:1;height:58px;border-radius:14px;border:3px dashed #CBD5E1;display:flex;align-items:center;padding-left:22px;font-weight:700;font-size:24px;color:#94A3B8}
.fq{position:absolute;z-index:8;padding:16px 28px;border-radius:26px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:32px;box-shadow:0 18px 40px rgba(0,0,0,.3)}
.qb{position:absolute;left:150px;top:0;bottom:0;width:1620px;display:flex;flex-direction:column;justify-content:center}
.qb .n{display:inline-flex;align-items:center;gap:22px;font-weight:800;font-size:32px;letter-spacing:.14em;text-transform:uppercase}
.qb .n b{display:inline-flex;width:84px;height:84px;border-radius:50%;align-items:center;justify-content:center;font-size:44px;letter-spacing:0}
.qb .bb{position:relative;align-self:flex-start;margin-top:44px;padding:44px 64px;border-radius:56px;border-bottom-left-radius:14px;font-weight:800;font-size:100px;line-height:1.06;letter-spacing:-.035em;max-width:1560px}
.qb .w{font-weight:700;font-size:30px;margin-top:30px;opacity:.8}
.qb .bar5{display:flex;gap:12px;margin-top:56px}
.qb .bar5 i{display:block;width:120px;height:12px;border-radius:6px;opacity:.25}
.qb .bar5 i.on{opacity:1}
.cream .qb .n{color:#B7791F}.cream .qb .n b{background:#0F172A;color:#E9C46A}.cream .qb .bb{background:#fff;color:#0F172A;border:3px solid #E7DFC9}.cream .qb .w{color:#6B4E16}.cream .qb .bar5 i{background:#0F172A}
.navy .qb .n{color:#93C5FD}.navy .qb .n b{background:#E9C46A;color:#0F172A}.navy .qb .bb{background:#fff;color:#0F172A}.navy .qb .w{color:#CBD5E1}.navy .qb .bar5 i{background:#E9C46A}
.blue .qb .n{color:#BFDBFE}.blue .qb .n b{background:#fff;color:#1D4ED8}.blue .qb .bb{background:#0F172A;color:#fff}.blue .qb .w{color:#DBEAFE}.blue .qb .bar5 i{background:#fff}
.t4{position:absolute;left:110px;right:110px;top:400px;display:flex;gap:30px}
.t4 .c{flex:1;height:420px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.08);padding:44px 40px;display:flex;flex-direction:column;justify-content:space-between}
.t4 .c i{font-style:normal;display:flex;width:110px;height:110px;border-radius:28px;background:#EFF6FF;color:#2563EB;align-items:center;justify-content:center;font-size:56px;font-weight:800}
.t4 .c.g i{background:#FBF3DC;color:#B7791F}
.t4 .c b{font-weight:800;font-size:48px;line-height:1.1;color:#0F172A}
.t4 .c small{display:block;font-weight:600;font-size:26px;color:#64748B;margin-top:10px}
.bio{margin:26px 22px 0;padding:26px;border-radius:22px;background:#fff;border:2px solid #E2E8F0}
.bio .a{font-weight:800;font-size:28px;color:#0F172A}
.bio .b{font-weight:600;font-size:23px;line-height:1.35;color:#475569;margin-top:10px}
.bio .sts{display:flex;gap:30px;margin-top:20px;font-weight:700;font-size:20px;color:#64748B}
.gr9{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:20px 22px 0}
.gr9 div{height:72px;border-radius:16px;background:#EFF6FF;border:2px solid #BFDBFE;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:23px;color:#1D4ED8}
.gr9 div.x{background:#F1F5F9;border-color:#E2E8F0;color:#CBD5E1;text-decoration:line-through}
.gr9 div.on{background:#2563EB;border-color:#2563EB;color:#fff}
.bk9{margin:22px 22px 0;height:78px;border-radius:18px;background:#0F172A;color:#fff;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center}
.tm9{position:absolute;left:110px;top:760px;display:inline-flex;align-items:center;gap:18px;padding:18px 34px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:40px}
.big9{position:absolute;left:110px;top:420px;width:1240px;padding:40px 54px;border-radius:40px;background:#fff;color:#0F172A;font-weight:800;font-size:68px;line-height:1.1;box-shadow:0 30px 80px rgba(0,0,0,.35)}
.big9 s{text-decoration-color:#DC2626;text-decoration-thickness:8px}
.eff9{position:absolute;left:110px;top:700px;padding:24px 44px;border-radius:999px;background:#7F1D1D;color:#FECACA;font-weight:800;font-size:48px}
.av9{position:absolute;left:990px;top:330px;width:820px;height:560px;border-radius:30px;padding:46px;background:#fff;border:3px solid #2563EB;box-shadow:0 30px 80px rgba(37,99,235,.15)}
.av9 .k{font-weight:800;font-size:28px;letter-spacing:.12em;color:#2563EB}
.av9 .s{font-size:84px;color:#E9C46A;letter-spacing:8px;margin-top:26px}
.av9 .t{font-weight:600;font-style:italic;font-size:32px;line-height:1.35;color:#6B4E16;margin-top:20px;padding:22px 28px;border-radius:20px;background:#FBF3DC}
.av9 .a{font-weight:800;font-size:46px;line-height:1.12;color:#0F172A;margin-top:30px}
.pf.l.x .rw i{background:#FEE2E2;color:#B91C1C}
.pf.l.x{background:#FEF2F2;border-color:#FCA5A5}
.pf.l.x .k{color:#B91C1C}
.lc9{display:flex;flex-direction:column;gap:26px;margin-top:40px}
.lc9 div{display:flex;align-items:center;gap:24px;padding:28px 34px;border-radius:26px;background:#fff;border:2px solid #E7DFC9;box-shadow:0 14px 36px rgba(15,23,42,.07);font-weight:800;font-size:44px;color:#0F172A}
.lc9 div i{font-style:normal;flex:none;width:74px;height:74px;border-radius:22px;background:#0F172A;color:#E9C46A;display:flex;align-items:center;justify-content:center;font-size:38px}
.lnk9{margin:18px 22px 0 auto;width:320px;padding:18px 20px;border-radius:20px;background:#fff;border:3px solid #2563EB}
.lnk9 .a{font-weight:800;font-size:23px;color:#1D4ED8}.lnk9 .b{font-weight:600;font-size:19px;color:#64748B;margin-top:4px}
.gp9{position:absolute;left:980px;top:150px;width:840px}
"""

T = dict(
    q=0.5, cab=4.45, pb=7.31, rep=9.59, vid=13.51, five=14.39, sans=20.49,
    c1=22.49, c1q=23.77, dec=24.81, bio=29.88, chem=32.39, dites=33.62, mom=36.10, l1=38.37, l2=40.40, l3=41.66, rest=45.0,
    cta=48.42, abo=50.92, lien=53.55,
    c2=58.77, c2q=59.79, i1=61.54, i2=62.43, i3=63.84, i4=64.88, quatre=65.9, manq=68.04, pers=68.92, jam=70.93, fiche=72.66, part=75.26,
    c3=77.73, c3q=78.91, avis=80.58, mom3=83.13, apres=86.75, msg=88.06, cad=90.80, faux=92.16, sinc=93.76,
    c4=96.50, c4q=97.68, perd=98.87, env=101.13, eff=102.42, lien4=103.82, pl=104.85, cr=109.33, deux=112.48,
    c5=114.85, c5q=117.08, bao=119.75, fac=123.76, m1=125.98, m2=128.61, m3=130.0, loc=131.7,
    rs=136.6, r1=137.37, r2=140.84, r3=142.39,
    g=147.14, gpg=150.65, gres=153.71, gesp=155.72, z=157.86, url=159.63, zabo=161.61)

body, js = "", ""


def qcard(id_, start, end, num, q, cls, logo, lead="Ce que se demande votre future cliente"):
    bars = "".join(f'<i{" class=on" if i < num else ""}></i>' for i in range(5))
    h = f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(start)}" data-duration="{r2(end - start)}" data-track-index="1">
  {logo}
  <div class="qb"><div class="n hid" id="{id_}n"><b>{num}</b>Question {num} sur 5</div>
    <div class="bb hid" id="{id_}b">{q}</div><div class="w hid" id="{id_}w">{lead}</div><div class="bar5">{bars}</div></div>
</div>'''
    j = pop(f"#{id_}n", start + .05, E) + pop(f"#{id_}b", start + .2, "back.out(1.4)", 50) + pop(f"#{id_}w", start + .8)
    return h, j


# ---------- A : accroche (0 -> vid) — lisible dès l'image 0
days = "".join(f'<div class="d"><b>{d}</b><span>Libre</span></div>' for d in ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"))
fqs = [("C'est pour moi&nbsp;?", 900, 150), ("Ça se passe comment&nbsp;?", 1440, 600), ("Je réserve où&nbsp;?", 960, 900)]
fqh = "".join(f'<div class="fq hid" id="afq{i}" style="left:{x}px;top:{y}px">{t}</div>' for i, (t, x, y) in enumerate(fqs))
body += f'''
<div id="a" class="clip navy" data-start="0" data-duration="{r2(T["vid"])}" data-track-index="1">
  <div class="hk9"><div class="q">Cabinet prêt.<br/><span>Agenda vide.</span></div>
    <div class="s hid" id="as1">Le problème n'est pas<br/><b>votre pratique.</b></div></div>
  <div class="wk" id="awk"><span class="illus" style="left:24px;bottom:16px">Illustration</span>
    <div class="hd">Cette semaine<small>Mon agenda</small></div>{days}</div>
  {fqh}
</div>'''
js += pop("#as1", T["pb"] + .1, E)
js += "".join(pop(f"#afq{i}", T["rep"] + .4 + i * 1.0, "back.out(2)") for i in range(3))

# ---------- B : les 5 questions (vid -> c1)
tiles = ["C'est pour moi&nbsp;?", "Ça se passe comment&nbsp;?", "Je peux lui faire confiance&nbsp;?", "Comment je réserve&nbsp;?", "Je peux en parler&nbsp;?"]
th = "".join(f'<div class="hid" id="bt{i}"><b>{i + 1}</b><span>{t}</span></div>' for i, t in enumerate(tiles))
body += f'''
<div id="b" class="clip light" data-start="{r2(T["vid"])}" data-duration="{r2(T["c1"] - T["vid"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="bc"><b>?</b>Avant de réserver</div>
    <div class="h hid" id="bh" style="font-size:76px">Les 5 questions <span>d'une future cliente</span></div></div>
  <div class="t5">{th}</div>
  <div class="both hid" id="bs" style="top:850px"><div>Même <span>sans publicité</span></div></div>
</div>'''
js += pop("#bc", T["vid"] + .05, E) + pop("#bh", T["vid"] + .25, E, 40)
js += "".join(pop(f"#bt{i}", T["five"] + .3 + i * .55, y=50) for i in range(5)) + pop("#bs", T["sans"], "back.out(2)")

# ---------- Q1
h, j = qcard("c1", T["c1"], T["dec"], 1, "«&nbsp;C'est pour moi&nbsp;?&nbsp;»", "cream", LOGO)
body += h; js += j

# Q1 : la bio trop courte (dec -> dites)
inner = ('<div class="phead"><div class="av">C</div>cabinet.exemple</div>'
         '<div class="bio"><div class="a">Cabinet Exemple</div><div class="b">Praticienne Reiki<br/>Sur rendez-vous</div>'
         '<div class="sts"><span>Publications</span><span>Abonnés</span></div></div>'
         '<div class="gr9" style="grid-template-columns:1fr 1fr 1fr;margin-top:26px">' + '<div class="x" style="height:118px;text-decoration:none"></div>' * 6 + '</div>'
         '<div class="lost8 hid" id="c1lo" style="top:520px"><div>Elle passe son chemin</div></div>')
body += f'''
<div id="c1m" class="clip warm" data-start="{r2(T["dec"])}" data-duration="{r2(T["dites"] - T["dec"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px"><div class="chap hid" id="c1mc"><b>1</b>Le problème</div>
    <div class="h hid" id="c1mh" style="font-size:74px">Elle découvre <span>votre pratique…</span></div>
    <div class="ok8 hid" id="c1mo" style="color:#B91C1C"><i style="background:#DC2626">✕</i>Et votre bio ne lui répond pas</div></div>
  {phone("c1ph", inner, 1240, 100)}
</div>'''
js += pop("#c1mc", T["dec"] + .05, E) + pop("#c1mh", T["dec"] + .25, E, 40) + fin("#c1ph", T["dec"] + .5)
js += pop("#c1mo", T["bio"] + .2) + pop("#c1lo", T["chem"], "back.out(2)")

# Q1 : avant / plutôt (dites -> cta)
body += f'''
<div id="c1s" class="clip light" data-start="{r2(T["dites"])}" data-duration="{r2(T["cta"] - T["dites"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="c1sc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="c1sh" style="font-size:60px">Dites <span>à qui</span> vous vous adressez</div></div>
  <div class="pf l hid" id="c1l"><span class="illus" style="right:24px;top:24px">Exemple</span><div class="k">AU LIEU DE</div>
    <div class="a">«&nbsp;Praticienne Reiki,<br/>sur rendez-vous&nbsp;»</div></div>
  <div class="pf r hid" id="c1r"><span class="illus" style="right:24px;top:24px">Exemple</span><div class="k">PLUTÔT · ON VIENT ME VOIR POUR…</div>
    <div class="rw hid" id="c1r0"><i>✓</i>Une période chargée</div>
    <div class="rw hid" id="c1r1"><i>✓</i>Un besoin de faire une pause</div>
    <div class="rw hid" id="c1r2"><i>✓</i>Prendre du temps pour soi</div>
    <div class="rw hid" id="c1r3" style="margin-top:46px;color:#2563EB"><i>↓</i>Au cabinet ou en visio · Réserver</div></div>
  <div class="both hid" id="c1b"><div>Simple, concrète, <span>sans promesse</span></div></div>
</div>'''
js += pop("#c1sc", T["dites"] + .05, E) + pop("#c1sh", T["dites"] + .25, E, 40)
js += f'tl.fromTo("#c1l",{{opacity:0,x:-80}},{{opacity:1,x:0,duration:.6,ease:"power3.out"}},{r2(T["dites"] + .7)});\n'
js += f'tl.fromTo("#c1r",{{opacity:0,x:80}},{{opacity:1,x:0,duration:.6,ease:"power3.out"}},{r2(T["mom"])});\n'
js += pop("#c1r0", T["l1"]) + pop("#c1r1", T["l2"]) + pop("#c1r2", T["l3"]) + pop("#c1r3", T["l3"] + 1.6) + pop("#c1b", T["rest"], "back.out(2)")

# ---------- CTA oral abonnement (cta -> c2)
body += f'''
<div id="cta" class="clip navy" data-start="{r2(T["cta"])}" data-duration="{r2(T["c2"] - T["cta"])}" data-track-index="1">
  {LOGOW}
  <div class="ctaC"><div class="k hid" id="ck">CES CONSEILS VOUS SONT UTILES&nbsp;?</div>
    <div class="b hid" id="cb">2 vidéos par semaine<br/><span>pour organiser votre cabinet</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="dsc hid" id="cd">↓ <span><b>Essai gratuit&nbsp;:</b> le lien est dans la description</span></div>
</div>'''
js += pop("#ck", T["cta"] + .1, E) + pop("#cy", T["abo"], "back.out(2)") + pop("#cb", T["abo"] + .9, E, 40)
js += f'tl.to("#cy",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(T["abo"] + 1.4)});\n' + pop("#cd", T["lien"] + .2)

# ---------- Q2
h, j = qcard("c2", T["c2"], T["i1"], 2, "«&nbsp;Ça se passe comment&nbsp;?&nbsp;»", "navy", LOGOW)
body += h; js += j

# Q2 : les 4 infos (i1 -> manq)
inf = [("⏱", "La durée", "1 h&nbsp;? 1 h 30&nbsp;?", ""), ("☰", "Le déroulé", "Ce qui se passe", "g"),
       ("⌂", "Le lieu", "Cabinet ou visio", ""), ("€", "Le tarif", "Affiché clairement", "g")]
ih = "".join(f'<div class="c {g} hid" id="c2t{k}"><i>{ic}</i><div><b>{a}</b><small>{s}</small></div></div>' for k, (ic, a, s, g) in enumerate(inf))
body += f'''
<div id="c2i" class="clip light" data-start="{r2(T["i1"])}" data-duration="{r2(T["manq"] - T["i1"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="c2ic"><b>2</b>Les 4 infos</div>
    <div class="h hid" id="c2ih" style="font-size:66px">Ce qu'elle cherche <span>avant de réserver</span></div></div>
  <div class="t4">{ih}</div>
</div>'''
js += pop("#c2ic", T["i1"] + .05, E) + pop("#c2ih", T["quatre"], E, 40)
js += "".join(pop(f"#c2t{k}", T[f"i{k + 1}"], y=50) for k in range(4))

# Q2 : le message jamais envoyé (manq -> fiche)
draft = ('<div class="phead"><div class="av">CE</div>Cabinet Exemple</div>'
         '<div style="position:absolute;left:0;right:0;top:420px">'
         '<div class="b8 me hid" id="c2dr" style="opacity:.55">Bonjour, ça dure combien de temps&nbsp;? Et c\'est combien&nbsp;?</div></div>'
         '<div class="lost8 hid" id="c2no" style="top:640px"><div>Message jamais envoyé</div></div>')
body += f'''
<div id="c2m" class="clip eve" data-start="{r2(T["manq"])}" data-duration="{r2(T["fiche"] - T["manq"])}" data-track-index="1">
  {LOGOW}
  <div class="night"><div class="clk hid" id="c2k" style="font-size:150px">Si une info<br/><span>manque…</span></div>
    <div class="todo hid" id="c2t">… elle doit vous écrire</div></div>
  {phone("c2ph", draft, 1240, 100)}
</div>'''
js += pop("#c2k", T["manq"] + .05, E) + fin("#c2ph", T["manq"] + .3) + pop("#c2t", T["pers"]) + pop("#c2dr", T["pers"] + .5)
js += f'tl.to("#c2dr",{{opacity:0,y:-20,duration:.5}},{r2(T["jam"] + .2)});\n' + pop("#c2no", T["jam"] + .6, "back.out(2)")

# Q2 : une fiche par prestation (fiche -> c3)
body += f'''
<div id="c2s" class="clip light" data-start="{r2(T["fiche"])}" data-duration="{r2(T["c3"] - T["fiche"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:760px"><div class="chap hid" id="c2sc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="c2sh" style="font-size:72px">Une fiche<br/><span>par prestation</span></div>
    <div class="ok8 hid" id="c2o1"><i>✓</i>Claire</div><div class="ok8 hid" id="c2o2"><i>✓</i>Complète</div></div>
  <div class="pres hid" id="c2p" style="left:990px;height:620px;top:230px"><span class="illus" style="right:24px;top:24px">Exemple</span>
    <div class="ic" style="background:#EFF6FF">{ns["CAM"]}</div><div class="tt">Séance de sophrologie</div>
    <div class="row"><i>⏱</i>Durée : 1 h</div><div class="row"><i>☰</i>Un échange, puis la pratique</div>
    <div class="row"><i>⌂</i>Au cabinet ou en visio</div><div class="row"><i>€</i>Votre tarif, affiché</div></div>
</div>'''
js += pop("#c2sc", T["fiche"] + .05, E) + pop("#c2sh", T["fiche"] + .25, E, 40) + fin("#c2p", T["fiche"] + .5)
js += pop("#c2o1", T["part"] - .6) + pop("#c2o2", T["part"] + .2)

# ---------- Q3
h, j = qcard("c3", T["c3"], T["avis"], 3, "«&nbsp;Je peux lui faire<br/>confiance&nbsp;?&nbsp;»", "blue", LOGOW)
body += h; js += j

# Q3 : le bon moment (avis -> cad)
msg = ('<div class="phead"><div class="av">C</div>Camille M.</div>'
       '<div style="position:absolute;left:0;right:0;top:170px">'
       '<div class="b8 hid" id="c3b0">Merci pour la séance, je me sens bien ce soir&nbsp;!</div>'
       '<div class="b8 me hid" id="c3b1">Merci à vous. Si vous le souhaitez, vous pouvez laisser un avis ici&nbsp;:</div>'
       '<div class="lnk9 hid" id="c3b2"><div class="a">🔗 Laisser un avis</div><div class="b">Lien direct</div></div></div>')
body += f'''
<div id="c3m" class="clip cream" data-start="{r2(T["avis"])}" data-duration="{r2(T["cad"] - T["avis"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px;width:900px"><div class="chap hid" id="c3mc"><b>3</b>Le bon moment</div>
    <div class="h hid" id="c3mh" style="font-size:64px;color:#0F172A">Demander un avis,<br/><span>oui. Mais quand&nbsp;?</span></div></div>
  <div class="chain" style="top:470px;width:760px"><div class="st hid" id="c3s0"><b>1</b>Une séance qui s'est bien passée</div>
    <div class="st hid" id="c3s1"><b>2</b>Juste après</div><div class="st hid" id="c3s2"><b>3</b>Un message court + un lien</div></div>
  {phone("c3ph", msg, 1240, 100)}
</div>'''
js += pop("#c3mc", T["avis"] + .05, E) + pop("#c3mh", T["avis"] + .25, E, 40) + fin("#c3ph", T["avis"] + .6)
js += pop("#c3s0", T["mom3"] + .3) + pop("#c3b0", T["mom3"] + 1.0) + pop("#c3s1", T["apres"]) + pop("#c3s2", T["msg"])
js += pop("#c3b1", T["msg"] + .3) + pop("#c3b2", T["msg"] + 1.2, "back.out(2)")

# Q3 : à éviter / ce qui rassure (cad -> c4)
body += f'''
<div id="c3s" class="clip light" data-start="{r2(T["cad"])}" data-duration="{r2(T["c4"] - T["cad"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="c3sc"><b>✓</b>Ce qui rassure vraiment</div></div>
  <div class="pf l x hid" id="c3l"><div class="k">À ÉVITER</div><div class="a">Des avis<br/>«&nbsp;arrangés&nbsp;»</div>
    <div class="rw hid" id="c3l1"><i>✕</i>Un cadeau en échange</div><div class="rw hid" id="c3l2"><i>✕</i>Un faux avis</div></div>
  <div class="av9 hid" id="c3r"><span class="illus" style="right:24px;top:24px">Illustration</span><div class="k">CE QUI RASSURE</div>
    <div class="s">★★★★★</div><div class="t">Les avis sincères de vos clientes</div><div class="a">Quelques avis vrais<br/><span style="color:#2563EB">plutôt qu'un long discours</span></div></div>
</div>'''
js += pop("#c3sc", T["cad"] + .05, E)
js += f'tl.fromTo("#c3l",{{opacity:0,x:-80}},{{opacity:1,x:0,duration:.6,ease:"power3.out"}},{r2(T["cad"] + .2)});\n'
js += pop("#c3l1", T["cad"] + .8) + pop("#c3l2", T["faux"] + .2)
js += f'tl.fromTo("#c3r",{{opacity:0,x:80}},{{opacity:1,x:0,duration:.6,ease:"power3.out"}},{r2(T["sinc"])});\n'

# ---------- Q4
h, j = qcard("c4", T["c4"], T["perd"], 4, "«&nbsp;Comment je réserve&nbsp;?&nbsp;»", "cream", LOGO)
body += h; js += j

# Q4 : envoyez-moi un message (perd -> lien4)
body += f'''
<div id="c4m" class="clip eve" data-start="{r2(T["perd"])}" data-duration="{r2(T["lien4"] - T["perd"])}" data-track-index="1">
  {LOGOW}
  <div class="hk9" style="top:170px;width:1700px"><div class="q hid" id="c4mq" style="font-size:84px">C'est souvent ici <span>qu'on perd du monde</span></div></div>
  <div class="big9 hid" id="c4mb"><s>«&nbsp;Envoyez-moi un message&nbsp;»</s></div>
  <div class="eff9 hid" id="c4me">= un effort de plus</div>
</div>'''
js += pop("#c4mq", T["perd"] + .05, E, 40) + pop("#c4mb", T["env"], "back.out(1.6)") + pop("#c4me", T["eff"], "back.out(2)")

# Q4 : un lien unique (lien4 -> c5)
slots = '<div class="x">Lun 10:00</div><div>Mar 14:00</div><div class="x">Mer 09:00</div><div id="c4on">Jeu 18:30</div><div>Ven 11:00</div><div class="x">Sam 10:00</div>'
book = ('<div class="phead"><div class="av">CE</div>Réserver une séance</div>'
        '<div class="cr" style="margin-top:20px"><div class="a">Séance de sophrologie</div><div class="b">1 h · Cabinet ou visio</div></div>'
        f'<div class="gr9 hid" id="c4gr">{slots}</div><div class="bk9 hid" id="c4bk">Réserver</div>')
body += f'''
<div id="c4s" class="clip light" data-start="{r2(T["lien4"])}" data-duration="{r2(T["c5"] - T["lien4"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px;justify-content:flex-start;top:180px"><div class="chap hid" id="c4sc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="c4sh" style="font-size:80px">Un seul lien,<br/><span>partout</span></div></div>
  <div class="sh8" style="top:560px;flex-direction:column;align-items:flex-start"><div class="hid" id="c4p0">Bio Instagram</div><div class="hid" id="c4p1">Fiche Google</div><div class="hid" id="c4p2">Carte de visite</div></div>
  <div class="tm9 hid" id="c4tm" style="top:900px">⏱ Réservé en 2 minutes</div>
  {phone("c4ph", book, 1240, 100)}
</div>'''
js += pop("#c4sc", T["lien4"] + .05, E) + pop("#c4sh", T["lien4"] + .25, E, 40) + fin("#c4ph", T["lien4"] + .6)
js += "".join(pop(f"#c4p{i}", T["pl"] + .3 + i * 1.3) for i in range(3))
js += pop("#c4gr", T["cr"]) + f'tl.to("#c4on",{{backgroundColor:"#2563EB",color:"#fff",duration:.3}},{r2(T["cr"] + 1.6)});\n'
js += pop("#c4bk", T["deux"]) + pop("#c4tm", T["deux"] + .4, "back.out(2)")

# ---------- Q5
h, j = qcard("c5", T["c5"], T["c5q"] + 2.4, 5, "«&nbsp;Je peux en parler<br/>autour de moi&nbsp;?&nbsp;»", "navy", LOGOW,
             lead="La dernière question… celle que l'on oublie")
body += h; js += j

# Q5 : bouche-à-oreille (c5q+2.4 -> fac)
t5s = T["c5q"] + 2.4
fr = ('<div class="phead"><div class="av">A</div>Anne</div>'
      '<div style="position:absolute;left:0;right:0;top:170px">'
      '<div class="b8 hid" id="c5b0">Vous connaissez une sophrologue près d\'ici&nbsp;?</div>'
      '<div class="b8 me hid" id="c5b1">Oui, la mienne&nbsp;! Voici sa page&nbsp;:</div>'
      '<div class="lnk9 hid" id="c5b2"><div class="a">🔗 Cabinet Exemple</div><div class="b">Prestations · avis · réservation</div></div></div>')
body += f'''
<div id="c5m" class="clip warm" data-start="{r2(t5s)}" data-duration="{r2(T["fac"] - t5s)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px"><div class="chap hid" id="c5mc"><b>5</b>Le bouche-à-oreille</div>
    <div class="h hid" id="c5mh" style="font-size:72px">Une source <span>précieuse</span><br/>pour un cabinet</div></div>
  {phone("c5ph", fr, 1240, 100)}
</div>'''
js += pop("#c5mc", t5s + .05, E) + pop("#c5mh", t5s + .25, E, 40) + fin("#c5ph", t5s + .4)
js += pop("#c5b0", t5s + 1.0) + pop("#c5b1", t5s + 2.2) + pop("#c5b2", t5s + 3.0, "back.out(2)")

# Q5 : facilitez-le (fac -> loc)
fm = [("☾", "#EFF6FF", "#2563EB", "Un message<br/>le lendemain", "m1"), ("✎", "#FBF3DC", "#B7791F", "Un compte rendu<br/>facile à retrouver", "m2"),
      ("🔗", "#EEF2FF", "#4338CA", "Un lien simple<br/>à transmettre", "m3")]
fh = "".join(f'<div class="c hid" id="c5f{i}" style="height:400px"><div class="ic" style="background:{bg};color:{c}">{ic}</div><div class="a">{a}</div></div>' for i, (ic, bg, c, a, _) in enumerate(fm))
body += f'''
<div id="c5s" class="clip light" data-start="{r2(T["fac"])}" data-duration="{r2(T["loc"] - T["fac"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="c5sc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="c5sh" style="font-size:66px">Facilitez-le, <span>après chaque séance</span></div></div>
  <div class="f3" style="top:420px">{fh}</div>
</div>'''
js += pop("#c5sc", T["fac"] + .05, E) + pop("#c5sh", T["fac"] + .25, E, 40)
js += "".join(pop(f"#c5f{i}", T[k], y=50) for i, (*_, k) in enumerate(fm))

# Q5 : près de chez vous (loc -> rs)
body += f'''
<div id="c5l" class="clip cream" data-start="{r2(T["loc"])}" data-duration="{r2(T["rs"] - T["loc"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:1500px"><div class="chap hid" id="c5lc" style="color:#B7791F"><b style="background:#0F172A;color:#E9C46A">⌂</b>Près de chez vous</div>
    <div class="h hid" id="c5lh" style="font-size:76px;color:#0F172A">Pensez aussi <span>au local</span></div>
    <div class="lc9"><div class="hid" id="c5l0"><i>↔</i>Des partenariats avec d'autres praticiens</div>
      <div class="hid" id="c5l1"><i>☀</i>Des ateliers découverte</div></div></div>
</div>'''
js += pop("#c5lc", T["loc"] + .05, E) + pop("#c5lh", T["loc"] + .25, E, 40) + pop("#c5l0", T["loc"] + .5, y=40) + pop("#c5l1", T["loc"] + 2.4, y=40)

# ---------- récap (rs -> g)
rc = [("Dites <span>pour qui</span><br/>et comment", T["r1"], ""), ("Rassurez avec<br/><span>de vrais avis</span>", T["r2"], " g"),
      ("Simplifiez la <span>réservation</span> et le bouche-à-oreille", T["r3"], "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += f'''
<div id="r" class="clip light" data-start="{r2(T["rs"])}" data-duration="{r2(T["g"] - T["rs"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>
</div>'''
js += pop("#rk", T["rs"] + .05, E) + "".join(pop(f"#rc{i}", t, y=50) for i, (_, t, _) in enumerate(rc))

# ---------- GuidPilot (g -> z)
gc = [("Votre page", "gpg"), ("Vos prestations", "gpg"), ("Vos avis", "gpg"), ("Réservation", "gres"), ("Paiement en ligne", "gres"),
      ("Espace client", "gesp"), ("Comptes rendus", "gesp")]
gch = "".join(f'<div class="hid" id="gc{i}">{a}</div>' for i, (a, _) in enumerate(gc))
body += f'''
<div id="g" class="clip light" data-start="{r2(T["g"])}" data-duration="{r2(T["z"] - T["g"])}" data-track-index="1">
  <div class="col" style="width:820px;justify-content:flex-start;top:130px"><img class="hid" id="gl" src="assets/logo_couleur.png" alt="GuidPilot" style="width:400px" />
    <div class="h hid" id="gb" style="font-size:60px">Un outil conçu<br/><span>pour les thérapeutes</span></div>
    <div class="chips8" style="margin-top:34px;max-width:820px">{gch}</div></div>
  <div class="zc hid" id="gz1" style="top:200px"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">Compte de démonstration</span></div><img src="assets/avis.png" alt="" /></div>
  <div class="pp8 hid" id="gpp" style="left:980px;top:560px;width:840px;height:440px"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="tp" style="height:130px;padding:28px 44px"><div class="k">VOTRE PAGE</div><div class="n" style="font-size:38px">Cabinet Exemple · Sophrologie</div></div>
    <div class="it">Séance de sophrologie · 1 h<span>Réserver</span></div>
    <div class="it">Séance en visio · 1 h<span>Réserver</span></div></div>
</div>'''
js += f'tl.fromTo("#gl",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"}},{r2(T["g"] + .1)});\n' + pop("#gb", T["g"] + .7, E, 40)
js += "".join(pop(f"#gc{i}", T[k] + (i % 3) * .35) for i, (_, k) in enumerate(gc)) + fin("#gz1", T["gpg"] + .8) + fin("#gpp", T["gres"])

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
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA4}{EXTRA5}{EXTRA7}{EXTRA8}{EXTRA9}</style></head><body>
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

d = ATELIER / "build" / "yt-trouver-clientes"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "avis.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, DUR)
