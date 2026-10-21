"""Assemble plusieurs voix off (une par paragraphe) en un seul wav avec des pauses, et écrit les temps de début/fin.
Usage : python3 assembler_voix.py <sortie.wav> <sortie.json> <voix1.mp3> <voix2.mp3> ...
Pause de 0,4 s au début et 0,7 s entre paragraphes ; voix normalisée (-15 LUFS), 48 kHz stéréo."""
import json, subprocess, sys, tempfile, pathlib

out_wav, out_json, files = sys.argv[1], sys.argv[2], sys.argv[3:]
tmp = pathlib.Path(tempfile.mkdtemp())
def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout)
parts, starts, ends, t = [], [], [], 0.4
def sil(d, n):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", str(d), "-c:a", "pcm_s16le", str(tmp / n)], check=True)
    return tmp / n
parts.append(sil(0.4, "s0.wav"))
for i, f in enumerate(files):
    w = tmp / f"p{i}.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f, "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(w)], check=True)
    d = dur(w); starts.append(round(t, 2)); t += d; ends.append(round(t, 2)); parts.append(w)
    if i < len(files) - 1:
        parts.append(sil(0.7, f"g{i}.wav")); t += 0.7
lst = tmp / "l.txt"; lst.write_text("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", out_wav], check=True)
json.dump({"starts": starts, "ends": ends, "total": round(t, 2)}, open(out_json, "w"))
print("ok", out_wav, round(t, 2), starts)
