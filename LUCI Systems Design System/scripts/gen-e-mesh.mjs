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
import { writeFileSync } from 'node:fs';
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
// Ghosted floorplan. Rooms come from recursive subdivision, but only the LEAVES
// are drawn (emitting every recursion level would nest boxes inside boxes and
// read as a chart rather than a plan). A minority of rooms carry a fixture bank
// — a seating or machine run occupying part of the floor, never the whole room.
// One block is rotated 45 degrees to echo the original's angled wing.
// ---------------------------------------------------------------------------
const emptyBlock = () => ({ major: [], minor: [], fixtures: [], marks: [] });

// A hall: one room outline, usually carrying a bank of parallel fixture runs
// (seating rows, machine banks) across part of its floor.
function hall(rng, out, x, y, w, h, opts = {}) {
  const { pitch = 4, fixtures = true, inset = 0.18 } = opts;
  out.minor.push(['r', x, y, w, h]);
  if (!fixtures || w < 8 || h < 8) return;
  const alongX = w >= h;
  const extent = alongX ? w : h;
  const span = extent * (0.55 + rng() * 0.4);
  const off = (extent - span) * rng();
  const count = Math.max(2, Math.round(span / pitch));
  for (let i = 0; i <= count; i++) {
    const t = off + (i * span) / count;
    if (alongX) out.fixtures.push([x + t, y + h * inset, x + t, y + h * (1 - inset)]);
    else out.fixtures.push([x + w * inset, y + t, x + w * (1 - inset), y + t]);
  }
}

// A corridor with rooms banded along one or both sides. Long parallel runs plus
// regular perpendicular dividers is what makes a drawing read as architecture —
// and it costs far fewer strokes than subdividing a rectangle.
function spine(rng, out, x, y, len, horiz, opts = {}) {
  const { cw = 5, depthA = 22, depthB = 22, room = 13, hallRate = 0.22, pitch = 3.8 } = opts;
  if (horiz) {
    out.major.push(['l', x, y, x + len, y]);
    out.major.push(['l', x, y + cw, x + len, y + cw]);
    for (const [d, edge, dir] of [[depthA, y, -1], [depthB, y + cw, 1]]) {
      if (!d) continue;
      const far = edge + dir * d;
      out.major.push(['l', x, far, x + len, far]);
      let cx = x;
      while (cx < x + len - room * 0.6) {
        const rw = room * (0.7 + rng() * 0.9);
        const next = Math.min(cx + rw, x + len);
        out.minor.push(['l', next, edge, next, far]);
        if (rng() < hallRate) hall(rng, out, cx + 1, Math.min(edge, far) + 1, next - cx - 2, d - 2, { pitch });
        cx = next;
      }
    }
  } else {
    out.major.push(['l', x, y, x, y + len]);
    out.major.push(['l', x + cw, y, x + cw, y + len]);
    for (const [d, edge, dir] of [[depthA, x, -1], [depthB, x + cw, 1]]) {
      if (!d) continue;
      const far = edge + dir * d;
      out.major.push(['l', far, y, far, y + len]);
      let cy = y;
      while (cy < y + len - room * 0.6) {
        const rh = room * (0.7 + rng() * 0.9);
        const next = Math.min(cy + rh, y + len);
        out.minor.push(['l', edge, next, far, next]);
        if (rng() < hallRate) hall(rng, out, Math.min(edge, far) + 1, cy + 1, d - 2, next - cy - 2, { pitch });
        cy = next;
      }
    }
  }
}

function scatter(rng, out, x, y, w, h, count, size) {
  for (let i = 0; i < count; i++) {
    const rw = size * (0.6 + rng() * 1.1);
    const rh = size * (0.6 + rng() * 1.1);
    const rx = x + rng() * (w - rw);
    const ry = y + rng() * (h - rh);
    if (rng() < 0.34) out.marks.push([rx, ry, 2, 2]);
    else out.minor.push(['r', rx, ry, rw, rh]);
  }
}

function buildPlan() {
  const rng = mulberry32(20260803);

  // Dense orthogonal core — density peaks where the original's does, in a bright
  // cluster around x 460-660 and a second mass beneath the angled wing.
  const dense = emptyBlock();
  spine(rng, dense, 462, 92, 244, true, { depthA: 26, depthB: 28, room: 12, hallRate: 0.3 });
  spine(rng, dense, 476, 176, 232, true, { cw: 4, depthA: 14, depthB: 20, room: 15, hallRate: 0.24 });
  spine(rng, dense, 468, 22, 156, true, { cw: 4, depthA: 12, depthB: 22, room: 14, hallRate: 0.2 });
  spine(rng, dense, 528, 8, 78, false, { cw: 4, depthA: 20, depthB: 22, room: 12, hallRate: 0.28 });
  spine(rng, dense, 632, 12, 96, false, { cw: 4, depthA: 22, depthB: 26, room: 13, hallRate: 0.26 });
  spine(rng, dense, 706, 96, 116, false, { cw: 4, depthA: 24, depthB: 22, room: 12, hallRate: 0.3 });
  spine(rng, dense, 892, 112, 100, false, { cw: 4, depthA: 28, depthB: 18, room: 14, hallRate: 0.26 });
  spine(rng, dense, 812, 34, 84, false, { cw: 4, depthA: 20, depthB: 24, room: 13, hallRate: 0.24 });
  hall(rng, dense, 848, 168, 76, 48, { pitch: 3.6 });
  hall(rng, dense, 596, 158, 62, 42, { pitch: 4.2 });
  hall(rng, dense, 476, 126, 50, 38, { pitch: 3.4 });
  scatter(rng, dense, 434, 30, 96, 170, 13, 7);
  scatter(rng, dense, 776, 56, 196, 160, 15, 7);

  // Angled wing — a dense band of rooms running off the top-right corner.
  const wing = emptyBlock();
  spine(rng, wing, 6, 26, 244, true, { cw: 5, depthA: 22, depthB: 26, room: 11, hallRate: 0.4, pitch: 3.4 });
  spine(rng, wing, 24, 104, 196, true, { cw: 4, depthA: 16, depthB: 22, room: 12, hallRate: 0.32, pitch: 3.6 });
  scatter(rng, wing, 10, 0, 230, 150, 12, 6);

  // Faint traces across the upper left — fragmentary rather than continuous, so the
  // left reads as a ghost of the drawing instead of a second banded structure.
  const faint = emptyBlock();
  spine(rng, faint, 18, 58, 104, true, { cw: 5, depthA: 24, depthB: 0, room: 20, hallRate: 0.14 });
  spine(rng, faint, 250, 40, 92, true, { cw: 4, depthA: 0, depthB: 26, room: 22, hallRate: 0.12 });
  spine(rng, faint, 62, 152, 116, true, { cw: 4, depthA: 16, depthB: 0, room: 24, hallRate: 0.1 });
  spine(rng, faint, 336, 130, 70, false, { cw: 4, depthA: 20, depthB: 0, room: 22, hallRate: 0.1 });
  scatter(rng, faint, 20, 16, 388, 214, 22, 9);

  return { dense, wing, faint };
}

// ---------------------------------------------------------------------------
// Emit
// ---------------------------------------------------------------------------
function line(a, b, c, d) {
  return `<line x1="${s(a)}" y1="${s(b)}" x2="${s(c)}" y2="${s(d)}"/>`;
}
function rect(x, y, w, h) {
  return `<rect x="${s(x)}" y="${s(y)}" width="${s(w)}" height="${s(h)}"/>`;
}

const shape = ([kind, ...v]) => (kind === 'r' ? rect(...v) : line(...v));

function planGroup(block) {
  const parts = [];
  if (block.major.length) parts.push(`<g class="pl-major">${block.major.map(shape).join('')}</g>`);
  if (block.minor.length) parts.push(`<g class="pl-minor">${block.minor.map(shape).join('')}</g>`);
  if (block.fixtures.length) parts.push(`<g class="pl-fix">${block.fixtures.map((f) => line(...f)).join('')}</g>`);
  if (block.marks.length) parts.push(`<g class="pl-mark">${block.marks.map((m) => rect(...m)).join('')}</g>`);
  return parts.join('');
}

function build({ solid }) {
  const { dense, wing, faint } = buildPlan();

  const css = `
    .em-plan rect, .em-plan line { fill: none; stroke: ${MINT}; }
    .em-plan .pl-major line, .em-plan .pl-major rect { stroke-width: 1.3; }
    .em-plan .pl-minor line, .em-plan .pl-minor rect { stroke-width: 0.8; }
    .em-plan .pl-fix line { stroke-width: 0.7; }
    .em-plan .pl-mark rect { fill: ${MINT}; stroke: none; }
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
    <linearGradient id="em-plan-cut" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
      <stop offset="34%" stop-color="#fff" stop-opacity="1"/>
      <stop offset="46%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="em-plan-mask">
      <rect width="${W}" height="${H}" fill="url(#em-plan-fade)"/>
    </mask>
    <mask id="em-plan-cut-mask">
      <rect width="${W}" height="${H}" fill="url(#em-plan-cut)"/>
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
  <g mask="url(#em-plan-cut-mask)">
    <g class="em-plan" mask="url(#em-plan-mask)">
      <g opacity="0.4">${planGroup(dense)}</g>
      <g opacity="0.38" transform="translate(${s(742)} ${s(168)}) rotate(-45)">${planGroup(wing)}</g>
      <g opacity="0.11">${planGroup(faint)}</g>
    </g>
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
