"""Stories FACEBOOK (02 au 08/11/2026) — reprise des stories Instagram de la semaine (specs_2026-11-02.py), adaptées à Facebook.
- Question / conseil / fonction (lun-02, mer-04, jeu-05, ven-06, dim-08 à 12h30) : images Instagram reprises telles quelles.
- Mot-clé THÉRAPEUTE (mar-03, sam-07 à 12h30) : variantes sans mot-clé → offre + guidpilot.fr.
- Teaser mar-03 20h00 (Reel partenaires) : la vidéo est publiée sur la page Facebook le même jour → « Nouvelle vidéo sur notre page ».
- Teasers lun-02, mer-04, jeu-05, ven-06, sam-07 : contenu non publié sur Facebook ce jour-là → remplacés par un conseil express."""
OFFRE = "14 jours gratuits, sans carte bancaire · guidpilot.fr"
VIDEO = "Nouvelle vidéo sur notre page 👆"

STORIES = [
 {"name": "fb_lun-02_2000_conseil-avis-lendemain", "type": "tip", "pill": "Astuce guidance",
  "title": "Demandez un avis [le lendemain] de la séance", "size": 96,
  "sub": "Un message court, avec son prénom : votre cliente a encore la séance en tête."},
 {"name": "fb_mar-03_1230_cabinet-therapeute", "type": "teaser", "kick": "Coach de vie, réflexologue, magnétiseuse ?",
  "title": "Moins de messages pour caler vos séances, [plus de temps pour vos clients].", "size": 86, "cta": OFFRE},
 {"name": "fb_mar-03_2000_teaser-partenaires", "type": "teaser", "pill": "Nouvelle vidéo",
  "title": "Vous recommandez des outils [à votre communauté] ?", "size": 96, "sub": "Devenez partenaire GuidPilot.", "cta": VIDEO},
 {"name": "fb_mer-04_2000_conseil-lien-visio", "type": "tip", "pill": "Astuce organisation",
  "title": "Le lien de visio, [dans le rappel]", "size": 100,
  "sub": "Votre cliente n'a pas à le chercher au dernier moment, et la séance commence à l'heure."},
 {"name": "fb_jeu-05_2000_conseil-conditions-annulation", "type": "tip", "pill": "Astuce cabinet",
  "title": "Affichez vos [conditions d'annulation] avant la réservation", "size": 90,
  "sub": "Votre cliente sait à quoi s'attendre, et vous évitez les malentendus."},
 {"name": "fb_ven-06_2000_conseil-anciennes-clientes", "type": "tip", "pill": "Astuce organisation",
  "title": "Semaine calme ? [Écrivez à vos anciennes clientes]", "size": 90,
  "sub": "Un message simple pour prendre de leurs nouvelles, avec votre lien de réservation."},
 {"name": "fb_sam-07_1230_cabinet-therapeute", "type": "teaser", "kick": "Sophrologue, hypnothérapeute ?",
  "title": "Séance à distance : le lien de visio part [sans que vous l'envoyiez].", "size": 86, "cta": OFFRE},
 {"name": "fb_sam-07_2000_conseil-notes-seance", "type": "tip", "pill": "Astuce cabinet",
  "title": "Vos notes de séance, [au même endroit]", "size": 96,
  "sub": "Fiche cliente, historique, comptes rendus : tout est prêt avant la séance suivante."},
]
