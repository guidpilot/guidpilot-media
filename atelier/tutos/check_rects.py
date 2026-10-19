"""Vérifie que tous les éléments visés d'un tuto sont trouvés : python3 check_rects.py <spec.py>"""
import sys, pathlib
from tuto_video import load_spec, resolve_shots
spec = load_spec(sys.argv[1])
w = pathlib.Path('build') / spec['slug']; w.mkdir(parents=True, exist_ok=True)
resolve_shots(spec, pathlib.Path('/home/claude/tuto/snaps'), w)
for i, sc in enumerate(spec['scenes']):
    if sc['type'] == 'shot':
        r = sc['_rect']; print(i, sc['snap'], {k: round(v) for k, v in r.items()}, sc['_click'] and [round(x) for x in sc['_click']])
