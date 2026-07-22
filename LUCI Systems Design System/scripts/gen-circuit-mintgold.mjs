// Generates guaranteed-seamless mint/gold circuit tiles that reproduce the ORIGINAL
// motif: nested L/bracket forms (three concentric 90-degree strokes — outer thin
// outline, middle thick bar, inner short line), oriented 45deg, on a staggered
// (brick) diagonal grid, gold->mint diagonal gradient, on black.
//
// Seamlessness: motif sits on a periodic brick lattice (x-period = STEP, y-period =
// 2*STEP) inside a canvas that is a whole multiple of both periods, the gradient
// is a periodic cosine (period = canvas), and every unit is drawn at +/-canvas
// offsets so edge-crossing shapes wrap. -> tiles with zero visible seams.
//
// Two scales of the SAME motif:
//   - big  (1024, STEP 64):  the bigger version for the website (cover/no-repeat)
//   - small (512,  STEP 40):  a finer/denser version for PDFs, infographics, social
import sharp from 'sharp';
import { writeFileSync } from 'node:fs';

const MINT = '#68E3BE';
const GOLD = '#CEB06E';
const BG = '#000000';

// gold -> mint along the diagonal, PERIODIC with period = canvas (one full cycle)
function gradColor(cx, cy, S) {
  const t = (1 - Math.cos(2 * Math.PI * (cx + cy) / S)) / 2;
  const a = [0xCE, 0xB0, 0x6E], b = [0x68, 0xE3, 0xBE];
  const r = Math.round(a[0] + (b[0] - a[0]) * t);
  const g = Math.round(a[1] + (b[1] - a[1]) * t);
  const bl = Math.round(a[2] + (b[2] - a[2]) * t);
  return `rgb(${r},${g},${bl})`;
}
// orientation cycles so the staggered grid reads as a diagonal maze
function orient(i, j) { return ((i + Math.floor(j / 2)) % 4); }

function build({ S, STEP, OFF, U, SW, MID, CORE, INNER, name, out }) {
  let svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${S}" height="${S}" viewBox="0 0 ${S} ${S}">`;
  svg += `<rect width="${S}" height="${S}" fill="${BG}"/>`;
  for (let j = 0; j < S / STEP; j++) {
    for (let i = 0; i < S / STEP; i++) {
      const cx0 = OFF + i * STEP + (j % 2) * OFF;
      const cy0 = OFF + j * STEP;
      const col = gradColor(cx0, cy0, S);
      const o = orient(i, j);
      for (const dx of [-S, 0, S]) {
        for (const dy of [-S, 0, S]) {
          const cx = cx0 + dx, cy = cy0 + dy;
          // L/bracket pointing top-right; orientations flip which corner opens
          const sx = (o === 1 || o === 2) ? -1 : 1;   // horizontal sign
          const sy = (o >= 2) ? -1 : 1;               // vertical sign
          const Lp = `M ${cx - sx * U} ${cy - sy * U} L ${cx + sx * U} ${cy - sy * U} L ${cx + sx * U} ${cy + sy * U}`;
          // outer thin outline
          svg += `<path d="${Lp}" stroke="${col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;
          // middle thick bar (hollow: colored stroke + black core)
          const m = U * 0.62;
          const Lm = `M ${cx - sx * m} ${cy - sy * m} L ${cx + sx * m} ${cy - sy * m} L ${cx + sx * m} ${cy + sy * m}`;
          svg += `<path d="${Lm}" stroke="${col}" stroke-width="${MID}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;
          svg += `<path d="${Lm}" stroke="${BG}" stroke-width="${MID - CORE}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>`;
          // inner short thin line near the corner
          const il = U * 0.34;
          const ix = cx + sx * (U - il) * 0.5, iy = cy - sy * (U - il) * 0.5;
          svg += `<path d="M ${ix - sx * il} ${iy} L ${ix + sx * il} ${iy}" stroke="${col}" stroke-width="2" stroke-linecap="round" fill="none"/>`;
        }
      }
    }
  }
  svg += `</svg>`;
  writeFileSync(out + '.svg', svg);
  sharp(Buffer.from(svg), { density: 144 }).resize(S, S).png().toFile(out + '.png').then(() => console.log('wrote', out));
}

build({ S: 1024, STEP: 64, OFF: 32, U: 18, SW: 5, MID: 5, CORE: 2.5, INNER: 7, name: 'big',  out: '/tmp/circuit-mintgold-big' });
build({ S: 512,  STEP: 40, OFF: 20, U: 11, SW: 4, MID: 4, CORE: 2.0, INNER: 5, name: 'small', out: '/tmp/circuit-mintgold-small' });
