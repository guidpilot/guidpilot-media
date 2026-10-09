"""Compose des musiques de fond ORIGINALES (donc sans droits d'auteur) pour les vidéos GuidPilot.
Usage : python3 compose.py <preset> <durée_s> <sortie.wav>
Presets : lofi (88 bpm, piano doux), aube (72 bpm, nappes lumineuses), elan (104 bpm, plus rythmé),
          cocon (64 bpm, très calme, sans percussion), pilote (96 bpm, corporate chaleureux)
"""
import sys, wave
import numpy as np

SR = 48000
PRESETS = {
    "lofi":   dict(bpm=88,  chords=[[48,55,59,62,64],[45,52,55,59,62],[41,48,52,55,60],[43,50,55,57,62]], arp=True,  drums="soft", pad=False, bright=1.0),
    "aube":   dict(bpm=72,  chords=[[50,57,61,64,69],[47,54,57,62,66],[43,50,54,57,62],[45,52,57,61,64]], arp=True,  drums="none", pad=True,  bright=1.3),
    "elan":   dict(bpm=104, chords=[[45,52,57,60,64],[41,48,53,57,60],[48,55,60,64,67],[43,50,55,59,62]], arp=True,  drums="full", pad=False, bright=1.1),
    "cocon":  dict(bpm=64,  chords=[[53,60,64,67,72],[50,57,60,65,69],[46,53,58,62,65],[48,55,60,64,67]], arp=False, drums="none", pad=True,  bright=0.8),
    "pilote": dict(bpm=96,  chords=[[52,59,63,66,71],[49,56,59,64,68],[45,52,57,61,64],[47,54,59,63,66]], arp=True,  drums="soft", pad=True,  bright=1.0),
}

def midi(m): return 440 * 2 ** ((m - 69) / 12)

def compose(p, dur, seed=0):
    rng = np.random.RandomState(seed)
    n_tot = int(SR * dur)
    out = np.zeros((n_tot, 2))
    beat = 60 / p["bpm"]; bar = 4 * beat

    def note(f, start, length, amp, pan=0.0, decay=2.2, pad=False):
        s = int(start * SR)
        if s >= n_tot: return
        n = min(int(length * SR), n_tot - s); tt = np.arange(n) / SR
        if pad:
            env = np.minimum(1, tt / 0.6) * np.minimum(1, (length - tt) / 0.6).clip(0, 1)
            w = (np.sin(2*np.pi*f*tt) + 0.5*np.sin(2*np.pi*f*1.003*tt) + 0.25*np.sin(2*np.pi*2*f*tt)) * env * amp
        else:
            env = np.minimum(1, tt / 0.01) * np.exp(-tt * decay)
            b = p["bright"]
            w = (np.sin(2*np.pi*f*tt) + 0.35*b*np.sin(2*np.pi*2*f*tt)*np.exp(-tt*4) + 0.12*b*np.sin(2*np.pi*3*f*tt)*np.exp(-tt*6)) * env * amp
        out[s:s+n, 0] += w * (1 - pan) * 0.9
        out[s:s+n, 1] += w * (1 + pan) * 0.9

    st, i = 0.0, 0
    while st < dur:
        ch = p["chords"][i % 4]
        note(midi(ch[0] - 12), st, bar, 0.20)
        for k, m in enumerate(ch[1:]):
            note(midi(m), st + k * 0.03, bar, 0.07, pan=(k - 1.5) * 0.25)
            if p["pad"]: note(midi(m), st, bar, 0.035, pan=(1.5 - k) * 0.3, pad=True)
        if p["arp"]:
            arp = [ch[2] + 12, ch[3] + 12, ch[4] + 12, ch[3] + 12]
            for b in range(8):
                note(midi(arp[b % 4]), st + b * beat / 2, beat, 0.04, pan=0.4 if b % 2 else -0.4, decay=3.0)
        st += bar; i += 1

    if p["drums"] != "none":
        for b in range(int(dur / beat) + 1):
            s = int(b * beat * SR); n = int(0.25 * SR)
            if s + n < n_tot and (b % 2 == 0 or p["drums"] == "full"):
                tt = np.arange(n) / SR
                k = np.sin(2*np.pi*(55 + 70*np.exp(-tt*30))*tt) * np.exp(-tt*14) * (0.28 if b % 2 == 0 else 0.15)
                out[s:s+n] += k[:, None]
            for off, amp in ((0.5, 0.03),) + (((0.25, 0.015), (0.75, 0.015)) if p["drums"] == "full" else ()):
                s2 = int((b + off) * beat * SR); n2 = int(0.06 * SR)
                if s2 + n2 < n_tot:
                    hh = rng.randn(n2) * np.exp(-np.arange(n2) / SR * 60) * amp
                    out[s2:s2+n2] += hh[:, None]
            if p["drums"] == "full" and b % 4 == 2:
                s3 = int(b * beat * SR); n3 = int(0.18 * SR)
                if s3 + n3 < n_tot:
                    sn = rng.randn(n3) * np.exp(-np.arange(n3) / SR * 25) * 0.06
                    out[s3:s3+n3] += sn[:, None]

    fade = np.ones(n_tot); f = int(1.5 * SR); fi = int(0.3 * SR)
    fade[-f:] = np.linspace(1, 0, f); fade[:fi] = np.linspace(0, 1, fi)
    out *= fade[:, None]; out /= np.max(np.abs(out)) * 1.1
    return out

if __name__ == "__main__":
    preset, dur, path = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    data = compose(PRESETS[preset], dur)
    w = wave.open(path, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((data * 32767).astype("<i2").tobytes()); w.close()
    print("ok", preset, dur, path)
