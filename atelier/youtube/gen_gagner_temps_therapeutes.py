"""Vidéo YouTube 1920x1080 : « Logiciel pour thérapeute : comment gagner du temps sur vos rendez-vous, paiements et factures »
(PRÉSENTATION + offre de Noël · public thérapeutes, mardi 17/11/2026 — programme du 17/11 au 31/12/2026).
Usage : python3 gen_gagner_temps_therapeutes.py <voix.wav> [DUR]  -> build/yt-gagner-temps/
Voix : 10 paragraphes générés un par un (voix/2026-11-17_yt-gagner-temps-p1..p10.mp3), assemblés dans l'ordre
p1,p2,p3,p5,p4,p6..p10 avec assembler_voix.py (p5 = CTA oral d'abonnement + rappel de l'offre de Noël, ~30 %). Total 177,5 s.
Temps T = début des phrases (silencedetect -30 dB / 0,22 s sur le wav assemblé + découpage des phrases).
Structure « une journée de cabinet en 5 moments » (nouvelle) : accroche 21:00 + liste du soir -> calcul que la personne
fait elle-même (20 min/jour = ? h/mois) -> 5 moments horodatés (9:00, 12:30, 17:45, 19:00, J+3), chacun = carte plein
écran à fond changeant avec frise des heures -> « avant » illustré -> « avec GuidPilot » (illustrations + captures démo
finance.png et avis.png) -> récap 3 cartes -> retour au calcul -> offre de Noël (20 s) -> écran de fin.
Offre de Noël (exception validée par Normane jusqu'au 31/12/2026) : 99 € payés une fois, 29 €/mois et 348 € en comparaison.
Aucune personne, aucun superlatif, aucun vocabulaire médical, aucun gain de temps chiffré promis.
Réutilise CSS et helpers de gen_payer_avant_guidance.py (et sa chaîne).
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_payer_avant_guidance.py").read_text()
ns = {"__file__": str(HERE / "gen_payer_avant_guidance.py")}
_argv = sys.argv[:]
sys.argv = sys.argv[:2]
exec(src.split("\nT = dict(")[0], ns)
sys.argv = _argv
CSS, EXTRA, EXTRA4, EXTRA5, EXTRA7, EXTRA8, EXTRA9, EXTRA10, ATELIER, KIT = (ns[k] for k in (
    "CSS", "EXTRA", "EXTRA4", "EXTRA5", "EXTRA7", "EXTRA8", "EXTRA9", "EXTRA10", "ATELIER", "KIT"))
pop, fin, phone, LOGO, LOGOW, E = (ns[k] for k in ("pop", "fin", "phone", "LOGO", "LOGOW", "E"))
LOCK = ('<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round">'
        '<rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>')

DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 179.6
r2 = lambda x: round(x, 2)

EXTRA11 = """
.td11{position:absolute;left:1080px;top:230px;width:740px;border-radius:30px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.35);overflow:hidden}
.td11 .hd{height:100px;padding:0 36px;display:flex;align-items:center;justify-content:space-between;background:#F1F5F9;font-weight:800;font-size:34px;color:#0F172A}
.td11 .hd small{padding:8px 18px;border-radius:999px;background:#0F172A;color:#E9C46A;font-size:26px}
.td11 .rw{display:flex;align-items:center;gap:24px;padding:30px 36px;border-top:2px solid #E2E8F0;font-weight:700;font-size:34px;color:#334155}
.td11 .rw i{font-style:normal;flex:none;width:44px;height:44px;border-radius:12px;border:4px solid #CBD5E1}
.day5{position:absolute;left:110px;right:110px;top:400px;display:flex;gap:26px}
.day5 .c{flex:1;height:400px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.08);padding:40px 34px;display:flex;flex-direction:column;justify-content:space-between}
.day5 .c b{font-weight:800;font-size:64px;letter-spacing:-.03em;color:#2563EB}
.day5 .c.g b{color:#B7791F}
.day5 .c div{font-weight:800;font-size:36px;line-height:1.15;color:#0F172A}
.eq{position:absolute;left:0;right:0;top:330px;display:flex;justify-content:center;align-items:center;gap:40px}
.eq .bx{width:400px;height:300px;border-radius:36px;background:#fff;border:3px solid #E7DFC9;box-shadow:0 24px 60px rgba(15,23,42,.08);display:flex;flex-direction:column;align-items:center;justify-content:center}
.eq .bx b{font-weight:800;font-size:120px;letter-spacing:-.04em;color:#0F172A;line-height:1}
.eq .bx small{font-weight:700;font-size:34px;color:#6B4E16;margin-top:18px}
.eq .bx.q{background:#0F172A;border-color:#0F172A}.eq .bx.q b{color:#E9C46A}.eq .bx.q small{color:#CBD5E1}
.eq .op{font-weight:800;font-size:96px;color:#B7791F}
.eqT{position:absolute;left:0;right:0;top:130px;text-align:center}
.eqT .h{font-size:76px;color:#0F172A}
.eqB{position:absolute;left:0;right:0;top:760px;text-align:center}
.eqB div{display:inline-block;padding:22px 48px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:42px}
.eqB div span{color:#E9C46A}
.bank{position:absolute;left:1080px;top:240px;width:740px;border-radius:30px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.35);overflow:hidden}
.bank .hd{height:96px;padding:0 36px;display:flex;align-items:center;background:#F1F5F9;font-weight:800;font-size:32px;color:#0F172A}
.bank .rw{display:flex;justify-content:space-between;padding:28px 36px;border-top:2px solid #E2E8F0;font-weight:700;font-size:32px;color:#334155}
.bank .rw.q{background:#FEF3C7;color:#92400E}
.tw11{display:flex;flex-direction:column;gap:24px;margin-top:40px}
.tw11 div{display:flex;align-items:center;gap:22px;padding:26px 34px;border-radius:26px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 14px 36px rgba(15,23,42,.07);font-weight:800;font-size:40px;color:#0F172A}
.tw11 div i{font-style:normal;flex:none;width:70px;height:70px;border-radius:20px;background:#EFF6FF;color:#2563EB;display:flex;align-items:center;justify-content:center;font-size:36px}
.conf{position:absolute;left:1010px;top:250px;width:800px;border-radius:30px;padding:46px 50px;background:#fff;border:3px solid #16A34A;box-shadow:0 30px 80px rgba(22,163,74,.15)}
.conf .k{font-weight:800;font-size:28px;letter-spacing:.12em;color:#16A34A}
.conf .t{font-weight:800;font-size:50px;color:#0F172A;margin-top:22px;line-height:1.1}
.conf .rw{display:flex;align-items:center;gap:20px;margin-top:26px;font-weight:700;font-size:34px;color:#334155}
.conf .rw i{font-style:normal;flex:none;width:52px;height:52px;border-radius:14px;background:#DCFCE7;color:#16A34A;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800}
.capf{position:absolute;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.capf img{display:block;width:100%}
.capf .dm{position:absolute;right:18px;top:14px;font-size:20px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:4px 16px}
.ring{position:absolute;border:7px solid #E9C46A;border-radius:26px;box-shadow:0 0 0 9999px rgba(15,23,42,.0)}
.mail{margin:30px 22px 0;padding:26px;border-radius:22px;background:#fff;border:2px solid #E2E8F0}
.mail .f{font-weight:700;font-size:20px;color:#64748B}
.mail .s{font-weight:800;font-size:27px;line-height:1.25;color:#0F172A;margin-top:10px}
.mail .b{font-weight:600;font-size:22px;line-height:1.35;color:#475569;margin-top:12px}
.mail .bt{margin-top:18px;height:60px;border-radius:14px;background:#2563EB;color:#fff;font-weight:800;font-size:23px;display:flex;align-items:center;justify-content:center}
.nop2{display:flex;gap:20px;margin-top:40px}
.nop2 div{padding:16px 30px;border-radius:999px;background:#7F1D1D;color:#FECACA;font-weight:800;font-size:32px;text-decoration:line-through;text-decoration-thickness:3px}
.fi11{position:absolute;left:1000px;top:200px;width:820px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.fi11 .hd{display:flex;align-items:center;gap:22px;padding:34px 40px;background:#0F172A;color:#fff;font-weight:800;font-size:40px}
.fi11 .hd i{font-style:normal;width:76px;height:76px;border-radius:50%;background:#E9C46A;color:#0F172A;display:flex;align-items:center;justify-content:center;font-size:32px}
.fi11 .tb{display:flex;gap:14px;padding:24px 40px 0}
.fi11 .tb span{padding:10px 22px;border-radius:999px;background:#F1F5F9;font-weight:700;font-size:24px;color:#475569}
.fi11 .tb span.on{background:#2563EB;color:#fff}
.fi11 .nt11{margin:26px 40px 40px;padding:30px;border-radius:22px;background:#FBF3DC;border:2px solid #E9C46A}
.fi11 .nt11 .k{display:flex;align-items:center;gap:12px;font-weight:800;font-size:26px;letter-spacing:.08em;color:#6B4E16}
.fi11 .nt11 .l{font-weight:600;font-size:30px;line-height:1.4;color:#334155;margin-top:16px}
.pv{display:inline-flex;align-items:center;gap:14px;margin:0 40px 36px;padding:16px 28px;border-radius:999px;background:#0F172A;color:#E9C46A;font-weight:800;font-size:28px}
.strk{display:flex;flex-direction:column;gap:28px;margin-top:50px}
.strk div{display:flex;align-items:center;gap:26px;padding:30px 40px;border-radius:26px;background:#fff;border:2px solid #E7DFC9;box-shadow:0 14px 36px rgba(15,23,42,.07);font-weight:800;font-size:48px;color:#0F172A}
.strk div i{font-style:normal;flex:none;width:70px;height:70px;border-radius:50%;background:#FEE2E2;color:#B91C1C;display:flex;align-items:center;justify-content:center;font-size:34px}
.strk div small{margin-left:auto;font-weight:700;font-size:28px;color:#B91C1C}
.fl11{position:absolute;left:110px;right:110px;top:380px;display:flex;align-items:center;gap:30px}
.fl11 .fk11{flex:1;height:400px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.08);padding:44px 40px;display:flex;flex-direction:column;justify-content:space-between}
.fl11 .fk11 i{font-style:normal;display:flex;width:110px;height:110px;border-radius:28px;background:#EFF6FF;color:#2563EB;align-items:center;justify-content:center;font-size:56px;font-weight:800}
.fl11 .fk11.g i{background:#FBF3DC;color:#B7791F}
.fl11 .fk11.n{background:#0F172A;border-color:#0F172A}.fl11 .fk11.n i{background:#1E293B}.fl11 .fk11.n b{color:#fff}.fl11 .fk11.n small{color:#CBD5E1}
.fl11 .fk11 b{font-weight:800;font-size:46px;line-height:1.1;color:#0F172A}
.fl11 .fk11 small{display:block;font-weight:600;font-size:26px;color:#64748B;margin-top:10px}
.fl11 .ar{flex:none;font-weight:800;font-size:70px;color:#2563EB}
.inv{position:absolute;left:1060px;top:200px;width:740px;border-radius:30px;padding:50px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.inv .k{display:flex;justify-content:space-between;font-weight:800;font-size:30px;letter-spacing:.1em;color:#2563EB}
.inv .ln{height:18px;border-radius:9px;background:#E2E8F0;margin-top:28px}
.inv .rw{display:flex;justify-content:space-between;margin-top:34px;font-weight:700;font-size:34px;color:#334155}
.inv .ok{display:inline-flex;align-items:center;gap:14px;margin-top:40px;padding:16px 30px;border-radius:999px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:32px}
.inv .au{display:inline-flex;margin:40px 0 0 16px;padding:16px 30px;border-radius:999px;background:#0F172A;color:#E9C46A;font-weight:800;font-size:32px}
.gift{position:absolute;left:0;right:0;top:640px;text-align:center}
.gift div{display:inline-flex;align-items:center;gap:18px;padding:24px 48px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:42px}
.xm{position:absolute;left:260px;right:260px;top:260px;border-radius:40px;padding:46px 60px;background:#1E293B;border:3px solid #E9C46A;text-align:center}
.xm .k{font-weight:800;font-size:30px;letter-spacing:.12em;color:#E9C46A}
.xm .p{font-weight:800;font-size:120px;letter-spacing:-.04em;line-height:1;color:#fff;margin-top:22px}
.xm .p span{color:#E9C46A}
.xm .s{font-weight:800;font-size:42px;color:#fff;margin-top:20px}
.xm .c{font-weight:600;font-size:32px;color:#CBD5E1;margin-top:14px}
.xm .np{display:inline-flex;align-items:center;gap:14px;margin-top:26px;padding:14px 30px;border-radius:999px;background:#14532D;color:#BBF7D0;font-weight:800;font-size:32px}
.xm .ch{font-weight:700;font-size:30px;color:#93C5FD;margin-top:30px}
.xm .cs{display:flex;justify-content:center;gap:18px;margin-top:16px}
.xm .cs div{padding:14px 28px;border-radius:999px;background:#0F172A;border:2px solid #475569;color:#F1F5F9;font-weight:800;font-size:30px}
.top14{position:absolute;left:0;right:0;top:150px;text-align:center}
.top14 div{display:inline-block;padding:14px 36px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:800;font-size:34px}
.endo{display:inline-flex;align-items:center;gap:16px;margin-top:40px;padding:20px 44px;border-radius:999px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:52px}
.endd{font-weight:700;font-size:38px;color:#CBD5E1;margin-top:22px}
"""

T = dict(
    il=0.47, vot=1.73, fac=9.12, pai=10.2, cr=11.2, vid=12.21, ce=15.31,
    av=21.25, calc=22.4, comb=26.56, pren=28.36, gard=29.9, temps=31.45,
    m1=33.92, msg=36.96, sam=38.79, fin1=39.87, une=41.84, cinq=43.07, avec1=44.66, ouvre=45.75, voit=47.59, mom=49.62, arr=50.74,
    cta=54.21, abo=56.89, xmas=59.6, gp=61.19, payes=65.16, lien=66.44,
    m2=68.86, avez=69.88, ouv=72.39, avec2=75.47, enl=79.62, cab=81.09, tab=82.52, enc=84.59,
    m3=86.92, vous3=90.05, rap=93.39, pend=95.54, notes=97.06, priv=101.31,
    m4=103.74, avant4=105.86, env=108.0, fact=110.64, avec4=111.77, audio=113.6, arr4=117.68, fac4=118.97,
    m5=122.03, son=125.38, futur=127.6,
    rs=131.48, s1=132.95, s2=136.26, s3=140.0, rep=145.78, chq=147.91,
    o=152.6, osi=156.1, o99=158.6, opaye=160.9, olieu=162.6, opre=165.1, ofin=166.9, oren=169.02, omois=169.79, oarr=170.71,
    z=172.7, zabo=174.9)

body, js = "", ""
HOURS = ["9:00", "12:30", "17:45", "19:00", "J+3"]


def mcard(id_, start, end, num, title, cls, logo, lead):
    st = "".join(f'<div class="st{" on" if i == num - 1 else ""}"><i>{"✓" if i < num - 1 else i + 1}</i>{s}</div>' for i, s in enumerate(HOURS))
    h = f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(start)}" data-duration="{r2(end - start)}" data-track-index="1">
  {logo}
  <div class="fz"><div class="n hid" id="{id_}n"><b>{num}</b>{HOURS[num - 1]} · Moment {num} sur 5</div>
    <div class="t hid" id="{id_}t">{title}</div><div class="w hid" id="{id_}w">{lead}</div>
    <div class="fr"><div class="ln"></div>{st}</div></div>
</div>'''
    j = pop(f"#{id_}n", start + .05, E) + pop(f"#{id_}t", start + .2, "back.out(1.3)", 50) + pop(f"#{id_}w", start + .9)
    return h, j


def clip(id_, cls, a, b, inner, logo=None):
    lg = logo if logo is not None else (LOGOW if cls in ("navy", "eve", "blue") else LOGO)
    return f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(a)}" data-duration="{r2(b - a)}" data-track-index="1">
  {lg}
{inner}
</div>'''


# ---------- A : accroche (0 -> vid), lisible dès l'image 0
rows = [("fac", "Facture de la séance de 18 h"), ("pai", "Vérifier le virement de mardi"), ("cr", "Envoyer le compte rendu")]
rh = "".join(f'<div class="rw" id="a{k}"><i></i>{t}</div>' for k, t in rows)
body += clip("a", "navy", 0, T["vid"], f'''
  <div class="hk9" style="top:240px;width:940px"><div class="q" style="font-size:104px">Séance finie à 19&nbsp;h.<br/><span>Encore au bureau à&nbsp;21&nbsp;h.</span></div>
    <div class="s hid" id="as1">Votre journée de cabinet<br/><b>continue… sur l'ordinateur.</b></div></div>
  <div class="td11"><div class="hd">À faire ce soir<small>21:00</small></div>{rh}</div>''')
js += pop("#as1", T["vot"] + 2.5, E) + "".join(f'tl.to("#a{k} i",{{backgroundColor:"#E9C46A",borderColor:"#E9C46A",duration:.3}},{T[k]});\n' for k, _ in rows)

# ---------- B : la journée (vid -> av)
d5 = [("9:00", "Caler une séance", ""), ("12:30", "Vérifier un paiement", "g"), ("17:45", "Rappel et notes", ""),
      ("19:00", "Compte rendu et facture", "g"), ("J+3", "Demander un avis", "")]
dh = "".join(f'<div class="c {g} hid" id="bd{k}"><b>{h_}</b><div>{t}</div></div>' for k, (h_, t, g) in enumerate(d5))
body += clip("b", "light", T["vid"], T["av"], f'''
  <div class="hdr" style="top:120px"><div class="chap hid" id="bc"><b>5</b>Moments d'une journée</div>
    <div class="h hid" id="bh" style="font-size:70px">Une journée de cabinet, <span>tâche par tâche</span></div></div>
  <div class="day5">{dh}</div>
  <div class="both hid" id="bs" style="top:880px"><div>Logiciel pour thérapeute · <span>récupérer ce temps</span></div></div>''')
js += pop("#bc", T["vid"] + .05, E) + pop("#bh", T["vid"] + .25, E, 40)
js += "".join(pop(f"#bd{k}", T["vid"] + 1.4 + k * .5, y=50) for k in range(5)) + pop("#bs", T["ce"] + 1.0, "back.out(2)")

# ---------- C : le calcul (av -> m1)
body += clip("c", "cream", T["av"], T["m1"], f'''
  <div class="eqT"><div class="chap hid" id="cc" style="color:#B7791F"><b style="background:#0F172A;color:#E9C46A">✎</b>Votre calcul</div></div>
  <div class="eq"><div class="bx hid" id="ce0"><b>20 min</b><small>d'administratif</small></div><div class="op hid" id="ce1">×</div>
    <div class="bx hid" id="ce2"><b>1 jour</b><small>de cabinet</small></div><div class="op hid" id="ce3">=</div>
    <div class="bx q hid" id="ce4"><b>?&nbsp;h</b><small>par mois</small></div></div>
  <div class="eqB hid" id="cb"><div>Gardez <span>votre</span> chiffre en tête</div></div>''')
js += pop("#cc", T["av"] + .05, E) + pop("#ce0", T["calc"] + .8) + pop("#ce1", T["calc"] + 1.6) + pop("#ce2", T["calc"] + 2.2)
js += pop("#ce3", T["comb"]) + pop("#ce4", T["comb"] + .3, "back.out(2)")
js += f'tl.to("#ce4",{{scale:1.07,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(T["pren"])});\n' + pop("#cb", T["gard"], "back.out(2)")

# ---------- Moment 1 : caler une séance
h, j = mcard("f1", T["m1"], T["msg"], 1, "Les messages <span>pour caler une séance</span>", "cream", LOGO, "Le matin, avant votre première cliente")
body += h; js += j
conv = ('<div class="phead"><div class="av">L</div>Léa M.</div>'
        '<div style="position:absolute;left:0;right:0;top:150px">'
        '<div class="b8 hid" id="g1a">Bonjour&nbsp;! Vous auriez une place jeudi&nbsp;?</div>'
        '<div class="b8 me hid" id="g1b">Jeudi c\'est complet, désolée…</div>'
        '<div class="b8 hid" id="g1c">Et samedi&nbsp;?</div>'
        '<div class="b8 hid" id="g1d">Finalement, plutôt vendredi 🙏</div></div>')
body += clip("g1", "eve", T["msg"], T["avec1"], f'''
  <div class="hk9" style="top:250px;width:940px"><div class="chap" style="color:#93C5FD"><b style="background:#E9C46A;color:#0F172A">✕</b>Avant</div>
    <div class="q hid" id="g1q" style="font-size:96px;margin-top:30px">Pour une seule séance…</div></div>
  <div class="eff9 hid" id="g1e" style="top:720px">5 ou 6 échanges</div>
  {phone("g1ph", conv, 1290, 100)}''')
js += fin("#g1ph", T["msg"] + .05) + pop("#g1a", T["msg"] + .3) + pop("#g1b", T["msg"] + 1.1) + pop("#g1c", T["sam"]) + pop("#g1d", T["fin1"] + .2)
js += pop("#g1q", T["une"], E, 40) + pop("#g1e", T["cinq"], "back.out(1.8)")

book = ('<div class="phead"><div class="av">CE</div>Cabinet Exemple</div>'
        '<div class="bio"><div class="a">Séance de sophrologie · 1 h</div><div class="b">Au cabinet ou en visio</div></div>'
        '<div class="gr9"><div class="x">Jeu 10:00</div><div id="h1v">Ven 18:00</div><div>Sam 9:30</div><div>Lun 14:00</div>'
        '<div class="x">Mar 11:00</div><div>Mer 17:00</div></div>'
        '<div class="bk9 hid" id="h1k">Réserver et régler</div>')
body += clip("h1", "light", T["avec1"], T["cta"], f'''
  <div class="col" style="width:820px"><div class="chap hid" id="h1c"><b>✓</b>Avec GuidPilot</div>
    <div class="h hid" id="h1h" style="font-size:80px">Elle réserve<br/><span>seule</span></div>
    <div class="ok8 hid" id="h1o1"><i>✓</i>Vos créneaux libres, visibles</div>
    <div class="ok8 hid" id="h1o2"><i>✓</i>Au moment qui lui convient</div>
    <div class="ok8 hid" id="h1o3"><i>✓</i>Directement dans votre agenda</div></div>
  {phone("h1ph", book, 1240, 100)}''')
js += pop("#h1c", T["avec1"] + .05, E) + pop("#h1h", T["avec1"] + .25, E, 40) + fin("#h1ph", T["ouvre"])
js += pop("#h1o1", T["voit"]) + f'tl.to("#h1v",{{backgroundColor:"#2563EB",borderColor:"#2563EB",color:"#FFFFFF",duration:.3}},{r2(T["voit"] + .8)});\n'
js += pop("#h1k", T["mom"]) + pop("#h1o2", T["mom"] + .2) + pop("#h1o3", T["arr"] + .3)

# ---------- CTA oral abonnement + offre (cta -> m2)
body += clip("cta", "navy", T["cta"], T["m2"], f'''
  <div class="ctaC" style="top:110px"><div class="k hid" id="ck">CES CONSEILS VOUS AIDENT&nbsp;?</div>
    <div class="b hid" id="cb2">2 vidéos par semaine<br/><span>pour votre cabinet</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="gift hid" id="cg"><div>🎁 Jusqu'au 31 décembre&nbsp;: 1 an pour 99&nbsp;€, payé une fois</div></div>
  <div class="dsc hid" id="cd" style="top:820px">↓ <span><b>Le lien</b> est dans la description</span></div>''')
js += pop("#ck", T["cta"] + .1, E) + pop("#cb2", T["cta"] + .6, E, 40) + pop("#cy", T["abo"], "back.out(2)")
js += f'tl.to("#cy",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(T["abo"] + .8)});\n'
js += pop("#cg", T["xmas"] + .2, "back.out(1.8)") + pop("#cd", T["lien"])

# ---------- Moment 2 : paiement
h, j = mcard("f2", T["m2"], T["ouv"], 2, "Vérifier <span>qui a payé</span>", "navy", LOGOW, "Midi et demi, entre deux séances")
body += h; js += j
body += clip("g2", "eve", T["ouv"], T["avec2"], '''
  <div class="hk9" style="top:300px;width:900px"><div class="q" style="font-size:92px">Le virement de mardi…<br/><span>il est arrivé&nbsp;?</span></div></div>
  <div class="bank hid" id="g2b"><span class="illus" style="right:24px;top:28px">Illustration</span><div class="hd">Relevé de compte</div>
    <div class="rw"><span>Virement · L. Martin</span><span>✓</span></div>
    <div class="rw"><span>Carte · Librairie</span><span>—</span></div>
    <div class="rw q"><span>Virement de… ?</span><span>🔍</span></div>
    <div class="rw"><span>Prélèvement · Téléphone</span><span>—</span></div></div>''')
js += fin("#g2b", T["ouv"] + .1)
body += clip("h2", "light", T["avec2"], T["tab"], f'''
  <div class="col" style="width:840px"><div class="chap hid" id="h2c"><b>✓</b>Avec GuidPilot</div>
    <div class="h hid" id="h2h" style="font-size:72px">Le règlement se fait<br/><span>à la réservation</span></div>
    <div class="tw11"><div class="hid" id="h2t0"><i>💳</i>En ligne</div><div class="hid" id="h2t1"><i>⌂</i>Ou au cabinet, si vous préférez</div></div></div>
  <div class="conf hid" id="h2f"><span class="illus" style="right:24px;top:24px">Illustration</span><div class="k">RÉSERVATION CONFIRMÉE</div>
    <div class="t">Séance de sophrologie · 1 h</div>
    <div class="rw"><i>✓</i>Vendredi · 18:00</div><div class="rw"><i>✓</i>Dans votre agenda</div><div class="rw"><i>✓</i>Règlement reçu</div></div>''')
js += pop("#h2c", T["avec2"] + .05, E) + pop("#h2h", T["avec2"] + .25, E, 40) + fin("#h2f", T["avec2"] + 1.2)
js += pop("#h2t0", T["enl"]) + pop("#h2t1", T["cab"])
# finance.png 1270x240 -> 1600x302 ; « À encaisser » x 340-617, y 95-185
sc = 1600 / 1270
body += clip("h2d", "light", T["tab"], T["m3"], f'''
  <div class="hdr" style="top:120px"><div class="chap hid" id="h2dc"><b>✓</b>Tableau de bord</div>
    <div class="h hid" id="h2dh" style="font-size:70px">Encaissé, <span>et reste à encaisser</span></div></div>
  <div class="capf hid" id="h2cap" style="left:160px;top:420px;width:1600px"><img src="assets/finance.png" alt="" /><span class="dm">Compte de démonstration</span></div>
  <div class="ring hid" id="h2r" style="left:{r2(160 + 340 * sc - 14)}px;top:{r2(420 + 95 * sc - 14)}px;width:{r2(277 * sc + 28)}px;height:{r2(90 * sc + 28)}px"></div>
  <div class="both hid" id="h2b" style="top:840px"><div>D'un coup d'œil · <span>sans ouvrir votre banque</span></div></div>''')
js += pop("#h2dc", T["tab"] + .05, E) + pop("#h2dh", T["tab"] + .25, E, 40) + fin("#h2cap", T["tab"] + .5, 0)
js += pop("#h2r", T["enc"] + .3, "back.out(2)") + pop("#h2b", T["enc"] + .8, "back.out(2)")

# ---------- Moment 3 : rappel et notes
h, j = mcard("f3", T["m3"], T["vous3"], 3, "Le rappel <span>et vos notes</span>", "cream", LOGO, "Juste avant la séance")
body += h; js += j
mail = ('<div class="phead"><div class="av">✉</div>Boîte de réception</div>'
        '<div class="mail hid" id="g3m"><div class="f">Cabinet Exemple · hier</div><div class="s">Rappel&nbsp;: votre séance demain à 18:00</div>'
        '<div class="b">Séance de sophrologie · 1 h<br/>Au cabinet</div><div class="bt">Voir mon rendez-vous</div></div>')
body += clip("g3", "eve", T["vous3"], T["pend"], f'''
  <div class="hk9" style="top:280px;width:900px"><div class="q" style="font-size:100px">Le rappel<br/><span>est déjà parti.</span></div>
    <div class="s hid" id="g3s"><b>Par e-mail,</b> sans message à écrire</div>
    <div class="nop2"><div class="hid" id="g3n">Écrire à chaque cliente</div></div></div>
  {phone("g3ph", mail, 1290, 100)}''')
js += fin("#g3ph", T["vous3"] + .05) + pop("#g3n", T["vous3"] + .8) + pop("#g3m", T["rap"] - .3, "back.out(1.6)") + pop("#g3s", T["rap"])
body += clip("h3", "light", T["pend"], T["m4"], f'''
  <div class="col" style="width:820px"><div class="chap hid" id="h3c"><b>✓</b>Avec GuidPilot</div>
    <div class="h hid" id="h3h" style="font-size:78px">Vos notes,<br/><span>dans sa fiche</span></div>
    <div class="ok8 hid" id="h3o1"><i>✓</i>Relues avant la séance</div>
    <div class="ok8 hid" id="h3o2"><i>✓</i>Jamais visibles par la cliente</div></div>
  <div class="fi11 hid" id="h3f"><span class="illus" style="right:24px;top:24px;background:#1E293B;color:#CBD5E1">Illustration</span>
    <div class="hd"><i>L</i>Fiche · Léa M.</div>
    <div class="tb"><span>Séances</span><span>Paiements</span><span class="on">Notes</span></div>
    <div class="nt11"><div class="k">{LOCK.format(s=30, c="#6B4E16")}NOTES PRIVÉES</div>
      <div class="l">Séance 3 · objectif de la semaine noté<br/>À reprendre&nbsp;: l'exercice de la séance 2<br/>Préfère les créneaux du soir</div></div>
    <div class="pv hid" id="h3p">{LOCK.format(s=28, c="#E9C46A")}Visible par vous seule</div></div>''')
js += pop("#h3c", T["pend"] + .05, E) + pop("#h3h", T["pend"] + .25, E, 40) + fin("#h3f", T["notes"])
js += pop("#h3o1", T["notes"] + 1.2) + pop("#h3p", T["priv"], "back.out(2)") + pop("#h3o2", T["priv"] + .4)

# ---------- Moment 4 : compte rendu et facture
h, j = mcard("f4", T["m4"], T["avant4"], 4, "Compte rendu <span>et facture</span>", "navy", LOGOW, "La séance est finie")
body += h; js += j
sk = [("Rédiger le compte rendu", "avant4", ""), ("L'envoyer par e-mail", "env", ""), ("Faire la facture", "fact", "le soir")]
skh = "".join(f'<div class="hid" id="g4s{k}"><i>✕</i>{t}{f"<small>{s}</small>" if s else ""}</div>' for k, (t, _, s) in enumerate(sk))
body += clip("g4", "cream", T["avant4"], T["avec4"], f'''
  <div class="col" style="width:1400px"><div class="chap" style="color:#B7791F"><b style="background:#0F172A;color:#E9C46A">✕</b>Avant</div>
    <div class="h hid" id="g4h" style="font-size:76px;color:#0F172A">Trois tâches <span>de plus</span></div>
    <div class="strk">{skh}</div></div>''')
js += pop("#g4h", T["avant4"] + .1, E, 40) + "".join(pop(f"#g4s{k}", T[t] + (.6 if k == 0 else 0), y=40) for k, (_, t, _) in enumerate(sk))
body += clip("h4", "light", T["avec4"], T["fac4"], f'''
  <div class="hdr" style="top:120px"><div class="chap hid" id="h4c"><b>✓</b>Avec GuidPilot</div>
    <div class="h hid" id="h4h" style="font-size:70px">Le compte rendu arrive <span>dans son espace</span></div></div>
  <div class="fl11"><div class="fk11 hid" id="h4f0"><i>✎</i><div><b>Écrit</b><small>Votre compte rendu</small></div></div>
    <div class="fk11 g hid" id="h4f1"><i>🎙</i><div><b>Ou en audio</b><small>Enregistré en quelques minutes</small></div></div>
    <div class="ar hid" id="h4a">→</div>
    <div class="fk11 n hid" id="h4f2"><i>{LOCK.format(s=56, c="#E9C46A")}</i><div><b>Espace sécurisé</b><small>De votre cliente</small></div></div></div>''')
js += pop("#h4c", T["avec4"] + .05, E) + pop("#h4h", T["avec4"] + .25, E, 40) + pop("#h4f0", T["avec4"] + 1.4, y=50)
js += pop("#h4f1", T["audio"], y=50) + pop("#h4a", T["arr4"] - .3) + pop("#h4f2", T["arr4"], "back.out(1.8)", 50)
body += clip("h4b", "light", T["fac4"], T["m5"], '''
  <div class="col" style="width:860px"><div class="chap hid" id="h4bc"><b>✓</b>Facture</div>
    <div class="h hid" id="h4bh" style="font-size:80px">Numérotée,<br/><span>créée automatiquement</span></div></div>
  <div class="inv hid" id="h4i"><span class="illus" style="right:24px;top:-44px">Illustration</span>
    <div class="k"><span>FACTURE</span><span>N° 2026-047</span></div><div class="ln" style="width:60%"></div><div class="ln" style="width:40%"></div>
    <div class="rw"><span>Séance de sophrologie · 1 h</span><span>Réglée</span></div>
    <div class="ok">✓ Envoyée dans son espace</div><div class="au">Automatique</div></div>''')
js += pop("#h4bc", T["fac4"] + .05, E) + pop("#h4bh", T["fac4"] + .25, E, 40) + fin("#h4i", T["fac4"] + .3)

# ---------- Moment 5 : avis
h, j = mcard("f5", T["m5"], T["son"], 5, "La demande <span>d'avis</span>", "cream", LOGO, "Quelques jours plus tard, elle part toute seule")
body += h; js += j
body += clip("h5", "light", T["son"], T["rs"], '''
  <div class="hdr" style="top:110px"><div class="chap hid" id="h5c"><b>★</b>Avis</div>
    <div class="h hid" id="h5h" style="font-size:70px">Son avis peut s'afficher <span>sur votre page</span></div></div>
  <div class="capf hid" id="h5cap" style="left:235px;top:360px;width:1450px"><img src="assets/avis.png" alt="" /><span class="dm">Compte de démonstration</span></div>
  <div class="both hid" id="h5b" style="top:840px"><div>Lu par vos futures clientes · <span>avant de réserver</span></div></div>''')
js += pop("#h5c", T["son"] + .05, E) + pop("#h5h", T["son"] + .25, E, 40) + fin("#h5cap", T["son"] + .6, 0) + pop("#h5b", T["futur"], "back.out(2)")

# ---------- récap (rs -> rep)
rc = [("Elle réserve<br/><span>et règle seule</span>", "s1", ""), ("Rappel, facture, avis&nbsp;:<br/><span>sans vous</span>", "s2", " g"),
      ("Chaque cliente,<br/><span>au même endroit</span>", "s3", "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += clip("r", "light", T["rs"], T["rep"], f'''
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>''')
js += pop("#rk", T["rs"] + .05, E) + "".join(pop(f"#rc{i}", T[k] + .2, y=50) for i, (_, k, _) in enumerate(rc))

# ---------- retour au calcul (rep -> o)
body += clip("c2", "cream", T["rep"], T["o"], '''
  <div class="eqT"><div class="chap hid" id="c2c" style="color:#B7791F"><b style="background:#0F172A;color:#E9C46A">✎</b>Reprenez votre calcul</div></div>
  <div class="eq"><div class="bx hid" id="c2e0"><b>20 min</b><small>d'administratif</small></div><div class="op hid" id="c2e1">×</div>
    <div class="bx hid" id="c2e2"><b>1 jour</b><small>de cabinet</small></div><div class="op hid" id="c2e3">=</div>
    <div class="bx q hid" id="c2e4"><b>?&nbsp;h</b><small>par mois</small></div></div>
  <div class="eqB hid" id="c2b"><div>Chaque tâche en moins&nbsp;: <span>du temps pour vous</span></div></div>''')
js += pop("#c2c", T["rep"] + .05, E) + "".join(pop(f"#c2e{k}", T["rep"] + .3 + k * .25) for k in range(5)) + pop("#c2b", T["chq"] + .3, "back.out(2)")

# ---------- offre de Noël (o -> z)
body += clip("o", "navy", T["o"], T["z"], f'''
  <img src="assets/logo_blanc.png" alt="GuidPilot" style="position:absolute;left:50%;top:50px;width:300px;margin-left:-150px" />
  <div class="top14 hid" id="o14"><div>Essai&nbsp;: 14 jours gratuits · sans carte bancaire</div></div>
  <div class="xm hid" id="oxm"><div class="k">🎁 OFFRE DE NOËL · JUSQU'AU 31 DÉCEMBRE</div>
    <div class="p hid" id="op">1 an pour <span>99&nbsp;€</span></div>
    <div class="s hid" id="os">payé une seule fois</div>
    <div class="c hid" id="oc">au lieu de 29&nbsp;€/mois, soit 348&nbsp;€ sur un an</div>
    <div class="np hid" id="on">✓ Aucun prélèvement automatique</div>
    <div class="ch hid" id="och">À la fin de l'année, vous choisissez&nbsp;:</div>
    <div class="cs"><div class="hid" id="oc0">Renouveler</div><div class="hid" id="oc1">Passer au mois</div><div class="hid" id="oc2">Arrêter · données en lecture</div></div></div>''', logo="")
js += pop("#o14", T["o"] + .1, E) + pop("#oxm", T["osi"], E, 40) + pop("#op", T["o99"], "back.out(1.6)", 40) + pop("#os", T["opaye"])
js += pop("#oc", T["olieu"]) + pop("#on", T["opre"], "back.out(2)") + pop("#och", T["ofin"]) + pop("#oc0", T["oren"]) + pop("#oc1", T["omois"]) + pop("#oc2", T["oarr"])

# ---------- écran de fin (z -> DUR)
t = T["z"]
body += f'''
<div id="z" class="clip navy" data-start="{r2(t)}" data-duration="{r2(DUR - t)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:230px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="endo">🎁 1 an pour 99&nbsp;€</div>
    <div class="endd">Jusqu'au 31 décembre · payé une fois</div>
    <div class="url" style="font-size:44px">guidpilot.fr/offre-fondatrice</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += f'tl.fromTo("#z6",{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"}},{r2(t + .1)});\n'
js += pop("#z9", T["zabo"]) + f'tl.to("#z9",{{scale:1.06,duration:.45,yoyo:true,repeat:2,ease:"sine.inOut"}},{r2(T["zabo"] + .6)});\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}{EXTRA4}{EXTRA5}{EXTRA7}{EXTRA8}{EXTRA9}{EXTRA10}{EXTRA11}</style></head><body>
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

d = ATELIER / "build" / "yt-gagner-temps"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "finance.png", "avis.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, DUR)
