#!/usr/bin/env python3
"""Render the rev 2 c02 body-title preview per BODY-TREATMENT-LOCK.md rev 2 (11 Sep 2026).

Implements the two-layer build: bed (full-bleed gradient, layer 1) + plate
(bottom-left corner plane, layer 2) + mint rule + two-line stat lockup.

Outputs (into ./previews/):
  04-body-c02-backed-transparent.png — transparent 1920x1080 overlay
  04-body-c02-backed-preview.jpg      — overlay composited over a frame
                                          from timeline clip 002 (s02)

Lock: ../BODY-TREATMENT-LOCK.md rev 2 — §3.2 bed, §3.3 plate, §5 worked example,
  §7 do-not list. Copy verbatim from titles.md: "100,000+ square feet of gaming."
Break: "100,000+" / "square feet of gaming."  Variant S (stat lockup).

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
PREV = HERE / "previews"
TIMELINE = HERE.parent / "timeline"
FONTS = Path("/Users/janehaynie/Documents/Cursor Projects/luci-design/LUCI Systems Design System/assets/fonts")
PREV.mkdir(parents=True, exist_ok=True)

# ---- Canvas
W, H = 1920, 1080

# ---- Tokens (LOCK §2)
OFF_WHITE = (245, 248, 250)      # #F5F8FA
MINT = (104, 227, 190)           # #68E3BE
NAVY_DEEP = (10, 22, 28)         # #0A161C

FONT_SEMIBOLD = FONTS / "SpaceGrotesk-SemiBold.ttf"
FONT_MEDIUM = FONTS / "SpaceGrotesk-Medium.ttf"

# ---- Type block geometry (LOCK §3.1 + §5 worked example)
LEFT_X = 160
LAST_BASELINE_Y = 920    # line 2 (qualifier) baseline — the anchor
LINE1_BASELINE_Y = 868   # line 1 (numeral) baseline
RULE_X0, RULE_X1 = 160, 216     # 56px wide
RULE_Y0, RULE_Y1 = 747, 750     # 3px tall (rev 2)

# ---- Bed — full-bleed gradient (LOCK §3.2, layer 1)
BED_PEAK = 0.45
BED_TOP_Y = 380          # alpha 0.00 at this y
BED_BOTTOM_Y = 1080     # alpha BED_PEAK at this y
BED_H_FALLOFF_START = 980    # multiplier 1.00 up to here
BED_H_FALLOFF_END = 1920     # multiplier 0.30 at x=1920
BED_H_FALLOFF_END_MULT = 0.30

# ---- Plate — bottom-left corner plane (LOCK §3.3, layer 2)
PLATE_DENSITY = 0.62          # tunable band 0.50-0.74; hold 0.62 for c02 preview
PLATE_TOP_Y = 680             # variant S plate top edge
PLATE_FULL_DENSITY_X = 1024   # full density 0 -> 1024
PLATE_FALLOFF_END_X = 1536    # quadratic ease to 0.00 at x=1536
PLATE_FEATHER_PX = 8          # vertical feather at top edge (compression control)

# ---- Shadow (LOCK §3.1)
SHADOW_ALPHA = 0.50
SHADOW_OFFSET = (0, 3)
SHADOW_BLUR = 22

# ---- Copy (verbatim from titles.md)
LINE1_TEXT = "100,000+"               # numeral — SemiBold 128
LINE2_TEXT = "square feet of gaming."  # qualifier — Medium 40


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(str(c) for c in cmd[:4])}...\n{r.stderr[-1500:]}")
    return r


def _smoothstep(t):
    """Standard smoothstep: 0 at t=0, 1 at t=1, smooth derivative at endpoints."""
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def build_bed() -> Image.Image:
    """Full-bleed gradient bed (LOCK §3.2, layer 1).

    Vertical: alpha 0.00 @ y=380 -> 0.45 @ y=1080, quadratic ease.
    Horizontal: multiplier 1.00 to x=980 -> 0.30 at x=1920, quadratic ease.
    Full-bleed, no radius, no blur, no visible edge.
    """
    ys = np.arange(H, dtype=np.float32)
    v_alpha = np.zeros(H, dtype=np.float32)
    mask = ys >= BED_TOP_Y
    t_v = (ys[mask] - BED_TOP_Y) / (BED_BOTTOM_Y - BED_TOP_Y)
    v_alpha[mask] = BED_PEAK * (t_v * t_v)  # quadratic ease

    xs = np.arange(W, dtype=np.float32)
    h_mult = np.ones(W, dtype=np.float32)
    mask_h = xs > BED_H_FALLOFF_START
    t_h = (xs[mask_h] - BED_H_FALLOFF_START) / (BED_H_FALLOFF_END - BED_H_FALLOFF_START)
    h_mult[mask_h] = 1.0 - (1.0 - BED_H_FALLOFF_END_MULT) * (t_h * t_h)

    alpha_2d = v_alpha[:, None] * h_mult[None, :]  # (H, W)
    alpha_8 = np.clip(alpha_2d * 255.0, 0, 255).astype(np.uint8)

    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    rgba[..., 0] = NAVY_DEEP[0]
    rgba[..., 1] = NAVY_DEEP[1]
    rgba[..., 2] = NAVY_DEEP[2]
    rgba[..., 3] = alpha_8
    return Image.fromarray(rgba).convert("RGBA")


def build_plate() -> Image.Image:
    """Bottom-left corner plate (LOCK §3.3, layer 2).

    Flat #0A161C @ 0.62 composited over the bed.
    - Bleeds left (x=0) and bottom (y=1080); no edge drawn on either.
    - Top edge hard at y=680, radius 0, 8px vertical feather.
    - Full density to x=1024; quadratic ease 1.00 -> 0.00 over x=1024..1536.
    - Nothing right of x=1536.
    """
    ys = np.arange(H, dtype=np.float32)
    xs = np.arange(W, dtype=np.float32)

    # Vertical feather: smoothstep over 8px centered on PLATE_TOP_Y.
    # 0 above (PLATE_TOP_Y - 4), 1.0 below (PLATE_TOP_Y + 4).
    v_feather = _smoothstep((ys - (PLATE_TOP_Y - PLATE_FEATHER_PX / 2)) / PLATE_FEATHER_PX)

    # Horizontal falloff: 1.0 for x <= 1024; quadratic ease to 0.0 at x=1536; 0 beyond.
    h_mult = np.ones(W, dtype=np.float32)
    mask_falloff = (xs > PLATE_FULL_DENSITY_X) & (xs <= PLATE_FALLOFF_END_X)
    t_h = (xs[mask_falloff] - PLATE_FULL_DENSITY_X) / (PLATE_FALLOFF_END_X - PLATE_FULL_DENSITY_X)
    h_mult[mask_falloff] = 1.0 - (t_h * t_h)  # quadratic ease 1.00 -> 0.00
    h_mult[xs > PLATE_FALLOFF_END_X] = 0.0

    alpha_2d = PLATE_DENSITY * v_feather[:, None] * h_mult[None, :]
    alpha_8 = np.clip(alpha_2d * 255.0, 0, 255).astype(np.uint8)

    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    rgba[..., 0] = NAVY_DEEP[0]
    rgba[..., 1] = NAVY_DEEP[1]
    rgba[..., 2] = NAVY_DEEP[2]
    rgba[..., 3] = alpha_8
    return Image.fromarray(rgba).convert("RGBA")


def draw_text_with_shadow(canvas: Image.Image, text: str, font: ImageFont.FreeTypeFont,
                           baseline_xy: tuple[int, int], fill, tracking: float):
    """Draw text anchored at left-baseline, with soft shadow per LOCK §3.1."""
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    sd.text((baseline_xy[0] + SHADOW_OFFSET[0], baseline_xy[1] + SHADOW_OFFSET[1]),
            text, font=font, fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], 255),
            anchor="ls", tracking=tracking)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=SHADOW_BLUR))
    r, g, b, a = shadow_layer.split()
    a = a.point(lambda v: int(v * SHADOW_ALPHA))
    shadow_layer = Image.merge("RGBA", (r, g, b, a))

    canvas = Image.alpha_composite(canvas, shadow_layer)
    draw = ImageDraw.Draw(canvas)
    draw.text(baseline_xy, text, font=font, fill=fill, anchor="ls", tracking=tracking)
    return canvas


def render_backed_c02() -> Image.Image:
    """Render the rev 2 c02 overlay: bed + plate + mint rule + two-line stat lockup."""
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    # 1. Bed (layer 1) — full-bleed gradient, never omitted
    canvas = Image.alpha_composite(canvas, build_bed())

    # 2. Plate (layer 2) — bottom-left corner plane, composited over the bed
    canvas = Image.alpha_composite(canvas, build_plate())

    # 3. Mint rule (56x3, fully opaque) — the only graphic element
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([RULE_X0, RULE_Y0, RULE_X1 - 1, RULE_Y1 - 1],
                   fill=(MINT[0], MINT[1], MINT[2], 255))

    # 4. Line 1 — numeral: SemiBold 128, -0.03em, off-white 100%
    font1 = ImageFont.truetype(str(FONT_SEMIBOLD), 128)
    fill1 = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], 255)
    canvas = draw_text_with_shadow(canvas, LINE1_TEXT, font1,
                                   (LEFT_X, LINE1_BASELINE_Y), fill1, tracking=-3.84)

    # 5. Line 2 — qualifier: Medium 40, +0.02em, off-white 80%
    font2 = ImageFont.truetype(str(FONT_MEDIUM), 40)
    fill2 = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], int(round(255 * 0.80)))
    canvas = draw_text_with_shadow(canvas, LINE2_TEXT, font2,
                                   (LEFT_X, LAST_BASELINE_Y), fill2, tracking=0.80)

    return canvas


def grab_frame(clip: Path, ts: float, out: Path):
    """Extract one 1920x1080 frame at timestamp ts from clip."""
    run([
        "ffmpeg", "-y", "-ss", f"{ts:.3f}", "-i", str(clip),
        "-frames:v", "1", "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080",
        "-q:v", "2", str(out),
    ])


def composite(frame_png: Path, overlay_png: Path, out: Path):
    """Alpha-composite the transparent overlay onto the frame, save as JPG preview."""
    bg = Image.open(frame_png).convert("RGBA")
    ov = Image.open(overlay_png).convert("RGBA")
    comp = Image.alpha_composite(bg, ov).convert("RGB")
    comp.save(out, quality=92)


def main():
    # --- Transparent overlay (bed + plate + mint rule + type) ---
    p_overlay = PREV / "04-body-c02-backed-transparent.png"
    overlay = render_backed_c02()
    overlay.save(p_overlay)
    print(f"WROTE {p_overlay.name}  ({p_overlay.stat().st_size} bytes)")

    # --- Composite over a frame from timeline clip 002 (s02) ---
    # Title window 6.3-9.7s into the full cut; clip 001 is 6.0s, so the window
    # maps to ~0.3-3.7s into clip 002. Grab a frame near the middle (~2.0s).
    clip002 = TIMELINE / "002-s02-Casino 1-gaming-100k.mp4"
    frame002 = PREV / "_frame-002-s02-backed.png"
    grab_frame(clip002, 2.0, frame002)
    prev_c02 = PREV / "04-body-c02-backed-preview.jpg"
    composite(frame002, p_overlay, prev_c02)
    print(f"WROTE {prev_c02.name}  ({prev_c02.stat().st_size} bytes)")

    # --- Clean up intermediate frame ---
    if frame002.exists():
        frame002.unlink()

    print("\nDONE. Rev 2 backed c02 preview files in:")
    print(f"  {PREV}")


if __name__ == "__main__":
    main()
