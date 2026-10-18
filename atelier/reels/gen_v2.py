"""Reels LIGNE ÉDITORIALE V2 (15/10/2026) : 15–30 s, accroche visible dès la 1re image, pas d'intro logo, fin courte.
Réutilise les scènes de gen_conseils.py (step / bad / list / vs / quote) et ajoute :
  - "hook2" : phrase-choc en très gros, déjà lisible à la frame 0 (pas de fondu depuis le noir) ;
  - "save"  : scène de fin courte « Enregistrez-la » (CONSEIL) ou « Commentez MOT-CLÉ » (PROMO, champ "kw"), + guidpilot.fr discret.
Pas de grand écran final logo + offre. Badge IA plus petit.
Usage : python3 reels/gen_v2.py <clé> <voix.wav>   (textes dans reels/v2_specs.py) → build/<slug>/
"""
import pathlib, shutil, sys, subprocess, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_conseils as gc
import gen_promos as gp  # active les scènes produit (shot / phone / myth / button / audio) — ajouté le 18/10/2026

EXTRA_V2 = """
.aibadge{font-size:22px !important;padding:8px 18px !important;top:56px !important;opacity:.85}
.hook2{font-weight:800;font-size:124px;line-height:1.04;color:#fff;letter-spacing:-.03em;width:960px}
.hook2 span{color:#E9C46A}
.hsub{margin-top:48px;font-weight:700;font-size:52px;color:#93C5FD;width:900px;line-height:1.25}
.savebox{width:900px;border:4px dashed #E9C46A;border-radius:40px;padding:60px 50px}
.savebox .ic{font-size:130px;line-height:1}
.savebox .t{margin-top:30px;font-weight:800;font-size:84px;line-height:1.08;color:#fff}
.savebox .q{margin-top:34px;font-weight:600;font-size:46px;line-height:1.3;color:#CBD5E1}
.vs p{font-size:54px !important}.vs h4{font-size:46px !important}
.site{position:absolute;left:0;right:0;bottom:170px;text-align:center;font-weight:700;font-size:40px;color:#64748B}
"""

_scene = gc.scene

def scene(i, sc, t0, t1):
    k = sc["k"]; sid = f"s{i}"; d = round(t1 - t0, 2)
    if k == "hook2":
        body = f'''<div class="center" style="top:{sc.get("top",560)}px"><div class="hook2" id="{sid}t"{f' style="font-size:{sc["size"]}px"' if sc.get("size") else ""}>{sc["title"]}</div>
{f'<div class="hsub" id="{sid}s">{sc["sub"]}</div>' if sc.get("sub") else ""}</div>'''
        js = [f'tl.fromTo("#{sid}t",{{scale:1.06}},{{scale:1,duration:.8,ease:E}},0);']
        if sc.get("sub"):
            js.append(f'tl.fromTo("#{sid}s",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.4,ease:E}},{round(t0 + sc.get("subt", 1.0),2)});')
        html = f'<div id="{sid}" class="clip navy" data-start="{round(t0,2)}" data-duration="{d}" data-track-index="1">{body}</div>'
        return html.replace(" ?", "&nbsp;?").replace(" !", "&nbsp;!").replace(" :", "&nbsp;:").replace("« ", "«&nbsp;").replace(" »", "&nbsp;»"), "\n".join(js)
    if k == "save":
        if sc.get("kw"):
            ic, t = "💬", f'Commentez <span style="color:#E9C46A">{sc["kw"]}</span>'
        else:
            ic, t = "🔖", "Enregistrez-la pour plus tard"
        body = f'''<div class="center" style="top:520px"><div class="savebox" id="{sid}b"><div class="ic">{ic}</div><div class="t">{t}</div>
{f'<div class="q">{sc["q"]}</div>' if sc.get("q") else ""}</div></div><div class="site">guidpilot.fr</div>'''
        js = [f'tl.fromTo("#{sid}b",{{opacity:0,scale:.85}},{{opacity:1,scale:1,duration:.5,ease:"back.out(1.7)"}},{round(t0+.05,2)});']
        html = f'<div id="{sid}" class="clip navy" data-start="{round(t0,2)}" data-duration="{d}" data-track-index="1">{body}</div>'
        return html.replace(" ?", "&nbsp;?"), "\n".join(js)
    return _scene(i, sc, t0, t1)


def build(spec, voix):
    gp.IMGS.clear()
    gc.align(spec, voix)
    # V2 : pas d'écran final long — la dernière scène (save) va jusqu'à la fin de la voix + 1,2 s
    spec["dur"] = round(spec["cta"] - 0.35 + 1.2, 2)
    scs = spec["scenes"]; dur = spec["dur"]
    bodies, jss = [], []
    for i, sc in enumerate(scs):
        t1 = scs[i + 1]["t"] if i + 1 < len(scs) else dur
        h, j = scene(i, sc, sc["t"], t1)
        bodies.append(h); jss.append(j)
    d = gc.BASE / "build" / spec["slug"]
    if d.exists(): shutil.rmtree(d)
    (d / "assets").mkdir(parents=True)
    for sub in ("fonts", "vendor"): shutil.copytree(gc.SRC / sub, d / sub)
    for f in ("hyperframes.json", "meta.json"): shutil.copy(gc.SRC / f, d / f)
    shutil.copy(voix, d / "assets" / "voix.wav")
    shutil.copy(gc.BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
    for im in gp.IMGS:
        shutil.copy(gc.SRC / "assets" / im, d / "assets" / im)
    html = gc.page(dur, "\n".join(bodies), "\n".join(jss), "voix.wav").replace("</style>", gc.EXTRA + gp.PCSS + EXTRA_V2 + "</style>", 1)
    (d / "index.html").write_text(html)
    print("ok", d, "durée", dur)


SPECS = {
"test-3-phrases": {"slug": "v2-test-3-phrases", "scenes": [
  {"k": "hook2", "title": "3 phrases qui font <span>fuir</span> vos clientes", "sub": "Sans que vous le sachiez.", "subt": 1.7,
   "say": "Trois phrases qui font fuir vos clientes. Sans que vous le sachiez."},
  {"k": "step", "n": 1, "top": 430, "extop": 920, "size": 88, "title": "Quand on vous demande <span>le prix</span>",
   "ex": ("vs", "« Ça dépend… »", "La durée et le tarif, clairement", 0.9), "ext": 1.0,
   "say": "Un : « ça dépend », quand on vous demande le prix. Donnez la durée et le tarif, clairement."},
  {"k": "step", "n": 2, "top": 430, "extop": 920, "size": 88, "title": "Pour <span>prendre rendez-vous</span>",
   "ex": ("vs", "« Écrivez-moi quand vous voulez »", "Un lien pour réserver", 1.0), "ext": 0.9,
   "say": "Deux : « écrivez-moi quand vous voulez ». Proposez plutôt un lien pour réserver."},
  {"k": "step", "n": 3, "top": 430, "extop": 920, "size": 88, "title": "Pour <span>rassurer</span>",
   "ex": ("vs", "Promettre des réponses", "Décrire comment se passe la séance", 1.0), "ext": 0.9,
   "say": "Trois : promettre des réponses. Décrivez plutôt comment se passe la séance."},
  {"k": "save", "q": "Laquelle avez-vous déjà dite&nbsp;? 👇",
   "say": "Enregistrez cette vidéo. Et dites-moi en commentaire laquelle vous avez déjà dite."},
]},
# ---------- Semaine du 19 au 25/10/2026 (tâche du dimanche 18/10) ----------
"mar-20-seance-1h": {"slug": "mar-20_reel-seance-1h", "music": "elan", "scenes": [
  {"k": "hook2", "title": "Votre séance dure 1&nbsp;h. Votre travail, <span>bien plus.</span>", "sub": "Le temps que personne ne voit.", "subt": 1.9,
   "say": "Votre séance dure une heure. Mais votre travail, bien plus."},
  {"k": "x", "tag": "LE TEMPS INVISIBLE", "title": "Autour de <span>chaque séance</span>", "top": 300, "extop": 640,
   "ex": ("list", ["Les messages pour caler le rendez-vous", "Le rappel de la veille", "L'encaissement, la facture", "Vos notes après la séance"], "auto"), "ext": 0.7,
   "say": "Les messages pour caler le rendez-vous, le rappel, la facture, vos notes."},
  {"k": "step", "n": 1, "top": 430, "extop": 930, "size": 84, "title": "Chronométrez <span>une semaine</span>",
   "ex": ("card", "LE CONSEIL", "Notez le temps passé autour de chaque séance."), "ext": 0.9,
   "say": "Un : pendant une semaine, chronométrez ce temps autour de chaque séance."},
  {"k": "step", "n": 2, "top": 430, "extop": 930, "size": 84, "title": "Un lien, <span>pas six messages</span>",
   "ex": ("vs", "Proposer des créneaux par message", "Envoyer votre lien de réservation", 0.9), "ext": 0.9,
   "say": "Deux : au lieu de proposer des créneaux par message, envoyez votre lien de réservation."},
  {"k": "step", "n": 3, "top": 430, "extop": 930, "size": 84, "title": "Comptez-le <span>dans votre tarif</span>",
   "ex": ("card", "À RETENIR", "Votre prix rémunère aussi ce temps-là."), "ext": 0.9,
   "say": "Trois : tenez-en compte dans votre tarif. Il rémunère aussi ce temps-là."},
  {"k": "save", "q": "Combien de temps passez-vous autour d'une séance&nbsp;? 👇",
   "say": "Enregistrez cette vidéo. Et vous, combien de temps passez-vous autour d'une séance ?"},
]},
"mer-21-ma-guidance": {"slug": "mer-21_reel-ma-guidance", "music": "lofi", "scenes": [
  {"k": "hook2", "title": "« Vous pouvez me renvoyer <span>ma guidance</span>&nbsp;? »", "sub": "Et vous la cherchez partout.", "subt": 2.0,
   "say": "« Vous pouvez me renvoyer ma guidance ? » Et vous la cherchez partout."},
  {"k": "x", "tag": "AVANT", "title": "Vos guidances, <span>éparpillées</span>", "top": 300, "extop": 700,
   "ex": ("list", ["!Un vocal perdu dans une conversation", "!Un texte dans vos e-mails", "!Un brouillon sur l'ordinateur"], "auto"), "ext": 0.6,
   "say": "Un vocal dans une conversation, un texte dans vos e-mails, un brouillon ailleurs."},
  {"k": "shot", "tag": "AVEC GUIDPILOT", "title": "Écrites ou vocales, <span>au même endroit</span>", "img": "guid.png", "W": 1270, "box": (20, 232, 415, 480),
   "say": "Avec Guide Pilote, toutes vos guidances, écrites ou vocales, sont au même endroit."},
  {"k": "shot", "title": "Brouillon ou finalisée&nbsp;: <span>vous savez où vous en êtes</span>", "img": "guid.png", "W": 1270, "box": (430, 150, 1235, 480), "size": 70,
   "say": "Brouillon ou finalisée : vous savez où vous en êtes."},
  {"k": "phone", "title": "Et votre cliente <span>la retrouve seule</span>", "size": 66,
   "items": [("🎧", "Guidance vocale"), ("📝", "Guidance écrite"), ("💬", "Messagerie privée")],
   "say": "Et votre cliente la retrouve seule, dans son espace."},
  {"k": "save", "kw": "GUIDANCE", "q": "et recevez la présentation en privé",
   "say": "Votre travail mérite d'être bien rangé."},
]},
"jeu-22-premier-appel": {"slug": "jeu-22_reel-premier-appel", "music": "cocon", "scenes": [
  {"k": "hook2", "title": "Elle appelle pour <span>«&nbsp;se&nbsp;renseigner&nbsp;»</span>. Que dire&nbsp;?", "size": 100,
   "say": "Elle appelle pour se renseigner. Que lui dire ?"},
  {"k": "step", "n": 1, "top": 430, "extop": 930, "size": 84, "title": "Demandez <span>ce qu'elle attend</span>",
   "ex": ("vs", "Réciter tout votre parcours", "« Qu'est-ce qui vous amène&nbsp;? »", 0.9), "ext": 0.9,
   "say": "Un : avant de parler de vous, demandez-lui ce qu'elle attend de l'accompagnement."},
  {"k": "step", "n": 2, "top": 430, "extop": 930, "size": 84, "title": "Expliquez <span>le déroulé</span>",
   "ex": ("card", "SIMPLEMENT", "La durée, le lieu ou la visio, comment se passe la première séance."), "ext": 0.9,
   "say": "Deux : expliquez simplement le déroulé. La durée, le lieu, comment se passe la première séance."},
  {"k": "step", "n": 3, "top": 430, "extop": 930, "size": 84, "title": "Proposez <span>un créneau précis</span>",
   "ex": ("vs", "« Rappelez-moi quand vous voulez »", "« Mardi 18&nbsp;h, ça vous irait&nbsp;? »", 0.9), "ext": 0.9,
   "say": "Trois : ne dites pas « rappelez-moi ». Proposez un créneau précis."},
  {"k": "bad", "top": 430, "extop": 930, "size": 84, "title": "Promettre <span>un résultat</span>",
   "ex": ("card", "PLUTÔT", "Décrivez votre accompagnement, jamais un résultat garanti."), "ext": 0.9,
   "say": "Et évitez de promettre un résultat. Décrivez votre accompagnement."},
  {"k": "save", "q": "Que dites-vous, vous, au premier appel&nbsp;? 👇",
   "say": "Enregistrez cette vidéo pour votre prochain appel."},
]},
"ven-23-rythme": {"slug": "ven-23_reel-rythme-guidance", "music": "aube", "scenes": [
  {"k": "hook2", "title": "Elle revient <span>chaque semaine</span>. Bonne nouvelle&nbsp;?", "size": 112, "sub": "Pas forcément.", "subt": 2.0,
   "say": "Elle revient chaque semaine. Bonne nouvelle ? Pas forcément."},
  {"k": "x", "tag": "LE PIÈGE", "top": 430, "extop": 930, "size": 80, "title": "La guidance <span>n'a pas le temps</span> de se vivre",
   "ex": ("card", "CE QUI SE PASSE", "Elle repose la même question, avant d'avoir pu avancer."), "ext": 1.0,
   "say": "Quand les séances s'enchaînent, la cliente repose souvent la même question, avant d'avoir pu avancer."},
  {"k": "step", "n": 1, "top": 430, "extop": 930, "size": 84, "title": "Proposez <span>un rythme</span>",
   "ex": ("card", "PAR EXEMPLE", "« Laissons passer quelques semaines avant d'y revenir. »"), "ext": 0.9,
   "say": "Un : proposez un rythme, quelques semaines entre deux séances."},
  {"k": "step", "n": 2, "top": 430, "extop": 930, "size": 84, "title": "Expliquez <span>pourquoi</span>",
   "ex": ("card", "AVEC DOUCEUR", "« Je préfère que vous ayez le temps de vivre ce qui a été dit. »"), "ext": 0.9,
   "say": "Deux : expliquez pourquoi. Elle a besoin de temps pour vivre ce qui a été dit."},
  {"k": "step", "n": 3, "top": 430, "extop": 930, "size": 84, "title": "Notez <span>la date</span> de chaque séance",
   "ex": ("card", "DANS SA FICHE", "Vous voyez tout de suite si les séances se rapprochent."), "ext": 0.9,
   "say": "Trois : notez la date de chaque séance. Vous voyez tout de suite si elles se rapprochent."},
  {"k": "save", "q": "Quel rythme conseillez-vous à vos clientes&nbsp;? 👇",
   "say": "Enregistrez cette vidéo, et dites-moi quel rythme vous conseillez."},
]},
"sam-24-concours": {"slug": "sam-24_reel-concours-2-jours", "music": "pilote", "scenes": [
  {"k": "hook2", "title": "Plus que <span>2 jours</span>", "sub": "pour gagner 1 an de GuidPilot", "subt": 0.9,
   "say": "Plus que deux jours pour gagner un an de Guide Pilote."},
  {"k": "x", "tag": "À GAGNER", "title": "Pour fêter <span>le lancement</span>", "top": 360, "extop": 760,
   "ex": ("list", ["1 an d'abonnement offert", "+ 2 abonnements de 3 mois"], "auto"), "ext": 0.6,
   "say": "À gagner : un an d'abonnement offert, et deux abonnements de trois mois."},
  {"k": "x", "tag": "POUR PARTICIPER", "title": "<span>3 étapes</span>, moins d'une minute", "top": 300, "extop": 680,
   "ex": ("list", ["Abonnez-vous à @guidpilot.fr", "Aimez cette publication", "Commentez « GuidPilot »"], "auto"), "ext": 0.6,
   "say": "Pour participer : abonnez-vous à notre compte, aimez cette publication, et commentez Guide Pilote."},
  {"k": "x", "tag": "FIN DU JEU", "top": 430, "extop": 900, "size": 84, "title": "Lundi <span>26 octobre</span>, 23&nbsp;h&nbsp;59",
   "ex": ("card", "TIRAGE AU SORT", "Le 27 octobre. Les gagnants sont contactés en message privé."), "ext": 0.9,
   "say": "Fin du jeu lundi vingt-six octobre au soir. Tirage au sort le vingt-sept."},
  {"k": "save", "kw": "GuidPilot", "q": "Ce jeu n'est ni organisé, ni parrainé, ni géré par Instagram.",
   "say": "Alors, commentez Guide Pilote. C'est maintenant."},
]},
"dim-25-tarifs": {"slug": "dim-25_reel-augmenter-tarifs", "music": "elan", "scenes": [
  {"k": "hook2", "title": "3 signes qu'il est temps d'<span>augmenter vos tarifs</span>",
   "say": "Trois signes qu'il est temps d'augmenter vos tarifs."},
  {"k": "step", "n": 1, "top": 520, "size": 88, "title": "Votre agenda est plein <span>des semaines à l'avance</span>", "extop": 1300,
   "say": "Un : votre agenda est plein plusieurs semaines à l'avance."},
  {"k": "step", "n": 2, "top": 430, "extop": 930, "size": 84, "title": "Vos prix n'ont pas bougé <span>depuis longtemps</span>",
   "ex": ("card", "ALORS QUE", "Votre expérience, elle, a grandi."), "ext": 1.0,
   "say": "Deux : vos prix n'ont pas bougé depuis longtemps, alors que votre expérience a grandi."},
  {"k": "step", "n": 3, "top": 520, "size": 88, "title": "Vous travaillez plus, <span>sans gagner mieux</span>", "extop": 1300,
   "say": "Trois : vous travaillez plus, sans gagner mieux."},
  {"k": "x", "tag": "COMMENT FAIRE", "title": "Sans <span>vous justifier</span>", "top": 300, "extop": 640,
   "ex": ("list", ["Prévenez un mois avant", "L'ancien prix pour les séances déjà réservées", "Une phrase claire, sans excuse"], "auto"), "ext": 0.7,
   "say": "Pour le faire : prévenez un mois avant, gardez l'ancien prix pour les séances déjà réservées, et annoncez-le simplement."},
  {"k": "save", "q": "À quand remonte votre dernière hausse&nbsp;? 👇",
   "say": "Enregistrez cette vidéo pour le jour où vous sauterez le pas."},
]},
}

if __name__ == "__main__":
    build(SPECS[sys.argv[1]], sys.argv[2])
