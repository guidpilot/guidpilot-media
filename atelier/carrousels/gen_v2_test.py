"""Carrousel TEST ligne éditoriale V2 (15/10/2026) — 8 slides 1080x1350, public guidance.
Structure V2 : accroche · second hook · 1 idée par slide · récap à enregistrer · question finale.
Usage : python3 carrousels/gen_v2_test.py  → build/carrousels/v2-test-*.png"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_carrousels as g
from gen_carrousels import point, quote, LOGO_C, LOGO_W

_esc = g.esc
def esc(t):
    out = _esc(t)
    for a, b in (("« ", "«&nbsp;"), (" »", "&nbsp;»"), (" :", "&nbsp;:"), (" ?", "&nbsp;?"), (" !", "&nbsp;!")):
        out = out.replace(a, b)
    return out
g.esc = esc

g.CSS += """
.hook h1{font-size:104px;margin-top:0}
.hook .badge{display:inline-block;margin-top:56px;background:#E9C46A;color:#0F172A;font-weight:800;font-size:36px;padding:18px 34px;border-radius:999px;align-self:flex-start}
.save{margin-top:56px;background:#fff;border:3px dashed #2563EB;border-radius:28px;padding:34px 40px;font-weight:700;font-size:42px;line-height:1.35;color:#0F172A}
.discreet{position:absolute;left:96px;right:96px;bottom:96px;font-weight:600;font-size:30px;color:#94A3B8;text-align:center}
.recap .li{color:#fff}
.recap .li i{background:#E9C46A;color:#0F172A}
"""

def cover_v2(title, badge):
    # Slide 1 : pas de logo, pas de kicker — seulement l'accroche, en très gros.
    return f'<div class="s navy hook"><h1>{esc(title)}</h1><div class="badge">{esc(badge)}</div><div class="swipe">Faites défiler →</div></div>'

def second_hook(n, total, msg, tip):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><div class="kicker">Vous connaissez ce message&nbsp;?</div>'
            f'<div class="quote" style="font-size:54px">« {esc(msg)} »</div><div class="tip">{esc(tip)}</div></div>')

def recap(n, total, title, items):
    lis = "".join(f'<div class="li"><i>✓</i>{esc(x)}</div>' for x in items)
    return (f'<div class="s navy recap"><div class="page">{n}/{total}</div><div class="kicker">À enregistrer</div>'
            f'<h2 style="color:#fff">{esc(title)}</h2><div class="list">{lis}</div></div>')

def last(n, total, question):
    return (f'<div class="s light"><div class="page">{n}/{total}</div><h2>{esc(question)}</h2>'
            f'<div class="save">🔖 Enregistrez ce post pour avoir les 3 messages sous la main.</div>'
            f'<div class="discreet">Envie d\'un outil pour gérer vos réservations ? Commentez GUIDANCE.</div></div>')

T = 8
g.C = {
 "v2-test-question-gratuite": [
  cover_v2("« Juste une petite question… » : comment répondre [sans offrir votre guidance]", "3 messages prêts à copier"),
  second_hook(2, T, "Désolée de vous déranger, j'ai juste une petite question rapide sur ma situation…",
              "Le message n°3 est celui que vos clientes respectent le plus."),
  point(3, T, "Pourquoi", "Répondre vite [n'aide personne]",
        "Quelques lignes par message n'ont ni le cadre ni le temps d'une vraie guidance. Et votre cliente apprend que votre travail est gratuit."),
  quote(4, T, "Message 1", "Pour une nouvelle cliente",
        "Merci pour votre message ! Votre question mérite une vraie séance pour y répondre sereinement. Voici le lien pour réserver."),
  quote(5, T, "Message 2", "Pour une cliente fidèle",
        "Je comprends que ce soit important pour vous. Je préfère prendre le temps de bien vous répondre : je vous propose une courte séance cette semaine."),
  quote(6, T, "Message 3", "Quand elle insiste",
        "Je tiens à vous accompagner correctement, et cela ne peut pas se faire en quelques messages. Mon lien de réservation reste à votre disposition."),
  recap(7, T, "Les 4 règles", ["Remerciez toujours", "Valorisez sa question", "Proposez un cadre : une séance", "Restez douce, sans céder"]),
  last(8, T, "Et vous, combien de « petites questions » [recevez-vous par semaine] ?"),
 ],
}

if __name__ == "__main__":
    g.main()
