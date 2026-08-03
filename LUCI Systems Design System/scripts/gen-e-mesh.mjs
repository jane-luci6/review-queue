// Generates the LUCI E-mesh motif as a resolution-independent SVG master.
//
// The E-mesh began life as a raster (a 1024x576 JPEG reused for the Teams background,
// desktop wallpaper, and LinkedIn cover) with the LUCI wordmark baked in. That file is
// too small for a full-bleed web hero and its logo collides with the site header, so the
// motif is rebuilt here in vector form.
//
// The composition is a faithful reconstruction, not a freehand redraw. The primary grid
// lines, node positions, the four gold nodes, and the hollow rings were all measured off
// the original raster, so the coordinate tables below are in the original's 1024x576
// space and are scaled up to the 1920x1080 master artboard (K = 1.875). Two deliberate
// departures from the original:
//
//   1. No logo. The master is logo-free so consumers can place their own lockup (the
//      website already has one in the header).
//   2. Grid lines run continuous. The original knocked the y=35 and y=97 lines out
//      behind the wordmark to give it clear space; with no logo, the gaps would read as
//      broken lines.
//
// The ghosted architectural floorplan in the upper right is procedurally generated from a
// fixed seed rather than traced — at background opacity it reads as texture, and a
// generated plan stays compact and editable where a trace would be a machine-made blob.
//
// Outputs (assets/diagrams/):
//   luci-e-mesh.svg        transparent canvas — for web, composited over a section tone
//   luci-e-mesh.solid.svg  navy canvas + vignette — for Teams/wallpaper/LinkedIn renders
//
// Usage: node scripts/gen-e-mesh.mjs
import { writeFileSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const MINT = '#68E3BE';
const GOLD = '#EDD086';
const NAVY = '#0A161C';

const SRC_W = 1024; // measurement space — the original raster
const W = 1920, H = 1080; // master artboard
const K = W / SRC_W; // 1.875

const OUT = path.join(path.dirname(fileURLToPath(import.meta.url)), '..', 'assets', 'diagrams');

const n2 = (n) => +(Math.round(n * 100) / 100).toFixed(2);
const s = (n) => n2(n * K); // source space -> master space

// Deterministic PRNG so the generated plan is identical on every run.
function mulberry32(a) {
  return function () {
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ---------------------------------------------------------------------------
// Primary grid — the signature layer. Measured extents; note the varied start
// and end points, which is what keeps the composition from feeling mechanical.
// ---------------------------------------------------------------------------
const V_MAIN = [
  // [x, y0, y1]
  [96.5, 26, 230],
  [404, 0, 576], // full height
  [573.2, 0, 162],
  [778, 0, 576], // full height
  [846, 151, 294],
  [856, 59, 233],
  [941.5, 35, 233],
];

const H_MAIN = [
  // [y, x0, x1]
  [35.5, 0, 781],
  [97.5, 0, 1024], // was knocked out behind the wordmark; continuous here
  [153.5, 84, 1024],
  [194.5, 85, 238],
  [230.7, 401, 944],
  [140.5, 647, 778],
];

// Secondary connectors — the short stepped runs that tie nodes into the grid.
const V_SUB = [
  [236, 174, 197],
  [392, 120, 156],
  [424, 146, 167],
  [473, 32, 142],
  [522.5, 109, 233],
  [536.5, 30, 73],
  [605, 30, 111],
  [620.5, 19, 156],
  [736, 149, 200],
  [773.5, 93, 142],
  [794, 118, 142],
  [819.5, 56, 100],
  [841, 106, 172],
  [895.5, 97, 117],
];

const H_SUB = [
  [21, 573, 623],
  [58, 773, 822],
  [63, 851, 944],
  [70.5, 534, 578],
  [117, 835, 944],
  [133, 743, 778],
  [170, 774, 846],
  [178.5, 773, 794],
  [187, 401, 425],
  [191, 783, 944],
  [200, 675, 719],
  [291, 775, 848],
];

// ---------------------------------------------------------------------------
// Nodes — filled dots on grid intersections. Gold is deliberately scarce: four
// nodes in a single cluster, per the mint-primary / gold-secondary rule.
// ---------------------------------------------------------------------------
const NODES_MINT = [
  [96.8, 35.3], [371.5, 35.3], [404, 35.3], [473.1, 35.3], [573, 35.3], [620.5, 35.3], [777.9, 35.4],
  [645.9, 41.7], [819.7, 57.9], [855.9, 62.9], [941.7, 63],
  [882.8, 89.2],
  [404, 97.5], [423.6, 97.4], [473, 97.4], [573.3, 98], [605.1, 97.5], [620.5, 97.5],
  [777.8, 97.5], [819.5, 97.5], [855.7, 97.3], [941.6, 97.4],
  [605.1, 108.8], [841.3, 115.7], [855.8, 116.8], [941.5, 116.9],
  [620.9, 126.4], [745.1, 133.1], [473.1, 139.7],
  [391.6, 153.8], [404, 154], [423.5, 153.9], [503.1, 153.9], [523, 153.9], [537.5, 153.9],
  [573.1, 153.8], [620.5, 153.9], [744.7, 153.8], [777.9, 153.9], [845.5, 154], [941.5, 153.8],
  [754.8, 165.8],
  [404, 187.5], [846.2, 191.7], [855.9, 191.4], [941.6, 191.4],
  [97, 194.6], [200.7, 194.7], [235.8, 194.8],
  [404.2, 229.9], [523, 229.7], [784.3, 229], [845.6, 230], [855.7, 229.7], [941.5, 229.7],
  [778, 291], [845.8, 291.4],
];

const NODES_GOLD = [
  [777.5, 170],
  [841.1, 169.8],
  [856, 154],
  [785.5, 191.2],
];

// Hollow rings — [x, y, r] in source space.
const RINGS = [
  [96.9, 152.9, 5],
  [538, 34, 3.2],
  [573.3, 70.7, 5.5],
  [699.3, 44.8, 6.5],
  [772.4, 51.8, 8],
  [776, 231.9, 5],
];

// ---------------------------------------------------------------------------
// Ghosted floorplan. the original E-mesh carried a real architectural drawing behind
// its grid — that fuzzy floorplan is what makes the motif read as architecture
// rather than a circuit. The drawing is sourced from a real CAD export
// (assets/diagrams/luci-e-mesh-floorplan.png), cleaned of the UI chrome
// (label bubbles, coloured highlights, dropdown, sidebar icons) so only the
// fine-line architectural drawing carries through. It sits as a raster underlay
// at low opacity, behind the vector grid — a hybrid: sharp vector grid + nodes
// + rings over a fuzzy raster plan, mirroring the original's structure.
// ---------------------------------------------------------------------------
const FLOORPLAN = 'luci-e-mesh-floorplan.png';
const FLOORPLAN_DATA = `data:image/png;base64,${readFileSync(path.join(OUT, FLOORPLAN), 'base64')}`;
// The floorplan PNG is 924x805 (source space). Anchored top-right, covering ~55%
// of the canvas width and ~70% of the height — matching the original where the
// floorplan sits in the upper-right and the lower-left stays clear. The em-plan-fade
// mask fades it out toward the lower-left. preserveAspectRatio 'slice' crops
// rather than letterboxing.
const FP_X = s(400);
const FP_Y = 0;
const FP_W = W - FP_X;
const FP_H = s(420);

function line(a, b, c, d) {
  return `<line x1="${s(a)}" y1="${s(b)}" x2="${s(c)}" y2="${s(d)}"/>`;
}
function rect(x, y, w, h) {
  return `<rect x="${s(x)}" y="${s(y)}" width="${s(w)}" height="${s(h)}"/>`;
}

function build({ solid }) {
  const css = `
    .em-grid line { stroke: ${MINT}; stroke-width: 1.7; }
    .em-grid-sub line { stroke: ${MINT}; stroke-width: 1.2; }
    .em-node { fill: ${MINT}; }
    .em-node-gold { fill: ${GOLD}; }
    .em-ring { fill: none; stroke: ${MINT}; stroke-width: 1.8; }`;

  const vignette = solid
    ? `<radialGradient id="em-vig" cx="22%" cy="8%" r="88%">
      <stop offset="0%" stop-color="#12262F"/>
      <stop offset="55%" stop-color="#0C1A22"/>
      <stop offset="100%" stop-color="#060F14"/>
    </radialGradient>`
    : '';

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="LUCI E-mesh: an engineering grid of mint nodes over a ghosted architectural floorplan">
  <title>LUCI E-mesh</title>
  <defs>
    <style>${css}
    </style>${vignette}
    <radialGradient id="em-plan-fade" cx="70%" cy="6%" r="72%" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
      <stop offset="46%" stop-color="#fff" stop-opacity="0.72"/>
      <stop offset="78%" stop-color="#fff" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </radialGradient>
    <mask id="em-plan-mask">
      <rect width="${W}" height="${H}" fill="url(#em-plan-fade)"/>
    </mask>
    <linearGradient id="em-grid-fade" x1="0" y1="0" x2="0.28" y2="1">
      <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
      <stop offset="42%" stop-color="#fff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0.5"/>
    </linearGradient>
    <mask id="em-grid-mask">
      <rect width="${W}" height="${H}" fill="url(#em-grid-fade)"/>
    </mask>
  </defs>
${solid ? `  <rect width="${W}" height="${H}" fill="url(#em-vig)"/>\n` : ''}
  <g mask="url(#em-plan-mask)">
    <image href="${FLOORPLAN_DATA}" x="${FP_X}" y="${FP_Y}" width="${FP_W}" height="${FP_H}" preserveAspectRatio="xMidYMid slice" opacity="0.55"/>
  </g>

  <g class="em-grid-layer" mask="url(#em-grid-mask)">
    <g class="em-grid" opacity="0.46">
${H_MAIN.map(([y, x0, x1]) => '      ' + line(x0, y, x1, y)).join('\n')}
${V_MAIN.map(([x, y0, y1]) => '      ' + line(x, y0, x, y1)).join('\n')}
    </g>
    <g class="em-grid-sub" opacity="0.26">
${H_SUB.map(([y, x0, x1]) => '      ' + line(x0, y, x1, y)).join('\n')}
${V_SUB.map(([x, y0, y1]) => '      ' + line(x, y0, x, y1)).join('\n')}
    </g>
    <g class="em-node" opacity="0.82">
${NODES_MINT.map(([x, y]) => `      <circle cx="${s(x)}" cy="${s(y)}" r="5.6"/>`).join('\n')}
    </g>
    <g class="em-node-gold" opacity="0.9">
${NODES_GOLD.map(([x, y]) => `      <circle cx="${s(x)}" cy="${s(y)}" r="6"/>`).join('\n')}
    </g>
    <g class="em-ring" opacity="0.6">
${RINGS.map(([x, y, r]) => `      <circle cx="${s(x)}" cy="${s(y)}" r="${s(r)}"/>`).join('\n')}
    </g>
  </g>
</svg>
`;
  return svg;
}

for (const solid of [false, true]) {
  const name = solid ? 'luci-e-mesh.solid.svg' : 'luci-e-mesh.svg';
  const out = path.join(OUT, name);
  const svg = build({ solid });
  writeFileSync(out, svg);
  console.log(`Wrote assets/diagrams/${name}  (${(svg.length / 1024).toFixed(1)} KB)`);
}
