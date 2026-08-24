#!/usr/bin/env bash
# Aliante Race & Sports — "In a world…" trailer, cut from real project footage.
# Picture cut only (silent). See aliante-trailer-prompt.md for the VO script and sound design.
set -euo pipefail

SRC="/Users/janehaynie/Library/CloudStorage/OneDrive-LUCISystems/Marketing - Documents/Content/Project Media/Aliante LED"
FONTS="/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/fonts"
WORK="/tmp/aliante-trailer-build"
CARDS="$WORK/cards"
OUT="${1:-$HOME/Desktop/aliante-trailer-v1.mp4}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

rm -rf "$WORK"; mkdir -p "$WORK"
python3 "$HERE/make-trailer-cards.py" "$CARDS"

# 2.39:1 inside a 1920x1080 frame: 1920x804 active, 138px bars.
GRADE="eq=contrast=1.14:brightness=-0.02:saturation=1.06,vignette=PI/5"
FIT="scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:804"
PAD="pad=1920:1080:0:138:black,format=yuv420p"
ENC=(-c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -an -movflags +faststart)

n=0
SEGFILE=""
# Sets $SEGFILE rather than echoing it — a command substitution would run this
# in a subshell and the counter increment would be lost.
seg() { n=$((n+1)); SEGFILE=$(printf "%s/%02d.mp4" "$WORK" "$n"); }

# --- shot: trim a clip, grade, letterbox -------------------------------------
# shot <file> <start> <dur> [extra filters]
shot() {
  local f="$1" ss="$2" d="$3" extra="${4:-}"
  seg; local out="$SEGFILE"
  local chain="$FIT,$GRADE"
  [ -n "$extra" ] && chain="$chain,$extra"
  chain="$chain,$PAD"
  ffmpeg -v error -ss "$ss" -t "$d" -i "$f" -vf "$chain" "${ENC[@]}" -y "$out"
  echo "file '$out'" >> "$WORK/list.txt"
}

# --- card: pre-rendered PNG title card ---------------------------------------
# This ffmpeg build has no drawtext filter, so make-trailer-cards.py renders the
# type with PIL (which also gives us real letter-spacing).
# card <key> <dur> [fade-in] [fade-out]
card() {
  local key="$1" d="$2" fi="${3:-0.25}" fo="${4:-0.25}"
  seg; local out="$SEGFILE"
  local png="$CARDS/card_${key}.png"
  local f="fade=t=in:st=0:d=$fi,fade=t=out:st=$(awk -v d="$d" -v o="$fo" 'BEGIN{print d-o}'):d=$fo,format=yuv420p"
  ffmpeg -v error -loop 1 -t "$d" -i "$png" -vf "$f" "${ENC[@]}" -y "$out"
  echo "file '$out'" >> "$WORK/list.txt"
}

# --- still: photo with a push that decelerates to a stop ---------------------
# still <file> <dur>
still() {
  local f="$1" d="$2"
  seg; local out="$SEGFILE"
  local frames; frames=$(awk -v d="$d" 'BEGIN{printf "%d", d*30}')
  # ease-out cubic: most of the move happens early, so it settles on the last beat
  local z="1+0.09*(1-pow(1-min(on/${frames}\,1)\,3))"
  ffmpeg -v error -loop 1 -t "$d" -i "$f" -vf \
"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:1607,\
zoompan=z='$z':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x804:fps=30,\
$GRADE,$PAD" "${ENC[@]}" -y "$out"
  echo "file '$out'" >> "$WORK/list.txt"
}

black() {
  local d="$1"; seg; local out="$SEGFILE"
  ffmpeg -v error -f lavfi -i "color=c=black:s=1920x1080:d=$d:r=30" \
    -vf format=yuv420p "${ENC[@]}" -y "$out"
  echo "file '$out'" >> "$WORK/list.txt"
}

# Structure: nothing finished appears until the payoff. Movements I-III are
# strictly before / in-progress footage, so the lit wall is genuinely withheld.
# Payoff in-points come off a camera-motion profile so each one settles.

echo "→ I. the world"
shot "$SRC/B-Roll/IMG_5017.mov"  1.5 2.6 "fade=t=in:st=0:d=1.0"   # COMING SOON barricade
card c1 3.0
shot "$SRC/IMG_4853.mov"         2.0 2.2                          # dark shell, plastic sheeting
card c2 2.0
shot "$SRC/IMG_4802.mov"         8.0 2.2                          # bare wall going up
card c3 2.2

echo "→ II. the hero"
shot "$SRC/IMG_4854.mov"         2.0 2.2
card c4 2.4
card c5 2.6

black 1.2

echo "→ III. the odds"
card c6 1.8
shot "$SRC/IMG_4862.mov"         1.0 2.2                          # panel grid, two lifts
card c7 1.8
shot "$SRC/IMG_4843.mov"         6.0 2.0
card c8 1.8
shot "$SRC/IMG_5001.mov"         9.0 1.6                          # cable tray
card c9 1.5
shot "$SRC/IMG_4843.mov"         1.5 1.6 "fade=t=out:st=1.2:d=0.4" # lift working the grid
card c10 1.4
shot "$SRC/IMG_4850.mov"       150.0 1.8                          # crew at the wall
card c11 2.6 0.25 0.8

echo "→ the silence"
black 2.0

echo "→ IV. the payoff — first finished footage in the whole cut"
shot "$SRC/IMG_5022.mov"         1.5 4.5 "fade=t=in:st=0:d=1.2"   # drifts, then settles
card c12 2.4
shot "$SRC/IMG_5240.mov"         0.2 2.2                          # calm, tight on the wall
shot "$SRC/IMG_5238.MOV"         9.5 3.6                          # lands on the hero wide
card c13 2.8
shot "$SRC/IMG_5235.mov"        17.5 3.0                          # lands, room full
still "$SRC/IMG_5033.jpeg"       2.6                              # run from a phone

echo "→ V. the tag"
card c14 3.0 0.4 0.4
card end1 3.5 0.5 0.3
card end2 2.6 0.4 0.8

echo "→ assembling"
ffmpeg -v error -f concat -safe 0 -i "$WORK/list.txt" -c copy -y "$OUT"

dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")
echo "✓ $OUT  (${dur}s)"
