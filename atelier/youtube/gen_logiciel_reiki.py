"""Vidéo YouTube 1920x1080 : « Logiciel pour praticienne Reiki : réservation, paiement et suivi des séances »
(série « Pensé pour votre métier » · public thérapeutes, mardi 27/10/2026).
Usage : python3 gen_logiciel_reiki.py <voix.wav>  -> build/yt-logiciel-reiki/
Voix : 9 paragraphes générés un par un (voix/2026-10-27_yt-reiki-p1..p9.mp3), assemblés dans l'ordre 1,2,4,3,5,6,7,8,9
(CTA oral d'abonnement après la 1re question, ~29 % de la vidéo) ; temps des phrases = silencedetect + syllabes par paragraphe.
Structure « 5 questions à vous poser » : chaque question = carte question plein écran (fond qui change de couleur) →
conseil illustré → « Dans GuidPilot ». Aucune personne représentée, aucun prix GuidPilot, aucun superlatif,
aucun vocabulaire médical, aucune promesse sur les effets du Reiki.
Réutilise CSS et helpers de gen_therapeutes_soir.py (+ EXTRA4 de gen_suivi_therapeutes.py).
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_therapeutes_soir.py").read_text()
ns = {"__file__": str(HERE / "gen_therapeutes_soir.py")}
exec(src.split("# ---------- A :")[0], ns)
CSS, EXTRA, ATELIER, KIT = ns["CSS"], ns["EXTRA"], ns["ATELIER"], ns["KIT"]
pop, fin, out, chap, phone, LOGO, E = (ns[k] for k in ("pop", "fin", "out", "chap", "phone", "LOGO", "E"))
EXTRA4 = (HERE / "gen_suivi_therapeutes.py").read_text().split('EXTRA4 = """')[1].split('"""')[0]

DUR = 159.8
LOGOW = '<img class="logo-corner" src="assets/logo_blanc.png" alt="GuidPilot" />'

EXTRA5 = """
.cream{background:#F8F4EC}.blue{background:#1D4ED8;color:#fff}
.hook{position:absolute;left:110px;top:150px;width:1700px}
.hook .a{font-weight:800;font-size:104px;line-height:1.04;letter-spacing:-.035em;color:#fff}
.hook .a span{color:#E9C46A}
.tline{position:absolute;left:110px;top:560px;width:1700px;height:360px}
.tbar{position:absolute;left:0;right:0;top:120px;height:12px;border-radius:6px;background:#334155;transform-origin:left center}
.tmid{position:absolute;left:700px;top:60px;width:300px;height:132px;border-radius:28px;background:#E9C46A;color:#0F172A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:54px}
.tside{position:absolute;top:0;width:640px}
.tside .l{font-weight:800;font-size:34px;letter-spacing:.14em;color:#93C5FD}
.tside .cs{display:flex;flex-wrap:wrap;gap:14px;margin-top:150px}
.tside .cs div{padding:14px 26px;border-radius:999px;background:#1E293B;border:2px solid #475569;font-weight:700;font-size:30px;color:#F1F5F9}
.qz{position:absolute;left:150px;top:0;bottom:0;width:1620px;display:flex;flex-direction:column;justify-content:center}
.qz .n{display:inline-flex;align-items:center;gap:22px;font-weight:800;font-size:34px;letter-spacing:.14em;text-transform:uppercase}
.qz .n b{display:inline-flex;width:84px;height:84px;border-radius:50%;align-items:center;justify-content:center;font-size:44px;letter-spacing:0}
.qz .q{font-weight:800;font-size:104px;line-height:1.06;letter-spacing:-.035em;margin-top:40px}
.qz .s{display:flex;gap:18px;margin-top:50px}
.qz .s div{padding:16px 32px;border-radius:999px;font-weight:700;font-size:32px}
.qz .bar5{display:flex;gap:12px;margin-top:70px}
.qz .bar5 i{display:block;width:120px;height:12px;border-radius:6px;opacity:.25}
.qz .bar5 i.on{opacity:1}
.cream .qz .n{color:#B7791F}.cream .qz .n b{background:#0F172A;color:#E9C46A}.cream .qz .q{color:#0F172A}.cream .qz .q span{color:#2563EB}
.cream .qz .s div{background:#fff;border:2px solid #E7DFC9;color:#0F172A}.cream .qz .bar5 i{background:#0F172A}
.navy .qz .n{color:#93C5FD}.navy .qz .n b{background:#E9C46A;color:#0F172A}.navy .qz .q{color:#fff}.navy .qz .q span{color:#E9C46A}
.navy .qz .s div{background:#1E293B;border:2px solid #475569;color:#F1F5F9}.navy .qz .bar5 i{background:#E9C46A}
.blue .qz .n{color:#BFDBFE}.blue .qz .n b{background:#fff;color:#1D4ED8}.blue .qz .q{color:#fff}.blue .qz .q span{color:#FDE68A}
.blue .qz .s div{background:rgba(255,255,255,.14);border:2px solid rgba(255,255,255,.35);color:#fff}.blue .qz .bar5 i{background:#fff}
.t5{position:absolute;left:0;right:0;top:470px;display:flex;justify-content:center;gap:26px}
.t5 div{width:300px;height:300px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.08);padding:30px;display:flex;flex-direction:column;justify-content:space-between}
.t5 b{display:flex;width:70px;height:70px;border-radius:50%;background:#0F172A;color:#E9C46A;align-items:center;justify-content:center;font-size:36px;font-weight:800}
.t5 span{font-weight:800;font-size:33px;line-height:1.18;color:#0F172A}
.pres{position:absolute;top:330px;width:780px;height:560px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.1);padding:46px 50px}
.pres .ic{width:96px;height:96px;border-radius:26px;display:flex;align-items:center;justify-content:center}
.pres .tt{font-weight:800;font-size:50px;color:#0F172A;margin-top:30px;line-height:1.1}
.pres .row{display:flex;align-items:center;gap:18px;margin-top:26px;font-weight:700;font-size:32px;color:#334155}
.pres .row i{font-style:normal;flex:none;width:48px;height:48px;border-radius:14px;background:#EFF6FF;color:#2563EB;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:800}
.pres .hl{position:absolute;left:30px;right:30px;border:5px solid #E9C46A;border-radius:20px;height:76px}
.cal{position:absolute;left:880px;top:200px;width:940px;height:760px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.cal .ct{height:110px;padding:0 40px;display:flex;align-items:center;justify-content:space-between;border-bottom:2px solid #E2E8F0;font-weight:800;font-size:36px;color:#0F172A}
.cal .ct small{font-weight:600;font-size:24px;color:#64748B}
.cal .hr{position:absolute;left:40px;right:40px;height:2px;background:#F1F5F9}
.cal .hl2{position:absolute;left:40px;font-weight:700;font-size:22px;color:#94A3B8}
.cal .evt{position:absolute;left:150px;right:40px;border-radius:18px;padding:18px 24px;font-weight:800;font-size:28px}
.cal .evt small{display:block;font-weight:600;font-size:22px;margin-top:4px}
.evt.a{background:#EFF6FF;border-left:10px solid #2563EB;color:#1E3A8A}
.evt.b{background:#FBF3DC;border-left:10px solid #E9C46A;color:#6B4E16}
.evt.n{background:#DCFCE7;border-left:10px solid #16A34A;color:#14532D}
.newb{position:absolute;right:30px;top:24px;padding:6px 16px;border-radius:999px;background:#16A34A;color:#fff;font-weight:800;font-size:20px}
.chain{position:absolute;left:110px;top:380px;width:700px}
.chain .st{display:flex;align-items:center;gap:22px;margin-bottom:22px;padding:22px 28px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07);font-weight:800;font-size:34px;color:#0F172A}
.chain .st b{flex:none;width:58px;height:58px;border-radius:50%;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px}
.ctaC{position:absolute;left:0;right:0;top:200px;text-align:center}
.ctaC .k{font-weight:700;font-size:30px;letter-spacing:.14em;color:#93C5FD}
.ctaC .b{font-weight:800;font-size:92px;line-height:1.08;letter-spacing:-.03em;color:#fff;margin-top:26px}
.ctaC .b span{color:#E9C46A}
.ytb{display:inline-flex;align-items:center;gap:22px;margin-top:60px;padding:26px 54px;border-radius:999px;background:#DC2626;color:#fff;font-weight:800;font-size:46px}
.ytb i{font-style:normal;display:inline-block;width:0;height:0;border-left:30px solid #fff;border-top:18px solid transparent;border-bottom:18px solid transparent}
.dsc{position:absolute;left:460px;right:460px;top:800px;padding:26px 36px;border-radius:24px;background:#1E293B;border:2px solid #475569;display:flex;align-items:center;gap:22px;font-weight:700;font-size:32px;color:#E2E8F0}
.dsc b{color:#93C5FD}
.vs2{position:absolute;top:300px;width:800px;height:420px;border-radius:30px;padding:46px;display:flex;flex-direction:column}
.vs2 .t{font-weight:800;font-size:56px;line-height:1.1}
.vs2 .d{font-weight:600;font-size:30px;margin-top:16px;line-height:1.35}
.vs2 .ok2{margin-top:auto;display:inline-flex;align-self:flex-start;align-items:center;gap:14px;padding:12px 24px;border-radius:999px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:28px}
.both{position:absolute;left:0;right:0;top:925px;text-align:center}
.both div{display:inline-block;padding:20px 44px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:40px}
.both div span{color:#E9C46A}
.rules{position:absolute;left:900px;top:170px;width:920px;padding:46px 50px;border-radius:30px;background:#FFFDF7;border:2px solid #E7DFC9;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.rules .tt{font-weight:800;font-size:42px;color:#0F172A}
.rules .ex{display:inline-block;margin-left:16px;padding:4px 14px;border-radius:999px;background:#F1F5F9;color:#64748B;font-weight:700;font-size:20px;vertical-align:middle}
.rules .r{display:flex;gap:20px;margin-top:30px;font-weight:700;font-size:32px;line-height:1.3;color:#334155}
.rules .r i{font-style:normal;flex:none;width:52px;height:52px;border-radius:50%;background:#0F172A;color:#E9C46A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px}
.rules .seen2{margin-top:40px;padding:22px 28px;border-radius:20px;background:#EFF6FF;border:2px solid #BFDBFE;font-weight:800;font-size:30px;color:#1D4ED8}
.pay{position:absolute;left:110px;top:330px;width:760px}
.pay .p{display:flex;align-items:center;gap:22px;margin-bottom:24px;padding:26px 30px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07)}
.pay .p .ic{flex:none;width:72px;height:72px;border-radius:20px;background:#EFF6FF;display:flex;align-items:center;justify-content:center;font-size:34px}
.pay .p b{display:block;font-weight:800;font-size:34px;color:#0F172A}
.pay .p small{display:block;font-weight:600;font-size:24px;color:#64748B;margin-top:4px}
.inv{position:absolute;left:1000px;top:160px;width:620px;height:560px;border-radius:16px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.12);padding:44px 50px}
.inv .h1{font-weight:800;font-size:42px;color:#0F172A}
.inv .no{display:inline-block;margin-top:12px;padding:8px 18px;border-radius:10px;background:#EFF6FF;color:#1D4ED8;font-weight:800;font-size:28px}
.inv .li2{display:flex;justify-content:space-between;margin-top:34px;font-weight:700;font-size:28px;color:#334155}
.inv .ln{height:14px;border-radius:7px;background:#E2E8F0;margin-top:24px}
.finf{position:absolute;left:880px;top:770px;width:940px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.finf img{display:block;width:940px}
.night{position:absolute;left:110px;top:300px;width:760px}
.clk{font-weight:800;font-size:200px;line-height:1;letter-spacing:-.04em;color:#fff}
.clk span{color:#E9C46A}
.night .d{font-weight:600;font-size:40px;color:#CBD5E1;margin-top:20px}
.todo{display:inline-flex;align-items:center;gap:16px;margin-top:40px;padding:20px 32px;border-radius:999px;background:#7F1D1D;color:#FECACA;font-weight:800;font-size:36px}
.typing{position:absolute;left:24px;right:24px;top:400px}
.mail{position:absolute;left:14px;right:14px;top:150px;padding:18px 20px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 30px rgba(15,23,42,.12)}
.mail .a{font-weight:800;font-size:22px;color:#0F172A}.mail .b{font-weight:600;font-size:19px;color:#64748B;margin-top:4px}
.rdv{margin:24px 22px 0;padding:24px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 10px 30px rgba(15,23,42,.06)}
.rdv .a{font-weight:800;font-size:28px;color:#0F172A}.rdv .b{font-weight:600;font-size:21px;color:#64748B;margin-top:6px}
.meet{margin-top:18px;height:70px;border-radius:16px;background:#2563EB;color:#fff;font-weight:800;font-size:25px;display:flex;align-items:center;justify-content:center;gap:12px}
.thread{position:absolute;left:0;right:0;top:130px;bottom:0;overflow:hidden}
.thread .bub{position:relative;display:table;max-width:320px;margin:14px 22px;font-size:24px;padding:14px 20px}
.thread .bub.me{margin-left:auto}
.thread .bub.cr{background:#E9C46A;color:#0F172A;font-weight:800}
.lost{position:absolute;left:1440px;top:420px;width:380px;padding:30px;border-radius:26px;background:#FEF2F2;border:2px solid #FECACA;text-align:center;font-weight:800;font-size:36px;color:#B91C1C;line-height:1.25}
.box2{position:absolute;left:1440px;top:420px;width:380px;padding:30px;border-radius:26px;background:#DCFCE7;border:2px solid #86EFAC;text-align:center;font-weight:800;font-size:36px;color:#15803D;line-height:1.25}
.locks{position:absolute;left:110px;top:640px;width:760px;display:flex;align-items:center;gap:24px;padding:28px 34px;border-radius:26px;background:#0F172A;color:#fff;font-weight:800;font-size:36px}
.locks small{display:block;font-weight:600;font-size:24px;color:#CBD5E1;margin-top:4px}
.audio{display:flex;align-items:center;gap:16px;margin-top:16px;padding:14px 18px;border-radius:16px;background:#EFF6FF}
.audio b{flex:none;width:44px;height:44px;border-radius:50%;background:#2563EB;display:flex;align-items:center;justify-content:center}
.audio b i{display:block;width:0;height:0;border-left:14px solid #fff;border-top:9px solid transparent;border-bottom:9px solid transparent;margin-left:4px}
.audio span{flex:1;height:30px;background:repeating-linear-gradient(90deg,#93C5FD 0 5px,transparent 5px 10px);border-radius:4px}
.stars{display:flex;gap:16px;margin-top:30px}
.stars i{font-style:normal;font-size:70px;color:#CBD5E1}
.avf{position:absolute;left:880px;top:200px;width:940px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.avf img{display:block;width:940px}
.ring4{position:absolute;left:236px;top:156px;width:226px;height:122px;border:6px solid #E9C46A;border-radius:22px}
.fk2{position:absolute;left:880px;top:610px;width:940px;padding:30px 40px;border-radius:26px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.1);display:flex;align-items:center;gap:30px}
.fk2 .a{font-weight:800;font-size:34px;color:#0F172A}.fk2 .b{font-weight:600;font-size:24px;color:#64748B;margin-top:4px}
.fk2 .n2{margin-left:auto;font-weight:800;font-size:64px;color:#2563EB}
.fk2 .n2 small{font-size:24px;color:#64748B;font-weight:700}
"""

CAL = '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'
HOME = '<svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#B7791F" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>'
CAM = '<svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="14" height="12" rx="3"/><path d="M16 10l6-3v10l-6-3"/></svg>'
LOCK = ('<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round">'
        '<rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>')
INSIDE = '<div class="inside hid" id="{id}"><i></i>Dans GuidPilot</div>'
body, js = "", ""


def qcard(id_, start, end, num, q, tags, cls, tag_times, logo=LOGOW):
    bars = "".join(f'<i{" class=on" if i < num else ""}></i>' for i in range(5))
    tg = "".join(f'<div class="hid" id="{id_}g{i}">{t}</div>' for i, t in enumerate(tags))
    h = f'''
<div id="{id_}" class="clip {cls}" data-start="{start}" data-duration="{round(end - start, 2)}" data-track-index="1">
  {logo}
  <div class="qz"><div class="n hid" id="{id_}n"><b>{num}</b>Question {num} sur 5</div>
    <div class="q hid" id="{id_}q">{q}</div><div class="s">{tg}</div><div class="bar5">{bars}</div></div>
</div>'''
    j = pop(f"#{id_}n", start + .05, E) + pop(f"#{id_}q", start + .2, E, 50)
    j += "".join(pop(f"#{id_}g{i}", t) for i, t in enumerate(tag_times))
    return h, j


# ---------- A : accroche (0 -> 12.7) — lisible dès l'image 0
av = [("Réservation", 5.35), ("Paiement", 6.37), ("Lieu", 7.11)]
ap = [("Compte rendu", 9.48), ("Séance suivante", 10.47), ("Avis", 11.64)]
avh = "".join(f'<div class="hid" id="av{i}">{a}</div>' for i, (a, _) in enumerate(av))
aph = "".join(f'<div class="hid" id="ap{i}">{a}</div>' for i, (a, _) in enumerate(ap))
body += f'''
<div id="a" class="clip navy" data-start="0" data-duration="12.7" data-track-index="1">
  {LOGOW}
  <div class="hook"><div class="a">Une séance de Reiki,<br/><span id="ah2">ce n'est jamais qu'une heure.</span></div></div>
  <div class="tline"><div class="tbar hid" id="atb"></div>
    <div class="tside" style="left:0"><div class="l hid" id="al1">AVANT</div><div class="cs">{avh}</div></div>
    <div class="tmid hid" id="atm">1 h</div>
    <div class="tside" style="left:1060px"><div class="l hid" id="al2">APRÈS</div><div class="cs">{aph}</div></div></div>
</div>'''
js += 'tl.fromTo("#ah2",{opacity:.25},{opacity:1,duration:.5},2.9);\n'
js += 'tl.fromTo("#atb",{opacity:1,scaleX:0},{opacity:1,scaleX:1,duration:1.4,ease:"power2.inOut"},3.6);\n'
js += pop("#atm", 3.9, "back.out(2)") + pop("#al1", 4.55, E)
js += "".join(pop(f"#av{i}", t) for i, (_, t) in enumerate(av))
js += pop("#al2", 8.3, E) + "".join(pop(f"#ap{i}", t) for i, (_, t) in enumerate(ap))

# ---------- T : 5 questions (12.7 -> 21.45)
qt = ["Réserver<br/>seule", "Le moment<br/>du paiement", "Le lien<br/>à distance", "Le compte<br/>rendu", "Le suivi<br/>en plusieurs séances"]
qth = "".join(f'<div class="hid" id="tq{i}"><b>{i + 1}</b><span>{t}</span></div>' for i, t in enumerate(qt))
body += f'''
<div id="t" class="clip light" data-start="12.7" data-duration="8.75" data-track-index="1">
  {LOGO}
  <div class="titleT" style="top:130px"><div class="k hid" id="tk">PRATICIENNE REIKI · LAHOCHI</div>
    <div class="b hid" id="tb" style="font-size:88px">5 questions à vous poser<br/><span>sur votre organisation</span></div></div>
  <div class="t5">{qth}</div>
  <div class="gpbadge" style="top:840px"><div class="hid" id="tgp">À la fin&nbsp;: ce que votre outil doit gérer à votre place</div></div>
</div>'''
js += pop("#tk", 12.8, E) + pop("#tb", 13.95, E, 40)
js += "".join(pop(f"#tq{i}", 14.6 + i * .35, y=50) for i in range(5)) + pop("#tgp", 16.4)

# ---------- Q1 carte (21.45 -> 26.15)
h, j = qcard("q1", 21.45, 26.15, 1, "Vos clientes peuvent-elles<br/><span>réserver seules&nbsp;?</span>",
             ["Au cabinet", "À distance"], "cream", [24.5, 25.0], LOGO)
body += h; js += j

# ---------- Q1 conseil : 2 prestations (26.15 -> 39.95)
body += f'''
<div id="q1b" class="clip light" data-start="26.15" data-duration="13.8" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="q1bc"><b>1</b>Le conseil</div>
    <div class="h hid" id="q1bh" style="font-size:58px">Deux séances, <span>deux prestations distinctes</span></div></div>
  <div class="pres hid" id="q1p1" style="left:110px"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="ic" style="background:#FBF3DC">{HOME}</div><div class="tt">Séance de Reiki<br/>au cabinet</div>
    <div class="row hid" id="q1r1"><i>⏱</i>Durée : 1 h</div><div class="row hid" id="q1r2"><i>✓</i>Déroulé : accueil, séance, échange</div>
    <div class="row hid" id="q1r3"><i>⌂</i>Adresse du cabinet</div></div>
  <div class="pres hid" id="q1p2" style="left:1030px"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="ic" style="background:#EFF6FF">{CAM}</div><div class="tt">Séance de Reiki<br/>à distance</div>
    <div class="row hid" id="q1r4"><i>⏱</i>Durée : 45 min</div><div class="row hid" id="q1r5"><i>✓</i>Déroulé : appel, séance, échange</div>
    <div class="row hid" id="q1r6"><i>▶</i>En visio</div></div>
  <div class="both"><div class="hid" id="q1x">Elle choisit <span>sans vous écrire</span>, vous savez où se passe la séance</div></div>
</div>'''
js += pop("#q1bc", 26.2, E) + pop("#q1bh", 26.4, E, 40)
js += fin("#q1p1", 27.4, -120) + fin("#q1p2", 28.6)
js += pop("#q1r1", 33.0) + pop("#q1r4", 33.3) + pop("#q1r2", 33.9) + pop("#q1r5", 34.2) + pop("#q1r3", 37.4) + pop("#q1r6", 37.7)
js += pop("#q1x", 35.0, E)

# ---------- Q1 Dans GuidPilot (39.95 -> 46.6)
st = [("Votre page publique", 40.85), ("La cliente choisit son créneau", 42.0), ("Le rendez-vous arrive dans l'agenda", 43.6)]
sth = "".join(f'<div class="st hid" id="q1s{i}"><b>{i + 1}</b>{a}</div>' for i, (a, _) in enumerate(st))
hours = "".join(f'<div class="hr" style="top:{150 + i * 120}px"></div><div class="hl2" style="top:{162 + i * 120}px">{h}</div>' for i, h in enumerate(["9 h", "10 h", "11 h", "14 h", "15 h"]))
body += f'''
<div id="q1c" class="clip light" data-start="39.95" data-duration="6.65" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:150px">{INSIDE.format(id="q1in")}
    <div class="h hid" id="q1ch" style="font-size:56px;margin-top:20px">De la page <span>à l'agenda</span></div></div>
  <div class="chain">{sth}</div>
  <div class="cal hid" id="q1cal"><span class="illus" style="left:40px;bottom:20px">Illustration</span>
    <div class="ct">Mardi 3 novembre<small>Agenda</small></div>{hours}
    <div class="evt a" style="top:150px;height:100px">Reiki · cabinet<small>9 h – 10 h · Léa M.</small></div>
    <div class="evt n hid" id="q1ev" style="top:390px;height:100px">Reiki · à distance<small>11 h – 11 h 45 · réservé en ligne</small><span class="newb">Nouveau</span></div></div>
</div>'''
js += pop("#q1in", 40.0) + pop("#q1ch", 40.3, E, 30) + fin("#q1cal", 40.6)
js += "".join(pop(f"#q1s{i}", t) for i, (_, t) in enumerate(st))
js += 'tl.fromTo("#q1ev",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.5,ease:"back.out(1.8)"},43.9);\n'

# ---------- CTA oral abonnement (46.6 -> 54.85)
body += f'''
<div id="cta" class="clip navy" data-start="46.6" data-duration="8.25" data-track-index="1">
  {LOGOW}
  <div class="ctaC"><div class="k hid" id="ck">CES CONSEILS VOUS SONT UTILES&nbsp;?</div>
    <div class="b hid" id="cb">2 vidéos par semaine<br/><span>pour organiser votre cabinet</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="dsc hid" id="cd">↓ <span><b>Essai gratuit&nbsp;:</b> le lien est dans la description</span></div>
</div>'''
js += pop("#ck", 46.7, E) + pop("#cb", 49.1, E, 40) + pop("#cy", 48.3, "back.out(2)")
js += 'tl.to("#cy",{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"},49.6);\n' + pop("#cd", 51.7)

# ---------- Q2 carte (54.85 -> 59.4)
h, j = qcard("q2", 54.85, 59.4, 2, "Quand le paiement<br/><span>arrive-t-il&nbsp;?</span>", ["En ligne, avant", "Au cabinet"], "navy", [57.25, 58.6])
body += h; js += j

# ---------- Q2 conseil (59.4 -> 68.1)
rl = [("Paiement", "en ligne à la réservation, ou au cabinet le jour J", 61.2), ("Annulation", "gratuite jusqu'à 24 h avant la séance", 62.5),
      ("Report", "possible une fois, en prévenant", 64.1)]
rlh = "".join(f'<div class="r hid" id="q2r{i}"><i>{i + 1}</i><div><b style="color:#0F172A">{a}&nbsp;:</b> {b}</div></div>' for i, (a, b, _) in enumerate(rl))
body += f'''
<div id="q2b" class="clip warm" data-start="59.4" data-duration="8.7" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px"><div class="chap hid" id="q2bc"><b>2</b>Le conseil</div>
    <div class="h hid" id="q2bh">Les deux se défendent.<br/><span>Écrivez-le avant.</span></div>
    <div class="ok hid" id="q2o1"><i>✓</i>Personne n'est surpris</div>
    <div class="ok hid" id="q2o2"><i>✓</i>Vous n'avez plus à réclamer</div></div>
  <div class="rules hid" id="q2ru"><div class="tt">Mes conditions<span class="ex">Exemple</span></div>{rlh}
    <div class="seen2 hid" id="q2s">Affichées avant la réservation</div></div>
</div>'''
js += pop("#q2bc", 59.45, E) + pop("#q2bh", 59.6, E, 40) + fin("#q2ru", 60.4)
js += "".join(pop(f"#q2r{i}", t) for i, (_, _, t) in enumerate(rl)) + pop("#q2s", 64.3)
js += pop("#q2o1", 65.4) + pop("#q2o2", 66.6)

# ---------- Q2 Dans GuidPilot (68.1 -> 75.45)
body += f'''
<div id="q2c" class="clip light" data-start="68.1" data-duration="7.35" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:150px">{INSIDE.format(id="q2in")}
    <div class="h hid" id="q2ch" style="font-size:56px;margin-top:20px">Payé, <span>puis facturé</span></div></div>
  <div class="pay"><div class="p hid" id="q2p1"><div class="ic">💳</div><div><b>En ligne, en réservant</b><small>carte ou PayPal</small></div></div>
    <div class="p hid" id="q2p2"><div class="ic">🏠</div><div><b>Au cabinet</b><small>chèque, espèces ou carte : enregistré en un clic</small></div></div></div>
  <div class="inv hid" id="q2inv"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="h1">Facture</div><div class="no">N° 2026-0042</div>
    <div class="li2"><span>Séance de Reiki · cabinet</span><span>1 h</span></div><div class="ln"></div><div class="ln" style="width:70%"></div>
    <div class="stamp hid" id="q2st" style="top:300px">PAYÉE</div></div>
  <div class="finf hid" id="q2fin" style="left:880px;top:780px;width:940px"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>
    <span class="demo">Compte de démonstration</span></div><img src="assets/finance.png" alt="" /></div>
</div>'''
js += pop("#q2in", 68.15) + pop("#q2ch", 68.4, E, 30) + pop("#q2p1", 69.0) + pop("#q2p2", 71.1)
js += fin("#q2inv", 73.3) + 'tl.fromTo("#q2st",{opacity:0,scale:1.6},{opacity:1,scale:1,duration:.35,ease:"back.out(2)"},74.0);\n'
js += pop("#q2fin", 73.6, y=40)

# ---------- Q3 carte (75.45 -> 79.05)
h, j = qcard("q3", 75.45, 79.05, 3, "Séance à distance&nbsp;:<br/><span>qui envoie le lien&nbsp;?</span>", ["Visio"], "blue", [77.2])
body += h; js += j

# ---------- Q3 conseil : la veille au soir (79.05 -> 83.05)
inner3 = ('<div class="phead"><div class="av">LM</div>Léa M.</div>'
          '<div class="typing"><div class="bub me hid" id="q3m1" style="position:relative;display:table;margin-left:auto;right:0">Bonsoir, voici le lien pour demain 11 h…</div></div>')
body += f'''
<div id="q3b" class="clip eve" data-start="79.05" data-duration="4.0" data-track-index="1">
  {LOGOW}
  <div class="night"><div class="clk hid" id="q3k">21<span>:</span>47</div><div class="d hid" id="q3d">La veille, à la main, pour chaque séance</div>
    <div class="todo hid" id="q3t">✕ Une tâche de trop</div></div>
  {phone("q3p", inner3, 1240, 100)}
</div>'''
js += pop("#q3k", 79.1, E) + pop("#q3d", 80.6, E) + fin("#q3p", 79.6) + pop("#q3m1", 80.2, y=20) + pop("#q3t", 81.7, "back.out(2)")

# ---------- Q3 Dans GuidPilot (83.05 -> 91.2)
inner3b = ('<div class="phead">Mon espace</div>'
           '<div class="mail hid" id="q3ml"><div class="a">✉ Rappel : votre séance demain à 11 h</div><div class="b">Reiki à distance · lien de visio inclus</div></div>'
           '<div class="rdv"><div class="a">Reiki à distance</div><div class="b">Mardi 3 nov. · 11 h – 11 h 45</div>'
           f'<div class="meet hid" id="q3mt">{CAM.replace("#2563EB", "#FFFFFF").replace("52", "34")}Rejoindre Google Meet</div></div>')
body += f'''
<div id="q3c" class="clip light" data-start="83.05" data-duration="8.15" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px">{INSIDE.format(id="q3in")}
    <div class="h hid" id="q3ch" style="font-size:62px">Le lien est prêt<br/><span>avec le rendez-vous</span></div>
    <div class="ok hid" id="q3o1"><i>✓</i>Lien Google Meet créé avec la séance</div>
    <div class="ok hid" id="q3o2"><i>✓</i>Votre cliente le retrouve dans son espace</div>
    <div class="ok hid" id="q3o3"><i>✓</i>Le rappel part par e-mail</div></div>
  {phone("q3p2", inner3b, 1240, 100)}
</div>'''
js += pop("#q3in", 83.1) + pop("#q3ch", 83.4, E, 40) + fin("#q3p2", 83.8)
js += pop("#q3o1", 84.1) + pop("#q3mt", 85.0, "back.out(2)") + pop("#q3o2", 86.55) + pop("#q3o3", 88.85)
js += 'tl.fromTo("#q3ml",{opacity:0,y:-60},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},89.0);\n'

# ---------- Q4 carte (91.2 -> 94.45)
h, j = qcard("q4", 91.2, 94.45, 4, "Après la séance,<br/><span>où va votre compte rendu&nbsp;?</span>", [], "cream", [], LOGO)
body += h; js += j

# ---------- Q4 conseil : perdu dans le fil (94.45 -> 104.1)
msgs = [("her", "Merci pour aujourd'hui"), ("me", "Avec plaisir"), ("cr", "📄 Compte rendu de séance"), ("her", "Vous avez un créneau jeudi ?"),
        ("me", "Oui, 14 h"), ("her", "Parfait"), ("her", "Je peux venir avec ma sœur ?"), ("me", "Bien sûr"), ("her", "Super, merci !"), ("her", "Vous me renvoyez le compte rendu ?")]
mh = "".join(f'<div class="bub {"me" if w == "me" else "her"}{" cr" if w == "cr" else ""}">{t}</div>' for w, t in msgs)
body += f'''
<div id="q4b" class="clip light" data-start="94.45" data-duration="9.65" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px;top:170px;bottom:auto"><div class="chap hid" id="q4bc"><b>4</b>Le conseil</div>
    <div class="h hid" id="q4bh">Envoyé par message,<br/><span>il se perd.</span></div>
    <div class="ok hid" id="q4o1"><i>✓</i>Rangé dans son espace, elle le relit quand elle veut</div></div>
  <div class="locks hid" id="q4lk">{LOCK.format(s=56, c="#E9C46A")}<div>Vos notes personnelles, à part<small>rien que pour vous</small></div></div>
  {phone("q4p", '<div class="phead"><div class="av">LM</div>Léa M.</div><div class="thread"><div id="q4th">' + mh + '</div></div>', 900, 100)}
  <div class="lost hid" id="q4x">Le compte rendu&nbsp;?<br/>Perdu dans le fil</div>
  <div class="box2 hid" id="q4y">Rangé&nbsp;:<br/>toujours au même endroit</div>
</div>'''
js += pop("#q4bc", 94.5, E) + pop("#q4bh", 94.7, E, 40) + fin("#q4p", 94.9)
js += 'tl.fromTo("#q4th",{y:0},{y:-430,duration:2.4,ease:"power1.inOut"},95.6);\n' + pop("#q4x", 96.2, "back.out(2)")
js += out("#q4x", 97.4) + pop("#q4y", 97.6, "back.out(2)") + pop("#q4o1", 97.6)
js += 'tl.fromTo("#q4lk",{opacity:0,y:40},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},101.1);\n'

# ---------- Q4 Dans GuidPilot (104.1 -> 112.95)
inner4 = ('<div class="phead">Mon espace</div>'
          '<div class="notif hid" id="q4n"><div class="ic"><img src="assets/favicon.png" alt="" /></div>'
          '<div><div class="a">Nouveau compte rendu</div><div class="b">Votre praticienne vous a écrit</div></div></div>'
          '<div class="cr"><div class="a">Compte rendu · séance du 3 nov.</div><div class="b">Reiki à distance</div>'
          '<div class="audio hid" id="q4au"><b><i></i></b><span></span></div><div class="nw">Nouveau</div></div>')
body += f'''
<div id="q4c" class="clip light" data-start="104.1" data-duration="8.85" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px">{INSIDE.format(id="q4in")}
    <div class="h hid" id="q4ch" style="font-size:56px;margin-top:20px">Écrit ou vocal, <span>livré dans son espace</span></div></div>
  <div class="two l hid" id="q4l" style="top:340px;width:560px;height:320px"><div class="lb">{LOCK.format(s=28, c="#E9C46A")}Notes internes</div>
    <div class="ttl" style="font-size:42px">Jamais visibles<br/>par votre cliente</div></div>
  <div class="two r hid" id="q4r" style="top:340px;left:700px;width:560px;height:320px"><div class="lb">✓ Compte rendu</div>
    <div class="ttl" style="font-size:42px">Écrit ou vocal,<br/>espace client sécurisé</div></div>
  {phone("q4p2", inner4, 1360, 100)}
</div>'''
js += pop("#q4in", 104.15) + pop("#q4ch", 104.4, E, 30)
js += 'tl.fromTo("#q4r",{opacity:0,x:60},{opacity:1,x:0,duration:.6,ease:"power3.out"},105.1);\n'
js += fin("#q4p2", 105.6) + pop("#q4au", 106.1) + 'tl.fromTo("#q4n",{opacity:0,y:60},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},107.3);\n'
js += 'tl.fromTo("#q4l",{opacity:0,x:-60},{opacity:1,x:0,duration:.6,ease:"power3.out"},109.4);\n'
js += 'tl.fromTo("#q4l",{scale:1},{scale:1.04,duration:.25,yoyo:true,repeat:1},111.3);\n'

# ---------- Q5 carte (112.95 -> 116.4)
h, j = qcard("q5", 112.95, 116.4, 5, "Suivez-vous vos clientes<br/><span>sur plusieurs séances&nbsp;?</span>", [], "navy", [])
body += h; js += j

# ---------- Q5 conseil (116.4 -> 125.15)
dots = "".join(f'<div id="q5d{i}"{" class=on" if i < 2 else ""}>{i + 1}</div>' for i in range(5))
body += f'''
<div id="q5b" class="clip warm" data-start="116.4" data-duration="8.75" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px"><div class="chap hid" id="q5bc"><b>5</b>Le conseil</div>
    <div class="h hid" id="q5bh">Un forfait,<br/><span>un cadre clair</span></div>
    <div class="soft hid" id="q5s" style="align-self:flex-start;margin-top:36px">Fin du cycle&nbsp;: demandez son avis, sans insister</div>
    <div class="stars hid" id="q5st"><i id="q5s0">★</i><i id="q5s1">★</i><i id="q5s2">★</i><i id="q5s3">★</i><i id="q5s4">★</i></div></div>
  <div class="fk hid" id="q5f"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="k">FORFAIT</div><div class="a">5 séances de Reiki</div><div class="b">Léa M. · cabinet ou à distance</div>
    <div class="dots">{dots}</div>
    <div class="left"><span>Séances restantes</span><b id="q5n">3</b></div></div>
</div>'''
js += pop("#q5bc", 116.45, E) + pop("#q5bh", 116.6, E, 40) + fin("#q5f", 117.0)
js += 'tl.to("#q5d2",{backgroundColor:"#2563EB",borderColor:"#2563EB",color:"#FFFFFF",duration:.4},118.0);\n'
js += 'tl.to("#q5n",{opacity:0,duration:.15},118.1);\n' + 'tl.set("#q5n",{textContent:"2"},118.25);\n' + 'tl.to("#q5n",{opacity:1,duration:.2},118.3);\n'
js += pop("#q5s", 120.9) + pop("#q5st", 122.1)
js += "".join(f'tl.to("#q5s{i}",{{color:"#E9C46A",duration:.2}},{122.5 + i * .25});\n' for i in range(5))

# ---------- Q5 Dans GuidPilot (125.15 -> 131.25)
body += f'''
<div id="q5c" class="clip light" data-start="125.15" data-duration="6.1" data-track-index="1">
  {LOGO}
  <div class="col" style="width:700px">{INSIDE.format(id="q5in")}
    <div class="h hid" id="q5ch" style="font-size:60px">Forfait décompté,<br/><span>avis sur votre page</span></div></div>
  <div class="avf hid" id="q5av"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>
    <span class="demo">Compte de démonstration</span></div><img src="assets/avis.png" alt="" /><div class="ring4 hid" id="q5r"></div></div>
  <div class="fk2 hid" id="q5fk"><div><div class="a">Forfait 5 séances</div><div class="b">une séance décomptée à chaque rendez-vous</div></div>
    <div class="n2" id="q5n2">2 <small>restantes</small></div></div>
</div>'''
js += pop("#q5in", 125.2) + pop("#q5ch", 125.4, E, 40) + pop("#q5fk", 126.2, y=40) + fin("#q5av", 128.0)
js += 'tl.fromTo("#q5r",{opacity:0,scale:1.3},{opacity:1,scale:1,duration:.5,ease:"back.out(1.6)"},129.0);\n'

# ---------- récap (131.25 -> 139.75)
rc = [("Des prestations claires,<br/><span>cabinet ou distance</span>", 132.2, ""), ("Paiement et conditions<br/><span>écrits avant</span>", 135.45, " g"),
      ("Un suivi rangé<br/><span>au même endroit</span>", 137.55, "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += f'''
<div id="r" class="clip light" data-start="131.25" data-duration="8.5" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>
</div>'''
js += pop("#rk", 131.35, E) + "".join(pop(f"#rc{i}", t, y=50) for i, (_, t, _) in enumerate(rc))

# ---------- GuidPilot (139.75 -> 151.0)
gc = [("Réservation", 143.86), ("Paiement", 144.93), ("Visio", 145.6), ("Comptes rendus", 146.47), ("Forfaits", 147.32), ("Factures", 148.17), ("Avis", 148.7)]
gch = "".join(f'<div class="hid" id="gc{i}">{a}</div>' for i, (a, _) in enumerate(gc))
body += f'''
<div id="g" class="clip light" data-start="139.75" data-duration="11.25" data-track-index="1">
  <div class="gpl"><img class="hid" id="gl" src="assets/logo_couleur.png" alt="GuidPilot" />
    <div class="b hid" id="gb">Un outil conçu pour<br/><span>les praticiens et les thérapeutes</span></div></div>
  <div class="gch" style="left:40px;right:40px;gap:16px">{gch}</div>
  <div class="gpbadge" style="top:930px"><div class="hid" id="gs">Dans un seul espace</div></div>
</div>'''
js += 'tl.fromTo("#gl",{opacity:0,scale:.92},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},139.85);\n' + pop("#gb", 140.6, E, 40)
js += "".join(pop(f"#gc{i}", t) for i, (_, t) in enumerate(gc)) + pop("#gs", 149.65)

# ---------- fin marine (151.0 -> DUR)
body += f'''
<div id="z" class="clip navy" data-start="151.0" data-duration="{round(DUR - 151.0, 2)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard hid" id="z7">✓ Sans carte bancaire</div>
    <div class="url hid" id="z8">guidpilot.fr</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += 'tl.fromTo("#z6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},151.1);\n'
js += pop("#z7", 153.2) + pop("#z8", 154.5) + pop("#z9", 157.0)
js += 'tl.to("#z9",{scale:1.06,duration:.45,yoyo:true,repeat:2,ease:"sine.inOut"},157.6);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA4}{EXTRA5}</style></head><body>
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

d = ATELIER / "build" / "yt-logiciel-reiki"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "avis.png", "finance.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
