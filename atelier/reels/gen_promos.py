"""Reels PROMO 18h00 (voix ElevenLabs Claire) : réutilise gen_conseils.py et ajoute des scènes produit.
Usage : python3 reels/gen_promos.py <clé> <voix.wav>      (textes/scènes : reels/promos_specs.py)
Nouvelles scènes : shot (capture démo + panoramique), phone (téléphone dessiné « Illustration »), myth (idée reçue),
et extras "button" (bouton cliqué) et "audio" (lecteur de guidance vocale). Sortie : build/<slug>/
"""
import pathlib, shutil, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import gen_conseils as gc

PCSS = """
.pframe{position:absolute;background:#fff;border-radius:28px;overflow:hidden;border:2px solid #E2E8F0;box-shadow:0 24px 60px rgba(15,23,42,.12)}
.ptag{display:inline-block;padding:14px 34px;border-radius:999px;background:#E0E7FF;color:#1E3A8A;font-weight:800;font-size:36px;letter-spacing:.08em}
.btncard{width:920px;background:#fff;border:2px solid #E2E8F0;border-radius:32px;padding:48px;box-shadow:0 18px 50px rgba(15,23,42,.08);position:relative}
.btncard .lab{font-weight:800;font-size:32px;letter-spacing:.1em;color:#64748B;margin-bottom:34px;text-align:left}
.bigbtn{display:inline-block;background:#2563EB;color:#fff;font-weight:800;font-size:50px;padding:34px 54px;border-radius:24px}
.cursor{position:absolute;width:70px;height:70px;border-radius:50%;background:rgba(15,23,42,.18);border:4px solid #0F172A}
.sent{margin-top:34px;font-weight:700;font-size:44px;color:#16A34A}
.audio{width:920px;background:#fff;border:2px solid #E2E8F0;border-radius:32px;padding:44px 48px;text-align:left;box-shadow:0 18px 50px rgba(15,23,42,.08)}
.audio .lab{font-weight:800;font-size:30px;letter-spacing:.1em;color:#2563EB}
.audio .tt{font-weight:700;font-size:50px;color:#0F172A;margin:18px 0 30px;line-height:1.2}
.player{display:flex;align-items:center;gap:30px}
.play{flex:none;width:110px;height:110px;border-radius:50%;background:#2563EB;color:#fff;display:flex;align-items:center;justify-content:center;font-size:50px}
.wave{display:flex;align-items:center;gap:9px;height:110px}
.wave i{display:block;width:12px;border-radius:6px;background:#93C5FD}
.phone{width:620px;height:1060px;border-radius:70px;background:#0F172A;padding:22px;box-shadow:0 30px 80px rgba(15,23,42,.25)}
.screen{width:100%;height:100%;border-radius:52px;background:#F6F8FC;overflow:hidden;text-align:left}
.ph-top{background:#0F172A;color:#fff;padding:70px 44px 44px}
.ph-top small{display:block;font-weight:600;font-size:28px;color:#94A3B8}
.ph-top b{display:block;font-weight:800;font-size:46px;margin-top:8px}
.row{display:flex;align-items:center;gap:26px;margin:26px 34px 0;background:#fff;border:2px solid #E2E8F0;border-radius:28px;padding:30px 30px;font-weight:700;font-size:40px;color:#0F172A}
.row i{font-style:normal;flex:none;width:76px;height:76px;border-radius:22px;background:#E0E7FF;display:flex;align-items:center;justify-content:center;font-size:40px}
.illu{margin-top:26px;font-weight:600;font-size:28px;color:#94A3B8;letter-spacing:.06em}
.myth{font-weight:700;font-size:62px;line-height:1.25;color:#64748B;width:900px;position:relative}
.stamp{display:inline-block;margin-top:40px;padding:16px 50px;border:8px solid #DC2626;color:#DC2626;border-radius:20px;font-weight:800;font-size:84px;letter-spacing:.12em;transform:rotate(-6deg)}
.truth{width:920px;margin-top:56px;background:#F0FDF4;border:2px solid #BBF7D0;border-radius:32px;padding:40px 46px;text-align:left;font-weight:700;font-size:52px;line-height:1.3;color:#0F172A}
.truth b{display:block;font-weight:800;font-size:32px;letter-spacing:.1em;color:#15803D;margin-bottom:14px}
"""

IMGS = set()

def _nbsp(body):
    for a_, b_ in ((" ?", "&nbsp;?"), (" !", "&nbsp;!"), (" :", "&nbsp;:"), (" »", "&nbsp;»"), ("« ", "«&nbsp;")):
        body = body.replace(a_, b_)
    return body

def scene(i, sc, t0, t1):
    k = sc["k"]; sid = f"s{i}"; d = round(t1 - t0, 2); js = []
    def a(sel, frm, to, at, ease="E"):
        js.append(f'tl.fromTo("{sel}",{frm},{{...{to},ease:{ease}}},{round(at,2)});')
    ex = sc.get("ex")
    if k not in ("shot", "phone", "myth") and not (ex and ex[0] in ("button", "audio")):
        return ORIG(i, sc, t0, t1)
    head = ""
    if sc.get("n") and k != "myth":
        head = f'<div class="num" id="{sid}n">{sc["n"]}</div>'
        a(f"#{sid}n", "{opacity:0,scale:.4}", "{opacity:1,scale:1,duration:.45}", t0 + .05, '"back.out(2)"')
    elif sc.get("tag"):
        head = f'<div class="ptag" id="{sid}n">{sc["tag"]}</div>'
        a(f"#{sid}n", "{opacity:0,y:-30}", "{opacity:1,y:0,duration:.4}", t0 + .05)
    title = f'<div class="stitle" id="{sid}t" style="margin-top:30px;font-size:{sc.get("size",76)}px">{sc.get("title","")}</div>' if sc.get("title") else ""
    if title: a(f"#{sid}t", "{opacity:0,y:40}", "{opacity:1,y:0,duration:.45}", t0 + .18)
    extra = ""
    if k == "shot":
        IMGS.add(sc["img"])
        x0, y0, x1, y1 = sc["box"]; bw, bh = x1 - x0, y1 - y0
        s = min(960 / bw, 980 / bh, 2.8)
        fw, fh = round(bw * s), round(bh * s)
        top = sc.get("ftop", round(600 + max(0, (1100 - fh - 56) / 2)) if not head else round(700 + max(0, (1000 - fh - 56) / 2)))
        left = (1080 - fw) // 2
        iw = round(sc["W"] * s)
        extra = (f'<div class="pframe" id="{sid}f" style="left:{left}px;top:{top}px;width:{fw}px"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="demo">Compte de démonstration</span></div>'
                 f'<div class="vp" style="height:{fh}px"><img class="shot" id="{sid}i" src="assets/{sc["img"]}" alt="" style="width:{iw}px;transform:translate({-round(x0*s)}px,{-round(y0*s)}px)" /></div></div>')
        a(f"#{sid}f", "{opacity:0,y:140,scale:.94}", "{opacity:1,y:0,scale:1,duration:.6}", t0 + .3)
        if sc.get("to"):
            tx, ty = sc["to"][:2]
            js.append(f'tl.fromTo("#{sid}i",{{x:{-round(x0*s)},y:{-round(y0*s)}}},{{x:{-round(tx*s)},y:{-round(ty*s)},duration:{max(1.0, round(d-1.6,2))},ease:"sine.inOut"}},{round(t0+1.1,2)});')
            extra = extra.replace(f'transform:translate({-round(x0*s)}px,{-round(y0*s)}px)', "")
        else:
            js.append(f'tl.fromTo("#{sid}f",{{scale:1}},{{scale:1.04,duration:{max(1.0, round(d-1.0,2))},ease:"sine.inOut"}},{round(t0+.9,2)});')
            extra = extra.replace(f'transform:translate({-round(x0*s)}px,{-round(y0*s)}px)', f'left:{-round(x0*s)}px;top:{-round(y0*s)}px')
        body = f'<div class="center" style="top:{sc.get("top",300)}px">{head}{title}</div>{extra}'
    elif k == "phone":
        rows = "".join(f'<div class="row" id="{sid}r{j}"><i>{ic}</i>{tx}</div>' for j, (ic, tx) in enumerate(sc["items"]))
        extra = (f'<div class="phone" id="{sid}p"><div class="screen"><div class="ph-top"><small>Espace client</small><b>Bonjour Julie</b></div>{rows}</div></div>'
                 f'<div class="illu" id="{sid}il">Illustration</div>')
        a(f"#{sid}p", "{opacity:0,y:200}", "{opacity:1,y:0,duration:.7}", t0 + .3)
        a(f"#{sid}il", "{opacity:0}", "{opacity:1,duration:.4}", t0 + .8)
        step = max(.45, (d - 1.6) / len(sc["items"]))
        for j in range(len(sc["items"])):
            a(f"#{sid}r{j}", "{opacity:0,x:-60}", "{opacity:1,x:0,duration:.4}", t0 + 1.0 + j * step, '"back.out(1.6)"')
        body = f'<div class="center" style="top:200px">{title}</div><div class="center" style="top:500px">{extra}</div>'
    elif k == "myth":
        head = f'<div class="num" id="{sid}n">{sc["n"]}</div>'
        a(f"#{sid}n", "{opacity:0,scale:.4}", "{opacity:1,scale:1,duration:.45}", t0 + .05, '"back.out(2)"')
        ts = t0 + d * sc.get("f", .3)
        body = (f'<div class="center" style="top:420px">{head}<div class="ptag" style="margin-top:34px" id="{sid}g">IDÉE REÇUE</div>'
                f'<div class="myth" id="{sid}m" style="margin-top:40px">{sc["myth"]}</div><div class="stamp" id="{sid}x">FAUX</div>'
                f'<div class="truth" id="{sid}v"><b>✓ EN RÉALITÉ</b>{sc["truth"]}</div></div>')
        a(f"#{sid}g", "{opacity:0,y:-20}", "{opacity:1,y:0,duration:.35}", t0 + .15)
        a(f"#{sid}m", "{opacity:0,y:40}", "{opacity:1,y:0,duration:.45}", t0 + .3)
        a(f"#{sid}x", "{opacity:0,scale:2.2}", "{opacity:1,scale:1,duration:.35}", ts, '"back.out(2)"')
        a(f"#{sid}v", "{opacity:0,y:60}", "{opacity:1,y:0,duration:.5}", ts + .35)
    else:  # extras button / audio sur scène claire
        at = t0 + sc.get("ext", 1.2)
        if ex[0] == "button":
            extra = (f'<div class="btncard" id="{sid}c"><div class="lab">{ex[1]}</div><div class="bigbtn" id="{sid}b">{ex[2]}</div>'
                     f'<div class="cursor" id="{sid}u" style="left:640px;top:250px"></div><div class="sent" id="{sid}ok">✓ Rappel envoyé</div></div>')
            a(f"#{sid}c", "{opacity:0,y:80}", "{opacity:1,y:0,duration:.5}", at)
            a(f"#{sid}u", "{opacity:0,x:200,y:160}", "{opacity:1,x:0,y:0,duration:.8}", at + .7)
            js.append(f'tl.to("#{sid}b",{{scale:.94,duration:.12,yoyo:true,repeat:1}},{round(at+1.6,2)});')
            a(f"#{sid}ok", "{opacity:0,y:20}", "{opacity:1,y:0,duration:.4}", min(at + 2.0, t1 - .8))
        else:
            bars = "".join(f'<i id="{sid}w{j}" style="height:{h}px"></i>' for j, h in enumerate([30,60,90,50,100,70,40,85,55,95,35,75,60,45,80,30,65,50,90,40,70,55]))
            extra = (f'<div class="audio" id="{sid}c"><div class="lab">{ex[1]}</div><div class="tt">{ex[2]}</div>'
                     f'<div class="player"><div class="play">▶</div><div class="wave">{bars}</div></div></div>')
            a(f"#{sid}c", "{opacity:0,y:80}", "{opacity:1,y:0,duration:.5}", at)
            js.append(f'tl.to("#{sid}c .wave i",{{background:"#2563EB",stagger:.08,duration:.1}},{round(at+.7,2)});')
        body = f'<div class="center" style="top:{sc.get("top",300)}px">{head}{title}</div><div class="center" style="top:{sc.get("extop",800)}px">{extra}</div>'
    cls = "light"
    html = f'<div id="{sid}" class="clip {cls}" data-start="{round(t0,2)}" data-duration="{d}" data-track-index="1">{_nbsp(body)}</div>'
    return html, "\n".join(js)

ORIG = gc.scene
gc.scene = scene

def build(key, voix):
    from promos_specs import SPECS
    spec = SPECS[key]
    IMGS.clear()
    gc.build(spec, voix)
    d = gc.BASE / "build" / spec["slug"]
    for im in IMGS:
        shutil.copy(gc.SRC / "assets" / im, d / "assets" / im)
    h = (d / "index.html").read_text().replace("</style>", PCSS + "</style>", 1)
    (d / "index.html").write_text(h)
    return spec

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
