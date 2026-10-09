#!/usr/bin/env bash
# Remplace la piste audio d'une vidéo rendue par : voix off + musique originale qui baisse quand la voix parle.
# Usage : mixer.sh <video_rendue.mp4> <voix.wav> <preset> <sortie.mp4> [volume_musique=0.32]
set -euo pipefail
VID="$1"; VOIX="$2"; PRESET="$3"; OUT="$4"; VOL="${5:-0.32}"
DIR="$(cd "$(dirname "$0")" && pwd)"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VID")
TMP=$(mktemp -d)
python3 "$DIR/compose.py" "$PRESET" "$DUR" "$TMP/musique.wav" >/dev/null
ffmpeg -loglevel error -y -i "$VOIX" -i "$TMP/musique.wav" -filter_complex \
  "[1:a]volume=${VOL}[m];[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,asplit=2[v][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];[v][md]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.95[a]" \
  -map "[a]" -t "$DUR" -ar 48000 "$TMP/mix.wav"
ffmpeg -loglevel error -y -i "$VID" -i "$TMP/mix.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest "$OUT"
rm -rf "$TMP"
echo "ok $OUT"
