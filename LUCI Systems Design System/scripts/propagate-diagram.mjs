#!/usr/bin/env node
// propagate-diagram.mjs
// Propagate a canonical diagram master to all its consumer copies.
//
// Usage:
//   node scripts/propagate-diagram.mjs <diagram-basename>            # propagate (writes)
//   node scripts/propagate-diagram.mjs <diagram-basename> --dry-run # report only, no writes
//   node scripts/propagate-diagram.mjs --audit                        # print full inventory, no writes
//
// What "propagate <name>" does:
//   1. Regenerate derived variant masters from the base master, where a builder exists
//      (delegates to ui_kits/sales/_build_deck_variants.py).
//   2. For every consumer copy of the diagram (across configured consumer folders),
//      re-derive the copy from the appropriate variant master, applying that
//      consumer's stored crop (viewBox/width/height read from the existing copy).
//      The master is never resized; only the copy is cropped.
//   3. Bump ?v=N on every <img> ref to that copy across the repo.
//   4. Flag raster (png/jpg) consumers that need re-export + the command to run.
//   5. Flag consumers whose master aspect ratio changed vs. the crop (re-crop review).
//
// See .cursor/rules/luci-propagation-workflow.mdc for the workflow.

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(path.join(__dirname, '..'));
const WEBSITE = path.resolve(path.join(ROOT, '..', '..', 'luci-website'));

const MASTER_DIR = path.join(ROOT, 'assets', 'diagrams');
const CONSUMER_DIRS = [
  path.join(ROOT, 'ui_kits', 'sales', 'assets', 'diagrams'),
  path.join(ROOT, 'ui_kits', 'review', 'assets', 'diagrams'),
  path.join(WEBSITE, 'public', 'images', 'diagrams'),
];
const DECK_BUILDER = path.join(ROOT, 'ui_kits', 'sales', '_build_deck_variants.py');
// Diagrams whose .deck.svg master is derived from the base master by DECK_BUILDER.
const DECK_DERIVED = new Set(['luci-what-luci-is']);

const RASTER_EXT = new Set(['.png', '.jpg', '.jpeg']);
const SVG_EXT = '.svg';

function exists(p) { try { fs.accessSync(p); return true; } catch { return false; } }
function read(p) { return fs.readFileSync(p, 'utf8'); }
function write(p, s) { fs.writeFileSync(p, s); }

// <svg ...> attributes parser (viewBox / width / height)
function svgHeaderAttrs(svg) {
  const head = svg.slice(0, svg.indexOf('>'));
  const vb = (head.match(/viewBox="([^"]+)"/) || [])[1];
  const w = (head.match(/\bwidth="([^"]+)"/) || [])[1];
  const h = (head.match(/\bheight="([^"]+)"/) || [])[1];
  return { viewBox: vb, width: w, height: h };
}

function setSvgAttrs(svg, attrs) {
  let out = svg;
  if (attrs.viewBox) {
    out = out.replace(/viewBox="[^"]*"/, 'viewBox="' + attrs.viewBox + '"');
    if (!/viewBox=/.test(out)) {
      out = out.replace(/<svg /, '<svg viewBox="' + attrs.viewBox + '" ');
    }
  }
  if (attrs.width) out = out.replace(/\bwidth="[^"]*"/, 'width="' + attrs.width + '"');
  if (attrs.height) out = out.replace(/\bheight="[^"]*"/, 'height="' + attrs.height + '"');
  return out;
}

function aspectOf(vb) {
  if (!vb) return null;
  const p = vb.trim().split(/\s+/).map(Number);
  if (p.length !== 4 || p.some(isNaN)) return null;
  return Math.round(((p[2] / p[3]) + Number.EPSILON) * 1000) / 1000;
}

// Find all master files (base + variants) for a basename.
function mastersFor(base) {
  if (!exists(MASTER_DIR)) return [];
  return fs.readdirSync(MASTER_DIR)
    .filter(f => f === base + SVG_EXT || f.startsWith(base + '.') && f.endsWith(SVG_EXT))
    .map(f => ({ file: f, path: path.join(MASTER_DIR, f) }));
}

// Find consumer copies of a given master file across CONSUMER_DIRS.
function consumersOf(masterFile) {
  const stem = masterFile.replace(/\.svg$/, '');
  const candidates = [masterFile, stem + '.png', stem + '.jpg', stem + '.jpeg'];
  const out = [];
  for (const dir of CONSUMER_DIRS) {
    if (!exists(dir)) continue;
    for (const c of candidates) {
      const p = path.join(dir, c);
      if (exists(p)) out.push({ dir, path: p });
    }
  }
  return out;
}

// Find <img> refs to a consumer copy (by its referenced path) in HTML/Astro/CSS files.
const REF_RE = /(?:src|href)=["'](?!https?:|#|mailto:|tel:|data:)([^"']+)["']/gi;
function refsTo(targets) {
  const hits = [];
  const seen = new Set();
  const roots = [ROOT, WEBSITE];
  for (const r of roots) {
    if (!exists(r)) continue;
    const stack = [r];
    while (stack.length) {
      const cur = stack.pop();
      let ents;
      try { ents = fs.readdirSync(cur, { withFileTypes: true }); } catch { continue; }
      for (const e of ents) {
        if (e.name === 'node_modules' || e.name === '.git' || e.name === 'dist' || e.name === '.texcheck') continue;
        const fp = path.join(cur, e.name);
        if (e.isDirectory()) { stack.push(fp); continue; }
        if (!/\.(html?|astro|css|md|mdx|ts|js|mjs|tsx|jsx)$/.test(e.name)) continue;
        let text;
        try { text = read(fp); } catch { continue; }
        REF_RE.lastIndex = 0;
        let m;
        while ((m = REF_RE.exec(text)) !== null) {
          const ref = m[1].trim().split(/[?#]/)[0];
          if (!ref) continue;
          // normalize: absolute /images/... lives under website public; relative assets/... under destDir
          let norm;
          if (ref.startsWith('/')) {
            let webRoot;
            if (fp.startsWith(path.join(ROOT, 'ui_kits', 'review') + path.sep)) webRoot = path.join(ROOT, 'ui_kits', 'review');
            else if (fp.startsWith(WEBSITE + path.sep)) webRoot = path.join(WEBSITE, 'public');
            else webRoot = path.dirname(fp);
            norm = path.join(webRoot, ref);
          } else norm = path.resolve(path.dirname(fp), ref);
          if (targets.has(norm)) {
            const key = fp + '\u0000' + m[1];
            if (seen.has(key)) continue;
            seen.add(key);
            hits.push({ file: fp, ref: m[1] });
          }
        }
      }
    }
  }
  return hits;
}

function bumpVersion(ref) {
  const m = ref.match(/\?v=(\d+)/);
  if (!m) return ref + '?v=1';
  const n = parseInt(m[1], 10) + 1;
  return ref.replace(/\?v=\d+/, '?v=' + n);
}

function orphans() {
  const masterNames = new Set(exists(MASTER_DIR) ? fs.readdirSync(MASTER_DIR) : []);
  const found = [];
  for (const dir of CONSUMER_DIRS) {
    if (!exists(dir)) continue;
    for (const f of fs.readdirSync(dir)) {
      if (!f.endsWith(SVG_EXT) || masterNames.has(f)) continue;
      found.push(path.join(dir, f));
    }
  }
  console.log('\n=== Orphan copies (no matching master) — drift / site-specific, decide: promote to master, rename, or remove ===');
  if (!found.length) { console.log('  (none)'); return; }
  for (const p of found) console.log('  ' + path.relative(ROOT, p));
}

function audit() {
  console.log('=== Canonical diagram inventory ===');
  const bases = new Set();
  for (const f of fs.readdirSync(MASTER_DIR)) {
    if (!f.endsWith(SVG_EXT)) continue;
    const stem = f.startsWith('luci-') || f.startsWith('embedded-') ? f.replace(/\.(deck|dark|web|anim|identity-only)\.svg$/, '.svg') : f;
    bases.add(f.replace(/\.(deck|dark|web|anim|identity-only)\.svg$/, '').replace(/\.svg$/, ''));
  }
  for (const base of [...bases].sort()) {
    const ms = mastersFor(base);
    console.log('\n' + base);
    for (const m of ms) {
      const cons = consumersOf(m.file);
      console.log('  master: ' + m.file);
      if (!cons.length) { console.log('    (no consumers)'); continue; }
      for (const c of cons) console.log('    -> ' + path.relative(ROOT, c.path));
    }
  }
  orphans();
}

function propagate(base, dryRun) {
  const masters = mastersFor(base);
  if (!masters.length) { console.error('No master found for "' + base + '" in ' + MASTER_DIR); process.exit(1); }
  const report = { diagram: base, masters: [], consumers: [], refs: [], raster: [], aspectWarnings: [], deckDerived: [] };

  // 1. regenerate derived variant masters
  if (DECK_DERIVED.has(base) && exists(DECK_BUILDER)) {
    report.deckDerived.push(base + '.deck.svg via _build_deck_variants.py');
    if (!dryRun) {
      try { execSync('python3 ' + DECK_BUILDER, { stdio: 'inherit' }); }
      catch (e) { console.error('  ! deck builder failed: ' + e.message); }
    }
  }

  for (const m of masters) {
    const mEntry = { master: m.file, consumers: [] };
    const mSvg = read(m.path);
    const mAttrs = svgHeaderAttrs(mSvg);
    const mAspect = aspectOf(mAttrs.viewBox);
    const cons = consumersOf(m.file);
    for (const c of cons) {
      const cEntry = { dest: path.relative(ROOT, c.path), kind: null, raster: null };
      const ext = path.extname(c.path);
      if (RASTER_EXT.has(ext)) {
        // raster consumer — flag for re-export, don't re-derive here
        cEntry.kind = 'raster';
        cEntry.raster = 're-export from ' + m.file + ' (run: npm run prepare:pdf for sales; or export SVG->PNG for website/hub)';
        report.raster.push(cEntry.dest);
        mEntry.consumers.push(cEntry);
        continue;
      }
      // SVG consumer — re-derive from master, applying the consumer's stored crop
      let cSvg;
      try { cSvg = read(c.path); } catch { cSvg = ''; }
      const cAttrs = svgHeaderAttrs(cSvg);
      let derived = mSvg;
      if (cAttrs.viewBox || cAttrs.width || cAttrs.height) {
        derived = setSvgAttrs(derived, { viewBox: cAttrs.viewBox, width: cAttrs.width, height: cAttrs.height });
      }
      cEntry.kind = 'svg';
      cEntry.changed = !exists(c.path) || derived !== cSvg;
      // aspect-ratio change flag
      if (mAspect && aspectOf(cAttrs.viewBox) && Math.abs(mAspect - aspectOf(cAttrs.viewBox)) > 0.05) {
        cEntry.aspectWarning = 'master aspect ' + mAspect + ' differs from crop aspect ' + aspectOf(cAttrs.viewBox) + ' — eyeball this crop';
        report.aspectWarnings.push(cEntry.dest);
      }
      if (!dryRun && cEntry.changed) write(c.path, derived);
      mEntry.consumers.push(cEntry);
      report.consumers.push(cEntry);
    }
    report.masters.push(mEntry);
  }

  // 3. bump ?v on <img> refs to the master + every re-derived SVG consumer copy (deduped)
  const targets = new Set();
  for (const m of masters) targets.add(m.path);
  for (const c of report.consumers) if (c.kind === 'svg') targets.add(path.join(ROOT, c.dest));
  const refHits = refsTo(targets);
  for (const h of refHits) {
    const old = h.ref;
    const next = bumpVersion(old);
    report.refs.push({ file: h.file, old, next });
    if (!dryRun) { let t = read(h.file); t = t.replace(old, next); write(h.file, t); }
  }

  // print report
  console.log('\n=== propagate ' + base + (dryRun ? ' (DRY RUN)' : '') + ' ===');
  for (const m of report.masters) {
    console.log('master: ' + m.master + ' (' + m.consumers.length + ' consumers)');
    for (const c of m.consumers) {
      let line = '  ' + c.kind + ' -> ' + c.dest;
      if (c.changed === false) line += ' (unchanged)';
      if (c.aspectWarning) line += '  [!] ' + c.aspectWarning;
      if (c.raster) line += '  [raster] ' + c.raster;
      console.log(line);
    }
  }
  if (report.refs.length) {
    console.log('\n?v bumps:');
    for (const r of report.refs) console.log('  ' + r.file + ': ' + r.old + ' -> ' + r.next);
  }
  if (report.aspectWarnings.length) {
    console.log('\n[!] ASPECT-CHANGE — re-crop review:');
    for (const d of report.aspectWarnings) console.log('  ' + d);
  }
  if (report.raster.length) {
    console.log('\n[raster] re-export needed (not auto-derived):');
    for (const d of report.raster) console.log('  ' + d);
  }
  console.log('\nNeeds deploy to go live: website (.37), portal (.17) — run deploy.sh / npm run deploy:portal');
  console.log('If sales copies changed, re-build the review mirror: npm run build:review  (regenerates ui_kits/review/sales/ from sales source)');
}

// CLI
const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
if (args.includes('--audit')) { audit(); process.exit(0); }
const base = args.find(a => !a.startsWith('--'));
if (!base) { console.log('Usage: propagate-diagram.mjs <basename> [--dry-run] | --audit'); process.exit(0); }
propagate(base, dryRun);
