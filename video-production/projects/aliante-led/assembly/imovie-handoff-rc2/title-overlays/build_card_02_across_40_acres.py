#!/usr/bin/env python3
"""Render one-off card 02: "Across more than 40 acres" (no period) — REVISED.

BODY-TREATMENT-LOCK.md rev 2 — two-layer build (bed + plate), N-class geometry.
One-off card in cards/ (not part of c02-c19 titles.md sequence).

Jane's rev 11 Sep (this card only — per-card override, NOT a house-rule change):
  - Highlight "40 acres" the same way as "100,000+" on card 01:
    SpaceGrotesk-SemiBold display scale (128), color mint #68E3BE.
  - Lead-in "Across more than" stays readable off-white Medium 52 @ 95%
    (same hierarchy as "With" on card 01).
  - No mint rule (Jane removed it on card 01; do not bring it back).
  - Keep plate + bed (rev 2), left-anchored.
  - Copy verbatim, no period: "Across more than 40 acres"

Per-card override of BODY-TREATMENT-LOCK.md (NOT a house-rule change):
  - §2: "Type is off-white, never mint..."  -> mint goes on "40 acres" here.
  - §3.1 / §1 / §7: the 56x3 mint rule is removed.
  - §6: "Nothing after the title slide sets type in mint." -> mint type here.
  These overrides apply to THIS CARD ONLY. The lock still governs every
  other body card (c02-c19) unchanged. Only Jane can promote a preference
  to a universal rule (per the learned-preferences rule, 11 Sep).

Layout: two lines (shared baseline at 128px exceeds the 864 measure, so the
brief's "break cleanly if measure needs it" fallback applies). Word order
preserved; "40" stays with "acres" on one line.
  Line 1: "Across more than" — Medium 52, off-white 95%, baseline y=800
  Line 2: "40 acres" — SemiBold 128, mint 100%, baseline y=920 (anchor)
The numeral sits on the anchor at the same 128px display scale as card 01's
"100,000+", in the same mint #68E3BE. S-class plate (top y=680) matches
card 01's geometry. 30px gap between line 1 baseline and the numeral cap-top.

Composite order: footage -> bed -> plate -> type (with shadow). No mint rule.
Never ship plate without bed. No pill, no radius, no centered text.
"""
from __future__ import annotations
import subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).resolve().parent
CARDS = HERE / "cards"
TIMELINE = HERE.parent / "timeline"
FONTS = Path("/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/assets/fonts")
CARDS.mkdir(parents=True, exist_ok=True)

W, H = 1920, 1080
OFF_WHITE = (245, 248, 250)   # #F5F8FA
MINT = (104, 227, 190)       # #68E3BE
NAVY_DEEP = (10, 22, 28)     # #0A161C
FONT_MEDIUM = FONTS / "SpaceGrotesk-Medium.ttf"
FONT_SEMIBOLD = FONTS / "SpaceGrotesk-SemiBold.ttf"

LEFT_X = 160
LAST_BASELINE_Y = 920        # anchor — last baseline (line 2, the numeral)
LINE1_BASELINE_Y = 800        # line 1 (lead-in) — 30px gap above numeral cap-top

# Bed (layer 1) — LOCK §3.2
BED_PEAK = 0.45
BED_TOP_Y = 380
BED_BOTTOM_Y = 1080
BED_H_FALLOFF_START = 980
BED_H_FALLOFF_END = 1920
BED_H_FALLOFF_END_MULT = 0.30

# Plate (layer 2) — LOCK §3.3, S-class (matches card 01's 128px numeral geometry)
PLATE_DENSITY = 0.62
PLATE_TOP_Y = 680            # S-class — same as card 01
PLATE_FULL_DENSITY_X = 1024
PLATE_FALLOFF_END_X = 1536
PLATE_FEATHER_PX = 8

SHADOW_ALPHA = 0.50
SHADOW_OFFSET = (0, 3)
SHADOW_BLUR = 22

# Copy (verbatim — Jane's line, no period)
LEADIN_TEXT = "Across more than"   # Medium 52, off-white 95%
HIGHLIGHT_TEXT = "40 acres"         # SemiBold 128, mint 100%

# Type sizes — match card 01's numeral pattern
HIGHLIGHT_SIZE = 128        # SemiBold — display scale, same as card 01's "100,000+"
MEDIUM_SIZE = 52            # Medium — readable lead-in, same as card 01's "With"
MEDIUM_OPACITY = 0.95       # ~95%, clearly readable, slightly subordinate

# Tracking
HIGHLIGHT_TRACKING = -3.84    # -0.03em at 128px (same as card 01 numeral)
MEDIUM_TRACKING = 0.52        # +0.01em at 52px (same as card 01 lead-in)

MEASURE_LIMIT_X = 1024       # right edge of 864 measure (160 + 864)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(str(c) for c in cmd[:4])}...\n{r.stderr[-1500:]}")
    return r


def _smoothstep(t):
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def build_bed():
    ys = np.arange(H, dtype=np.float32)
    v_alpha = np.zeros(H, dtype=np.float32)
    mask = ys >= BED_TOP_Y
    t_v = (ys[mask] - BED_TOP_Y) / (BED_BOTTOM_Y - BED_TOP_Y)
    v_alpha[mask] = BED_PEAK * (t_v * t_v)
    xs = np.arange(W, dtype=np.float32)
    h_mult = np.ones(W, dtype=np.float32)
    mask_h = xs > BED_H_FALLOFF_START
    t_h = (xs[mask_h] - BED_H_FALLOFF_START) / (BED_H_FALLOFF_END - BED_H_FALLOFF_START)
    h_mult[mask_h] = 1.0 - (1.0 - BED_H_FALLOFF_END_MULT) * (t_h * t_h)
    alpha_2d = v_alpha[:, None] * h_mult[None, :]
    alpha_8 = np.clip(alpha_2d * 255.0, 0, 255).astype(np.uint8)
    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    rgba[..., 0] = NAVY_DEEP[0]
    rgba[..., 1] = NAVY_DEEP[1]
    rgba[..., 2] = NAVY_DEEP[2]
    rgba[..., 3] = alpha_8
    return Image.fromarray(rgba).convert("RGBA")


def build_plate():
    ys = np.arange(H, dtype=np.float32)
    xs = np.arange(W, dtype=np.float32)
    v_feather = _smoothstep((ys - (PLATE_TOP_Y - PLATE_FEATHER_PX / 2)) / PLATE_FEATHER_PX)
    h_mult = np.ones(W, dtype=np.float32)
    mask_falloff = (xs > PLATE_FULL_DENSITY_X) & (xs <= PLATE_FALLOFF_END_X)
    t_h = (xs[mask_falloff] - PLATE_FULL_DENSITY_X) / (PLATE_FALLOFF_END_X - PLATE_FULL_DENSITY_X)
    h_mult[mask_falloff] = 1.0 - (t_h * t_h)
    h_mult[xs > PLATE_FALLOFF_END_X] = 0.0
    alpha_2d = PLATE_DENSITY * v_feather[:, None] * h_mult[None, :]
    alpha_8 = np.clip(alpha_2d * 255.0, 0, 255).astype(np.uint8)
    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    rgba[..., 0] = NAVY_DEEP[0]
    rgba[..., 1] = NAVY_DEEP[1]
    rgba[..., 2] = NAVY_DEEP[2]
    rgba[..., 3] = alpha_8
    return Image.fromarray(rgba).convert("RGBA")


def _text_width(font, text, tracking):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    if len(text) > 1:
        w += int(round(tracking * (len(text) - 1)))
    return w


def draw_two_lines(canvas):
    """Two-line layout: lead-in (Medium 52, off-white 95%) on line 1, highlight
    (SemiBold 128, mint 100%) on line 2 (the anchor). Word order preserved;
    "40" stays with "acres" on one line."""
    font_med = ImageFont.truetype(str(FONT_MEDIUM), MEDIUM_SIZE)
    font_semi = ImageFont.truetype(str(FONT_SEMIBOLD), HIGHLIGHT_SIZE)
    fill_med = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], int(round(255 * MEDIUM_OPACITY)))
    fill_hl = (MINT[0], MINT[1], MINT[2], 255)

    # Shadow layer for both lines
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    sd.text((LEFT_X + SHADOW_OFFSET[0], LINE1_BASELINE_Y + SHADOW_OFFSET[1]),
            LEADIN_TEXT, font=font_med,
            fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], 255),
            anchor="ls", tracking=MEDIUM_TRACKING)
    sd.text((LEFT_X + SHADOW_OFFSET[0], LAST_BASELINE_Y + SHADOW_OFFSET[1]),
            HIGHLIGHT_TEXT, font=font_semi,
            fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], 255),
            anchor="ls", tracking=HIGHLIGHT_TRACKING)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=SHADOW_BLUR))
    r, g, b, a = shadow_layer.split()
    a = a.point(lambda v: int(v * SHADOW_ALPHA))
    shadow_layer = Image.merge("RGBA", (r, g, b, a))
    canvas = Image.alpha_composite(canvas, shadow_layer)

    # Actual text
    draw = ImageDraw.Draw(canvas)
    draw.text((LEFT_X, LINE1_BASELINE_Y), LEADIN_TEXT, font=font_med,
              fill=fill_med, anchor="ls", tracking=MEDIUM_TRACKING)
    draw.text((LEFT_X, LAST_BASELINE_Y), HIGHLIGHT_TEXT, font=font_semi,
              fill=fill_hl, anchor="ls", tracking=HIGHLIGHT_TRACKING)
    return canvas


def render_card():
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    canvas = Image.alpha_composite(canvas, build_bed())
    canvas = Image.alpha_composite(canvas, build_plate())
    canvas = draw_two_lines(canvas)
    return canvas


def main():
    font_med = ImageFont.truetype(str(FONT_MEDIUM), MEDIUM_SIZE)
    font_semi = ImageFont.truetype(str(FONT_SEMIBOLD), HIGHLIGHT_SIZE)

    leadin_w = _text_width(font_med, LEADIN_TEXT, MEDIUM_TRACKING)
    highlight_w = _text_width(font_semi, HIGHLIGHT_TEXT, HIGHLIGHT_TRACKING)
    line1_right = LEFT_X + leadin_w
    line2_right = LEFT_X + highlight_w

    print("Layout: two lines (shared baseline at 128px exceeds measure 864;")
    print("  breaking cleanly per brief). Word order preserved; '40' with 'acres'.")
    print(f"  line 1: '{LEADIN_TEXT}' Medium 52 off-white 95% -> right x={line1_right} (limit {MEASURE_LIMIT_X})")
    print(f"  line 2: '{HIGHLIGHT_TEXT}' SemiBold 128 mint -> right x={line2_right} (limit {MEASURE_LIMIT_X})")

    p_overlay = CARDS / "card-02-across-40-acres-transparent.png"
    overlay = render_card()
    overlay.save(p_overlay)
    print(f"\nWROTE {p_overlay.name}  ({p_overlay.stat().st_size} bytes)")

    # Composite over same clip as before
    clip003 = TIMELINE / "003-s03-Casino 3-gaming-acres.mp4"
    frame003 = CARDS / "_frame-003-s03-card02.png"
    grab_frame(clip003, 2.0, frame003)
    prev = CARDS / "card-02-across-40-acres-preview.jpg"
    composite(frame003, p_overlay, prev)
    print(f"WROTE {prev.name}  ({prev.stat().st_size} bytes)")

    if frame003.exists():
        frame003.unlink()

    print("\nDONE. Revised one-off card 02 files in:")
    print(f"  {CARDS}")


def grab_frame(clip, ts, out):
    run([
        "ffmpeg", "-y", "-ss", f"{ts:.3f}", "-i", str(clip),
        "-frames:v", "1", "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-q:v", "2", str(out),
    ])


def composite(frame_png, overlay_png, out):
    bg = Image.open(frame_png).convert("RGBA")
    ov = Image.open(overlay_png).convert("RGBA")
    comp = Image.alpha_composite(bg, ov).convert("RGB")
    comp.save(out, quality=92)


if __name__ == "__main__":
    main()
