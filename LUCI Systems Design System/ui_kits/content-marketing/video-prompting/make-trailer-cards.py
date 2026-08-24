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


MAX_TEXT_W = 1520  # keep type off the edges at 1920 wide


def fit_size(draw, lines, size, tracking):
    """Shrink until the longest line clears MAX_TEXT_W."""
    while size > 24:
        font = ImageFont.truetype(str(SG), size)
        widest = max(tracked_width(draw, ln, font, tracking) for ln in lines)
        if widest <= MAX_TEXT_W:
            return size
        size -= 2
    return size


def statement(path, lines, size=56, tracking=4.0, accent_last=False):
    """Standard trailer card: mint rule, then one or two lines of tracked type."""
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    size = fit_size(d, lines, size, tracking)
    font = ImageFont.truetype(str(SG), size)

    line_gap = int(size * 1.34)
    block_h = line_gap * (len(lines) - 1)
    first_cy = BAND_MID - block_h / 2 + 14

    rule(d, first_cy - size * 0.95)
    for i, ln in enumerate(lines):
        last = i == len(lines) - 1
        color = MINT if (accent_last and last) else OFF_WHITE
        draw_tracked(d, ln, font, tracking, first_cy + i * line_gap, color)

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


# Classic trailer-narrator structure, five movements:
#   I   THE WORLD      three escalating "where" clauses (rule of three)
#   II  THE HERO       the refusal, then the call
#   III THE ODDS       impossible, then the escalation — lines get shorter
#   IV  THE PAYOFF     after the silence
#   V   THE TAG        CTA + logo
# Line length is the pacing device: long in I and II, clipped in III.
CARDS = {
    # --- I. the world ---
    "c1": (["IN A WORLD WHERE A SPORTSBOOK",
            "LIVES OR DIES BY THE WALL IN FRONT OF IT\u2026"], 48, 3.0),
    "c2": (["WHERE THE COMPETITION NEVER SLEEPS\u2026"], 50, 3.6),
    "c3": (["AND GUEST EXPECTATIONS",
            "HAVE NEVER BEEN HIGHER\u2026"], 52, 3.6),

    # --- II. the hero ---
    "c4": (["ONE CASINO REFUSED TO SETTLE FOR SECOND BEST."], 48, 3.0),
    "c5": (["SO THEY CALLED THE ONLY TEAM",
            "THAT COULD BUILD IT."], 52, 3.6),

    # --- III. the odds (short, accelerating) ---
    "c6": (["IT LOOKED IMPOSSIBLE."], 66, 5.6),
    "c7": (["LUCI SHOWED UP ANYWAY."], 66, 5.6),
    "c8": (["ONE 2,000-SQUARE-FOOT WALL."], 58, 4.4),
    "c9": (["TWENTY-FOUR ZONES."], 66, 5.6),
    "c10": (["SIX LAYOUTS."], 72, 6.4),
    "c11": (["ONE TEAM THAT WOULDN\u2019T STOP",
             "UNTIL THE JOB WAS DONE."], 54, 3.8),

    # --- IV. the payoff ---
    "c12": (["LUCI BROKE EVERY EXPECTATION."], 58, 4.4),
    "c13": (["AND BUILT ONE OF THE BIGGEST LED WALLS",
             "IN THE KNOWN UNIVERSE."], 48, 3.0),

    # --- V. the tag ---
    "c14": (["COME SEE HOW THEY DID IT.", "ALIANTE CASINO"], 54, 4.0, True),
    "end2": (["ONE PROPERTY.   ONE INTERFACE."], 50, 4.0),
}


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/aliante-trailer-build/cards")
    out.mkdir(parents=True, exist_ok=True)

    for key, spec in CARDS.items():
        lines, size, tracking = spec[0], spec[1], spec[2]
        accent_last = spec[3] if len(spec) > 3 else False
        statement(out / f"card_{key}.png", lines, size, tracking, accent_last)
    end_logo(out / "card_end1.png")

    print(f"wrote {len(CARDS) + 1} cards to {out}")


if __name__ == "__main__":
    main()
