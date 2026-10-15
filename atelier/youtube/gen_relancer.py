"""Vidéo YouTube 1920x1080 : « Relancer une cliente sans paraître insistante » (conseil).
Usage : python3 gen_relancer.py <voix.wav> [social]  -> build/yt-relancer/ (ou build/yt-relancer-social/ : fin « Lien en bio » pour Instagram/TikTok)
Temps calés sur voix/2026-10-11_yt-relancer-cliente.mp3 (117,1 s) avec silencedetect.
Scènes : téléphone à notifications, citation en grand, frise, avant/après en écran partagé,
liste à cocher, bulles de conversation, illustration du bouton de rappel, capture avis, récap, fin.
"""
import pathlib, shutil, sys

HERE = pathlib.Path(__file__).parent
base = (HERE / "gen_presentation.py").read_text().split("T = dict(")[0]
ns = {"__file__": str(HERE / "gen_presentation.py")}
exec(base, ns)
CSS, frame, ATELIER, KIT = ns["CSS"], ns["frame"], ns["ATELIER"], ns["KIT"]
DUR = 118.6
T = dict(b=14.0, c=21.2, c2=37.2, d=54.3, e=70.6, f=85.2, g=102.6, h=111.3)

EXTRA = """
.phone{position:absolute;width:430px;height:840px;border-radius:56px;background:#F8FAFC;border:10px solid #334155;box-shadow:0 30px 80px rgba(0,0,0,.35);overflow:hidden}
.notch{position:absolute;left:50%;top:14px;width:120px;height:28px;margin-left:-60px;border-radius:999px;background:#1E293B}
.clock{position:absolute;left:0;right:0;top:70px;text-align:center;font-weight:800;font-size:78px;color:#0F172A;letter-spacing:-.02em}
.date{position:absolute;left:0;right:0;top:170px;text-align:center;font-weight:600;font-size:22px;color:#64748B}
.notif{position:absolute;left:18px;right:18px;padding:18px 20px;border-radius:22px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 8px 24px rgba(15,23,42,.08)}
.notif .t{font-weight:700;font-size:19px;color:#64748B;display:flex;align-items:center;gap:10px}
.notif .t i{font-style:normal;width:30px;height:30px;border-radius:9px;display:inline-flex;align-items:center;justify-content:center;font-size:17px;color:#fff}
.notif .m{font-weight:700;font-size:23px;color:#0F172A;margin-top:8px;line-height:1.3}
.hk{position:absolute;left:130px;top:300px;width:1060px}
.hk .big{width:1060px;text-align:left;font-size:78px}
.ask{margin-top:44px;display:inline-flex;gap:20px;align-items:center;font-weight:800;font-size:46px;color:#E9C46A}
.titleA{position:absolute;left:0;right:0;top:250px;text-align:center;color:#fff}
.chips3{position:absolute;left:0;right:0;top:700px;display:flex;justify-content:center;gap:30px}
.c5{padding:22px 40px;border-radius:999px;background:#1E293B;border:2px solid #334155;color:#E2E8F0;font-weight:700;font-size:38px;display:flex;align-items:center;gap:16px}
.c5 b{display:inline-flex;width:48px;height:48px;border-radius:50%;background:#2563EB;color:#fff;align-items:center;justify-content:center;font-size:26px}
.quote{position:absolute;left:0;right:0;top:250px;text-align:center}
.quote .q{font-weight:800;font-size:104px;line-height:1.1;letter-spacing:-.03em;color:#0F172A}
.quote .q span{color:#2563EB}
.quote .qm{font-weight:800;font-size:200px;line-height:.6;color:#E9C46A;height:90px}
.quote .s{font-weight:600;font-size:44px;color:#475569;margin-top:56px}
.quote .s2{display:inline-block;margin-top:36px;padding:18px 40px;border-radius:999px;background:#0F172A;color:#fff;font-weight:700;font-size:38px}
.secth{position:absolute;left:110px;top:110px}
.secth .h{font-size:64px}
.tl{position:absolute;left:150px;right:150px;top:540px;height:8px;border-radius:4px;background:#E2E8F0}
.tlf{position:absolute;left:0;top:0;height:8px;border-radius:4px;background:#2563EB;width:100%;transform-origin:left center}
.mk{position:absolute;top:470px;width:400px;margin-left:-200px;text-align:center}
.mk .dt{width:48px;height:48px;border-radius:50%;margin:46px auto 0;background:#fff;border:8px solid #2563EB}
.mk .dt.gold{border-color:#E9C46A}.mk .dt.navy{border-color:#0F172A;background:#0F172A}
.mk .lb{font-weight:800;font-size:46px;margin-top:30px;color:#0F172A}
.mk .sb{font-weight:600;font-size:32px;color:#64748B;margin-top:10px;line-height:1.35}
.mk .day{position:absolute;left:0;right:0;top:0;font-weight:800;font-size:30px;color:#2563EB;letter-spacing:.06em}
.tone{position:absolute;left:0;right:0;top:820px;text-align:center}
.tone div{display:inline-block;padding:20px 44px;border-radius:999px;background:#FBF3DC;color:#6B4E16;font-weight:800;font-size:38px}
.half{position:absolute;top:0;bottom:0;width:960px}
.half.l{left:0;background:#FEF2F2}.half.r{left:960px;background:#F0FDF4}
.hlab{position:absolute;left:0;right:0;top:120px;text-align:center;font-weight:800;font-size:42px}
.half.l .hlab{color:#B91C1C}.half.r .hlab{color:#15803D}
.msgcard{position:absolute;left:110px;width:740px;top:230px;padding:40px 44px;border-radius:30px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 20px 60px rgba(15,23,42,.10)}
.msgcard .who{font-weight:700;font-size:24px;color:#64748B;margin-bottom:18px}
.msgcard .txt{font-weight:600;font-size:33px;line-height:1.45;color:#0F172A}
.msgcard .txt u{text-decoration:none;color:#2563EB;font-weight:800}
.bad .txt{color:#991B1B;font-weight:800}
.strike{position:absolute;left:90px;width:780px;top:420px;height:10px;border-radius:5px;background:#DC2626;transform-origin:left center;transform:rotate(-8deg)}
.flags{position:absolute;left:0;right:0;top:820px;display:flex;justify-content:center;gap:18px}
.flag{padding:14px 28px;border-radius:999px;background:#fff;border:3px solid #FCA5A5;color:#B91C1C;font-weight:800;font-size:30px}
.okl{position:absolute;left:0;right:0;top:820px;display:flex;justify-content:center;gap:18px}
.okl div{padding:14px 28px;border-radius:999px;background:#fff;border:3px solid #86EFAC;color:#15803D;font-weight:800;font-size:30px}
.x{display:flex;align-items:center;gap:22px;margin:22px 0;font-weight:700;font-size:40px;color:#0F172A}
.x i{font-style:normal;flex:none;width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:30px;background:#DCFCE7;color:#16A34A}
.x.no{color:#64748B}.x.no i{background:#FEE2E2;color:#DC2626}
.x.no s{text-decoration-thickness:3px}
.mail{position:absolute;left:1080px;top:250px;width:720px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.mail .mh{padding:26px 34px;background:#0F172A;color:#fff;font-weight:700;font-size:26px}
.mail .mb{padding:34px}
.mail .mt{font-weight:800;font-size:36px}
.mail .mp{font-weight:500;font-size:27px;color:#475569;margin-top:14px;line-height:1.4}
.stars{margin-top:24px;font-size:58px;letter-spacing:10px;color:#CBD5E1}
.mail .free{margin-top:20px;display:inline-block;padding:12px 26px;border-radius:999px;background:#EFF6FF;color:#2563EB;font-weight:800;font-size:26px}
.cal{position:absolute;left:1080px;top:800px;display:flex;gap:14px}
.cal div{width:96px;height:96px;border-radius:18px;background:#fff;border:2px solid #E2E8F0;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:800;font-size:30px;color:#94A3B8}
.cal div small{font-size:18px;font-weight:700}
.cal .on{background:#2563EB;border-color:#2563EB;color:#fff}
.cal .on2{background:#EFF6FF;border-color:#2563EB;color:#2563EB}
.chat{position:absolute;left:820px;top:170px;width:990px;height:740px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12);overflow:hidden}
.chat .ch{height:96px;border-bottom:2px solid #E2E8F0;display:flex;align-items:center;gap:20px;padding:0 34px}
.av{width:60px;height:60px;border-radius:50%;background:#E2E8F0;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:24px;color:#0F172A}
.chat .nm{font-weight:800;font-size:30px}.chat .st{font-weight:600;font-size:22px;color:#64748B}
.illus{position:absolute;right:30px;top:30px;font-size:18px;font-weight:600;color:#64748B;background:#F1F5F9;border-radius:999px;padding:4px 14px}
.bub{position:absolute;max-width:640px;padding:22px 28px;border-radius:28px;font-weight:600;font-size:29px;line-height:1.4}
.bub.in{left:34px;background:#F1F5F9;color:#0F172A;border-bottom-left-radius:8px}
.bub.out{right:34px;background:#2563EB;color:#fff;border-bottom-right-radius:8px}
.when{position:absolute;left:0;right:0;text-align:center;font-weight:700;font-size:22px;color:#94A3B8}
.col2{position:absolute;left:110px;top:0;bottom:0;width:660px;display:flex;flex-direction:column;justify-content:center}
.nos{margin-top:40px}
.panel{position:absolute;left:880px;top:150px;width:900px;padding:40px 46px;border-radius:28px;background:#fff;border:2px solid #E2E8F0;box-shadow:0 30px 80px rgba(15,23,42,.12)}
.panel h4{font-weight:800;font-size:38px}.panel .sm{font-weight:600;font-size:25px;color:#64748B;margin-top:8px}
.paybox{margin-top:28px;padding:28px 30px;border-radius:20px;background:#FBF3DC;border:2px solid #F1DFA6}
.paybox .pt{font-weight:800;font-size:30px;color:#6B4E16}
.btns{display:flex;gap:16px;margin-top:20px}
.btn{flex:1;padding:18px;border-radius:14px;text-align:center;font-weight:700;font-size:25px;background:#fff;border:2px solid #E2E8F0;color:#0F172A}
.btn.rm{margin-top:16px;display:flex;align-items:center;justify-content:center;gap:12px;border-color:#2563EB;color:#2563EB;font-size:28px;padding:22px}
.hint{margin-top:12px;font-weight:600;font-size:22px;color:#64748B;text-align:center}
.cursor{position:absolute;width:44px;height:44px;z-index:30}
.toast{position:absolute;left:880px;top:800px;width:900px;padding:24px 30px;border-radius:18px;background:#0F172A;color:#fff;font-weight:700;font-size:28px;display:flex;align-items:center;gap:16px}
.toast i{font-style:normal;width:40px;height:40px;border-radius:50%;background:#16A34A;display:flex;align-items:center;justify-content:center;font-size:22px}
.rule{position:absolute;left:880px;top:920px;width:900px;text-align:center;font-weight:800;font-size:30px;color:#6B4E16}
.flow{position:absolute;left:820px;top:640px;width:1000px;display:flex;align-items:center;justify-content:space-between}
.flow div{padding:18px 26px;border-radius:16px;background:#fff;border:2px solid #E2E8F0;font-weight:700;font-size:28px;color:#0F172A}
.flow b{font-size:36px;color:#2563EB}
.ask2{position:absolute;left:0;right:0;top:740px;text-align:center;font-weight:800;font-size:40px;color:#2563EB}
.rec{display:flex;align-items:center;gap:22px;font-weight:700;font-size:48px;color:#fff;margin:22px 0}
.rec i{font-style:normal;flex:none;width:66px;height:66px;border-radius:50%;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:32px}
"""

def phone(id_, inner, left, top):
    return f'<div class="phone" id="{id_}" style="left:{left}px;top:{top}px"><div class="notch"></div>{inner}</div>'

def notif(id_, top, color, icon, app, msg):
    return (f'<div class="notif" id="{id_}" style="top:{top}px"><div class="t"><i style="background:{color}">{icon}</i>{app}</div>'
            f'<div class="m">{msg}</div></div>')

hook_phone = phone("ph", '<div class="clock">09:41</div><div class="date">Lundi</div>'
    + notif("n1", 250, "#D97706", "€", "Paiements", "Séance du 12/10 : toujours en attente")
    + notif("n2", 410, "#7C3AED", "★", "Avis", "Aucun avis reçu depuis 2 mois")
    + notif("n3", 570, "#2563EB", "✉", "Messages", "Sophie : pas de nouvelles depuis 3 mois") + '<div class="ask2" id="n4">Relancer ?</div>', 1330, 120)

chaps = ["Quand", "Combien de fois", "Quoi écrire"]
c3 = "".join(f'<div class="c5" id="q{i}"><b>{i+1}</b>{t}</div>' for i, t in enumerate(chaps))

def chap(id_, num, txt, title, color="#2563EB"):
    return (f'<div class="secth"><div class="chap" id="{id_}c"><b>{num}</b>{txt}</div>'
            f'<div class="h" id="{id_}h">{title}</div></div>')

LOGO = '<img class="logo-corner" src="assets/logo_couleur.png" alt="GuidPilot" />'

body = f'''
<div id="a" class="clip navy" data-start="0" data-duration="{T['b']}" data-track-index="1">
  <div class="hk" id="a1"><div class="big">Une cliente à relancer… <span>sans paraître insistante ?</span></div>
    <div class="ask" id="a1b">Relancer… ou laisser filer ?</div></div>
  {hook_phone}
  <div id="a2" style="position:absolute;inset:0">
    <div class="titleA"><div style="font-weight:700;font-size:30px;letter-spacing:.16em;color:#E9C46A">CONSEILS DE PRATICIENNE</div>
      <div class="big" style="width:auto;margin-top:26px;font-size:80px">Relancer une cliente<br/><span>avec tact</span></div></div>
    <div class="chips3">{c3}</div>
  </div>
</div>
<div id="b" class="clip light" data-start="{T['b']}" data-duration="{round(T['c']-T['b'],2)}" data-track-index="1">
  {LOGO}
  <div class="quote"><div class="qm" id="bq0">“</div>
    <div class="q" id="bq">Relancer, ce n'est pas <span>insister.</span></div>
    <div class="s" id="bs">Le plus souvent, votre cliente a simplement oublié.</div>
    <div class="s2" id="bs2">Un message clair lui rend service</div></div>
</div>
<div id="c" class="clip light" data-start="{T['c']}" data-duration="{round(T['c2']-T['c'],2)}" data-track-index="1">
  {LOGO}
  {chap("c", 1, "Premier cas", "Le paiement <span>en attente</span>")}
  <div class="tl" id="tl"><div class="tlf" id="tlf"></div></div>
  <div class="mk" id="k1" style="left:300px"><div class="day">JOUR J</div><div class="dt navy"></div><div class="lb">Date prévue</div><div class="sb">Le règlement n'est pas arrivé</div></div>
  <div class="mk" id="k2" style="left:740px"><div class="day">J + 1 ou 2</div><div class="dt"></div><div class="lb">1er rappel</div><div class="sb">Court et aimable</div></div>
  <div class="mk" id="k3" style="left:1180px"><div class="day">J + 7</div><div class="dt"></div><div class="lb">2e relance</div><div class="sb">Si rien ne bouge</div></div>
  <div class="mk" id="k4" style="left:1620px"><div class="day">ENSUITE</div><div class="dt gold"></div><div class="lb">Échange direct</div><div class="sb">Plutôt qu'un 3e message</div></div>
  <div class="tone" id="ct"><div>Un ton neutre et factuel</div></div>
</div>
<div id="c2" class="clip light" data-start="{T['c2']}" data-duration="{round(T['d']-T['c2'],2)}" data-track-index="1">
  <div class="half l" id="hl"><div class="hlab">✕ À éviter</div>
    <div class="msgcard bad"><div class="who">Message trop insistant</div>
      <div class="txt">URGENT !!! Vous ne m'avez TOUJOURS pas payée. Je ne comprends pas…</div></div>
    <div class="strike" id="stk"></div>
    <div class="flags"><div class="flag" id="f1">MAJUSCULES</div><div class="flag" id="f2">« !!! »</div><div class="flag" id="f3">Reproches</div></div>
  </div>
  <div class="half r" id="hr"><div class="hlab">✓ Bien tourné</div>
    <div class="msgcard" style="top:210px"><div class="who">Exemple de message</div>
      <div class="txt"><span id="w1">Bonjour Julie, petit rappel :</span> <span id="w2">le règlement de votre séance du 12 octobre est encore en attente.</span>
      <span id="w3"><u>Voici le lien pour régler.</u></span> <span id="w4">Si c'est déjà fait, ne tenez pas compte de ce message.</span></div></div>
    <div class="okl" id="okl"><div>Court</div><div>Factuel</div><div>Le lien direct</div></div>
  </div>
</div>
<div id="d" class="clip light" data-start="{T['d']}" data-duration="{round(T['e']-T['d'],2)}" data-track-index="1">
  {LOGO}
  <div class="col2"><div class="chap" id="dc"><b>2</b>Deuxième cas</div><div class="h" id="dh">Demander <span>un avis</span></div>
    <div class="nos">
      <div class="x" id="x1"><i>✓</i>2 ou 3 jours après la séance</div>
      <div class="x" id="x2"><i>✓</i>Une seule relance</div>
      <div class="x no" id="x3"><i>✕</i><s>Un cadeau contre un avis</s></div>
      <div class="x no" id="x4"><i>✕</i><s>Demander une note précise</s></div>
    </div></div>
  <div class="mail" id="dm"><div class="mh">✉ Nouveau message</div><div class="mb">
    <div class="mt">Votre avis compte</div>
    <div class="mp">Merci pour notre séance. Si vous le souhaitez, vous pouvez partager votre ressenti en quelques mots.</div>
    <div class="stars" id="st">★★★★★</div><div class="free" id="fr">Un avis doit rester libre</div></div></div>
  <div class="cal" id="cal"><div><small>LUN</small>12</div><div class="on2"><small>MAR</small>13</div><div class="on" id="c14"><small>MER</small>14</div><div><small>JEU</small>15</div><div><small>VEN</small>16</div></div>
</div>
<div id="e" class="clip light" data-start="{T['e']}" data-duration="{round(T['f']-T['e'],2)}" data-track-index="1">
  {LOGO}
  <div class="col2" style="width:640px"><div class="chap" id="ec"><b>3</b>Troisième cas</div><div class="h" id="eh">Proposer <span>une nouvelle séance</span></div>
    <div class="p" id="ep">Respectez son rythme. Rappelez un élément de votre dernier échange, puis laissez la porte ouverte.</div>
    <div class="nos" id="eno">
      <div class="x no" id="y1"><i>✕</i><s>Les relances en rafale</s></div>
      <div class="x no" id="y2"><i>✕</i><s>La culpabilité</s></div></div></div>
  <div class="chat" id="ech"><div class="ch"><div class="av">SL</div><div><div class="nm">Sophie L.</div><div class="st">Dernière séance il y a 2 mois</div></div></div>
    <span class="illus">Illustration</span>
    <div class="when" style="top:130px">Il y a 2 mois</div>
    <div class="bub in" style="top:180px">Merci beaucoup, j'y vois plus clair pour mon projet de déménagement.</div>
    <div class="when" id="e0" style="top:330px">Aujourd'hui</div>
    <div class="bub out" id="e1" style="top:380px">Bonjour Sophie, j'espère que votre projet de déménagement avance bien.</div>
    <div class="bub out" id="e2" style="top:530px">Si vous souhaitez faire le point, mes disponibilités sont sur ma page.</div>
  </div>
</div>
<div id="f" class="clip light" data-start="{T['f']}" data-duration="{round(T['g']-T['f'],2)}" data-track-index="1">
  {LOGO}
  <div class="col2" style="width:700px"><div class="chap" id="fc"><b>✓</b>Avec GuidPilot</div><div class="h" id="fh">Le rappel de paiement <span>en un clic</span></div>
    <div class="p" id="fp">Votre cliente reçoit un e-mail avec le lien pour régler.</div>
    <div class="tag" id="ft">Un rappel par jour au maximum</div></div>
  <div class="panel" id="fpan"><span class="illus">Illustration</span><h4>Tirage de tarot · Visio</h4><div class="sm">Lundi 12 octobre · 14:00 · Sophie L.</div>
    <div class="paybox"><div class="pt">Paiement en attente</div>
      <div class="btns"><div class="btn">Voir la facture</div><div class="btn">Marquer comme payée</div></div>
      <div class="btn rm" id="rmb">🔔 Envoyer un rappel de paiement</div>
      <div class="hint" id="hint">Aucun rappel envoyé pour l'instant.</div></div></div>
  <svg class="cursor" id="cur" viewBox="0 0 24 24" style="left:1500px;top:900px"><path d="M3 2l7 19 2.5-7.5L20 11z" fill="#0F172A" stroke="#fff" stroke-width="1.5"/></svg>
  <div class="toast" id="fto"><i>✓</i>Rappel envoyé à sophie.l@exemple.fr</div>
  <div id="fav" style="position:absolute;inset:0">
    <div class="col2" style="width:640px"><div class="chap"><b>✓</b>Avec GuidPilot</div><div class="h">Demandes d'avis <span>et relances</span></div>
      <div class="p">Depuis votre espace, en quelques secondes.</div></div>
    <div class="flow" id="flw"><div>Séance réalisée</div><b>→</b><div>Demande d'avis</div><b>→</b><div>Relance si besoin</div></div>
    {frame("fa", "avis.png", 1000, 260, 300)}
    <div class="tag" id="fat" style="position:absolute;left:820px;top:800px">Les avis s'affichent ensuite sur votre page</div>
  </div>
</div>
<div id="g" class="clip navy" data-start="{T['g']}" data-duration="{round(T['h']-T['g'],2)}" data-track-index="1">
  <div style="position:absolute;left:0;right:0;top:120px;text-align:center"><div class="big" style="width:auto;font-size:76px" id="gh">Récapitulons</div></div>
  <div style="position:absolute;left:500px;top:320px">
    <div class="rec" id="r_1"><i>1</i>Un message court</div>
    <div class="rec" id="r_2"><i>2</i>Un ton neutre</div>
    <div class="rec" id="r_3"><i>3</i>Deux relances au maximum</div>
    <div class="rec" id="r_4"><i>4</i>Jamais de contrepartie pour un avis</div>
  </div>
</div>
<div id="h" class="clip navy" data-start="{T['h']}" data-duration="{round(DUR-T['h'],2)}" data-track-index="1">
  <div class="center" id="g6" style="top:150px"><img src="assets/logo_blanc.png" alt="GuidPilot" style="width:380px;display:block" />
    <div class="offer" style="margin-top:46px">Essai gratuit</div>
    <div class="big14">14 jours gratuits</div>
    <div class="nocard" id="g7">✓ Sans carte bancaire</div>
    <div class="url" id="g8">guidpilot.fr</div>
    <div class="sub" id="g9"><i></i>Abonnez-vous : 2 vidéos par semaine</div>
  </div>
</div>'''

E = "power3.out"
def pop(sel, t, ease="back.out(1.6)", y=30):
    return f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:.45,ease:"{ease}"}},{t});\n'
def fin(sel, t):
    return f'tl.fromTo("{sel}",{{opacity:0,x:120,scale:.95}},{{opacity:1,x:0,scale:1,duration:.7,ease:"{E}"}},{t});\n'
def head(i, t):
    return pop(f"#{i}c", t + .1, E) + pop(f"#{i}h", t + .25, E, 40)
def hl(sel, t):
    return f'tl.fromTo("{sel}",{{backgroundColor:"rgba(37,99,235,0)"}},{{backgroundColor:"rgba(37,99,235,.12)",duration:.4}},{t});\n'

# A : accroche (0 -> 14)
js = pop("#a1", 0.4, E, 50) + fin("#ph", 0.8)
js += pop("#n1", 1.0, y=-40) + pop("#n2", 2.9, y=-40) + pop("#n3", 4.5, y=-40)
js += pop("#a1b", 8.2) + pop("#n4", 6.6)
js += 'tl.to(["#a1","#ph"],{opacity:0,y:-30,duration:.5,ease:"power2.in"},9.6);\n'
js += 'tl.fromTo("#a2",{opacity:0,scale:.92},{opacity:1,scale:1,duration:.7,ease:"back.out(1.4)"},10.0);\n'
js += pop("#q0", 10.4, y=40) + pop("#q1", 11.3, y=40) + pop("#q2", 12.3, y=40)

# B : citation (14 -> 21.2)
js += pop("#bq0", 14.2, E) + 'tl.fromTo("#bq",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},15.1);\n'
js += pop("#bs", 17.1, E) + pop("#bs2", 19.2)

# C : frise paiement (21.2 -> 37.2)
js += head("c", T['c'])
js += 'tl.fromTo("#tl",{opacity:0},{opacity:1,duration:.4},23.0);\n'
js += 'tl.fromTo("#tlf",{scaleX:0},{scaleX:.12,duration:.5},23.2);\n' + pop("#k1", 23.3)
js += 'tl.to("#tlf",{scaleX:.38,duration:.8},24.4);\n' + pop("#k2", 24.8)
js += 'tl.to("#tlf",{scaleX:.62,duration:.8},28.8);\n' + pop("#k3", 29.2)
js += 'tl.to("#tlf",{scaleX:1,duration:.8},32.0);\n' + pop("#k4", 32.4)
js += pop("#ct", 35.3) + 'tl.to("#ct div",{scale:1.06,duration:.35,yoyo:true,repeat:3,ease:"sine.inOut"},35.9);\n'

# C2 : avant / après (37.2 -> 54.3)
js += 'tl.fromTo("#hr",{opacity:0,x:-280},{opacity:1,x:-480,duration:.7,ease:"power3.out"},37.3);\n'
js += 'tl.to("#hr",{x:0,duration:.7,ease:"power3.inOut"},49.2);\n'
js += 'tl.set(["#w1","#w2","#w3","#w4"],{opacity:.12},37.3);\n'
js += "".join(f'tl.to("#w{i+1}",{{opacity:1,duration:.4}},{t});\n' for i, t in enumerate([39.3, 41.2, 45.5, 47.0]))
js += 'tl.fromTo("#hl",{opacity:0,x:-200},{opacity:1,x:0,duration:.7,ease:"power3.out"},49.4);\n'
js += pop("#okl", 47.8) + pop("#f1", 50.4) + pop("#f2", 51.9) + pop("#f3", 53.2)
js += 'tl.fromTo("#stk",{scaleX:0},{scaleX:1,duration:.5,ease:"power2.out"},51.2);\n'

# D : avis (54.3 -> 70.6)
js += head("d", T['d']) + fin("#dm", 55.0)
js += pop("#x1", 56.2) + 'tl.fromTo("#cal",{opacity:0,y:40},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},56.4);\n'
js += 'tl.fromTo("#c14",{scale:1},{scale:1.12,duration:.35,yoyo:true,repeat:3,ease:"sine.inOut"},57.4);\n'
js += pop("#x2", 61.8) + pop("#x3", 63.4) + pop("#x4", 67.2)
js += 'tl.to("#st",{color:"#E9C46A",duration:.6,stagger:.1},59.0);\n'
js += pop("#fr", 69.0)

# E : nouvelle séance (70.6 -> 85.2)
js += head("e", T['e']) + fin("#ech", 71.2)
js += pop("#ep", 73.5, E) + pop("#e0", 75.0) + pop("#e1", 75.4, y=40) + pop("#e2", 79.1, y=40)
js += pop("#y1", 82.6) + pop("#y2", 84.0)

# F : GuidPilot (85.2 -> 102.6)
js += head("f", T['f']) + fin("#fpan", 85.8)
js += 'tl.fromTo("#cur",{opacity:0,x:0,y:0},{opacity:1,x:-140,y:-385,duration:1.1,ease:"power2.inOut"},87.0);\n'
js += 'tl.to("#rmb",{scale:.95,duration:.12,yoyo:true,repeat:1},88.6);\n'
js += 'tl.to("#rmb",{backgroundColor:"#EFF6FF",duration:.3},88.7);\n'
js += 'tl.call(()=>{document.getElementById("hint").textContent="Dernier rappel envoyé le 13/10 à 09:42"},null,88.9);\n'
js += pop("#fto", 89.0, y=40) + pop("#fp", 90.6, E) + pop("#ft", 93.2)
js += 'tl.to(["#fpan","#cur","#fto","#fp","#ft","#fc","#fh"],{opacity:0,duration:.4},95.6);\n'
js += 'tl.fromTo("#fav",{opacity:0,x:80},{opacity:1,x:0,duration:.6,ease:"power3.out"},95.9);\n'
js += pop("#flw", 97.3) + pop("#fat", 100.2)

# G : récap (102.6 -> 111.3)
js += pop("#gh", 102.7, E)
js += "".join(f'tl.fromTo("#r_{i+1}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.45,ease:"back.out(1.6)"}},{t});\n'
              for i, t in enumerate([104.5, 105.4, 106.8, 108.9]))

# H : fin
js += 'tl.fromTo("#g6",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.7,ease:"back.out(1.5)"},111.4);\n'
js += pop("#g7", 112.6) + pop("#g8", 113.6) + pop("#g9", 115.0)
js += 'tl.to("#g9",{scale:1.06,duration:.45,yoyo:true,repeat:3,ease:"sine.inOut"},115.6);\n'

hidden = ["#a2", "#a1b", "#n1", "#n2", "#n3", "#bq0", "#bq", "#bs", "#bs2", "#tl", "#k1", "#k2", "#k3", "#k4", "#ct",
          "#hl", "#hr", "#f1", "#f2", "#f3", "#x1", "#x2", "#x3", "#x4", "#cal", "#fr", "#ep", "#e0", "#e1", "#e2", "#y1", "#y2",
          "#cur", "#fto", "#flw", "#okl", "#n4", "#fp", "#ft", "#fav", "#fat", "#g7", "#g8", "#g9"]
html = f'''<!doctype html><html lang="fr"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="vendor/gsap.min.js"></script><style>{CSS}{EXTRA}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1920" data-height="1080">
<div class="aibadge">Voix off générée par IA</div>
<audio id="voix" src="assets/voix.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
{body}
</div>
<script>
const tl=gsap.timeline({{paused:true}});
tl.set({hidden!r},{{opacity:0}},0);
{js}
window.__timelines["main"]=tl;
</script></body></html>'''

SOCIAL = len(sys.argv) > 2 and sys.argv[2] == "social"
if SOCIAL:
    html = html.replace('<i></i>Abonnez-vous : 2 vidéos par semaine', 'Lien en bio · Suivez-nous pour d\'autres conseils')
d = ATELIER / "build" / ("yt-relancer-social" if SOCIAL else "yt-relancer")
if d.exists(): shutil.rmtree(d)
(d / "assets").mkdir(parents=True)
for sub in ("fonts", "vendor"): shutil.copytree(KIT / sub, d / sub)
for f in ("hyperframes.json", "meta.json"): shutil.copy(KIT / f, d / f)
for a in ("avis.png", "logo_blanc.png"): shutil.copy(KIT / "assets" / a, d / "assets" / a)
shutil.copy(ATELIER / "assets" / "logo_couleur.png", d / "assets" / "logo_couleur.png")
shutil.copy(sys.argv[1], d / "assets" / "voix.wav")
(d / "index.html").write_text(html)
print("ok", d)
