"""Vidéo YouTube 1920x1080 : « Espace client pour tarologue et voyante : ce que voit votre cliente »
(tuto · public guidance, vendredi 16/10/2026).
Usage : python3 gen_espace_client_guidance.py <voix.wav>  -> build/yt-espace-client-guidance/
Temps calés sur voix/2026-10-16_yt-espace-client-guidance.mp3 (131,6 s) : silencedetect -32 dB / 0,15 s
+ estimation par syllabes, recalée sur les pauses longues (fins de phrases).
Scènes : téléphone « Je ne retrouve plus ma guidance » + pièces éparpillées (accroche visible dès la 1re image),
titre en chemin de 5 étapes, e-mail d'accès illustré + connexion + cadenas, téléphone « Mes rendez-vous » (visio Google Meet,
« Prendre un nouveau rendez-vous »), notification de guidance + lecteur audio + frise « ce soir / dans 3 mois »,
avant / après WhatsApp perso vs fil privé, relevé « Mes factures », écran marine des 4 cadenas (ce qu'elle ne voit jamais),
conseil avec message prêt à copier, citation, récap en 3 cartes, GuidPilot (≤ 15 s), fin marine.
Aucune capture : pas de capture de l'espace client dans le kit → illustrations marquées « Illustration ».
Réutilise CSS et helpers de gen_therapeutes_soir.py.
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_therapeutes_soir.py").read_text()
ns = {"__file__": str(HERE / "gen_therapeutes_soir.py")}
exec(src.split("# ---------- A :")[0], ns)
CSS, EXTRA, ATELIER, KIT = ns["CSS"], ns["EXTRA"], ns["ATELIER"], ns["KIT"]
pop, fin, out, lion, chap, phone, LOGO, E = (ns[k] for k in ("pop", "fin", "out", "lion", "chap", "phone", "LOGO", "E"))

DUR = 132.4
T = dict(t=13.45, s1=20.8, s2=33.6, s3=48.9, s4=62.9, s5=73.3, s6=81.3, s7=92.6, q=105.9, r=109.15, g=117.35, end=123.0)

EXTRA3 = """
.hk3{position:absolute;left:110px;top:150px;width:900px}
.hk3 .b{font-weight:800;font-size:82px;line-height:1.08;letter-spacing:-.03em;color:#0F172A}
.hk3 .b span{color:#2563EB}
.hk3 .s{font-weight:600;font-size:36px;color:#475569;margin-top:30px;line-height:1.35}
.chips{position:absolute;left:110px;top:640px;width:860px;display:flex;flex-wrap:wrap;gap:16px}
.chips div{padding:14px 28px;border-radius:999px;background:#0F172A;font-weight:700;font-size:30px;color:#fff}
.scat3{position:absolute;left:110px;top:560px;width:860px;height:440px}
.it{position:absolute;padding:22px 26px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.08);font-weight:700;font-size:28px;color:#0F172A}
.it small{display:block;font-weight:600;font-size:21px;color:#64748B;margin-top:6px}
.wave{display:flex;align-items:center;gap:5px;margin-top:10px}
.wave i{display:block;width:7px;border-radius:4px;background:#2563EB}
.ts{position:absolute;left:0;right:0;top:150px;text-align:center;font-weight:600;font-size:22px;color:#94A3B8}
.bub.lg{max-width:370px;font-size:28px;line-height:1.32}
.titleT .b{font-size:90px}
.path{position:absolute;left:160px;top:560px;width:1600px;height:300px}
.pl{position:absolute;left:0;top:70px;width:1600px;height:10px;border-radius:5px;background:#CBD5E1;transform-origin:left center}
.st5{position:absolute;top:0;width:150px;height:150px;margin-left:-75px;border-radius:50%;background:#fff;border:10px solid #2563EB;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:58px;color:#0F172A;box-shadow:0 16px 40px rgba(15,23,42,.1)}
.st5.g{border-color:#E9C46A}
.sl5{position:absolute;top:180px;width:300px;margin-left:-150px;text-align:center;font-weight:800;font-size:32px;color:#0F172A;line-height:1.2}
.mail{position:absolute;left:900px;top:170px;width:900px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.mail .mh{padding:26px 36px;border-bottom:2px solid #E2E8F0;background:#F8FAFC}
.mail .mh .f{font-weight:600;font-size:22px;color:#64748B}
.mail .mh .o{font-weight:800;font-size:34px;color:#0F172A;margin-top:6px}
.mail .mb{padding:34px 36px}
.mail .ln{height:14px;border-radius:7px;background:#E2E8F0;margin-top:18px}
.mbtn{display:inline-block;margin-top:34px;padding:20px 40px;border-radius:16px;background:#2563EB;color:#fff;font-weight:800;font-size:30px}
.login{position:absolute;left:900px;top:640px;width:900px;padding:30px 36px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.1)}
.login .lb{font-weight:700;font-size:22px;color:#64748B}
.login .fld{margin-top:12px;height:70px;border-radius:14px;border:2px solid #CBD5E1;display:flex;align-items:center;padding:0 22px;font-weight:600;font-size:28px;color:#0F172A}
.devs{display:flex;gap:16px;margin-top:20px}
.devs div{padding:10px 22px;border-radius:999px;background:#EFF6FF;color:#1D4ED8;font-weight:800;font-size:24px}
.lockb{position:absolute;left:110px;top:820px;display:flex;align-items:center;gap:18px;padding:22px 30px;border-radius:22px;background:#0F172A;color:#fff;font-weight:800;font-size:32px}
.rdv{margin:22px 22px 0;padding:22px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 10px 30px rgba(15,23,42,.06)}
.rdv .k{font-weight:800;font-size:18px;letter-spacing:.12em;color:#2563EB}
.rdv .k.p{color:#94A3B8}
.rdv .a{font-weight:800;font-size:27px;color:#0F172A;margin-top:6px}
.rdv .b{font-weight:600;font-size:21px;color:#64748B;margin-top:4px}
.meet{display:inline-flex;align-items:center;gap:10px;margin-top:14px;padding:10px 18px;border-radius:12px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:21px}
.notif{position:absolute;left:14px;right:14px;bottom:30px;z-index:4;padding:18px 20px;border-radius:22px;background:rgba(255,255,255,.97);border:2px solid #E2E8F0;box-shadow:0 18px 40px rgba(15,23,42,.18);display:flex;gap:14px;align-items:center}
.notif .ic{flex:none;width:52px;height:52px;border-radius:14px;background:#0F172A;display:flex;align-items:center;justify-content:center}
.notif .ic img{width:38px}
.notif .a{font-weight:800;font-size:22px;color:#0F172A}
.notif .b{font-weight:600;font-size:19px;color:#64748B;margin-top:2px}
.gw{margin:22px 22px 0;padding:24px;border-radius:22px;background:#fff;border:2px solid #E2E8F0}
.gw .a{font-weight:800;font-size:26px;color:#0F172A}
.gw .ln{height:12px;border-radius:6px;background:#E2E8F0;margin-top:14px}
.player{margin:18px 22px 0;padding:22px;border-radius:22px;background:#0F172A;color:#fff}
.player .a{font-weight:800;font-size:24px}
.player .row{display:flex;align-items:center;gap:16px;margin-top:16px}
.player .pb{flex:none;width:56px;height:56px;border-radius:50%;background:#2563EB;display:flex;align-items:center;justify-content:center}
.player .wv{display:flex;align-items:center;gap:5px}
.player .wv i{display:block;width:7px;border-radius:4px;background:#93C5FD}
.when{display:flex;gap:20px;margin-top:34px}
.when div{flex:1;padding:22px 24px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;text-align:center}
.when b{display:block;font-weight:800;font-size:34px;color:#0F172A}
.when small{display:block;font-weight:600;font-size:22px;color:#64748B;margin-top:6px}
.bigl{position:absolute;left:110px;top:880px;width:760px;font-weight:800;font-size:40px;color:#15803D}
.split{position:absolute;top:290px;width:820px;height:700px;border-radius:30px;padding:40px}
.split.l{left:110px;background:#FEF2F2;border:2px solid #FECACA}
.split.r{left:990px;background:#F0FDF4;border:2px solid #BBF7D0}
.split .lb{display:inline-flex;align-items:center;gap:12px;padding:10px 24px;border-radius:999px;font-weight:800;font-size:28px}
.split.l .lb{background:#FEE2E2;color:#B91C1C}.split.r .lb{background:#DCFCE7;color:#15803D}
.wa{display:flex;align-items:center;gap:18px;margin-top:20px;padding:18px 22px;border-radius:18px;background:#fff;border:2px solid #FDE2E2}
.wa .av{width:58px;height:58px;font-size:22px;background:#F1F5F9;color:#64748B}
.wa b{display:block;font-weight:800;font-size:27px;color:#0F172A}
.wa small{display:block;font-weight:600;font-size:21px;color:#64748B;margin-top:2px}
.wa .n{margin-left:auto;flex:none;width:40px;height:40px;border-radius:50%;background:#DC2626;color:#fff;font-weight:800;font-size:20px;display:flex;align-items:center;justify-content:center}
.wa.cl{border:3px dashed #DC2626}
.thread{position:relative;margin-top:24px;height:470px}
.thread .bub{max-width:560px;font-size:27px}
.hist{position:absolute;left:40px;right:40px;bottom:36px;text-align:center;font-weight:800;font-size:34px;color:#15803D}
.ledger .lr .st{font-size:22px;height:50px;margin-top:-25px}
.dl{position:absolute;right:170px;top:50%;margin-top:-22px;width:44px;height:44px;border-radius:12px;background:#EFF6FF;display:flex;align-items:center;justify-content:center}
.ask{position:absolute;left:110px;top:800px;width:700px;padding:22px 28px;border-radius:24px;border-bottom-left-radius:8px;background:#fff;border:2px solid #E2E8F0;font-weight:600;font-size:28px;color:#94A3B8}
.ask .x{position:absolute;left:20px;right:20px;top:50%;height:5px;border-radius:3px;background:#DC2626;transform-origin:left center}
.locks{position:absolute;left:110px;top:330px;width:1700px;display:grid;grid-template-columns:1fr 1fr;gap:30px}
.lk{display:flex;align-items:center;gap:26px;padding:34px 40px;border-radius:26px;background:#1E293B;border:2px solid #334155}
.lk .ic{flex:none;width:80px;height:80px;border-radius:20px;background:#0F172A;border:2px solid #E9C46A;display:flex;align-items:center;justify-content:center}
.lk b{display:block;font-weight:800;font-size:40px;color:#fff}
.lk small{display:block;font-weight:600;font-size:24px;color:#94A3B8;margin-top:6px}
.nvt{position:absolute;left:110px;top:120px;width:1700px}
.nvt .k{font-weight:700;font-size:28px;letter-spacing:.14em;color:#E9C46A}
.nvt .b{font-weight:800;font-size:70px;line-height:1.1;letter-spacing:-.02em;color:#fff;margin-top:16px}
.nvt .b span{color:#93C5FD}
.each{position:absolute;left:0;right:0;top:850px;text-align:center}
.each div{display:inline-block;padding:22px 48px;border-radius:999px;background:#fff;color:#0F172A;font-weight:800;font-size:40px}
.each span{color:#2563EB}
.copy{position:absolute;left:960px;top:200px;width:860px;padding:44px 48px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;border-top:10px solid #2563EB;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.copy .tg{display:inline-block;padding:8px 20px;border-radius:999px;background:#EFF6FF;color:#1D4ED8;font-weight:800;font-size:22px;letter-spacing:.06em}
.copy .tx{font-weight:700;font-size:42px;line-height:1.35;color:#0F172A;margin-top:28px}
.copy .tx span{display:inline}
.copy .ft{margin-top:30px;font-weight:600;font-size:24px;color:#64748B}
.rc{position:absolute;left:110px;top:330px;width:1700px;display:flex;gap:34px}
.rcard{flex:1;height:440px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.08);padding:44px 40px;display:flex;flex-direction:column}
.rcard b{display:flex;width:84px;height:84px;border-radius:50%;background:#2563EB;color:#fff;align-items:center;justify-content:center;font-size:42px;font-weight:800}
.rcard.g b{background:#E9C46A;color:#0F172A}
.rcard div{font-weight:800;font-size:44px;line-height:1.18;color:#0F172A;margin-top:40px}
.rcard div span{color:#2563EB}
.gpl{position:absolute;left:0;right:0;top:230px;text-align:center}
.gpl img{width:520px}
.gpl .b{font-weight:800;font-size:66px;line-height:1.12;letter-spacing:-.02em;color:#0F172A;margin-top:46px}
.gpl .b span{color:#2563EB}
.gch{position:absolute;left:0;right:0;top:720px;display:flex;justify-content:center;gap:26px}
.gch div{padding:20px 40px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:36px}
"""

LOCK = ('<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="#E9C46A" stroke-width="2.2" stroke-linecap="round">'
        '<rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>')
PLAY = '<svg width="24" height="24" viewBox="0 0 24 24"><path d="M7 4l13 8-13 8z" fill="#fff"/></svg>'
DL = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.6" stroke-linecap="round"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'
wave = lambda hs: "".join(f'<i style="height:{h}px"></i>' for h in hs)
body, js = "", ""

# ---------- A : « Je ne retrouve plus ma guidance » (0 -> 13.45) — accroche lisible dès l'image 0
inner = ('<div class="phead"><div class="av">CR</div>Camille R.</div><div class="ts">Aujourd\'hui · 21:14</div>'
         '<div class="bub her lg" id="ab0" style="top:200px">Vous pouvez me renvoyer ma guidance&nbsp;?</div>'
         '<div class="bub her lg hid" id="ab1" style="top:360px">Je ne la retrouve plus…</div>'
         '<div class="bub her lg hid" id="ab2" style="top:490px">C\'était un vocal, il y a deux mois.</div>'
         '<div class="bub her lg hid" id="ab3" style="top:660px">Ou peut-être un e-mail&nbsp;?</div>')
body += f'''
<div id="a" class="clip light" data-start="0" data-duration="{T['t']}" data-track-index="1">
  {LOGO}
  <div class="hk3"><div class="b">« Je ne retrouve plus<br/><span>ma guidance… »</span></div>
    <div class="s hid" id="as">Vous avez déjà reçu ce message&nbsp;?</div></div>
  <div class="chips" id="ach"><div class="hid" id="ac0">Tarologue</div><div class="hid" id="ac1">Voyante</div><div class="hid" id="ac2">Médium</div></div>
  <div class="scat3">
    <div class="it hid" id="ai0" style="left:0;top:20px;transform:rotate(-4deg)">Message vocal · 4:12<div class="wave">{wave([14, 30, 22, 40, 18, 34, 26, 12, 30, 20])}</div><small>quelque part dans WhatsApp</small></div>
    <div class="it hid" id="ai1" style="left:430px;top:60px;transform:rotate(3deg)">Re : Re : votre guidance<small>noyé dans les e-mails</small></div>
    <div class="it hid" id="ai2" style="left:180px;top:250px;transform:rotate(-2deg)">Capture d'écran.png<small>perdue dans la galerie photos</small></div>
  </div>
  <div style="position:absolute;inset:0">{phone("ap", inner, 1180, 100)}</div>
</div>'''
js += 'gsap.set("#ap",{opacity:1});\n'
js += pop("#ab1", 1.8, y=20) + pop("#as", 3.4, E) + pop("#ac0", 3.95) + pop("#ac1", 4.7) + pop("#ac2", 5.3)
js += pop("#ab2", 6.5, y=20) + pop("#ab3", 9.0, y=20)
js += out("#ach", 8.5, .3) + pop("#ai0", 10.6) + pop("#ai1", 11.3) + pop("#ai2", 12.3)

# ---------- T : titre en chemin (13.45 -> 20.8)
steps = ["L'accès", "Ses<br/>rendez-vous", "Ses<br/>guidances", "La<br/>messagerie", "Ses<br/>factures"]
xs = [0, 400, 800, 1200, 1600]
ph = "".join(f'<div class="st5{" g" if i == 2 else ""} hid" id="tp{i}" style="left:{x}px">{i + 1}</div>'
             f'<div class="sl5 hid" id="tl{i}" style="left:{x}px">{s}</div>' for i, (s, x) in enumerate(zip(steps, xs)))
body += f'''
<div id="t" class="clip light" data-start="{T['t']}" data-duration="{round(T['s1'] - T['t'], 2)}" data-track-index="1">
  {LOGO}
  <div class="titleT hid" id="tt" style="top:150px"><div class="k">L'ESPACE CLIENT · PRATICIENNES EN GUIDANCE</div>
    <div class="b">Ce que voit <span>votre cliente</span></div></div>
  <div class="path"><div class="pl hid" id="tpl"></div>{ph}</div>
</div>'''
js += 'tl.fromTo("#tt",{opacity:0,y:40},{opacity:1,y:0,duration:.7,ease:"back.out(1.4)"},13.55);\n'
js += 'tl.fromTo("#tpl",{opacity:1,scaleX:0},{opacity:1,scaleX:1,duration:2.4,ease:"power1.inOut"},15.4);\n'
js += "".join(pop(f"#tp{i}", 15.4 + i * .55) + pop(f"#tl{i}", 15.55 + i * .55) for i in range(5))

# ---------- 1 : l'accès (20.8 -> 33.6)
h1, j1 = chap("s1", 1, "L'accès", "Un lien par e-mail,<br/><span>et elle est chez elle</span>", T['s1'])
body += f'''
<div id="s1" class="clip light" data-start="{T['s1']}" data-duration="{round(T['s2'] - T['s1'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px;top:-120px">{h1}
    <div class="ok hid" id="s1o1"><i>✓</i>Dès sa première réservation</div>
    <div class="ok hid" id="s1o2"><i>✓</i>Connexion avec son adresse e-mail</div></div>
  <div class="mail hid" id="s1m"><span class="illus" style="right:24px;top:22px">Illustration</span>
    <div class="mh"><div class="f">De : votre praticienne · via GuidPilot</div><div class="o">Votre espace client est prêt</div></div>
    <div class="mb"><div class="ln" style="width:92%;margin-top:0"></div><div class="ln" style="width:78%"></div>
      <div class="mbtn hid" id="s1b">Accéder à mon espace</div></div></div>
  <div class="login hid" id="s1l"><div class="lb">Adresse e-mail</div><div class="fld">camille@exemple.fr</div>
    <div class="devs hid" id="s1d"><div>Téléphone</div><div>Ordinateur</div></div></div>
  <div class="lockb hid" id="s1k">{LOCK.format(s=40)}Elle ne voit que ce qui la concerne</div>
</div>'''
js += j1 + fin("#s1m", 21.6) + pop("#s1o1", 22.0) + pop("#s1b", 24.5)
js += 'tl.to("#s1b",{scale:.94,duration:.15,yoyo:true,repeat:1},25.6);\n'
js += pop("#s1l", 26.4) + pop("#s1o2", 26.6) + pop("#s1d", 28.2)
js += 'tl.fromTo("#s1k",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.5,ease:"back.out(2)"},30.2);\n'

# ---------- 2 : ses rendez-vous (33.6 -> 48.9)
h2, j2 = chap("s2", 2, "Ses rendez-vous", "Passés, à venir…<br/><span>et le suivant</span>", T['s2'])
inner = ('<div class="phead">Mes rendez-vous</div>'
         '<div class="rdv hid" id="r0"><div class="k">À VENIR</div><div class="a">Tirage du mois</div><div class="b">Jeudi 22 octobre · 18:00 · 1 h</div>'
         '<div class="meet hid" id="r0m">● Visio · Google Meet</div></div>'
         '<div class="rdv hid" id="r1"><div class="k p">PASSÉ</div><div class="a">Guidance écrite</div><div class="b">Mardi 13 octobre</div></div>'
         '<div class="btn hid" id="r2" style="height:auto;padding:18px 20px;text-align:center;line-height:1.25">Prendre un nouveau rendez-vous</div>'
         '<div class="noted hid" id="r3" style="margin:20px 22px 0">✓ Rendez-vous réservé</div>')
body += f'''
<div id="s2" class="clip light" data-start="{T['s2']}" data-duration="{round(T['s3'] - T['s2'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px">{h2}
    <div class="ok hid" id="s2o1"><i>✓</i>Séances passées et à venir</div>
    <div class="ok hid" id="s2o2"><i>✓</i>Date, heure, prestation</div>
    <div class="ok hid" id="s2o3"><i>✓</i>Le lien Google Meet pour la visio</div>
    <div class="ok hid" id="s2o4"><i>✓</i>Elle reprend rendez-vous elle-même</div></div>
  {phone("s2p", inner, 1180, 100)}
</div>'''
js += j2 + fin("#s2p", 34.0) + pop("#s2o1", 35.6) + pop("#r0", 35.8, y=20) + pop("#r1", 36.6, y=20)
js += pop("#s2o2", 37.9) + 'tl.to("#r0",{borderColor:"#2563EB",duration:.3},38.0);\n'
js += pop("#s2o3", 40.4) + pop("#r0m", 41.2)
js += pop("#s2o4", 43.9) + pop("#r2", 44.3) + 'tl.to("#r2",{scale:.94,duration:.15,yoyo:true,repeat:1},46.3);\n' + pop("#r3", 46.9)

# ---------- 3 : ses guidances (48.9 -> 62.9)
h3, j3 = chap("s3", 3, "Ses guidances · le plus important", "Elle la relit,<br/><span>elle la réécoute</span>", T['s3'])
wv = wave([16, 30, 22, 42, 18, 36, 26, 14, 32, 22, 40, 18, 28, 12, 24])
inner = ('<div class="phead">Mes guidances</div>'
         '<div class="notif hid" id="g3n"><div class="ic"><img src="assets/favicon.png" alt="" /></div>'
         '<div><div class="a">Nouvelle guidance disponible</div><div class="b">Votre praticienne vous a livré une guidance</div></div></div>'
         '<div class="gw hid" id="g3w"><div class="a">Guidance écrite · 16 oct.</div><div class="ln" style="width:95%"></div>'
         '<div class="ln" style="width:88%"></div><div class="ln" style="width:70%"></div></div>'
         f'<div class="player hid" id="g3p"><div class="a">Guidance vocale · 4:12</div><div class="row"><div class="pb">{PLAY}</div>'
         f'<div class="wv" id="g3wv">{wv}</div></div></div>'
         '<div class="gw hid" id="g3o"><div class="a">Guidance vocale · 13 sept.</div><div class="ln" style="width:60%"></div></div>')
body += f'''
<div id="s3" class="clip warm" data-start="{T['s3']}" data-duration="{round(T['s4'] - T['s3'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:800px;top:-60px">{h3}
    <div class="when"><div class="hid" id="g3a"><b>Ce soir</b><small>elle la relit</small></div>
      <div class="hid" id="g3b"><b>Dans 3 mois</b><small>elle réécoute votre voix</small></div></div></div>
  <div class="bigl hid" id="g3x">Votre travail ne se perd plus.</div>
  {phone("s3p", inner, 1180, 100)}
</div>'''
js += j3 + 'tl.to("#s3c b",{backgroundColor:"#E9C46A",color:"#0F172A",duration:.3},50.0);\n'
js += fin("#s3p", 50.2) + pop("#g3w", 51.4, y=20) + pop("#g3p", 52.6, y=20)
js += 'tl.fromTo("#g3n",{opacity:0,y:60},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},54.4);\n'
js += pop("#g3a", 56.8) + 'tl.to("#g3w",{borderColor:"#2563EB",duration:.3},56.9);\n'
js += pop("#g3o", 59.95, y=20) + pop("#g3b", 58.5) + 'tl.to("#g3wv i",{scaleY:.4,duration:.25,yoyo:true,repeat:5,stagger:.05,ease:"sine.inOut"},58.6);\n'
js += out("#g3n", 59.6, .3) + pop("#g3x", 60.0)

# ---------- 4 : la messagerie, avant / après (62.9 -> 73.3)
body += f'''
<div id="s4" class="clip light" data-start="{T['s4']}" data-duration="{round(T['s5'] - T['s4'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:100px"><div class="chap hid" id="s4c"><b>4</b>La messagerie</div>
    <div class="h hid" id="s4h" style="font-size:60px">Un fil privé, <span>à part de votre WhatsApp</span></div></div>
  <div class="split l hid" id="s4l"><div class="lb">✕ WhatsApp personnel</div>
    <div class="wa"><div class="av">M</div><div><b>Maman</b><small>Tu viens dimanche ?</small></div><div class="n">2</div></div>
    <div class="wa"><div class="av">É</div><div><b>Groupe de l'école</b><small>Réunion jeudi à 18 h</small></div><div class="n">14</div></div>
    <div class="wa cl hid" id="s4w"><div class="av">CR</div><div><b>Camille R.</b><small>Une question sur ma guidance…</small></div><div class="n">1</div></div>
    <div class="wa"><div class="av">S</div><div><b>Sophie</b><small>Photo</small></div><div class="n">3</div></div></div>
  <div class="split r hid" id="s4r"><div class="lb">✓ Fil privé de Camille</div><span class="illus" style="right:24px;top:30px">Illustration</span>
    <div class="thread">
      <div class="bub her hid" id="s4b0" style="top:0">J'ai une question sur ma guidance du 13&nbsp;octobre.</div>
      <div class="bub me hid" id="s4b1" style="top:170px">Bien sûr, je vous réponds ici même.</div></div>
    <div class="hist hid" id="s4x">✓ Tout l'historique au même endroit</div></div>
</div>'''
js += pop("#s4c", 63.0, E) + pop("#s4h", 63.3, E, 40)
js += 'tl.fromTo("#s4l",{opacity:0,x:-60},{opacity:1,x:0,duration:.6,ease:"power3.out"},64.6);\n'
js += pop("#s4w", 66.6) + 'tl.to("#s4w",{x:12,duration:.08,yoyo:true,repeat:5},67.1);\n'
js += 'tl.fromTo("#s4r",{opacity:0,x:60},{opacity:1,x:0,duration:.6,ease:"power3.out"},68.0);\n'
js += pop("#s4b0", 68.5, y=20) + 'tl.to("#s4l",{opacity:.45,duration:.5},69.5);\n' + pop("#s4b1", 70.8, y=20) + pop("#s4x", 72.4)

# ---------- 5 : ses factures (73.3 -> 81.3)
h5, j5 = chap("s5", 5, "Ses factures", "Elle les retrouve<br/><span>sans vous les demander</span>", T['s5'])
fac = [("F-2026-0142", "Tirage du mois · 16 oct."), ("F-2026-0118", "Guidance écrite · 13 oct."), ("F-2026-0097", "Séance découverte · 2 sept.")]
lrs = "".join(f'<div class="lr hid" id="f{i}"><div class="ic">€</div><div><div class="a">{a}</div><div class="b">{b}</div></div>'
              f'<div class="dl">{DL}</div><div class="st v">Réglée</div></div>' for i, (a, b) in enumerate(fac))
body += f'''
<div id="s5" class="clip light" data-start="{T['s5']}" data-duration="{round(T['s6'] - T['s5'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:740px;top:-140px">{h5}</div>
  <div class="ask hid" id="s5a">« Vous pouvez me renvoyer ma facture&nbsp;? »<div class="x" id="s5ax"></div></div>
  <div class="ledger hid" id="s5l"><span class="illus" style="right:30px;top:30px">Illustration</span>
    <div class="tt">Mes factures</div><div class="dd">et l'historique de mes règlements</div>{lrs}</div>
</div>'''
js += j5 + fin("#s5l", 74.2) + pop("#f0", 76.4) + pop("#f1", 76.9) + pop("#f2", 77.4)
js += 'tl.to("#s5l .dd",{color:"#2563EB",duration:.3},79.0);\n'
js += pop("#s5a", 79.2) + 'tl.fromTo("#s5ax",{scaleX:0},{scaleX:1,duration:.5,ease:"power2.inOut"},80.4);\n'

# ---------- 6 : ce qu'elle ne voit jamais (81.3 -> 92.6)
lk = [("Vos notes personnelles", "restent privées", 83.4), ("Les autres clientes", "invisibles pour elle", 85.8),
      ("Votre agenda complet", "elle ne voit que ses séances", 87.5), ("Vos revenus", "ils ne regardent que vous", 88.8)]
lks = "".join(f'<div class="lk hid" id="k{i}"><div class="ic">{LOCK.format(s=44)}</div><div><b>{a}</b><small>{b}</small></div></div>'
              for i, (a, b, _) in enumerate(lk))
body += f'''
<div id="s6" class="clip navy" data-start="{T['s6']}" data-duration="{round(T['s7'] - T['s6'], 2)}" data-track-index="1">
  <div class="nvt"><div class="k hid" id="s6k">ET MAINTENANT</div><div class="b hid" id="s6b">Ce que votre cliente <span>ne voit jamais</span></div></div>
  <div class="locks">{lks}</div>
  <div class="each hid" id="s6e"><div>Chacune ne voit <span>que ce qui la concerne.</span></div></div>
</div>'''
js += pop("#s6k", 81.4, E) + pop("#s6b", 82.1, E, 40)
js += "".join(pop(f"#k{i}", t) for i, (_, _, t) in enumerate(lk))
js += 'tl.fromTo("#s6e",{opacity:0,y:30},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},89.8);\n'

# ---------- 7 : le conseil + message prêt à copier (92.6 -> 105.9)
chunks = [("« Votre guidance, ", 99.7), ("vos rendez-vous et vos factures vous attendent dans votre espace. ", 100.7), ("Vous pouvez m'y écrire à tout moment. »", 104.1)]
ctx = "".join(f'<span class="hid" id="cp{i}">{t}</span>' for i, (t, _) in enumerate(chunks))
body += f'''
<div id="s7" class="clip warm" data-start="{T['s7']}" data-duration="{round(T['q'] - T['s7'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:780px">
    <div class="cons hid" id="s7k" style="margin-top:0"><div class="l">LE CONSEIL · AVEC OU SANS OUTIL</div>
      <div class="t">À la fin de la première séance, dites-lui <span style="color:#2563EB">où elle retrouvera tout</span>.</div></div>
    <div class="ok hid" id="s7o1"><i>✓</i>Une seule phrase suffit</div>
    <div class="ok hid" id="s7o2"><i>✓</i>Elle sait où revenir</div></div>
  <div class="copy hid" id="s7c"><div class="tg">MESSAGE PRÊT À COPIER</div><div class="tx">{ctx}</div>
    <div class="ft hid" id="s7f">À adapter avec vos mots.</div></div>
</div>'''
js += pop("#s7k", 92.8, E) + pop("#s7o1", 96.2) + pop("#s7o2", 97.7)
js += fin("#s7c", 98.9) + "".join(f'tl.fromTo("#cp{i}",{{opacity:0}},{{opacity:1,duration:.5}},{t});\n' for i, (_, t) in enumerate(chunks))
js += pop("#s7f", 104.9)

# ---------- citation (105.9 -> 109.15)
body += f'''
<div id="q" class="clip light" data-start="{T['q']}" data-duration="{round(T['r'] - T['q'], 2)}" data-track-index="1">
  {LOGO}
  <div class="quote"><div class="qm hid" id="qm">“</div>
    <div class="q hid" id="qq">Une cliente qui sait où trouver les choses<br/><span>se sent accompagnée.</span></div></div>
</div>'''
js += pop("#qm", 105.95, E) + 'tl.fromTo("#qq",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},106.05);\n'

# ---------- récap en 3 points (109.15 -> 117.35)
rc = [("Un seul espace<br/><span>pour votre cliente</span>", 110.0, ""), ("Ses guidances,<br/><span>toujours à portée de main</span>", 111.8, " g"),
      ("Vos notes<br/><span>restent les vôtres</span>", 115.1, "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += f'''
<div id="r" class="clip light" data-start="{T['r']}" data-duration="{round(T['g'] - T['r'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>
</div>'''
js += pop("#rk", 109.25, E) + "".join(pop(f"#rc{i}", t, y=50) for i, (_, t, _) in enumerate(rc))

# ---------- GuidPilot (117.35 -> 123.0)
body += f'''
<div id="g" class="clip light" data-start="{T['g']}" data-duration="{round(T['end'] - T['g'], 2)}" data-track-index="1">
  <div class="gpl hid" id="gl"><img src="assets/logo_couleur.png" alt="GuidPilot" />
    <div class="b">L'espace client est inclus,<br/><span>avec tout votre cabinet</span></div></div>
  <div class="gch"><div class="hid" id="gc0">Agenda</div><div class="hid" id="gc1">Fiches clientes</div><div class="hid" id="gc2">Factures</div></div>
</div>'''
js += 'tl.fromTo("#gl",{opacity:0,scale:.92},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},117.45);\n'
js += pop("#gc0", 120.0) + pop("#gc1", 121.4) + pop("#gc2", 122.2)

# ---------- fin marine (123.0 -> DUR)
body += f'''
<div id="z" class="clip navy" data-start="{T['end']}" data-duration="{round(DUR - T['end'], 2)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard hid" id="z7">✓ Sans carte bancaire</div>
    <div class="url hid" id="z8">guidpilot.fr</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += 'tl.fromTo("#z6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},123.1);\n'
js += pop("#z7", 125.6) + pop("#z8", 126.9) + pop("#z9", 128.9)
js += 'tl.to("#z9",{scale:1.06,duration:.45,yoyo:true,repeat:3,ease:"sine.inOut"},129.8);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA3}</style></head><body>
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

d = ATELIER / "build" / "yt-espace-client-guidance"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
shutil.copy(KIT / "assets" / "logo_blanc.png", d / "assets" / "logo_blanc.png")
shutil.copy(KIT / "assets" / "favicon.png", d / "assets" / "favicon.png")
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
