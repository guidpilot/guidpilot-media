"""Reels CONSEILS (voix ElevenLabs Claire) : générateur générique à scènes.
Usage : python3 reels/gen_conseils.py <slug> <voix.wav>
Les temps de chaque scène (t) sont calés sur la voix (silencedetect). Sortie : build/<slug>/
"""
import pathlib, shutil, sys, json, subprocess, html as H
src = (pathlib.Path(__file__).parent / "gen_reels.py").read_text().split("# ---------- Reel 1")[0]
ns = {"__file__": str(pathlib.Path(__file__).parent / "gen_reels.py")}
exec(src, ns)
CSS, cta, cta_js, page, BASE, SRC = ns["CSS"], ns["cta"], ns["cta_js"], ns["page"], ns["BASE"], ns["SRC"]

EXTRA = """
.num{display:inline-flex;align-items:center;justify-content:center;width:132px;height:132px;border-radius:50%;background:#2563EB;color:#fff;font-weight:800;font-size:80px}
.tag{display:inline-block;padding:14px 34px;border-radius:999px;background:#E0E7FF;color:#1E3A8A;font-weight:800;font-size:36px;letter-spacing:.08em}
.tag.bad{background:#FEE2E2;color:#991B1B}
.card{width:920px;background:#fff;border:2px solid #E2E8F0;border-radius:32px;padding:44px 48px;text-align:left;box-shadow:0 18px 50px rgba(15,23,42,.08)}
.card .lab{font-weight:800;font-size:32px;letter-spacing:.1em;color:#64748B;margin-bottom:18px}
.card .txt{font-weight:600;font-size:54px;line-height:1.3;color:#0F172A}
.bub{max-width:820px;padding:30px 40px;border-radius:36px;font-weight:600;font-size:44px;line-height:1.3;text-align:left}
.bub.in{background:#fff;border:2px solid #E2E8F0;border-bottom-left-radius:10px;align-self:flex-start;margin-left:80px}
.bub.out{background:#2563EB;color:#fff;border-bottom-right-radius:10px;align-self:flex-end;margin-right:80px}
.bub small{display:block;font-size:28px;font-weight:600;opacity:.7;margin-top:10px}
.vs{display:flex;gap:28px;width:960px}
.vs>div{flex:1;border-radius:30px;padding:40px 34px;text-align:left}
.vs .no{background:#FEF2F2;border:2px solid #FECACA}
.vs .yes{background:#F0FDF4;border:2px solid #BBF7D0}
.vs h4{font-weight:800;font-size:42px;margin-bottom:22px}
.vs .no h4{color:#B91C1C}.vs .yes h4{color:#15803D}
.vs p{font-weight:600;font-size:46px;line-height:1.3;color:#0F172A}
.chk{display:flex;align-items:center;gap:22px;text-align:left;font-weight:700;font-size:48px;color:#0F172A;margin:16px 0;width:900px;background:#fff;border:2px solid #E2E8F0;border-radius:26px;padding:24px 30px}
.chk i{font-style:normal;flex:none;width:68px;height:68px;border-radius:50%;background:#DCFCE7;color:#16A34A;display:flex;align-items:center;justify-content:center;font-size:40px}
.chk.x i{background:#FEE2E2;color:#DC2626}
.quote{font-weight:800;font-size:92px;line-height:1.1;color:#fff;width:920px;letter-spacing:-.02em}
.quote span{color:#E9C46A}
.qm{font-weight:800;font-size:220px;line-height:.6;color:#E9C46A;height:120px}
.sub{margin-top:36px;font-weight:600;font-size:46px;color:#94A3B8;width:880px;line-height:1.3}
.brand{font-weight:700;font-size:58px;line-height:1.25;color:#fff;width:900px}
.brand span{color:#60A5FA}
"""

def esc(s):  # textes saisis avec <span> autorisé
    return s

def scene(i, sc, t0, t1):
    """Renvoie (html, js) d'une scène entre t0 et t1."""
    k = sc["k"]; sid = f"s{i}"; d = round(t1 - t0, 2)
    js = []
    def a(sel, frm, to, at, ease="E"):
        js.append(f'tl.fromTo("{sel}",{frm},{{...{to},ease:{ease}}},{round(at,2)});')
    if k == "hook":
        body = f'''<div class="center" style="top:520px"><div class="kicker" id="{sid}k" style="font-size:40px">{sc["kicker"]}</div>
<div class="big" id="{sid}t" style="margin-top:44px;font-size:{sc.get("size",96)}px">{sc["title"]}</div>
{f'<div class="sub" id="{sid}s">{sc["sub"]}</div>' if sc.get("sub") else ""}</div>'''
        a(f"#{sid}k", "{opacity:0,y:30}", "{opacity:1,y:0,duration:.4}", t0 + .05)
        a(f"#{sid}t", "{opacity:0,y:60}", "{opacity:1,y:0,duration:.6}", t0 + .2)
        if sc.get("sub"): a(f"#{sid}s", "{opacity:0,y:30}", "{opacity:1,y:0,duration:.5}", t0 + sc.get("subt", 1.2))
        cls = "navy"
    elif k == "quote":
        body = f'''<div class="center" style="top:560px"><div class="qm" id="{sid}m">“</div>
<div class="quote" id="{sid}t">{sc["title"]}</div></div>'''
        a(f"#{sid}m", "{opacity:0,scale:.5}", "{opacity:1,scale:1,duration:.5}", t0 + .05, '"back.out(2)"')
        a(f"#{sid}t", "{opacity:0,y:50}", "{opacity:1,y:0,duration:.6}", t0 + .25)
        cls = "navy"
    elif k == "brand":
        body = f'''<div class="center" style="top:560px"><img id="{sid}l" src="assets/logo_blanc.png" alt="GuidPilot" style="width:600px;display:block" />
<div class="brand" id="{sid}t" style="margin-top:70px">{sc["title"]}</div></div>'''
        a(f"#{sid}l", "{opacity:0,scale:.7}", "{opacity:1,scale:1,duration:.6}", t0 + .05, '"back.out(1.5)"')
        a(f"#{sid}t", "{opacity:0,y:50}", "{opacity:1,y:0,duration:.5}", t0 + .6)
        cls = "navy"
    else:  # scènes claires : step / bad / list / vs
        head = ""
        if k == "step":
            head = f'<div class="num" id="{sid}n">{sc["n"]}</div>'
            a(f"#{sid}n", "{opacity:0,scale:.4}", "{opacity:1,scale:1,duration:.45}", t0 + .05, '"back.out(2)"')
        elif k == "bad":
            head = f'<div class="tag bad" id="{sid}n">✕ ERREUR À ÉVITER</div>'
            a(f"#{sid}n", "{opacity:0,y:-30}", "{opacity:1,y:0,duration:.4}", t0 + .05)
        elif sc.get("tag"):
            head = f'<div class="tag" id="{sid}n">{sc["tag"]}</div>'
            a(f"#{sid}n", "{opacity:0,y:-30}", "{opacity:1,y:0,duration:.4}", t0 + .05)
        title = f'<div class="stitle" id="{sid}t" style="margin-top:30px;font-size:{sc.get("size",76)}px">{sc["title"]}</div>'
        a(f"#{sid}t", "{opacity:0,y:40}", "{opacity:1,y:0,duration:.45}", t0 + .18)
        extra = ""; ex = sc.get("ex")
        at = t0 + sc.get("ext", 1.3)
        if ex:
            typ = ex[0]
            if typ == "card":
                extra = f'<div class="card" id="{sid}c"><div class="lab">{ex[1]}</div><div class="txt">{ex[2]}</div></div>'
                a(f"#{sid}c", "{opacity:0,y:80,scale:.95}", "{opacity:1,y:0,scale:1,duration:.55}", at)
            elif typ == "chat":
                parts = []
                for j, (side, txt) in enumerate(ex[1]):
                    parts.append(f'<div class="bub {side}" id="{sid}b{j}">{txt}</div>')
                    a(f"#{sid}b{j}", "{opacity:0,y:40,scale:.9}", "{opacity:1,y:0,scale:1,duration:.4}", at + j * ex[2], '"back.out(1.6)"')
                extra = '<div style="display:flex;flex-direction:column;gap:26px;width:1080px">' + "".join(parts) + "</div>"
            elif typ == "vs":
                extra = f'''<div class="vs"><div class="no" id="{sid}v1"><h4>✕ À éviter</h4><p>{ex[1]}</p></div><div class="yes" id="{sid}v2"><h4>✓ Plutôt</h4><p>{ex[2]}</p></div></div>'''
                a(f"#{sid}v1", "{opacity:0,x:-80}", "{opacity:1,x:0,duration:.5}", at)
                a(f"#{sid}v2", "{opacity:0,x:80}", "{opacity:1,x:0,duration:.5}", at + ex[3])
            elif typ == "list":
                items = []
                step = ex[2] if ex[2] != "auto" else max(0.5, (d - at + t0 - 0.8) / len(ex[1]))
                for j, txt in enumerate(ex[1]):
                    x = " x" if txt.startswith("!") else ""
                    txt = txt.lstrip("!")
                    items.append(f'<div class="chk{x}" id="{sid}i{j}"><i>{"✕" if x else "✓"}</i>{txt}</div>')
                    a(f"#{sid}i{j}", "{opacity:0,x:-80}", "{opacity:1,x:0,duration:.4}", at + j * step, '"back.out(1.6)"')
                extra = "".join(items)
        body = f'''<div class="center" style="top:{sc.get("top",300)}px">{head}{title}</div>
<div class="center" style="top:{sc.get("extop",780)}px">{extra}</div>'''
        cls = "light"
    import re
    body = re.sub(r"(\d) (h|minutes)\b", r"\1&nbsp;\2", body)
    for a_, b_ in ((" ?", "&nbsp;?"), (" !", "&nbsp;!"), (" :", "&nbsp;:"), (" »", "&nbsp;»"), ("« ", "«&nbsp;"), ("vos <span>créneaux", "vos&nbsp;<span>créneaux")):
        body = body.replace(a_, b_)
    html = f'<div id="{sid}" class="clip {cls}" data-start="{round(t0,2)}" data-duration="{d}" data-track-index="1">{body}</div>'
    return html, "\n".join(js)


def align(spec, voix):
    """Calcule t de chaque scène : proportion de caractères, recalée sur la fin de silence la plus proche."""
    import re
    out = subprocess.run(["ffmpeg", "-i", voix, "-af", "silencedetect=noise=-30dB:d=0.18", "-f", "null", "-"], capture_output=True, text=True).stderr
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", out)]
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", out)]
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", voix], capture_output=True, text=True).stdout)
    s0 = ends[0] if starts and starts[0] < 0.05 else 0.0
    s1 = max([x for x in starts if x > total * 0.8] or [total])
    lens = [len(sc["say"]) for sc in spec["scenes"]]
    tot = sum(lens); acc = 0; ts = []
    for L in lens:
        est = s0 + (s1 - s0) * acc / tot
        near = min(ends, key=lambda e: abs(e - est)) if ends else est
        ts.append(near if abs(near - est) < 1.3 else est)
        acc += L
    ts[0] = 0.0
    for sc, t in zip(spec["scenes"], ts): sc["t"] = round(max(0, t - 0.12), 2)
    spec["cta"] = round(s1 + 0.35, 2); spec["dur"] = round(spec["cta"] + 4.6, 2)
    print(spec["slug"], "voix", total, "scènes", [sc["t"] for sc in spec["scenes"]], "cta", spec["cta"], "durée", spec["dur"])


def build(spec, voix):
    align(spec, voix)
    slug, dur = spec["slug"], spec["dur"]
    scs = spec["scenes"]; cta_t = spec["cta"]
    bodies, jss = [], []
    for i, sc in enumerate(scs):
        t1 = scs[i + 1]["t"] if i + 1 < len(scs) else cta_t
        h, j = scene(i, sc, sc["t"], t1)
        bodies.append(h); jss.append(j)
    bodies.append(cta(cta_t, round(dur - cta_t, 2)))
    js = "\n".join(jss) + "\n" + cta_js(cta_t, cta_t + 1.4, cta_t + 2.2)
    d = BASE / "build" / slug
    if d.exists(): shutil.rmtree(d)
    (d / "assets").mkdir(parents=True)
    for sub in ("fonts", "vendor"): shutil.copytree(SRC / sub, d / sub)
    for f in ("hyperframes.json", "meta.json"): shutil.copy(SRC / f, d / f)
    shutil.copy(SRC / "assets" / "logo_blanc.png", d / "assets" / "logo_blanc.png")
    shutil.copy(voix, d / "assets" / "voix.wav")
    shutil.copy(BASE / "reels" / "ambient30.wav", d / "assets" / "ambient.wav")
    html = page(dur, "\n".join(bodies), js, "voix.wav").replace("Lien en bio ↓", "Lien en bio · guidpilot.fr").replace("</style>", EXTRA + "</style>", 1)
    (d / "index.html").write_text(html)
    print("ok", d)


if __name__ == "__main__":
    sys.path.insert(0, str(pathlib.Path(__file__).parent))
    from conseils_specs import SPECS
    build(SPECS[sys.argv[1]], sys.argv[2])
