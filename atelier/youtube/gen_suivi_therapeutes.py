"""Vidéo YouTube 1920x1080 : « Sophrologue, hypnothérapeute : organiser le suivi de vos clientes sur plusieurs séances »
(tuto · public thérapeutes, mardi 20/10/2026).
Usage : python3 gen_suivi_therapeutes.py <voix.wav>  -> build/yt-suivi-therapeutes/
Temps calés sur voix/2026-10-20_yt-suivi-therapeutes-plusieurs-seances.mp3 (133,4 s) : silencedetect -35 dB / 0,12 s
+ estimation par syllabes, recalée à la main sur les pauses de fin de phrase.
Scènes : carnet papier illustré + 3 questions (accroche lisible dès l'image 0), titre en chemin de 5 étapes,
fiche cliente illustrée (frise + onglets), bloc-notes « 2 minutes, 3 questions » + cadenas, écran partagé
notes privées / compte rendu partagé, flux écrire-vocal → rendez-vous → espace client + téléphone notifié,
carte forfait 5 séances qui se décompte + date suivante + « Prendre un nouveau rendez-vous »,
questions de bilan puis capture avis.png (Compte de démonstration) entourée, récap 3 cartes, GuidPilot (≤ 18 s), fin marine.
Vocabulaire thérapeutes : aucun terme médical (séance, cabinet, clientes, compte rendu de séance).
Réutilise CSS et helpers de gen_therapeutes_soir.py.
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_therapeutes_soir.py").read_text()
ns = {"__file__": str(HERE / "gen_therapeutes_soir.py")}
exec(src.split("# ---------- A :")[0], ns)
CSS, EXTRA, ATELIER, KIT = ns["CSS"], ns["EXTRA"], ns["ATELIER"], ns["KIT"]
pop, fin, out, chap, phone, LOGO, E = (ns[k] for k in ("pop", "fin", "out", "chap", "phone", "LOGO", "E"))

DUR = 134.0
T = dict(t=15.4, s1=24.4, s2=40.8, s3=58.3, s3b=65.0, s4=75.5, s5=94.4, s5b=103.4, r=110.45, g=116.85, end=124.8)

EXTRA4 = """
.hk4{position:absolute;left:110px;top:140px;width:900px}
.hk4 .k{font-weight:700;font-size:28px;letter-spacing:.14em;color:#2563EB}
.hk4 .b{font-weight:800;font-size:96px;line-height:1.04;letter-spacing:-.03em;color:#0F172A;margin-top:18px}
.hk4 .b span{color:#2563EB}
.qs{position:absolute;left:110px;top:470px;width:860px}
.qq{display:flex;align-items:center;gap:22px;margin-top:22px;padding:24px 30px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07);font-weight:700;font-size:36px;color:#0F172A}
.qq i{font-style:normal;flex:none;width:58px;height:58px;border-radius:50%;background:#FEF3C7;color:#92400E;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:32px}
.prof4{position:absolute;left:110px;top:900px;display:flex;gap:16px}
.prof4 div{padding:14px 28px;border-radius:999px;background:#0F172A;font-weight:700;font-size:30px;color:#fff}
.nb{position:absolute;left:1060px;top:150px;width:720px;height:820px}
.nbk{position:absolute;left:40px;top:40px;width:620px;height:760px;border-radius:12px 26px 26px 12px;background:#FFFDF7;border:2px solid #E7DFC9;border-left:34px solid #1E3A8A;box-shadow:0 30px 80px rgba(15,23,42,.16);transform:rotate(-3deg);padding:60px 50px}
.nbk .rl{height:2px;background:#E7E1D0;margin-top:46px}
.scr{position:absolute;font-family:"Inter",sans-serif;font-weight:600;font-style:italic;color:#475569}
.post{position:absolute;width:220px;height:200px;padding:22px;background:#FDE68A;box-shadow:0 14px 30px rgba(15,23,42,.15);font-weight:700;font-size:24px;color:#6B4E16;line-height:1.3}
.qmk{position:absolute;font-weight:800;font-size:120px;color:#DC2626;opacity:.85}
.st5{position:absolute;top:0;width:150px;height:150px;margin-left:-75px;border-radius:50%;background:#fff;border:10px solid #2563EB;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:58px;color:#0F172A;box-shadow:0 16px 40px rgba(15,23,42,.1)}
.st5.g{border-color:#E9C46A}
.sl5{position:absolute;top:180px;width:300px;margin-left:-150px;text-align:center;font-weight:800;font-size:32px;color:#0F172A;line-height:1.2}
.notif{position:absolute;left:14px;right:14px;bottom:30px;z-index:4;padding:18px 20px;border-radius:22px;background:rgba(255,255,255,.97);border:2px solid #E2E8F0;box-shadow:0 18px 40px rgba(15,23,42,.18);display:flex;gap:14px;align-items:center}
.notif .ic{flex:none;width:52px;height:52px;border-radius:14px;background:#0F172A;display:flex;align-items:center;justify-content:center}
.notif .ic img{width:38px}
.notif .a{font-weight:800;font-size:22px;color:#0F172A}
.notif .b{font-weight:600;font-size:19px;color:#64748B;margin-top:2px}
.inside i{display:inline-block;width:16px;height:16px;border-radius:50%;background:#E9C46A}
.path5{position:absolute;left:160px;top:560px;width:1600px;height:320px}
.pl5{position:absolute;left:0;top:70px;width:1600px;height:10px;border-radius:5px;background:#CBD5E1;transform-origin:left center}
.gpbadge{position:absolute;left:0;right:0;top:930px;text-align:center}
.gpbadge div{display:inline-flex;align-items:center;gap:18px;padding:16px 34px;border-radius:999px;background:#fff;border:2px solid #E2E8F0;font-weight:800;font-size:32px;color:#0F172A;box-shadow:0 14px 34px rgba(15,23,42,.08)}
.gpbadge img{height:40px}
.inside{display:inline-flex;align-items:center;gap:14px;margin-top:34px;padding:14px 26px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:28px;align-self:flex-start}
.inside img{height:30px}
.tabs{position:absolute;left:40px;right:40px;bottom:40px;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.tabs div{padding:22px 26px;border-radius:20px;background:#EFF6FF;border:2px solid #BFDBFE;font-weight:800;font-size:30px;color:#1D4ED8;text-align:center}
.pad{position:absolute;left:900px;top:150px;width:920px;height:800px;border-radius:26px;background:#FFFDF7;border:2px solid #E7DFC9;box-shadow:0 30px 80px rgba(15,23,42,.12);padding:50px 56px}
.pad .tt{font-weight:800;font-size:40px;color:#0F172A}
.pad .dd{font-weight:600;font-size:24px;color:#8A6A2B;margin-top:8px}
.nl3{display:flex;align-items:flex-start;gap:22px;margin-top:40px}
.nl3 b{flex:none;width:60px;height:60px;border-radius:50%;background:#0F172A;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:30px}
.nl3 div{font-weight:700;font-size:36px;line-height:1.25;color:#0F172A;padding-top:8px}
.nl3 small{display:block;font-weight:600;font-size:24px;color:#94A3B8;margin-top:8px;font-style:italic}
.timer{position:absolute;right:50px;top:50px;padding:12px 24px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:28px}
.priv{position:absolute;left:56px;right:56px;bottom:44px;display:flex;align-items:center;gap:20px;padding:24px 30px;border-radius:22px;background:#0F172A;color:#fff;font-weight:800;font-size:32px}
.priv small{display:block;font-weight:600;font-size:23px;color:#CBD5E1;margin-top:4px}
.two{position:absolute;top:330px;width:820px;height:540px;border-radius:30px;padding:44px}
.two.l{left:110px;background:#FBF3DC;border:2px solid #F1DFA6}
.two.r{left:990px;background:#EFF6FF;border:2px solid #BFDBFE}
.two .lb{display:inline-flex;align-items:center;gap:14px;padding:10px 24px;border-radius:999px;font-weight:800;font-size:28px}
.two.l .lb{background:#0F172A;color:#fff}.two.r .lb{background:#2563EB;color:#fff}
.two .ttl{font-weight:800;font-size:46px;line-height:1.15;color:#0F172A;margin-top:30px}
.two .row{display:flex;align-items:center;gap:16px;margin-top:22px;font-weight:600;font-size:30px;color:#334155}
.two .row i{font-style:normal;flex:none;width:14px;height:14px;border-radius:50%;background:#0F172A}
.two.r .row i{background:#2563EB}
.two .ln{height:14px;border-radius:7px;background:rgba(15,23,42,.1);margin-top:22px}
.flow{position:absolute;left:110px;top:310px;width:1000px}
.fs{display:flex;align-items:center;gap:24px;margin-bottom:26px;padding:24px 30px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07)}
.fs .ic{flex:none;width:72px;height:72px;border-radius:20px;background:#EFF6FF;display:flex;align-items:center;justify-content:center}
.fs b{display:block;font-weight:800;font-size:36px;color:#0F172A}
.fs small{display:block;font-weight:600;font-size:24px;color:#64748B;margin-top:4px}
.fs .or{margin-left:auto;padding:8px 18px;border-radius:999px;background:#F1F5F9;font-weight:800;font-size:22px;color:#64748B}
.seen{display:inline-flex;align-items:center;gap:10px;margin:18px 22px 0;padding:12px 20px;border-radius:14px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:22px}
.fk{position:absolute;left:960px;top:170px;width:860px;padding:46px 50px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.fk .k{font-weight:800;font-size:22px;letter-spacing:.12em;color:#2563EB}
.fk .a{font-weight:800;font-size:46px;color:#0F172A;margin-top:10px}
.fk .b{font-weight:600;font-size:26px;color:#64748B;margin-top:6px}
.dots{display:flex;gap:22px;margin-top:40px}
.dots div{width:110px;height:110px;border-radius:50%;border:8px solid #CBD5E1;background:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:40px;color:#94A3B8}
.dots div.on{border-color:#2563EB;background:#2563EB;color:#fff}
.left{display:flex;align-items:center;justify-content:space-between;margin-top:40px;padding:24px 30px;border-radius:22px;background:#F8FAFC;border:2px solid #E2E8F0}
.left span{font-weight:700;font-size:30px;color:#334155}
.left b{font-weight:800;font-size:54px;color:#2563EB}
.nxt{position:absolute;left:960px;top:760px;width:860px;display:flex;gap:24px}
.nxt div{flex:1;padding:24px 28px;border-radius:24px;background:#0F172A;color:#fff;font-weight:800;font-size:30px;line-height:1.25}
.nxt div small{display:block;font-weight:600;font-size:22px;color:#93C5FD;margin-bottom:6px}
.nxt div.bl{background:#2563EB}
.bq{position:absolute;left:960px;top:330px;width:860px}
.bq .bub{position:relative;display:table;max-width:760px;margin-bottom:30px;font-size:38px;padding:28px 34px}
.bq .bub.me{margin-left:auto}
.bq .bub.her{left:0}
.soft{display:inline-block;margin-top:10px;padding:16px 30px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:800;font-size:32px}
.af{position:absolute;left:880px;top:200px;width:940px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.af .bar{height:46px;background:#F1F5F9;border-bottom:2px solid #E2E8F0;display:flex;align-items:center;padding-left:20px;gap:10px}
.af .dot{width:13px;height:13px;border-radius:50%;background:#CBD5E1}
.af .demo{position:absolute;right:18px;top:9px;font-size:18px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:3px 14px}
.af img{display:block;width:940px}
.ring2{position:absolute;left:8px;top:150px;width:232px;height:128px;border:6px solid #E9C46A;border-radius:24px}
.avl{position:absolute;left:880px;top:600px;width:940px;display:flex;flex-direction:column;gap:18px}
.avl div{display:flex;align-items:center;gap:18px;padding:22px 28px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;font-weight:800;font-size:32px;color:#0F172A}
.avl div i{font-style:normal;flex:none;width:50px;height:50px;border-radius:50%;background:#DCFCE7;color:#16A34A;display:flex;align-items:center;justify-content:center;font-size:26px}
.rc{position:absolute;left:110px;top:330px;width:1700px;display:flex;gap:34px}
.rcard{flex:1;height:440px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.08);padding:44px 40px;display:flex;flex-direction:column}
.rcard b{display:flex;width:84px;height:84px;border-radius:50%;background:#2563EB;color:#fff;align-items:center;justify-content:center;font-size:42px;font-weight:800}
.rcard.g b{background:#E9C46A;color:#0F172A}
.rcard div{font-weight:800;font-size:44px;line-height:1.18;color:#0F172A;margin-top:40px}
.rcard div span{color:#2563EB}
.gpl{position:absolute;left:0;right:0;top:200px;text-align:center}
.gpl img{width:500px}
.gpl .b{font-weight:800;font-size:66px;line-height:1.12;letter-spacing:-.02em;color:#0F172A;margin-top:40px}
.gpl .b span{color:#2563EB}
.gch{position:absolute;left:0;right:0;top:760px;display:flex;justify-content:center;gap:22px}
.gch div{padding:18px 34px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:32px}
"""

LOCK = ('<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round">'
        '<rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>')
PEN = '<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.2" stroke-linecap="round"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg>'
MIC = '<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>'
CAL = '<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.2" stroke-linecap="round"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'
USR = '<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.2" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>'
GPB = '<img src="assets/logo_couleur.png" alt="GuidPilot" />'
INSIDE = '<div class="inside hid" id="{id}"><i></i>Dans GuidPilot</div>'
body, js = "", ""

# ---------- A : le carnet de Sophie (0 -> 15.4) — accroche lisible dès l'image 0
qs = [("Qu'avait-on abordé la dernière fois&nbsp;?", 4.45), ("Combien de séances lui reste-t-il&nbsp;?", 6.35), ("La 3<sup>e</sup> séance est-elle réglée&nbsp;?", 8.05)]
qh = "".join(f'<div class="qq hid" id="aq{i}"><i>?</i><span>{t}</span></div>' for i, (t, _) in enumerate(qs))
body += f'''
<div id="a" class="clip light" data-start="0" data-duration="{T['t']}" data-track-index="1">
  {LOGO}
  <div class="hk4"><div class="k">MARDI · 4<sup>e</sup> SÉANCE</div><div class="b">Sophie arrive.<br/><span>Et votre carnet&nbsp;?</span></div></div>
  <div class="qs">{qh}</div>
  <div class="prof4" id="apr"><div class="hid" id="ap0">Sophrologue</div><div class="hid" id="ap1">Hypnothérapeute</div><div class="hid" id="ap2">Praticienne Reiki</div></div>
  <div class="nb"><span class="illus" style="right:40px;top:0">Illustration</span>
    <div class="nbk" id="anb">
      <div class="scr" style="left:60px;top:60px;font-size:30px">Sophie — 3<sup>e</sup> séance ?</div>
      <div class="scr" style="left:90px;top:130px;font-size:26px;text-decoration:line-through">rappeler jeudi</div>
      <div class="scr" style="left:60px;top:210px;font-size:26px">réglé ? chèque… ou virement</div>
      <div class="scr" style="left:120px;top:300px;font-size:26px">voir notes du 6/10 (où ?)</div>
      <div class="scr" style="left:60px;top:390px;font-size:26px">forfait : 2 ou 3 restantes</div>
      <div class="rl"></div><div class="rl"></div><div class="rl"></div>
    </div>
    <div class="post hid" id="apo1" style="left:470px;top:470px;transform:rotate(6deg)">Sophie : lui envoyer le compte rendu</div>
    <div class="post hid" id="apo2" style="left:0;top:560px;transform:rotate(-7deg);background:#BFDBFE;color:#1E3A8A">Prochaine séance&nbsp;: ???</div>
    <div class="qmk hid" id="aqm" style="left:560px;top:120px">?</div>
  </div>
</div>'''
js += 'tl.fromTo("#anb",{rotation:-6},{rotation:-3,duration:1.6,ease:"power2.out"},0.1);\n'
js += pop("#apo1", 2.4) + pop("#apo2", 3.2)
js += "".join(pop(f"#aq{i}", t) for i, (_, t) in enumerate(qs))
js += pop("#aqm", 9.2, "back.out(3)") + 'tl.to("#aqm",{rotation:12,duration:.2,yoyo:true,repeat:3},9.7);\n'
js += pop("#ap0", 10.2) + pop("#ap1", 11.0) + pop("#ap2", 12.4)
js += 'tl.to(".qq",{borderColor:"#2563EB",duration:.3,stagger:.12},13.2);\n'

# ---------- T : titre en chemin de 5 étapes (15.4 -> 24.4)
steps = ["Une fiche<br/>par cliente", "Vos notes<br/>privées", "Le compte<br/>rendu", "Un cadre<br/>clair", "Bilan<br/>et avis"]
xs = [0, 400, 800, 1200, 1600]
ph = "".join(f'<div class="st5{" g" if i == 4 else ""} hid" id="tp{i}" style="left:{x}px">{i + 1}</div>'
             f'<div class="sl5 hid" id="tl{i}" style="left:{x}px">{s}</div>' for i, (s, x) in enumerate(zip(steps, xs)))
body += f'''
<div id="t" class="clip light" data-start="{T['t']}" data-duration="{round(T['s1'] - T['t'], 2)}" data-track-index="1">
  {LOGO}
  <div class="titleT hid" id="tt" style="top:140px"><div class="k">SOPHROLOGUES · HYPNOTHÉRAPEUTES · PRATICIENNES REIKI</div>
    <div class="b" style="font-size:84px">Le suivi de vos clientes<br/><span>sur plusieurs séances</span></div></div>
  <div class="path5"><div class="pl5 hid" id="tpl"></div>{ph}</div>
  <div class="gpbadge"><div class="hid" id="tgp">+ à chaque étape&nbsp;: comment faire dans {GPB}</div></div>
</div>'''
js += 'tl.fromTo("#tt",{opacity:0,y:40},{opacity:1,y:0,duration:.7,ease:"back.out(1.4)"},15.5);\n'
js += 'tl.fromTo("#tpl",{opacity:1,scaleX:0},{opacity:1,scaleX:1,duration:2.6,ease:"power1.inOut"},16.6);\n'
js += "".join(pop(f"#tp{i}", 16.6 + i * .6) + pop(f"#tl{i}", 16.75 + i * .6) for i in range(5))
js += pop("#tgp", 21.5)

# ---------- 1 : une fiche par cliente (24.4 -> 40.8)
h1, j1 = chap("s1", 1, "Une fiche par cliente", "Tout ce qui la concerne,<br/><span>au même endroit</span>", T['s1'])
evs = [("Rendez-vous passés et à venir", "4 séances · prochaine le 3 nov.", "", 29.8, 210),
       ("Règlements", "3 séances réglées", " g", 30.6, 330),
       ("Vos échanges", "messages au même endroit", " p", 31.5, 450)]
evh = "".join(f'<div class="ev hid" id="e{i}" style="top:{y}px"><div class="dt{c}"></div><div><div class="tx">{a}</div><div class="sm">{b}</div></div></div>'
              for i, (a, b, c, _, y) in enumerate(evs))
tabs = [("Rendez-vous", 37.0), ("Comptes rendus", 38.45), ("Factures", 39.3), ("Avis", 40.1)]
tbh = "".join(f'<div class="hid" id="tb{i}">{a}</div>' for i, (a, _) in enumerate(tabs))
body += f'''
<div id="s1" class="clip light" data-start="{T['s1']}" data-duration="{round(T['s2'] - T['s1'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px">{h1}
    {INSIDE.format(id="s1in")}
    <div class="ok hid" id="s1o1"><i>✓</i>Créée dès sa réservation en ligne</div></div>
  <div class="card hid" id="s1c"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="ch"><div class="av">SM</div><div><div class="nm">Sophie M.</div><div class="sb">Cliente depuis septembre</div></div></div>
    <div class="vline hid" id="s1v"></div>{evh}
    <div class="tabs">{tbh}</div></div>
</div>'''
js += j1 + fin("#s1c", 25.4) + 'tl.fromTo("#s1v",{opacity:1,scaleY:0},{opacity:1,scaleY:1,duration:2.2},29.6);\n'
js += "".join(pop(f"#e{i}", t, y=20) for i, (_, _, _, t, _) in enumerate(evs))
js += pop("#s1in", 32.4) + pop("#s1o1", 33.6)
js += "".join(pop(f"#tb{i}", t) for i, (_, t) in enumerate(tabs))

# ---------- 2 : vos notes après chaque séance (40.8 -> 58.3)
h2, j2 = chap("s2", 2, "Après chaque séance", "2 minutes,<br/><span>3 questions</span>", T['s2'])
nl = [("Ce que nous avons abordé", "« respiration, prise de parole en public »", 44.1),
      ("Ce qu'elle souhaite travailler ensuite", "« s'affirmer en réunion »", 45.3),
      ("À me rappeler la prochaine fois", "« préfère la séance en fin de journée »", 47.0)]
nlh = "".join(f'<div class="nl3 hid" id="n{i}"><b>{i + 1}</b><div>{a}<small>{b}</small></div></div>' for i, (a, b, _) in enumerate(nl))
body += f'''
<div id="s2" class="clip warm" data-start="{T['s2']}" data-duration="{round(T['s3'] - T['s2'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px">{h2}
    <div class="cons hid" id="s2k"><div class="l">POUR VOUS SEULE</div><div class="t">Des notes de travail,<br/>pas un document à partager.</div></div>
    {INSIDE.format(id="s2in")}
    <div class="ok hid" id="s2o1"><i>✓</i>Notes internes de la fiche</div></div>
  <div class="pad hid" id="s2p"><span class="illus" style="left:56px;bottom:6px">Illustration</span>
    <div class="timer hid" id="s2t">⏱ 2 min</div>
    <div class="tt">Sophie M. · séance du 13 oct.</div><div class="dd">Notes après la séance</div>{nlh}
    <div class="priv hid" id="s2v">{LOCK.format(s=46, c="#E9C46A")}<div>Notes internes<small>votre cliente ne les voit jamais</small></div></div></div>
</div>'''
js += j2 + fin("#s2p", 41.6) + pop("#s2t", 42.3)
js += "".join(pop(f"#n{i}", t) for i, (_, _, t) in enumerate(nl))
js += pop("#s2k", 50.4, E) + pop("#s2in", 51.8) + pop("#s2o1", 53.6)
js += 'tl.fromTo("#s2v",{opacity:0,y:40},{opacity:1,y:0,duration:.5,ease:"back.out(1.8)"},55.4);\n'

# ---------- 3a : notes privées / compte rendu partagé (58.3 -> 65.0)
body += f'''
<div id="s3" class="clip light" data-start="{T['s3']}" data-duration="{round(T['s3b'] - T['s3'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:125px"><div class="chap hid" id="s3c"><b>3</b>Le compte rendu</div>
    <div class="h hid" id="s3h" style="font-size:60px">Ce que vous notez <span>≠ ce que vous partagez</span></div></div>
  <div class="two l hid" id="s3l"><div class="lb">{LOCK.format(s=28, c="#E9C46A")}Vos notes</div>
    <div class="ttl">Pour vous, en vrac</div>
    <div class="row"><i></i>abréviations, pistes</div><div class="row"><i></i>impressions personnelles</div><div class="row"><i></i>rappels pratiques</div></div>
  <div class="two r hid" id="s3r"><div class="lb">✓ Compte rendu de séance</div>
    <div class="ttl">Pour elle, au propre</div>
    <div class="ln" style="width:95%"></div><div class="ln" style="width:88%"></div><div class="ln" style="width:72%"></div>
    <div class="row hid" id="s3x" style="margin-top:34px"><i></i>rédigé à part, relu</div></div>
</div>'''
js += pop("#s3c", 58.4, E) + pop("#s3h", 58.7, E, 40)
js += 'tl.fromTo("#s3l",{opacity:0,x:-60},{opacity:1,x:0,duration:.6,ease:"power3.out"},59.6);\n'
js += 'tl.fromTo("#s3r",{opacity:0,x:60},{opacity:1,x:0,duration:.6,ease:"power3.out"},60.6);\n'
js += 'tl.to("#s3l",{opacity:.5,duration:.4},62.2);\n' + pop("#s3x", 63.8)

# ---------- 3b : écrire ou vocal -> rendez-vous -> espace client (65.0 -> 75.5)
fl = [("Écrit", "rédigé à votre rythme", PEN, 66.2, "ou"), ("Vocal", "enregistré à votre voix", MIC, 67.5, ""),
      ("Relié au rendez-vous", "séance du 13 octobre", CAL, 68.9, ""), ("Livré dans son espace", "espace client sécurisé", USR, 70.3, "")]
flh = "".join(f'<div class="fs hid" id="f{i}"><div class="ic">{ic}</div><div><b>{a}</b><small>{b}</small></div>'
              + (f'<div class="or">{o}</div>' if o else "") + '</div>' for i, (a, b, ic, _, o) in enumerate(fl))
inner = ('<div class="phead">Mon espace</div>'
         '<div class="notif hid" id="s3n"><div class="ic"><img src="assets/favicon.png" alt="" /></div>'
         '<div><div class="a">Nouveau compte rendu</div><div class="b">Votre praticienne vous a écrit</div></div></div>'
         '<div class="cr hid" id="s3cr"><div class="a">Compte rendu · séance du 13 oct.</div><div class="b">Sophrologie · 1 h</div>'
         '<div class="nw">Nouveau</div></div>'
         '<div class="seen hid" id="s3s">✓ Consulté le 13 oct. à 19:42</div>')
body += f'''
<div id="s3b" class="clip light" data-start="{T['s3b']}" data-duration="{round(T['s4'] - T['s3b'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:110px"><div class="inside hid" id="s3bin" style="margin-top:0"><i></i>Dans GuidPilot</div>
    <div class="h hid" id="s3bh" style="font-size:56px;margin-top:20px">Rédigé ou enregistré, <span>puis livré</span></div></div>
  <div class="flow">{flh}</div>
  {phone("s3p", inner, 1300, 100)}
</div>'''
js += pop("#s3bin", 65.1) + pop("#s3bh", 65.4, E, 30) + "".join(pop(f"#f{i}", t) for i, (_, _, _, t, _) in enumerate(fl))
js += fin("#s3p", 70.6) + pop("#s3cr", 71.6, y=20)
js += 'tl.fromTo("#s3n",{opacity:0,y:60},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},73.2);\n'
js += pop("#s3s", 74.2, y=20) + 'tl.to("#f3",{borderColor:"#2563EB",duration:.3},74.2);\n'

# ---------- 4 : un cadre clair (75.5 -> 94.4)
h4, j4 = chap("s4", 4, "Un cadre clair", "Un forfait,<br/><span>et la date suivante</span>", T['s4'])
dots = "".join(f'<div id="d{i}"{" class=on" if i < 3 else ""}>{i + 1}</div>' for i in range(5))
body += f'''
<div id="s4" class="clip light" data-start="{T['s4']}" data-duration="{round(T['s5'] - T['s4'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:760px">{h4}
    {INSIDE.format(id="s4in")}
    <div class="ok hid" id="s4o1"><i>✓</i>Une séance décomptée à chaque fois</div>
    <div class="ok hid" id="s4o2"><i>✓</i>Elle voit ce qu'il lui reste</div>
    <div class="ok hid" id="s4o3"><i>✓</i>Elle reprend rendez-vous elle-même</div></div>
  <div class="fk hid" id="s4f"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="k">FORFAIT</div><div class="a">5 séances de sophrologie</div><div class="b">Sophie M. · valable 6 mois</div>
    <div class="dots">{dots}</div>
    <div class="left hid" id="s4l"><span>Séances restantes</span><b id="s4n">2</b></div></div>
  <div class="nxt"><div class="hid" id="s4d"><small>Avant qu'elle reparte</small>Prochaine séance : mardi 3&nbsp;nov.</div>
    <div class="bl hid" id="s4b"><small>Depuis son espace</small>Prendre un nouveau rendez-vous</div></div>
</div>'''
js += j4 + fin("#s4f", 78.0) + pop("#s4d", 80.5)
js += pop("#s4in", 83.0) + pop("#s4l", 84.6)
js += 'tl.to("#d3",{backgroundColor:"#2563EB",borderColor:"#2563EB",color:"#FFFFFF",duration:.4},86.4);\n'
js += 'tl.fromTo("#d3",{scale:1},{scale:1.15,duration:.2,yoyo:true,repeat:1},86.4);\n'
js += 'tl.to("#s4n",{opacity:0,duration:.15},86.6);\n' + 'tl.set("#s4n",{textContent:"1"},86.75);\n' + 'tl.to("#s4n",{opacity:1,duration:.2},86.8);\n'
js += pop("#s4o1", 86.4) + pop("#s4o2", 88.6) + 'tl.to("#s4l",{borderColor:"#2563EB",duration:.3},89.0);\n'
js += pop("#s4o3", 92.4) + pop("#s4b", 92.6) + 'tl.to("#s4b",{scale:.95,duration:.15,yoyo:true,repeat:1},93.6);\n'

# ---------- 5a : faire le point (94.4 -> 103.4)
h5, j5 = chap("s5", 5, "Fin du cycle", "Faites le point,<br/><span>ensemble</span>", T['s5'])
body += f'''
<div id="s5" class="clip warm" data-start="{T['s5']}" data-duration="{round(T['s5b'] - T['s5'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:760px">{h5}
    <div class="soft hid" id="s5s" style="align-self:flex-start;margin-top:36px">Sans jamais forcer</div></div>
  <div class="bq"><span class="illus" style="right:0;top:-50px">Illustration</span>
    <div class="bub me hid" id="s5q0" style="right:0">Que retenez-vous de ces séances&nbsp;?</div>
    <div class="bub me hid" id="s5q1" style="right:0">Quelle suite souhaitez-vous&nbsp;?</div>
    <div class="bub her hid" id="s5q2">Je voudrais continuer une fois par mois.</div></div>
</div>'''
js += j5 + pop("#s5q0", 97.9, y=20) + pop("#s5q1", 100.9, y=20) + pop("#s5s", 102.6) + pop("#s5q2", 102.0, y=20)

# ---------- 5b : demander son avis (103.4 -> 110.45)
avl = [("Un lien d'avis personnel", 106.9), ("Publié : il s'affiche sur votre page", 108.4)]
avh = "".join(f'<div class="hid" id="av{i}"><i>✓</i>{a}</div>' for i, (a, _) in enumerate(avl))
body += f'''
<div id="s5b" class="clip light" data-start="{T['s5b']}" data-duration="{round(T['r'] - T['s5b'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:700px"><div class="chap" style="color:#2563EB"><b>5</b>Puis</div>
    <div class="h hid" id="s5bh">Demandez-lui<br/><span>son avis</span></div>
    {INSIDE.format(id="s5bin")}</div>
  <div class="af hid" id="s5f"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>
    <span class="demo">Compte de démonstration</span></div><img src="assets/avis.png" alt="" />
    <div class="ring2 hid" id="s5r"></div></div>
  <div class="avl">{avh}</div>
</div>'''
js += pop("#s5bh", 103.5, E, 40) + fin("#s5f", 104.2) + pop("#s5bin", 105.0)
js += "".join(pop(f"#av{i}", t) for i, (_, t) in enumerate(avl))
js += 'tl.fromTo("#s5r",{opacity:0,scale:1.3},{opacity:1,scale:1,duration:.5,ease:"back.out(1.6)"},108.6);\n'

# ---------- récap en 3 points (110.45 -> 116.85)
rc = [("Une fiche<br/><span>par cliente</span>", 111.4, ""), ("Des notes privées,<br/><span>à part du compte rendu</span>", 112.6, " g"),
      ("Un cadre clair<br/><span>pour la suite</span>", 115.1, "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += f'''
<div id="r" class="clip light" data-start="{T['r']}" data-duration="{round(T['g'] - T['r'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>
</div>'''
js += pop("#rk", 110.55, E) + "".join(pop(f"#rc{i}", t, y=50) for i, (_, t, _) in enumerate(rc))

# ---------- GuidPilot (116.85 -> 124.8)
gc = [("Fiches clientes", 117.0), ("Notes privées", 118.0), ("Comptes rendus", 119.0), ("Forfaits", 119.7), ("Avis", 120.3)]
gch = "".join(f'<div class="hid" id="gc{i}">{a}</div>' for i, (a, _) in enumerate(gc))
body += f'''
<div id="g" class="clip light" data-start="{T['g']}" data-duration="{round(T['end'] - T['g'], 2)}" data-track-index="1">
  <div class="gpl"><img class="hid" id="gl" src="assets/logo_couleur.png" alt="GuidPilot" />
    <div class="b hid" id="gb">Tout le suivi de votre cabinet,<br/><span>dans un seul espace</span></div></div>
  <div class="gch">{gch}</div>
</div>'''
js += 'tl.fromTo("#gl",{opacity:0,scale:.92},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},116.95);\n'
js += "".join(pop(f"#gc{i}", t) for i, (_, t) in enumerate(gc)) + pop("#gb", 121.0, E, 40)

# ---------- fin marine (124.8 -> DUR)
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
js += 'tl.fromTo("#z6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},124.9);\n'
js += pop("#z7", 127.4) + pop("#z8", 128.6) + pop("#z9", 130.6)
js += 'tl.to("#z9",{scale:1.06,duration:.45,yoyo:true,repeat:3,ease:"sine.inOut"},131.4);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA4}</style></head><body>
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

d = ATELIER / "build" / "yt-suivi-therapeutes"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "avis.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
