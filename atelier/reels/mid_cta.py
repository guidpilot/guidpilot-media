"""CTA de mi-vidéo (décision de Normane du 26/10/2026).

Constat : le CTA n'était qu'à la fin des vidéos, or la plupart des gens décrochent avant.
Règle : UNE seule action demandée, montrée DEUX fois :
  1. un bandeau discret vers 35-40 % de la vidéo, APRÈS une première info utile (jamais sur l'accroche),
     affiché ~3,5 s par-dessus la scène en cours, sans couper la voix ;
  2. l'écran de fin habituel (inchangé).

Le bandeau est un simple calque (comme le badge IA) animé par la timeline GSAP : il marche avec tous
les gabarits (V2, V3, conseils, promos, ManyChat) qui produisent une page avec `\\n</div>\\n<script>` et
`window.__timelines["main"]=tl;`.

Zone sûre respectée : bandeau entre y≈1360 et y≈1490, x de 60 à 930 (rien sous 1500, rien à droite de 930).

Utilisation dans un générateur, une fois le HTML final construit :
    import mid_cta
    html = mid_cta.apply(html, [sc["t"] for sc in scenes], dur, mid_cta.label_for(spec))
Désactiver pour une vidéo : "mid_cta": False dans sa spec. Forcer un texte : "mid_cta": "🔖 Enregistrez-la".
"""

CSS = """
#midcta{position:absolute;left:60px;width:870px;top:1360px;z-index:70;opacity:0;pointer-events:none;
  display:flex;align-items:center;gap:22px;padding:26px 34px;border-radius:34px;
  background:#0F172A;border:4px solid #E9C46A;box-shadow:0 18px 50px rgba(15,23,42,.35);font-family:"Inter",sans-serif}
#midcta .mi{flex:none;font-size:58px;line-height:1}
#midcta .mt{font-weight:800;font-size:46px;line-height:1.12;color:#fff;letter-spacing:-.01em}
#midcta .mt span{color:#E9C46A}
"""

# Libellés par défaut (vouvoiement, < 10 mots, aucun prix)
SAVE = ("🔖", "Enregistrez-la <span>pour plus tard</span>")


def keyword(kw):
    return ("💬", f'Commentez <span>{kw}</span>')


OFFER = ("👉", "14 jours gratuits · <span>lien en bio</span>")


def label_for(spec, default=None):
    """Choisit le texte du bandeau à partir de la spec.
    - "mid_cta": False → aucun bandeau ; "mid_cta": "texte" → texte forcé (icône 👉) ;
    - sinon : mot-clé ManyChat si la vidéo en a un (scène finale "save" avec "kw", ou champ "mot"),
      sinon `default` (ex. OFFER quand l'écran de fin est l'offre 14 jours), sinon « Enregistrez-la »."""
    v = spec.get("mid_cta", True)
    if v is False:
        return None
    if isinstance(v, str):
        return ("👉", v)
    if isinstance(v, (tuple, list)):
        return tuple(v)
    kw = spec.get("mot")
    for sc in spec.get("scenes", []):
        if isinstance(sc, dict) and sc.get("kw"):
            kw = sc["kw"]
    if kw:
        return keyword(kw)
    return default or SAVE


def pick_time(starts, dur, show=3.5):
    """Heure d'apparition : début de la 1re scène qui commence à ≥ 30 % de la vidéo (+0,4 s),
    jamais pendant la 1re scène (accroche) ni pendant la dernière (écran de fin).
    Renvoie (t, durée) ou None si la vidéo est trop courte pour un bandeau lisible."""
    if len(starts) < 3 or dur < 12:
        return None
    last = starts[-1]
    target = dur * 0.30
    cands = [t for t in starts[1:-1] if t >= target] or [starts[1]]
    t = round(min(cands) + 0.4, 2)
    if t > dur * 0.50:  # on reste « un peu avant le milieu »
        t = round(max(starts[1] + 0.4, dur * 0.36), 2)
    d = round(min(show, last - 0.3 - t), 2)
    if d < 2.2:
        return None
    return t, d


def apply(html, starts, dur, label):
    """Injecte le bandeau (CSS + calque + animations) dans une page déjà construite."""
    if not label:
        print("mid-cta : désactivé pour cette vidéo")
        return html
    when = pick_time(starts, dur)
    if not when:
        print("mid-cta : vidéo trop courte, pas de bandeau")
        return html
    t, d = when
    icon, text = label
    for a, b in ((" ?", "&nbsp;?"), (" !", "&nbsp;!")):
        text = text.replace(a, b)
    layer = f'<div id="midcta"><div class="mi">{icon}</div><div class="mt">{text}</div></div>'
    js = (f'tl.fromTo("#midcta",{{opacity:0,y:60,scale:.94}},{{opacity:1,y:0,scale:1,duration:.45,ease:"back.out(1.7)"}},{t});\n'
          f'tl.to("#midcta",{{scale:1.04,duration:.35,yoyo:true,repeat:1,ease:"sine.inOut"}},{round(t + .9, 2)});\n'
          f'tl.to("#midcta",{{opacity:0,y:40,duration:.35,ease:"power2.in"}},{round(t + d - .35, 2)});\n')
    marker_root, marker_js = "\n</div>\n<script>", 'window.__timelines["main"]=tl;'
    if marker_root not in html or marker_js not in html or "</style>" not in html:
        raise RuntimeError("mid-cta : structure de page inattendue, bandeau non injecté")
    html = html.replace("</style>", CSS + "</style>", 1)
    html = html.replace(marker_root, "\n" + layer + marker_root, 1)
    html = html.replace(marker_js, js + marker_js, 1)
    print(f"mid-cta : « {icon} {label[1]} » à {t}s pendant {d}s ({round(100 * t / dur)} % de {dur}s)")
    return html
