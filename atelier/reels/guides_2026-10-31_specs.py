"""Reels V3 « guides offerts » (29/10/2026).
- ig31 : Reel Instagram + Short YouTube + Reel Facebook du samedi 31/10 18h30 (cadre légal, guide 2).
- tt02 : TikTok du lundi 02/11 10h00 (trop de choix, guide 2), vocabulaire neutre « praticien ».
Usage : python3 reels/guides_2026-10-31_specs.py <clé> <voix.wav>"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_tiktok_v3 as v3

SPECS = {
"ig31": {"slug": "ig31-trois-phrases-a-ne-jamais-ecrire", "music": "elan",
 "mid_cta": "3 guides offerts · guidpilot.fr",
 "scenes": [
  {"k": "hook", "bg": "marine", "title": "3 phrases à ne jamais écrire [dans vos publications.]", "size": 118, "top": 450,
   "say": "Trois phrases que vous ne devriez jamais écrire dans vos publications."},
  {"k": "num", "bg": "creme", "n": "1", "title": "« Résultats [garantis] »", "size": 110,
   "sub": "Promettre un résultat peut être une pratique commerciale trompeuse.", "subt": 1.2,
   "say": "Un : « résultats garantis ». Promettre un résultat peut être considéré comme une pratique commerciale trompeuse."},
  {"k": "num", "bg": "or", "n": "2", "title": "« Mes soins [guérissent] »", "size": 110,
   "sub": "Guérir, traiter une maladie : ces mots relèvent du médical.", "subt": 1.2,
   "say": "Deux : « mes soins guérissent ». Guérir, traiter une maladie : ces mots relèvent du médical."},
  {"k": "num", "bg": "bleu", "n": "3", "title": "« Arrêtez votre [traitement] »", "size": 104,
   "sub": "Y pousser peut être un délit, depuis 2024.", "subt": 1.3,
   "say": "Et trois : « arrêtez votre traitement ». Pousser quelqu'un à abandonner un traitement médical peut constituer un délit, depuis 2024."},
  {"k": "words", "bg": "creme", "title": "Décrivez plutôt [votre approche.]", "size": 128, "top": 520,
   "sub": "Le déroulé, la durée, et ce que la personne peut en attendre, honnêtement.", "subt": 1.4, "subtop": 1060,
   "say": "À la place, décrivez votre approche, le déroulé de la séance, et ce que la personne peut en attendre, honnêtement."},
  {"k": "end", "bg": "marine", "title": "Votre dernière publication <span style=\"color:#E9C46A\">passe le test&nbsp;?</span>",
   "save": "📘 3 guides offerts sur guidpilot.fr",
   "say": "Votre dernière publication passe le test ? Nos trois guides offerts vous en disent plus, sur guidpilot.fr."},
 ]},
"tt02": {"slug": "tt02-trop-de-prestations", "music": "aube",
 "caption": "Praticien : trop de prestations sur votre page fait hésiter vos clientes. #pourtoi #praticien",
 "scenes": [
  {"k": "hook", "bg": "bleu", "title": "12 prestations sur votre page… [et moins de réservations.]", "size": 112, "top": 450,
   "say": "Douze prestations sur votre page… et moins de réservations."},
  {"k": "words", "bg": "marine", "title": "Trop de choix [fait hésiter.]", "size": 150, "top": 560,
   "say": "Trop de choix fait hésiter."},
  {"k": "tiles", "bg": "creme", "title": "Une étude [célèbre]",
   "items": [("24", "confitures\u00a0:\u00a03\u00a0% achètent"), ("6", "confitures\u00a0:\u00a030\u00a0% achètent")],
   "say": "Une étude célèbre l'a montré : sur un stand, avec six confitures au lieu de vingt-quatre, les visiteurs achetaient bien plus."},
  {"k": "num", "bg": "or", "n": "1", "title": "Gardez [3 à 4] offres", "say": "Gardez trois ou quatre offres."},
  {"k": "num", "bg": "creme", "n": "2", "title": "Nom, durée, [format]", "say": "Un nom clair, une durée, un format."},
  {"k": "num", "bg": "bleu", "n": "3", "title": "Une ligne [« pour qui ? »]", "size": 112, "say": "Et une ligne : pour qui."},
  {"k": "end", "bg": "marine", "title": "Combien de prestations affichez-vous <span style=\"color:#E9C46A\">aujourd'hui&nbsp;?</span>",
   "save": "Enregistrez cette vidéo 🔖", "say": "Combien de prestations affichez-vous aujourd'hui ?"},
 ]},
}

if __name__ == "__main__":
    if sys.argv[1] == "check":
        for k, s in SPECS.items():
            blob = str(s).lower()
            print(k, [w for w in v3.INTERDITS if w in blob] if k.startswith("tt") else "-", "|", " ".join(sc["say"] for sc in s["scenes"]))
    else:
        v3.build(SPECS[sys.argv[1]], sys.argv[2])
