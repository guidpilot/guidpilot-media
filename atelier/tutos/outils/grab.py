"""Extrait la dernière capture HTML renvoyée par le navigateur intégré et l'enregistre : python3 grab.py <nom>"""
import glob, json, os, sys
files = sorted(glob.glob('/root/.claude/projects/-home-claude/5ba92c8e-caf3-5b0c-b941-3cff9988c4e0/tool-results/mcp-remote-devices-Claude_Browser__javascript_tool-*.txt'), key=os.path.getmtime)
src = sys.argv[2] if len(sys.argv)>2 else files[-1]
if not src.startswith('/'): src=[f for f in files if src in f][0]
files=[src]
t = json.load(open(src))[0]['text']
s = t.index('<!doctype'); e = t.rindex('</html>') + 7
h = t[s:e]
if '\\n' in h[:300] or '\\"' in h[:2000]:
    h = json.loads('"' + h + '"')
os.makedirs('/home/claude/tuto/snaps', exist_ok=True)
open(f'/home/claude/tuto/snaps/{sys.argv[1]}.html', 'w').write(h)
print(sys.argv[1], len(h), os.path.basename(files[-1]))
