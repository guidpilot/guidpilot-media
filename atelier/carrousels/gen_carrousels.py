"""Génère les carrousels Instagram GuidPilot (1080x1350) en PNG via Chromium headless."""
import base64, html, pathlib, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
ATELIER = ROOT.parent
FONTS = ATELIER / "kit" / "fonts"
LOGO_W = base64.b64encode(open(ATELIER / "assets" / "logo_blanc.png", "rb").read()).decode()
LOGO_C = base64.b64encode(open(ATELIER / "assets" / "logo_couleur.png", "rb").read()).decode()

def font_face():
    out = ""
    for w in (400, 600, 700, 800):
        b = base64.b64encode(open(FONTS / f"inter-latin-{w}-normal.woff2", "rb").read()).decode()
        out += f'@font-face{{font-family:Inter;src:url(data:font/woff2;base64,{b}) format("woff2");font-weight:{w}}}'
    return out

CSS = font_face() + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:Inter,sans-serif;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;padding:150px 96px 200px;display:flex;flex-direction:column;justify-content:center}
.navy{background:#0F172A;color:#fff}
.light{background:#F6F8FC;color:#0F172A}
.kicker{font-weight:700;font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:#E9C46A}
.light .kicker{color:#2563EB}
h1{font-weight:800;font-size:92px;line-height:1.05;letter-spacing:-.02em;margin-top:34px}
h1 span{color:#60A5FA}
h2{font-weight:800;font-size:80px;line-height:1.1;letter-spacing:-.02em;margin-top:30px}
h2 span{color:#2563EB}
.num{font-weight:800;font-size:170px;line-height:1;color:#2563EB;letter-spacing:-.04em}
p{font-weight:500;font-size:48px;line-height:1.4;color:#475569;margin-top:40px}
.navy p{color:#CBD5E1}
.quote{margin-top:46px;background:#fff;border:3px solid #E2E8F0;border-left:12px solid #2563EB;border-radius:28px;padding:48px 52px;font-weight:600;font-size:46px;line-height:1.45;color:#0F172A}
.tip{margin-top:44px;background:#FBF3DC;color:#6B4E16;border-radius:24px;padding:30px 40px;font-weight:600;font-size:34px;line-height:1.4}
.swipe{position:absolute;right:96px;bottom:96px;font-weight:700;font-size:34px;color:#E9C46A}
.light .swipe{color:#2563EB}
.foot{position:absolute;left:96px;bottom:96px;height:56px}
.foot img{height:56px}
.page{position:absolute;right:96px;top:110px;font-weight:700;font-size:28px;color:#94A3B8}
.list{margin-top:44px}
.li{display:flex;align-items:center;gap:26px;font-weight:700;font-size:44px;margin:22px 0}
.li i{font-style:normal;width:66px;height:66px;border-radius:50%;background:#1E3A8A;color:#93C5FD;display:flex;align-items:center;justify-content:center;font-size:36px;flex:none}
.cta{margin-top:60px;display:inline-block;background:#2563EB;color:#fff;font-weight:800;font-size:46px;padding:32px 56px;border-radius:999px}
.nocard{margin-top:28px;font-weight:700;font-size:38px;color:#4ADE80}
.biglogo{width:560px;display:block;margin-bottom:60px}
"""

def esc(t):
    return html.escape(t).replace("[", "<span>").replace("]", "</span>")

def cover(kicker, title, sub):
    return f'<div class="s navy"><div class="kicker">{esc(kicker)}</div><h1>{esc(title)}</h1><p>{esc(sub)}</p><div class="foot"><img src="data:image/png;base64,{LOGO_W}"></div><div class="swipe">Faites défiler →</div></div>'

def point(n, total, num, title, text, extra=""):
    return f'<div class="s light"><div class="page">{n}/{total}</div><div class="num">{esc(num)}</div><h2>{esc(title)}</h2><p>{esc(text)}</p>{extra}<div class="foot"><img src="data:image/png;base64,{LOGO_C}"></div></div>'

def quote(n, total, label, title, msg, extra=""):
    return f'<div class="s light"><div class="page">{n}/{total}</div><div class="kicker">{esc(label)}</div><h2>{esc(title)}</h2><div class="quote">« {esc(msg)} »</div>{extra}<div class="foot"><img src="data:image/png;base64,{LOGO_C}"></div></div>'

def cta(title, items):
    lis = "".join(f'<div class="li"><i>✓</i>{esc(x)}</div>' for x in items)
    return f'<div class="s navy"><img class="biglogo" src="data:image/png;base64,{LOGO_W}"><h2 style="color:#fff">{esc(title)}</h2><div class="list">{lis}</div><div class="cta">14 jours gratuits · Lien en bio</div><div class="nocard">✓ Sans carte bancaire</div></div>'

C = {
 "c1-organisation": [
  cover("Praticiennes en guidance", "5 signes que votre organisation vous fait [perdre des clientes]", "Tarologue, médium, énergéticienne : faites le test."),
  point(2,7,"1","Vos rendez-vous se prennent [par messages]","Chaque échange vous prend du temps. Et une cliente qui attend une réponse finit souvent par réserver ailleurs."),
  point(3,7,"2","Tout est noté [dans un carnet]","Impossible de retrouver l'historique d'une cliente juste avant sa séance."),
  point(4,7,"3","Vous demandez le paiement [par message]","C'est gênant pour vous, et peu rassurant pour elle."),
  point(5,7,"4","Personne n'est relancé [après la séance]","Pas de suivi, pas d'avis : la cliente ne revient pas et ne vous recommande pas."),
  point(6,7,"5","Vos guidances partent [par WhatsApp]","Elles se perdent dans les conversations et ne font pas professionnel."),
  cta("Et si tout était au même endroit ?", ["Réservation et paiement en ligne","Agenda et fiches clientes","Guidances écrites ou vocales","Factures et demandes d'avis"]),
 ],
 "c2-avis": [
  cover("Avis clients", "Demander un avis [sans paraître insistante]", "3 messages prêts à copier pour votre prochaine séance."),
  point(2,7,"Pourquoi ?","Les avis [rassurent]","Une future cliente qui hésite lit les avis avant de réserver. C'est souvent ce qui la décide."),
  point(3,7,"Quand ?","24 à 48 h [après la séance]","Quand l'échange est encore frais, sans attendre plusieurs semaines.", '<div class="tip">Ne proposez jamais de réduction ou de cadeau en échange d\'un avis.</div>'),
  quote(4,7,"Message 1","Juste après la séance","Merci pour votre confiance. Si la séance vous a été utile, votre avis aidera d'autres personnes à me trouver. Cela prend une minute."),
  quote(5,7,"Message 2","Relance douce, 5 jours après","Je me permets un petit rappel, sans aucune obligation : votre retour compte beaucoup pour moi."),
  quote(6,7,"Message 3","Pour une cliente fidèle","Cela fait plusieurs séances que nous avançons ensemble. Accepteriez-vous de partager votre expérience en quelques mots ?"),
  cta("Avec GuidPilot, c'est en un clic", ["Demande d'avis après chaque séance","Relance quand vous le souhaitez","Avis affichés sur votre page"]),
 ],
 "c3-paiement": [
  cover("Paiement à l'avance", "Le demander [sans passer pour une arnaque]", "4 réflexes qui rassurent vos clientes avant la séance."),
  point(2,7,"Le constat","Le secteur [inspire de la méfiance]","Beaucoup de clientes hésitent à payer d'avance, à cause des arnaques qu'elles ont vues passer."),
  point(3,7,"1","Affichez [vos tarifs]","Prix, durée, format (visio, cabinet, écrit) : tout doit être visible avant de réserver."),
  point(4,7,"2","Annoncez [votre cadre]","Délai pour annuler, report possible : un cadre clair rassure et vous protège."),
  point(5,7,"3","Un paiement [sécurisé]","Un vrai paiement en ligne inspire plus confiance qu'un virement demandé par message."),
  point(6,7,"4","Envoyez [une facture]","Une facture claire, avec vos coordonnées, montre que vous êtes une professionnelle."),
  cta("GuidPilot le fait pour vous", ["Page de réservation avec vos tarifs","Paiement en ligne sécurisé","Facture créée automatiquement"]),
 ],
}

def main():
    out = ATELIER / "build" / "carrousels"; out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for name, slides in C.items():
            for i, s in enumerate(slides, 1):
                pg.set_content(f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{s}</body></html>")
                pg.wait_for_timeout(150)
                pg.screenshot(path=str(out / f"{name}-{i:02d}.png"))
        b.close()
    print("ok")

if __name__ == "__main__":
    main()
