#!/usr/bin/env python3
"""Apply PDF-export HTML fixes to sales document templates."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SALES = ROOT / "ui_kits" / "sales"

LOGO_BLACK = "assets/logos/luci-wordmark-black-320.png"
LOGO_WHITE = "assets/logos/luci-wordmark-white-320.png"
PARAGON_LOGO = "assets/logos/paragon-casino-resort-print.png"

DEFAULT_FILES = [
    SALES / "capabilities-document.html",
    SALES / "paragon-capabilities.html",
    SALES / "_template-sales-document.html",
    SALES / "budgetary-estimate.html",
    SALES / "brochure.html",
    SALES / "field-activation-guide.html",
]

LOGO_SLOTS = [
    ("doc-opener-hero__logo", LOGO_WHITE),
    ("doc-close__logo", LOGO_WHITE),
    ("cap-opener-hero__logo", LOGO_WHITE),
    ("cap-close__logo", LOGO_WHITE),
]

SVG_TO_JPG = [
    ("assets/diagrams/luci-what-luci-is.svg", "assets/diagrams/luci-what-luci-is.jpg"),
    ("assets/diagrams/embedded-operation-orbit-names.svg", "assets/diagrams/embedded-operation-orbit-names.png"),
    ("../../assets/diagrams/embedded-operation-orbit-names.svg", "assets/diagrams/embedded-operation-orbit-names.png"),
    ("assets/case-relocation.svg", "assets/case-relocation.jpg"),
    ("assets/features/feature-map-dashboard.svg", "assets/features/feature-map-dashboard.jpg"),
    ("assets/features/feature-open-integration.svg", "assets/features/feature-open-integration.jpg"),
    ("assets/features/feature-pin-control.svg", "assets/features/feature-pin-control.jpg"),
    ("assets/features/feature-monitoring.svg", "assets/features/feature-monitoring.jpg"),
    ("assets/features/feature-presets.svg", "assets/features/feature-presets.jpg"),
    ("assets/features/feature-automation.svg", "assets/features/feature-automation.jpg"),
    ("assets/diagrams/luci-consolidation-ledger.svg", "assets/diagrams/luci-consolidation-ledger.jpg"),
    ("../../assets/diagrams/embedded-operation-orbit.svg", "assets/diagrams/embedded-operation-orbit.jpg"),
    ("assets/diagrams/embedded-operation-orbit.svg", "assets/diagrams/embedded-operation-orbit.jpg"),
]


def replace_logo_src(html: str, class_name: str, file_src: str) -> str:
    html = re.sub(
        rf'<img class="{class_name}" src="(?:data:image/[^"]+|[^"]*"iVBORw0KGgo[^"]*|(?:\.\./)*assets/logos/[^"]+)" alt=',
        f'<img class="{class_name}" src="{file_src}" alt=',
        html,
        count=1,
    )
    return html


def patch(html: str, *, paragon: bool = False, budgetary: bool = False, fag_prospect: bool = False) -> str:
    out = html
    out = re.sub(r"<style data-luci-fonts>[\s\S]*?</style>\s*", "", out, count=1)
    out = re.sub(
        r"\s*<link rel=\"preconnect\" href=\"https://fonts\.googleapis\.com\">\s*"
        r"<link rel=\"preconnect\" href=\"https://fonts\.gstatic\.com\" crossorigin>\s*"
        r"<link href=\"https://fonts\.googleapis\.com/css2[^\"]+\" rel=\"stylesheet\">\s*",
        "\n  <!-- Google Fonts removed for PDF export — use luci-brand-fonts.css (static Inter). -->\n  ",
        out,
        count=1,
    )
    for class_name, file_src in LOGO_SLOTS:
        out = replace_logo_src(out, class_name, file_src)
    # Cover logo: white on dark covers, black on light covers (brochure/budgetary/FAG-print
    # covers are light; scope-of-work and FAG-prospect covers are dark).
    cover_match = re.search(r'class="([^"]*\bdoc-page--cover\b[^"]*)"', out)
    cover_is_dark = bool(cover_match and 'doc-page--dark' in cover_match.group(1))
    out = replace_logo_src(out, 'doc-cover__logo', LOGO_WHITE if cover_is_dark else LOGO_BLACK)
    for svg, jpg in SVG_TO_JPG:
        out = out.replace(f'src="{svg}', f'src="{jpg}')
    out = out.replace(
        'src="../../assets/logos/ameristar-council-bluffs.svg',
        'src="assets/logos/ameristar-council-bluffs.jpg',
    )
    out = out.replace(
        'src="assets/diagrams/luci-system-architecture.png',
        'src="assets/diagrams/luci-system-architecture.jpg',
    )
    out = out.replace(
        'src="../../assets/diagrams/luci-system-architecture.png',
        'src="assets/diagrams/luci-system-architecture.jpg',
    )
    out = re.sub(
        r'(<img src="assets/client-logo-02\.(?:png|jpg)"[^>]*?)width="(?:5248|1400)" height="(?:424|113)"',
        r'\1width="1000" height="81"',
        out,
    )
    out = out.replace('src="assets/client-logo-02.png"', 'src="assets/client-logo-02.jpg"')
    out = out.replace('src="assets/interface-floor-view.png', 'src="assets/interface-floor-view.jpg')
    if 'cap-opener-hero__logo' in out:
        # Brochure PDF — pre-baked assets replace live CSS overlays (feather, orbit).
        out = out.replace(
            'src="assets/interface-floor-view.jpg',
            'src="assets/interface-floor-view-brochure.jpg',
        )
        out = out.replace(
            'src="assets/diagrams/embedded-operation-orbit.jpg',
            'src="assets/diagrams/embedded-operation-orbit-brochure.png',
        )
    elif budgetary or 'doc-page--overview' in out:
        out = out.replace(
            'src="assets/interface-floor-view.jpg',
            'src="assets/interface-floor-view-budgetary.jpg',
        )
    if 'cap-opener-hero__logo' in out and 'luci-brand-fonts.css' not in out:
        out = out.replace(
            '<link rel="stylesheet" href="brochure.css">',
            '<link rel="stylesheet" href="../../assets/fonts/luci-brand-fonts.css">\n  <link rel="stylesheet" href="brochure.css">',
        )
    if paragon:
        out = out.replace(
            'src="assets/logos/paragon-casino-resort.png',
            f'src="{PARAGON_LOGO}"',
        )
        out = out.replace(
            'src="assets/logos/paragon-casino-resort-print.jpg"',
            f'src="{PARAGON_LOGO}"',
        )
        out = out.replace(
            'src="assets/logos/paragon-casino-resort-print.png"',
            f'src="{PARAGON_LOGO}"',
        )
    if fag_prospect:
        # Replace CSS gradients + mask-images (which Chrome turns into PDF
        # Shading/Pattern XObjects that make macOS Preview blink on open) with
        # pre-baked raster backgrounds. Scoped to the FAG prospect only.
        out = out.replace(
            "</head>",
            "<style>\n"
            ".doc-page--cover, .doc-page--close { background: #0A161C !important; }\n"
            ".doc-page--cover::before, .doc-page--close::before {\n"
            "  background: url('assets/textures/fag-cover-bg-print.jpg') no-repeat center top / cover !important;\n"
            "  -webkit-mask-image: none !important; mask-image: none !important; opacity: 1 !important;\n"
            "}\n"
            ".doc--activation .flag-band {\n"
            "  background: url('assets/textures/fag-flagband-bg-print.jpg') no-repeat right center / cover !important;\n"
            "}\n"
            ".doc--activation .flag-band::before { content: none !important; }\n"
            ".doc--activation .doc-page--nav::after {\n"
            "  background-image: url('assets/textures/fag-nav-bg-print.png') !important;\n"
            "  background-repeat: no-repeat !important; background-position: right center !important;\n"
            "  background-size: 420px auto !important;\n"
            "  -webkit-mask-image: none !important; mask-image: none !important; opacity: 0.35 !important;\n"
            "}\n"
            ".doc--activation .doc-uc__num {\n"
            "  background: url('assets/textures/fag-uc-tile-print.png') no-repeat center / cover !important;\n"
            "}\n"
            ".doc-uc__benefits li::before, .doc-feature::before {\n"
            "  background-color: transparent !important;\n"
            "  background-image: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%232b9e80' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E\") !important;\n"
            "  background-repeat: no-repeat !important; background-position: center !important; background-size: contain !important;\n"
            "  -webkit-mask: none !important; mask: none !important;\n"
            "}\n"
            "</style>\n</head>",
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Patch sales HTML for PDF export.")
    parser.add_argument(
        "--input",
        type=Path,
        help="Single HTML file to patch (writes to --output or stdout).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Destination for patched HTML when using --input.",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Patch DEFAULT_FILES in place (legacy; prefer --input/--output for PDF export).",
    )
    args = parser.parse_args()

    if args.input:
        raw = args.input.read_text(encoding="utf-8")
        patched = patch(raw, paragon=args.input.name.startswith("paragon-"), budgetary="budgetary-estimate" in args.input.name, fag_prospect="field-activation-guide-prospect" in args.input.name)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(patched, encoding="utf-8")
            print(f"patched {args.input} → {args.output}")
        else:
            sys.stdout.write(patched)
        return 0

    if not args.in_place:
        print("Nothing to do. Pass --input/--output for PDF export, or --in-place to patch templates.", file=sys.stderr)
        return 0

    changed = 0
    for path in DEFAULT_FILES:
        if not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        patched = patch(raw, paragon=path.name.startswith("paragon-"), budgetary="budgetary-estimate" in path.name, fag_prospect="field-activation-guide-prospect" in path.name)
        if patched != raw:
            path.write_text(patched, encoding="utf-8")
            print(f"patched {path.relative_to(ROOT)}  ({len(raw)//1024} KB → {len(patched)//1024} KB)")
            changed += 1
    print(f"{changed} file(s) updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
