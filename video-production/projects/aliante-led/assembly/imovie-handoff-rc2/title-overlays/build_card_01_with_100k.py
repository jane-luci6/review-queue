#!/usr/bin/env python3
"""Render one-off card: "With 100,000+ square feet of gaming,"

Implements BODY-TREATMENT-LOCK.md rev 2 (11 Sep 2026) — the two-layer build
(bed + plate) + mint rule + two-line lockup. S-class plate geometry.

This is a one-off card (not part of the c02–c19 sequence in titles.md). It
lives in cards/ — separate from previews/ which holds the c02 series.

Jane's type note for THIS card (overrides the old S qualifier being too quiet):
  - "100,000+" must be LARGER — SemiBold, display scale (same spirit as the
    approved S numeral at 128).
  - The rest must be READABLE — not the old 40px @ 80% whisper. Medium ~52,
    ~95% opacity for "With" and "square feet of gaming,".
  - Layout: two lines. Line 1 mixes "With" (Medium 52) + "100,000+" (SemiBold
    128) on a shared baseline. Line 2 "square feet of gaming," (Medium 52).
  - Copy verbatim, trailing comma preserved: "With 100,000+ square feet of gaming,"

Outputs (into ./cards/):
  card-01-with-100k-transparent.png — transparent 1920x1080 overlay
  card-01-with-100k-preview.jpg      — overlay composited over a frame
                                        from timeline clip 002 (s02)

Lock: ../BODY-TREATMENT-LOCK.md rev 2 — §3.2 bed, §3.3 plate, §5 worked example,
  §7 do-not list. S-class plate geometry (top edge y=680).
Composite order: footage -> bed -> plate -> mint rule -> type (with shadow).
Never ship the plate without the bed. No pill, no radius, no centered text,
no soft_dark_backing, no second ornament.
"""
from __future__ import annotations
import subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---- Paths
HERE = Path(__file__).resolve().parent
CARDS = HERE / "cards"
TIMELINE = HERE.parent / "timeline"
FONTS = Path("/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/assets/fonts")
CARDS.mkdir(parents=True, exist_ok=True)

# ---- Canvas
W, H = 1920, 1080

# ---- Tokens (LOCK §2)
OFF_WHITE = (245, 248, 250)      # #F5F8FA
MINT = (104, 227, 190)           # #68E3BE
NAVY_DEEP = (10, 22, 28)         # #0A161C

FONT_SEMIBOLD = FONTS / "SpaceGrotesk-SemiBold.ttf"
FONT_MEDIUM = FONTS / "SpaceGrotesk-Medium.ttf"

# ---- Type block geometry (LOCK §3.1 + §5, S-class)
LEFT_X = 160
LAST_BASELINE_Y = 920    # line 2 baseline — the anchor
LINE1_BASELINE_Y = 868   # line 1 baseline (numeral + "With")
RULE_X0, RULE_X1 = 160, 216     # 56px wide
RULE_Y0, RULE_Y1 = 747, 750     # 3px tall (rev 2)

# ---- Bed — full-bleed gradient (LOCK §3.2, layer 1)
BED_PEAK = 0.45
BED_TOP_Y = 380
BED_BOTTOM_Y = 1080
BED_H_FALLOFF_START = 980
BED_H_FALLOFF_END = 1920
BED_H_FALLOFF_END_MULT = 0.30

# ---- Plate — bottom-left corner plane (LOCK §3.3, layer 2) — S-class
PLATE_DENSITY = 0.62
PLATE_TOP_Y = 680             # S-class plate top edge
PLATE_FULL_DENSITY_X = 1024
PLATE_FALLOFF_END_X = 1536
PLATE_FEATHER_PX = 8

# ---- Shadow (LOCK §3.1)
SHADOW_ALPHA = 0.50
SHADOW_OFFSET = (0, 3)
SHADOW_BLUR = 22

# ---- Copy (verbatim — Jane's new line, trailing comma)
WITH_TEXT = "With"                    # Medium 52, 95% opacity
NUMERAL_TEXT = "100,000+"             # SemiBold 128, 100% opacity
QUALIFIER_TEXT = "square feet of gaming,"  # Medium 52, 95% opacity (trailing comma)

# ---- Type sizes for this card (Jane's note: numeral large, rest readable)
NUMERAL_SIZE = 128      # SemiBold — display scale, same spirit as approved S
MEDIUM_SIZE = 52        # Medium — readable, not the old 40px whisper
MEDIUM_OPACITY = 0.95   # ~90-100%, clearly readable, slightly subordinate

# ---- Tracking
NUMERAL_TRACKING = -3.84    # -0.03em at 128px
MEDIUM_TRACKING = 0.52      # +0.01em at 52px


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(str(c) for c in cmd[:4])}...\n{r.stderr[-1500:]}")
    return r


def _smoothstep(t):
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def build_bed() -> Image.Image:
    """Full-bleed gradient bed (LOCK §3.2, layer 1)."""
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


def build_plate() -> Image.Image:
    """Bottom-left corner plate (LOCK §3.3, layer 2) — S-class geometry."""
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


def _text_width(font: ImageFont.FreeTypeFont, text: str, tracking: float) -> int:
    """Measure rendered text width including tracking adjustment."""
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    # tracking is in px-per-char (em * size); add for inter-character gaps
    if len(text) > 1:
        w += int(round(tracking * (len(text) - 1)))
    return w


def draw_line1_mixed(canvas: Image.Image) -> Image.Image:
    """Line 1: 'With' (Medium 52, 95%) + '100,000+' (SemiBold 128, 100%), shared baseline.

    Both pieces anchored at left-baseline ('ls'); 'With' drawn first at x=160,
    then '100,000+' starts after 'With ' + a natural space gap.
    """
    font_med = ImageFont.truetype(str(FONT_MEDIUM), MEDIUM_SIZE)
    font_semibold = ImageFont.truetype(str(FONT_SEMIBOLD), NUMERAL_SIZE)

    fill_med = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], int(round(255 * MEDIUM_OPACITY)))
    fill_num = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], 255)

    # Measure "With" in Medium to find where "100,000+" starts
    with_w = _text_width(font_med, WITH_TEXT, MEDIUM_TRACKING)
    # Natural space in Medium 52 (~14px) + a small extra gap so the numeral breathes
    space_w = _text_width(font_med, " ", 0)
    gap_extra = 10  # px — slight breathing room before the large numeral
    numeral_x = LEFT_X + with_w + space_w + gap_extra

    # --- Shadow layer for both pieces ---
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    sd.text((LEFT_X + SHADOW_OFFSET[0], LINE1_BASELINE_Y + SHADOW_OFFSET[1]),
            WITH_TEXT, font=font_med,
            fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], 255),
            anchor="ls", tracking=MEDIUM_TRACKING)
    sd.text((numeral_x + SHADOW_OFFSET[0], LINE1_BASELINE_Y + SHADOW_OFFSET[1]),
            NUMERAL_TEXT, font=font_semibold,
            fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], 255),
            anchor="ls", tracking=NUMERAL_TRACKING)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=SHADOW_BLUR))
    r, g, b, a = shadow_layer.split()
    a = a.point(lambda v: int(v * SHADOW_ALPHA))
    shadow_layer = Image.merge("RGBA", (r, g, b, a))
    canvas = Image.alpha_composite(canvas, shadow_layer)

    # --- Actual text ---
    draw = ImageDraw.Draw(canvas)
    draw.text((LEFT_X, LINE1_BASELINE_Y), WITH_TEXT, font=font_med,
              fill=fill_med, anchor="ls", tracking=MEDIUM_TRACKING)
    draw.text((numeral_x, LINE1_BASELINE_Y), NUMERAL_TEXT, font=font_semibold,
              fill=fill_num, anchor="ls", tracking=NUMERAL_TRACKING)
    return canvas


def draw_line2(canvas: Image.Image) -> Image.Image:
    """Line 2: 'square feet of gaming,' (Medium 52, 95%), baseline y=920."""
    font_med = ImageFont.truetype(str(FONT_MEDIUM), MEDIUM_SIZE)
    fill = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], int(round(255 * MEDIUM_OPACITY)))

    # Shadow
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    sd.text((LEFT_X + SHADOW_OFFSET[0], LAST_BASELINE_Y + SHADOW_OFFSET[1]),
            QUALIFIER_TEXT, font=font_med,
            fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], 255),
            anchor="ls", tracking=MEDIUM_TRACKING)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=SHADOW_BLUR))
    r, g, b, a = shadow_layer.split()
    a = a.point(lambda v: int(v * SHADOW_ALPHA))
    shadow_layer = Image.merge("RGBA", (r, g, b, a))
    canvas = Image.alpha_composite(canvas, shadow_layer)

    draw = ImageDraw.Draw(canvas)
    draw.text((LEFT_X, LAST_BASELINE_Y), QUALIFIER_TEXT, font=font_med,
              fill=fill, anchor="ls", tracking=MEDIUM_TRACKING)
    return canvas


def render_card() -> Image.Image:
    """Render the one-off card overlay: bed + plate + mint rule + two-line lockup."""
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    # 1. Bed (layer 1)
    canvas = Image.alpha_composite(canvas, build_bed())

    # 2. Plate (layer 2) — S-class
    canvas = Image.alpha_composite(canvas, build_plate())

    # 3. Mint rule (56x3, fully opaque)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([RULE_X0, RULE_Y0, RULE_X1 - 1, RULE_Y1 - 1],
                   fill=(MINT[0], MINT[1], MINT[2], 255))

    # 4. Line 1 — "With" (Medium 52, 95%) + "100,000+" (SemiBold 128, 100%)
    canvas = draw_line1_mixed(canvas)

    # 5. Line 2 — "square feet of gaming," (Medium 52, 95%)
    canvas = draw_line2(canvas)

    return canvas


def grab_frame(clip: Path, ts: float, out: Path):
    run([
        "ffmpeg", "-y", "-ss", f"{ts:.3f}", "-i", str(clip),
        "-frames:v", "1", "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-q:v", "2", str(out),
    ])


def composite(frame_png: Path, overlay_png: Path, out: Path):
    bg = Image.open(frame_png).convert("RGBA")
    ov = Image.open(overlay_png).convert("RGBA")
    comp = Image.alpha_composite(bg, ov).convert("RGB")
    comp.save(out, quality=92)


def main():
    # --- Transparent overlay ---
    p_overlay = CARDS / "card-01-with-100k-transparent.png"
    overlay = render_card()
    overlay.save(p_overlay)
    print(f"WROTE {p_overlay.name}  ({p_overlay.stat().st_size} bytes)")

    # --- Measure and report line widths (verify inside measure 864) ---
    font_med = ImageFont.truetype(str(FONT_MEDIUM), MEDIUM_SIZE)
    font_semibold = ImageFont.truetype(str(FONT_SEMIBOLD), NUMERAL_SIZE)
    with_w = _text_width(font_med, WITH_TEXT, MEDIUM_TRACKING)
    space_w = _text_width(font_med, " ", 0)
    numeral_w = _text_width(font_semibold, NUMERAL_TEXT, NUMERAL_TRACKING)
    line1_right = LEFT_X + with_w + space_w + 10 + numeral_w
    line2_w = _text_width(font_med, QUALIFIER_TEXT, MEDIUM_TRACKING)
    line2_right = LEFT_X + line2_w
    print(f"  line 1: 'With' w={with_w} + space {space_w} + gap 10 + '100,000+' w={numeral_w} -> right x={line1_right} (limit 1024)")
    print(f"  line 2: 'square feet of gaming,' w={line2_w} -> right x={line2_right} (limit 1024)")

    # --- Composite over a frame from timeline clip 002 (s02) ---
    clip002 = TIMELINE / "002-s02-Casino 1-gaming-100k.mp4"
    frame002 = CARDS / "_frame-002-s02-card01.png"
    grab_frame(clip002, 2.0, frame002)
    prev = CARDS / "card-01-with-100k-preview.jpg"
    composite(frame002, p_overlay, prev)
    print(f"WROTE {prev.name}  ({prev.stat().st_size} bytes)")

    # --- Clean up intermediate frame ---
    if frame002.exists():
        frame002.unlink()

    print("\nDONE. One-off card files in:")
    print(f"  {CARDS}")


if __name__ == "__main__":
    main()
