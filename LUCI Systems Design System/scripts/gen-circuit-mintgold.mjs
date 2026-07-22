// Generates a guaranteed-seamless mint/gold circuit-bracket texture tile.
// Seamlessness: motif is placed on a periodic brick lattice (x-period 64, y-period 128)
// inside a 1024x1024 canvas (a whole multiple of both periods), so the left/right and
// top/bottom edges are the same phase -> tiles with no visible seams.
//
// Motif: hollow L-shaped bracket outlines (thick colored stroke + thinner black core)
// with a smaller parallel inner bar, colored along a gold->mint diagonal gradient,
// on a black background (matches the existing lighten-blend usage on navy sections).
import sharp from 'sharp';
import { writeFileSync } from 'node:fs';

const S = 1024;            // canvas size (whole multiple of lattice periods)
const STEP = 64;           // lattice spacing
const OFF = 32;            // brick row offset (STEP/2)
const UNIT = 18;           // half-extent of each bracket
const SW = 5;              // outer stroke width
const CORE = 2.5;          // black core width (makes the L hollow)
const INNER = 7;          // inner parallel bar half-length

const MINT = '#68E3BE';
const GOLD = '#CEB06E';
const BG = '#000000';

// gold -> mint along the diagonal, but PERIODIC with period = canvas (1024) so the
// gradient wraps seamlessly at the tile edges (cosine completes one cycle per canvas).
function gradColor(cx, cy) {
  const t = (1 - Math.cos(2 * Math.PI * (cx + cy) / S)) / 2; // 0..1, period S in (cx+cy)
  const a = [0xCE, 0xB0, 0x6E];
  const b = [0x68, 0xE3, 0xBE];
  const r = Math.round(a[0] + (b[0] - a[0]) * t);
  const g = Math.round(a[1] + (b[1] - a[1]) * t);
  const bl = Math.round(a[2] + (b[2] - a[2]) * t);
  return `rgb(${r},${g},${bl})`;
}

// orientation of the L bracket by position -> a diagonal maze rhythm
function orient(i, j) {
  return ((i + Math.floor(j / 2)) % 4);
}

let svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${S}" height="${S}" viewBox="0 0 ${S} ${S}">`;
svg += `<rect width="${S}" height="${S}" fill="${BG}"/>`;

for (let j = 0; j < S / STEP; j++) {
  for (let i = 0; i < S / STEP; i++) {
    const cx0 = OFF + i * STEP + (j % 2) * OFF;
    const cy0 = OFF + j * STEP;
    const col = gradColor(cx0, cy0);
    const o = orient(i, j);
    // Draw at 9 offsets (±S) so any unit crossing a canvas edge has its wrapped
    // continuation drawn on the opposite edge -> seamless tiling. SVG clips to viewBox.
    for (const dx of [-S, 0, S]) {
      for (const dy of [-S, 0, S]) {
        const cx = cx0 + dx;
        const cy = cy0 + dy;
    // L bracket: two perpendicular bars meeting at a corner, orientation o
    // corner point depends on o (0=TL,1=TR,2=BR,3=BL)
    let hx1, hy1, hx2, hy2, vx1, vy1, vx2, vy2;
    const u = UNIT;
    if (o === 0) { hx1 = cx - u; hy1 = cy - u; hx2 = cx + u; hy2 = cy - u; vx1 = cx - u; vy1 = cy - u; vx2 = cx - u; vy2 = cy + u; }
    else if (o === 1) { hx1 = cx - u; hy1 = cy - u; hx2 = cx + u; hy2 = cy - u; vx1 = cx + u; vy1 = cy - u; vx2 = cx + u; vy2 = cy + u; }
    else if (o === 2) { hx1 = cx - u; hy1 = cy + u; hx2 = cx + u; hy2 = cy + u; vx1 = cx + u; vy1 = cy - u; vx2 = cx + u; vy2 = cy + u; }
    else { hx1 = cx - u; hy1 = cy + u; hx2 = cx + u; hy2 = cy + u; vx1 = cx - u; vy1 = cy - u; vx2 = cx - u; vy2 = cy + u; }
    const Lpath = `M ${hx1} ${hy1} L ${hx2} ${hy2} L ${vx2} ${vy2}`;
    // hollow: outer color stroke + inner black core stroke
    svg += `<path d="${Lpath}" stroke="${col}" stroke-width="${SW}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;
    svg += `<path d="${Lpath}" stroke="${BG}" stroke-width="${SW - CORE}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;
    // inner parallel bar (short), offset inward from the corner
    let ix1, iy1, ix2, iy2;
    const il = INNER;
    if (o === 0) { ix1 = cx - il; iy1 = cy - u + 3; ix2 = cx + il; iy2 = cy - u + 3; }
    else if (o === 1) { ix1 = cx - il; iy1 = cy - u + 3; ix2 = cx + il; iy2 = cy - u + 3; }
    else if (o === 2) { ix1 = cx - il; iy1 = cy + u - 3; ix2 = cx + il; iy2 = cy + u - 3; }
    else { ix1 = cx - il; iy1 = cy + u - 3; ix2 = cx + il; iy2 = cy + u - 3; }
    svg += `<path d="M ${ix1} ${iy1} L ${ix2} ${iy2}" stroke="${col}" stroke-width="${SW - 1.5}" stroke-linecap="round" fill="none"/>`;
      }
    }
  }
}
svg += `</svg>`;

writeFileSync('/tmp/circuit-tile.svg', svg);
// rasterize to PNG at 2x for retina crispness, then downsample to 1024 for the master
await sharp(Buffer.from(svg), { density: 144 })
  .resize(S, S)
  .png()
  .toFile('/tmp/circuit-mintgold-seamless.png');
console.log('wrote /tmp/circuit-mintgold-seamless.png');
