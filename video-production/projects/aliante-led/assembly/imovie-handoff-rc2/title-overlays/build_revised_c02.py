#!/usr/bin/env python3
"""Render the revised c02 body-title preview per BODY-TREATMENT-LOCK.md (Claude lock, 11 Sep 2026).

Outputs (into ./previews/):
  03-body-c02-revised-transparent.png — transparent 1920×1080 overlay (scrim + mint rule + text)
  03-body-c02-revised-preview.jpg    — overlay composited over a frame from timeline clip 002

Lock: ../BODY-TREATMENT-LOCK.md
  - Variant S (stat lockup): numeral SemiBold 128 / qualifier Medium 40 @ 80%
  - Left anchor x=160; last baseline y=920; line 1 baseline y=867
  - Mint rule 56×3 at x=160→216, y=744→747
  - Scrim: #0A161C, alpha 0.00 @ y=430 → 0.62 @ y=1080, quadratic ease; horizontal falloff 1.00 → 0.35 at x=1920
  - Shadow: #0A161C @ 50%, offset (0,3), blur 22
  - No pill, no radius, no centered text, no soft_dark_backing

Copy verbatim from titles.md: "100,000+ square feet of gaming."
Break: "100,000+" / "square feet of gaming."
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

# ---- Tokens (from BODY-TREATMENT-LOCK.md §2)
OFF_WHITE = (245, 248, 250)      # #F5F8FA
MINT = (104, 227, 190)           # #68E3BE
NAVY_DEEP = (10, 22, 28)         # #0A161C

FONT_SEMIBOLD = FONTS / "SpaceGrotesk-SemiBold.ttf"
FONT_MEDIUM = FONTS / "SpaceGrotesk-Medium.ttf"

# ---- Lock geometry (from §3 and §5 worked example)
LEFT_X = 160
LAST_BASELINE_Y = 920    # line 2 (qualifier) baseline — the anchor
LINE1_BASELINE_Y = 867   # line 1 (numeral) baseline
RULE_X0, RULE_X1 = 160, 216     # 56px wide
RULE_Y0, RULE_Y1 = 744, 747     # 3px tall

# Scrim
SCRIM_PEAK = 0.62
SCRIM_TOP_Y = 430        # alpha 0.00 at this y
SCRIM_BOTTOM_Y = 1080    # alpha SCRIM_PEAK at this y
SCRIM_H_FALLOFF_START = 980    # multiplier 1.00 up to here
SCRIM_H_FALLOFF_END = 1920     # multiplier 0.35 at x=1920
SCRIM_H_FALLOFF_END_MULT = 0.35

# Shadow
SHADOW_ALPHA = 0.50
SHADOW_OFFSET = (0, 3)
SHADOW_BLUR = 22

# Copy (verbatim from titles.md)
LINE1_TEXT = "100,000+"              # numeral — SemiBold 128
LINE2_TEXT = "square feet of gaming."  # qualifier — Medium 40


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(str(c) for c in cmd[:4])}...\n{r.stderr[-1500:]}")
    return r


def build_scrim() -> Image.Image:
    """Full-bleed gradient scrim per §3.

    Vertical: alpha 0.00 @ y=430 → 0.62 @ y=1080, quadratic ease.
    Horizontal: multiplier 1.00 to x=980 → 0.35 at x=1920, quadratic ease.
    Returns an RGBA Image. No radius, no blur, no visible edge.
    """
    ys = np.arange(H, dtype=np.float32)
    v_alpha = np.zeros(H, dtype=np.float32)
    mask = ys >= SCRIM_TOP_Y
    t_v = (ys[mask] - SCRIM_TOP_Y) / (SCRIM_BOTTOM_Y - SCRIM_TOP_Y)
    v_alpha[mask] = SCRIM_PEAK * (t_v * t_v)  # quadratic ease

    xs = np.arange(W, dtype=np.float32)
    h_mult = np.ones(W, dtype=np.float32)
    mask_h = xs > SCRIM_H_FALLOFF_START
    t_h = (xs[mask_h] - SCRIM_H_FALLOFF_START) / (SCRIM_H_FALLOFF_END - SCRIM_H_FALLOFF_START)
    h_mult[mask_h] = 1.0 - (1.0 - SCRIM_H_FALLOFF_END_MULT) * (t_h * t_h)

    alpha_2d = v_alpha[:, None] * h_mult[None, :]  # (H, W)
    alpha_8 = np.clip(alpha_2d * 255.0, 0, 255).astype(np.uint8)

    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    rgba[..., 0] = NAVY_DEEP[0]
    rgba[..., 1] = NAVY_DEEP[1]
    rgba[..., 2] = NAVY_DEEP[2]
    rgba[..., 3] = alpha_8
    img = Image.fromarray(rgba)
    return img.convert("RGBA")


def draw_text_with_shadow(canvas: Image.Image, text: str, font: ImageFont.FreeTypeFont,
                          baseline_xy: tuple[int, int], fill, tracking: float):
    """Draw text anchored at left-baseline, with soft shadow per §3."""
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    sd.text((baseline_xy[0] + SHADOW_OFFSET[0], baseline_xy[1] + SHADOW_OFFSET[1]),
            text, font=font, fill=(NAVY_DEEP[0], NAVY_DEEP[1], NAVY_DEEP[2], 255),
            anchor="ls", tracking=tracking)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=SHADOW_BLUR))
    # scale shadow alpha to 50%
    r, g, b, a = shadow_layer.split()
    a = a.point(lambda v: int(v * SHADOW_ALPHA))
    shadow_layer = Image.merge("RGBA", (r, g, b, a))

    canvas = Image.alpha_composite(canvas, shadow_layer)
    draw = ImageDraw.Draw(canvas)
    draw.text(baseline_xy, text, font=font, fill=fill, anchor="ls", tracking=tracking)
    return canvas


def render_revised_c02() -> Image.Image:
    """Render the revised c02 overlay: scrim + mint rule + two-line stat lockup."""
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    # 1. Scrim (full-bleed gradient, no edges)
    canvas = Image.alpha_composite(canvas, build_scrim())

    # 2. Mint rule (56×3, fully opaque)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([RULE_X0, RULE_Y0, RULE_X1 - 1, RULE_Y1 - 1],
                   fill=(MINT[0], MINT[1], MINT[2], 255))

    # 3. Line 1 — numeral: SemiBold 128, -0.03em, off-white 100%
    font1 = ImageFont.truetype(str(FONT_SEMIBOLD), 128)
    fill1 = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], 255)
    canvas = draw_text_with_shadow(canvas, LINE1_TEXT, font1,
                                   (LEFT_X, LINE1_BASELINE_Y), fill1, tracking=-3.84)

    # 4. Line 2 — qualifier: Medium 40, +0.02em, off-white 80%
    font2 = ImageFont.truetype(str(FONT_MEDIUM), 40)
    fill2 = (OFF_WHITE[0], OFF_WHITE[1], OFF_WHITE[2], int(round(255 * 0.80)))
    canvas = draw_text_with_shadow(canvas, LINE2_TEXT, font2,
                                   (LEFT_X, LAST_BASELINE_Y), fill2, tracking=0.80)

    return canvas


def grab_frame(clip: Path, ts: float, out: Path):
    """Extract one 1920×1080 frame at timestamp ts from clip."""
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
    # --- Transparent overlay ---
    p_overlay = PREV / "03-body-c02-revised-transparent.png"
    overlay = render_revised_c02()
    overlay.save(p_overlay)
    print(f"WROTE {p_overlay.name}  ({p_overlay.stat().st_size} bytes)")

    # --- Composite over a frame from timeline clip 002 (s02) ---
    clip002 = TIMELINE / "002-s02-Casino 1-gaming-100k.mp4"
    frame002 = PREV / "_frame-002-s02-revised.png"
    grab_frame(clip002, 2.0, frame002)
    prev_c02 = PREV / "03-body-c02-revised-preview.jpg"
    composite(frame002, p_overlay, prev_c02)
    print(f"WROTE {prev_c02.name}  ({prev_c02.stat().st_size} bytes)")

    # --- Clean up intermediate frame ---
    if frame002.exists():
        frame002.unlink()

    print("\nDONE. Revised c02 preview files in:")
    print(f"  {PREV}")


if __name__ == "__main__":
    main()
