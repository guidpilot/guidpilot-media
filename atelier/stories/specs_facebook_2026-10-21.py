"""Stories FACEBOOK (21 au 25/10/2026) — demande de Normane du 21/10/2026 : reprendre les stories Instagram sur Facebook.
Différences avec Instagram : pas de mot-clé ManyChat (il ne fonctionne que sur Instagram) → « guidpilot.fr » à la place ;
teasers « Nouvelle vidéo sur notre page » ; aucune story jeu-concours (concours Instagram uniquement).
Les stories « question » et « fonction » d'Instagram sont reprises telles quelles (dossier 2026-10-19_au_25/stories)."""
OFFRE = "14 jours gratuits, sans carte bancaire · guidpilot.fr"
VIDEO = "Nouvelle vidéo sur notre page 👆"

STORIES = [
 {"name": "fb_mer-21_1445_partenaires", "type": "teaser", "pill": "Programme partenaire", "title": "GuidPilot cherche des [partenaires]",
  "sub": "Formateurs, créateurs de contenu, praticiens et thérapeutes qui ont une communauté.",
  "cta": "Candidature sur guidpilot.fr · tous les détails dans notre dernière publication"},
 {"name": "fb_jeu-22_1230_cabinet-therapeute", "type": "teaser", "kick": "Sophrologue, hypnothérapeute, praticienne Reiki ?",
  "title": "Votre cabinet, [dans un seul espace].", "cta": OFFRE},
 {"name": "fb_jeu-22_2000_teaser-premier-appel", "type": "teaser", "pill": "Nouvelle vidéo", "title": "Elle appelle pour [« se renseigner »]. Que dire ?",
  "size": 96, "cta": VIDEO},
 {"name": "fb_ven-23_2000_teaser-rythme", "type": "teaser", "pill": "Nouvelle vidéo", "title": "Elle revient [chaque semaine]. Bonne nouvelle ?", "cta": VIDEO},
 {"name": "fb_dim-25_1230_guidance", "type": "teaser", "kick": "Praticienne en guidance ?",
  "title": "Réservations, guidances, factures : [tout au même endroit].", "size": 92, "cta": OFFRE},
]
