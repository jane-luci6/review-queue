# Aliante LED — Rough Cut 1 Notes

**Built:** 2026-09-08 (PT)  
**Owner:** Maker  
**Authority:** `editorial/paper-edit-final.md` + `design/minimum-visual-editing-treatment.md`

## Deliverable
- **Export:** `assembly/aliante-led-rough-cut-1.mp4`
- **Absolute path:** `/Users/janehaynie/Documents/Cursor Projects/luci-design/video-production/projects/aliante-led/assembly/aliante-led-rough-cut-1.mp4`
- **Duration (ffprobe):** 112.000s (~1:52)
- **Format:** 1920×1080, 24fps, H.264 (yuv420p) + AAC mono ambient bed (audio r2 revise)
- **Also:** `assembly/aliante-led-rough-cut-1-r2.mp4` (identical safety twin of current export)
- **Not published** to Content/Video or website

## Assembly summary
1. Parsed paper-edit into 32 timeline segments (11 sections, 112s contiguous).
2. Resolved asset IDs via `analysis/asset-manifest.json`. Manifest paths for Mike’s folder omitted `Before Photos/` nesting — resolved on disk to `Before Photos/Mike's Before Photos/…` (same filenames). **I0065** also had a same-name duplicate under `B-Roll/`; used the Mike’s path matching the asset id / matched-viewpoint preview (finished LED wall hero).
3. Extracted/scaled each shot to 1920×1080 cover/center crop @ 24fps; **all source audio muted**.
4. Stills held static (no Ken Burns). 5-photo build: I0054→I0059→I0062→I0008→I0027 at ~1.1s each (26/26/27/26/27 frames = 5.5s exact).
5. Hard-cut concat of all segments.
6. Burned 24 supers with Pillow overlays (ffmpeg build lacked libass/drawtext): Syncopate Bold **only** on title L1 `Aliante Casino + Hotel`; Space Grotesk Bold for subtitle, all body cards, end card. Soft navy scrim `#0A161C` ~50% under type. Center stack for titles + end; lower-third for body. Fade ~0.4s (~10 frames @24).
7. Placeholder continuous instrumental: soft ambient sine/pink-noise bed generated with ffmpeg lavfi; mixed quiet (~0.22). No lyrics/voice.
8. Work intermediates left under `assembly/_work/` (segments, picture_silent, checks, build_meta).

## Shot count
- **32 segments** covering all paper-edit beats S1–S11
- **24 onscreen cards**, verbatim from paper-edit absolute times

## Commands (summary)
- Per-shot: `ffmpeg -ss … -i SRC -t … -vf scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24` (+ `tpad` freeze holds on V0038/V0007 tails)
- Stills: `ffmpeg -loop 1 -frames:v N …`
- Concat demuxer → `picture_silent.mp4`
- Ambient: lavfi `sine` + `anoisesrc` → `ambient_bed.m4a`
- Supers: Pillow RGBA overlays → frame-pipe composite → libx264/aac export

## Self-check
| Item | Status |
|---|---|
| All required asset IDs resolved | Yes (path nesting fix noted) |
| Source ranges per paper-edit | Yes |
| Verbatim cards | Yes (24/24) |
| Syncopate only on title L1 | Yes |
| Space Grotesk elsewhere | Yes |
| Source muted | Yes |
| Placeholder music | Yes (audible ambient, loudnorm ~−29 LUFS, ducked under cards) |
| 1080p 16:9 | Yes |
| No publish | Yes (assembly/ only) |
| Stills static | Yes |
| 5-photo ~1.1s | Yes (5.5s total) |
| End card verbatim AV | Yes |

## Gaps / notes for CoS
- Homebrew ffmpeg 8.1.1 on this Mac has **no libass / drawtext**; supers burned via Pillow. Typography is correct faces/weights from design-system TTFs.
- Manifest `absolute_path` for Mike’s images missing `Before Photos/` prefix; also duplicate `IMG_4879.jpeg` under B-Roll — flagged, resolved to Mike’s path for I0065.
- Frame-quantized durations at 24fps (e.g. 3.2s → 3.2083s) — total still **112.000s**.
- Placeholder music is generated ambient, not licensed/selected bed — deferred polish.
- **Audio revise (2026-09-08 PT):** Critical inaudible bed fixed — see Audio revise section.

## Audio revise (r2) — 2026-09-08 PT
**Owner:** Maker  
**Trigger:** Review Critical — placeholder ambient bed effectively inaudible.

| Metric | Before (rough cut 1) | After (r2 / current) |
|---|---|---|
| volumedetect mean | −75.3 dB | −28.9 dB |
| volumedetect max | −68.0 dB | −17.8 dB |
| ebur128 Integrated | −70.0 LUFS | **−30.2 LUFS** |
| ebur128 LRA | 0.0 LU | 4.5 LU (duck activity) |

**Method (audio-only remux; picture untouched):**
1. Regenerated soft continuous instrumental/ambient (layered sines + pink noise, no lyrics/voice) for 112s.
2. `loudnorm=I=-28:LRA=7:TP=-1.5` → preduck Integrated −28.0 LUFS.
3. Duck ~4.4 dB (`volume=0.6`) under merged card windows from `overlay_meta.json` (titles/body/end). Spot-check: unducked gap ~42–53s mean −26.2 dB; ducked card ~20–24s mean −30.7 dB.
4. Remux onto existing cut with **`-c:v copy`** (H.264 stream untouched: 1920×1080, 24fps, 2688 frames, ~6895 kb/s). AAC mono ~160k replaces prior near-silent bed. Source picture audio remains absent/muted.
5. Export: overwrite `assembly/aliante-led-rough-cut-1.mp4`; safety twin `assembly/aliante-led-rough-cut-1-r2.mp4`. Work: `assembly/_work/ambient_bed_loud_preduck.wav`, `ambient_bed_r2.m4a`, `checks/audio_r2_verify.txt`.

**Not changed:** video frames, supers, fonts, shot order, copy, source media.

