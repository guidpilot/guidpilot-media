"""Planche contact d'un tuto (une image par scène) : python3 planche.py <slug> <sortie.jpg>"""
import json, subprocess, sys, tempfile, pathlib
from PIL import Image
slug, out = sys.argv[1], sys.argv[2]
b = json.load(open(f"build/{slug}/timing.json"))["bounds"]
tmp = pathlib.Path(tempfile.mkdtemp()); ims = []
for i in range(len(b) - 1):
    t = b[i] + min(4.5, (b[i + 1] - b[i]) * 0.7); f = tmp / f"{i:02d}.jpg"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", f"build/{slug}.mp4", "-frames:v", "1", "-vf", "scale=640:-1", str(f)])
    ims.append(Image.open(f))
W, H = ims[0].size; s = Image.new("RGB", (W * 3, H * ((len(ims) + 2) // 3)), "white")
for i, im in enumerate(ims): s.paste(im, ((i % 3) * W, (i // 3) * H))
s.save(out, quality=85)
