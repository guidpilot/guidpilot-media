"""Style V3 (25/10/2026) — demande de Normane : « changer le style, on a l'impression que c'est toujours pareil »
et « au début, un hook qui donne envie de voir le reste ».

Différences avec V2 (marine/blanc + cartes) :
- fonds unis qui changent à CHAQUE plan (crème, or, marine, bleu) ;
- typographie géante, alignée à gauche, qui apparaît MOT PAR MOT, mots clés surlignés au marqueur or ;
- barre de progression en haut (segments façon story) : on sait qu'il reste une suite → rétention ;
- accroche = boucle ouverte (question / promesse « le dernier point… ») dans la 1re seconde ;
- scènes « notifs » (téléphone + notifications qui tombent), « liste numérotée » géante, « tuiles », « cadenas » ;
- fin sur une question (pas d'écran 14 jours sur TikTok), logo officiel discret.
Aucune personne représentée. Vouvoiement. Zone sûre TikTok : rien d'important sous y=1500 ni à droite de x=930.

Usage : python3 reels/gen_tiktok_v3.py <clé> <voix.wav>  → build/<slug>/ ; textes dans SPECS ci-dessous.
Puis : cd build/<slug> && npx hyperframes render --output ../<slug>.mp4 ; musique/mixer.sh.
"""
import html as H, pathlib, re, shutil, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_conseils as gc

PAL = {  # fond, texte, surlignage (fond du marqueur), texte surligné
    "creme": ("#FBF7EE", "#0F172A", "#E9C46A", "#0F172A"),
    "or": ("#E9C46A", "#0F172A", "#0F172A", "#FFFFFF"),
    "marine": ("#0F172A", "#FFFFFF", "#E9C46A", "#0F172A"),
    "bleu": ("#2563EB", "#FFFFFF", "#0F172A", "#FFFFFF"),
}

CSS = gc.CSS.split(".navy{")[0] + """
.clip{position:absolute;inset:0;overflow:hidden}
.wrap{position:absolute;left:90px;right:150px;top:0;bottom:0}
.kin{position:absolute;left:0;right:0;font-weight:800;letter-spacing:-.035em;line-height:1.02}
.kin .w{display:inline-block;margin-right:.22em;position:relative;white-space:nowrap}
.kin .w.hl{padding:0 .12em;margin-left:-.06em}
.kin .w.hl::before{content:"";position:absolute;left:0;right:0;top:.12em;bottom:.02em;border-radius:.14em;background:var(--hl);z-index:-1;transform:scaleX(var(--s,0));transform-origin:left}
.kin .w>b{position:relative;font-weight:800}
.small{position:absolute;left:0;right:0;font-weight:700;font-size:50px;line-height:1.25}
.eyebrow{position:absolute;left:0;font-weight:800;font-size:34px;letter-spacing:.14em;text-transform:uppercase;padding:12px 26px;border-radius:999px}
.prog{position:absolute;left:40px;right:40px;top:128px;height:10px;display:flex;gap:10px;z-index:60}
.prog i{flex:1;height:10px;border-radius:6px;background:rgba(148,163,184,.35);overflow:hidden;position:relative}
.prog i b{position:absolute;inset:0;background:#E9C46A;transform:scaleX(0);transform-origin:left}
.aibadge3{position:absolute;left:40px;top:156px;z-index:60;font-weight:600;font-size:26px;padding:8px 18px;border-radius:999px;background:rgba(15,23,42,.6);color:#E2E8F0}
.phone{position:absolute;left:150px;width:640px;height:1000px;border-radius:70px;background:#0B1220;border:14px solid #1E293B;box-shadow:0 40px 90px rgba(15,23,42,.35);overflow:hidden}
.phone .clock{position:absolute;top:70px;left:0;right:0;text-align:center;color:#E2E8F0;font-weight:700;font-size:96px;letter-spacing:-.02em}
.phone .date{position:absolute;top:190px;left:0;right:0;text-align:center;color:#94A3B8;font-weight:600;font-size:30px}
.notif{position:absolute;left:28px;right:28px;background:rgba(248,250,252,.96);border-radius:30px;padding:24px 26px;display:flex;gap:20px;align-items:flex-start}
.notif .ic{flex:none;width:64px;height:64px;border-radius:16px;background:#0F172A;color:#E9C46A;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:34px}
.notif .tx{flex:1;text-align:left}
.notif .ap{font-weight:700;font-size:22px;color:#64748B;letter-spacing:.04em;text-transform:uppercase}
.notif .ti{font-weight:800;font-size:30px;color:#0F172A;margin-top:4px;line-height:1.2}
.notif .bo{font-weight:600;font-size:26px;color:#334155;margin-top:4px;line-height:1.25}
.bignum{position:absolute;left:-12px;font-weight:800;font-size:360px;line-height:.8;letter-spacing:-.06em}
.tile{position:absolute;width:400px;height:300px;border-radius:40px;padding:36px 34px;display:flex;flex-direction:column;justify-content:space-between}
.tile .g{font-size:70px;line-height:1;font-weight:800}
.tile .l{font-weight:800;font-size:44px;line-height:1.1;letter-spacing:-.02em}
.lockc{position:absolute;left:0;width:840px;border-radius:44px;padding:54px 50px;border:5px dashed #E9C46A}
.lockc .k{font-size:110px;line-height:1}
.lockc .t{margin-top:26px;font-weight:800;font-size:76px;line-height:1.05;letter-spacing:-.03em;color:#fff}
.lockc .s{margin-top:22px;font-weight:600;font-size:44px;color:#CBD5E1;line-height:1.25}
.strike{position:absolute;left:0;height:12px;border-radius:6px;background:#DC2626;transform-origin:left;transform:scaleX(0)}
.endq{position:absolute;left:0;right:0;font-weight:800;font-size:96px;line-height:1.05;letter-spacing:-.03em;color:#fff}
.endlogo{position:absolute;left:0;width:330px}
.save{position:absolute;left:0;font-weight:700;font-size:40px;color:#E9C46A}
"""


def words(txt, size, top, pal, sid, color=None):
    """Texte cinétique : [mot] = surligné. Renvoie (html, ids des mots, ids surlignés)."""
    bg, fg, hl, hlt = PAL[pal]
    out, ids, hls = [], [], []
    for n, tok in enumerate(re.findall(r"\[[^\]]+\]|\S+", txt)):
        wid = f"{sid}w{n}"
        if tok.startswith("["):
            for m, part in enumerate(tok[1:-1].split()):
                pid = f"{wid}_{m}"
                out.append(f'<span class="w hl" id="{pid}" style="--hl:{hl}"><b style="color:{hlt}">{H.escape(part)}</b></span>')
                ids.append(pid); hls.append(pid)
        else:
            out.append(f'<span class="w" id="{wid}">{H.escape(tok)}</span>'); ids.append(wid)
    html = f'<div class="kin" style="top:{top}px;font-size:{size}px;color:{color or fg}">{"".join(out)}</div>'
    return html.replace(" ?", "&nbsp;?").replace(" !", "&nbsp;!"), ids, hls


def kin_js(ids, hls, t, step=0.11):
    js = []
    for k, i in enumerate(ids):
        js.append(f'tl.fromTo("#{i}",{{opacity:0,y:70,rotate:4}},{{opacity:1,y:0,rotate:0,duration:.32,ease:"back.out(2)"}},{t + k * step:.2f});')
    for k, i in enumerate(hls):
        js.append(f'tl.fromTo("#{i}",{{"--s":0}},{{"--s":1,duration:.22,ease:"power2.out"}},{t + ids.index(i) * step:.2f});')
    return js


def scene(i, sc, t0, t1, nseg):
    sid = f"s{i}"; pal = sc.get("bg", "creme"); bg, fg, hl, hlt = PAL[pal]
    body, js = [], []
    k = sc["k"]
    js.append(f'tl.fromTo("#{sid}",{{scale:1.06}},{{scale:1,duration:.55,ease:"power3.out"}},{t0:.2f});')
    if sc.get("eyebrow"):
        ebg, efg = (("#0F172A", "#E9C46A") if pal in ("creme", "or") else ("#E9C46A", "#0F172A"))
        body.append(f'<div class="eyebrow" id="{sid}e" style="top:{sc.get("etop", 540)}px;background:{ebg};color:{efg}">{H.escape(sc["eyebrow"])}</div>')
        js.append(f'tl.fromTo("#{sid}e",{{opacity:0,x:-40}},{{opacity:1,x:0,duration:.35,ease:"power3.out"}},{t0 + .05:.2f});')
    if k in ("hook", "words"):
        h, ids, hls = words(sc["title"], sc.get("size", 132), sc.get("top", 520) + 140, pal, sid)
        body.append(h); js += kin_js(ids, hls, t0 + (0.0 if k == "hook" else .1), sc.get("step", .11))
        if sc.get("sub"):
            body.append(f'<div class="small" id="{sid}u" style="top:{sc.get("subtop", 1180) + 140}px;color:{fg};opacity:.82">{H.escape(sc["sub"])}</div>')
            js.append(f'tl.fromTo("#{sid}u",{{opacity:0,y:30}},{{opacity:.82,y:0,duration:.4,ease:"power3.out"}},{t0 + sc.get("subt", 1.2):.2f});')
        if sc.get("strike"):
            body.append(f'<div class="strike" id="{sid}x" style="top:{sc["strike"][0]}px;width:{sc["strike"][1]}px"></div>')
            js.append(f'tl.to("#{sid}x",{{scaleX:1,duration:.35,ease:"power2.inOut"}},{t0 + sc.get("striket", 1.2):.2f});')
    elif k == "num":
        body.append(f'<div class="bignum" id="{sid}n" style="top:{sc.get("ntop", 330)}px;color:{hl if pal == "marine" else fg};opacity:.95">{sc["n"]}</div>')
        js.append(f'tl.fromTo("#{sid}n",{{opacity:0,scale:.5,x:-60}},{{opacity:.95,scale:1,x:0,duration:.45,ease:"back.out(1.8)"}},{t0:.2f});')
        h, ids, hls = words(sc["title"], sc.get("size", 120), sc.get("top", 760), pal, sid)
        body.append(h); js += kin_js(ids, hls, t0 + .25)
        if sc.get("sub"):
            body.append(f'<div class="small" id="{sid}u" style="top:{sc.get("subtop", 1180)}px;color:{fg};opacity:.82">{H.escape(sc["sub"])}</div>')
            js.append(f'tl.fromTo("#{sid}u",{{opacity:0,y:30}},{{opacity:.82,y:0,duration:.4,ease:"power3.out"}},{t0 + sc.get("subt", 1.0):.2f});')
    elif k == "notifs":
        h, ids, hls = words(sc["title"], sc.get("size", 92), 300, pal, sid)
        body.append(h); js += kin_js(ids, hls, t0 + .05, .08)
        ph = [f'<div class="phone" id="{sid}p" style="top:{sc.get("ptop", 560)}px"><div class="clock">{sc.get("clock", "09:41")}</div><div class="date">{H.escape(sc.get("date", "mardi 28 octobre"))}</div>']
        for n, (ic, ap, ti, bo) in enumerate(sc["items"]):
            ph.append(f'<div class="notif" id="{sid}n{n}" style="top:{290 + n * 190}px"><div class="ic">{ic}</div><div class="tx"><div class="ap">{H.escape(ap)}</div><div class="ti">{H.escape(ti)}</div><div class="bo">{H.escape(bo)}</div></div></div>')
        body.append("".join(ph) + "</div>")
        js.append(f'tl.fromTo("#{sid}p",{{y:220,opacity:0}},{{y:0,opacity:1,duration:.5,ease:"power3.out"}},{t0 + .15:.2f});')
        span = max(.6, (t1 - t0 - 1.0) / max(1, len(sc["items"])))
        for n in range(len(sc["items"])):
            js.append(f'tl.fromTo("#{sid}n{n}",{{y:-120,opacity:0,scale:.92}},{{y:0,opacity:1,scale:1,duration:.4,ease:"back.out(1.6)"}},{t0 + .6 + n * span:.2f});')
    elif k == "tiles":
        h, ids, hls = words(sc["title"], sc.get("size", 92), 300, pal, sid)
        body.append(h); js += kin_js(ids, hls, t0 + .05, .08)
        cols = [("#FFFFFF", "#0F172A"), ("#E9C46A", "#0F172A"), ("#2563EB", "#FFFFFF"), ("#1E293B", "#FFFFFF")]
        span = max(.5, (t1 - t0 - .9) / len(sc["items"]))
        for n, (g, lab) in enumerate(sc["items"]):
            x, y = (n % 2) * 430, 620 + (n // 2) * 330
            tb, tf = cols[n % 4]
            body.append(f'<div class="tile" id="{sid}t{n}" style="left:{x}px;top:{y}px;background:{tb};color:{tf}"><div class="g">{g}</div><div class="l">{lab}</div></div>')
            js.append(f'tl.fromTo("#{sid}t{n}",{{opacity:0,scale:.6,rotate:n%2?6:-6}},{{opacity:1,scale:1,rotate:0,duration:.45,ease:"back.out(1.7)"}},{t0 + .5 + n * span:.2f});'.replace("n%2?6:-6", "6" if n % 2 else "-6"))
    elif k == "lock":
        h, ids, hls = words(sc["title"], sc.get("size", 100), 330, pal, sid)
        body.append(h); js += kin_js(ids, hls, t0 + .05, .09)
        body.append(f'<div class="lockc" id="{sid}l" style="top:{sc.get("ltop", 760)}px"><div class="k">🔒</div><div class="t">{sc["card"]}</div><div class="s">{H.escape(sc["note"])}</div></div>')
        js.append(f'tl.fromTo("#{sid}l",{{opacity:0,y:90}},{{opacity:1,y:0,duration:.5,ease:"back.out(1.5)"}},{t0 + .7:.2f});')
    elif k == "end":
        body.append(f'<div class="endq" id="{sid}q" style="top:{sc.get("top", 640)}px">{sc["title"]}</div>')
        js.append(f'tl.fromTo("#{sid}q",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.5,ease:"power3.out"}},{t0 + .05:.2f});')
        body.append(f'<div class="save" id="{sid}s" style="top:{sc.get("savetop", 1150)}px">{H.escape(sc.get("save", "Répondez en commentaire 👇"))}</div>')
        js.append(f'tl.fromTo("#{sid}s",{{opacity:0,x:-40}},{{opacity:1,x:0,duration:.4,ease:"power3.out"}},{t0 + .8:.2f});')
        body.append(f'<img class="endlogo" id="{sid}g" src="assets/logo_blanc.png" alt="GuidPilot" style="top:1300px" />')
        js.append(f'tl.fromTo("#{sid}g",{{opacity:0}},{{opacity:1,duration:.5}},{t0 + 1.0:.2f});')
    html = (f'<div id="{sid}" class="clip" data-start="{t0}" data-duration="{round(t1 - t0, 2)}" data-track-index="1" '
            f'style="background:{bg}"><div class="wrap">{"".join(body)}</div></div>')
    js.append(f'tl.to("#pb{i} b",{{scaleX:1,duration:{max(.3, t1 - t0):.2f},ease:"none"}},{t0:.2f});')
    return html, "\n".join(js)


def build(spec, voix):
    gc.align(spec, voix)
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voix],
                                 capture_output=True, text=True).stdout)
    dur = round(total + 1.4, 2)
    scs = spec["scenes"]; n = len(scs)
    bodies, jss = [], []
    for i, sc in enumerate(scs):
        t1 = scs[i + 1]["t"] if i + 1 < n else dur
        h, j = scene(i, sc, sc["t"], t1, n)
        bodies.append(h); jss.append(j)
    prog = '<div class="prog">' + "".join(f'<i id="pb{i}"><b></b></i>' for i in range(n)) + "</div>"
    page = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="vendor/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{dur}" data-width="1080" data-height="1920">
{prog}<div class="aibadge3">Voix off générée par IA</div>
<audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{dur}" data-volume="1"></audio>
{"".join(bodies)}
</div>
<script>
const tl=gsap.timeline({{paused:true}});
{chr(10).join(jss)}
window.__timelines["main"]=tl;
</script></body></html>'''
    import mid_cta  # CTA de mi-vidéo (26/10/2026) : TikTok → « Enregistrez-la » ; Reel IG en V3 → mot-clé si "mot"/"kw"
    page = mid_cta.apply(page, [sc["t"] for sc in scs], dur, mid_cta.label_for(spec))
    d = gc.BASE / "build" / spec["slug"]
    if d.exists(): shutil.rmtree(d)
    (d / "assets").mkdir(parents=True)
    for sub in ("fonts", "vendor"): shutil.copytree(gc.SRC / sub, d / sub)
    for f in ("hyperframes.json", "meta.json"): shutil.copy(gc.SRC / f, d / f)
    shutil.copy(gc.SRC / "assets" / "logo_blanc.png", d / "assets" / "logo_blanc.png")
    shutil.copy(voix, d / "assets" / "voix.wav")
    (d / "index.html").write_text(page)
    print("ok", d, "durée", dur)


SPECS = {
"tt7": {"slug": "tt7-rappel-automatique", "music": "lofi", "file": "07-le-rappel-qui-part-tout-seul.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : le rappel de séance qui part tout seul. #pourtoi #praticien",
 "scenes": [
  {"k": "hook", "bg": "marine", "title": "Votre cliente a oublié son [rendez-vous.]", "size": 128, "top": 470,
   "sub": "Et ce n'est pas elle, le problème.", "subt": 1.6, "subtop": 1060,
   "say": "Votre cliente a oublié son rendez-vous. Et ce n'est pas elle, le problème."},
  {"k": "words", "bg": "or", "title": "Il lui manquait [un rappel.]", "size": 150, "top": 560,
   "say": "Il lui manquait juste un rappel."},
  {"k": "notifs", "bg": "creme", "title": "Dès qu'elle [réserve]", "clock": "18:32", "date": "lundi 27 octobre",
   "items": [("✓", "E-mail · GuidPilot", "Réservation confirmée", "Séance de 60 min · jeudi 14:00"),
             ("⏰", "E-mail · GuidPilot", "Rappel : votre séance approche", "Jeudi 14:00 · à très bientôt")],
   "say": "Avec GuidPilot, dès qu'elle réserve, elle reçoit une confirmation par e-mail. Puis un rappel avant la séance, envoyé tout seul."},
  {"k": "words", "bg": "bleu", "title": "Vous, vous n'y [pensez plus.]", "size": 140, "top": 600,
   "say": "Vous, vous n'y pensez plus."},
  {"k": "end", "bg": "marine", "title": "Vos rappels, vous les envoyez encore <span style=\"color:#E9C46A\">à la main&nbsp;?</span>",
   "say": "Et vos rappels, vous les envoyez encore à la main ?"},
 ]},
"tt8": {"slug": "tt8-lien-visio-automatique", "music": "elan", "file": "08-trois-messages-avant-la-visio.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : 3 messages que vous n'écrivez plus avant une séance en visio. #pourtoi #praticien",
 "scenes": [
  {"k": "hook", "bg": "or", "title": "Séance en visio : [3 messages] que vous n'écrivez plus.", "size": 118, "top": 450,
   "say": "Avant une séance en visio, il y a trois messages que vous n'avez plus besoin d'écrire."},
  {"k": "num", "bg": "creme", "n": "1", "title": "La [confirmation]", "say": "Un : la confirmation."},
  {"k": "num", "bg": "marine", "n": "2", "title": "Le [lien] de la visio", "say": "Deux : le lien de la visio."},
  {"k": "num", "bg": "bleu", "n": "3", "title": "Le [rappel]", "say": "Trois : le rappel."},
  {"k": "notifs", "bg": "creme", "title": "Le lien Google Meet part [tout seul]", "size": 84, "clock": "10:05", "date": "mercredi 29 octobre",
   "items": [("✓", "E-mail · GuidPilot", "Votre séance en ligne est confirmée", "Mercredi 18:00 · 45 min"),
             ("▶", "Lien de la séance", "Rejoindre avec Google Meet", "Le lien est dans votre confirmation")],
   "say": "Avec GuidPilot, quand votre cliente réserve une séance en ligne, le lien Google Meet est créé et envoyé automatiquement, avec la confirmation."},
  {"k": "end", "bg": "marine", "title": "Il ne vous reste qu'à <span style=\"color:#E9C46A\">vous connecter.</span>",
   "save": "Enregistrez cette vidéo 🔖", "say": "Il ne vous reste plus qu'à vous connecter."},
 ]},
"tt9": {"slug": "tt9-espace-client", "music": "aube", "file": "09-ce-que-voit-votre-cliente.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : ce que voit votre cliente dans son espace. #pourtoi #praticien",
 "scenes": [
  {"k": "hook", "bg": "creme", "title": "Ce que voit votre cliente [quand elle se connecte…]", "size": 118, "top": 450,
   "sub": "Le dernier point va vous rassurer.", "subt": 1.9, "subtop": 1110,
   "say": "Voici ce que voit votre cliente quand elle se connecte à son espace. Et le dernier point va vous rassurer."},
  {"k": "tiles", "bg": "marine", "title": "Dans [son espace]",
   "items": [("📅", "Ses rendez-vous"), ("✎", "Ce que vous lui avez écrit ou enregistré"), ("€", "Ses factures en PDF"), ("✉", "Vos échanges, à part")],
   "say": "Ses rendez-vous, à venir et passés. Ce que vous lui avez écrit ou enregistré après la séance. Ses factures, en PDF. Et vos échanges, à part de votre messagerie personnelle."},
  {"k": "lock", "bg": "marine", "title": "Ce qu'elle ne voit [jamais]", "card": "Vos notes privées", "note": "Elles restent pour vous.",
   "say": "Ce qu'elle ne voit jamais : vos notes privées. Elles restent pour vous."},
  {"k": "end", "bg": "marine", "title": "Vos clientes retrouvent-elles <span style=\"color:#E9C46A\">tout facilement&nbsp;?</span>",
   "say": "Vos clientes retrouvent-elles tout facilement ?"},
 ]},
"tt10": {"slug": "tt10-paiement-en-ligne", "music": "pilote", "file": "10-je-vous-fais-le-virement-ce-soir.mp4",
 "caption": "Comment gagner du temps avec GuidPilot : le paiement en ligne au moment de réserver. #pourtoi #praticien",
 "scenes": [
  {"k": "hook", "bg": "bleu", "title": "« Je vous fais le virement [ce soir.] »", "size": 128, "top": 470,
   "sub": "Vous connaissez la suite.", "subt": 1.7, "subtop": 1080,
   "say": "« Je vous fais le virement ce soir. » Vous connaissez la suite."},
  {"k": "words", "bg": "marine", "title": "3 jours plus tard, vous vérifiez [encore] votre compte.", "size": 112, "top": 520,
   "say": "Trois jours plus tard, vous vérifiez encore votre compte."},
  {"k": "notifs", "bg": "creme", "title": "Elle paie [en réservant]", "clock": "21:14", "date": "jeudi 30 octobre",
   "items": [("€", "GuidPilot", "Paiement reçu", "Séance de jeudi · réglée en ligne"),
             ("✓", "GuidPilot", "Facture marquée Payée", "Numérotée automatiquement")],
   "say": "Avec GuidPilot, votre cliente peut payer en ligne au moment où elle réserve. La facture passe toute seule à Payée."},
  {"k": "words", "bg": "or", "title": "Plus personne [à relancer.]", "size": 140, "top": 600,
   "say": "Et vous n'avez plus à relancer personne."},
  {"k": "end", "bg": "marine", "title": "Combien de virements attendez-vous <span style=\"color:#E9C46A\">en ce moment&nbsp;?</span>",
   "say": "Combien de virements attendez-vous, en ce moment ?"},
 ]},
}

INTERDITS = ["guidance", "tarot", "tarolog", "voyan", "médium", "medium", "cartomanc", "divinatoire", "reiki", "thérapeute", "therapeute"]

if __name__ == "__main__":
    if sys.argv[1] == "check":
        for k, s in SPECS.items():
            blob = str(s).lower(); print(k, [w for w in INTERDITS if w in blob] or "ok", " ".join(sc["say"] for sc in s["scenes"]))
    else:
        build(SPECS[sys.argv[1]], sys.argv[2])
