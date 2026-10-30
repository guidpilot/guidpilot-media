"""Vidéo YouTube 1920x1080 : « Tarologue, voyante indépendante : 5 erreurs administratives à éviter »
(conseil · public guidance, vendredi 30/10/2026).
Usage : python3 gen_erreurs_admin_guidance.py <voix.wav>  -> build/yt-erreurs-admin/
Voix : 9 paragraphes générés un par un (voix/2026-10-30_yt-erreurs-admin-p1..p9.mp3), assemblés avec assembler_voix.py
(starts 0.4, 18.33, 40.39, 48.52, 68.45, 86.52, 106.21, 123.54, 134.41 ; total 154.98). CTA oral d'abonnement = p3 (~26 %).
Structure « 5 erreurs » : chaque erreur = carte plein écran (fond qui change) -> scène illustrée du problème -> « Le bon réflexe ».
GuidPilot n'apparaît qu'à la fin (~14 s). Aucune personne représentée, aucun prix GuidPilot, aucun superlatif,
prudence factures : pas de « obligatoire », renvoi vers l'expert-comptable.
Réutilise CSS et helpers de gen_therapeutes_soir.py + EXTRA4 (gen_suivi_therapeutes.py) + EXTRA5 (gen_logiciel_reiki.py).
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_therapeutes_soir.py").read_text()
ns = {"__file__": str(HERE / "gen_therapeutes_soir.py")}
exec(src.split("# ---------- A :")[0], ns)
CSS, EXTRA, ATELIER, KIT = ns["CSS"], ns["EXTRA"], ns["ATELIER"], ns["KIT"]
pop, fin, out, phone, LOGO, E = (ns[k] for k in ("pop", "fin", "out", "phone", "LOGO", "E"))
EXTRA4 = (HERE / "gen_suivi_therapeutes.py").read_text().split('EXTRA4 = """')[1].split('"""')[0]
EXTRA5 = (HERE / "gen_logiciel_reiki.py").read_text().split('EXTRA5 = """')[1].split('"""')[0]

DUR = 160.0
LOGOW = '<img class="logo-corner" src="assets/logo_blanc.png" alt="GuidPilot" />'

EXTRA6 = """
.hq{position:absolute;left:110px;top:190px;width:1700px}
.hq .q{font-weight:800;font-size:116px;line-height:1.05;letter-spacing:-.035em;color:#0F172A}
.hq .q span{color:#2563EB}
.hq .s{font-weight:600;font-size:40px;color:#475569;margin-top:34px;line-height:1.3}
.apps{position:absolute;left:110px;top:640px;display:flex;gap:40px}
.app{position:relative;width:380px;height:240px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 18px 44px rgba(15,23,42,.08);padding:28px;display:flex;flex-direction:column;justify-content:space-between}
.app .ic{width:70px;height:70px;border-radius:20px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:34px;color:#fff}
.app b{font-weight:800;font-size:34px;color:#0F172A}
.app .x{position:absolute;right:22px;top:22px;width:54px;height:54px;border-radius:50%;background:#FEE2E2;color:#DC2626;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:30px}
.nf{position:absolute;left:1440px;top:720px;padding:22px 40px;border-radius:999px;background:#DC2626;color:#fff;font-weight:800;font-size:44px;transform:rotate(-4deg);z-index:8}
.mag{position:absolute;width:120px;height:120px;border-radius:50%;border:14px solid #0F172A;z-index:7}
.mag:after{content:"";position:absolute;right:-50px;bottom:-34px;width:60px;height:18px;border-radius:9px;background:#0F172A;transform:rotate(40deg)}
.costs{position:absolute;left:110px;top:560px;display:flex;gap:40px}
.cst{width:560px;height:300px;border-radius:30px;background:#1E293B;border:2px solid #475569;padding:40px;display:flex;align-items:center;gap:36px}
.cst .ic{flex:none;width:150px;height:150px;border-radius:50%;background:#0F172A;border:8px solid #E9C46A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:76px;color:#E9C46A}
.cst b{font-weight:800;font-size:54px;line-height:1.1;color:#fff}
.cst small{display:block;font-weight:600;font-size:28px;color:#94A3B8;margin-top:10px}
.h2a{position:absolute;left:110px;top:160px;width:1700px;font-weight:800;font-size:86px;line-height:1.08;letter-spacing:-.03em;color:#fff}
.h2a span{color:#E9C46A}
.ez{position:absolute;left:150px;top:0;bottom:0;width:1620px;display:flex;flex-direction:column;justify-content:center}
.ez .n{display:inline-flex;align-items:center;gap:22px;font-weight:800;font-size:34px;letter-spacing:.14em;text-transform:uppercase}
.ez .n b{display:inline-flex;width:84px;height:84px;border-radius:50%;align-items:center;justify-content:center;font-size:44px;letter-spacing:0;background:#DC2626;color:#fff}
.ez .q{font-weight:800;font-size:108px;line-height:1.05;letter-spacing:-.035em;margin-top:40px}
.ez .s{display:flex;gap:18px;margin-top:50px}
.ez .s div{padding:16px 32px;border-radius:999px;font-weight:700;font-size:32px}
.ez .bar5{display:flex;gap:12px;margin-top:70px}
.ez .bar5 i{display:block;width:120px;height:12px;border-radius:6px;opacity:.25}
.ez .bar5 i.on{opacity:1}
.cream .ez .n{color:#B91C1C}.cream .ez .q{color:#0F172A}.cream .ez .q span{color:#2563EB}
.cream .ez .s div{background:#fff;border:2px solid #E7DFC9;color:#0F172A}.cream .ez .bar5 i{background:#0F172A}
.navy .ez .n{color:#FCA5A5}.navy .ez .q{color:#fff}.navy .ez .q span{color:#E9C46A}
.navy .ez .s div{background:#1E293B;border:2px solid #475569;color:#F1F5F9}.navy .ez .bar5 i{background:#E9C46A}
.blue .ez .n{color:#FECACA}.blue .ez .n b{background:#fff;color:#1D4ED8}.blue .ez .q{color:#fff}.blue .ez .q span{color:#FDE68A}
.blue .ez .s div{background:rgba(255,255,255,.14);border:2px solid rgba(255,255,255,.35);color:#fff}.blue .ez .bar5 i{background:#fff}
.res{position:absolute;left:0;right:0;top:420px;display:flex;justify-content:center;gap:40px}
.res div{width:500px;height:360px;border-radius:30px;background:#fff;border:2px solid #FECACA;box-shadow:0 24px 60px rgba(15,23,42,.08);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:28px}
.res i{font-style:normal;width:110px;height:110px;border-radius:50%;background:#FEE2E2;color:#DC2626;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:60px}
.res b{font-weight:800;font-size:46px;color:#0F172A;text-align:center;line-height:1.15}
.reflex{display:inline-flex;align-items:center;gap:16px;padding:14px 28px;border-radius:999px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:30px;letter-spacing:.06em;text-transform:uppercase;align-self:flex-start}
.reflex i{font-style:normal;display:flex;width:44px;height:44px;border-radius:50%;background:#16A34A;color:#fff;align-items:center;justify-content:center;font-size:26px;letter-spacing:0}
.fac{position:absolute;left:1000px;top:130px;width:760px;height:860px;border-radius:18px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.14);padding:50px 56px}
.fac .h1{font-weight:800;font-size:52px;color:#0F172A}
.fac .no{display:inline-block;margin-top:14px;padding:10px 22px;border-radius:12px;background:#EFF6FF;color:#1D4ED8;font-weight:800;font-size:34px}
.fac .ex{position:absolute;right:30px;top:30px}
.ml{display:flex;align-items:center;gap:22px;margin-top:30px;padding:20px 26px;border-radius:18px;background:#F8FAFC;border:2px solid #E2E8F0;font-weight:700;font-size:32px;color:#0F172A}
.ml i{font-style:normal;flex:none;width:48px;height:48px;border-radius:50%;background:#DCFCE7;color:#16A34A;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:800}
.ec{position:absolute;left:0;right:0;top:200px;display:flex;flex-direction:column;align-items:center;text-align:center}
.ec .q{font-weight:800;font-size:84px;line-height:1.1;letter-spacing:-.03em;color:#0F172A}
.ec .a{margin-top:60px;display:inline-flex;align-items:center;gap:26px;padding:30px 50px;border-radius:30px;background:#0F172A;color:#fff;font-weight:800;font-size:54px}
.ec .a span{color:#E9C46A}
.ec .b{margin-top:34px;font-weight:700;font-size:40px;color:#2563EB}
.ec .w{margin-top:70px;padding:12px 28px;border-radius:999px;background:#F1F5F9;color:#64748B;font-weight:600;font-size:26px}
.srcs{position:absolute;left:110px;top:330px;width:900px}
.src{display:flex;align-items:center;gap:26px;margin-bottom:30px;padding:28px 34px;border-radius:26px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07)}
.src .ic{flex:none;width:84px;height:84px;border-radius:22px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:40px}
.src b{font-weight:800;font-size:40px;color:#0F172A}
.src small{display:block;font-weight:600;font-size:26px;color:#64748B;margin-top:4px}
.eom2{position:absolute;left:1140px;top:300px;width:660px;height:600px;border-radius:30px;background:#FEF2F2;border:2px solid #FECACA;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.eom2 .d{font-weight:800;font-size:38px;color:#7F1D1D;letter-spacing:.1em}
.eom2 .qm2{font-weight:800;font-size:260px;line-height:1;color:#DC2626}
.eom2 .t{font-weight:800;font-size:44px;color:#7F1D1D;line-height:1.2;padding:0 40px}
.payres{display:inline-flex;align-items:center;gap:18px;margin-top:40px;padding:20px 34px;border-radius:22px;background:#2563EB;color:#fff;font-weight:800;font-size:36px;align-self:flex-start}
.uptd{display:inline-block;margin-top:28px;padding:14px 28px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:800;font-size:30px;align-self:flex-start}
.voc{display:flex;align-items:center;gap:14px;margin-top:14px;padding:12px 16px;border-radius:16px;background:#DCFCE7}
.voc b{flex:none;width:44px;height:44px;border-radius:50%;background:#16A34A;display:flex;align-items:center;justify-content:center}
.voc b i{display:block;width:0;height:0;border-left:14px solid #fff;border-top:9px solid transparent;border-bottom:9px solid transparent;margin-left:4px}
.voc span{flex:1;height:28px;background:repeating-linear-gradient(90deg,#86EFAC 0 5px,transparent 5px 10px);border-radius:4px}
.thr{width:420px;padding:24px;border-radius:26px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.12)}
.thr .l{height:14px;border-radius:7px;background:#E2E8F0;margin-top:16px}
.thr .k{margin-top:16px;padding:12px 16px;border-radius:14px;background:#FEF3C7;color:#92400E;font-weight:800;font-size:24px}
.later{position:absolute;left:110px;top:780px;display:flex;align-items:center;gap:30px}
.later .c{width:170px;height:170px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.08);overflow:hidden;text-align:center}
.later .c div{height:50px;background:#2563EB;color:#fff;font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center}
.later .c b{display:block;font-weight:800;font-size:72px;color:#0F172A;margin-top:12px}
.later .t{font-weight:800;font-size:48px;color:#0F172A}
.later .z{padding:16px 30px;border-radius:999px;background:#FEE2E2;color:#B91C1C;font-weight:800;font-size:36px}
.call{position:absolute;left:110px;top:330px;width:900px}
.sp{display:inline-block;margin:0 18px 26px 0;padding:22px 34px;border-radius:40px;background:#fff;border:3px dashed #94A3B8;font-weight:800;font-size:40px;color:#334155}
.mis{position:absolute;left:110px;top:760px;font-weight:800;font-size:56px;color:#0F172A}
.mis span{color:#DC2626}
.vsx{position:absolute;left:1100px;top:300px;width:720px;height:520px}
.vsx .bb{position:absolute;width:420px;padding:36px;border-radius:40px;font-weight:800;font-size:42px;text-align:center}
.vsx .bb.a{left:0;top:40px;background:#2563EB;color:#fff;border-bottom-left-radius:10px}
.vsx .bb.b{right:0;top:330px;background:#0F172A;color:#fff;border-bottom-right-radius:10px}
.vsx .vs{position:absolute;left:300px;top:190px;width:120px;height:120px;border-radius:50%;background:#E9C46A;color:#0F172A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:44px;z-index:3}
.cond{position:absolute;left:1000px;top:150px;width:820px;padding:46px 50px;border-radius:30px;background:#FFFDF7;border:2px solid #E7DFC9;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.cond .tt{font-weight:800;font-size:44px;color:#0F172A}
.cond .ex2{display:inline-block;margin-left:16px;padding:4px 14px;border-radius:999px;background:#F1F5F9;color:#64748B;font-weight:700;font-size:20px;vertical-align:middle}
.cond .r{display:flex;gap:20px;margin-top:28px;font-weight:700;font-size:32px;line-height:1.3;color:#334155}
.cond .r i{font-style:normal;flex:none;width:50px;height:50px;border-radius:50%;background:#0F172A;color:#E9C46A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:24px}
.sent{margin-top:34px;display:flex;align-items:center;gap:16px;padding:20px 26px;border-radius:20px;background:#EFF6FF;border:2px solid #BFDBFE;font-weight:800;font-size:28px;color:#1D4ED8}
.steps3{position:absolute;left:110px;top:430px;width:820px}
.s3{display:flex;align-items:center;gap:24px;margin-bottom:26px;padding:24px 30px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07);font-weight:800;font-size:36px;color:#0F172A}
.s3 b{flex:none;width:60px;height:60px;border-radius:50%;background:#16A34A;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px}
.eve2{position:absolute;left:110px;top:560px;display:flex;gap:30px}
.eve2 div{padding:26px 46px;border-radius:26px;background:#1E293B;border:2px solid #475569;font-weight:800;font-size:58px;color:#fff}
.eve2 div span{color:#E9C46A}
.tm{position:absolute;left:110px;top:330px;width:620px;height:620px;border-radius:50%;background:#fff;border:22px solid #E2E8F0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.tm b{font-weight:800;font-size:190px;line-height:1;letter-spacing:-.05em;color:#2563EB}
.tm small{font-weight:800;font-size:48px;color:#0F172A}
.tm svg{position:absolute;left:-22px;top:-22px}
.cl4{position:absolute;left:880px;top:300px;width:940px}
.cq{display:flex;align-items:center;gap:26px;margin-bottom:26px;padding:28px 34px;border-radius:26px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07);font-weight:800;font-size:42px;color:#0F172A}
.cq i{font-style:normal;flex:none;width:66px;height:66px;border-radius:18px;border:5px solid #CBD5E1;background:#fff;color:#fff;display:flex;align-items:center;justify-content:center;font-size:36px}
.light4{position:absolute;left:880px;right:0;top:130px;text-align:left;font-weight:800;font-size:64px;color:#0F172A;letter-spacing:-.02em}
.light4 span{color:#16A34A}
.gcol{position:absolute;left:110px;top:150px;width:780px}
.gcol img.lg{width:400px}
.gcol .b{font-weight:800;font-size:58px;line-height:1.12;letter-spacing:-.02em;color:#0F172A;margin-top:34px}
.gcol .b span{color:#2563EB}
.gl{display:flex;align-items:center;gap:20px;margin-top:22px;padding:18px 26px;border-radius:20px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 10px 26px rgba(15,23,42,.06);font-weight:800;font-size:34px;color:#0F172A}
.gl i{font-style:normal;flex:none;width:50px;height:50px;border-radius:14px;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px}
.gshot{position:absolute;left:960px;width:880px;background:#fff;border-radius:22px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.gshot img{display:block;width:880px}
"""

body, js = "", ""


def ecard(id_, start, end, num, q, tags, cls, tag_times, label=None):
    bars = "".join(f'<i{" class=on" if i < num else ""}></i>' for i in range(5))
    tg = "".join(f'<div class="hid" id="{id_}g{i}">{t}</div>' for i, t in enumerate(tags))
    lab = label or f"Erreur {num} sur 5"
    logo = LOGO if cls == "cream" else LOGOW
    h = f'''
<div id="{id_}" class="clip {cls}" data-start="{start}" data-duration="{round(end - start, 2)}" data-track-index="1">
  {logo}
  <div class="ez"><div class="n hid" id="{id_}n"><b>{num}</b>{lab}</div>
    <div class="q hid" id="{id_}q">{q}</div><div class="s">{tg}</div><div class="bar5">{bars}</div></div>
</div>'''
    j = pop(f"#{id_}n", start + .05, E) + pop(f"#{id_}q", start + .2, E, 50)
    j += "".join(pop(f"#{id_}g{i}", t) for i, t in enumerate(tag_times))
    return h, j


def clip(id_, cls, start, end, inner):
    return f'''
<div id="{id_}" class="clip {cls}" data-start="{start}" data-duration="{round(end - start, 2)}" data-track-index="1">
{inner}
</div>'''


REFLEX = '<div class="reflex hid" id="{id}"><i>✓</i>Le bon réflexe</div>'

# ---------- A : accroche (0 -> 6.43) — phrase lisible dès l'image 0
apps = [("@", "#2563EB", "Vos mails", 2.27), ("✆", "#16A34A", "WhatsApp", 3.35), ("✎", "#B7791F", "Votre carnet", 4.28)]
apph = "".join(f'<div class="app hid" id="aa{i}"><div class="ic" style="background:{c}">{s}</div><b>{n}</b><div class="x hid" id="ax{i}">✕</div></div>'
               for i, (s, c, n, _) in enumerate(apps))
body += clip("a", "light", 0, 6.43, f'''  {LOGO}
  <div class="hq"><div class="q">« Vous pouvez me renvoyer<br/><span>ma facture&nbsp;?</span>&nbsp;»</div></div>
  <div class="apps">{apph}</div>
  <div class="nf hid" id="anf">Introuvable.</div>''')
for i, (_, _, _, t) in enumerate(apps):
    js += pop(f"#aa{i}", t, y=40) + pop(f"#ax{i}", t + .55, "back.out(2)", 0)
js += 'tl.fromTo("#anf",{opacity:0,scale:1.4},{opacity:1,scale:1,duration:.45,ease:"back.out(1.8)"},5.04);\n'

# ---------- B : ce que ça coûte (6.43 -> 14.03)
body += clip("b", "navy", 6.43, 14.03, f'''  {LOGOW}
  <div class="h2a hid" id="bh">Tarologue, voyante, médium<br/><span>à votre compte&nbsp;?</span></div>
  <div class="costs"><div class="cst hid" id="bc0"><div class="ic">⏱</div><div><b>Du temps</b><small>chercher, refaire, vérifier</small></div></div>
    <div class="cst hid" id="bc1"><div class="ic">€</div><div><b>Parfois<br/>de l'argent</b><small>une séance jamais réglée</small></div></div></div>''')
js += pop("#bh", 6.5, E, 40) + pop("#bc0", 9.59, y=50) + pop("#bc1", 12.72, y=50)

# ---------- T : 5 erreurs (14.03 -> 18.33)
tt = ["Factures<br/>sans numéro", "Qui a<br/>payé&nbsp;?", "Notes<br/>éparpillées", "Rien<br/>d'écrit", "Tout<br/>le soir"]
tth = "".join(f'<div class="hid" id="tq{i}"><b>{i + 1}</b><span>{t}</span></div>' for i, t in enumerate(tt))
body += clip("t", "light", 14.03, 18.33, f'''  {LOGO}
  <div class="titleT" style="top:130px"><div class="k hid" id="tk">PRATICIENNES EN GUIDANCE</div>
    <div class="b hid" id="tb" style="font-size:88px">5 erreurs administratives<br/><span>fréquentes</span></div></div>
  <div class="t5">{tth}</div>
  <div class="gpbadge" style="top:840px"><div class="hid" id="tgp">À corriger dès cette semaine</div></div>''')
js += pop("#tk", 14.08, E) + pop("#tb", 14.2, E, 40)
js += "".join(pop(f"#tq{i}", 14.7 + i * .25, y=50) for i in range(5)) + pop("#tgp", 15.6)

# ---------- E1 carte (18.33 -> 22.76)
h, j = ecard("e1", 18.33, 22.76, 1, "Des factures faites<br/><span>à la main</span>", ["Au dernier moment", "Sans numéro"], "cream", [20.94, 21.92])
body += h; js += j

# ---------- E1 résultat (22.76 -> 25.83)
rs = [("?", "Des oublis", 22.76), ("2×", "Des doublons", 23.71), ("…", "Une cliente<br/>qui attend", 24.42)]
rsh = "".join(f'<div class="hid" id="r1{i}"><i>{a}</i><b>{b}</b></div>' for i, (a, b, _) in enumerate(rs))
body += clip("e1b", "light", 22.76, 25.83, f'''  {LOGO}
  <div class="hdr" style="top:150px"><div class="chap hid" id="e1bc" style="color:#DC2626"><b style="background:#DC2626">1</b>Résultat</div></div>
  <div class="res">{rsh}</div>''')
js += pop("#e1bc", 22.8, E) + "".join(pop(f"#r1{i}", t, y=50) for i, (_, _, t) in enumerate(rs))

# ---------- E1 bon réflexe (25.83 -> 34.13)
ml = [("Un numéro à la suite", 27.95), ("Vos coordonnées", 29.09), ("Celles de votre cliente", 30.23), ("La date", 31.54), ("La prestation et le montant", 31.97)]
mlh = "".join(f'<div class="ml hid" id="m{i}"><i>✓</i>{a}</div>' for i, (a, _) in enumerate(ml))
body += clip("e1c", "light", 25.83, 34.13, f'''  {LOGO}
  <div class="col" style="width:820px">{REFLEX.format(id="e1r")}
    <div class="h hid" id="e1h" style="font-size:76px">Une facture<br/><span>par séance</span></div>
    <div class="uptd hid" id="e1u">numérotée à la suite</div></div>
  <div class="fac hid" id="e1f"><span class="illus ex">Exemple</span><div class="h1">Facture</div><div class="no">N° 2026-041</div>{mlh}</div>''')
js += pop("#e1r", 25.9, E) + pop("#e1h", 26.7, E, 40) + fin("#e1f", 26.9) + pop("#e1u", 27.95)
js += "".join(pop(f"#m{i}", t, y=20) for i, (_, t) in enumerate(ml))

# ---------- E1 expert-comptable (34.13 -> 40.39)
body += clip("e1d", "warm", 34.13, 40.39, f'''  {LOGO}
  <div class="ec"><div class="q hid" id="ecq">Les mentions propres<br/>à votre statut&nbsp;?</div>
    <div class="a hid" id="eca">Demandez à votre <span>expert-comptable</span></div>
    <div class="b hid" id="ecb">C'est lui qui connaît votre situation.</div>
    <div class="w hid" id="ecw">Cette vidéo ne remplace pas un conseil juridique ou fiscal.</div></div>''')
js += pop("#ecq", 34.2, E, 40) + pop("#eca", 35.72, "back.out(1.6)", 40) + pop("#ecb", 37.62) + pop("#ecw", 38.4)

# ---------- CTA abonnement (40.39 -> 48.52)
body += clip("c", "navy", 40.39, 48.52, f'''  {LOGOW}
  <div class="ctaC"><div class="k hid" id="ck">CES CONSEILS VOUS SONT UTILES&nbsp;?</div>
    <div class="b hid" id="cb">2 vidéos par semaine<br/><span>pour les praticiennes</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="dsc hid" id="cd" style="left:420px;right:420px">↓ L'outil présenté à la fin&nbsp;: <b>lien dans la description</b></div>''')
js += pop("#ck", 40.45, E) + pop("#cy", 41.93, "back.out(2)") + pop("#cb", 42.79, E, 40) + pop("#cd", 44.74)
js += 'tl.to("#cy",{scale:1.07,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"},43.4);\n'

# ---------- E2 carte (48.52 -> 51.72)
h, j = ecard("e2", 48.52, 51.72, 2, "Ne plus savoir<br/><span>qui a payé</span>", [], "navy", [])
body += h; js += j

# ---------- E2 problème (51.72 -> 58.57)
sr = [("⇄", "#EFF6FF", "#2563EB", "Un virement ici", "« je vous l'ai fait hier »", 51.72),
      ("▭", "#F5F3FF", "#7C3AED", "Un paiement en ligne là", "sur une autre appli", 52.77),
      ("€", "#FBF3DC", "#B7791F", "Des espèces", "au salon du bien-être", 54.12)]
srh = "".join(f'<div class="src hid" id="s{i}"><div class="ic" style="background:{bg};color:{c}">{ic}</div><div><b>{a}</b><small>{b}</small></div></div>'
              for i, (ic, bg, c, a, b, _) in enumerate(sr))
body += clip("e2b", "light", 51.72, 58.57, f'''  {LOGO}
  <div class="hdr" style="top:150px"><div class="chap hid" id="e2bc" style="color:#DC2626"><b style="background:#DC2626">2</b>Le problème</div></div>
  <div class="srcs">{srh}</div>
  <div class="eom2 hid" id="eo"><div class="d">FIN DU MOIS</div><div class="qm2">?</div><div class="t hid" id="eot">Impossible<br/>de faire le point</div></div>''')
js += pop("#e2bc", 51.75, E) + "".join(pop(f"#s{i}", t, y=40) for i, (*_, t) in enumerate(sr))
js += fin("#eo", 55.9) + pop("#eot", 56.98)

# ---------- E2 bon réflexe (58.57 -> 68.45)
lr = [("CM", "Camille M.", "Tirage 3 cartes · 26/10", "v", "Payé", 59.64), ("SL", "Sophie L.", "Guidance écrite · 27/10", "q", "À encaisser", 60.3),
      ("NR", "Nadia R.", "Guidance vocale · 28/10", "q", "À encaisser", 60.9)]
lrh = "".join(f'<div class="lr hid" id="l{i}"><div class="ic">{a}</div><div><div class="a">{b}</div><div class="b">{c}</div></div>'
              f'<div class="st {s}" id="ls{i}">{t}</div></div>' for i, (a, b, c, s, t, _) in enumerate(lr))
body += clip("e2c", "light", 58.57, 68.45, f'''  {LOGO}
  <div class="col" style="width:720px">{REFLEX.format(id="e2r")}
    <div class="h hid" id="e2h" style="font-size:76px">Un seul relevé,<br/><span>à jour le jour même</span></div>
    <div class="payres hid" id="e2p">Régler à la réservation</div></div>
  <div class="ledger hid" id="e2l"><span class="illus" style="right:30px;top:30px">Exemple</span>
    <div class="tt">Mes règlements</div><div class="dd">Octobre · noms fictifs</div>{lrh}
    <div class="eom hid" id="e2t" style="text-decoration:none;color:#0F172A;background:#DCFCE7">Payé, ou à encaisser&nbsp;: c'est tout.</div></div>''')
js += pop("#e2r", 58.62, E) + pop("#e2h", 59.0, E, 40) + fin("#e2l", 59.3)
js += "".join(pop(f"#l{i}", t, y=20) for i, (*_, t) in enumerate(lr))
js += 'tl.to("#ls1",{backgroundColor:"#DCFCE7",color:"#15803D",duration:.3},62.19);\n' + 'tl.set("#ls1",{textContent:"Payé"},62.3);\n'
js += pop("#e2t", 62.6) + pop("#e2p", 64.96, "back.out(1.8)")

# ---------- E3 carte (68.45 -> 71.82)
h, j = ecard("e3", 68.45, 71.82, 3, "Des guidances et des notes<br/><span>éparpillées</span>", [], "blue", [])
body += h; js += j

# ---------- E3 problème (71.82 -> 80.88)
body += clip("e3b", "warm", 71.82, 80.88, f'''  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="e3bc" style="color:#DC2626"><b style="background:#DC2626">3</b>Le problème</div></div>
  <div class="scat hid" id="sc0" style="left:150px;top:300px;transform:rotate(-5deg)"><div class="book" style="position:relative"><b></b></div>
    <div style="margin-top:20px;font-weight:800;font-size:32px;color:#0F172A">Un tirage dans un carnet</div></div>
  <div class="scat hid" id="sc1" style="left:640px;top:330px;transform:rotate(3deg)"><div class="msg">Message vocal<div class="voc"><b><i></i></b><span></span></div></div>
    <div style="margin-top:20px;font-weight:800;font-size:32px;color:#0F172A">Un vocal sur WhatsApp</div></div>
  <div class="scat hid" id="sc2" style="left:1200px;top:290px;transform:rotate(-2deg)"><div class="thr"><div class="l"></div><div class="l" style="width:70%"></div>
    <div class="k">« Et pour mon travail&nbsp;? »</div><div class="l"></div><div class="l" style="width:60%"></div></div>
    <div style="margin-top:20px;font-weight:800;font-size:32px;color:#0F172A">Une question perdue dans un fil</div></div>
  <div class="later"><div class="c hid" id="lc"><div>+ 3 MOIS</div><b>☾</b></div>
    <div class="t hid" id="lt">Elle revient…</div><div class="z hid" id="lz">vous repartez de zéro</div></div>''')
js += pop("#e3bc", 71.85, E) + pop("#sc0", 71.82, y=40) + pop("#sc1", 73.23, y=40) + pop("#sc2", 74.82, y=40)
js += pop("#lc", 77.11) + pop("#lt", 77.4) + pop("#lz", 79.71, "back.out(1.8)")

# ---------- E3 bon réflexe (80.88 -> 86.52)
evs = [("Dates", "12/06 · 18/09 · 29/10", "", 82.9), ("Questions", "travail, déménagement", " g", 83.7), ("Guidances livrées", "écrite + vocale, rangées", " p", 84.44)]
evh = "".join(f'<div class="ev hid" id="v{i}" style="top:{220 + i * 150}px"><div class="dt{c}"></div><div><div class="tx">{a}</div><div class="sm">{b}</div></div></div>'
              for i, (a, b, c, _) in enumerate(evs))
body += clip("e3c", "light", 80.88, 86.52, f'''  {LOGO}
  <div class="col" style="width:700px">{REFLEX.format(id="e3r")}
    <div class="h hid" id="e3h" style="font-size:76px">Une fiche<br/><span>par cliente</span></div></div>
  <div class="card hid" id="e3k"><span class="illus" style="right:24px;top:24px">Illustration</span>
    <div class="ch"><div class="av">CM</div><div><div class="nm">Camille M.</div><div class="sb">cliente depuis juin · nom fictif</div></div></div>
    <div class="vline"></div>{evh}</div>''')
js += pop("#e3r", 80.93, E) + pop("#e3h", 81.73, E, 40) + fin("#e3k", 81.9)
js += "".join(pop(f"#v{i}", t, y=20) for i, (*_, t) in enumerate(evs))

# ---------- E4 carte (86.52 -> 89.10)
h, j = ecard("e4", 86.52, 89.1, 4, "Aucune trace<br/><span>écrite</span>", [], "cream", [])
body += h; js += j

# ---------- E4 problème (89.10 -> 97.75)
sp = [("Annulation&nbsp;?", 89.1), ("Report", 90.5), ("Remboursement", 91.07)]
sph = "".join(f'<div class="sp hid" id="p{i}">{a}</div>' for i, (a, _) in enumerate(sp))
body += clip("e4b", "light", 89.1, 97.75, f'''  {LOGO}
  <div class="hdr" style="top:150px"><div class="chap hid" id="e4bc" style="color:#DC2626"><b style="background:#DC2626">4</b>Tout se dit au téléphone</div></div>
  <div class="call">{sph}</div>
  <div class="mis hid" id="mi">Un malentendu… <span>et rien d'écrit.</span></div>
  <div class="vsx"><div class="bb a hid" id="vb0">Votre parole</div><div class="vs hid" id="vv">VS</div><div class="bb b hid" id="vb1">La sienne</div></div>''')
js += pop("#e4bc", 89.15, E) + "".join(pop(f"#p{i}", t) for i, (_, t) in enumerate(sp)) + pop("#mi", 93.46, E, 40)
js += 'tl.fromTo("#p0,#p1,#p2",{opacity:1},{opacity:.35,duration:.6},92.1);\n'
js += pop("#vb0", 95.45) + pop("#vv", 95.9, "back.out(2)") + pop("#vb1", 96.2)

# ---------- E4 bon réflexe (97.75 -> 106.21)
s3 = [("Écrivez-les une fois", 97.9), ("Envoyez-les avant la première séance", 101.25), ("Gardez les échanges par écrit", 103.26)]
s3h = "".join(f'<div class="s3 hid" id="t3{i}"><b>{i + 1}</b>{a}</div>' for i, (a, _) in enumerate(s3))
body += clip("e4c", "light", 97.75, 106.21, f'''  {LOGO}
  <div class="hdr" style="top:150px;width:800px">{REFLEX.format(id="e4r")}
    <div class="h hid" id="e4h" style="font-size:66px">Vos conditions,<br/><span>noir sur blanc</span></div></div>
  <div class="steps3">{s3h}</div>
  <div class="cond hid" id="cnd"><div class="tt">Mes conditions <span class="ex2">Exemple</span></div>
    <div class="r"><i>1</i>Annulation&nbsp;: merci de prévenir 24&nbsp;h avant.</div>
    <div class="r"><i>2</i>Report&nbsp;: possible une fois, selon mes disponibilités.</div>
    <div class="r"><i>3</i>Guidance écrite&nbsp;: livrée sous 48&nbsp;h.</div>
    <div class="sent hid" id="cs">✓ Envoyées avec la confirmation du rendez-vous</div></div>''')
js += pop("#e4r", 97.8, E) + pop("#e4h", 98.1, E, 40) + fin("#cnd", 98.4)
js += "".join(pop(f"#t3{i}", t, y=30) for i, (_, t) in enumerate(s3)) + pop("#cs", 101.6)

# ---------- E5 carte (106.21 -> 110.61)
body += clip("e5", "navy", 106.21, 110.61, f'''  {LOGOW}
  <div class="ez"><div class="n hid" id="e5n"><b>5</b>Et la dernière</div>
    <div class="q hid" id="e5q">Tout garder pour<br/><span>le soir ou le dimanche</span></div>
    <div class="s"><div class="hid" id="e5g0">21 h, encore devant l'écran</div><div class="hid" id="e5g1">Dimanche après-midi</div></div>
    <div class="bar5"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i></div></div>''')
js += pop("#e5n", 106.26, E) + pop("#e5q", 108.43, E, 50) + pop("#e5g0", 109.2) + pop("#e5g1", 109.7)

# ---------- E5 bon réflexe (110.61 -> 123.54)
cq = [("Le paiement est reçu&nbsp;?", 113.46), ("La facture est prête&nbsp;?", 114.94), ("La guidance est livrée&nbsp;?", 116.75), ("Les notes sont rangées&nbsp;?", 118.24)]
cqh = "".join(f'<div class="cq hid" id="q{i}"><i id="qi{i}">✓</i>{a}</div>' for i, (a, _) in enumerate(cq))
ring = ('<svg width="620" height="620" viewBox="0 0 620 620"><circle id="tring" cx="310" cy="310" r="299" fill="none" stroke="#2563EB" stroke-width="22" '
        'stroke-linecap="round" stroke-dasharray="1879" stroke-dashoffset="1879" transform="rotate(-90 310 310)"/></svg>')
body += clip("e5b", "light", 110.61, 123.54, f'''  {LOGO}
  <div class="hdr" style="top:120px">{REFLEX.format(id="e5r")}</div>
  <div class="tm hid" id="tm">{ring}<b>10</b><small>minutes après<br/>chaque séance</small></div>
  <div class="cl4">{cqh}</div>
  <div class="light4 hid" id="l4" style="top:935px;font-size:50px">4 questions, <span>une semaine légère.</span></div>''')
js += pop("#e5r", 110.66, E) + 'tl.fromTo("#tm",{opacity:0,scale:.85},{opacity:1,scale:1,duration:.6,ease:"back.out(1.6)"},111.89);\n'
js += 'tl.to("#tring",{attr:{"stroke-dashoffset":0},duration:9,ease:"none"},112.2);\n'
for i, (_, t) in enumerate(cq):
    js += pop(f"#q{i}", t, y=30) + f'tl.to("#qi{i}",{{backgroundColor:"#16A34A",borderColor:"#16A34A",duration:.3}},{t + .9});\n'
js += pop("#l4", 120.05, E, 30)

# ---------- récap (123.54 -> 134.41)
rc = [("Des factures numérotées<br/><span>dès la séance</span>", 124.61, ""), ("Un seul endroit pour<br/><span>paiements et clientes</span>", 126.87, " g"),
      ("Des conditions<br/><span>écrites</span>", 129.29, "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += clip("r", "light", 123.54, 134.41, f'''  {LOGO}
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>
  <div class="gpbadge" style="top:840px"><div class="hid" id="rb">⏱ Le tout vérifié en 10 minutes après chaque séance</div></div>''')
js += pop("#rk", 123.6, E) + "".join(pop(f"#rc{i}", t, y=50) for i, (_, t, _) in enumerate(rc)) + pop("#rb", 130.78)

# ---------- GuidPilot (134.41 -> 148.05)
gl = [("€", "Paiement à la réservation", 140.1), ("◉", "Fiche cliente", 142.1), ("♪", "Guidances écrites ou vocales,<br/>dans un espace privé", 142.87), ("F", "Factures générées automatiquement", 146.03)]
glh = "".join(f'<div class="gl hid" id="gg{i}"><i>{a}</i><span>{b}</span></div>' for i, (a, b, _) in enumerate(gl))
DEMO = '<div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">Compte de démonstration</span></div>'
body += clip("g", "light", 134.41, 148.05, f'''
  <div class="gcol"><img class="lg hid" id="glg" src="assets/logo_couleur.png" alt="GuidPilot" />
    <div class="b hid" id="gb">Un outil conçu pour<br/><span>les praticiennes en guidance</span></div>{glh}</div>
  <div class="gshot hid" id="gs0" style="top:150px">{DEMO}<img src="assets/guid.png" alt="" /></div>
  <div class="gshot hid" id="gs1" style="top:700px">{DEMO}<img src="assets/finance.png" alt="" /></div>''')
js += 'tl.fromTo("#glg",{opacity:0,scale:.92},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},134.5);\n' + pop("#gb", 136.66, E, 40)
js += "".join(pop(f"#gg{i}", t, y=20) for i, (_, _, t) in enumerate(gl)) + fin("#gs0", 137.6) + fin("#gs1", 146.03)

# ---------- fin marine (148.05 -> DUR)
body += f'''
<div id="z" class="clip navy" data-start="148.05" data-duration="{round(DUR - 148.05, 2)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard hid" id="z7">✓ Sans carte bancaire</div>
    <div class="url hid" id="z8">guidpilot.fr</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += 'tl.fromTo("#z6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},148.1);\n'
js += pop("#z7", 150.18) + pop("#z8", 151.27) + pop("#z9", 152.74)
js += 'tl.to("#z9",{scale:1.06,duration:.45,yoyo:true,repeat:3,ease:"sine.inOut"},153.6);\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA4}{EXTRA5}{EXTRA6}</style></head><body>
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

d = ATELIER / "build" / "yt-erreurs-admin"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "guid.png", "finance.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
