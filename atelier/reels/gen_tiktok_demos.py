"""Démos TikTok verticales (lot du 25/10/2026) : réutilise gen_v2.build (hook2 / shot / x / phone / brand).
Usage : python3 reels/gen_tiktok_demos.py <clé> <voix.wav>   (textes : reels/tiktok_demos_specs.py) → build/<slug>/
"""
import pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_v2
import gen_conseils as gc
from tiktok_demos_specs import SPECS

if __name__ == "__main__":
    spec = SPECS[sys.argv[1]]
    gen_v2.build(spec, sys.argv[2])
    d = gc.BASE / "build" / spec["slug"]
    shutil.copy(gc.SRC / "assets" / "logo_blanc.png", d / "assets" / "logo_blanc.png")  # logo officiel pour la scène brand
