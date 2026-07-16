#!/usr/bin/env node
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(path.join(__dirname, '..'));

const PDF_BUDGETS = {
  'assets/sales/LUCI-Brochure.pdf': 500 * 1024,
  'assets/sales/LUCI-Case-Study-Ameristar-Council-Bluffs.pdf': 500 * 1024,
};

const ASSET_REF = /(?:src|href)=["'](?!https?:|#|mailto:|tel:|data:)([^"']+)["']/gi;
const CSS_URL_REF = /url\(['"]?([^'")\s?#]+)['"]?\)/gi;

function kb(n) { return `${(n / 1024).toFixed(1)} KB`; }

function walk(dir) {
  const out = [];
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) out.push(...walk(p));
    else out.push(p);
  }
  return out;
}

function collectRefs(filePath, refs) {
  if (!fs.existsSync(filePath)) return;
  const text = fs.readFileSync(filePath, 'utf8');
  const base = path.dirname(filePath);
  ASSET_REF.lastIndex = 0;
  let m;
  while ((m = ASSET_REF.exec(text)) !== null) {
    const ref = m[1].trim().split(/[?#]/)[0];
    if (!ref || ref.startsWith('/')) continue;
    refs.add(path.resolve(base, ref));
  }
  CSS_URL_REF.lastIndex = 0;
  while ((m = CSS_URL_REF.exec(text)) !== null) {
    const ref = m[1].trim().split(/[?#]/)[0];
    if (!ref || ref.startsWith('data:') || ref.startsWith('http')) continue;
    refs.add(path.resolve(base, ref));
  }
}

let failures = 0;
console.log('\n=== PDF size budgets ===');
for (const [rel, budget] of Object.entries(PDF_BUDGETS)) {
  const abs = path.join(root, rel);
  if (!fs.existsSync(abs)) { console.log(`  MISSING  ${rel}`); failures++; continue; }
  const size = fs.statSync(abs).size;
  const ok = size <= budget;
  console.log(`  ${ok ? 'OK' : 'OVER'}  ${rel}  ${kb(size)}  (budget ${kb(budget)})`);
  if (!ok) failures++;
}

const reviewDir = path.join(root, 'ui_kits', 'review');
if (fs.existsSync(reviewDir)) {
  let total = 0;
  for (const p of walk(reviewDir)) total += fs.statSync(p).size;
  console.log(`\n=== Review site total: ${kb(total)} ===`);
}

process.exit(failures ? 1 : 0);
