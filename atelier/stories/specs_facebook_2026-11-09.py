"""Stories FACEBOOK (09 au 15/11/2026) — reprise des stories Instagram de la semaine (specs_2026-11-09.py), adaptées à Facebook.
- Question / conseil / fonction (lun-09, mer-11, jeu-12, ven-13, dim-15 à 12h30) : images Instagram reprises telles quelles.
- Mot-clé THÉRAPEUTE (mar-10, sam-14 à 12h30) : variantes sans mot-clé → offre + guidpilot.fr.
- Teasers lun-09, mar-10, ven-13 (Reels aussi publiés sur la page le même jour) : « Nouvelle vidéo sur notre page ».
- Teasers jeu-12, sam-14 (posts aussi publiés sur la page le même jour) : « Nouvelle publication sur notre page ».
- Teaser mer-11 (Reel astrologue non publié sur Facebook) : remplacé par un conseil express."""
OFFRE = "14 jours gratuits, sans carte bancaire · guidpilot.fr"
VIDEO = "Nouvelle vidéo sur notre page 👆"
PUBLI = "Nouvelle publication sur notre page 👆"

STORIES = [
 {"name": "fb_lun-09_2000_teaser-c-est-combien", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "« C'est combien ? » [Vous répondez quoi ?]", "size": 104, "sub": "3 réponses à ne plus envoyer.", "cta": VIDEO},
 {"name": "fb_mar-10_1230_cabinet-therapeute", "type": "teaser", "kick": "Réflexologue, praticienne Reiki, hypnothérapeute ?",
  "title": "Vos clientes réservent et règlent en ligne, [même pendant vos séances].", "size": 84, "cta": OFFRE},
 {"name": "fb_mar-10_2000_teaser-partenaires", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Vous conseillez des outils [aux praticiens] ?", "size": 100, "sub": "Parlons partenariat.", "cta": VIDEO},
 {"name": "fb_mer-11_2000_conseil-guidance-ecrite", "type": "tip", "pill": "Astuce guidance",
  "title": "Votre guidance écrite, [dans un espace dédié]", "size": 96,
  "sub": "Votre cliente la retrouve et la relit quand elle veut, sans fouiller ses mails."},
 {"name": "fb_jeu-12_2000_teaser-annulation", "type": "teaser", "pill": "Nouvelle publication",
  "title": "Elle annule [une heure avant.]", "size": 104, "sub": "4 réponses prêtes à copier.", "cta": PUBLI},
 {"name": "fb_ven-13_2000_teaser-avant-de-reserver", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Ce que vos clientes regardent [avant de réserver]", "size": 96, "sub": "Et que vous ne voyez pas.", "cta": VIDEO},
 {"name": "fb_sam-14_1230_cabinet-therapeute", "type": "teaser", "kick": "Sophrologue, réflexologue, magnétiseuse ?",
  "title": "Paiement au cabinet ou en ligne : [la facture se crée toute seule].", "size": 84, "cta": OFFRE},
 {"name": "fb_sam-14_2000_teaser-reflexologue", "type": "teaser", "pill": "Nouvelle publication",
  "title": "Réflexologue : [une journée,] deux façons de la vivre", "size": 96, "sub": "Avant / après, heure par heure.", "cta": PUBLI},
]
