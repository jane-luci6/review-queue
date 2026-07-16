import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..');
const masterPath = join(root, 'assets', 'diagrams', 'luci-consolidation-ledger.svg');

const ALT =
  'Consolidation ledger: today four or more multimedia systems, five or more equipment racks, fifteen or more receivers, and one hundred plus hardware devices, forty gig AV-over-IP links, thousands per change, and locked code. With LUCI: one interface, one equipment rack, one gig consolidated network, changes included in service, and code that is yours.';

const VARIANTS = {
  master: {
    cssRules: `
      .h-today { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:13px; letter-spacing:2.7px; fill:#8698a2; text-anchor:end; }
      .h-luci  { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:13px; letter-spacing:2.7px; fill:#68e3be; text-anchor:start; }
      .cat { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:10px; letter-spacing:2.2px; fill:#8698a2; fill-opacity:0.55; text-anchor:start; }
      .n-ghost { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:28px; fill:#8698a2; text-anchor:end; }
      .l-ghost { font-family:'Inter',sans-serif; font-weight:400; font-size:13px; fill:#8698a2; fill-opacity:0.86; text-anchor:end; }
      .hero { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:140px; fill:#68e3be; text-anchor:start; dominant-baseline:central; }
      .outcome-word { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:18px; fill:#e8eef2; text-anchor:start; dominant-baseline:central; letter-spacing:0.02em; }
      .n-luci { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:32px; fill:#68e3be; text-anchor:start; }
      .n-luci.q { fill:#edd086; }
      .l-luci { font-family:'Inter',sans-serif; font-weight:600; font-size:14px; fill:#e8eef2; text-anchor:start; }
    `,
    chipR: 22,
    chipStroke: 3,
  },
  deck: {
    cssRules: `
      .h-today { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:18px; letter-spacing:2.7px; fill:#8698a2; text-anchor:end; }
      .h-luci  { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:18px; letter-spacing:2.7px; fill:#68e3be; text-anchor:start; }
      .cat { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:13px; letter-spacing:2.2px; fill:#8698a2; fill-opacity:0.55; text-anchor:start; }
      .n-ghost { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:38px; fill:#8698a2; text-anchor:end; }
      .l-ghost { font-family:'Inter',sans-serif; font-weight:400; font-size:17px; fill:#8698a2; fill-opacity:0.86; text-anchor:end; }
      .hero { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:168px; fill:#68e3be; text-anchor:start; dominant-baseline:central; }
      .outcome-word { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:24px; fill:#e8eef2; text-anchor:start; dominant-baseline:central; letter-spacing:0.02em; }
      .n-luci { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:42px; fill:#68e3be; text-anchor:start; }
      .n-luci.q { fill:#edd086; }
      .l-luci { font-family:'Inter',sans-serif; font-weight:600; font-size:18px; fill:#e8eef2; text-anchor:start; }
    `,
    chipR: 28,
    chipStroke: 4,
  },
};

function chipMarkup({ r, stroke }) {
  const s = r / 22;
  return `<circle r="${r}" fill="#68e3be"/>
      <path d="M${-8 * s},0 H${8 * s} M${2 * s},${-6 * s} L${8 * s},0 L${2 * s},${6 * s}" stroke="#0a161c" stroke-width="${stroke}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;
}

function goldChipMarkup({ r, stroke }) {
  const s = r / 22;
  return `<circle r="${r}" fill="#edd086"/>
      <path d="M${-8 * s},0 H${8 * s} M${2 * s},${-6 * s} L${8 * s},0 L${2 * s},${6 * s}" stroke="#0a161c" stroke-width="${stroke}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;
}

function buildSvg(variantKey, fontFaces) {
  const v = VARIANTS[variantKey];
  const chip = chipMarkup({ r: v.chipR, stroke: v.chipStroke });
  const goldChip = goldChipMarkup({ r: v.chipR, stroke: v.chipStroke });

  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 680" font-family="'Space Grotesk','Inter',sans-serif" role="img" aria-label="${ALT}">
  <defs>
    <clipPath id="ledger-card"><rect x="0" y="0" width="720" height="680" rx="0" ry="0"/></clipPath>
    <linearGradient id="spineGrad" x1="0" y1="64" x2="0" y2="680" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#68e3be" stop-opacity="0"/>
      <stop offset="0.25" stop-color="#68e3be" stop-opacity="0.35"/>
      <stop offset="0.75" stop-color="#edd086" stop-opacity="0.25"/>
      <stop offset="1" stop-color="#edd086" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="wedgeGrad" x1="300" y1="0" x2="360" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#edd086" stop-opacity="0.16"/>
      <stop offset="1" stop-color="#68e3be" stop-opacity="0.30"/>
    </linearGradient>
    <style>
${fontFaces}
${v.cssRules}
    </style>
  </defs>
  <g clip-path="url(#ledger-card)">
    <rect x="0" y="0" width="720" height="680" fill="#0a161c"/>

    <text class="h-today" x="326" y="40">TODAY</text>
    <text class="h-luci" x="394" y="40">WITH LUCI</text>

    <line x1="360" y1="64" x2="360" y2="680" stroke="url(#spineGrad)" stroke-width="1"/>
    <line x1="48" y1="64" x2="672" y2="64" stroke="#ffffff" stroke-opacity="0.08"/>

    <text class="cat" x="48" y="124">SOFTWARE</text>
    <text class="n-ghost" x="326" y="113">4+</text>
    <text class="l-ghost" x="326" y="135">multimedia systems</text>

    <line x1="48" y1="153" x2="326" y2="153" stroke="#ffffff" stroke-opacity="0.06"/>

    <text class="cat" x="48" y="248">HARDWARE</text>
    <text class="n-ghost" x="326" y="177">5+</text>
    <text class="l-ghost" x="326" y="199">equipment racks</text>
    <text class="n-ghost" x="326" y="237">15+</text>
    <text class="l-ghost" x="326" y="259">receivers</text>
    <text class="n-ghost" x="326" y="297">100+</text>
    <text class="l-ghost" x="326" y="319">hardware devices</text>

    <path d="M 334 97 L 334 335 L 360 216 Z" fill="url(#wedgeGrad)"/>

    <g transform="translate(360,216)">
      ${chip}
    </g>

    <g transform="translate(394, 216)">
      <text class="hero" x="0" y="0">1</text>
      <line x1="72" y1="8" x2="198" y2="8" stroke="#ffffff" stroke-opacity="0.14" stroke-width="1"/>
      <text class="outcome-word" x="72" y="-14">interface</text>
      <text class="outcome-word" x="72" y="30">equipment rack</text>
    </g>

    <line x1="48" y1="360" x2="672" y2="360" stroke="#ffffff" stroke-opacity="0.08"/>
    <line x1="360" y1="352" x2="360" y2="368" stroke="#68e3be" stroke-opacity="0.5" stroke-width="1"/>

    <text class="cat" x="48" y="414">NETWORK</text>
    <text class="n-ghost" x="326" y="402">40 Gb</text>
    <text class="l-ghost" x="326" y="426">AV-over-IP links</text>
    <g transform="translate(360,414)">
      ${chip}
    </g>
    <text class="n-luci" x="394" y="402">1 Gb</text>
    <text class="l-luci" x="394" y="426">consolidated network</text>

    <line x1="48" y1="460" x2="672" y2="460" stroke="#ffffff" stroke-opacity="0.06"/>

    <text class="cat" x="48" y="504">SERVICE</text>
    <text class="n-ghost" x="326" y="492">$1,000s</text>
    <text class="l-ghost" x="326" y="516">per change</text>
    <g transform="translate(360,504)">
      ${goldChip}
    </g>
    <text class="n-luci q" x="394" y="492">Included</text>
    <text class="l-luci" x="394" y="516">in service</text>

    <line x1="48" y1="548" x2="672" y2="548" stroke="#ffffff" stroke-opacity="0.06"/>

    <text class="cat" x="48" y="614">CODE</text>
    <text class="n-ghost" x="326" y="602">Locked</text>
    <text class="l-ghost" x="326" y="626">code held hostage</text>
    <g transform="translate(360,614)">
      ${goldChip}
    </g>
    <text class="n-luci q" x="394" y="602">Yours</text>
    <text class="l-luci" x="394" y="626">standardized, documented, owned</text>
  </g>
</svg>
`;
}

const existing = readFileSync(masterPath, 'utf8');
const styleMatch = existing.match(/<style>([\s\S]*?)<\/style>/);
if (!styleMatch) throw new Error('Could not extract <style> block from existing SVG');
const fontFaces = (styleMatch[1].match(/@font-face\{[^}]+\}/g) || []).join('\n      ');
if (!fontFaces) throw new Error('No @font-face rules found in existing SVG style block');

const masterSvg = buildSvg('master', fontFaces);
const deckSvg = buildSvg('deck', fontFaces);

const copies = [
  [masterPath, masterSvg],
  [join(root, 'assets', 'diagrams', 'luci-consolidation-ledger.deck.svg'), deckSvg],
  [join(root, 'ui_kits', 'sales', 'assets', 'diagrams', 'luci-consolidation-ledger.svg'), masterSvg],
  [join(root, 'ui_kits', 'sales', 'assets', 'diagrams', 'luci-consolidation-ledger.deck.svg'), deckSvg],
  [join(root, 'ui_kits', 'review', 'assets', 'diagrams', 'luci-consolidation-ledger.svg'), masterSvg],
  [join(root, 'ui_kits', 'review', 'sales', 'assets', 'diagrams', 'luci-consolidation-ledger.svg'), masterSvg],
  [join(root, 'ui_kits', 'review', 'sales', 'assets', 'diagrams', 'luci-consolidation-ledger.deck.svg'), deckSvg],
];

for (const [dest, body] of copies) {
  mkdirSync(dirname(dest), { recursive: true });
  writeFileSync(dest, body);
  console.log('Wrote', dest, Buffer.byteLength(body), 'bytes');
}
