"""Vidéo YouTube 1920x1080 : « Le tableau de bord GuidPilot : où en est votre activité en 30 secondes » (tuto/promo).
Usage : python3 gen_tableau_de_bord.py <voix.wav>  -> build/yt-tableau-de-bord/
Temps calés sur voix/2026-10-12_yt-tableau-de-bord.mp3 (103,5 s) : silencedetect -32 dB / 0,1 s + alignement
des groupes de mots par nombre de syllabes (programmation dynamique).
Scènes : bureau du matin illustré (café, horloge, ordinateur), titre marine à puces, gros plans zoomés sur dash.png
avec cercle de mise en valeur (4 cartes, suivi financier, agenda + actions rapides), chiffre animé « À encaisser »,
clic curseur, liste à cocher, fiche cliente illustrée en frise, chronomètre 30 s + routine cochée, citation, fin.
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
base = (HERE / "gen_presentation.py").read_text().split("T = dict(")[0]
ns = {"__file__": str(HERE / "gen_presentation.py")}
exec(base, ns)
CSS, ATELIER, KIT = ns["CSS"], ns["ATELIER"], ns["KIT"]
DUR = 106.0
T = dict(a2=15.0, b=21.45, c=37.0, d=53.65, e=66.45, f=78.45, g=90.0, h=93.3)
IW, IH = 1270, 1122  # dash.png

EXTRA = """
.warm{background:#F8F4EC}
.hk{position:absolute;left:120px;top:190px;width:760px}
.hk .time{font-weight:800;font-size:150px;line-height:1;letter-spacing:-.04em;color:#0F172A}
.hk .s1{font-weight:600;font-size:46px;color:#475569;margin-top:26px;line-height:1.3}
.hk .q{font-weight:800;font-size:62px;line-height:1.12;letter-spacing:-.02em;color:#0F172A;margin-top:56px}
.hk .q span{color:#2563EB}
.hchips{display:flex;flex-wrap:wrap;gap:16px;margin-top:40px}
.hchips div{padding:16px 28px;border-radius:999px;background:#fff;border:2px solid #E2E8F0;font-weight:700;font-size:32px;color:#0F172A;box-shadow:0 8px 24px rgba(15,23,42,.06)}
.hchips div b{color:#2563EB}
.scene{position:absolute;left:930px;top:120px;width:900px;height:860px}
.lap{position:absolute;left:150px;top:400px;width:640px;height:400px;border-radius:22px 22px 0 0;background:#1E293B;padding:18px}
.lap .scr{position:relative;width:100%;height:100%;border-radius:8px;overflow:hidden;background:#F6F8FC}
.lap .scr img{position:absolute;left:0;top:0;width:604px}
.lapb{position:absolute;left:90px;top:800px;width:760px;height:26px;border-radius:0 0 26px 26px;background:#334155}
.desk{position:absolute;left:-40px;right:-40px;top:826px;height:34px;border-radius:10px;background:#C9A574}
.win{position:absolute;left:470px;top:0;width:330px;height:300px;border-radius:16px;background:#DBEAFE;border:10px solid #fff;box-shadow:0 10px 30px rgba(15,23,42,.08)}
.win:before{content:"";position:absolute;left:50%;top:0;bottom:0;width:10px;margin-left:-5px;background:#fff}
.win:after{content:"";position:absolute;top:50%;left:0;right:0;height:10px;margin-top:-5px;background:#fff}
.sun{position:absolute;left:520px;top:190px;width:90px;height:90px;border-radius:50%;background:#FDE68A}
.wclock{position:absolute;left:90px;top:30px;width:230px;height:230px;border-radius:50%;background:#fff;border:12px solid #0F172A;box-shadow:0 10px 30px rgba(15,23,42,.1)}
.wclock i{position:absolute;left:50%;top:50%;width:8px;margin-left:-4px;border-radius:4px;background:#0F172A;transform-origin:50% 100%}
.wclock .hr{height:58px;margin-top:-58px;transform:rotate(255deg)}
.wclock .mn{height:82px;margin-top:-82px;transform:rotate(180deg);background:#2563EB}
.wclock .ct{position:absolute;left:50%;top:50%;width:20px;height:20px;margin:-10px 0 0 -10px;border-radius:50%;background:#E9C46A}
.mug{position:absolute;left:0;top:700px;width:120px;height:126px;border-radius:0 0 30px 30px;background:#fff;border:6px solid #0F172A}
.mug:after{content:"";position:absolute;right:-50px;top:22px;width:44px;height:56px;border:10px solid #0F172A;border-left:none;border-radius:0 30px 30px 0}
.mug b{position:absolute;left:18px;right:18px;top:40px;height:10px;border-radius:5px;background:#E9C46A}
.steam{position:absolute;top:590px;width:14px;height:90px;border-radius:7px;background:rgba(100,116,139,.35)}
.plant{position:absolute;left:800px;top:660px;width:90px;height:110px;border-radius:0 0 18px 18px;background:#0F172A}
.leaf{position:absolute;width:44px;height:90px;border-radius:44px 0;background:#16A34A;opacity:.75}
.demo2{position:absolute;right:10px;top:8px;font-size:15px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:2px 10px;z-index:3}
.illus{position:absolute;font-size:18px;font-weight:600;color:#64748B;background:#F1F5F9;border-radius:999px;padding:4px 14px}
.titleA{position:absolute;left:0;right:0;top:220px;text-align:center;color:#fff}
.chips4{position:absolute;left:0;right:0;top:640px;display:flex;justify-content:center;gap:26px}
.c5{padding:22px 36px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:700;font-size:34px;display:flex;align-items:center;gap:16px}
.c5 b{display:inline-flex;width:48px;height:48px;border-radius:50%;background:#2563EB;color:#fff;align-items:center;justify-content:center;font-size:26px}
.zf{position:absolute;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.zf .vp{position:relative;overflow:hidden}
.zf .vp img{position:absolute;left:0;top:0;width:1270px;max-width:none;transform-origin:0 0}
.ring{position:absolute;left:0;top:0;border:6px solid #E9C46A;border-radius:26px;box-shadow:0 0 0 9999px rgba(15,23,42,.18);z-index:4}
.lst{margin-top:40px}
.li{display:flex;align-items:center;gap:20px;margin:16px 0;padding:16px 22px;border-radius:18px;font-weight:700;font-size:36px;color:#94A3B8;border:2px solid transparent}
.li i{font-style:normal;flex:none;width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:26px;background:#E2E8F0;color:#64748B}
.li.on{color:#0F172A;background:#fff;border-color:#E2E8F0;box-shadow:0 10px 30px rgba(15,23,42,.06)}
.li.on i{background:#2563EB;color:#fff}
.hdr{position:absolute;left:110px;top:100px;display:flex;align-items:center;gap:36px}
.hdr .h{margin-top:0;font-size:62px}
.statc{position:absolute;left:110px;top:720px;width:900px;height:260px;border-radius:28px;background:#0F172A;color:#fff;padding:40px 50px}
.statc .l{font-weight:700;font-size:30px;color:#E9C46A;letter-spacing:.1em;text-transform:uppercase}
.statc .n{font-weight:800;font-size:120px;letter-spacing:-.03em;line-height:1.1;margin-top:10px}
.why{position:absolute;left:1070px;top:740px;width:740px}
.why .w1{font-weight:800;font-size:46px;line-height:1.2;color:#0F172A}
.why .w1 span{color:#2563EB}
.why .w2{margin-top:26px;display:inline-block;padding:16px 28px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:800;font-size:30px}
.cursor{position:absolute;width:48px;height:48px;z-index:30}
.colr{position:absolute;left:1210px;top:0;bottom:0;width:620px;display:flex;flex-direction:column;justify-content:center}
.ck{display:flex;align-items:center;gap:20px;margin:14px 0;font-weight:700;font-size:36px;color:#0F172A}
.ck i{font-style:normal;flex:none;width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px;background:#DCFCE7;color:#16A34A}
.card{position:absolute;left:880px;top:130px;width:940px;height:860px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.card .ch{height:150px;padding:0 44px;display:flex;align-items:center;gap:26px;border-bottom:2px solid #E2E8F0}
.av{width:86px;height:86px;border-radius:50%;background:#DBEAFE;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:34px;color:#1D4ED8}
.card .nm{font-weight:800;font-size:40px}.card .st{font-weight:600;font-size:24px;color:#64748B;margin-top:4px}
.tabs{display:flex;gap:12px;padding:22px 44px 0}
.tabs div{padding:10px 22px;border-radius:999px;font-weight:700;font-size:22px;color:#64748B;background:#F1F5F9}
.tabs .on{background:#0F172A;color:#fff}
.vline{position:absolute;left:84px;top:290px;width:6px;height:390px;border-radius:3px;background:#E2E8F0;transform-origin:top center}
.ev{position:absolute;left:62px;width:820px;display:flex;align-items:center;gap:26px}
.ev .dt{flex:none;width:50px;height:50px;border-radius:50%;background:#fff;border:8px solid #2563EB}
.ev .dt.g{border-color:#16A34A}.ev .dt.p{border-color:#7C3AED}.ev .dt.o{border-color:#E9C46A}
.ev .tx{font-weight:700;font-size:30px;color:#0F172A}
.ev .sm{font-weight:600;font-size:22px;color:#64748B;margin-top:4px}
.badge{margin-left:auto;padding:8px 18px;border-radius:999px;font-weight:800;font-size:20px}
.b-ok{background:#DCFCE7;color:#15803D}.b-bl{background:#EFF6FF;color:#2563EB}
.note{position:absolute;left:40px;right:40px;bottom:36px;padding:26px 30px;border-radius:22px;background:#FBF3DC;border:2px solid #F1DFA6;display:flex;align-items:center;gap:22px}
.note .nt{font-weight:800;font-size:30px;color:#6B4E16}.note .ns{font-weight:600;font-size:23px;color:#8A6A2B;margin-top:4px}
.eye{position:absolute;left:110px;top:800px;display:inline-flex;align-items:center;gap:16px;padding:18px 30px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:32px}
.watch{position:absolute;left:170px;top:210px;width:620px;height:620px}
.watch .num{position:absolute;left:0;right:0;top:215px;text-align:center;font-weight:800;font-size:170px;letter-spacing:-.04em;color:#fff}
.watch .lab{position:absolute;left:0;right:0;top:420px;text-align:center;font-weight:700;font-size:34px;color:#94A3B8;letter-spacing:.12em}
.rout{position:absolute;left:900px;top:200px;width:900px}
.rout .t1{font-weight:700;font-size:30px;letter-spacing:.16em;color:#E9C46A}
.rout .h{color:#fff;font-size:76px}
.rout .h span{color:#60A5FA}
.rk{display:flex;align-items:center;gap:26px;margin:30px 0;font-weight:700;font-size:46px;color:#fff}
.rk i{font-style:normal;flex:none;width:70px;height:70px;border-radius:50%;background:#1E293B;border:3px solid #334155;color:#fff;display:flex;align-items:center;justify-content:center;font-size:34px}
.rk.on i{background:#16A34A;border-color:#16A34A}
.clear{margin-top:40px;display:inline-block;padding:18px 36px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:800;font-size:36px}
.quote{position:absolute;left:0;right:0;top:250px;text-align:center}
.quote .qm{font-weight:800;font-size:200px;line-height:.6;color:#E9C46A;height:90px}
.quote .q{font-weight:800;font-size:84px;line-height:1.12;letter-spacing:-.03em;color:#0F172A}
.quote .q span{color:#2563EB}
.quote .s{display:inline-block;margin-top:50px;padding:18px 40px;border-radius:999px;background:#0F172A;color:#fff;font-weight:700;font-size:36px}
"""

def view(rx, ry, rw, rh, VW, VH, smax=1.9):
    s = min(VW / rw, VH / rh, smax)
    s = max(s, VW / IW, VH / IH)
    cx, cy = rx + rw / 2, ry + rh / 2
    x = min(0, max(VW - IW * s, VW / 2 - cx * s))
    y = min(0, max(VH - IH * s, VH / 2 - cy * s))
    return round(x, 1), round(y, 1), round(s, 4)

def ring_box(rect, v, pad=10):
    x, y, s = v
    rx, ry, rw, rh = rect
    return dict(x=round(x + rx * s - pad, 1), y=round(y + ry * s - pad, 1), width=round(rw * s + 2 * pad), height=round(rh * s + 2 * pad))

def zframe(id_, left, top, VW, VH):
    return (f'<div class="zf" id="{id_}" style="left:{left}px;top:{top}px;width:{VW + 4}px"><div class="bar"><span class="dot"></span><span class="dot"></span>'
            f'<span class="dot"></span><span class="demo">Compte de démonstration</span></div>'
            f'<div class="vp" style="width:{VW}px;height:{VH}px"><img id="{id_}i" src="assets/dash.png" alt="" />'
            f'<div class="ring" id="{id_}r"></div></div></div>')

E = "power3.out"
def pop(sel, t, ease="back.out(1.6)", y=30):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{t});\n'
def fin(sel, t, x=120):
    return f'tl.fromTo("{sel}",{{opacity:0,x:{x},scale:.96}},{{opacity:1,x:0,scale:1,duration:.7,ease:"{E}"}},{t});\n'
def zset(id_, v, t):
    return f'tl.set("#{id_}i",{{x:{v[0]},y:{v[1]},scale:{v[2]}}},{t});\n'
def zto(id_, v, t, d=1.0):
    return f'tl.to("#{id_}i",{{x:{v[0]},y:{v[1]},scale:{v[2]},duration:{d},ease:"power2.inOut"}},{t});\n'
def rset(id_, box, t):
    return f'tl.set("#{id_}r",{box},{t});\n'.replace("'", "")
def rto(id_, box, t, d=.6):
    b = dict(box); b["duration"] = d
    return f'tl.to("#{id_}r",{b},{t});\n'.replace("'", "")
def ron(id_, t):
    return f'tl.fromTo("#{id_}r",{{opacity:0,scale:1.15}},{{opacity:1,scale:1,duration:.45,ease:"back.out(1.6)"}},{t});\n'
def lion(sel, t):
    return (f'tl.to("{sel}",{{color:"#0F172A",backgroundColor:"#FFFFFF",borderColor:"#E2E8F0",boxShadow:"0 10px 30px rgba(15,23,42,.08)",duration:.35}},{t});\n'
            f'tl.to("{sel} i",{{backgroundColor:"#2563EB",color:"#FFFFFF",duration:.35}},{t});\n'
            f'tl.fromTo("{sel}",{{scale:.96}},{{scale:1,duration:.35,ease:"back.out(2)"}},{t});\n')
def rkon(sel, t):
    return f'tl.to("{sel} i",{{backgroundColor:"#16A34A",borderColor:"#16A34A",duration:.35}},{t});\n'

LOGO = '<img class="logo-corner" src="assets/logo_couleur.png" alt="GuidPilot" />'
js = ""

# ---------- A : le matin (0 -> 15) puis titre (15 -> 21.45)
steam = "".join(f'<div class="steam" id="sm{i}" style="left:{30 + i * 28}px"></div>' for i in range(3))
leaves = ('<div class="leaf" style="left:790px;top:580px;transform:rotate(-30deg)"></div>'
          '<div class="leaf" style="left:840px;top:560px;transform:rotate(20deg)"></div>'
          '<div class="leaf" style="left:815px;top:600px;transform:rotate(-5deg)"></div>')
scene = (f'<div class="scene" id="sc"><span class="illus" style="left:0;top:-60px">Illustration</span>'
         f'<div class="win"></div><div class="sun"></div>'
         f'<div class="wclock"><i class="hr"></i><i class="mn"></i><div class="ct"></div></div>'
         f'{steam}<div class="mug"><b></b></div>{leaves}<div class="plant"></div>'
         f'<div class="lap"><div class="scr"><span class="demo2">Compte de démonstration</span><img id="lapi" src="assets/dash.png" alt="" /></div></div>'
         f'<div class="lapb"></div><div class="desk"></div></div>')
chaps = ["Les 4 cartes", "Le suivi financier", "Les actions rapides", "La fiche cliente"]
c4 = "".join(f'<div class="c5" id="q{i}"><b>{i + 1}</b>{t}</div>' for i, t in enumerate(chaps))
body = f'''
<div id="a" class="clip warm" data-start="0" data-duration="{T['b']}" data-track-index="1">
  <div id="a1" style="position:absolute;inset:0">
    <div class="hk"><div class="time" id="at">8 h 30</div>
      <div class="s1" id="as">Le café est encore chaud.<br/>Première séance dans une heure.</div>
      <div class="q" id="aq">Où en est votre activité <span>aujourd'hui ?</span></div>
      <div class="hchips"><div id="h1"><b>✓</b> Rendez-vous</div><div id="h2"><b>✓</b> Guidances à livrer</div><div id="h3"><b>✓</b> Paiements en attente</div></div>
    </div>
    {scene}
  </div>
  <div id="a2" class="navy" style="position:absolute;inset:0">
    <div class="titleA"><div style="font-weight:700;font-size:30px;letter-spacing:.16em;color:#E9C46A">TUTO GUIDPILOT</div>
      <div class="big" style="width:auto;margin-top:26px;font-size:86px">Le tableau de bord<br/><span>en 30 secondes</span></div></div>
    <div class="chips4">{c4}</div>
  </div>
</div>'''
js += 'tl.fromTo("#at",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.7,ease:"back.out(1.6)"},0.3);\n'
js += fin("#sc", 0.5) + pop("#as", 2.9, E)
js += "".join(f'tl.fromTo("#sm{i}",{{opacity:0,y:30}},{{opacity:1,y:-50,duration:2.2,repeat:4,ease:"sine.inOut"}},{1.2 + i * .5});\n' for i in range(3))
js += 'tl.fromTo("#lapi",{y:0},{y:-150,duration:6,ease:"sine.inOut"},5.0);\n'
js += pop("#aq", 6.6, E, 40) + pop("#h1", 11.05) + pop("#h2", 12.1) + pop("#h3", 13.7)
js += 'tl.fromTo("#a2",{opacity:0},{opacity:1,duration:.6},15.0);\n'
js += 'tl.fromTo(".titleA",{opacity:0,y:40},{opacity:1,y:0,duration:.7,ease:"back.out(1.4)"},15.2);\n'
js += pop("#q0", 16.6, y=40) + pop("#q1", 17.4, y=40) + pop("#q2", 18.2, y=40) + pop("#q3", 19.0, y=40)

# ---------- B : les 4 cartes (21.45 -> 37)
VW, VH = 1060, 760
c1, c2, c3, c4r = (22, 152, 284, 174), (330, 152, 284, 174), (637, 152, 284, 174), (944, 152, 285, 174)
vB0 = view(0, 0, IW, IH, VW, VH)
vB1 = view(10, 120, 620, 260, VW, VH)
vB2 = view(630, 120, 620, 260, VW, VH)
body += f'''
<div id="b" class="clip light" data-start="{T['b']}" data-duration="{round(T['c'] - T['b'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:600px"><div class="chap" id="bc"><b>1</b>Les 4 cartes</div><div class="h" id="bh">Votre journée <span>en un coup d'œil</span></div>
    <div class="lst"><div class="li" id="l1"><i>1</i>Rendez-vous aujourd'hui</div><div class="li" id="l2"><i>2</i>Guidances à livrer</div>
      <div class="li" id="l3"><i>3</i>Revenus du mois</div><div class="li" id="l4"><i>4</i>Note moyenne</div></div></div>
  {zframe("zb", 770, 150, VW, VH)}
</div>'''
js += pop("#bc", 21.6, E) + pop("#bh", 21.8, E, 40) + fin("#zb", 21.7) + zset("zb", vB0, 21.45)
js += 'tl.set("#zbr",{opacity:0},21.45);\n'
js += zto("zb", vB1, 22.8, 1.0)
js += rset("zb", ring_box(c1, vB1), 23.5) + ron("zb", 23.64) + lion("#l1", 23.64)
js += rto("zb", ring_box(c2, vB1), 27.18) + lion("#l2", 27.18)
js += zto("zb", vB2, 30.6, 0.9) + rto("zb", ring_box(c3, vB2), 30.6, 0.9) + lion("#l3", 31.07)
js += rto("zb", ring_box(c4r, vB2), 33.61) + lion("#l4", 33.61)

# ---------- C : suivi financier (37 -> 53.65)
VWc, VHc = 1700, 330
vC = view(20, 350, 1210, 210, VWc, VHc, smax=1.42)
m1, m2, m3, m4 = (47, 436, 277, 88), (341, 436, 276, 88), (634, 436, 277, 88), (927, 436, 277, 88)
vf = (1055, 380, 160, 38)
vfb = ring_box(vf, vC, 6)
cur_x = 110 + 2 + vfb["x"] + vfb["width"] * 0.55
cur_y = 300 + 2 + 46 + vfb["y"] + vfb["height"] * 0.6
body += f'''
<div id="c" class="clip light" data-start="{T['c']}" data-duration="{round(T['d'] - T['c'], 2)}" data-track-index="1">
  {LOGO}
  <div class="hdr"><div class="chap" id="cc"><b>2</b>Le suivi financier</div></div>
  <div style="position:absolute;left:110px;top:170px" class="h" id="ch">Ce qui est encaissé… <span>et ce qui ne l'est pas encore</span></div>
  {zframe("zc", 110, 300, VWc, VHc)}
  <div class="statc" id="cs"><div class="l">À encaisser</div><div class="n"><span id="cn">0</span>,00 €</div></div>
  <div class="why"><div class="w1" id="cw">Des règlements en attente ? <span>Vous le voyez tout de suite.</span></div>
    <div class="w2" id="cw2">« Voir les factures » : le détail en un clic</div></div>
  <svg class="cursor" id="ccur" viewBox="0 0 24 24" style="left:{round(cur_x) + 260}px;top:{round(cur_y) + 300}px"><path d="M3 2l7 19 2.5-7.5L20 11z" fill="#0F172A" stroke="#fff" stroke-width="1.5"/></svg>
</div>'''
js += pop("#cc", 37.2, E) + pop("#ch", 37.4, E, 40) + fin("#zc", 37.6) + zset("zc", vC, 37.0)
js += 'tl.set("#zcr",{opacity:0},37.0);\n'
js += rset("zc", ring_box(m1, vC), 39.2) + ron("zc", 39.3)
js += rto("zc", ring_box(m2, vC), 41.1) + rto("zc", ring_box(m3, vC), 42.38) + rto("zc", ring_box(m4, vC), 43.65)
js += rto("zc", ring_box(m2, vC), 44.82)
js += pop("#cs", 45.2, E, 50)
js += 'tl.fromTo("#cn",{innerText:0},{innerText:160,snap:{innerText:1},duration:1.6,ease:"power2.out"},46.6);\n'
js += 'tl.to("#cs",{scale:1.04,duration:.3,yoyo:true,repeat:1,ease:"sine.inOut"},48.3);\n'
js += pop("#cw", 48.1, E)
js += 'tl.fromTo("#ccur",{opacity:0,x:0,y:0},{opacity:1,x:-260,y:-300,duration:1.1,ease:"power2.inOut"},50.3);\n'
js += rto("zc", vfb, 50.6, .7)
js += 'tl.to("#ccur",{scale:.85,duration:.12,yoyo:true,repeat:1},51.6);\n'
js += pop("#cw2", 52.0)

# ---------- D : agenda + actions rapides (53.65 -> 66.45)
VWd, VHd = 1040, 780
vD1 = view(20, 580, 786, 424, VWd, VHd)
vD2 = view(836, 580, 394, 424, VWd, VHd)
ag_item = (47, 680, 733, 163)
acts = [(864, 660, 338, 70), (864, 742, 338, 70), (864, 824, 338, 70), (864, 906, 338, 70)]
body += f'''
<div id="d" class="clip light" data-start="{T['d']}" data-duration="{round(T['e'] - T['d'], 2)}" data-track-index="1">
  {LOGO}
  {zframe("zd", 90, 150, VWd, VHd)}
  <div class="colr"><div class="chap" id="dc"><b>3</b>Agenda et actions rapides</div><div class="h" id="dh">L'essentiel<br/><span>à un clic</span></div>
    <div style="margin-top:34px">
      <div class="ck" id="k1"><i>✓</i>Planifier un rendez-vous</div><div class="ck" id="k2"><i>✓</i>Ajouter une cliente</div>
      <div class="ck" id="k3"><i>✓</i>Créer une guidance</div><div class="ck" id="k4"><i>✓</i>Éditer une facture</div></div>
    <div class="tag" id="dt">Plus besoin de chercher dans les menus</div></div>
</div>'''
js += fin("#zd", 53.75, -120) + zset("zd", vD1, 53.65) + pop("#dc", 54.0, E) + pop("#dh", 54.2, E, 40)
js += 'tl.set("#zdr",{opacity:0},53.65);\n'
js += rset("zd", ring_box(ag_item, vD1), 55.4) + ron("zd", 55.53)
js += zto("zd", vD2, 58.0, 0.9) + rto("zd", ring_box(acts[0], vD2), 58.0, 0.9)
js += pop("#k1", 60.14) + pop("#k2", 61.39) + rto("zd", ring_box(acts[1], vD2), 61.39)
js += pop("#k3", 62.6) + rto("zd", ring_box(acts[2], vD2), 62.6) + pop("#k4", 63.7) + rto("zd", ring_box(acts[3], vD2), 63.7)
js += pop("#dt", 65.03)

# ---------- E : fiche cliente (66.45 -> 78.45)
evs = [("dt", "Séance · Tirage de tarot", "12 septembre · Visio", '<span class="badge b-ok">Payée</span>', 300),
       ("dt p", "Guidance écrite livrée", "14 septembre · Espace client", "", 400),
       ("dt o", "Message de Léa", "20 septembre · Messagerie", "", 500),
       ("dt g", "Séance · Suivi mensuel", "Aujourd'hui · 14:00", '<span class="badge b-bl">À venir</span>', 600)]
evh = "".join(f'<div class="ev" id="ev{i}" style="top:{top}px"><div class="{c}"></div><div><div class="tx">{a}</div><div class="sm">{b}</div></div>{bd}</div>'
              for i, (c, a, b, bd, top) in enumerate(evs))
lock = '<svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#6B4E16" stroke-width="2.2" stroke-linecap="round"><rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
eye = '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#E9C46A" stroke-width="2.2" stroke-linecap="round"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/><path d="M4 20L20 4"/></svg>'
body += f'''
<div id="e" class="clip light" data-start="{T['e']}" data-duration="{round(T['f'] - T['e'], 2)}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:680px"><div class="chap" id="ec"><b>4</b>La fiche cliente</div><div class="h" id="eh">Toute son histoire <span>au même endroit</span></div>
    <div class="p" id="ep">Ses séances passées, ses paiements et vos échanges : pour préparer chaque séance sereinement.</div></div>
  <div class="eye" id="eey">{eye}Jamais visibles par votre cliente</div>
  <div class="card" id="ecd"><span class="illus" style="right:30px;top:24px">Illustration</span>
    <div class="ch"><div class="av">LM</div><div><div class="nm">Léa M.</div><div class="st">Cliente depuis mars · 6 séances</div></div></div>
    <div class="tabs"><div class="on">Historique</div><div>Paiements</div><div>Messages</div><div>Documents</div></div>
    <div class="vline" id="evl"></div>{evh}
    <div class="note" id="enote">{lock}<div><div class="nt">Notes personnelles</div><div class="ns">Visibles uniquement par vous</div></div></div>
  </div>
</div>'''
js += pop("#ec", 66.6, E) + pop("#eh", 66.8, E, 40) + fin("#ecd", 67.2)
js += 'tl.fromTo("#evl",{scaleY:0},{scaleY:1,duration:2.4,ease:"power1.inOut"},69.9);\n'
js += pop("#ev0", 70.1) + pop("#ep", 70.4, E) + pop("#ev1", 71.61) + pop("#ev2", 72.54) + pop("#ev3", 73.2)
js += pop("#enote", 74.03, y=60) + 'tl.to("#enote",{scale:1.03,duration:.3,yoyo:true,repeat:3,ease:"sine.inOut"},74.6);\n'
js += pop("#eey", 76.47)

# ---------- F : routine du matin (78.45 -> 90)
R = 280
circ = round(2 * 3.14159 * R, 1)
body += f'''
<div id="f" class="clip navy" data-start="{T['f']}" data-duration="{round(T['g'] - T['f'], 2)}" data-track-index="1">
  <div class="watch" id="fw"><svg width="620" height="620" viewBox="0 0 620 620">
    <circle cx="310" cy="310" r="{R}" fill="none" stroke="#1E293B" stroke-width="26"/>
    <circle id="fring" cx="310" cy="310" r="{R}" fill="none" stroke="#2563EB" stroke-width="26" stroke-linecap="round" stroke-dasharray="{circ}" stroke-dashoffset="{circ}" transform="rotate(-90 310 310)"/>
    <rect x="285" y="-2" width="50" height="26" rx="8" fill="#E9C46A"/></svg>
    <div class="num"><span id="fn">0</span> s</div><div class="lab">CHAQUE MATIN</div></div>
  <div class="rout"><div class="t1" id="ft">MON CONSEIL</div><div class="h" id="fh">Votre routine <span>du matin</span></div>
    <div style="margin-top:40px">
      <div class="rk" id="r1"><i>1</i>Vos rendez-vous du jour</div>
      <div class="rk" id="r2"><i>2</i>Vos guidances à livrer</div>
      <div class="rk" id="r3"><i>3</i>Ce qui reste à encaisser</div></div>
    <div class="clear" id="fcl">Et la journée commence l'esprit clair</div></div>
</div>'''
js += 'tl.fromTo("#fw",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},78.6);\n'
js += pop("#ft", 78.7, E) + pop("#fh", 78.9, E, 40)
js += f'tl.to("#fring",{{attr:{{"stroke-dashoffset":0}},duration:9.5,ease:"none"}},79.4);\n'
js += 'tl.fromTo("#fn",{innerText:0},{innerText:30,snap:{innerText:1},duration:9.5,ease:"none"},79.4);\n'
for i, t in enumerate([82.05, 83.84, 86.23]):
    js += pop(f"#r{i + 1}", t - .1, y=20) + rkon(f"#r{i + 1}", t + .6)
js += pop("#fcl", 88.16)

# ---------- G : citation (90 -> 93.3) puis fin (93.3 -> DUR)
body += f'''
<div id="g" class="clip light" data-start="{T['g']}" data-duration="{round(T['h'] - T['g'], 2)}" data-track-index="1">
  {LOGO}
  <div class="quote"><div class="qm" id="gq0">“</div>
    <div class="q" id="gq">GuidPilot s'améliore<br/><span>chaque semaine</span></div>
    <div class="s" id="gs">grâce aux retours des praticiennes</div></div>
</div>
<div id="h" class="clip navy" data-start="{T['h']}" data-duration="{round(DUR - T['h'], 2)}" data-track-index="1">
  <div class="center" id="g6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard" id="g7">✓ Sans carte bancaire</div>
    <div class="url" id="g8">guidpilot.fr</div>
    <div class="sub" id="g9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += pop("#gq0", 90.1, E) + 'tl.fromTo("#gq",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},90.3);\n'
js += pop("#gs", 91.4)
js += 'tl.fromTo("#g6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},93.4);\n'
js += pop("#g7", 97.3) + pop("#g8", 98.6) + pop("#g9", 100.1)
js += 'tl.to("#g9",{scale:1.06,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"},101.9);\n'

hidden = ["#as", "#aq", "#h1", "#h2", "#h3", "#a2", "#q0", "#q1", "#q2", "#q3",
          "#cs", "#cw", "#cw2", "#ccur", "#k1", "#k2", "#k3", "#k4", "#dt",
          "#ep", "#ev0", "#ev1", "#ev2", "#ev3", "#enote", "#eey", "#r1", "#r2", "#r3", "#fcl",
          "#gq0", "#gq", "#gs", "#g7", "#g8", "#g9"]
html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1920" data-height="1080">
<div class="aibadge">Voix off générée par IA</div>
<audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
{body}
</div>
<script>
const tl=gsap.timeline({{paused:true}});
gsap.set({hidden!r},{{opacity:0}});
{js}
window.__timelines["main"]=tl;
</script></body></html>'''

d = ATELIER / "build" / "yt-tableau-de-bord"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for a in ("dash.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
