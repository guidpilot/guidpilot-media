"""Vidéo YouTube 1920x1080 : « Logiciel pour sophrologue et hypnothérapeute : les 4 moments d'un cycle de séances »
(série « Pensé pour votre métier » · public thérapeutes, mardi 03/11/2026).
Usage : python3 gen_logiciel_sophro_hypno.py <voix.wav> <sent.json> [DUR]  -> build/yt-sophro-hypno/
Voix : 10 paragraphes générés un par un (voix/2026-11-03_yt-sophro-p1..p10.mp3), assemblés avec assembler_voix.py.
sent.json = début absolu de chaque phrase, par paragraphe (silencedetect + syllabes, recalé à la main sur 2 phrases).
Structure « parcours en 4 moments » : une route à 4 étapes revient à chaque moment (carte plein écran, fond qui change,
épingle « Vous êtes ici ») -> conseil illustré -> « Dans GuidPilot ». CTA oral d'abonnement après le moment 1 (~32 %).
Aucune personne représentée, aucune capture avec photo, aucun prix GuidPilot, aucun superlatif, aucun vocabulaire médical.
Réutilise CSS et helpers de gen_logiciel_reiki.py (qui lui-même reprend gen_therapeutes_soir.py + EXTRA4).
"""
import json, pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_logiciel_reiki.py").read_text()
ns = {"__file__": str(HERE / "gen_logiciel_reiki.py")}
exec(src.split("\n# ---------- A :")[0], ns)
CSS, EXTRA, EXTRA4, EXTRA5, ATELIER, KIT = (ns[k] for k in ("CSS", "EXTRA", "EXTRA4", "EXTRA5", "ATELIER", "KIT"))
pop, fin, out, phone, LOGO, LOGOW, E, INSIDE, LOCK, CAM, HOME = (ns[k] for k in (
    "pop", "fin", "out", "phone", "LOGO", "LOGOW", "E", "INSIDE", "LOCK", "CAM", "HOME"))

P = json.load(open(sys.argv[2]))
P[0][3] = round(P[0][0] + 5.6, 2)      # « Si vous êtes sophrologue… » (pas de silence net après « oublié »)
P[7][3] = round(P[7][0] + 8.07, 2)     # « Le bon réflexe : un forfait… »
DUR = float(sys.argv[3]) if len(sys.argv) > 3 else 185.5
r2 = lambda x: round(x, 2)

EXTRA7 = """
.hk7{position:absolute;left:110px;top:150px;width:860px}
.hk7 .d{font-weight:800;font-size:44px;letter-spacing:.06em;color:#93C5FD}
.hk7 .c{font-weight:800;font-size:220px;line-height:1;letter-spacing:-.045em;color:#fff;margin-top:6px}
.hk7 .c span{color:#E9C46A}
.hk7 .a{font-weight:800;font-size:66px;line-height:1.1;letter-spacing:-.02em;color:#fff;margin-top:34px}
.hk7 .b{font-weight:700;font-size:44px;color:#FDE68A;margin-top:24px}
.prof7{position:absolute;left:110px;top:880px;display:flex;gap:16px}
.prof7 div{padding:14px 30px;border-radius:999px;background:#1E293B;border:2px solid #475569;font-weight:700;font-size:32px;color:#F1F5F9}
.ag{position:absolute;left:1030px;top:150px;width:790px;height:620px;border-radius:30px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.35);overflow:hidden}
.ag .ct{height:100px;padding:0 36px;display:flex;align-items:center;justify-content:space-between;border-bottom:2px solid #E2E8F0;font-weight:800;font-size:34px;color:#0F172A}
.ag .ct small{font-weight:600;font-size:22px;color:#64748B}
.ag .hr{position:absolute;left:36px;right:36px;height:2px;background:#F1F5F9}
.ag .hl{position:absolute;left:36px;font-weight:700;font-size:22px;color:#94A3B8}
.ag .ev{position:absolute;left:140px;right:36px;width:auto;display:block;border-radius:18px;padding:18px 24px;font-weight:800;font-size:28px}
.ag .ev small{display:block;font-weight:600;font-size:22px;margin-top:4px}
.ag .ev.a{background:#EFF6FF;border-left:10px solid #2563EB;color:#1E3A8A}
.ag .ev.x{background:#FEF2F2;border-left:10px solid #DC2626;color:#7F1D1D}
.abs{position:absolute;right:20px;top:20px;padding:8px 18px;border-radius:999px;background:#DC2626;color:#fff;font-weight:800;font-size:22px}
.sms{position:absolute;left:1100px;top:810px;width:660px;padding:24px 28px;border-radius:24px;background:rgba(255,255,255,.97);box-shadow:0 20px 50px rgba(0,0,0,.35);display:flex;gap:20px;align-items:center}
.sms .ic{flex:none;width:60px;height:60px;border-radius:16px;background:#16A34A;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px}
.sms .a{font-weight:800;font-size:24px;color:#0F172A}.sms .b{font-weight:600;font-size:26px;color:#334155;margin-top:4px}
.cyc{position:absolute;left:160px;top:250px;width:1600px;height:300px}
.cyc .ln{position:absolute;left:0;right:0;top:70px;height:10px;border-radius:5px;background:#CBD5E1;transform-origin:left center}
.cyc .s{position:absolute;top:30px;width:90px;height:90px;margin-left:-45px;border-radius:50%;background:#fff;border:10px solid #2563EB;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:34px;color:#0F172A}
.cyc .t{position:absolute;top:150px;width:220px;margin-left:-110px;text-align:center}
.cyc .t div{display:inline-block;padding:8px 18px;border-radius:999px;font-weight:700;font-size:24px}
.cyc .t .cb{background:#FBF3DC;color:#6B4E16}.cyc .t .vi{background:#EFF6FF;color:#1D4ED8}
.cyc .lab{position:absolute;left:0;top:-40px;font-weight:800;font-size:30px;letter-spacing:.12em;color:#2563EB}
.m4{position:absolute;left:110px;right:110px;top:640px;display:flex;gap:30px}
.m4 div{flex:1;height:250px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.08);padding:30px;display:flex;flex-direction:column;justify-content:space-between}
.m4 b{display:flex;width:70px;height:70px;border-radius:50%;background:#0F172A;color:#E9C46A;align-items:center;justify-content:center;font-size:36px;font-weight:800}
.m4 span{font-weight:800;font-size:38px;line-height:1.15;color:#0F172A}
.mq{position:absolute;left:0;right:0;top:470px;text-align:center}
.mq .t{font-weight:800;font-size:58px;line-height:1.1;color:#0F172A}
.mq .t span{color:#2563EB}
.mz{position:absolute;left:150px;top:150px;width:1620px}
.mz .n{display:inline-flex;align-items:center;gap:22px;font-weight:800;font-size:34px;letter-spacing:.14em;text-transform:uppercase}
.mz .n b{display:inline-flex;width:84px;height:84px;border-radius:50%;align-items:center;justify-content:center;font-size:44px;letter-spacing:0}
.mz .q{font-weight:800;font-size:120px;line-height:1.04;letter-spacing:-.035em;margin-top:40px}
.route{position:absolute;left:190px;top:700px;width:1540px;height:220px}
.route .ln{position:absolute;left:0;right:0;top:56px;height:12px;border-radius:6px;opacity:.3}
.route .done{position:absolute;left:0;top:56px;height:12px;border-radius:6px}
.route .st{position:absolute;top:22px;width:80px;height:80px;margin-left:-40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:34px}
.route .lb{position:absolute;top:122px;width:330px;margin-left:-165px;text-align:center;font-weight:700;font-size:28px;line-height:1.2}
.route .pin{position:absolute;top:-58px;width:220px;margin-left:-110px;text-align:center}
.route .pin div{display:inline-block;padding:8px 20px;border-radius:999px;font-weight:800;font-size:22px}
.cream .mz .n{color:#B7791F}.cream .mz .n b{background:#0F172A;color:#E9C46A}.cream .mz .q{color:#0F172A}.cream .mz .q span{color:#2563EB}
.cream .route .ln,.cream .route .done{background:#0F172A}.cream .route .st{background:#fff;border:6px solid #0F172A;color:#0F172A}.cream .route .lb{color:#334155}
.navy .mz .n{color:#93C5FD}.navy .mz .n b{background:#E9C46A;color:#0F172A}.navy .mz .q{color:#fff}.navy .mz .q span{color:#E9C46A}
.navy .route .ln,.navy .route .done{background:#E9C46A}.navy .route .st{background:#1E293B;border:6px solid #E9C46A;color:#fff}.navy .route .lb{color:#CBD5E1}
.blue .mz .n{color:#BFDBFE}.blue .mz .n b{background:#fff;color:#1D4ED8}.blue .mz .q{color:#fff}.blue .mz .q span{color:#FDE68A}
.blue .route .ln,.blue .route .done{background:#fff}.blue .route .st{background:#1D4ED8;border:6px solid #fff;color:#fff}.blue .route .lb{color:#DBEAFE}
.route .st.cur{background:#E9C46A!important;border-color:#E9C46A!important;color:#0F172A!important;transform:scale(1.25)}
.route .pin div{background:#E9C46A;color:#0F172A}
.qsb{position:absolute;left:24px;right:24px;top:170px}
.qsb .bub{position:relative;display:table;max-width:none;white-space:nowrap;margin:0 0 22px 0;font-size:27px}
.qsb .bub.her{left:0}
.xline{position:absolute;left:-6px;right:-6px;top:50%;height:6px;margin-top:-3px;border-radius:3px;background:#DC2626;transform-origin:left center}
.ppage{position:absolute;left:880px;top:150px;width:940px;height:800px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.ppage .tp{height:220px;background:#0F172A;padding:46px 50px;color:#fff}
.ppage .tp .k{font-weight:700;font-size:22px;letter-spacing:.14em;color:#E9C46A}
.ppage .tp .n{font-weight:800;font-size:48px;margin-top:12px}
.ppage .tp .m{display:inline-block;margin-top:16px;padding:6px 18px;border-radius:999px;background:#1E293B;border:2px solid #475569;font-weight:700;font-size:22px;color:#E2E8F0}
.ppage .it{position:relative;margin:30px 44px 0;padding:28px 30px;border-radius:22px;border:2px solid #E2E8F0;background:#F8FAFC}
.ppage .it .a{font-weight:800;font-size:34px;color:#0F172A}
.ppage .it .b{display:flex;gap:12px;margin-top:14px}
.ppage .it .b span{padding:6px 16px;border-radius:999px;background:#fff;border:2px solid #E2E8F0;font-weight:700;font-size:22px;color:#334155}
.ppage .it .rv{position:absolute;right:28px;top:50%;margin-top:-32px;height:64px;padding:0 28px;border-radius:16px;background:#2563EB;color:#fff;font-weight:800;font-size:26px;display:flex;align-items:center}
.ppage .ft{margin:30px 44px 0;padding:22px 28px;border-radius:18px;background:#FBF3DC;font-weight:700;font-size:26px;color:#6B4E16}
.email{position:absolute;left:900px;top:190px;width:900px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.email .eh{height:96px;padding:0 40px;display:flex;align-items:center;gap:20px;background:#F1F5F9;border-bottom:2px solid #E2E8F0;font-weight:800;font-size:30px;color:#0F172A}
.email .eh i{font-style:normal;width:54px;height:54px;border-radius:14px;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px}
.email .bd{padding:40px 46px}
.email .tt{font-weight:800;font-size:46px;color:#0F172A}
.email .rw{display:flex;align-items:center;gap:24px;margin-top:30px;padding:22px 28px;border-radius:20px;background:#F8FAFC;border:2px solid #E2E8F0;font-weight:700;font-size:32px;color:#334155}
.email .rw b{flex:none;width:150px;font-weight:800;color:#2563EB}
.note7{position:absolute;left:110px;top:560px;width:720px;padding:34px 40px;border-radius:26px;background:#FFFDF7;border:2px solid #E7DFC9;box-shadow:0 20px 50px rgba(15,23,42,.1)}
.note7 .h7{display:flex;align-items:center;gap:16px;font-weight:800;font-size:32px;color:#0F172A}
.note7 .h7 small{margin-left:auto;padding:6px 16px;border-radius:999px;background:#0F172A;color:#E9C46A;font-weight:800;font-size:20px}
.note7 .l7{font-weight:600;font-style:italic;font-size:28px;color:#475569;margin-top:20px}
.nbk7{position:absolute;left:980px;top:170px;width:700px;height:760px;border-radius:12px 26px 26px 12px;background:#FFFDF7;border:2px solid #E7DFC9;border-left:34px solid #1E3A8A;box-shadow:0 30px 80px rgba(15,23,42,.16);transform:rotate(-2deg);padding:56px 56px}
.nbk7 .t{font-weight:800;font-size:38px;color:#0F172A}
.nbk7 .r{display:flex;align-items:center;gap:26px;margin-top:40px;font-weight:600;font-style:italic;font-size:34px;color:#475569}
.nbk7 .r b{font-style:normal;font-weight:800;color:#1E3A8A;letter-spacing:.2em}
.nbk7 .q{position:absolute;right:60px;bottom:60px;font-weight:800;font-size:150px;color:#DC2626}
.tri{position:absolute;left:110px;right:110px;top:380px;display:flex;gap:36px}
.tri .c{position:relative;flex:1;height:500px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.08);padding:40px;overflow:hidden}
.tri .c .k{font-weight:800;font-size:24px;letter-spacing:.12em;color:#2563EB}
.tri .c .a{font-weight:800;font-size:44px;line-height:1.12;color:#0F172A;margin-top:14px}
.tri .dots6{display:flex;flex-wrap:wrap;gap:16px;margin-top:40px}
.tri .dots6 div{width:80px;height:80px;border-radius:50%;border:7px solid #CBD5E1;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:30px;color:#94A3B8}
.tri .dots6 div.on{border-color:#2563EB;background:#2563EB;color:#fff}
.tri .stars i{font-size:64px}
.tri .ln{height:14px;border-radius:7px;background:#E2E8F0;margin-top:22px}
.capf{position:absolute;left:880px;width:940px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.capf img{display:block;width:940px}
"""

body, js = "", ""
STOPS = ["Avant la 1<sup>re</sup> séance", "La veille", "Juste après", "Sur tout le cycle"]
XS = [0, 513, 1026, 1540]


def mcard(id_, start, end, num, title, cls, logo):
    sts = "".join(f'<div class="st{" cur" if i == num - 1 else ""}" style="left:{x}px">{i + 1}</div>'
                  f'<div class="lb" style="left:{x}px">{STOPS[i]}</div>' for i, x in enumerate(XS))
    h = f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(start)}" data-duration="{r2(end - start)}" data-track-index="1">
  {logo}
  <div class="mz"><div class="n hid" id="{id_}n"><b>{num}</b>Moment {num} sur 4</div><div class="q hid" id="{id_}q">{title}</div></div>
  <div class="route"><div class="ln"></div><div class="done" id="{id_}d" style="width:{XS[num - 1]}px"></div>{sts}
    <div class="pin hid" id="{id_}p" style="left:{XS[num - 1]}px"><div>Vous êtes ici</div></div></div>
</div>'''
    j = pop(f"#{id_}n", start + .05, E) + pop(f"#{id_}q", start + .2, E, 50)
    j += f'tl.fromTo("#{id_}d",{{scaleX:0,transformOrigin:"left center"}},{{scaleX:1,duration:.8,ease:"power2.inOut"}},{r2(start + .3)});\n'
    j += pop(f"#{id_}p", start + 1.0, "back.out(2)", -20)
    return h, j


# ---------- A : accroche (0 -> P[0][4]) — lisible dès l'image 0
tA = P[0][4]
body += f'''
<div id="a" class="clip navy" data-start="0" data-duration="{r2(tA)}" data-track-index="1">
  <div class="hk7"><div class="d">MARDI</div><div class="c">18<span>:</span>40</div>
    <div class="a">Votre cliente de 18 h<br/>n'est pas venue.</div>
    <div class="b hid" id="ab">Elle avait simplement oublié.</div></div>
  <div class="ag"><span class="illus" style="left:36px;bottom:20px">Illustration</span>
    <div class="ct">Mardi 3 novembre<small>Agenda</small></div>
    <div class="hr" style="top:150px"></div><div class="hl" style="top:162px">17 h</div>
    <div class="hr" style="top:300px"></div><div class="hl" style="top:312px">18 h</div>
    <div class="hr" style="top:450px"></div><div class="hl" style="top:462px">19 h</div>
    <div class="ev a" style="top:160px;height:110px">Sophrologie · suivi<small>17 h – 18 h · Claire B.</small></div>
    <div class="ev x" id="aev" style="top:310px;height:110px">Hypnose · séance 3<small>18 h – 19 h · Sarah L.</small><span class="abs hid" id="aab">Absente</span></div></div>
  <div class="sms hid" id="asms"><div class="ic">✉</div><div><div class="a">Sarah L. · 18:52</div><div class="b">Désolée, j'avais complètement oublié&nbsp;!</div></div></div>
  <div class="prof7"><div class="hid" id="ap0">Sophrologue</div><div class="hid" id="ap1">Hypnothérapeute</div></div>
</div>'''
js += pop("#aab", 1.2, "back.out(2)") + pop("#ab", P[0][2], E) + pop("#asms", P[0][2] + .3, y=60)
js += pop("#ap0", P[0][3] + .9) + pop("#ap1", P[0][3] + 1.5)

# ---------- B : un cycle, 4 moments (P[0][4] -> P[1][0])
cyc = "".join(f'<div class="s hid" id="bs{i}" style="left:{i * 320}px">{i + 1}</div>'
              f'<div class="t hid" id="bt{i}" style="left:{i * 320}px"><div class="{"vi" if i in (2, 4) else "cb"}">{"Visio" if i in (2, 4) else "Cabinet"}</div></div>' for i in range(6))
m4 = "".join(f'<div class="hid" id="bm{i}"><b>{i + 1}</b><span>{s}</span></div>' for i, s in enumerate(STOPS))
body += f'''
<div id="b" class="clip light" data-start="{r2(tA)}" data-duration="{r2(P[1][0] - tA)}" data-track-index="1">
  {LOGO}
  <div class="cyc"><div class="lab hid" id="blab">UN CYCLE DE SÉANCES</div><div class="ln hid" id="bln"></div>{cyc}</div>
  <div class="m4">{m4}</div>
  <div class="mq hid" id="bq"><div class="t">4 moments où votre outil doit <span>travailler à votre place</span></div></div>
</div>'''
js += pop("#blab", tA + .1, E) + f'tl.fromTo("#bln",{{opacity:1,scaleX:0}},{{opacity:1,scaleX:1,duration:1.4,ease:"power2.inOut"}},{r2(tA + .3)});\n'
js += "".join(pop(f"#bs{i}", tA + .5 + i * .3, "back.out(2)") + pop(f"#bt{i}", tA + 2.4 + i * .25) for i in range(6))
t5 = P[0][5]
js += pop("#bq", t5 + .1, E, 40) + "".join(pop(f"#bm{i}", t5 + 2.2 + i * .5, y=50) for i in range(4))

# ---------- M1 carte
h, j = mcard("m1", P[1][0], P[1][1], 1, "Avant la<br/><span>première séance</span>", "cream", LOGO)
body += h; js += j

# ---------- M1 conseil : 2 prestations (P[1][1] -> P[1][4])
s = P[1]
body += f'''
<div id="m1b" class="clip light" data-start="{r2(s[1])}" data-duration="{r2(s[4] - s[1])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="m1bc"><b>1</b>Le conseil</div>
    <div class="h hid" id="m1bh" style="font-size:56px">Première séance plus longue&nbsp;? <span>Deux prestations.</span></div></div>
  <div class="pres hid" id="m1p1" style="left:110px;top:360px"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="ic" style="background:#FBF3DC">{HOME}</div><div class="tt">Première séance<br/>d'hypnose</div>
    <div class="row hid" id="m1r1"><i>⏱</i>Durée : 1 h 30</div><div class="row hid" id="m1r2"><i>€</i>Son propre tarif</div>
    <div class="row hid" id="m1r3"><i>⌂</i>Au cabinet</div></div>
  <div class="pres hid" id="m1p2" style="left:1030px;top:360px"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="ic" style="background:#EFF6FF">{CAM}</div><div class="tt">Séance<br/>de suivi</div>
    <div class="row hid" id="m1r4"><i>⏱</i>Durée : 1 h</div><div class="row hid" id="m1r5"><i>€</i>Son propre tarif</div>
    <div class="row hid" id="m1r6"><i>▶</i>Au cabinet ou en visio</div></div>
</div>'''
js += pop("#m1bc", s[1] + .05, E) + pop("#m1bh", s[1] + .25, E, 40)
js += fin("#m1p1", s[2] + 1.6, -120) + fin("#m1p2", s[2] + 5.2)
js += pop("#m1r1", s[2] + 3.0) + pop("#m1r2", s[2] + 4.0) + pop("#m1r4", s[2] + 6.0) + pop("#m1r5", s[2] + 6.4)
js += pop("#m1r3", s[3] + 1.6) + pop("#m1r6", s[3] + 2.4)

# ---------- M1 : 3 messages évités (P[1][4] -> P[2][0])
qs = ["C'est combien de temps&nbsp;?", "C'est au cabinet&nbsp;?", "Et la première fois&nbsp;?"]
qh = "".join(f'<div class="bub her hid" id="m1q{i}">{q}<i class="xline hid" id="m1x{i}"></i></div>' for i, q in enumerate(qs))
body += f'''
<div id="m1d" class="clip warm" data-start="{r2(s[4])}" data-duration="{r2(P[2][0] - s[4])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:780px"><div class="h hid" id="m1dh" style="font-size:80px">Elle choisit seule.<br/><span>Sans trois messages.</span></div></div>
  {phone("m1ph", '<div class="phead"><div class="av">SL</div>Sarah L.</div><div class="qsb">' + qh + '</div>', 1240, 100)}
</div>'''
js += pop("#m1dh", s[4] + .1, E, 40) + fin("#m1ph", s[4] + .1)
js += "".join(pop(f"#m1q{i}", s[4] + .5 + i * .35, y=20) for i in range(3))
js += "".join(f'tl.fromTo("#m1x{i}",{{opacity:1,scaleX:0}},{{opacity:1,scaleX:1,duration:.3}},{r2(s[4] + 2.0 + i * .25)});\n' for i in range(3))

# ---------- M1 : conditions écrites (P[2][0] -> P[2][1])
s = P[2]
rl = [("Paiement", "en ligne à la réservation, ou au cabinet"), ("Annulation", "gratuite jusqu'à 48 h avant"), ("Report", "possible une fois, en prévenant")]
rlh = "".join(f'<div class="r hid" id="m1c{i}"><i>{i + 1}</i><div><b style="color:#0F172A">{a}&nbsp;:</b> {b}</div></div>' for i, (a, b) in enumerate(rl))
body += f'''
<div id="m1e" class="clip light" data-start="{r2(s[0])}" data-duration="{r2(s[1] - s[0])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px"><div class="chap hid" id="m1ec"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="m1eh">Vos conditions,<br/><span>écrites avant.</span></div></div>
  <div class="rules hid" id="m1ru"><div class="tt">Mes conditions<span class="ex">Exemple</span></div>{rlh}
    <div class="seen2 hid" id="m1s">Affichées avant la réservation</div></div>
</div>'''
js += pop("#m1ec", s[0] + .05, E) + pop("#m1eh", s[0] + .25, E, 40) + fin("#m1ru", s[0] + .6)
js += pop("#m1c0", s[0] + 2.6) + pop("#m1c1", s[0] + 4.4) + pop("#m1c2", s[0] + 5.0) + pop("#m1s", s[0] + 5.4)

# ---------- M1 Dans GuidPilot (P[2][1] -> P[3][0])
body += f'''
<div id="m1g" class="clip light" data-start="{r2(s[1])}" data-duration="{r2(P[3][0] - s[1])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px">{INSIDE.format(id="m1gi")}
    <div class="h hid" id="m1gh" style="font-size:60px">Chaque prestation<br/><span>a sa durée, son lieu,<br/>son tarif</span></div>
    <div class="ok hid" id="m1go1"><i>✓</i>Réservation depuis votre page</div>
    <div class="ok hid" id="m1go2"><i>✓</i>Règlement en ligne ou au cabinet</div></div>
  <div class="ppage hid" id="m1pp"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="tp"><div class="k">VOTRE PAGE</div><div class="n">Sophrologie &amp; hypnose</div><div class="m">Au cabinet · En visio</div></div>
    <div class="it hid" id="m1i1"><div class="a">Première séance d'hypnose</div><div class="b"><span>1 h 30</span><span>Au cabinet</span></div><div class="rv">Réserver</div></div>
    <div class="it hid" id="m1i2"><div class="a">Séance de suivi</div><div class="b"><span>1 h</span><span>Cabinet ou visio</span></div><div class="rv">Réserver</div></div>
    <div class="ft hid" id="m1ft">Conditions d'annulation affichées avant de réserver</div></div>
</div>'''
js += pop("#m1gi", s[1] + .05) + pop("#m1gh", s[1] + .3, E, 40) + fin("#m1pp", s[1] + .5)
js += pop("#m1i1", s[1] + 1.6) + pop("#m1i2", s[1] + 2.4) + pop("#m1ft", s[1] + 3.3)
js += pop("#m1go1", s[2] + .3) + pop("#m1go2", s[2] + 2.4)
js += f'tl.to("#m1i1 .rv",{{scale:1.1,duration:.25,yoyo:true,repeat:1}},{r2(s[2] + 1.0)});\n'

# ---------- CTA oral abonnement (P[3][0] -> P[4][0])
s = P[3]
body += f'''
<div id="cta" class="clip navy" data-start="{r2(s[0])}" data-duration="{r2(P[4][0] - s[0])}" data-track-index="1">
  {LOGOW}
  <div class="ctaC"><div class="k hid" id="ck">CES CONSEILS VOUS SONT UTILES&nbsp;?</div>
    <div class="b hid" id="cb">2 vidéos par semaine<br/><span>pour organiser votre cabinet</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="dsc hid" id="cd">↓ <span><b>Essai gratuit&nbsp;:</b> le lien est dans la description</span></div>
</div>'''
js += pop("#ck", s[0] + .1, E) + pop("#cy", s[0] + 1.6, "back.out(2)") + pop("#cb", s[0] + 2.6, E, 40)
js += f'tl.to("#cy",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(s[0] + 3.2)});\n' + pop("#cd", s[1] + .2)

# ---------- M2 carte
s = P[4]
h, j = mcard("m2", s[0], s[1], 2, "La veille<br/><span>de la séance</span>", "navy", LOGOW)
body += h; js += j

# ---------- M2 : rappel à la main le soir (P[4][1] -> P[4][3])
inner = ('<div class="phead"><div class="av">SL</div>Sarah L.</div>'
         '<div class="typing"><div class="bub me hid" id="m2m" style="position:relative;display:table;margin-left:auto;right:0">Bonsoir, je vous rappelle notre séance demain à 18 h…</div></div>')
body += f'''
<div id="m2b" class="clip eve" data-start="{r2(s[1])}" data-duration="{r2(s[3] - s[1])}" data-track-index="1">
  {LOGOW}
  <div class="night"><div class="clk hid" id="m2k">21<span>:</span>47</div><div class="d hid" id="m2d">Un rappel à la main, pour chaque séance de demain</div>
    <div class="todo hid" id="m2t">✕ Une tâche de trop</div></div>
  {phone("m2p", inner, 1240, 100)}
</div>'''
js += pop("#m2k", s[1] + .05, E) + pop("#m2d", s[1] + 1.2, E) + fin("#m2p", s[1] + .4) + pop("#m2m", s[2] + .2, y=20)
js += pop("#m2t", s[2] + 2.4, "back.out(2)")

# ---------- M2 : le bon réflexe (P[4][3] -> P[4][4])
body += f'''
<div id="m2c" class="clip light" data-start="{r2(s[3])}" data-duration="{r2(s[4] - s[3])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:700px"><div class="chap hid" id="m2cc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="m2ch">Un rappel<br/><span>automatique,<br/>la veille</span></div></div>
  <div class="email hid" id="m2e"><span class="illus" style="right:24px;top:28px">Illustration</span>
    <div class="eh"><i>✉</i>Rappel de votre séance</div>
    <div class="bd"><div class="tt">C'est demain&nbsp;!</div>
      <div class="rw hid" id="m2r0"><b>Jour</b>Mercredi 4 novembre</div>
      <div class="rw hid" id="m2r1"><b>Heure</b>18 h – 19 h</div>
      <div class="rw hid" id="m2r2"><b>Lieu</b>Au cabinet, ou lien de la visio</div></div></div>
</div>'''
js += pop("#m2cc", s[3] + .05, E) + pop("#m2ch", s[3] + .25, E, 40) + fin("#m2e", s[3] + .5)
js += pop("#m2r0", s[3] + 3.0) + pop("#m2r1", s[3] + 3.6) + pop("#m2r2", s[3] + 4.3)

# ---------- M2 Dans GuidPilot (P[4][4] -> P[5][0])
inner2 = ('<div class="phead">Mon espace</div>'
          '<div class="mail hid" id="m2ml"><div class="a">✉ Rappel : votre séance demain à 18 h</div><div class="b">Séance de suivi · en visio · lien inclus</div></div>'
          '<div class="rdv" style="margin-top:150px"><div class="a">Séance de suivi</div><div class="b">Mercredi 4 nov. · 18 h – 19 h</div>'
          f'<div class="meet hid" id="m2mt">{CAM.replace("#2563EB", "#FFFFFF").replace("52", "34")}Rejoindre la visio</div></div>')
body += f'''
<div id="m2g" class="clip light" data-start="{r2(s[4])}" data-duration="{r2(P[5][0] - s[4])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px">{INSIDE.format(id="m2gi")}
    <div class="h hid" id="m2gh" style="font-size:62px">Le rappel part<br/><span>la veille, par e-mail</span></div>
    <div class="ok hid" id="m2go1"><i>✓</i>Sans rien envoyer vous-même</div>
    <div class="ok hid" id="m2go2"><i>✓</i>Lien de visio inclus pour les séances à distance</div></div>
  {phone("m2p2", inner2, 1240, 100)}
</div>'''
js += pop("#m2gi", s[4] + .05) + pop("#m2gh", s[4] + .3, E, 40) + fin("#m2p2", s[4] + .6)
js += f'tl.fromTo("#m2ml",{{opacity:0,y:-60}},{{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"}},{r2(s[4] + 1.6)});\n'
js += pop("#m2go1", s[4] + 2.4) + pop("#m2go2", s[4] + 3.4) + pop("#m2mt", s[4] + 3.8, "back.out(2)")

# ---------- M3 carte
s = P[5]
h, j = mcard("m3", s[0], s[1], 3, "Juste après<br/><span>la séance</span>", "blue", LOGOW)
body += h; js += j

# ---------- M3 : deux écrits, deux endroits (P[5][1] -> P[6][0])
body += f'''
<div id="m3b" class="clip light" data-start="{r2(s[1])}" data-duration="{r2(P[6][0] - s[1])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="m3bc"><b>3</b>Le conseil</div>
    <div class="h hid" id="m3bh" style="font-size:58px">Deux écrits, <span>deux endroits différents</span></div></div>
  <div class="two l hid" id="m3l"><div class="lb">{LOCK.format(s=28, c="#E9C46A")}Vos notes personnelles</div>
    <div class="ttl">À reprendre<br/>la prochaine fois</div><div class="ln"></div><div class="ln" style="width:75%"></div><div class="ln" style="width:60%"></div>
    <div class="soft hid" id="m3pv" style="margin-top:34px;background:#0F172A;color:#E9C46A">Privé</div></div>
  <div class="two r hid" id="m3r"><div class="lb">✓ Ce que votre cliente garde</div>
    <div class="row hid" id="m3r1"><i></i>Un compte rendu de séance</div>
    <div class="row hid" id="m3r2"><i></i>L'exercice vu en séance, en audio</div>
    <div class="audio hid" id="m3au" style="margin-top:30px;padding:22px 24px"><b style="width:60px;height:60px"><i></i></b><span style="height:40px"></span></div>
    <div class="row hid" id="m3r3"><i></i>À refaire chez elle</div></div>
</div>'''
js += pop("#m3bc", s[1] + .05, E) + pop("#m3bh", s[1] + .25, E, 40)
js += 'tl.fromTo("#m3l",{opacity:0,x:-80},{opacity:1,x:0,duration:.6,ease:"power3.out"},' + str(r2(s[2] + .1)) + ');\n'
js += pop("#m3pv", s[3] + .1, "back.out(2)")
js += 'tl.fromTo("#m3r",{opacity:0,x:80},{opacity:1,x:0,duration:.6,ease:"power3.out"},' + str(r2(s[4] + .1)) + ');\n'
js += pop("#m3r1", s[4] + 2.0) + pop("#m3r2", s[4] + 3.6) + pop("#m3au", s[4] + 4.3) + pop("#m3r3", s[4] + 5.6)

# ---------- M3 Dans GuidPilot (P[6][0] -> P[7][0])
s = P[6]
inner3 = ('<div class="phead">Mon espace</div>'
          '<div class="notif hid" id="m3n"><div class="ic"><img src="assets/favicon.png" alt="" /></div>'
          '<div><div class="a">Nouveau compte rendu</div><div class="b">Votre praticienne vous a écrit</div></div></div>'
          '<div class="cr"><div class="a">Compte rendu · séance du 3 nov.</div><div class="b">Exercice de respiration (audio)</div>'
          '<div class="audio"><b><i></i></b><span></span></div><div class="nw">Nouveau</div></div>'
          '<div class="cr"><div class="a">Compte rendu · séance du 27 oct.</div><div class="b">Écrit</div></div>')
body += f'''
<div id="m3g" class="clip light" data-start="{r2(s[0])}" data-duration="{r2(P[7][0] - s[0])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:760px;top:120px;bottom:auto">{INSIDE.format(id="m3gi")}
    <div class="h hid" id="m3gh" style="font-size:60px">Notes à part,<br/><span>compte rendu livré</span></div>
    <div class="ok hid" id="m3go"><i>✓</i>Écrit ou vocal, dans son espace sécurisé</div></div>
  <div class="note7 hid" id="m3nt" style="top:620px"><div class="h7">{LOCK.format(s=40, c="#B7791F")}Notes internes<small>Jamais visibles</small></div>
    <div class="l7">« Séance 4 : reprendre l'exercice du début »</div><div class="l7" style="font-size:22px;font-style:normal;color:#8A6A2B">Fiche cliente · Sarah L.</div></div>
  {phone("m3p", inner3, 1300, 100)}
</div>'''
js += pop("#m3gi", s[0] + .05) + pop("#m3gh", s[0] + .3, E, 40) + pop("#m3nt", s[0] + 1.4, y=40)
js += pop("#m3go", s[1] + .2)
js += fin("#m3p", s[1] + .5)
js += f'tl.fromTo("#m3n",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"}},{r2(s[2] + .2)});\n'

# ---------- M4 carte
s = P[7]
h, j = mcard("m4", s[0], s[1], 4, "Sur tout<br/><span>le cycle</span>", "cream", LOGO)
body += h; js += j

# ---------- M4 : qui compte ? (P[7][1] -> P[7][3])
body += f'''
<div id="m4b" class="clip warm" data-start="{r2(s[1])}" data-duration="{r2(s[3] - s[1])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:760px"><div class="chap hid" id="m4bc"><b>4</b>La question</div>
    <div class="h hid" id="m4bh" style="font-size:76px">Forfait de 6 séances&nbsp;:<br/><span>qui compte celles<br/>qui restent&nbsp;?</span></div></div>
  <div class="nbk7 hid" id="m4nb"><span class="illus" style="right:24px;top:24px">Illustration</span><div class="t">Forfaits en cours</div>
    <div class="r">Sarah L. <b>||||</b></div><div class="r">Claire B. <b>||</b> <span style="color:#DC2626">(ou |||&nbsp;?)</span></div>
    <div class="r">Inès M. <b>|</b></div><div class="q hid" id="m4q">?</div></div>
</div>'''
js += pop("#m4bc", s[1] + .05, E) + pop("#m4bh", s[1] + .25, E, 40) + fin("#m4nb", s[1] + 1.0)
js += pop("#m4q", s[2] + .2, "back.out(2.5)")

# ---------- M4 : le bon réflexe en 3 (P[7][3] -> P[7][4])
dots = "".join(f'<div{" class=on" if i < 2 else ""} id="m4d{i}">{i + 1}</div>' for i in range(6))
body += f'''
<div id="m4c" class="clip light" data-start="{r2(s[3])}" data-duration="{r2(s[4] - s[3])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="m4cc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="m4ch" style="font-size:58px">Un cycle <span>suivi du début à la fin</span></div></div>
  <div class="tri">
    <div class="c hid" id="m4t0"><span class="illus" style="right:20px;top:20px">Illustration</span><div class="k">FORFAIT</div><div class="a">Séance après séance</div><div class="dots6">{dots}</div></div>
    <div class="c hid" id="m4t1"><div class="k">FACTURES</div><div class="a">Une par règlement</div><div class="ln"></div><div class="ln" style="width:70%"></div><div class="ln"></div>
      <div class="stamp hid" id="m4st" style="right:40px;top:300px">PAYÉE</div></div>
    <div class="c hid" id="m4t2"><div class="k">FIN DU CYCLE</div><div class="a">Une demande d'avis, sans insister</div>
      <div class="stars" style="margin-top:50px"><i id="m4s0">★</i><i id="m4s1">★</i><i id="m4s2">★</i><i id="m4s3">★</i><i id="m4s4">★</i></div></div>
  </div>
</div>'''
js += pop("#m4cc", s[3] + .05, E) + pop("#m4ch", s[3] + .25, E, 40)
js += pop("#m4t0", s[3] + 1.6, y=50) + f'tl.to("#m4d2",{{backgroundColor:"#2563EB",borderColor:"#2563EB",color:"#FFFFFF",duration:.4}},{r2(s[3] + 3.0)});\n'
js += pop("#m4t1", s[3] + 4.2, y=50) + f'tl.fromTo("#m4st",{{opacity:0,scale:1.6}},{{opacity:1,scale:1,duration:.35,ease:"back.out(2)"}},{r2(s[3] + 5.4)});\n'
js += pop("#m4t2", s[3] + 6.4, y=50) + "".join(f'tl.to("#m4s{i}",{{color:"#E9C46A",duration:.2}},{r2(s[3] + 8.0 + i * .2)});\n' for i in range(5))

# ---------- M4 Dans GuidPilot (P[7][4] -> P[8][0])
body += f'''
<div id="m4g" class="clip light" data-start="{r2(s[4])}" data-duration="{r2(P[8][0] - s[4])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px">{INSIDE.format(id="m4gi")}
    <div class="h hid" id="m4gh" style="font-size:58px">Forfait décompté,<br/><span>factures et avis<br/>au même endroit</span></div></div>
  <div class="fk2 hid" id="m4fk" style="top:170px"><div><div class="a">Forfait 6 séances · Sarah L.</div><div class="b">visible aussi dans son espace</div></div>
    <div class="n2" id="m4n2">3 <small>restantes</small></div></div>
  <div class="capf hid" id="m4fi" style="top:400px"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>
    <span class="demo">Compte de démonstration</span></div><img src="assets/finance.png" alt="" /></div>
  <div class="capf hid" id="m4av" style="top:690px"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>
    <span class="demo">Compte de démonstration</span></div><img src="assets/avis.png" alt="" /></div>
</div>'''
js += pop("#m4gi", s[4] + .05) + pop("#m4gh", s[4] + .3, E, 40) + pop("#m4fk", s[4] + 1.2, y=40)
js += 'tl.to("#m4n2",{opacity:0,duration:.15},' + str(r2(s[4] + 3.2)) + ');\n'
js += 'tl.set("#m4n2",{innerHTML:"2 <small>restantes</small>"},' + str(r2(s[4] + 3.36)) + ');\n' + 'tl.to("#m4n2",{opacity:1,duration:.2},' + str(r2(s[4] + 3.4)) + ');\n'
js += fin("#m4fi", s[5] + .1) + fin("#m4av", s[5] + 2.6)

# ---------- récap (P[8][0] -> P[9][0])
s = P[8]
rc = [("Prestations claires,<br/><span>conditions écrites</span>", s[1] + .1, ""), ("Un rappel automatique,<br/><span>la veille</span>", s[2] + .1, " g"),
      ("Notes d'un côté,<br/><span>compte rendu de l'autre</span>", s[3] + .1, "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += f'''
<div id="r" class="clip light" data-start="{r2(s[0])}" data-duration="{r2(P[9][0] - s[0])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>
</div>'''
js += pop("#rk", s[0] + .05, E) + "".join(pop(f"#rc{i}", t, y=50) for i, (_, t, _) in enumerate(rc))

# ---------- GuidPilot (P[9][0] -> P[9][1])
s = P[9]
gc = ["Réservation", "Paiement", "Rappels", "Comptes rendus", "Forfaits", "Factures", "Avis"]
gch = "".join(f'<div class="hid" id="gc{i}">{a}</div>' for i, a in enumerate(gc))
body += f'''
<div id="g" class="clip light" data-start="{r2(s[0])}" data-duration="{r2(s[1] - s[0])}" data-track-index="1">
  <div class="gpl"><img class="hid" id="gl" src="assets/logo_couleur.png" alt="GuidPilot" />
    <div class="b hid" id="gb">Un outil conçu pour<br/><span>les praticiens et les thérapeutes</span></div></div>
  <div class="gch" style="left:40px;right:40px;gap:16px">{gch}</div>
  <div class="gpbadge" style="top:930px"><div class="hid" id="gs">Dans un seul espace</div></div>
</div>'''
js += f'tl.fromTo("#gl",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"}},{r2(s[0] + .1)});\n' + pop("#gb", s[0] + .8, E, 40)
js += "".join(pop(f"#gc{i}", s[0] + 4.2 + i * .6) for i in range(7)) + pop("#gs", s[1] - 1.2)

# ---------- fin marine (P[9][1] -> DUR)
t = s[1]
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
js += pop("#z7", t + 2.2) + pop("#z8", t + 3.6) + pop("#z9", s[2] + .2)
js += f'tl.to("#z9",{{scale:1.06,duration:.45,yoyo:true,repeat:2,ease:"sine.inOut"}},{r2(s[2] + .8)});\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA4}{EXTRA5}{EXTRA7}</style></head><body>
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

d = ATELIER / "build" / "yt-sophro-hypno"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "avis.png", "finance.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, DUR)
