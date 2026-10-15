"""Vidéo YouTube 1920x1080 : « Sophrologue, hypnothérapeute, praticienne Reiki : 5 tâches administratives à ne plus faire le soir »
(conseil · public thérapeutes, mardi 13/10/2026).
Usage : python3 gen_therapeutes_soir.py <voix.wav>  -> build/yt-therapeutes-soir/
Temps calés sur voix/2026-10-13_yt-therapeutes-5-taches-soir.mp3 (114,5 s) : silencedetect -30 dB / 0,15 s
+ alignement des groupes de mots par nombre de syllabes (programmation dynamique).
Scènes : bureau du soir illustré (lampe, horloge 21 h, ordinateur plein de notifications), titre clair à 5 cartes,
téléphone à bulles puis grille de créneaux, relevé de règlements à cocher, pile de factures numérotées + tampon,
notes éparpillées qui se rangent dans une fiche cliente (frise), frise des annulations + règle écrite,
GuidPilot (liste qui s'allume + visuels : téléphone, facture, capture finance.png zoomée avec cercle, fiche, espace client),
citation, fin marine.
Vocabulaire thérapeutes : aucun terme médical (séance, cabinet, clientes, compte rendu de séance).
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
base = (HERE / "gen_presentation.py").read_text().split("T = dict(")[0]
ns = {"__file__": str(HERE / "gen_presentation.py")}
exec(base, ns)
CSS, ATELIER, KIT = ns["CSS"], ns["ATELIER"], ns["KIT"]
DUR = 116.0
T = dict(t=15.88, s1=20.47, s2=33.35, s3=45.97, s4=60.10, s5=70.96, g0=83.2, g1=85.7, q=101.65, end=104.22)

EXTRA = """
.hid{}
.eve{background:#0F172A;color:#fff}
.hk{position:absolute;left:120px;top:150px;width:780px}
.hk .time{font-weight:800;font-size:170px;line-height:1;letter-spacing:-.04em;color:#fff}
.hk .time span{color:#E9C46A}
.hk .s1{font-weight:600;font-size:46px;color:#CBD5E1;margin-top:30px;line-height:1.3}
.hk .s2{font-weight:800;font-size:52px;color:#fff;margin-top:22px;line-height:1.2}
.prof{position:absolute;left:120px;top:770px;width:820px;display:flex;flex-wrap:wrap;gap:16px}
.prof div{padding:14px 28px;border-radius:999px;background:#1E293B;border:2px solid #334155;font-weight:700;font-size:32px;color:#E2E8F0}
.room{position:absolute;left:960px;top:110px;width:880px;height:880px}
.illus{position:absolute;font-size:18px;font-weight:600;color:#64748B;background:#F1F5F9;border-radius:999px;padding:4px 14px;z-index:6}
.win{position:absolute;left:520px;top:20px;width:300px;height:280px;border-radius:16px;background:#1E3A8A;border:10px solid #334155}
.win:before{content:"";position:absolute;left:50%;top:0;bottom:0;width:10px;margin-left:-5px;background:#334155}
.win:after{content:"";position:absolute;top:50%;left:0;right:0;height:10px;margin-top:-5px;background:#334155}
.moon{position:absolute;left:600px;top:60px;width:70px;height:70px;border-radius:50%;background:#FDE68A;box-shadow:inset -18px -6px 0 #1E3A8A}
.wclock{position:absolute;left:150px;top:30px;width:220px;height:220px;border-radius:50%;background:#F8FAFC;border:12px solid #334155}
.wclock i{position:absolute;left:50%;top:50%;width:8px;margin-left:-4px;border-radius:4px;background:#0F172A;transform-origin:50% 100%}
.wclock .hr{height:56px;margin-top:-56px;transform:rotate(270deg)}
.wclock .mn{height:80px;margin-top:-80px;transform:rotate(0deg);background:#2563EB}
.wclock .ct{position:absolute;left:50%;top:50%;width:20px;height:20px;margin:-10px 0 0 -10px;border-radius:50%;background:#E9C46A}
.cone{position:absolute;left:-10px;top:300px;width:420px;height:520px;background:linear-gradient(180deg,rgba(233,196,106,.22),rgba(233,196,106,0));clip-path:polygon(38% 0,62% 0,100% 100%,0 100%)}
.lampb{position:absolute;left:40px;top:780px;width:150px;height:22px;border-radius:12px;background:#E9C46A}
.lampa{position:absolute;left:105px;top:330px;width:16px;height:460px;border-radius:8px;background:#94A3B8}
.lamps{position:absolute;left:30px;top:250px;width:170px;height:100px;background:#E9C46A;clip-path:polygon(25% 0,75% 0,100% 100%,0 100%)}
.lap{position:absolute;left:250px;top:400px;width:600px;height:390px;border-radius:22px 22px 0 0;background:#334155;padding:18px}
.lap .scr{position:relative;width:100%;height:100%;border-radius:8px;overflow:hidden;background:#F6F8FC;padding:22px}
.lapb{position:absolute;left:200px;top:790px;width:700px;height:24px;border-radius:0 0 24px 24px;background:#475569}
.desk{position:absolute;left:-40px;right:-40px;top:814px;height:34px;border-radius:10px;background:#7C5A34}
.nt{display:flex;align-items:center;gap:16px;background:#fff;border:2px solid #E2E8F0;border-radius:16px;padding:14px 18px;margin-bottom:14px;box-shadow:0 8px 20px rgba(15,23,42,.08)}
.nt i{font-style:normal;flex:none;width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:800;color:#fff;background:#2563EB}
.nt b{font-weight:800;font-size:26px;color:#0F172A}
.nt span{margin-left:auto;font-weight:700;font-size:20px;color:#DC2626}
.mug{position:absolute;left:880px;top:700px;width:0}
.titleT{position:absolute;left:0;right:0;top:170px;text-align:center}
.titleT .k{font-weight:700;font-size:28px;letter-spacing:.14em;color:#2563EB}
.titleT .b{font-weight:800;font-size:96px;line-height:1.05;letter-spacing:-.03em;color:#0F172A;margin-top:24px}
.titleT .b span{color:#2563EB}
.cards5{position:absolute;left:0;right:0;top:600px;display:flex;justify-content:center;gap:28px}
.c5{width:300px;height:250px;border-radius:26px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.08);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px}
.c5 b{display:flex;width:76px;height:76px;border-radius:50%;background:#0F172A;color:#fff;align-items:center;justify-content:center;font-size:38px;font-weight:800}
.c5 div{font-weight:800;font-size:32px;color:#0F172A;text-align:center;line-height:1.15}
.cons{margin-top:36px;padding:28px 32px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;border-left:10px solid #E9C46A;box-shadow:0 14px 40px rgba(15,23,42,.06)}
.cons .l{font-weight:800;font-size:24px;letter-spacing:.14em;color:#B7791F}
.cons .t{font-weight:700;font-size:36px;line-height:1.3;color:#0F172A;margin-top:10px}
.ok{display:flex;align-items:center;gap:18px;margin-top:22px;font-weight:700;font-size:34px;color:#0F172A}
.ok i{font-style:normal;flex:none;width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px;background:#DCFCE7;color:#16A34A}
.phone{position:absolute;width:460px;height:880px;border-radius:64px;background:#0F172A;padding:20px;box-shadow:0 40px 90px rgba(15,23,42,.25)}
.phone .ps{position:relative;width:100%;height:100%;border-radius:46px;background:#F6F8FC;overflow:hidden}
.phone .notch{position:absolute;left:50%;top:14px;width:120px;height:30px;margin-left:-60px;border-radius:16px;background:#0F172A;z-index:5}
.phead{height:130px;padding:62px 28px 0;background:#fff;border-bottom:2px solid #E2E8F0;font-weight:800;font-size:26px;color:#0F172A;display:flex;align-items:center;gap:14px}
.phead .av{width:44px;height:44px;border-radius:50%;background:#DBEAFE;color:#1D4ED8;font-size:20px;display:flex;align-items:center;justify-content:center}
.bub{position:absolute;max-width:300px;padding:18px 24px;border-radius:26px;font-weight:600;font-size:30px;line-height:1.25}
.bub.me{right:24px;background:#2563EB;color:#fff;border-bottom-right-radius:8px}
.bub.her{left:24px;background:#fff;color:#0F172A;border:2px solid #E2E8F0;border-bottom-left-radius:8px}
.cnt{position:absolute;left:1440px;top:330px;width:380px;padding:30px;border-radius:26px;background:#FEF2F2;border:2px solid #FECACA;text-align:center}
.cnt .n{font-weight:800;font-size:110px;line-height:1;color:#DC2626}
.cnt .l{font-weight:700;font-size:28px;color:#7F1D1D;margin-top:10px;line-height:1.3}
.slots{position:absolute;inset:0;background:#F6F8FC;padding:150px 26px 0}
.slots .tt{font-weight:800;font-size:30px;color:#0F172A}
.slots .dd{font-weight:600;font-size:22px;color:#64748B;margin-top:6px}
.sg{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:26px}
.sg div{height:72px;border-radius:16px;background:#fff;border:2px solid #E2E8F0;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:26px;color:#0F172A}
.sg div.x{color:#CBD5E1;text-decoration:line-through;background:#F1F5F9}
.sg div.on{background:#2563EB;border-color:#2563EB;color:#fff}
.noted{margin-top:30px;padding:20px;border-radius:18px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:26px;text-align:center}
.ledger{position:absolute;left:900px;top:160px;width:920px;height:820px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);padding:46px 50px}
.ledger .tt{font-weight:800;font-size:40px;color:#0F172A}
.ledger .dd{font-weight:600;font-size:24px;color:#64748B;margin-top:6px}
.lr{position:relative;display:flex;align-items:center;gap:24px;margin-top:26px;padding:24px 28px;border-radius:20px;background:#F8FAFC;border:2px solid #E2E8F0}
.lr .ic{flex:none;width:64px;height:64px;border-radius:16px;background:#EFF6FF;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:800;color:#2563EB}
.lr .a{font-weight:800;font-size:32px;color:#0F172A}
.lr .b{font-weight:600;font-size:22px;color:#64748B;margin-top:4px}
.lr .st{position:absolute;right:28px;top:50%;margin-top:-30px;height:60px;padding:0 24px;border-radius:999px;display:flex;align-items:center;font-weight:800;font-size:26px}
.st.q{background:#FEF3C7;color:#92400E}
.st.v{background:#DCFCE7;color:#15803D}
.eom{display:inline-flex;align-items:center;gap:14px;margin-top:22px;padding:16px 28px;border-radius:999px;background:#F1F5F9;color:#64748B;font-weight:800;font-size:30px;text-decoration:line-through;text-decoration-color:#DC2626;text-decoration-thickness:4px}
.warm{background:#F8F4EC}
.sheet{position:absolute;width:520px;height:700px;border-radius:14px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.12);padding:40px 44px}
.sheet .h1{font-weight:800;font-size:40px;color:#0F172A}
.sheet .no{display:inline-block;margin-top:12px;padding:8px 18px;border-radius:10px;background:#EFF6FF;color:#1D4ED8;font-weight:800;font-size:28px}
.sheet .ln{height:16px;border-radius:8px;background:#E2E8F0;margin-top:22px}
.sheet .tot{position:absolute;left:44px;right:44px;bottom:60px;height:70px;border-radius:14px;background:#F1F5F9}
.stamp{position:absolute;right:40px;top:280px;padding:14px 30px;border:6px solid #16A34A;border-radius:16px;color:#16A34A;font-weight:800;font-size:44px;letter-spacing:.08em;transform:rotate(-12deg);background:rgba(255,255,255,.85)}
.goldtag{display:inline-block;margin-top:30px;padding:16px 28px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:700;font-size:28px;align-self:flex-start}
.scat{position:absolute}
.book{width:300px;height:380px;border-radius:12px 22px 22px 12px;background:#1E3A8A;border-left:24px solid #172554;box-shadow:0 20px 50px rgba(15,23,42,.18)}
.book b{position:absolute;left:60px;top:60px;width:170px;height:60px;border-radius:8px;background:#E9C46A}
.file{width:300px;height:360px;border-radius:16px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.12);padding:34px}
.file .fn{font-weight:800;font-size:24px;color:#1D4ED8;margin-bottom:24px}
.file .ln{height:14px;border-radius:7px;background:#E2E8F0;margin-top:20px}
.msg{width:360px;padding:26px;border-radius:26px;border-bottom-left-radius:8px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.12);font-weight:600;font-size:28px;color:#0F172A;line-height:1.3}
.card{position:absolute;left:880px;top:140px;width:940px;height:840px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.card .ch{height:150px;padding:0 44px;display:flex;align-items:center;gap:26px;border-bottom:2px solid #E2E8F0}
.av{width:86px;height:86px;border-radius:50%;background:#DBEAFE;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:34px;color:#1D4ED8}
.card .nm{font-weight:800;font-size:40px}.card .sb{font-weight:600;font-size:24px;color:#64748B;margin-top:4px}
.vline{position:absolute;left:84px;top:200px;width:6px;height:330px;border-radius:3px;background:#E2E8F0;transform-origin:top center}
.ev{position:absolute;left:62px;width:820px;display:flex;align-items:center;gap:26px}
.ev .dt{flex:none;width:50px;height:50px;border-radius:50%;background:#fff;border:8px solid #2563EB}
.ev .dt.g{border-color:#16A34A}.ev .dt.p{border-color:#7C3AED}
.ev .tx{font-weight:700;font-size:30px;color:#0F172A}
.ev .sm{font-weight:600;font-size:22px;color:#64748B;margin-top:4px}
.note{position:absolute;left:40px;right:40px;bottom:36px;padding:26px 30px;border-radius:22px;background:#FBF3DC;border:2px solid #F1DFA6}
.note .nh{display:flex;align-items:center;gap:18px;font-weight:800;font-size:30px;color:#6B4E16}
.note .nl{height:14px;border-radius:7px;background:#F1DFA6;margin-top:16px}
.note .ns{font-weight:600;font-size:22px;color:#8A6A2B;margin-left:auto}
.hdr{position:absolute;left:110px;top:110px;width:1500px}
.frise{position:absolute;left:160px;top:390px;width:1600px;height:200px}
.fl{position:absolute;left:0;top:60px;width:1600px;height:10px;border-radius:5px;background:#CBD5E1;transform-origin:left center}
.fp{position:absolute;top:30px;width:70px;height:70px;margin-left:-35px;border-radius:50%;background:#fff;border:10px solid #2563EB}
.fp.gold{border-color:#E9C46A}.fp.navy{border-color:#0F172A}
.fx{position:absolute;top:120px;width:420px;margin-left:-210px;text-align:center;font-weight:800;font-size:34px;color:#0F172A}
.fx small{display:block;font-weight:600;font-size:24px;color:#64748B;margin-top:6px}
.rule{position:absolute;left:110px;top:700px;width:960px;padding:34px 44px;border-radius:28px;background:#0F172A;color:#fff}
.rule .l{font-weight:700;font-size:26px;letter-spacing:.14em;color:#E9C46A}
.rule .t{font-weight:800;font-size:48px;line-height:1.2;margin-top:12px}
.rule .t span{color:#93C5FD}
.side{position:absolute;left:1140px;top:710px;width:680px}
.gp{position:absolute;left:0;right:0;top:300px;text-align:center}
.gp .b{font-weight:800;font-size:80px;line-height:1.1;letter-spacing:-.02em;color:#fff;margin-top:50px}
.gp .b span{color:#60A5FA}
.lst{margin-top:36px}
.li{display:flex;align-items:center;gap:20px;margin:14px 0;padding:16px 22px;border-radius:18px;font-weight:700;font-size:33px;color:#94A3B8;border:2px solid transparent}
.li i{font-style:normal;flex:none;width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:26px;background:#E2E8F0;color:#64748B}
.vis{position:absolute;left:960px;top:120px;width:880px;height:880px}
.zf{position:absolute;left:10px;top:250px;width:864px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.zf .vp{position:relative;width:860px;height:240px;overflow:hidden}
.zf .vp img{position:absolute;left:-40px;top:0;width:1270px;max-width:none}
.ring{position:absolute;left:290px;top:84px;width:300px;height:114px;border:6px solid #E9C46A;border-radius:26px;box-shadow:0 0 0 9999px rgba(15,23,42,.16)}
.cap{position:absolute;left:10px;top:600px;width:864px;text-align:center;font-weight:800;font-size:40px;color:#0F172A}
.cap span{color:#2563EB}
.mini{position:absolute;left:60px;top:150px;width:760px;height:600px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.mini .ch{height:130px;padding:0 36px;display:flex;align-items:center;gap:22px;border-bottom:2px solid #E2E8F0}
.mini .r{display:flex;align-items:center;gap:20px;margin:26px 36px 0;font-weight:700;font-size:28px;color:#0F172A}
.mini .r i{flex:none;width:18px;height:18px;border-radius:50%;background:#2563EB}
.cr{margin:24px 22px 0;padding:24px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 10px 30px rgba(15,23,42,.06)}
.cr .a{font-weight:800;font-size:28px;color:#0F172A}
.cr .b{font-weight:600;font-size:21px;color:#64748B;margin-top:6px}
.cr .nw{display:inline-block;margin-top:14px;padding:6px 16px;border-radius:999px;background:#EFF6FF;color:#2563EB;font-weight:800;font-size:20px}
.btn{margin:20px 22px 0;height:76px;border-radius:18px;background:#2563EB;color:#fff;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center}
.quote{position:absolute;left:0;right:0;top:290px;text-align:center}
.quote .qm{font-weight:800;font-size:200px;line-height:.6;color:#E9C46A;height:90px}
.quote .q{font-weight:800;font-size:86px;line-height:1.12;letter-spacing:-.03em;color:#0F172A}
.quote .q span{color:#2563EB}
"""

E = "power3.out"
def pop(sel, t, ease="back.out(1.6)", y=30):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{t});\n'
def fin(sel, t, x=120):
    return f'tl.fromTo("{sel}",{{opacity:0,x:{x},scale:.96}},{{opacity:1,x:0,scale:1,duration:.7,ease:"{E}"}},{t});\n'
def out(sel, t, d=.4):
    return f'tl.to("{sel}",{{opacity:0,duration:{d}}},{t});\n'
def lion(sel, t):
    return (f'tl.to("{sel}",{{color:"#0F172A",backgroundColor:"#FFFFFF",borderColor:"#E2E8F0",boxShadow:"0 10px 30px rgba(15,23,42,.08)",duration:.35}},{t});\n'
            f'tl.to("{sel} i",{{backgroundColor:"#2563EB",color:"#FFFFFF",duration:.35}},{t});\n'
            f'tl.fromTo("{sel}",{{scale:.96}},{{scale:1,duration:.35,ease:"back.out(2)"}},{t});\n')
def chap(id_, n, txt, title, t):
    return (f'<div class="chap hid" id="{id_}c"><b>{n}</b>{txt}</div><div class="h hid" id="{id_}h">{title}</div>',
            pop(f"#{id_}c", t + .1, E) + pop(f"#{id_}h", t + .3, E, 40))
def phone(id_, inner, left, top):
    return (f'<div class="phone hid" id="{id_}" style="left:{left}px;top:{top}px"><div class="ps"><div class="notch"></div>{inner}</div>'
            f'<span class="illus" style="left:150px;bottom:-50px">Illustration</span></div>')

LOGO = '<img class="logo-corner" src="assets/logo_couleur.png" alt="GuidPilot" />'
body, js = "", ""

# ---------- A : 21 h, le bureau du soir (0 -> 15.88)
notes = [("@", "3 messages à confirmer", "!"), ("€", "Paiements à vérifier", "?"), ("F", "Factures à préparer", "4")]
nts = "".join(f'<div class="nt hid" id="an{i}"><i>{a}</i><b>{b}</b><span>{c}</span></div>' for i, (a, b, c) in enumerate(notes))
body += f'''
<div id="a" class="clip eve" data-start="0" data-duration="{T['t']}" data-track-index="1">
  <div class="hk"><div class="time hid" id="at">21 h<span>00</span></div>
    <div class="s1 hid" id="as1">Votre dernière séance est terminée depuis longtemps…</div>
    <div class="s2 hid" id="as2">et vous êtes encore devant votre ordinateur.</div></div>
  <div class="prof"><div class="hid" id="ap0">Sophrologue</div><div class="hid" id="ap1">Hypnothérapeute</div>
    <div class="hid" id="ap2">Praticienne Reiki</div><div class="hid" id="ap3">Réflexologue</div></div>
  <div class="room hid" id="aroom"><span class="illus" style="left:0;top:-50px">Illustration</span>
    <div class="win"></div><div class="moon"></div>
    <div class="wclock"><i class="hr"></i><i class="mn"></i><div class="ct"></div></div>
    <div class="cone hid" id="acone"></div><div class="lampa"></div><div class="lamps"></div><div class="lampb"></div>
    <div class="lap"><div class="scr">{nts}</div></div><div class="lapb"></div><div class="desk"></div></div>
</div>'''
js += 'tl.fromTo("#at",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.7,ease:"back.out(1.6)"},0.1);\n'
js += fin("#aroom", 0.4) + 'tl.fromTo("#acone",{opacity:0},{opacity:1,duration:1.2},1.2);\n'
js += pop("#as1", 1.0, E) + pop("#as2", 3.4, E)
js += pop("#an0", 5.38) + pop("#an1", 6.59) + pop("#an2", 7.78)
js += pop("#ap0", 9.01) + pop("#ap1", 10.1) + pop("#ap2", 11.47) + pop("#ap3", 12.6)
js += 'tl.to(".nt span",{scale:1.25,duration:.25,yoyo:true,repeat:3,ease:"sine.inOut"},13.6);\n'

# ---------- T : titre (15.88 -> 20.47)
cards = ["Rendez-vous", "Paiements", "Factures", "Notes de<br/>séance", "Annulations"]
c5 = "".join(f'<div class="c5 hid" id="tc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, t in enumerate(cards))
body += f'''
<div id="t" class="clip light" data-start="{T['t']}" data-duration="{round(T['s1'] - T['t'], 2)}" data-track-index="1">
  {LOGO}
  <div class="titleT hid" id="tt"><div class="k">SOPHROLOGUES · HYPNOTHÉRAPEUTES · PRATICIENNES REIKI</div>
    <div class="b">5 tâches à ne plus faire<br/><span>le soir</span></div></div>
  <div class="cards5">{c5}</div>
</div>'''
js += 'tl.fromTo("#tt",{opacity:0,y:40},{opacity:1,y:0,duration:.7,ease:"back.out(1.4)"},16.0);\n'
js += "".join(pop(f"#tc{i}", 17.0 + i * .5, y=50) for i in range(5))

# ---------- 1 : rendez-vous (20.47 -> 33.35)
h1, j1 = chap("s1", 1, "Les rendez-vous", "Un créneau,<br/><span>message après message</span>", T['s1'])
bubs = [("me", "Mardi ?", 170, 23.66), ("her", "Plutôt jeudi.", 270, 24.26), ("me", "10 h ?", 370, 25.07), ("her", "Plutôt 11 h.", 470, 25.79)]
bh = "".join(f'<div class="bub {c} hid" id="b{i}" style="top:{y}px">{t}</div>' for i, (c, t, y, _) in enumerate(bubs))
slots = ('<div class="slots hid" id="sl"><div class="tt">Choisissez votre créneau</div><div class="dd">Séance individuelle · 1 h</div>'
         '<div class="sg"><div class="x">Mar. 10:00</div><div>Mar. 14:00</div><div>Jeu. 10:00</div><div id="slon">Jeu. 11:00</div>'
         '<div class="x">Ven. 9:00</div><div>Ven. 16:00</div></div><div class="noted hid" id="sln">✓ Rendez-vous noté</div></div>')
inner = f'<div class="phead"><div class="av">CR</div>Camille R.</div>{bh}{slots}'
body += f'''
<div id="s1" class="clip light" data-start="{T['s1']}" data-duration="{round(T['s2'] - T['s1'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:760px">{h1}
    <div class="cons hid" id="s1k"><div class="l">LE CONSEIL</div><div class="t">Laissez vos clientes choisir elles&#8209;mêmes un créneau libre.</div></div>
    <div class="ok hid" id="s1o1"><i>✓</i>Plus d'allers-retours</div>
    <div class="ok hid" id="s1o2"><i>✓</i>Le rendez-vous est noté au bon endroit</div></div>
  {phone("s1p", inner, 960, 110)}
  <div class="cnt hid" id="s1n"><div class="n">4</div><div class="l">messages<br/>pour un seul rendez&#8209;vous</div></div>
</div>'''
js += j1 + fin("#s1p", 20.7)
js += "".join(pop(f"#b{i}", t, y=20) for i, (_, _, _, t) in enumerate(bubs))
js += pop("#s1n", 26.3) + out("#s1n", 27.4)
js += pop("#s1k", 27.52, E) + 'tl.fromTo("#sl",{opacity:0,y:60},{opacity:1,y:0,duration:.6,ease:"power3.out"},28.0);\n'
js += 'tl.to("#slon",{backgroundColor:"#2563EB",borderColor:"#2563EB",color:"#FFFFFF",duration:.3},29.3);\n'
js += 'tl.fromTo("#slon",{scale:1},{scale:1.08,duration:.2,yoyo:true,repeat:1},29.3);\n'
js += pop("#s1o1", 30.06) + pop("#s1o2", 31.06) + pop("#sln", 31.3)

# ---------- 2 : paiements (33.35 -> 45.97)
h2, j2 = chap("s2", 2, "Les paiements", "Qui a payé ?<br/><span>Le recoupement du soir</span>", T['s2'])
rows = [("V", "Virement · Sophie L.", "Séance du 6 octobre"), ("E", "Espèces · Nadia B.", "Séance du 8 octobre"), ("C", "Chèque · Camille R.", "Séance du 9 octobre")]
rh = "".join(f'<div class="lr hid" id="r{i}"><div class="ic">{a}</div><div><div class="a">{b}</div><div class="b">{c}</div></div>'
             f'<div class="st q" id="rq{i}">À vérifier ?</div><div class="st v hid" id="rv{i}">✓ Noté le jour même</div></div>' for i, (a, b, c) in enumerate(rows))
body += f'''
<div id="s2" class="clip light" data-start="{T['s2']}" data-duration="{round(T['s3'] - T['s2'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px">{h2}
    <div class="cons hid" id="s2k"><div class="l">LE CONSEIL</div><div class="t">Demandez le règlement au moment de la réservation.</div></div>
    <div class="ok hid" id="s2o"><i>✓</i>Chaque paiement noté le jour même</div>
    <div class="eom hid" id="s2e">En fin de mois</div></div>
  <div class="ledger hid" id="s2l"><span class="illus" style="right:30px;top:30px">Illustration</span>
    <div class="tt">Mes règlements</div><div class="dd">Octobre</div>{rh}</div>
</div>'''
js += j2 + fin("#s2l", 33.6)
js += pop("#r0", 35.67) + pop("#r1", 36.34) + pop("#r2", 37.63)
js += 'tl.to(".st.q",{x:-8,duration:.08,yoyo:true,repeat:5},38.7);\n'
js += pop("#s2k", 39.46, E) + pop("#s2o", 42.94)
js += "".join(out(f"#rq{i}", 43.1 + i * .3, .2) + pop(f"#rv{i}", 43.1 + i * .3, y=10) for i in range(3))
js += pop("#s2e", 44.66)

# ---------- 3 : factures (45.97 -> 60.10)
h3, j3 = chap("s3", 3, "Les factures", "Une facture<br/><span>par séance</span>", T['s3'])
def sheet(i, no, left, top, rot, extra="", hid=" hid"):
    lines = "".join(f'<div class="ln" style="width:{w}%"></div>' for w in (90, 70, 85, 60, 75))
    return (f'<div class="sheet{hid}" id="f{i}" style="left:{left}px;top:{top}px;transform:rotate({rot}deg)">'
            f'<div class="h1">Facture</div><div class="no">N° {no}</div>{lines}<div class="tot"></div>{extra}</div>')
stamp = '<div class="stamp hid" id="fst">RÉGLÉE</div>'
body += f'''
<div id="s3" class="clip warm" data-start="{T['s3']}" data-duration="{round(T['s4'] - T['s3'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px">{h3}
    <div class="cons hid" id="s3k"><div class="l">LE CONSEIL</div><div class="t">Un seul modèle, et la facture éditée dès que la séance est réglée.</div></div>
    <div class="goldtag hid" id="s3g">Règles précises : votre expert-comptable</div></div>
  <div style="position:absolute;left:960px;top:150px;width:860px;height:860px"><span class="illus" style="left:0;top:-40px">Illustration</span>
    {sheet(0, "2026-041", 40, 90, -8)}{sheet(1, "2026-042", 170, 60, 3)}{sheet(2, "2026-043", 300, 110, -2, stamp)}</div>
</div>'''
js += j3
js += 'tl.fromTo("#f0",{opacity:0,y:-200},{opacity:1,y:0,duration:.6,ease:"power3.out"},47.02);\n'
js += 'tl.fromTo("#f1",{opacity:0,y:-200},{opacity:1,y:0,duration:.6,ease:"power3.out"},48.29);\n'
js += 'tl.fromTo("#f2",{opacity:0,y:-200},{opacity:1,y:0,duration:.6,ease:"power3.out"},49.0);\n'
js += 'tl.to(".sheet .no",{backgroundColor:"#2563EB",color:"#FFFFFF",duration:.3,stagger:.35},49.4);\n'
js += pop("#s3k", 51.02, E)
js += 'tl.fromTo("#fst",{opacity:0,scale:2.2},{opacity:1,scale:1,duration:.35,ease:"power4.in"},53.9);\n'
js += pop("#s3g", 55.92)

# ---------- 4 : notes de séance (60.10 -> 70.96)
h4, j4 = chap("s4", 4, "Les notes de séance", "Où sont<br/><span>mes notes ?</span>", T['s4'])
lock = '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#6B4E16" stroke-width="2.2" stroke-linecap="round"><rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
evs = [("dt", "Séance découverte · 1 h", "2 septembre · Au cabinet", 230), ("dt p", "Séance de sophrologie · 1 h", "23 septembre · Au cabinet", 330),
       ("dt g", "Séance de suivi · 1 h", "Aujourd'hui · 18:00", 430)]
evh = "".join(f'<div class="ev hid" id="e{i}" style="top:{top}px"><div class="{c}"></div><div><div class="tx">{a}</div><div class="sm">{b}</div></div></div>'
              for i, (c, a, b, top) in enumerate(evs))
body += f'''
<div id="s4" class="clip light" data-start="{T['s4']}" data-duration="{round(T['s5'] - T['s4'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px">{h4}
    <div class="cons hid" id="s4k"><div class="l">LE CONSEIL</div><div class="t">Une seule fiche par cliente.</div></div>
    <div class="ok hid" id="s4o"><i>✓</i>Tout au même endroit</div></div>
  <div class="scat hid" id="x0" style="left:980px;top:200px;transform:rotate(-6deg)"><div class="book"><b></b></div></div>
  <div class="scat hid" id="x1" style="left:1420px;top:150px;transform:rotate(5deg)"><div class="file"><div class="fn">notes_camille.docx</div>
    <div class="ln"></div><div class="ln" style="width:70%"></div><div class="ln"></div><div class="ln" style="width:55%"></div></div></div>
  <div class="scat hid" id="x2" style="left:1250px;top:640px;transform:rotate(-3deg)"><div class="msg">Note : penser à revoir l'exercice de respiration</div></div>
  <div class="card hid" id="s4card"><span class="illus" style="right:30px;top:24px">Illustration</span>
    <div class="ch"><div class="av">CR</div><div><div class="nm">Camille R.</div><div class="sb">Cliente depuis septembre · 3 séances</div></div></div>
    <div class="vline hid" id="evl"></div>{evh}
    <div class="note hid" id="s4n"><div class="nh">{lock}Notes personnelles<span class="ns">Visibles uniquement par vous</span></div>
      <div class="nl" style="width:90%"></div><div class="nl" style="width:65%"></div></div></div>
</div>'''
js += j4
js += 'tl.fromTo("#x0",{opacity:0,scale:.6},{opacity:1,scale:1,duration:.45,ease:"back.out(1.8)"},63.19);\n'
js += 'tl.fromTo("#x1",{opacity:0,scale:.6},{opacity:1,scale:1,duration:.45,ease:"back.out(1.8)"},63.75);\n'
js += 'tl.fromTo("#x2",{opacity:0,scale:.6},{opacity:1,scale:1,duration:.45,ease:"back.out(1.8)"},64.35);\n'
js += pop("#s4k", 65.31, E)
js += 'tl.to(["#x0","#x1","#x2"],{x:120,y:60,scale:.3,opacity:0,duration:.6,ease:"power2.in",stagger:.08},65.6);\n'
js += 'tl.fromTo("#s4card",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.6,ease:"back.out(1.4)"},66.04);\n'
js += 'tl.fromTo("#evl",{opacity:1,scaleY:0},{opacity:1,scaleY:1,duration:1.6,ease:"power1.inOut"},66.5);\n'
js += pop("#e0", 66.6) + pop("#e1", 67.2) + pop("#e2", 67.8) + pop("#s4n", 68.6, y=50)
js += pop("#s4o", 70.16)

# ---------- 5 : annulations (70.96 -> 83.2)
body += f'''
<div id="s5" class="clip light" data-start="{T['s5']}" data-duration="{round(T['g0'] - T['s5'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr"><div class="chap hid" id="s5c"><b>5</b>Les annulations</div>
    <div class="h hid" id="s5h">La dernière minute, <span>avec une règle claire</span></div></div>
  <div class="frise"><div class="fl hid" id="s5l"></div>
    <div class="fp hid" id="p0" style="left:0"></div><div class="fx hid" id="px0" style="left:-35px;margin-left:0;text-align:left">Réservation<small>la règle est déjà affichée</small></div>
    <div class="fp gold hid" id="p1" style="left:1100px"></div><div class="fx hid" id="px1" style="left:1100px">24 h avant<small>dernier report possible</small></div>
    <div class="fp navy hid" id="p2" style="left:1600px"></div><div class="fx hid" id="px2" style="left:1635px;margin-left:-420px;text-align:right">La séance<small>à l'heure prévue</small></div></div>
  <div class="rule hid" id="s5r"><div class="l">MA RÈGLE, ÉCRITE</div><div class="t">Report possible jusqu'à <span>24 h avant</span> la séance.</div></div>
  <div class="side"><div class="ok hid" id="s5o1"><i>✓</i>Connue avant la réservation</div>
    <div class="ok hid" id="s5o2"><i>✓</i>La même règle pour tout le monde</div></div>
</div>'''
js += pop("#s5c", 71.06, E) + pop("#s5h", 71.3, E, 40)
js += 'tl.fromTo("#s5l",{opacity:1,scaleX:0},{opacity:1,scaleX:1,duration:2.2,ease:"power1.inOut"},72.0);\n'
js += pop("#p0", 72.0) + pop("#px0", 72.2) + pop("#p1", 73.2) + pop("#px1", 73.4) + pop("#p2", 74.0) + pop("#px2", 74.2)
js += 'tl.fromTo("#s5r",{opacity:0,y:60},{opacity:1,y:0,duration:.6,ease:"back.out(1.4)"},74.92);\n'
js += 'tl.to("#p1",{scale:1.3,duration:.3,yoyo:true,repeat:3},76.6);\n'
js += pop("#s5o1", 79.42) + pop("#s5o2", 81.52)

# ---------- 6 : GuidPilot (83.2 -> 101.65)
items = ["Réservation et paiement en ligne", "Une facture à chaque paiement", "Ce qui reste à encaisser", "Fiche cliente et notes privées", "Compte rendu dans l'espace client"]
lis = "".join(f'<div class="li" id="l{i}"><i>{i + 1}</i>{t}</div>' for i, t in enumerate(items))
v1 = phone("v1", '<div class="slots" style="padding-top:110px"><div class="tt">Séance individuelle · 1 h</div><div class="dd">Jeudi 15 octobre</div>'
              '<div class="sg"><div>10:00</div><div class="on">11:00</div><div>14:00</div><div>16:00</div></div>'
              '<div class="btn" style="margin:30px 0 0">Réserver et payer</div><div class="noted">✓ Paiement reçu</div></div>', 210, 0)
v2 = ('<div class="hid" id="v2" style="position:absolute;left:0;top:0;width:880px;height:880px"><span class="illus" style="left:180px;top:20px">Illustration</span>'
      + sheet(9, "2026-044", 180, 80, 0, '<div class="stamp" style="top:300px">PAYÉE</div>', "") + '</div>')
v3 = ('<div class="hid" id="v3" style="position:absolute;inset:0"><div class="zf"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>'
      '<span class="demo">Compte de démonstration</span></div><div class="vp"><img src="assets/finance.png" alt="" /><div class="ring hid" id="v3r"></div></div></div>'
      '<div class="cap">Votre tableau de bord :<br/><span>ce qui reste à encaisser</span></div></div>')
v4 = (f'<div class="hid" id="v4" style="position:absolute;inset:0"><div class="mini"><span class="illus" style="right:24px;top:20px">Illustration</span>'
      f'<div class="ch"><div class="av">CR</div><div><div class="nm" style="font-weight:800;font-size:36px">Camille R.</div><div style="font-weight:600;font-size:22px;color:#64748B">3 séances</div></div></div>'
      f'<div class="r"><i></i>Historique des séances</div><div class="r"><i></i>Paiements et factures</div><div class="r"><i></i>Messages échangés</div>'
      f'<div class="note" style="bottom:30px"><div class="nh">{lock}Notes privées</div><div class="ns" style="margin:8px 0 0 58px">Jamais visibles par votre cliente</div>'
      f'<div class="nl" style="width:85%"></div></div></div></div>')
v5 = phone("v5", '<div class="phead">Mon espace</div>'
              '<div class="cr"><div class="a">Compte rendu de séance</div><div class="b">Séance de suivi · 13 octobre</div><div class="nw">Nouveau</div></div>'
              '<div class="cr"><div class="a">Mes factures</div><div class="b">3 documents</div></div>'
              '<div class="cr"><div class="a">Messagerie</div><div class="b">Échanger avec votre praticienne</div></div>'
              '<div class="btn">Lire le compte rendu</div>', 210, 0)
body += f'''
<div id="g0" class="clip navy" data-start="{T['g0']}" data-duration="{round(T['g1'] - T['g0'], 2)}" data-track-index="1">
  <div class="gp hid" id="gpi"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:440px" />
    <div class="b">C'est exactement pour cela<br/><span>que GuidPilot existe</span></div></div>
</div>
<div id="g1" class="clip light" data-start="{T['g1']}" data-duration="{round(T['q'] - T['g1'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:800px"><div class="chap"><b>✓</b>Avec GuidPilot</div><div class="lst">{lis}</div></div>
  <div class="vis">{v1}{v2}{v3}{v4}{v5}</div>
</div>'''
js += 'tl.fromTo("#gpi",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},83.3);\n'
vt = [85.7, 87.73, 89.7, 92.33, 97.17]
for i, t in enumerate(vt):
    js += lion(f"#l{i}", t)
    js += f'tl.fromTo("#v{i + 1}",{{opacity:0,x:80}},{{opacity:1,x:0,duration:.5,ease:"{E}"}},{t});\n'
    if i < 4:
        js += out(f"#v{i + 1}", vt[i + 1] - .35, .3)
js += pop("#v3r", 90.6) + 'tl.to("#v3r",{scale:1.05,duration:.3,yoyo:true,repeat:3},91.0);\n'

# ---------- citation (101.65 -> 104.22) puis fin (104.22 -> DUR)
body += f'''
<div id="q" class="clip light" data-start="{T['q']}" data-duration="{round(T['end'] - T['q'], 2)}" data-track-index="1">
  {LOGO}
  <div class="quote"><div class="qm hid" id="qm">“</div>
    <div class="q hid" id="qq">Moins d'administratif le soir,<br/><span>plus de temps pour vous.</span></div></div>
</div>
<div id="z" class="clip navy" data-start="{T['end']}" data-duration="{round(DUR - T['end'], 2)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard hid" id="z7">✓ Sans carte bancaire</div>
    <div class="url hid" id="z8">guidpilot.fr</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += pop("#qm", 101.7, E) + 'tl.fromTo("#qq",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},101.8);\n'
js += 'tl.fromTo("#z6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},104.3);\n'
js += pop("#z7", 107.43) + pop("#z8", 108.75) + pop("#z9", 110.12)
js += 'tl.to("#z9",{scale:1.06,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"},111.2);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}</style></head><body>
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

d = ATELIER / "build" / "yt-therapeutes-soir"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for a in ("finance.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
