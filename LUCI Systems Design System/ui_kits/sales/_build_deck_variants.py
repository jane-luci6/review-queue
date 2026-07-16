"""Rebuild sales-deck diagram variants from their canonical SVGs.

The deck references cropped/enlarged ".deck.svg" variants of two canonical
diagrams (what-luci-is, embedded-operation-orbit). These had drifted because
there was no build step: they were produced once and not maintained as the
canonicals evolved. This script derives them from the current canonical each
run so they stay in sync.

what-luci-is: crop to the LUCI+Systems duo, enlarge fonts, NO extra depth
(matches the canonical -- the deck's former mint glow + extra soft shadows
were dropped per the flat direction).

Run:  python3 ui_kits/sales/_build_deck_variants.py
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DIAG = ROOT / "assets" / "diagrams"


def _apply(svg: str, reps: list[tuple[str, str]]) -> str:
    for old, new in reps:
        if old not in svg:
            sys.exit(f"!! pattern not found: {old[:80]!r}")
        svg = svg.replace(old, new, 1)
    return svg


def build_what_luci_is() -> None:
    canon = (DIAG / "luci-what-luci-is.svg").read_text()
    deck = _apply(canon, [
        # crop viewBox to the LUCI + Systems duo
        ('viewBox="0 0 900 460"', 'viewBox="4 0 596 312"'),
        # enlarge fonts for slide scale
        ('.nm { font-weight:700; font-size:26px; letter-spacing:-.01em; fill:#10232D; text-anchor:middle; }',
         '.nm { font-weight:700; font-size:32px; letter-spacing:-.01em; fill:#10232D; text-anchor:middle; }'),
        ('.rl { font-weight:700; font-size:11.5px; letter-spacing:.14em; fill:#2b9e80; text-anchor:middle; }',
         '.rl { font-weight:700; font-size:14px; letter-spacing:.05em; fill:#2b9e80; text-anchor:middle; }'),
        ('.sub { font-weight:400; font-size:13px; letter-spacing:.01em; fill:#8294A0; text-anchor:middle; }',
         '.sub { font-weight:400; font-size:11px; letter-spacing:.01em; fill:#8294A0; text-anchor:middle; }'),
        # nudge labels for the enlarged fonts
        ('<text class="nm" x="177" y="248">LUCI</text>',
         '<text class="nm" x="177" y="250">LUCI</text>'),
        ('<text class="rl" x="177" y="273">THE ORCHESTRATION PLATFORM</text>',
         '<text class="rl" x="177" y="274">THE ORCHESTRATION PLATFORM</text>'),
        ('<text class="sub" x="177" y="293">Software &amp; minimal hardware</text>',
         '<text class="sub" x="177" y="298">Software &amp; minimal hardware</text>'),
        ('<text class="nm" x="462" y="248">Systems</text>',
         '<text class="nm" x="462" y="250">Systems</text>'),
        ('<text class="rl" x="462" y="273">THE EMBEDDED OPERATION</text>',
         '<text class="rl" x="462" y="274">THE EMBEDDED OPERATION</text>'),
        ('<text class="sub" x="462" y="293">Our team, processes, and standards</text>',
         '<text class="sub" x="462" y="298">Our team, processes, and standards</text>'),
    ])
    out = DIAG / "luci-what-luci-is.deck.svg"
    out.write_text(deck)
    print(f"built {out.name} ({len(deck)} bytes) from canonical -- flat, no extra depth")


if __name__ == "__main__":
    build_what_luci_is()
