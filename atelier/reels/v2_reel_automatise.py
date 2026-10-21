"""Reel PROMO « Pourquoi un système automatisé » (21/10/2026), skill guidpilot-communication v3 :
accroche qui ouvre une boucle, journée en 3 heures, déculpabilisation, vraies captures, urgence honnête, mot-clé.
Usage : python3 reels/v2_reel_automatise.py <voix.wav>
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_v2

SPEC = {"slug": "2026-10-21_reel-automatise", "music": "elan", "scenes": [
  {"k": "hook2", "title": "Votre agenda peut se remplir <span>la nuit</span>.", "size": 116,
   "sub": "Restez 20 secondes, je vous montre comment.", "subt": 2.3,
   "say": "Et si vos clients réservaient pendant que vous dormez ? Restez vingt secondes, je vous montre comment."},
  {"k": "x", "tag": "9 H · EN PLEINE SÉANCE", "title": "Les demandes <span>s'empilent</span>", "top": 300, "extop": 640,
   "ex": ("chat", [("in", "Vous avez une dispo jeudi ?"), ("in", "Je réserve comment ?"), ("in", "Et pour payer ?")], 0.45), "ext": 0.5,
   "say": "Neuf heures, en pleine séance : les demandes s'empilent."},
  {"k": "x", "tag": "13 H · LA PAUSE", "title": "Qui a <span>payé</span> ?", "top": 300, "extop": 640,
   "ex": ("list", ["Virement de Julie", "!PayPal de Sarah : en attente", "!Virement de Léa : introuvable"], 0.4), "ext": 0.5,
   "say": "Treize heures : vous vérifiez qui a payé."},
  {"k": "x", "tag": "22 H · LE SOIR", "title": "Et il reste <span>les factures</span>", "top": 430, "extop": 900, "size": 84,
   "ex": ("card", "CHAQUE SOIR", "Factures, relances, messages en retard…"), "ext": 0.5,
   "say": "Et le soir, les factures."},
  {"k": "quote", "title": "Le problème, ce n'est pas vous. <span>Tout repose sur vous.</span>",
   "say": "Le problème, ce n'est pas vous : c'est que tout repose sur vous."},
  {"k": "shot", "tag": "AVEC GUIDPILOT", "title": "Ils réservent et paient <span>en ligne</span>", "img": "page_np.png", "W": 1100, "box": (80, 90, 960, 470),
   "say": "Avec Guide Pilote, vos clients réservent et paient en ligne, sur votre page."},
  {"k": "shot", "tag": "AVEC GUIDPILOT", "title": "La facture se crée <span>toute seule</span>", "img": "finance.png", "W": 1270, "box": (600, 30, 1240, 200),
   "say": "Ils reçoivent leur rappel, et la facture se crée toute seule."},
  {"k": "x", "tag": "À RETENIR", "title": "Une demande qui attend…", "top": 430, "extop": 820, "size": 84,
   "ex": ("card", "C'EST", "Un client qui peut réserver ailleurs."), "ext": 0.6,
   "say": "Car chaque demande qui attend, c'est un client qui peut réserver ailleurs."},
  {"k": "save", "kw": "GUIDANCE", "q": "14 jours gratuits, sans carte bancaire",
   "say": "Retrouvez vos soirées. Commentez Guidance pour recevoir le lien."},
]}

# Version Facebook : pas de mot-clé ManyChat, fin logo + essai + site.
import copy, shutil
SPEC_FB = copy.deepcopy(SPEC)
SPEC_FB["slug"] = "2026-10-21_reel-automatise-facebook"
SPEC_FB["scenes"][-1] = {"k": "brand", "title": "14 jours gratuits, <span>sans carte bancaire</span><br>guidpilot.fr",
   "say": "Retrouvez vos soirées. Essayez Guide Pilote gratuitement pendant quatorze jours, sur guide pilote point F R."}

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "facebook":
        gen_v2.build(SPEC_FB, sys.argv[1])
        shutil.copy(gen_v2.gc.SRC / "assets" / "logo_blanc.png", gen_v2.gc.BASE / "build" / SPEC_FB["slug"] / "assets" / "logo_blanc.png")
    else:
        gen_v2.build(SPEC, sys.argv[1])
