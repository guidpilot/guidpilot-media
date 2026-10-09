import numpy as np, wave
sr=48000; bpm=88; beat=60/bpm; dur=18.0
t=np.arange(int(sr*dur))/sr; out=np.zeros((len(t),2))
def note(f,start,length,amp=0.18,pan=0.0):
    n=int(length*sr); s=int(start*sr)
    if s>=len(t): return
    n=min(n,len(t)-s); tt=np.arange(n)/sr
    env=np.minimum(1,tt/0.01)*np.exp(-tt*2.2)
    w=(np.sin(2*np.pi*f*tt)+0.35*np.sin(2*np.pi*2*f*tt)*np.exp(-tt*4)+0.12*np.sin(2*np.pi*3*f*tt)*np.exp(-tt*6))*env*amp
    out[s:s+n,0]+=w*(1-pan)*0.9; out[s:s+n,1]+=w*(1+pan)*0.9
def midi(m): return 440*2**((m-69)/12)
# Cmaj9 - Am9 - Fmaj9 - G6sus  (progression douce, originale)
chords=[[48,55,59,62,64],[45,52,55,59,62],[41,48,52,55,60],[43,50,55,57,62]]
bar=4*beat; i=0; st=0.0
while st<dur:
    ch=chords[i%4]
    note(midi(ch[0]-12),st,bar,0.20)
    for k,m in enumerate(ch[1:]): note(midi(m),st+k*0.03,bar,0.075,pan=(k-1.5)*0.25)
    # arpège léger
    arp=[ch[2]+12,ch[3]+12,ch[4]+12,ch[3]+12]
    for b in range(8): note(midi(arp[b%4]),st+b*beat/2,beat,0.045,pan=0.4 if b%2 else -0.4)
    st+=bar; i+=1
# percussion douce : kick + shaker
for b in range(int(dur/beat)+1):
    s=int(b*beat*sr); n=int(0.25*sr)
    if s+n<len(t) and b%2==0:
        tt=np.arange(n)/sr; k=np.sin(2*np.pi*(55+70*np.exp(-tt*30))*tt)*np.exp(-tt*14)*0.28
        out[s:s+n]+=k[:,None]
    s2=int((b+0.5)*beat*sr); n2=int(0.06*sr)
    if s2+n2<len(t):
        hh=np.random.RandomState(b).randn(n2)*np.exp(-np.arange(n2)/sr*60)*0.03
        out[s2:s2+n2]+=hh[:,None]
fade=np.ones(len(t)); f=int(1.5*sr); fade[-f:]=np.linspace(1,0,f); fade[:int(.3*sr)]=np.linspace(0,1,int(.3*sr))
out*=fade[:,None]; out/=np.max(np.abs(out))*1.1
w=wave.open('musique.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
w.writeframes((out*32767).astype('<i2').tobytes()); w.close()
