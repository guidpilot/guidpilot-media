"""Vidéo YouTube 1920x1080 : « Logiciel pour tarologue et voyante : 1 an pour 99 €, l'offre de Noël expliquée »
(OFFRE DE NOËL · public guidance, vendredi 27/11/2026 — programme du 17/11 au 31/12/2026).
Usage : python3 gen_offre_noel_guidance.py <voix.wav> <voix.json> [DUR]  -> build/yt-offre-noel-guidance/
Voix : 10 paragraphes (voix/2026-11-27_yt-offre-guidance-p1..p10.mp3) ; p3 coupé en deux à 5,41 s (p3a / p3b)
pour placer le CTA oral d'abonnement (p4) à ~25 % ; ordre p1,p2,p3a,p4,p3b,p5..p10 (assembler_voix.py).
Temps : début de paragraphe exact (voix.json) + ancrage des ponctuations sur les silences (silencedetect -32 dB / 0,16 s)
+ interpolation par nombre de caractères (fonction tm()).
Structure NOUVELLE « le ticket de l'année » : accroche « 3 formats de consultation. Combien d'outils ? » (lisible dès
l'image 0) -> 3 formats + 3 outils éparpillés qui se regroupent en une carte 99 € -> calendrier de 12 jetons à 29 €
(compteur jusqu'à 348 €) recouvert par un seul jeton 99 € -> chapitre 1/3 -> CTA -> « ticket » de l'année qui se remplit
(à gauche) + illustration à droite (3 fiches de prestation · téléphone espace client avec guidance audio + notes
privées · captures démo finance.png / avis.png) -> chapitre 2/3 + frise du calendrier (aujourd'hui, 14 jours,
avant le 31/12, 12 mois) -> chapitre 3/3 + 3 panneaux -> 2 questions fréquentes en bulles -> récap -> offre -> fin.
Offre de Noël (exception validée par Normane jusqu'au 31/12/2026) : 99 € payés une fois, 29 €/mois et 348 € en comparaison.
Aucune personne, aucun superlatif, aucune promesse de prédiction ni de rentabilité.
"""
import json, pathlib, re, shutil, subprocess, sys

HERE = pathlib.Path(__file__).parent
src = (HERE / "gen_offre_noel_therapeutes.py").read_text()
ns = {"__file__": str(HERE / "gen_offre_noel_therapeutes.py")}
_argv = sys.argv[:]
sys.argv = sys.argv[:2]
exec(src.split("\nT = {")[0], ns)
sys.argv = _argv
CSS, ATELIER, KIT, LOGO, LOGOW, E, LOCK, EXTRAS, EXTRA13 = (ns[k] for k in
    ("CSS", "ATELIER", "KIT", "LOGO", "LOGOW", "E", "LOCK", "EXTRAS", "EXTRA13"))
pop, setv = ns["pop"], ns["setv"]
r2 = lambda x: round(x, 2)

WAV, JS = sys.argv[1], json.load(open(sys.argv[2]))
DUR = float(sys.argv[3]) if len(sys.argv) > 3 else round(JS["total"] + 4.2, 2)

SEG = [
 "Une consultation de tarot en visio, une guidance écrite, une guidance vocale. Trois formats, et souvent trois outils pour les gérer. Jusqu'au 31 décembre, Guide Pilote vous propose une année entière pour 99 euros, payés une seule fois. Dans cette vidéo, vous saurez ce que cela comprend, comment cela se passe, et ce qui arrive au bout d'un an.",
 "D'abord, le calcul. Au mois, Guide Pilote coûte 29 euros, soit 348 euros sur une année. Avec l'offre de Noël, c'est 99 euros pour les douze mois. Faites la comparaison avec votre propre tarif : 99 euros, cela représente combien de vos consultations ?",
 "Première partie : ce qui est compris. Toutes les fonctions de l'abonnement, sans option à ajouter.",
 "Si ces vidéos vous aident, abonnez-vous : nous en publions deux par semaine pour les praticiennes en guidance. Et le lien de l'offre est en première ligne de la description.",
 "Avant la consultation : votre page de praticienne, avec une fiche par format, visio, guidance écrite ou guidance vocale, avec le tarif et le délai. Votre cliente réserve, règle en ligne, et le rendez-vous arrive dans votre agenda.",
 "Pendant et après : le lien Google Meet pour vos consultations en visio, et la fiche de chaque cliente, avec vos notes personnelles, qu'elle ne voit jamais. Surtout, votre guidance écrite ou vocale est déposée dans son espace client sécurisé. Elle la retrouve quand elle veut, sans fouiller dans une messagerie.",
 "Côté gestion : les factures numérotées se créent automatiquement. Le tableau de bord vous montre ce qui est encaissé, et ce qui reste à encaisser. Les demandes d'avis partent après la consultation, et les avis peuvent s'afficher sur votre page. Aucune commission sur vos consultations, hors frais du moyen de paiement.",
 "Deuxième partie : comment cela se passe. Vous créez votre compte, avec quatorze jours gratuits, sans carte bancaire. Vous testez avec vos vraies prestations. Puis, avant le 31 décembre, vous réglez 99 euros, une seule fois, pour douze mois d'accès complet. Aucun prélèvement automatique : rien ne repart sans votre accord.",
 "Troisième partie : au bout d'un an, c'est vous qui choisissez. Vous renouvelez pour une nouvelle année. Vous passez au mois, sans engagement. Ou vous arrêtez, et vos données restent accessibles en lecture.",
 "Deux questions reviennent souvent. Je suis déjà en essai, est-ce que je peux en profiter ? Oui, vous pouvez choisir l'offre pendant votre essai, jusqu'au 31 décembre. Et si je préfère payer au mois ? C'est possible : le mois à 29 euros reste disponible.",
 "En résumé : toutes les fonctions, de la réservation à la guidance livrée et à la facture. Un seul paiement de 99 euros, sans prélèvement automatique. Et au bout d'un an, vous décidez. Commencez par les quatorze jours gratuits, sans carte bancaire. Le lien est dans la description : 1 an pour 99 euros, jusqu'au 31 décembre.",
]
ST, EN = JS["starts"], JS["ends"]
assert len(ST) == len(SEG)
out = subprocess.run(["ffmpeg", "-i", WAV, "-af", "silencedetect=noise=-32dB:d=0.16", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
SIL = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]


def anchors(i):
    txt, a, b = SEG[i], ST[i], EN[i]
    L = len(txt)
    pts = [(0, a)]
    for m in re.finditer(r"[.,:?;]\s", txt):
        c = m.end()
        est = a + (b - a) * c / L
        cand = [s for s in SIL if a < s < b and abs(s - est) < 1.1 and s > pts[-1][1] + .2]
        if cand:
            pts.append((c, min(cand, key=lambda s: abs(s - est))))
    pts.append((L, b))
    return pts


ANC = [anchors(i) for i in range(len(SEG))]


def tm(i, phrase, occ=1):
    txt = SEG[i]
    k = -1
    for _ in range(occ):
        k = txt.index(phrase, k + 1)
    pts = ANC[i]
    for (c0, t0), (c1, t1) in zip(pts, pts[1:]):
        if c0 <= k <= c1:
            return r2(t0 + (t1 - t0) * (k - c0) / max(1, c1 - c0))
    return r2(EN[i])


EXTRA27 = """
.hk27{position:absolute;left:0;right:0;top:110px;text-align:center}
.hk27 .tg{display:inline-block;padding:12px 32px;border-radius:999px;background:#1E293B;border:2px solid #475569;color:#E2E8F0;font-weight:800;font-size:32px}
.hk27 .q{font-weight:800;font-size:96px;line-height:1.05;letter-spacing:-.035em;color:#fff;margin-top:26px}
.hk27 .q span{color:#E9C46A}
.fm27{position:absolute;left:170px;right:170px;top:470px;display:flex;justify-content:space-between}
.fm27 .f{width:470px;height:200px;border-radius:30px;background:#fff;padding:30px 36px;display:flex;align-items:center;gap:26px}
.fm27 .f i{font-style:normal;flex:none;display:flex;width:96px;height:96px;border-radius:26px;background:#EFF6FF;color:#2563EB;align-items:center;justify-content:center;font-size:50px}
.fm27 .f b{font-weight:800;font-size:44px;line-height:1.1;color:#0F172A}
.tl27{position:absolute;left:170px;right:170px;top:720px;display:flex;justify-content:space-between}
.tl27 div{width:470px;text-align:center}
.tl27 span{display:inline-block;padding:16px 30px;border-radius:16px;background:#1E293B;border:2px dashed #64748B;color:#CBD5E1;font-weight:700;font-size:32px}
.one27{position:absolute;left:560px;right:560px;top:655px;height:255px;border-radius:36px;background:#FBF3DC;border:4px solid #E9C46A;text-align:center;padding-top:26px}
.one27 small{display:block;font-weight:800;font-size:30px;letter-spacing:.1em;color:#6B4E16}
.one27 b{display:block;font-weight:800;font-size:104px;letter-spacing:-.04em;line-height:1.05;color:#0F172A}
.one27 em{font-style:normal;font-weight:700;font-size:30px;color:#6B4E16}
.cal27{position:absolute;left:120px;width:1040px;top:290px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.cal27 div{height:170px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.cal27 div small{font-weight:700;font-size:24px;color:#64748B;text-transform:uppercase;letter-spacing:.06em}
.cal27 div b{font-weight:800;font-size:52px;color:#334155;margin-top:8px}
.cal27 div.on{background:#334155;border-color:#334155}.cal27 div.on small{color:#CBD5E1}.cal27 div.on b{color:#fff}
.tot27{position:absolute;left:1240px;right:110px;top:290px;border-radius:30px;background:#0F172A;padding:40px 44px;color:#fff}
.tot27 small{display:block;font-weight:700;font-size:26px;letter-spacing:.1em;color:#94A3B8;text-transform:uppercase}
.tot27 .nn{position:relative;height:130px;margin-top:10px}
.tot27 .nn b{position:absolute;left:0;top:0;font-weight:800;font-size:110px;letter-spacing:-.03em;color:#fff;opacity:0}
.tot27 em{display:block;font-style:normal;font-weight:700;font-size:28px;color:#94A3B8;margin-top:6px}
.stamp27{position:absolute;left:300px;top:380px;width:680px;height:400px;border-radius:40px;background:#E9C46A;box-shadow:0 30px 80px rgba(15,23,42,.30);text-align:center;padding-top:50px}
.stamp27 small{display:block;font-weight:800;font-size:34px;letter-spacing:.1em;color:#6B4E16}
.stamp27 b{display:block;font-weight:800;font-size:170px;letter-spacing:-.04em;line-height:1;color:#0F172A;margin-top:14px}
.stamp27 em{display:block;font-style:normal;font-weight:800;font-size:36px;color:#0F172A;margin-top:18px}
.ask27{position:absolute;left:1240px;right:110px;top:640px;border-radius:30px;background:#fff;border:3px solid #2563EB;padding:34px 40px;font-weight:800;font-size:44px;line-height:1.15;color:#0F172A}
.ask27 span{color:#2563EB}
.pt27{position:absolute;left:150px;right:150px;top:0;bottom:0;display:flex;align-items:center;gap:80px}
.pt27 .big{flex:none;width:330px;height:330px;border-radius:50%;background:#E9C46A;color:#0F172A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:220px;letter-spacing:-.05em}
.pt27>div:last-child{flex:1}
.pt27 .k{font-weight:800;font-size:34px;letter-spacing:.14em;text-transform:uppercase;color:#93C5FD}
.pt27 .q{font-weight:800;font-size:100px;line-height:1.05;letter-spacing:-.035em;color:#fff;margin-top:24px}
.pt27 .q span{color:#E9C46A}
.pt27 .bar{display:flex;gap:14px;margin-top:44px}
.pt27 .bar i{display:block;width:170px;height:14px;border-radius:7px;background:rgba(255,255,255,.25)}
.pt27 .bar i.on{background:#E9C46A}
.pt27 .ok{display:inline-flex;margin-top:40px;padding:18px 36px;border-radius:999px;background:rgba(255,255,255,.14);border:2px solid rgba(255,255,255,.4);color:#fff;font-weight:800;font-size:36px}
.tk27{position:absolute;left:90px;top:110px;bottom:60px;width:640px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.10);padding:0 0 30px}
.tk27 .hd{height:110px;border-radius:30px 30px 0 0;background:#0F172A;display:flex;flex-direction:column;justify-content:center;padding:0 40px}
.tk27 .hd b{font-weight:800;font-size:38px;color:#E9C46A}
.tk27 .hd small{font-weight:700;font-size:24px;color:#94A3B8;margin-top:4px}
.tk27 .perf{height:0;border-top:4px dashed #E2E8F0;margin:0 26px}
.tk27 .sec{padding:12px 40px 0}
.tk27 .sec .t{font-weight:800;font-size:24px;letter-spacing:.1em;text-transform:uppercase;color:#2563EB;margin-bottom:6px}
.tk27 .ln{display:flex;align-items:center;gap:18px;font-weight:700;font-size:28px;color:#0F172A;height:44px}
.tk27 .ln i{font-style:normal;flex:none;display:flex;width:38px;height:38px;border-radius:50%;background:#DCFCE7;color:#15803D;align-items:center;justify-content:center;font-size:22px;font-weight:800}
.tk27 .ln.dim{color:#CBD5E1}.tk27 .ln.dim i{background:#F1F5F9;color:#CBD5E1}
.tk27 .tot{position:absolute;left:40px;right:40px;bottom:30px;display:flex;justify-content:space-between;align-items:center;padding-top:20px;border-top:3px solid #0F172A;font-weight:800;font-size:36px;color:#0F172A}
.tk27 .tot span{padding:8px 24px;border-radius:999px;background:#E9C46A}
.rt27{position:absolute;left:800px;right:90px;top:110px;bottom:60px}
.rt27 .h{font-weight:800;font-size:76px;letter-spacing:-.02em;color:#0F172A}
.rt27 .h span{color:#2563EB}
.pr27{display:flex;gap:24px;margin-top:50px}
.pr27 .c{flex:1;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 50px rgba(15,23,42,.08);padding:30px 30px}
.pr27 .c i{font-style:normal;display:flex;width:80px;height:80px;border-radius:22px;background:#EFF6FF;color:#2563EB;align-items:center;justify-content:center;font-size:42px}
.pr27 .c b{display:block;font-weight:800;font-size:36px;line-height:1.1;color:#0F172A;margin-top:22px}
.pr27 .c small{display:block;font-weight:700;font-size:25px;color:#64748B;margin-top:14px;line-height:1.45}
.pr27 .c small u{text-decoration:none;color:#0F172A}
.fl27{display:flex;align-items:center;gap:20px;margin-top:44px}
.fl27 div{padding:22px 32px;border-radius:999px;background:#0F172A;color:#fff;font-weight:800;font-size:34px}
.fl27 div.g{background:#E9C46A;color:#0F172A}
.fl27 em{font-style:normal;font-weight:800;font-size:44px;color:#2563EB}
.il27{display:inline-block;margin-top:22px;font-weight:700;font-size:22px;color:#94A3B8}
.ph27{position:absolute;left:0;top:150px;width:430px;height:760px;border-radius:56px;background:#0F172A;padding:18px}
.ph27 .sc{width:100%;height:100%;border-radius:42px;background:#F6F8FC;overflow:hidden;padding:30px 26px}
.ph27 .sc .tt{font-weight:800;font-size:30px;color:#0F172A}
.ph27 .sc .tt small{display:block;font-weight:600;font-size:20px;color:#64748B;margin-top:4px}
.ph27 .pc27{margin-top:22px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;padding:22px}
.ph27 .pc27 b{display:block;font-weight:800;font-size:25px;color:#0F172A}
.ph27 .pc27 small{display:block;font-weight:600;font-size:19px;color:#64748B;margin-top:4px}
.ph27 .pl{display:flex;align-items:center;gap:14px;margin-top:16px}
.ph27 .pl i{font-style:normal;flex:none;display:flex;width:52px;height:52px;border-radius:50%;background:#2563EB;color:#fff;align-items:center;justify-content:center;font-size:22px}
.ph27 .wv{flex:1;display:flex;align-items:center;gap:4px;height:40px}
.ph27 .wv s{display:block;flex:1;border-radius:3px;background:#93C5FD}
.ph27 .tx s{display:block;height:12px;border-radius:6px;background:#E2E8F0;margin-top:12px}
.nt27{position:absolute;left:500px;right:0;top:190px;border-radius:30px;background:#FFFBEF;border:3px solid #E9C46A;padding:30px 34px}
.nt27 .t{display:flex;align-items:center;gap:16px;font-weight:800;font-size:32px;color:#6B4E16}
.nt27 s{display:block;height:14px;border-radius:7px;background:#EDE6D6;margin-top:16px}
.nt27 .no{margin-top:22px;font-weight:800;font-size:28px;color:#B91C1C}
.mt27{position:absolute;left:500px;right:0;top:530px;display:flex;flex-direction:column;gap:20px}
.mt27 div{display:flex;align-items:center;gap:20px;padding:24px 30px;border-radius:24px;background:#fff;border:2px solid #E2E8F0;font-weight:800;font-size:32px;color:#0F172A}
.mt27 div i{font-style:normal;flex:none;display:flex;width:60px;height:60px;border-radius:18px;background:#EFF6FF;color:#2563EB;align-items:center;justify-content:center;font-size:32px}
.mt27 div.x{color:#94A3B8;text-decoration:line-through;background:#F8FAFC}
.cp27{position:absolute;left:0;right:0;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 18px 50px rgba(15,23,42,.12);overflow:hidden}
.cp27 img{display:block;width:100%}
.cp27 .dm{position:absolute;right:14px;top:10px;font-size:18px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:3px 14px}
.ring27{position:absolute;border:6px solid #E9C46A;border-radius:22px}
.cm27{position:absolute;left:0;right:0;top:790px;display:flex;gap:18px}
.cm27 div{padding:18px 30px;border-radius:999px;background:#DCFCE7;color:#15803D;border:2px solid #86EFAC;font-weight:800;font-size:30px}
.road27{position:absolute;left:120px;right:120px;top:520px;height:14px;border-radius:7px;background:#E2E8F0}
.road27 b{position:absolute;left:0;right:0;top:0;bottom:0;border-radius:7px;background:#2563EB;transform-origin:left center}
.st27{position:absolute;top:440px;width:400px;margin-left:-200px;text-align:center}
.st27 .dt{width:96px;height:96px;margin:0 auto;border-radius:50%;background:#fff;border:6px solid #2563EB;display:flex;align-items:center;justify-content:center;font-size:42px}
.st27.g .dt{border-color:#E9C46A;background:#FBF3DC}
.st27 .w{font-weight:800;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:#64748B;margin-top:26px}
.st27 b{display:block;font-weight:800;font-size:40px;line-height:1.12;color:#0F172A;margin-top:12px}
.st27 small{display:block;font-weight:700;font-size:27px;color:#64748B;margin-top:10px}
.st27.g b{color:#6B4E16}
.hd27{position:absolute;left:120px;right:120px;top:140px}
.hd27 .h{font-weight:800;font-size:76px;letter-spacing:-.02em;color:#0F172A}
.hd27 .h span{color:#2563EB}
.np27{position:absolute;left:0;right:0;top:900px;display:flex;justify-content:center;gap:24px}
.np27 div{padding:20px 40px;border-radius:999px;font-weight:800;font-size:38px}
.np27 .a{background:#DCFCE7;color:#15803D;border:2px solid #86EFAC}
.np27 .b{background:#0F172A;color:#fff}
.sg27{position:absolute;left:120px;right:120px;top:350px;display:flex;gap:40px}
.sg27 .p{flex:1;position:relative;height:520px}
.sg27 .p .pole{position:absolute;left:50%;top:150px;bottom:0;width:22px;margin-left:-11px;border-radius:6px;background:#CBD5E1}
.sg27 .p .bd{position:relative;margin:0 20px;border-radius:30px;background:#fff;border:3px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.10);padding:34px 36px;min-height:300px}
.sg27 .p .bd i{font-style:normal;display:flex;width:90px;height:90px;border-radius:26px;background:#EFF6FF;color:#2563EB;align-items:center;justify-content:center;font-size:46px}
.sg27 .p .bd b{display:block;font-weight:800;font-size:50px;color:#0F172A;margin-top:24px}
.sg27 .p .bd small{display:block;font-weight:700;font-size:29px;line-height:1.3;color:#64748B;margin-top:12px}
.sg27 .p.k .bd{border-color:#E9C46A}
.faq27{position:absolute;left:330px;right:330px;top:140px;bottom:150px;border-radius:40px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.10);padding:0 0 30px;overflow:hidden}
.faq27 .hd{height:110px;background:#0F172A;display:flex;align-items:center;gap:20px;padding:0 44px;color:#fff;font-weight:800;font-size:36px}
.faq27 .hd i{font-style:normal;display:flex;width:62px;height:62px;border-radius:50%;background:#E9C46A;color:#0F172A;align-items:center;justify-content:center;font-size:32px}
.faq27 .bx{padding:30px 44px;display:flex;flex-direction:column;gap:22px}
.bq27{align-self:flex-end;max-width:900px;padding:24px 34px;border-radius:30px 30px 8px 30px;background:#2563EB;color:#fff;font-weight:700;font-size:36px;line-height:1.25}
.ba27{align-self:flex-start;max-width:980px;padding:24px 34px;border-radius:30px 30px 30px 8px;background:#F1F5F9;color:#0F172A;font-weight:700;font-size:36px;line-height:1.25}
.ba27 b{color:#15803D}
"""

body, js = "", ""


def clip(id_, cls, a, b, inner, logo=None):
    lg = logo if logo is not None else (LOGOW if cls in ("navy", "eve", "blue") else LOGO)
    return f'''
<div id="{id_}" class="clip {cls}" data-start="{r2(a)}" data-duration="{r2(b - a)}" data-track-index="1">
  {lg}
{inner}
</div>'''


def part(id_, cls, a, b, num, kk, q, extra=""):
    bars = "".join(f'<i class="{"on" if k < num else ""}"></i>' for k in range(3))
    return clip(id_, cls, a, b, f'''
  <div class="pt27"><div class="big hid" id="{id_}b">{num}</div>
    <div><div class="k hid" id="{id_}k">Partie {num} sur 3 · {kk}</div><div class="q hid" id="{id_}q">{q}</div>
      <div class="bar">{bars}</div>{extra}</div></div>''')


def part_js(id_, a):
    return (f'tl.fromTo("#{id_}b",{{opacity:0,scale:.6,rotation:-20}},{{opacity:1,scale:1,rotation:0,duration:.6,ease:"back.out(1.7)"}},{r2(a + .02)});\n'
            + pop(f"#{id_}k", a + .15, E) + pop(f"#{id_}q", a + .3, E, 40))


S = lambda i: ST[i]
END = lambda i: EN[i]

# ---------- 0 : accroche (0 -> S1) — lisible dès l'image 0
t_tar, t_vis = 0.0, tm(0, "guidance écrite")
body += clip("a", "navy", 0, S(1), f'''
  <div class="hk27"><div class="tg">Tarologue · Voyante · Médium</div>
    <div class="q">3 formats de consultation.<br/><span>Combien d'outils&nbsp;?</span></div></div>
  <div class="fm27"><div class="f hid" id="af1"><i>🎥</i><b>Consultation<br/>en visio</b></div>
    <div class="f hid" id="af2"><i>✍</i><b>Guidance<br/>écrite</b></div>
    <div class="f hid" id="af3"><i>🎙</i><b>Guidance<br/>vocale</b></div></div>
  <div class="tl27"><div><span class="hid" id="ao1">Messages privés</span></div><div><span class="hid" id="ao2">E&#8209;mail + virement</span></div>
    <div><span class="hid" id="ao3">Vocal sur messagerie</span></div></div>
  <div class="one27 hid" id="a99"><small>🎁 JUSQU'AU 31 DÉCEMBRE</small><b>1 an · 99&nbsp;€</b><em>payés une seule fois</em></div>
  <div class="chips13" style="top:940px"><div class="hid" id="ac1"><i>1</i>Ce que cela comprend</div><div class="hid" id="ac2"><i>2</i>Comment ça se passe</div>
    <div class="hid" id="ac3"><i>3</i>Au bout d'un an</div></div>''')
js += pop("#af1", .5, "back.out(1.6)") + pop("#af2", tm(0, "une guidance écrite"), "back.out(1.6)") + pop("#af3", tm(0, "une guidance vocale"), "back.out(1.6)")
t3 = tm(0, "Trois formats")
js += pop("#ao1", tm(0, "trois outils")) + pop("#ao2", tm(0, "trois outils") + .35) + pop("#ao3", tm(0, "trois outils") + .7)
t31 = tm(0, "Jusqu'au 31")
js += f'tl.to(".tl27 span",{{opacity:0,y:-60,scale:.6,duration:.5,ease:"power2.in"}},{r2(t31 - .2)});\n'
js += f'tl.to(".fm27",{{y:-40,opacity:.35,duration:.5}},{r2(t31 - .2)});\n'
js += f'tl.fromTo("#a99",{{opacity:0,scale:.7,y:40}},{{opacity:1,scale:1,y:0,duration:.6,ease:"back.out(1.7)"}},{r2(tm(0, "99 euros") - .25)});\n'
tdv = tm(0, "Dans cette vidéo")
js += f'tl.to("#a99",{{y:-40,scale:.85,duration:.5}},{r2(tdv)});\n'
js += pop("#ac1", tm(0, "ce que cela comprend")) + pop("#ac2", tm(0, "comment cela")) + pop("#ac3", tm(0, "ce qui arrive"))

# ---------- 1 : le calcul (S1 -> S2)
cal = "".join(f'<div class="hid" id="m{k}"><small>Mois {k + 1}</small><b>29&nbsp;€</b></div>' for k in range(12))
nums = "".join(f'<b id="n{k}">{29 * (k + 1)}&nbsp;€</b>' for k in range(12))
body += clip("b", "cream", S(1), S(2), f'''
  <div class="hd27" style="top:110px"><div class="chap hid" id="bc" style="color:#B7791F"><b style="background:#0F172A;color:#E9C46A">€</b>Le calcul</div></div>
  <div class="cal27">{cal}</div>
  <div class="tot27 hid" id="bt"><small>Au mois, sur un an</small><div class="nn">{nums}</div><em>29&nbsp;€ × 12 mois</em></div>
  <div class="stamp27 hid" id="bs"><small>🎁 OFFRE DE NOËL</small><b>99&nbsp;€</b><em>pour les 12 mois · payés une fois</em></div>
  <div class="ask27 hid" id="bq">99&nbsp;€ = combien de <span>vos consultations&nbsp;?</span></div>''')
js += pop("#bc", S(1) + .05, E)
ta, tz = tm(1, "Au mois"), tm(1, "348")
js += pop("#bt", ta, E)
for k in range(12):
    tk = r2(ta + .3 + (tz - ta + .2) * k / 11)
    js += pop(f"#m{k}", tk, "back.out(2)", 20) + f'tl.set("#m{k}",{{backgroundColor:"#334155",borderColor:"#334155"}},{tk});tl.set("#m{k} b",{{color:"#fff"}},{tk});tl.set("#m{k} small",{{color:"#CBD5E1"}},{tk});\n'
    js += (setv(f"#n{k - 1}", tk, 0) if k else "") + setv(f"#n{k}", tk)
js += f'tl.fromTo("#bs",{{opacity:0,scale:1.6,rotation:-8}},{{opacity:1,scale:1,rotation:-3,duration:.55,ease:"back.out(1.4)"}},{r2(tm(1, "99 euros pour") - .1)});\n'
js += f'tl.to(".cal27",{{opacity:.35,duration:.4}},{r2(tm(1, "99 euros pour"))});\n'
js += pop("#bq", tm(1, "Faites la comparaison"), "back.out(1.8)")

# ---------- 2 : partie 1 (S2 -> S3)
body += part("p1", "blue", S(2), S(3), 1, "Ce qui est compris", "Qu'est-ce qui est <span>compris&nbsp;?</span>",
             '<div><div class="ok hid" id="p1o">✓ Toutes les fonctions de l\'abonnement · aucune option à ajouter</div></div>')
js += part_js("p1", S(2)) + pop("#p1o", tm(2, "Toutes les fonctions"), "back.out(2)")

# ---------- 3 : CTA oral (S3 -> S4)
a = S(3)
body += clip("cta", "navy", a, S(4), '''
  <div class="ctaC" style="top:110px"><div class="k hid" id="ck">CES VIDÉOS VOUS AIDENT&nbsp;?</div>
    <div class="b hid" id="cb2">2 vidéos par semaine<br/><span>pour les praticiennes en guidance</span></div>
    <div class="ytb hid" id="cy"><i></i>Abonnez-vous</div></div>
  <div class="gift hid" id="cg"><div>🎁 Jusqu'au 31 décembre&nbsp;: 1 an pour 99&nbsp;€, payé une fois</div></div>
  <div class="dsc hid" id="cd" style="top:820px">↓ <span><b>Le lien de l'offre</b> est en 1re ligne de la description</span></div>''')
js += pop("#ck", a + .1, E) + pop("#cb2", a + .5, E, 40) + pop("#cy", tm(3, "abonnez-vous"), "back.out(2)")
js += f'tl.to("#cy",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{r2(tm(3, "abonnez-vous") + .8)});\n'
js += pop("#cg", tm(3, "Et le lien") - .2, "back.out(1.8)") + pop("#cd", tm(3, "première ligne"))

# ---------- ticket de l'année (S4 -> S7), 3 sous-scènes à droite
TK = [("Avant la consultation", [("Votre page de praticienne", 4, "votre page"), ("Une fiche par format", 4, "une fiche"),
                                 ("Réservation + paiement en ligne", 4, "réserve"), ("Agenda", 4, "agenda")]),
      ("Pendant et après", [("Lien Google Meet", 5, "Google Meet"), ("Fiche et notes personnelles", 5, "la fiche"),
                            ("Guidance écrite ou vocale livrée", 5, "votre guidance"), ("Espace client sécurisé", 5, "espace client")]),
      ("Gestion", [("Factures numérotées", 6, "factures"), ("Tableau de bord", 6, "tableau de bord"),
                   ("Demandes d'avis", 6, "demandes d'avis"), ("0 % de commission*", 6, "Aucune commission")])]
lines, tkjs = "", ""
n = 0
for si, (tt, items) in enumerate(TK):
    lines += f'<div class="sec"><div class="t">{tt}</div>'
    for (lab, seg, key) in items:
        lines += f'<div class="ln dim" id="l{n}"><i>✓</i>{lab}</div>'
        t = tm(seg, key)
        tkjs += f'tl.to("#l{n}",{{color:"#0F172A",duration:.25}},{t});tl.to("#l{n} i",{{backgroundColor:"#DCFCE7",color:"#15803D",duration:.25}},{t});\n'
        tkjs += f'tl.fromTo("#l{n}",{{x:-14}},{{x:0,duration:.35,ease:"back.out(2)"}},{t});\n'
        n += 1
    lines += '</div>'
ticket = f'''<div class="tk27"><div class="hd"><b>🎁 Votre année GuidPilot</b><small>Toutes les fonctions de l'abonnement</small></div>
  <div class="perf"></div>{lines}
  <div class="tot"><div>12 mois</div><span>99&nbsp;€ · une fois</span></div></div>'''
# le ticket est posé sur un clip couvrant S4 -> S7 (track 2), les illustrations changent à droite (track 1)
body += f'''
<div id="tk" class="clip light" data-start="{r2(S(4))}" data-duration="{r2(S(7) - S(4))}" data-track-index="1">
  {LOGO}
  {ticket}
  <div class="rt27" id="r1">
    <div class="h hid" id="r1h">Avant <span>la consultation</span></div>
    <div class="pr27"><div class="c hid" id="r1a"><i>🎥</i><b>Consultation en visio</b><small>Durée · <u>votre tarif</u><br/>Lien de visio prévu</small></div>
      <div class="c hid" id="r1b"><i>✍</i><b>Guidance écrite</b><small><u>Votre tarif</u><br/>Délai de livraison affiché</small></div>
      <div class="c hid" id="r1c"><i>🎙</i><b>Guidance vocale</b><small><u>Votre tarif</u><br/>Délai de livraison affiché</small></div></div>
    <div class="il27 hid" id="r1i">Illustration</div>
    <div class="fl27"><div class="hid" id="r1f1">Elle réserve</div><em class="hid" id="r1e1">→</em><div class="g hid" id="r1f2">Elle règle en ligne</div>
      <em class="hid" id="r1e2">→</em><div class="hid" id="r1f3">📅 Votre agenda</div></div>
  </div>
  <div class="rt27" id="r2" style="opacity:0">
    <div class="h hid" id="r2h">Pendant <span>et après</span></div>
    <div class="ph27 hid" id="r2p"><div class="sc"><div class="tt">Mon espace<small>Espace client sécurisé · Illustration</small></div>
      <div class="pc27"><b>🎙 Votre guidance vocale</b><small>Déposée par votre praticienne</small>
        <div class="pl"><i>▶</i><div class="wv">{"".join(f'<s style="height:{h}px"></s>' for h in (14,26,34,20,38,30,16,28,36,22,12,30,24,18,32,26,14,20))}</div></div></div>
      <div class="pc27 tx"><b>✍ Votre guidance écrite</b><s></s><s style="width:80%"></s><s style="width:60%"></s></div>
      <div class="pc27"><b>📅 Mes rendez-vous</b><small>Lien Google Meet prêt</small></div></div></div>
    <div class="nt27 hid" id="r2n"><div class="t">{LOCK.format(s=36, c="#B7791F")}Vos notes personnelles</div><s></s><s style="width:70%"></s>
      <div class="no">Jamais visibles par votre cliente</div></div>
    <div class="mt27"><div class="x hid" id="r2x"><i>💬</i>Chercher le vocal dans la messagerie</div>
      <div class="hid" id="r2y"><i>✓</i>Elle la retrouve quand elle veut</div></div>
  </div>
  <div class="rt27" id="r3" style="opacity:0">
    <div class="h hid" id="r3h">Côté <span>gestion</span></div>
    <div class="cp27 hid" id="r3f" style="top:150px"><img src="assets/finance.png" alt="" /><span class="dm">Compte de démonstration</span></div>
    <div class="ring27 hid" id="r3r" style="top:140px;height:240px;left:-10px;right:-10px"></div>
    <div class="cp27 hid" id="r3a" style="top:470px"><img src="assets/avis.png" alt="" /><span class="dm">Compte de démonstration</span></div>
    <div class="cm27"><div class="hid" id="r3c">0 % de commission sur vos consultations</div><div class="hid" id="r3d" style="background:#fff;color:#64748B;border-color:#E2E8F0">*hors frais du moyen de paiement</div></div>
  </div>
</div>'''
js += pop(".tk27", S(4) + .02, E, 40) + tkjs
js += pop("#r1h", S(4) + .2, E, 40) + pop("#r1a", tm(4, "visio,")) + pop("#r1b", tm(4, "guidance écrite")) + pop("#r1c", tm(4, "guidance vocale"))
js += pop("#r1i", tm(4, "guidance vocale") + .3)
js += f'tl.to(".pr27 u",{{color:"#2563EB",duration:.3}},{tm(4, "avec le tarif")});\n'
js += pop("#r1f1", tm(4, "réserve")) + pop("#r1e1", tm(4, "règle") - .2) + pop("#r1f2", tm(4, "règle"), "back.out(2)")
js += pop("#r1e2", tm(4, "et le rendez-vous")) + pop("#r1f3", tm(4, "arrive"), "back.out(2)")
js += f'tl.to("#r1",{{opacity:0,duration:.35}},{r2(S(5) - .3)});\n' + setv("#r2", S(5) - .05)
js += pop("#r2h", S(5) + .05, E, 40) + pop("#r2p", tm(5, "Google Meet") - .3, E, 60)
js += pop("#r2n", tm(5, "vos notes"), "back.out(1.6)")
js += f'tl.to("#r2p",{{scale:1.04,duration:.4,yoyo:true,repeat:1}},{tm(5, "Surtout")});\n'
js += pop("#r2x", tm(5, "Elle la retrouve")) + pop("#r2y", tm(5, "sans fouiller"), "back.out(2)")
js += f'tl.to("#r2x",{{opacity:.5,duration:.3}},{tm(5, "sans fouiller")});\n'
js += f'tl.to("#r2",{{opacity:0,duration:.35}},{r2(S(6) - .3)});\n' + setv("#r3", S(6) - .05)
js += pop("#r3h", S(6) + .05, E, 40) + pop("#r3f", tm(6, "Le tableau"), E, 60) + pop("#r3r", tm(6, "ce qui reste"), "back.out(2)")
js += pop("#r3a", tm(6, "Les demandes"), E, 60)
js += pop("#r3c", tm(6, "Aucune commission"), "back.out(2)") + pop("#r3d", tm(6, "hors frais"))

# ---------- 7 : partie 2 + frise (S7 -> S8)
a7, tv = S(7), tm(7, "Vous créez")
body += part("p2", "navy", a7, tv, 2, "Comment ça se passe", "Comment cela se passe, <span>concrètement&nbsp;?</span>")
js += part_js("p2", a7)
stp = [("Aujourd'hui", "Vous créez votre compte", "Sans carte bancaire", "✎", "", 160, "Vous créez"),
       ("14 jours", "Essai gratuit", "Avec vos vraies prestations", "✓", "", 560, "Vous testez"),
       ("Avant le 31/12", "99&nbsp;€, une seule fois", "Paiement unique", "🎁", " g", 960, "vous réglez"),
       ("Ensuite", "12 mois d'accès complet", "Toutes les fonctions", "📅", "", 1360, "douze mois")]
# positions en px depuis la gauche de la route (left 120 → 1800, largeur 1680)
st_html = "".join(f'<div class="st27{g} hid" id="t{k}" style="left:{120 + x * 1680 // 1520}px"><div class="dt">{ic}</div><div class="w">{w}</div><b>{b}</b><small>{s}</small></div>'
                  for k, (w, b, s, ic, g, x, _) in enumerate(stp))
body += clip("tt", "light", tv, S(8), f'''
  <div class="hd27"><div class="chap"><b>▶</b>Partie 2 · En 4 temps</div><div class="h" style="margin-top:20px">De l'essai <span>à l'année complète</span></div></div>
  <div class="road27"><b id="rdb"></b></div>{st_html}
  <div class="np27"><div class="a hid" id="tn">✓ Aucun prélèvement automatique</div><div class="b hid" id="tr">Rien ne repart sans votre accord</div></div>''')
js += f'tl.fromTo("#rdb",{{scaleX:0}},{{scaleX:1,duration:{r2(tm(7, "douze mois") - tv)},ease:"none"}},{r2(tv)});\n'
for k, (*_, key) in enumerate(stp):
    js += pop(f"#t{k}", tv if k == 0 else tm(7, key), "back.out(1.8)", 40)
js += f'tl.to("#t2 .dt",{{scale:1.15,duration:.35,yoyo:true,repeat:1}},{tm(7, "99 euros")});\n'
js += pop("#tn", tm(7, "Aucun prélèvement"), "back.out(2)") + pop("#tr", tm(7, "rien ne repart"), "back.out(2)")

# ---------- 8 : partie 3 + 3 panneaux (S8 -> S9)
a8, tr8 = S(8), tm(8, "Vous renouvelez")
body += part("p3", "blue", a8, tr8, 3, "Au bout d'un an", "Au bout d'un an, <span>vous choisissez</span>")
js += part_js("p3", a8)
body += clip("sg", "cream", tr8, S(9), '''
  <div class="hd27" style="top:120px"><div class="h hid" id="sgh">Au bout d'un an, <span>3 chemins</span></div></div>
  <div class="sg27"><div class="p hid" id="sg1"><div class="pole"></div><div class="bd"><i>↻</i><b>Renouveler</b><small>Pour une nouvelle année</small></div></div>
    <div class="p hid" id="sg2"><div class="pole"></div><div class="bd"><i>📅</i><b>Passer au mois</b><small>Sans engagement</small></div></div>
    <div class="p k hid" id="sg3"><div class="pole"></div><div class="bd"><i>⏸</i><b>Arrêter</b><small id="sg3s" class="hid">Vos données restent accessibles, en lecture</small></div></div></div>''')
js += pop("#sgh", tr8 + .02, E, 40) + pop("#sg1", tr8 + .1, "back.out(1.6)", 60) + pop("#sg2", tm(8, "Vous passez"), "back.out(1.6)", 60)
js += pop("#sg3", tm(8, "Ou vous arrêtez"), "back.out(1.6)", 60) + pop("#sg3s", tm(8, "vos données"))

# ---------- 9 : questions fréquentes (S9 -> S10)
a9 = S(9)
body += clip("fq", "light", a9, S(10), '''
  <div class="faq27"><div class="hd"><i>?</i>Les 2 questions qui reviennent</div>
    <div class="bx"><div class="bq27 hid" id="q1">Je suis déjà en essai. Je peux en profiter&nbsp;?</div>
      <div class="ba27 hid" id="a1"><b>Oui.</b> Vous pouvez choisir l'offre pendant votre essai, jusqu'au 31 décembre.</div>
      <div class="bq27 hid" id="q2">Et si je préfère payer au mois&nbsp;?</div>
      <div class="ba27 hid" id="a2"><b>C'est possible.</b> Le mois à 29&nbsp;€ reste disponible.</div></div></div>''')
js += pop(".faq27", a9 + .02, E, 40) + pop("#q1", tm(9, "Je suis"), "back.out(1.6)") + pop("#a1", tm(9, "Oui"), "back.out(1.6)")
js += pop("#q2", tm(9, "Et si je"), "back.out(1.6)") + pop("#a2", tm(9, "C'est possible"), "back.out(1.6)")

# ---------- 10 : récap puis offre puis fin
a10, to = S(10), tm(10, "Commencez")
rc = [("Toutes les fonctions,<br/><span>de la réservation à la guidance livrée</span>", "toutes les fonctions", ""),
      ("Un seul paiement&nbsp;:<br/><span>99&nbsp;€, sans prélèvement</span>", "Un seul paiement", " g"),
      ("Au bout d'un an,<br/><span>vous décidez</span>", "Et au bout", "")]
rcs = "".join(f'<div class="rcard{c} hid" id="rc{i}"><b>{i + 1}</b><div>{t}</div></div>' for i, (t, _, c) in enumerate(rc))
body += clip("r", "light", a10, to, f'''
  <div class="hdr" style="top:130px"><div class="chap hid" id="rk"><b>✓</b>En résumé</div></div>
  <div class="rc">{rcs}</div>''')
js += pop("#rk", a10 + .05, E) + "".join(pop(f"#rc{i}", tm(10, k) - .05, y=50) for i, (_, k, _) in enumerate(rc))
tz = r2(EN[10] + .3)
body += clip("o", "navy", to, tz, '''
  <img src="assets/logo_blanc.png" alt="GuidPilot" style="position:absolute;left:50%;top:40px;width:280px;margin-left:-140px" />
  <div class="top14 hid" id="o14" style="top:140px"><div>Pour commencer&nbsp;: 14 jours gratuits · sans carte bancaire</div></div>
  <div class="xm" style="top:250px"><div class="k">🎁 OFFRE DE NOËL · JUSQU'AU 31 DÉCEMBRE</div>
    <div class="p">1 an pour <span>99&nbsp;€</span></div>
    <div class="s">payé une seule fois</div>
    <div class="c">au lieu de 29&nbsp;€/mois, soit 348&nbsp;€ sur un an</div>
    <div class="np">✓ Aucun prélèvement automatique</div></div>
  <div class="dsc hid" id="od" style="top:900px">↓ <span><b>Le lien</b> est dans la description</span></div>''', logo="")
js += pop("#o14", to + .1, "back.out(2)") + pop("#od", tm(10, "Le lien"), "back.out(2)")
body += f'''
<div id="z" class="clip navy" data-start="{tz}" data-duration="{r2(DUR - tz)}" data-track-index="1">
  <div class="center hid" id="z6" style="top:220px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="endo">🎁 1 an pour 99&nbsp;€</div>
    <div class="endd">Jusqu'au 31 décembre · payé une fois</div>
    <div class="url" style="font-size:44px">guidpilot.fr/offre-fondatrice</div>
    <div class="sub hid" id="z9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''
js += f'tl.fromTo("#z6",{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.5)"}},{r2(tz + .05)});\n'
js += pop("#z9", tz + .5) + f'tl.to("#z9",{{scale:1.06,duration:.45,yoyo:true,repeat:2,ease:"sine.inOut"}},{r2(tz + 1.1)});\n'

html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRAS}{EXTRA13}{EXTRA27}</style></head><body>
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

d = ATELIER / "build" / "yt-offre-noel-guidance"
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for f in ("logo_blanc.png", "favicon.png", "finance.png", "avis.png"): shutil.copy(KIT / "assets" / f, d / "assets" / f)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(WAV, d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d, DUR, "CTA", ST[3], "segments", ST)
