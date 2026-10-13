"""Carrousels JEU-CONCOURS (images) — jeudi 15/10 et dimanche 18/10/2026 20h00, 6 slides 1080x1350.
Style repris des Reels concours m2/m5 (fond marine, étapes numérotées, écran final « Commentez GuidPilot »).
Usage : python3 carrousels/gen_concours_2026-10-15.py  → build/carrousels/q*.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_carrousels as g
from gen_carrousels import LOGO_W, LOGO_C

def esc(t):
    out = g.esc(t)
    for a, b in (("« ", "«&nbsp;"), (" »", "&nbsp;»"), (" :", "&nbsp;:"), (" ?", "&nbsp;?"), (" !", "&nbsp;!"), ("@guidpilot.fr", "<b class=h>@guidpilot.fr</b>"), ("2 abonnements", "2&nbsp;abonnements"), ("3 abonnements", "3&nbsp;abonnements"), ("lundi 26 octobre", "lundi 26&nbsp;octobre")):
        out = out.replace(a, b)
    return out

g.CSS += """
.kicker{font-size:36px}
.swipe{font-size:36px}
.lot{margin-top:40px;background:#fff;border:3px solid #E2E8F0;border-radius:32px;padding:44px 52px;display:flex;align-items:center;gap:44px}
.lot .v{font-weight:800;font-size:96px;line-height:1;color:#2563EB;letter-spacing:-.03em;flex:none;min-width:300px}
.lot .t{font-weight:700;font-size:42px;line-height:1.3;color:#0F172A}
.lot.first{border-color:#2563EB;border-width:4px}
.badge{display:inline-block;background:#FBF3DC;color:#6B4E16;border-radius:999px;padding:16px 34px;font-weight:700;font-size:36px}
.step{margin-top:34px;background:#1E293B;border:2px solid #334155;border-radius:30px;padding:40px 44px;display:flex;align-items:center;gap:36px}
.step i{font-style:normal;flex:none;width:88px;height:88px;border-radius:50%;background:#E9C46A;color:#0F172A;font-weight:800;font-size:48px;display:flex;align-items:center;justify-content:center}
.step div{font-weight:700;font-size:46px;line-height:1.25;color:#fff}
.step b,.h{font-weight:700;color:#93C5FD}
.navy h2{color:#fff}
.navy h2 span,.navy h1 span{color:#60A5FA}
.dm{margin-top:48px;background:#fff;border:3px solid #E2E8F0;border-left:12px solid #2563EB;border-radius:28px;padding:44px 50px;font-weight:600;font-size:44px;line-height:1.4;color:#0F172A}
.date{margin-top:44px;display:flex;align-items:center;gap:40px}
.cal{flex:none;width:230px;border-radius:30px;overflow:hidden;background:#fff;border:3px solid #E2E8F0;text-align:center}
.cal .m{background:#0F172A;color:#fff;font-weight:700;font-size:36px;padding:14px 0;letter-spacing:.08em}
.cal .d{font-weight:800;font-size:110px;color:#0F172A;line-height:1.2}
.cal .w{font-weight:600;font-size:36px;color:#64748B;padding-bottom:18px}
.date p{margin-top:0}
.chk{margin-top:44px}
.chk div{display:flex;align-items:center;gap:26px;background:#fff;border:3px solid #E2E8F0;border-radius:24px;padding:22px 34px;margin:18px 0;font-weight:700;font-size:44px;color:#0F172A}
.chk i{font-style:normal;flex:none;width:60px;height:60px;border-radius:50%;background:#DCFCE7;color:#16A34A;display:flex;align-items:center;justify-content:center;font-size:34px}
.fin{align-items:center;text-align:center}
.fin .biglogo{width:520px;margin:0 auto 70px}
.fin .c{font-weight:800;font-size:80px;color:#fff}
.word{margin:34px auto 30px;background:#fff;border-radius:36px;padding:36px 70px;display:inline-flex;align-items:center;gap:30px;font-weight:800;font-size:110px;color:#0F172A;letter-spacing:-.02em}
.word i{font-style:normal;width:96px;height:96px;border-radius:50%;background:#DBEAFE;display:flex;align-items:center;justify-content:center;font-size:52px}
.fin .pp{font-weight:800;font-size:72px;color:#fff}
.fin .pp span{color:#E9C46A}
.fin .badge{margin-top:56px}
.fin .site{margin-top:44px;font-weight:700;font-size:44px;color:#CBD5E1}
"""

def logo(c): return f'<div class="foot"><img src="data:image/png;base64,{LOGO_C if c else LOGO_W}"></div>'

def cover(k, t, sub):
    return f'<div class="s navy"><div class="kicker">{esc(k)}</div><h1>{esc(t)}</h1><p>{esc(sub)}</p>{logo(0)}<div class="swipe">Faites défiler →</div></div>'

def lots(k, t, sub=""):
    return (f'<div class="s light"><div class="kicker">{esc(k)}</div><h2>{esc(t)}</h2>'
            f'<div class="lot first"><div class="v">1 an</div><div class="t">d\'abonnement GuidPilot offert</div></div>'
            f'<div class="lot"><div class="v">2 × 3 mois</div><div class="t">d\'abonnement GuidPilot offerts</div></div>'
            f'{f"<p>{esc(sub)}</p>" if sub else ""}{logo(1)}</div>')

def steps(k, t):
    st = ["Abonnez-vous à @guidpilot.fr", "Aimez [cette publication]", "Commentez [« GuidPilot »]"]
    s = "".join(f'<div class="step"><i>{i}</i><div>{esc(x).replace("<span>","<b>").replace("</span>","</b>")}</div></div>' for i, x in enumerate(st, 1))
    return f'<div class="s navy"><div class="kicker">{esc(k)}</div><h2>{esc(t)}</h2>{s}{logo(0)}</div>'

def tirage(k, t, txt, dm):
    return (f'<div class="s light"><div class="kicker">{esc(k)}</div><h2>{esc(t)}</h2>'
            f'<div class="date"><div class="cal"><div class="m">OCTOBRE</div><div class="d">26</div><div class="w">lundi</div></div><p>{esc(txt)}</p></div>'
            f'<div class="dm">📩 {esc(dm)}</div>{logo(1)}</div>')

def produit(k, t, items):
    c = "".join(f'<div><i>✓</i>{esc(x)}</div>' for x in items)
    return f'<div class="s light"><div class="kicker">{esc(k)}</div><h2>{esc(t)}</h2><div class="chk">{c}</div>{logo(1)}</div>'

def fin():
    return (f'<div class="s navy fin"><img class="biglogo" src="data:image/png;base64,{LOGO_W}">'
            f'<div class="c">Commentez</div><div><div class="word"><i>💬</i>GuidPilot</div></div>'
            f'<div class="pp">pour <span>participer</span></div>'
            f'<div><div class="badge">Tirage au sort · lundi 26 octobre</div></div><div class="site">guidpilot.fr</div></div>')

g.C = {
 "q1-gagnez-1-an": [
  cover("Jeu-concours GuidPilot", "Gagnez [1 an] de GuidPilot", "Thérapeutes, praticiennes bien-être et en guidance : 3 abonnements sont à gagner."),
  lots("À gagner", "[3 lots] à gagner", "Le logiciel pour gérer votre activité, offert."),
  steps("Pour participer", "3 étapes, [c'est tout]"),
  tirage("Et ensuite ?", "Tirage au sort le [lundi 26 octobre]", "Fin du jeu et tirage au sort le lundi 26 octobre 2026.",
         "En commentant « GuidPilot », vous recevez automatiquement un message privé qui confirme votre participation."),
  produit("GuidPilot en une phrase", "Votre activité [dans un seul espace]", ["Rendez-vous", "Clientes", "Guidances", "Factures", "Avis"]),
  fin(),
 ],
 "q2-plus-que-8-jours": [
  cover("Jeu-concours GuidPilot", "Plus que [8 jours] pour participer", "1 an de GuidPilot à gagner, et 2 abonnements de 3 mois."),
  lots("Toujours à gagner", "Ce que vous [pouvez gagner]", "Pour les praticiennes en guidance et les thérapeutes."),
  steps("Il est encore temps", "Moins d'une minute [pour participer]"),
  tirage("Le grand jour", "Rendez-vous [lundi 26 octobre]", "Le jeu se termine et le tirage au sort a lieu ce jour-là.",
         "Déjà commenté ? Regardez vos messages privés : la confirmation de participation vous y attend."),
  produit("C'est quoi, GuidPilot ?", "[Un seul espace] pour gérer votre activité", ["Vos rendez-vous", "Vos clientes", "Vos guidances", "Vos factures", "Vos avis"]),
  fin(),
 ],
}

if __name__ == "__main__":
    g.main()
