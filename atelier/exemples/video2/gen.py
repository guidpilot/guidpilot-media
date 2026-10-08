"""Génère index.html de la vidéo 2 à partir d'un tableau de timings (scènes calées sur la voix)."""
import json, sys

# Début de chaque scène (secondes) + durée totale. Ajusté sur la voix off.
T = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {
    "s1": 0, "s2": 6.5, "s3": 10.5, "s4": 15, "s5": 19.5, "s6": 24.5, "s7": 28, "end": 36,
    "nocard": 31.5, "bio": 33,
}
order = ["s1", "s2", "s3", "s4", "s5", "s6", "s7"]
D = {k: round((T[order[i + 1]] if i + 1 < len(order) else T["end"]) - T[k], 2) for i, k in enumerate(order)}

def clip(id_, cls):
    return f'id="{id_}" class="clip {cls}" data-start="{T[id_]}" data-duration="{D[id_]}" data-track-index="1"'

STAR = '<svg class="star" viewBox="0 0 24 24"><path fill="#E9B949" d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.6 7L12 17.3 5.8 20.9l1.6-7L2 9.2l7.1-.6z"/></svg>'

html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="vendor/gsap.min.js"></script>
<style>
@font-face{{font-family:"Inter";src:url("fonts/inter-latin-400-normal.woff2") format("woff2");font-weight:400}}
@font-face{{font-family:"Inter";src:url("fonts/inter-latin-600-normal.woff2") format("woff2");font-weight:600}}
@font-face{{font-family:"Inter";src:url("fonts/inter-latin-700-normal.woff2") format("woff2");font-weight:700}}
@font-face{{font-family:"Inter";src:url("fonts/inter-latin-800-normal.woff2") format("woff2");font-weight:800}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#F6F8FC}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;font-family:"Inter",sans-serif;color:#0F172A}}
.clip{{position:absolute;inset:0}}
.navy{{background:#0F172A}} .light{{background:#F6F8FC}}
.center{{position:absolute;left:0;right:0;display:flex;flex-direction:column;align-items:center;text-align:center}}
.kicker{{font-weight:700;font-size:44px;letter-spacing:.14em;color:#E9C46A;text-transform:uppercase}}
.hook{{font-weight:800;font-size:96px;line-height:1.06;color:#fff;letter-spacing:-.02em;margin-top:28px;width:920px}}
.hook b{{color:#60A5FA;font-weight:800}}
.gchip{{position:relative;margin:14px 0;padding:24px 44px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#94A3B8;font-weight:600;font-size:44px;white-space:nowrap}}
.strike{{position:absolute;left:30px;right:30px;top:50%;height:6px;margin-top:-3px;background:#F87171;border-radius:3px}}
.cards{{position:absolute;left:0;right:0;top:250px;height:200px}}
.tcard{{position:absolute;left:470px;top:0;width:120px;height:190px;border:4px solid #E9C46A;border-radius:16px}}
.logo-big{{width:820px;display:block}}
.claim{{font-weight:800;font-size:84px;line-height:1.1;color:#fff;margin-top:70px;width:920px;letter-spacing:-.02em}}
.claim span{{color:#E9C46A}}
.stitle{{font-weight:800;font-size:82px;line-height:1.08;letter-spacing:-.02em;width:920px}}
.stitle span{{color:#2563EB}}
.sub{{font-weight:600;font-size:40px;color:#64748B;margin-top:22px;width:900px;line-height:1.3}}
.frame{{position:absolute;left:60px;width:960px;background:#fff;border-radius:28px;overflow:hidden;border:2px solid #E2E8F0}}
.bar{{height:56px;background:#F1F5F9;border-bottom:2px solid #E2E8F0;display:flex;align-items:center;padding-left:24px;gap:12px}}
.dot{{width:16px;height:16px;border-radius:50%;background:#CBD5E1}}
.demo{{position:absolute;right:24px;top:12px;font-size:22px;font-weight:600;color:#64748B;background:#fff;border:2px solid #E2E8F0;border-radius:999px;padding:4px 16px}}
.vp{{position:relative;overflow:hidden}}
.shot{{position:absolute;left:0;top:0;display:block;max-width:none}}
.pill{{position:absolute;padding:26px 40px;border-radius:24px;background:#0F172A;color:#fff;font-weight:700;font-size:42px;white-space:nowrap}}
.pill i{{font-style:normal;color:#4ADE80;margin-right:16px}}
.check{{display:flex;align-items:center;gap:22px;font-weight:700;font-size:46px;color:#0F172A;margin:16px 0;width:820px}}
.check i{{font-style:normal;flex:none;width:64px;height:64px;border-radius:50%;background:#DCFCE7;color:#16A34A;display:flex;align-items:center;justify-content:center;font-size:38px}}
.invoice{{position:absolute;left:300px;width:480px;height:300px;background:#fff;border:2px solid #E2E8F0;border-radius:24px;padding:36px}}
.invoice .l{{height:18px;border-radius:9px;background:#E2E8F0;margin-bottom:20px}}
.invoice .t{{font-weight:800;font-size:40px;color:#0F172A;margin-bottom:26px}}
.paid{{position:absolute;right:28px;bottom:28px;background:#DCFCE7;color:#15803D;font-weight:800;font-size:34px;padding:10px 24px;border-radius:999px}}
.zero{{font-weight:800;font-size:330px;line-height:.9;color:#0F172A;letter-spacing:-.05em}}
.zero span{{font-size:160px;color:#2563EB}}
.zlabel{{font-weight:800;font-size:72px;margin-top:20px}}
.zsub{{font-weight:700;font-size:56px;color:#2563EB;margin-top:60px;width:900px;line-height:1.15}}
.fine{{font-weight:500;font-size:30px;color:#64748B;margin-top:50px}}
.offer{{display:inline-block;background:#FBF3DC;color:#6B4E16;font-weight:700;font-size:38px;padding:16px 36px;border-radius:999px;letter-spacing:.02em}}
.big14{{font-weight:800;font-size:200px;line-height:.95;color:#fff;letter-spacing:-.04em;margin-top:40px}}
.big14 small{{display:block;font-size:92px;letter-spacing:-.02em;margin-top:12px}}
.nocard{{margin-top:44px;font-weight:700;font-size:62px;color:#4ADE80}}
.price{{margin-top:44px;font-weight:600;font-size:40px;color:#CBD5E1;line-height:1.45;width:900px}}
.bio{{margin-top:60px;display:inline-block;background:#2563EB;color:#fff;font-weight:800;font-size:58px;padding:30px 60px;border-radius:999px}}
.aibadge{{position:absolute;left:40px;top:64px;z-index:50;padding:12px 24px;border-radius:999px;background:rgba(15,23,42,.72);color:#E2E8F0;font-family:Inter,sans-serif;font-weight:600;font-size:28px;letter-spacing:.01em;border:1px solid rgba(255,255,255,.25)}}
.stars{{display:flex;gap:22px;justify-content:center}} .star{{width:100px;height:100px}}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T['end']}" data-width="1080" data-height="1920">
  <div class="aibadge">Voix off générée par IA</div>
  <audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{T['end']}" data-volume="1"></audio>

  <div {clip('s1','navy')}>
    <div class="cards"><div class="tcard" id="c1"></div><div class="tcard" id="c2"></div><div class="tcard" id="c3"></div></div>
    <div class="center" style="top:500px">
      <div class="kicker" id="k1">Tarot · Guidance · Médiumnité</div>
      <div class="hook" id="h1">Les logiciels classiques <b>ne sont pas faits pour vous</b></div>
    </div>
    <div class="center" style="top:1010px">
      <div class="gchip" id="g1">Agenda générique<span class="strike" id="x1"></span></div>
      <div class="gchip" id="g2">Réservation générique<span class="strike" id="x2"></span></div>
      <div class="gchip" id="g3">Facturation générique<span class="strike" id="x3"></span></div>
    </div>
  </div>

  <div {clip('s2','navy')}>
    <div class="center" style="top:620px">
      <img class="logo-big" id="logo2" src="assets/logo_blanc.png" alt="GuidPilot" />
      <div class="claim" id="claim2">Conçu pour <span>les praticiens de la guidance.</span></div>
    </div>
  </div>

  <div {clip('s3','light')}>
    <div class="center" style="top:170px">
      <div class="stitle" id="t3">Votre propre <span>page praticien</span></div>
      <div class="sub" id="u3">Prestations · Avis · Réservation en ligne</div>
    </div>
    <div class="frame" id="f3" style="top:540px">
      <div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">Compte de démonstration</span></div>
      <div class="vp" style="height:780px"><img class="shot" id="i3" src="assets/page.png" alt="" style="width:1200px" /></div>
    </div>
    <div class="center" style="top:1410px"><div class="stars" id="stars3">{STAR*5}</div></div>
  </div>

  <div {clip('s4','light')}>
    <div class="center" style="top:170px">
      <div class="stitle" id="t4">Visible dans <span>l'annuaire GuidPilot</span></div>
      <div class="sub" id="u4">De nouveaux clients vous trouvent</div>
    </div>
    <div class="frame" id="f4" style="top:560px">
      <div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">guidpilot.fr/praticiens</span></div>
      <div class="vp" style="height:408px"><img class="shot" id="i4" src="assets/annuaire.png" alt="" style="width:960px" /></div>
    </div>
    <div class="pill" id="p4" style="left:140px;top:1130px">Recherche par spécialité ou ville</div>
  </div>

  <div {clip('s5','light')}>
    <div class="center" style="top:170px">
      <div class="stitle" id="t5">Facture créée <span>automatiquement</span></div>
      <div class="sub" id="u5">À chaque réservation payée</div>
    </div>
    <div class="invoice" id="inv5" style="top:520px">
      <div class="t">Facture</div><div class="l" style="width:80%"></div><div class="l" style="width:60%"></div><div class="l" style="width:70%"></div>
      <div class="paid" id="paid5">Payée ✓</div>
    </div>
    <div class="frame" id="f5" style="top:880px">
      <div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">Compte de démonstration</span></div>
      <div class="vp" style="height:300px"><img class="shot" id="i5" src="assets/finance.png" alt="" style="width:1580px" /></div>
    </div>
    <div class="center" style="top:1260px">
      <div class="check" id="k5a"><i>✓</i>Numérotation automatique</div>
      <div class="check" id="k5b"><i>✓</i>Mentions légales incluses</div>
    </div>
  </div>

  <div {clip('s6','light')}>
    <div class="center" style="top:330px">
      <div class="zero" id="z6">0<span>%</span></div>
      <div class="zlabel" id="zl6">de commission sur vos séances</div>
      <div class="zsub" id="zs6">Vos clients restent les vôtres.</div>
      <div class="fine" id="zf6">Hors frais du moyen de paiement (Stripe, PayPal)</div>
    </div>
  </div>

  <div {clip('s7','navy')}>
    <div class="center" style="top:200px"><img id="logo7" src="assets/logo_blanc.png" alt="GuidPilot" style="width:520px;display:block" /></div>
    <div class="center" style="top:470px">
      <div class="offer" id="o7">Essai gratuit</div>
      <div class="big14" id="b7">14 jours<small>gratuits</small></div>
      <div class="nocard" id="n7">✓ Sans carte bancaire</div>
      <div class="bio" id="bio7">Lien dans la bio ↓</div>
    </div>
  </div>
</div>
<script>
const T={json.dumps(T)}; const D={json.dumps(D)};
const tl = gsap.timeline({{ paused: true }});
const E="power3.out";
/* S1 */
tl.fromTo("#c1",{{opacity:0,rotation:0,x:0}},{{opacity:1,rotation:-14,x:-110,duration:.6,ease:E}},.1);
tl.fromTo("#c2",{{opacity:0,y:30}},{{opacity:1,y:-10,duration:.6,ease:E}},.15);
tl.fromTo("#c3",{{opacity:0,rotation:0,x:0}},{{opacity:1,rotation:14,x:110,duration:.6,ease:E}},.2);
tl.fromTo("#k1",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.5,ease:E}},.25);
tl.fromTo("#h1",{{opacity:0,y:60,scale:.94}},{{opacity:1,y:0,scale:1,duration:.6,ease:"back.out(1.6)"}},.45);
const s1=D.s1;
["#g1","#g2","#g3"].forEach((g,i)=>{{
  tl.fromTo(g,{{opacity:0,y:40}},{{opacity:1,y:0,duration:.4,ease:E}},3.6+i*.3);
  tl.fromTo("#x"+(i+1),{{scaleX:0}},{{scaleX:1,duration:.3,ease:"power2.out",transformOrigin:"left center"}},4.9+i*.3);
}});
/* S2 */
tl.fromTo("#logo2",{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"}},T.s2+.05);
tl.fromTo("#claim2",{{opacity:0,y:50}},{{opacity:1,y:0,duration:.55,ease:E}},T.s2+.7);
/* écrans */
function screen(id,t0,dur,pan){{
  tl.fromTo("#t"+id,{{opacity:0,y:40}},{{opacity:1,y:0,duration:.45,ease:E}},t0+.05);
  tl.fromTo("#u"+id,{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},t0+.2);
  tl.fromTo("#f"+id,{{opacity:0,y:160,scale:.92}},{{opacity:1,y:0,scale:1,duration:.6,ease:E}},t0+.15);
  if(pan) tl.fromTo("#i"+id,{{x:pan[0],y:pan[1]}},{{x:pan[2],y:pan[3],duration:dur-.4,ease:"sine.inOut"}},t0+.4);
}}
screen(3,T.s3,D.s3,[0,0,-240,0]);
document.querySelectorAll("#stars3 .star").forEach((s,i)=>tl.fromTo(s,{{opacity:0,scale:0,rotation:-40}},{{opacity:1,scale:1,rotation:0,duration:.35,ease:"back.out(2.4)"}},T.s3+D.s3*.45+i*.12));
screen(4,T.s4,D.s4,null);
tl.fromTo("#p4",{{opacity:0,y:60,scale:.8}},{{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(1.8)"}},T.s4+D.s4*.45);
/* S5 facture */
tl.fromTo("#t5",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.45,ease:E}},T.s5+.05);
tl.fromTo("#u5",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},T.s5+.2);
tl.fromTo("#inv5",{{opacity:0,y:-80,rotation:-6}},{{opacity:1,y:0,rotation:0,duration:.6,ease:"back.out(1.6)"}},T.s5+.3);
tl.fromTo("#paid5",{{opacity:0,scale:2}},{{opacity:1,scale:1,duration:.35,ease:"back.out(2)"}},T.s5+1.1);
tl.fromTo("#f5",{{opacity:0,y:120}},{{opacity:1,y:0,duration:.6,ease:E}},T.s5+D.s5*.5);
tl.fromTo("#i5",{{x:0}},{{x:-620,duration:D.s5*.5-.3,ease:"sine.inOut"}},T.s5+D.s5*.5+.3);
tl.fromTo("#k5a",{{opacity:0,x:-40}},{{opacity:1,x:0,duration:.4,ease:E}},T.s5+1.4);
tl.fromTo("#k5b",{{opacity:0,x:-40}},{{opacity:1,x:0,duration:.4,ease:E}},T.s5+1.7);
/* S6 0 % */
tl.fromTo("#z6",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.8)"}},T.s6+.05);
tl.fromTo("#zl6",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},T.s6+.4);
tl.fromTo("#zs6",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},T.s6+D.s6*.5);
tl.fromTo("#zf6",{{opacity:0}},{{opacity:1,duration:.4}},T.s6+D.s6*.5+.3);
/* S7 */
tl.fromTo("#logo7",{{opacity:0,y:-30}},{{opacity:1,y:0,duration:.5,ease:E}},T.s7+.05);
tl.fromTo("#o7",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.4,ease:E}},T.s7+.2);
tl.fromTo("#b7",{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.7)"}},T.s7+.35);
tl.fromTo("#n7",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.45,ease:E}},T.nocard);
tl.fromTo("#bio7",{{opacity:0,y:40,scale:.9}},{{opacity:1,y:0,scale:1,duration:.5,ease:"back.out(2)"}},T.bio);
tl.to("#bio7",{{scale:1.06,duration:.45,yoyo:true,repeat:5,ease:"sine.inOut"}},T.bio+.6);
window.__timelines["main"] = tl;
</script>
</body>
</html>
"""
open("index.html", "w").write(html)
print("ok", T, D)
