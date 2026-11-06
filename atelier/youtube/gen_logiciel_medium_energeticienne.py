"""Vidéo YouTube 1920x1080 : « Logiciel pour médium et énergéticienne : la checklist des consultations à distance »
(série « Pensé pour votre métier » · public guidance, vendredi 06/11/2026).
Usage : python3 gen_logiciel_medium_energeticienne.py <voix.wav> [DUR]  -> build/yt-medium-energeticienne/
Voix : 9 paragraphes générés un par un (voix/2026-11-06_yt-medium-p1..p9.mp3), assemblés avec assembler_voix.py
dans l'ordre p1, p2, p4 (CTA), p3, p5, p6, p7, p8, p9 -> CTA oral d'abonnement après le point 1 (~29 %).
Temps T = début des phrases (silencedetect -30 dB / 0,15 s sur le wav assemblé, 143,3 s).
Structure « checklist en 4 cases » (nouvelle) : carte plein écran à fond changeant + presse-papiers dont la case se coche
-> problème illustré -> le bon réflexe. GuidPilot seulement à la fin (16 s). Aucune personne, aucun prix GuidPilot,
aucun superlatif, aucune promesse de prédiction ou de résultat, aucune plateforme nommée.
Réutilise CSS et helpers de gen_logiciel_reiki.py + EXTRA7 de gen_logiciel_sophro_hypno.py.
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_logiciel_reiki.py").read_text()
ns = {"__file__": str(HERE / "gen_logiciel_reiki.py")}
exec(src.split("\n# ---------- A :")[0], ns)
CSS, EXTRA, EXTRA4, EXTRA5, ATELIER, KIT = (ns[k] for k in ("CSS", "EXTRA", "EXTRA4", "EXTRA5", "ATELIER", "KIT"))
pop, fin, out, phone, LOGO, LOGOW, E, LOCK, CAM = (ns[k] for k in ("pop", "fin", "out", "phone", "LOGO", "LOGOW", "E", "LOCK", "CAM"))
EXTRA7 = (HERE / "gen_logiciel_sophro_hypno.py").read_text().split('EXTRA7 = """')[1].split('"""')[0]

DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 146.6
r2 = lambda x: round(x, 2)

EXTRA8 = """
.hk8{position:absolute;left:110px;top:170px;width:960px}
.hk8 .q{font-weight:800;font-size:84px;line-height:1.08;letter-spacing:-.025em;color:#fff}
.hk8 .q span{color:#E9C46A}
.hk8 .t{display:inline-block;margin-top:44px;padding:14px 30px;border-radius:999px;background:#1E293B;border:2px solid #475569;font-weight:700;font-size:34px;color:#F1F5F9}
.hk8 .s{font-weight:700;font-size:46px;line-height:1.2;color:#FDE68A;margin-top:40px}
.b8{position:relative;display:table;max-width:330px;margin:14px 20px;padding:14px 20px;border-radius:24px;font-weight:600;font-size:25px;line-height:1.3;background:#fff;border:2px solid #E2E8F0;color:#0F172A}
.b8.me{margin-left:auto;background:#2563EB;border-color:#2563EB;color:#fff}
.b8.au{display:flex;align-items:center;gap:14px;width:300px;background:#DBEAFE;border-color:#BFDBFE;color:#1E3A8A}
.b8.au b{flex:none;width:46px;height:46px;border-radius:50%;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:20px}
.b8.au span{flex:1;height:26px;background:repeating-linear-gradient(90deg,#60A5FA 0 5px,transparent 5px 10px);border-radius:4px}
.ph8{margin:14px 20px;height:190px;border-radius:22px;background:#CBD5E1;position:relative;overflow:hidden}
.ph8.r{margin-left:auto;width:250px}.ph8.l{width:250px}
.ph8:after{content:"";position:absolute;left:30px;right:30px;bottom:0;height:90px;background:#94A3B8;clip-path:polygon(0 100%,30% 20%,55% 70%,75% 35%,100% 100%)}
.ph8:before{content:"";position:absolute;right:40px;top:30px;width:44px;height:44px;border-radius:50%;background:#F1F5F9}
.scr8{position:absolute;left:0;right:0;top:120px}
.lost8{position:absolute;left:0;right:0;top:300px;text-align:center;z-index:5}
.lost8 div{display:inline-block;padding:12px 26px;border-radius:999px;background:#DC2626;color:#fff;font-weight:800;font-size:26px}
.chips8{display:flex;gap:16px;margin-top:30px;flex-wrap:wrap}
.chips8 div{padding:12px 28px;border-radius:999px;background:#fff;border:2px solid #E2E8F0;font-weight:700;font-size:30px;color:#0F172A}
.chips8 div.d{background:#0F172A;color:#E9C46A;border-color:#0F172A}
.brd{position:absolute;left:1120px;top:140px;width:700px;height:800px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.18);padding:90px 46px 40px}
.brd .clp{position:absolute;left:50%;top:-26px;width:220px;height:64px;margin-left:-110px;border-radius:18px;background:#0F172A;border:6px solid #E9C46A}
.brd .tt{font-weight:800;font-size:34px;letter-spacing:.1em;color:#64748B}
.brd .rw{position:relative;display:flex;align-items:center;gap:26px;margin-top:34px;padding:24px 26px;border-radius:22px;border:3px solid #E2E8F0;background:#F8FAFC}
.brd .rw .bx{flex:none;width:62px;height:62px;border-radius:16px;border:5px solid #CBD5E1;background:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:38px;color:#fff}
.brd .rw .tx{font-weight:800;font-size:36px;line-height:1.15;color:#0F172A}
.brd .rw.done .bx{background:#2563EB;border-color:#2563EB}
.brd .rw.done .tx{color:#64748B}
.brd .rw.cur{border-color:#E9C46A;background:#FFFBEB}
.brd .rw .bl{filter:blur(9px)}
.brd .rw .lq{position:absolute;right:22px;top:50%;margin-top:-26px;padding:8px 18px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:24px}
.ck{position:absolute;left:110px;top:0;bottom:0;width:900px;display:flex;flex-direction:column;justify-content:center}
.ck .n{display:inline-flex;align-items:center;gap:22px;font-weight:800;font-size:34px;letter-spacing:.14em;text-transform:uppercase}
.ck .n b{display:inline-flex;width:84px;height:84px;border-radius:50%;align-items:center;justify-content:center;font-size:44px;letter-spacing:0}
.ck .q{font-weight:800;font-size:112px;line-height:1.04;letter-spacing:-.035em;margin-top:36px}
.cream .ck .n{color:#B7791F}.cream .ck .n b{background:#0F172A;color:#E9C46A}.cream .ck .q{color:#0F172A}.cream .ck .q span{color:#2563EB}
.navy .ck .n{color:#93C5FD}.navy .ck .n b{background:#E9C46A;color:#0F172A}.navy .ck .q{color:#fff}.navy .ck .q span{color:#E9C46A}
.blue .ck .n{color:#BFDBFE}.blue .ck .n b{background:#fff;color:#1D4ED8}.blue .ck .q{color:#fff}.blue .ck .q span{color:#FDE68A}
.f3{position:absolute;left:110px;right:110px;top:380px;display:flex;gap:36px}
.f3 .c{position:relative;flex:1;height:560px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.08);padding:40px}
.f3 .ic{width:96px;height:96px;border-radius:24px;display:flex;align-items:center;justify-content:center;font-size:48px;font-weight:800}
.f3 .a{font-weight:800;font-size:46px;line-height:1.12;color:#0F172A;margin-top:26px}
.f3 .rw{display:flex;align-items:center;gap:14px;margin-top:20px;font-weight:700;font-size:29px;color:#334155}
.f3 .rw i{font-style:normal;flex:none;width:44px;height:44px;border-radius:12px;background:#EFF6FF;color:#2563EB;display:flex;align-items:center;justify-content:center;font-size:24px}
.f3 .rw.g i{background:#FBF3DC;color:#B7791F}
.bank{position:absolute;left:1080px;top:190px;width:740px;border-radius:28px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.35)}
.bank .hd{border-radius:28px 28px 0 0}
.bank .hd{height:96px;padding:0 36px;display:flex;align-items:center;justify-content:space-between;background:#F1F5F9;font-weight:800;font-size:32px;color:#0F172A}
.bank .hd small{font-weight:600;font-size:22px;color:#64748B}
.bank .ln{display:flex;align-items:center;justify-content:space-between;padding:28px 36px;border-top:2px solid #E2E8F0;font-weight:700;font-size:30px;color:#334155}
.bank .ln b{padding:6px 18px;border-radius:999px;font-size:22px}
.bank .ln b.w{background:#FEF3C7;color:#92400E}.bank .ln b.x{background:#FEE2E2;color:#B91C1C}
.bk8{position:absolute;left:1000px;top:170px;width:820px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.bk8 .tp{padding:34px 44px;background:#0F172A;color:#fff;font-weight:800;font-size:38px}
.bk8 .tp small{display:block;font-weight:600;font-size:24px;color:#CBD5E1;margin-top:8px}
.bk8 .st{display:flex;align-items:center;gap:22px;margin:26px 44px 0;padding:22px 26px;border-radius:20px;background:#F8FAFC;border:2px solid #E2E8F0;font-weight:700;font-size:30px;color:#334155}
.bk8 .st i{font-style:normal;flex:none;width:52px;height:52px;border-radius:50%;background:#16A34A;color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800}
.bk8 .cd{margin:26px 44px 40px;padding:26px 30px;border-radius:20px;background:#FFFDF7;border:2px solid #E7DFC9}
.bk8 .cd .k{display:flex;justify-content:space-between;font-weight:800;font-size:26px;letter-spacing:.08em;color:#B7791F}
.bk8 .cd .k span{padding:4px 14px;border-radius:999px;background:#0F172A;color:#E9C46A;font-size:18px;letter-spacing:.06em}
.bk8 .cd .l{font-weight:600;font-size:28px;color:#334155;margin-top:14px}
.ok8{display:flex;align-items:center;gap:18px;margin-top:26px;font-weight:800;font-size:40px;color:#0F172A}
.ok8 i{font-style:normal;flex:none;width:56px;height:56px;border-radius:50%;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px}
.pf{position:absolute;top:330px;width:820px;height:560px;border-radius:30px;padding:46px}
.pf.l{left:110px;background:#F1F5F9;border:3px dashed #94A3B8}
.pf.r{left:990px;background:#fff;border:3px solid #2563EB;box-shadow:0 30px 80px rgba(37,99,235,.15)}
.pf .k{font-weight:800;font-size:28px;letter-spacing:.12em;color:#64748B}
.pf.r .k{color:#2563EB}
.pf .a{font-weight:800;font-size:50px;line-height:1.12;color:#0F172A;margin-top:18px}
.pf .rw{display:flex;align-items:center;gap:18px;margin-top:30px;font-weight:700;font-size:32px;color:#334155}
.pf .rw i{font-style:normal;flex:none;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px}
.pf.l .rw i{background:#E2E8F0;color:#475569}.pf.r .rw i{background:#2563EB;color:#fff}
.pp8{position:absolute;left:880px;top:130px;width:940px;height:830px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.pp8 .tp{height:200px;background:#0F172A;padding:40px 50px;color:#fff}
.pp8 .tp .k{font-weight:700;font-size:22px;letter-spacing:.14em;color:#E9C46A}
.pp8 .tp .n{font-weight:800;font-size:46px;margin-top:12px}
.pp8 .tp .so{display:flex;gap:12px;margin-top:14px}
.pp8 .tp .so span{padding:6px 18px;border-radius:999px;background:#1E293B;border:2px solid #475569;font-weight:700;font-size:22px;color:#E2E8F0}
.pp8 .it{display:flex;align-items:center;justify-content:space-between;margin:24px 44px 0;padding:22px 28px;border-radius:20px;border:2px solid #E2E8F0;background:#F8FAFC;font-weight:800;font-size:30px;color:#0F172A}
.pp8 .it span{height:56px;padding:0 24px;border-radius:14px;background:#2563EB;color:#fff;font-size:24px;display:flex;align-items:center}
.pp8 .rv8{margin:24px 44px 0;padding:22px 28px;border-radius:20px;background:#FBF3DC}
.pp8 .rv8 .s{font-size:38px;color:#E9C46A;letter-spacing:4px}
.pp8 .rv8 .t{font-weight:600;font-style:italic;font-size:26px;color:#6B4E16;margin-top:6px}
.pp8 .lk{display:flex;align-items:center;gap:16px;margin:24px 44px 0;padding:18px 26px;border-radius:18px;border:3px solid #2563EB;font-weight:800;font-size:28px;color:#1D4ED8}
.sh8{position:absolute;left:110px;top:780px;display:flex;gap:18px}
.sh8 div{padding:14px 28px;border-radius:999px;background:#0F172A;color:#fff;font-weight:700;font-size:30px}
.zc{position:absolute;left:980px;top:210px;width:840px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.14)}
.zc img{display:block;width:840px}
.com8{position:absolute;left:110px;top:830px;display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.com8 b{padding:12px 28px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:34px}
.com8 small{font-weight:600;font-size:24px;color:#64748B}
"""

T = dict(
    q=0.67, sem=2.95, aud=6.37, si=10.03, ck=12.37, ck2=14.08, der=17.45,
    p1=21.12, p1b=24.55, v1=27.87, v2=28.70, v3=29.96, br1=31.0, f1=34.61, f2=35.88, f3=37.01, ch=39.08,
    cta=42.06, abo=43.93, lien=47.90,
    p2=52.05, p2b=55.43, vir=58.74, sol=60.27, reg=61.84, cond=63.99, pers=65.56, gen=68.0,
    p3=69.98, p3b=73.86, env=75.58, perd=77.41, br3=80.79, rel=83.70, reec=85.50, notes=87.74,
    p4=91.44, p4b=93.73, reste=95.04, com=98.27, pg=100.97, pres=101.84, soc=103.09, avis=104.86, gard=106.26, part=107.71,
    rs=109.74, r1=110.50, r2=114.65, r3=116.82,
    g=119.64, gpg=123.09, gres=123.97, gmeet=126.01, ggui=127.63, gfac=130.74, gav=131.56, gcom=132.66,
    z=135.61, url=138.98, zabo=140.83)

ITEMS = ["Réserver sans<br/>vos messages", "Payée avant<br/>la consultation", "Une guidance<br/>bien rangée", "Une page<br/>à votre nom"]
body, js = "", ""


def board(id_, cur, mask_last=False, done_upto=None):
    done_upto = cur - 1 if done_upto is None else done_upto
    rows = ""
    for i, t in enumerate(ITEMS):
        cls = " done" if i < done_upto else (" cur" if i == cur - 1 else "")
        tx = f'<span class="bl">{t}</span><span class="lq">Le dernier…</span>' if (mask_last and i == 3) else t
        rows += f'<div class="rw{cls}" id="{id_}r{i}"><div class="bx">{"✓" if i < done_upto else ""}</div><div class="tx">{tx}</div></div>'
    return f'<div class="brd hid" id="{id_}"><div class="clp"></div><div class="tt">CONSULTATIONS À DISTANCE</div>{rows}</div>'


def ccard(id_, start, end, num, title, cls, logo):
    h = f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(start)}" data-duration="{r2(end - start)}" data-track-index="1">
  {logo}
  <div class="ck"><div class="n hid" id="{id_}n"><b>{num}</b>Point {num} sur 4</div><div class="q hid" id="{id_}q">{title}</div></div>
  {board(id_ + "b", num)}
</div>'''
    j = pop(f"#{id_}n", start + .05, E) + pop(f"#{id_}q", start + .2, E, 50) + fin(f"#{id_}b", start + .3)
    j += f'tl.fromTo("#{id_}br{num - 1}",{{scale:1}},{{scale:1.05,duration:.3,yoyo:true,repeat:1}},{r2(start + 1.1)});\n'
    return h, j


# ---------- A : accroche (0 -> si) — lisible dès l'image 0
clutter = ('<div class="phead"><div class="av">LM</div>Léa M.</div><div class="scr8" id="ascr">'
           '<div class="ph8 r"></div><div class="b8">Merci pour hier soir&nbsp;!</div><div class="b8 me">Avec plaisir</div>'
           '<div class="b8 au"><b>▶</b><span></span>20:12</div><div class="ph8 l"></div><div class="b8 me">Bon week-end</div>'
           '<div class="b8">Je ne retrouve plus l\'audio de ma guidance…</div></div>'
           '<div class="lost8 hid" id="alost"><div>Où est l\'audio&nbsp;?</div></div>')
body += f'''
<div id="a" class="clip navy" data-start="0" data-duration="{r2(T["si"])}" data-track-index="1">
  <div class="hk8"><div class="q">« Je ne retrouve plus <span>l'audio de ma guidance.&nbsp;»</span></div>
    <div class="t hid" id="at">3 semaines après la consultation</div>
    <div class="s hid" id="as">L'audio est quelque part,<br/>entre deux conversations.</div></div>
  {phone("aph", clutter, 1260, 100)}
</div>'''
js += f'gsap.set("#aph",{{opacity:1}});\n' + pop("#at", T["sem"]) + pop("#as", T["aud"], E)
js += f'tl.fromTo("#ascr",{{y:0}},{{y:-260,duration:1.6,ease:"power2.inOut"}},{r2(T["aud"] + .3)});\n'
js += pop("#alost", T["aud"] + 2.0, "back.out(2)")

# ---------- B : checklist (si -> p1)
body += f'''
<div id="b" class="clip light" data-start="{r2(T["si"])}" data-duration="{r2(T["p1"] - T["si"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:900px"><div class="chap hid" id="bc"><b>✓</b>La checklist</div>
    <div class="h hid" id="bh" style="font-size:76px">Médium, énergéticienne&nbsp;:<br/><span>vous consultez à distance&nbsp;?</span></div>
    <div class="chips8"><div class="hid" id="bp0">Médium</div><div class="hid" id="bp1">Énergéticienne</div><div class="d hid" id="bp2">À distance</div></div></div>
  {board("bb", 0, mask_last=True, done_upto=0)}
</div>'''
js += pop("#bc", T["si"] + .05, E) + pop("#bh", T["si"] + .25, E, 40) + "".join(pop(f"#bp{i}", T["si"] + 1.0 + i * .4) for i in range(3))
js += f'gsap.set("#bbr0,#bbr1,#bbr2,#bbr3",{{opacity:0}});\n' + fin("#bb", T["ck"])
js += "".join(pop(f"#bbr{i}", T["ck2"] + i * .45, y=30) for i in range(3)) + pop("#bbr3", T["der"], "back.out(2)")
js += f'tl.to("#bbr3",{{borderColor:"#E9C46A",backgroundColor:"#FFFBEB",duration:.3}},{r2(T["der"] + .4)});\n'

# ---------- P1 carte
h, j = ccard("c1", T["p1"], T["p1b"], 1, "Une réservation<br/><span>sans vos messages</span>", "cream", LOGO)
body += h; js += j

# ---------- P1 : chaque question coûte un échange (p1b -> br1)
qs = ["C'est en visio&nbsp;?", "Ça dure combien&nbsp;?", "Vous êtes libre jeudi&nbsp;?"]
qh = "".join(f'<div class="b8 hid" id="c1q{i}">{q}</div>' for i, q in enumerate(qs))
body += f'''
<div id="c1m" class="clip warm" data-start="{r2(T["p1b"])}" data-duration="{r2(T["br1"] - T["p1b"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:780px"><div class="h hid" id="c1mh" style="font-size:84px">Chaque question<br/><span>= un échange</span></div>
    <div class="ok8 hid" id="c1mc" style="color:#B91C1C"><i style="background:#DC2626">✕</i>Et la réservation attend</div></div>
  {phone("c1ph", '<div class="phead"><div class="av">CM</div>Camille M.</div><div style="position:absolute;left:0;right:0;top:130px">' + qh + '</div>', 1240, 100)}
</div>'''
js += pop("#c1mh", T["p1b"] + .1, E, 40) + fin("#c1ph", T["p1b"] + .2)
for i, k in enumerate(("v1", "v2", "v3")):
    js += pop(f"#c1q{i}", T[k], y=20)
js += pop("#c1mc", T["v3"] + 1.2)

# ---------- P1 : une prestation par format (br1 -> cta)
fm = [("▶", "#EFF6FF", "#2563EB", "Consultation<br/>en visio", ["Durée : 1 h", "Son tarif", "Lien de visio prévu"]),
      ("✎", "#FBF3DC", "#B7791F", "Guidance<br/>écrite", ["Sans rendez-vous", "Son tarif", "Livrée sous 3 jours"]),
      ("♪", "#EEF2FF", "#4338CA", "Guidance<br/>vocale", ["Audio de 20 min", "Son tarif", "Livrée sous 3 jours"])]
fh = ""
for i, (ic, bg, c, a, rows) in enumerate(fm):
    rr = "".join(f'<div class="rw{" g" if k == 2 else ""} hid" id="f{i}r{k}"><i>{"⏱€✓"[k]}</i>{t}</div>' for k, t in enumerate(rows))
    fh += f'<div class="c hid" id="f{i}"><span class="illus" style="right:20px;top:20px">Exemple</span><div class="ic" style="background:{bg};color:{c}">{ic}</div><div class="a">{a}</div>{rr}</div>'
body += f'''
<div id="c1f" class="clip light" data-start="{r2(T["br1"])}" data-duration="{r2(T["cta"] - T["br1"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="c1fc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="c1fh" style="font-size:62px">Une prestation <span>par format</span></div></div>
  <div class="f3">{fh}</div>
</div>'''
js += pop("#c1fc", T["br1"] + .05, E) + pop("#c1fh", T["br1"] + .25, E, 40)
js += pop("#f0", T["f1"], y=50) + pop("#f1", T["f2"], y=50) + pop("#f2", T["f3"], y=50)
for k in range(3):
    js += "".join(pop(f"#f{i}r{k}", T["ch"] + k * .8 + i * .15) for i in range(3))

# ---------- CTA oral abonnement (cta -> p2)
body += f'''
<div id="cta" class="clip navy" data-start="{r2(T["cta"])}" data-duration="{r2(T["p2"] - T["cta"])}" data-track-index="1">
  {LOGOW}
  <div class="ctaC"><div class="k hid" id="ck">CETTE CHECKLIST VOUS EST UTILE&nbsp;?</div>
    <div class="b hid" id="cb">2 vidéos par semaine<br/><span>pour organiser votre activité</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="dsc hid" id="cd">↓ <span><b>Essai gratuit&nbsp;:</b> le lien est dans la description</span></div>
</div>'''
js += pop("#ck", T["cta"] + .1, E) + pop("#cy", T["abo"], "back.out(2)") + pop("#cb", T["abo"] + .9, E, 40)
js += f'tl.to("#cy",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(T["abo"] + 1.4)});\n' + pop("#cd", T["lien"] + .2)

# ---------- P2 carte
h, j = ccard("c2", T["p2"], T["p2b"], 2, "Le paiement<br/><span>avant la consultation</span>", "navy", LOGOW)
body += h; js += j

# ---------- P2 : on attend le virement (p2b -> sol)
body += f'''
<div id="c2m" class="clip eve" data-start="{r2(T["p2b"])}" data-duration="{r2(T["sol"] - T["p2b"])}" data-track-index="1">
  {LOGOW}
  <div class="night"><div class="clk hid" id="c2k">J<span>+</span>3</div><div class="d hid" id="c2d">À distance, pas de « fin de séance » pour régler</div>
    <div class="todo hid" id="c2t">… vous attendez le virement</div></div>
  <div class="bank hid" id="c2b"><span class="illus" style="left:0;bottom:-46px">Illustration</span>
    <div class="hd">Mes virements<small>Cette semaine</small></div>
    <div class="ln">Guidance vocale · Camille M.<b class="w hid" id="c2w0">En attente</b></div>
    <div class="ln">Visio · Sophie R.<b class="w hid" id="c2w1">En attente</b></div>
    <div class="ln">Guidance écrite · Inès L.<b class="x hid" id="c2w2">Pas reçu</b></div></div>
</div>'''
js += pop("#c2k", T["p2b"] + .05, E) + pop("#c2d", T["p2b"] + .8, E) + fin("#c2b", T["p2b"] + .4)
js += pop("#c2w0", T["p2b"] + 1.8, "back.out(2)") + pop("#c2w1", T["p2b"] + 2.4, "back.out(2)") + pop("#c2t", T["vir"])
js += pop("#c2w2", T["vir"] + .5, "back.out(2)")

# ---------- P2 : réglé à la réservation (sol -> p3)
body += f'''
<div id="c2s" class="clip light" data-start="{r2(T["sol"])}" data-duration="{r2(T["p3"] - T["sol"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:820px"><div class="chap hid" id="c2sc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="c2sh" style="font-size:72px">Réglé<br/><span>au moment de réserver</span></div>
    <div class="ok8 hid" id="c2o1"><i>✓</i>Personne n'a à le demander</div>
    <div class="ok8 hid" id="c2o2"><i>✓</i>Personne n'est gêné</div></div>
  <div class="bk8 hid" id="c2k8"><span class="illus" style="left:24px;bottom:16px">Illustration</span>
    <div class="tp">Réservation confirmée<small>Guidance vocale · livrée sous 3 jours</small></div>
    <div class="st hid" id="c2st"><i>✓</i>Règlement effectué à la réservation</div>
    <div class="cd hid" id="c2cd"><div class="k">MES CONDITIONS<span>EXEMPLE</span></div>
      <div class="l">Annulation gratuite jusqu'à 24 h avant</div><div class="l">Report possible une fois</div>
      <div class="l">Lues avant de réserver</div></div></div>
</div>'''
js += pop("#c2sc", T["sol"] + .05, E) + pop("#c2sh", T["sol"] + .25, E, 40) + fin("#c2k8", T["sol"] + .5)
js += pop("#c2st", T["reg"] + .2, "back.out(2)") + pop("#c2cd", T["cond"] + .1, y=40)
js += pop("#c2o1", T["pers"] + .3) + pop("#c2o2", T["gen"])

# ---------- P3 carte
h, j = ccard("c3", T["p3"], T["p3b"], 3, "Une guidance<br/><span>bien rangée</span>", "blue", LOGOW)
body += h; js += j

# ---------- P3 : l'audio qui se perd (p3b -> br3)
lost = ('<div class="phead"><div class="av">♥</div>Famille</div><div class="scr8" id="c3scr">'
        '<div class="b8 au" style="opacity:.9"><b>▶</b><span></span>20:12</div><div class="b8">Joyeux anniversaire&nbsp;!</div>'
        '<div class="ph8 r"></div><div class="b8">Tu viens dimanche&nbsp;?</div><div class="ph8 l"></div>'
        '<div class="b8 me">Oui, vers midi</div><div class="ph8 r"></div><div class="b8">On prend le dessert</div></div>')
body += f'''
<div id="c3m" class="clip warm" data-start="{r2(T["p3b"])}" data-duration="{r2(T["br3"] - T["p3b"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:800px"><div class="chap hid" id="c3mc"><b>3</b>Le problème</div>
    <div class="h hid" id="c3mh" style="font-size:76px">20 minutes d'audio…<br/><span>entre deux photos de famille</span></div>
    <div class="ok8 hid" id="c3mo" style="color:#B91C1C"><i style="background:#DC2626">✕</i>Messagerie personnelle</div></div>
  {phone("c3ph", lost, 1240, 100)}
</div>'''
js += pop("#c3mc", T["p3b"] + .05, E) + pop("#c3mh", T["p3b"] + .25, E, 40) + fin("#c3ph", T["p3b"] + .3)
js += pop("#c3mo", T["env"] + .2) + f'tl.fromTo("#c3scr",{{y:0}},{{y:-560,duration:2.4,ease:"power2.inOut"}},{r2(T["perd"])});\n'

# ---------- P3 : espace privé (br3 -> notes)
inner3 = ('<div class="phead">Mon espace</div>'
          '<div class="notif hid" id="c3n"><div class="ic"><img src="assets/favicon.png" alt="" /></div>'
          '<div><div class="a">Nouvelle guidance</div><div class="b">Votre praticienne vous a écrit</div></div></div>'
          '<div class="cr hid" id="c3c1"><div class="a">Guidance écrite · 4 nov.</div><div class="b">À relire quand vous voulez</div><div class="nw">Nouveau</div></div>'
          '<div class="cr hid" id="c3c2"><div class="a">Guidance vocale · 4 nov.</div><div class="b">20 min</div><div class="audio"><b><i></i></b><span></span></div></div>')
body += f'''
<div id="c3s" class="clip light" data-start="{r2(T["br3"])}" data-duration="{r2(T["notes"] - T["br3"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:800px"><div class="chap hid" id="c3sc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="c3sh" style="font-size:70px">Un espace privé<br/><span>pour chaque cliente</span></div>
    <div class="ok8 hid" id="c3o1"><i>✓</i>Elle relit l'écrit</div>
    <div class="ok8 hid" id="c3o2"><i>✓</i>Elle réécoute l'audio</div></div>
  {phone("c3p2", inner3, 1240, 100)}
</div>'''
js += pop("#c3sc", T["br3"] + .05, E) + pop("#c3sh", T["br3"] + .25, E, 40) + fin("#c3p2", T["br3"] + .5)
js += pop("#c3c1", T["br3"] + 1.4) + pop("#c3c2", T["br3"] + 2.0)
js += pop("#c3o1", T["rel"]) + pop("#c3o2", T["reec"])
js += f'tl.fromTo("#c3n",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"}},{r2(T["rel"] + .6)});\n'

# ---------- P3 : notes privées (notes -> p4)
body += f'''
<div id="c3t" class="clip cream" data-start="{r2(T["notes"])}" data-duration="{r2(T["p4"] - T["notes"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:760px"><div class="h hid" id="c3th" style="font-size:80px;color:#0F172A">Vos notes,<br/><span>de votre côté</span></div></div>
  <div class="note7 hid" id="c3nt" style="left:960px;top:380px;width:840px"><div class="h7">{LOCK.format(s=44, c="#B7791F")}Notes personnelles<small>Jamais visibles par la cliente</small></div>
    <div class="l7">« Revenir sur la question du travail la prochaine fois »</div><div class="l7" style="font-size:22px;font-style:normal;color:#8A6A2B">Fiche cliente · Camille M. · Exemple</div></div>
</div>'''
js += pop("#c3th", T["notes"] + .1, E, 40) + pop("#c3nt", T["notes"] + .6, y=40)

# ---------- P4 carte
h, j = ccard("c4", T["p4"], T["p4b"], 4, "Une page<br/><span>à votre nom</span>", "cream", LOGO)
body += h; js += j

# ---------- P4 : plateforme vs votre page (p4b -> pg)
body += f'''
<div id="c4m" class="clip light" data-start="{r2(T["p4b"])}" data-duration="{r2(T["pg"] - T["p4b"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:120px"><div class="chap hid" id="c4mc"><b>4</b>La question</div>
    <div class="h hid" id="c4mh" style="font-size:58px">Vos clientes vous trouvent <span>où&nbsp;?</span></div></div>
  <div class="pf l hid" id="c4l"><span class="illus" style="right:24px;top:24px">Illustration</span><div class="k">SUR UNE PLATEFORME</div><div class="a">Une cliente<br/>qui vous découvre</div>
    <div class="rw hid" id="c4l1"><i>1</i>D'abord cliente de la plateforme</div>
    <div class="rw hid" id="c4l2"><i>2</i>Souvent une commission par consultation</div></div>
  <div class="pf r hid" id="c4r"><div class="k">VOTRE PAGE</div><div class="a">Une cliente<br/>qui vous retrouve</div>
    <div class="rw"><i>✓</i>Un lien qui reste le vôtre</div></div>
</div>'''
js += pop("#c4mc", T["p4b"] + .05, E) + pop("#c4mh", T["p4b"] + .25, E, 40)
js += f'tl.fromTo("#c4l",{{opacity:0,x:-80}},{{opacity:1,x:0,duration:.6,ease:"power3.out"}},{r2(T["p4b"] + .6)});\n'
js += pop("#c4l1", T["reste"] + .1) + pop("#c4l2", T["com"] + .1)
js += f'tl.fromTo("#c4r",{{opacity:0,x:80}},{{opacity:1,x:0,duration:.6,ease:"power3.out"}},{r2(T["com"] + 1.4)});\n'

# ---------- P4 : votre page (pg -> rs)
body += f'''
<div id="c4p" class="clip warm" data-start="{r2(T["pg"])}" data-duration="{r2(T["rs"] - T["pg"])}" data-track-index="1">
  {LOGO}
  <div class="col" style="width:720px;justify-content:flex-start;top:200px"><div class="chap hid" id="c4pc"><b>✓</b>Le bon réflexe</div>
    <div class="h hid" id="c4ph" style="font-size:70px">Une page à vous,<br/><span>un lien à partager</span></div></div>
  <div class="sh8"><div class="hid" id="c4s0">Bio Instagram</div><div class="hid" id="c4s1">TikTok</div><div class="hid" id="c4s2">E-mail</div></div>
  <div class="pp8 hid" id="c4pp"><span class="illus" style="left:24px;bottom:20px">Illustration</span>
    <div class="tp"><div class="k">VOTRE PAGE</div><div class="n">Médium &amp; énergéticienne</div>
      <div class="so hid" id="c4so"><span>Instagram</span><span>TikTok</span></div></div>
    <div class="it hid" id="c4i1">Consultation en visio · 1 h<span>Réserver</span></div>
    <div class="it hid" id="c4i2">Guidance vocale<span>Réserver</span></div>
    <div class="rv8 hid" id="c4av"><div class="s">★★★★★</div><div class="t">Les avis de vos clientes s'affichent ici</div></div>
    <div class="lk hid" id="c4lk">🔗 Votre lien personnel</div></div>
</div>'''
js += pop("#c4pc", T["pg"] + .05, E) + pop("#c4ph", T["pg"] + .25, E, 40) + fin("#c4pp", T["pg"] + .4)
js += pop("#c4i1", T["pres"]) + pop("#c4i2", T["pres"] + .5) + pop("#c4so", T["soc"], "back.out(2)") + pop("#c4av", T["avis"])
js += pop("#c4lk", T["gard"], "back.out(2)") + "".join(pop(f"#c4s{i}", T["part"] + i * .35) for i in range(3))

# ---------- récap (rs -> g)
rc = [("Une prestation par format,<br/><span>réservée et payée</span>", T["r1"], ""), ("Une guidance rangée<br/><span>dans un espace privé</span>", T["r2"], " g"),
      ("Une page à votre nom,<br/><span>avec vos avis</span>", T["r3"], "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += f'''
<div id="r" class="clip light" data-start="{r2(T["rs"])}" data-duration="{r2(T["g"] - T["rs"])}" data-track-index="1">
  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>
</div>'''
js += pop("#rk", T["rs"] + .05, E) + "".join(pop(f"#rc{i}", t, y=50) for i, (_, t, _) in enumerate(rc))

# ---------- GuidPilot (g -> z)
gc = [("Votre page", "gpg"), ("Réservation", "gres"), ("Paiement en ligne", "gres"), ("Google Meet", "gmeet"),
      ("Guidances écrites et vocales", "ggui"), ("Factures", "gfac"), ("Avis", "gav")]
gch = "".join(f'<div class="hid" id="gc{i}">{a}</div>' for i, (a, _) in enumerate(gc))
body += f'''
<div id="g" class="clip light" data-start="{r2(T["g"])}" data-duration="{r2(T["z"] - T["g"])}" data-track-index="1">
  <div class="col" style="width:820px;justify-content:flex-start;top:110px"><img class="hid" id="gl" src="assets/logo_couleur.png" alt="GuidPilot" style="width:400px" />
    <div class="h hid" id="gb" style="font-size:58px">Un outil conçu pour<br/><span>les praticiennes en guidance</span></div>
    <div class="chips8" style="margin-top:34px;max-width:820px">{gch}</div></div>
  <div class="zc hid" id="gz1"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">Compte de démonstration</span></div><img src="assets/guid.png" alt="" /></div>
  <div class="zc hid" id="gz2" style="top:690px"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">Compte de démonstration</span></div><img src="assets/avis.png" alt="" /></div>
  <div class="com8 hid" id="gcm"><b>0 % de commission sur vos séances</b><small>hors frais du moyen de paiement</small></div>
</div>'''
js += f'tl.fromTo("#gl",{{opacity:0,scale:.92}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"}},{r2(T["g"] + .1)});\n' + pop("#gb", T["g"] + .7, E, 40)
js += "".join(pop(f"#gc{i}", T[k] + (.4 if i == 2 else 0)) for i, (_, k) in enumerate(gc))
js += fin("#gz1", T["ggui"] + .2) + fin("#gz2", T["gav"]) + pop("#gcm", T["gcom"], "back.out(2)")

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
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA4}{EXTRA5}{EXTRA7}{EXTRA8}</style></head><body>
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

d = ATELIER / "build" / "yt-medium-energeticienne"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "avis.png", "guid.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, DUR)
