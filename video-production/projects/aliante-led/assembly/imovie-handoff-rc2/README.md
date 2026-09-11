# Aliante Rough Cut 2 — iMovie handoff

This folder reproduces **Rough Cut 2** (RC2) as separate, editable pieces for iMovie. It does **not** contain a new cut. The picture edit, shot order, and timing are unchanged from `assembly/aliante-led-rough-cut-2.mp4`.

## What's here

```
imovie-handoff-rc2/
  timeline/                              40 clips, numbered 001–040 in cut order
  alternates/                            curated replacement options by category
  titles.md                              every onscreen text, in order, verbatim copy
  aliante-led-rough-cut-2-reference.mp4  RC2 master — reference only, do not re-import as the edit
  README.md                              this file
```

## How to reproduce RC2 in iMovie

1. Open iMovie → create a new **Movie** project (16:9, 1920×1080, 24 fps if offered).
2. Import the **entire `timeline/` folder** (File → Import Media, or drag the folder in).
3. Drag the clips onto the timeline **in numbered order**: `001-…` → `040-…`. They are already trimmed to the exact in/out and duration RC2 uses, so placing them back-to-back reproduces the RC2 picture track exactly.
4. Add the titles from `titles.md`:
   - Each row lists the clip number it sits over, the **exact copy** (do not reword), and the approximate start time / duration.
   - Place an iMovie title over the matching clip, paste the copy, and set the duration to match.
   - See `titles.md` → Role legend for the intended type/style per card.
5. Compare against `aliante-led-rough-cut-2-reference.mp4` to confirm timing and titles match. (Do not drop the reference into the edit — it is for checking only.)

## Notes

- **Clip format:** all 40 timeline clips are H.264, 1920×1080, 24 fps, no burned-in text. Stills in RC2 were rendered to short video clips of the exact duration, so the timeline auto-reproduces without setting photo durations by hand.
- **Audio:** RC2's audio is a single synthetic ambient bed, not per-clip source audio. The timeline clips are silent (faithful to RC2). Add your own music/ambient in iMovie — the original bed lives at `assembly/_work_rc2/ambient_bed_rc2.m4a` if you want to reference it, but it is **not** part of this handoff.
- **Same source used more than once:** clips `021` and `023` both come from `IMG_4817.mov`; clips `025`, `026`, and `039` all come from `IMG_5235.mov`. Each use is a separate, independently-trimmed file in this folder — keep them in order.
- **End card:** clip `040` is the dedicated LUCI end card (navy + logo). The end-card tagline title (`c19`) sits over it.

## Alternates (`alternates/`)

A small, curated set of strong replacement options — **not** the whole library. Swap one in for a timeline clip if you want a different angle; trim it in iMovie to match. Organized by category:

| Folder | Count | What it is |
|---|---|---|
| `casino-floor/` | 3 | Finished casino-floor shots (2 stills + 1 construction-barricade clip) |
| `broader-property-lobby/` | 3 | Lobby / food-court B-roll not used in RC2 |
| `construction-build/` | 3 | LED wall + ticker install, technicians on lifts |
| `rack-room/` | 3 | Pan active→empty racks, decommissioned projectors, completed LUCI racks |
| `finished-wall/` | 3 | Finished curved LED wall, multi-source, with people |
| `finished-ticker/` | 2 | Finished wrap-around LED ticker, with people |
| `live-sportsbook-with-people/` | 3 | Live sportsbook/racebook/bar with people |
| `true-before-sportsbook-photos/` | 3 | The true "before" sportsbook photos (I0090 / I0091 / I0092) |
| `matched-progress-photos/` | 5 | The five matched-viewpoint progress photos in approved order (I0054 → I0059 → I0062 → I0008 → I0027) |

The true-before photos and the five matched-progress photos are already in the RC2 timeline (clips `006`–`008` and `033`–`037`); they are included here again as easy replacement options.

## Source of truth (do not edit)

- Shot timing: `assembly/_work_rc2/build_meta.json`
- Title text/timing: `assembly/_work_rc2/overlay_meta.json`
- RC2 master (untouched): `assembly/aliante-led-rough-cut-2.mp4`
- Source media (read-only, OneDrive): `Marketing - Documents/Content/Project Media/Aliante LED/`

## Do not

- Do not re-edit the picture, swap shots, or change timing — this handoff reproduces RC2, it does not make Rough Cut 3.
- Do not burn text into the video clips; titles are added in iMovie from `titles.md`.
- Do not modify, move, rename, or delete any source file under OneDrive or the `assembly/` master.
