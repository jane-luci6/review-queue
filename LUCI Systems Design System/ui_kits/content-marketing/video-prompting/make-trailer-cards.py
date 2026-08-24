#!/usr/bin/env python3
"""Render the Aliante trailer title cards as 1920x1080 PNGs.

This ffmpeg build has no drawtext filter, and rendering the cards here gives us
real letter-spacing control, which the tracked trailer type needs.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONTS = Path(
    "/Users/janehaynie/Documents/Cursor Projects/luci-design/"
    "LUCI Systems Design System/fonts"
)
SG = FONTS / "SpaceGrotesk-Bold.ttf"
SYN = FONTS / "Syncopate-Bold.ttf"

W, H = 1920, 1080
MINT = (104, 227, 190)
OFF_WHITE = (245, 248, 250)
BLACK = (0, 0, 0)

# 2.39:1 active band inside the 1080 frame — keep type inside it.
BAND_TOP, BAND_H = 138, 804
BAND_MID = BAND_TOP + BAND_H // 2


def tracked_width(draw, text, font, tracking):
    w = sum(draw.textlength(ch, font=font) for ch in text)
    return w + tracking * max(len(text) - 1, 0)


def draw_tracked(draw, text, font, tracking, cy, color):
    """Draw letter-spaced text centered horizontally at vertical center cy."""
    total = tracked_width(draw, text, font, tracking)
    x = (W - total) / 2
    ascent, descent = font.getmetrics()
    y = cy - (ascent + descent) / 2
    for ch in text:
        draw.text((x, y), ch, font=font, fill=color)
        x += draw.textlength(ch, font=font) + tracking


def rule(draw, cy, width=80, thickness=3, color=MINT):
    x0 = (W - width) / 2
    draw.rectangle([x0, cy, x0 + width, cy + thickness], fill=color)


def statement(path, lines, size=56, tracking=4.0):
    """Standard trailer card: mint rule, then one or two lines of tracked type."""
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(SG), size)

    line_gap = int(size * 1.34)
    block_h = line_gap * (len(lines) - 1)
    first_cy = BAND_MID - block_h / 2 + 14

    rule(d, first_cy - size * 0.95)
    for i, ln in enumerate(lines):
        draw_tracked(d, ln, font, tracking, first_cy + i * line_gap, OFF_WHITE)

    img.save(path)
    return path


def end_logo(path):
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)

    # "LUCI" is a single display word — Syncopate is correct here.
    f_luci = ImageFont.truetype(str(SYN), 84)
    draw_tracked(d, "LUCI", f_luci, 26.0, BAND_MID - 46, OFF_WHITE)

    rule(d, BAND_MID + 34)

    f_tag = ImageFont.truetype(str(SG), 24)
    draw_tracked(
        d,
        "THE ORCHESTRATION ENGINE FOR ENTERPRISE MULTIMEDIA",
        f_tag,
        5.2,
        BAND_MID + 86,
        MINT,
    )
    img.save(path)
    return path


CARDS = {
    "a": (["IN A WORLD WHERE EVERY SCREEN", "ANSWERS TO A DIFFERENT MASTER"], 52, 3.6),
    "b": (["ONE CREW.", "ONE CURVED WALL."], 62, 5.0),
    "c": (["SIX RUNS TO EVERY NODE."], 58, 4.4),
    "d": (["TWENTY-FOUR ZONES."], 62, 5.0),
    "e": (["ONE CANVAS."], 68, 6.0),
    "f": (["HUNDREDS OF A/V ENDPOINTS."], 56, 4.2),
    "g": (["ONE INTERFACE."], 68, 6.0),
    "end2": (["ONE PROPERTY.   ONE INTERFACE."], 50, 4.0),
}


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/aliante-trailer-build/cards")
    out.mkdir(parents=True, exist_ok=True)

    for key, (lines, size, tracking) in CARDS.items():
        statement(out / f"card_{key}.png", lines, size, tracking)
    end_logo(out / "card_end1.png")

    print(f"wrote {len(CARDS) + 1} cards to {out}")


if __name__ == "__main__":
    main()
