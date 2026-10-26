"""Stories FACEBOOK (26/10 au 01/11/2026) — reprise des stories Instagram de la semaine (specs_2026-10-26.py), adaptées à Facebook.
- Concours (lun-26 12h30) : non repris (Instagram uniquement).
- Question / conseil / fonction (mer-28, jeu-29, ven-30, dim-01 à 12h30) : images Instagram reprises telles quelles.
- Mot-clé THÉRAPEUTE (mar-27, sam-31 à 12h30) : variantes sans mot-clé → offre + guidpilot.fr.
- Teasers Reels lun-26, mar-27, mer-28 : la même vidéo est publiée sur la page Facebook le même jour → « Nouvelle vidéo sur notre page ».
- Teasers carrousels jeu-29, ven-30, sam-31 : carrousel non publié sur Facebook ce jour-là → remplacés par un conseil express."""
OFFRE = "14 jours gratuits, sans carte bancaire · guidpilot.fr"
VIDEO = "Nouvelle vidéo sur notre page 👆"

STORIES = [
 {"name": "fb_lun-26_2000_teaser-parcours-complet", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Réservation, paiement, guidance : [le parcours complet]", "size": 96, "sub": "En moins de 2 minutes.", "cta": VIDEO},
 {"name": "fb_mar-27_1230_cabinet-therapeute", "type": "teaser", "kick": "Sophrologue, praticienne Reiki ou LaHoChi ?",
  "title": "Vos séances, vos règlements, vos factures : [au même endroit].", "size": 90, "cta": OFFRE},
 {"name": "fb_mar-27_2000_teaser-cabinet-2-minutes", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Votre cabinet, [en 2 minutes]", "sub": "Réservation, rappel, encaissement, compte rendu.", "cta": VIDEO},
 {"name": "fb_mer-28_2000_teaser-pendant-que-vous-dormez", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Et si vos clientes réservaient [pendant que vous dormez] ?", "size": 96, "cta": VIDEO},
 {"name": "fb_jeu-29_2000_conseil-lien-reservation", "type": "tip", "pill": "Astuce organisation",
  "title": "Votre lien de réservation, [visible partout]", "size": 96,
  "sub": "Dans votre bio, votre signature d'e-mail et vos réponses : vos clientes réservent même pendant vos séances."},
 {"name": "fb_ven-30_2000_conseil-petite-question", "type": "tip", "pill": "Astuce guidance",
  "title": "« Juste une petite question… » : [répondez avec un cadre]", "size": 90,
  "sub": "Une réponse courte et bienveillante, puis le lien vers la séance adaptée."},
 {"name": "fb_sam-31_1230_cabinet-therapeute", "type": "teaser", "kick": "Hypnothérapeute, réflexologue, magnétiseuse ?",
  "title": "Vos clients réservent en ligne. [Vous, vous restez en séance.]", "size": 88, "cta": OFFRE},
 {"name": "fb_sam-31_2000_conseil-demi-journee", "type": "tip", "pill": "Astuce organisation",
  "title": "Gardez [une demi-journée] sans séance", "size": 96,
  "sub": "Pour l'administratif, la préparation et votre repos. Votre semaine respire."},
]
