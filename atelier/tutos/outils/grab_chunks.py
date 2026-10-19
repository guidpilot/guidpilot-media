"""Recompose une capture renvoyée en morceaux ('@@CHUNKn@@' + slice) :
python3 grab_chunks.py <nom> <id-fichier-0> <id-fichier-1> ... [--scroll Y]"""
import glob, json, re, sys
args = sys.argv[1:]
scroll = dlg = None
if "--scroll" in args:
    i = args.index("--scroll"); scroll = int(args[i + 1]); del args[i:i + 2]
if "--dlg" in args:
    i = args.index("--dlg"); dlg = int(args[i + 1]); del args[i:i + 2]
name, ids = args[0], args[1:]
D = '/root/.claude/projects/-home-claude/5ba92c8e-caf3-5b0c-b941-3cff9988c4e0/tool-results/'
parts = []
for n, fid in enumerate(ids):
    f = glob.glob(D + f'*javascript_tool-{fid}*.txt')[0]
    t = json.load(open(f))[0]['text']
    tag = f'@@CHUNK{n}@@'
    i = t.index(tag) + len(tag); j = t.rindex('"\n')
    parts.append(json.loads('"' + t[i:j] + '"'))
h = ''.join(parts)
assert h.startswith('<!doctype') and h.rstrip().endswith('</html>'), 'capture incomplète'
if scroll is not None or dlg is not None:
    m = re.search(r'<!--GPSNAP (\{.*?\})-->', h); meta = json.loads(m.group(1))
    if scroll is not None: meta['scrollY'] = scroll
    if dlg is not None: meta['dlgTop'] = dlg
    h = h.replace(m.group(0), '<!--GPSNAP ' + json.dumps(meta) + '-->', 1)
open(f'/home/claude/tuto/snaps/{name}.html', 'w').write(h)
print(name, len(h))
