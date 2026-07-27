#!/usr/bin/env node
/**
 * Builds the hosted Internal Marketing Materials Portal output in ui_kits/review/:
 * generates review-queue.json + library-manifest.json, copies the internal portal,
 * Customization Studio preview docs, sales PDFs, email library, messaging docs,
 * and queue-linked preview assets. Served statically (root rewrites to
 * /internal-portal/index.html). Comments/approvals sync server-side via the
 * comments_api container (nginx-proxied at /api/comments); localStorage is a
 * cache + offline fallback. Archive live feedback with scripts/pull-review-comments.mjs.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { syncMessagingDocs, applyMessagingDocsToQueue } from './sync-messaging-docs.mjs';
import { syncReviewVersions } from './sync-review-versions.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(path.join(__dirname, '..'));
const reviewDir = path.join(root, 'ui_kits', 'review');

const ASSET_REF =
  /(?:src|href|poster)=["'](?!https?:|#|mailto:|tel:|data:)([^"']+)["']/gi;

const CSS_URL_REF = /url\(['"]?([^'"\)\s?#]+)['"]?\)/gi;

const SALES_ASSET_SKIP = /(?:\.orig\.png$|^hardware-|luci-floor-control-static|interface-floor-view\.orig)/i;

function queueItems(queue) {
  return [...(queue.dueForReview || []), ...(queue.upcoming || [])];
}

/** Resolve design-system source HTML for an asset (hub path wins). */
function sourceHtmlPath(item) {
  const hub = (item.hubPreviewPath || '').trim();
  if (hub) return path.join(root, hub);
  const prev = (item.previewUrl || '').trim();
  if (!prev || /^https?:\/\//i.test(prev)) return null;
  const cleaned = prev.replace(/^\.\.\//, '');
  if (cleaned.startsWith('ui_kits/')) return path.join(root, cleaned);
  return path.join(reviewDir, cleaned);
}

/** Published path under the review site root (no Preview Hub). */
function publishPreviewPath(item) {
  const hub = (item.hubPreviewPath || '').trim();
  if (hub) return hub.replace(/^ui_kits\//, '');
  const prev = (item.previewUrl || '').trim();
  if (!prev || /^https?:\/\//i.test(prev)) return '';
  return prev.replace(/^\.\.\//, '').replace(/^ui_kits\//, '');
}

function ensureDir(filePath) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
}

function copyFile(src, dest, copied) {
  if (!src || !fs.existsSync(src) || copied.has(src)) return false;
  ensureDir(dest);
  fs.copyFileSync(src, dest);
  copied.add(src);
  return true;
}

/** Published HTML uses root-absolute /assets/ so logos load inside the iframe on Netlify. */
function rewritePreviewHtmlPaths(destHtmlPath) {
  let html = fs.readFileSync(destHtmlPath, 'utf8');
  html = html.replace(/\.\.\/review\/assets\//g, '/assets/');
  html = html.replace(/\.\.\/\.\.\/assets\//g, '/assets/');
  html = html.replace(/\.\.\/assets\//g, '/assets/');
  html = html.replace(/<p class="(?:cap|doc)-hub-link">[\s\S]*?<\/p>\s*/gi, '');
  fs.writeFileSync(destHtmlPath, html);
}

function copyDirRecursive(srcDir, destDir, copied) {
  if (!fs.existsSync(srcDir)) return;
  for (const entry of fs.readdirSync(srcDir, { withFileTypes: true })) {
    if (entry.name.startsWith('.')) continue;
    const src = path.join(srcDir, entry.name);
    const dest = path.join(destDir, entry.name);
    if (entry.isDirectory()) {
      fs.mkdirSync(dest, { recursive: true });
      copyDirRecursive(src, dest, copied);
    } else {
      copyFile(src, dest, copied);
    }
  }
}

function publishAssetCopy(sourceAsset, destAsset, copied) {
  if (!sourceAsset.startsWith(root) || !fs.existsSync(sourceAsset)) return false;
  if (SALES_ASSET_SKIP.test(path.basename(sourceAsset))) return false;
  const newlyCopied = copyFile(sourceAsset, destAsset, copied);
  if (!newlyCopied || !fs.statSync(sourceAsset).isFile()) return newlyCopied;
  if (/\.html?$/i.test(sourceAsset)) copyLinkedAssets(sourceAsset, destAsset, copied);
  return newlyCopied;
}

function resolveAndCopyRef(ref, baseDir, destDir, copied) {
  const clean = ref.trim().split(/[?#]/)[0];
  if (!clean || clean.startsWith('/') || clean.startsWith('data:')) return;
  const sourceAsset = path.resolve(baseDir, clean);
  if (!sourceAsset.startsWith(root)) return;
  if (sourceAsset === reviewDir || sourceAsset.startsWith(reviewDir + path.sep)) return;
  const relFromRoot = path.relative(root, sourceAsset);
  if (relFromRoot.startsWith('..')) return;
  const relFromBase = path.relative(baseDir, sourceAsset);
  const destAsset =
    relFromBase && !relFromBase.startsWith('..') && !path.isAbsolute(relFromBase)
      ? path.join(destDir, relFromBase)
      : path.join(reviewDir, relFromRoot);
  publishAssetCopy(sourceAsset, destAsset, copied);
}

function copyCssLinkedAssets(cssFile, destCssFile, copied) {
  if (!fs.existsSync(cssFile)) return;
  let css = fs.readFileSync(cssFile, 'utf8');
  const cssDir = path.dirname(cssFile);
  const destDir = path.dirname(destCssFile);
  let match;
  CSS_URL_REF.lastIndex = 0;
  while ((match = CSS_URL_REF.exec(css)) !== null) {
    resolveAndCopyRef(match[1], cssDir, destDir, copied);
  }
}

function copySalesAssetsForDoc(publishPath, copied) {
  if (!publishPath.startsWith('sales/')) return;
  const srcHtml = path.join(root, 'ui_kits', publishPath);
  if (!fs.existsSync(srcHtml)) return;
  const destHtml = path.join(reviewDir, publishPath);
  copyLinkedAssets(srcHtml, destHtml, copied);
  const html = fs.readFileSync(srcHtml, 'utf8');
  const htmlDir = path.dirname(srcHtml);
  const destDir = path.dirname(destHtml);
  const linkRe = /<link[^>]+rel=["']stylesheet["'][^>]+href=["']([^"']+)["']|<link[^>]+href=["']([^"']+)["'][^>]+rel=["']stylesheet["']/gi;
  let m;
  while ((m = linkRe.exec(html)) !== null) {
    const href = (m[1] || m[2] || '').split(/[?#]/)[0];
    if (!href || href.startsWith('http') || href.startsWith('/')) continue;
    const cssPath = path.resolve(htmlDir, href);
    const destCss = path.join(destDir, path.relative(htmlDir, cssPath));
    copyCssLinkedAssets(cssPath, destCss, copied);
  }
}

function copySalesBundle(publishPath, copied) {
  copySalesAssetsForDoc(publishPath, copied);
}

function collectManifestAssetRefs(refs) {
  const manifestPath = path.join(reviewDir, 'library-manifest.json');
  if (!fs.existsSync(manifestPath)) return;
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  for (const group of manifest.groups || []) {
    for (const item of group.items || []) {
      for (const dl of item.downloads || []) {
        if (dl.path && String(dl.path).startsWith('assets/')) refs.add(String(dl.path).split(/[?#]/)[0]);
      }
    }
  }
}

function collectHtmlAssetRefs(htmlFile, refs) {
  if (!fs.existsSync(htmlFile)) return;
  const html = fs.readFileSync(htmlFile, 'utf8');
  const baseDir = path.dirname(htmlFile);
  let match;
  ASSET_REF.lastIndex = 0;
  while ((match = ASSET_REF.exec(html)) !== null) {
    const ref = match[1].trim().split(/[?#]/)[0];
    if (!ref || ref.startsWith('/')) continue;
    const resolved = path.resolve(baseDir, ref);
    if (!resolved.startsWith(root)) continue;
    const rel = path.relative(root, resolved);
    if (!rel.startsWith('..') && rel.startsWith('assets/')) refs.add(rel);
  }
}

function syncSharedAssets(copied) {
  const refs = new Set([
    'assets/fonts/luci-brand-fonts.css',
    'assets/logos/luci-full-white.png',
    'assets/logos/luci-full-mintmark-blacktext.png',
    'assets/logos/luci-full-mintmark-white.png',
  ]);
  collectManifestAssetRefs(refs);
  const messagingDir = path.join(reviewDir, 'messaging');
  if (fs.existsSync(messagingDir)) {
    for (const name of fs.readdirSync(messagingDir)) {
      if (!/\.html?$/i.test(name)) continue;
      collectHtmlAssetRefs(path.join(messagingDir, name), refs);
    }
  }
  for (const rel of refs) {
    const src = path.join(root, rel);
    const dest = path.join(reviewDir, rel);
    publishAssetCopy(src, dest, copied);
  }
}

/** Copy sales PDFs (brochure, case study) into the review site so download links resolve. */
function syncSalesPdfs(copied) {
  const srcDir = path.join(root, 'assets', 'sales');
  const destDir = path.join(reviewDir, 'assets', 'sales');
  if (!fs.existsSync(srcDir)) return;
  fs.mkdirSync(destDir, { recursive: true });
  for (const name of fs.readdirSync(srcDir)) {
    if (!/\.pdf$/i.test(name)) continue;
    copyFile(path.join(srcDir, name), path.join(destDir, name), copied);
  }
}

/** Co-located customization masters + skills (internal-portal/customization/<id>/). */
const CUSTOMIZATION_TEMPLATES = [
  { id: 'capabilities-document', src: 'sales/capabilities-document.html' },
  { id: 'sales-deck', src: 'sales/sales-deck.html' },
  { id: 'scope-of-work', src: 'sales/scope-of-work.html' },
  { id: 'proposal', src: 'sales/proposal.html' },
  { id: 'budgetary-estimate', src: 'sales/budgetary-estimate.html' },
];

/** Portal origin for Cursor context injection (Mike pastes preview URL in chat). */
const PORTAL_ORIGIN = 'http://10.10.1.17:8081';

const CURSOR_DOC_META = {
  'capabilities-document': {
    title: 'Capabilities document',
    master: 'LUCI Systems Design System/ui_kits/sales/capabilities-document.html',
    clientFile: 'LUCI Systems Design System/ui_kits/sales/{client}-capabilities.html',
    editMode: {
      enabled: true,
      hint: 'Click mint-highlighted text on the cover and close page to edit. Pages 2–8 are locked.',
      lockedPages:
        '.cap-page--what, .cap-page--why, .doc-page--reduces, .doc-page--architecture, .doc-page--systems, .doc-page--deployment, .doc-page--proof',
      lockedElements: '.doc-cover__logo, .doc-close__logo, .doc-close__company',
    },
  },
  'sales-deck': {
    title: 'Sales deck',
    master: 'LUCI Systems Design System/ui_kits/sales/sales-deck.html',
    clientFile: 'LUCI Systems Design System/ui_kits/sales/{client}-sales-deck.html',
    editMode: {
      enabled: true,
      hint: 'Click highlighted text on slides 1–2 to edit copy. Swap client logo and property photos in the baked-in slots. Slides 3–12 are locked.',
      lockedPages: '#s3, #s4, #s5, #s6, #s7, #s8, #s9, #s10, #s11, #s12, #s2 .s-foot',
      lockedElements: '.cover__logo, .cover__rule, .close__logo',
    },
  },
  'scope-of-work': {
    title: 'Scope of work',
    master: 'LUCI Systems Design System/ui_kits/sales/scope-of-work.html',
    clientFile: 'LUCI Systems Design System/ui_kits/sales/{client}-scope-of-work.html',
    editMode: {
      enabled: true,
      hint: 'Click highlighted text to edit scope sections. LUCI cover logo stays locked.',
      lockedPages: '',
      lockedElements: '.doc-cover__logo',
    },
  },
  'proposal': {
    title: 'Proposal',
    master: 'LUCI Systems Design System/ui_kits/sales/proposal.html',
    clientFile: 'LUCI Systems Design System/ui_kits/sales/{client}-proposal.html',
    editMode: {
      enabled: true,
      hint: 'Click highlighted text to edit cover, scope, specs, fee, estimates, terms, and the close page. COB advantage + architecture boilerplate (page 3), spec schema labels, warranty grid, and gallery layout stay locked.',
      lockedPages: '.doc-page--led-advantage',
      lockedElements: '.doc-cover__logo, .led-advantage-grid, .led-arch-text, .led-terms-grid, .led-spec-row__label',
    },
  },
  'budgetary-estimate': {
    title: 'Budgetary estimate',
    master: 'LUCI Systems Design System/ui_kits/sales/budgetary-estimate.html',
    clientFile: 'LUCI Systems Design System/ui_kits/sales/{client}-budgetary-estimate.html',
    editMode: {
      enabled: true,
      hint: 'Edit cover hero/summary, the page-2 intro statement, scope items, proposal figures, investment totals, tiers, and close contact. The What-LUCI-is identity + feature cards, delivers grid, and close panel stay locked.',
      lockedPages: '.be-delivers',
      lockedElements: '.doc-cover__logo, .be-why, .be-close',
    },
  },
};

function injectCursorContext(html, templateId, fileName) {
  const meta = CURSOR_DOC_META[templateId];
  if (!meta) return html;
  const base = `${PORTAL_ORIGIN}/internal-portal/customization`;
  const previewPath = `${base}/${templateId}/${fileName}`;
  const context = {
    version: 1,
    docId: templateId,
    title: meta.title,
    portalOrigin: PORTAL_ORIGIN,
    previewUrl: previewPath,
    skills: {
      router: `${base}/CURSOR.md`,
      brand: `${base}/_brand/SKILL.md`,
      template: `${base}/${templateId}/SKILL.md`,
      agents: `${base}/${templateId}/AGENTS.md`,
      manifest: `${base}/cursor-manifest.json`,
    },
    source: { master: meta.master, clientFile: meta.clientFile },
    editMode: meta.editMode,
    workflow:
      'Paste this page URL into Cursor chat. Agent fetches the skill URLs above before editing. No specific folder required. Open the same URL in a browser to click-edit highlighted text.',
  };
  const editAssets = [
    `<link rel="stylesheet" href="${base}/luci-doc-edit.css">`,
    `<script src="${base}/luci-doc-edit.js" defer></script>`,
  ].join('\n  ');
  const block = [
    `<!-- luci-cursor-doc: ${templateId} -->`,
    `<script type="application/json" id="luci-cursor-context">${JSON.stringify(context)}</script>`,
    editAssets,
  ].join('\n  ');
  if (html.includes('id="luci-cursor-context"')) return html;
  return html.replace(/<head>/i, `<head>\n  ${block}`);
}

function rewriteCustomizationHtml(html, templateId, fileName) {
  let out = html;
  out = out.replace(/<p class="(?:cap|doc)-hub-link">[\s\S]*?<\/p>\s*/gi, '');
  out = out.replace(/\.\.\/\.\.\/assets\//g, '/assets/');
  out = out.replace(/\.\.\/assets\//g, '/assets/');
  out = out.replace(/href="sales-document\.css[^"]*"/gi, 'href="/sales/sales-document.css?v=4"');
  out = out.replace(/href="capabilities-document\.css[^"]*"/gi, 'href="/sales/capabilities-document.css"');
  out = out.replace(/href="brochure\.css[^"]*"/gi, 'href="/sales/brochure.css?v=3"');
  out = out.replace(/href="scope-of-work\.css[^"]*"/gi, 'href="/sales/scope-of-work.css?v=20"');
  out = out.replace(/href="proposal\.css[^"]*"/gi, 'href="/sales/proposal.css?v=3"');
  out = out.replace(/href="budgetary-estimate\.css[^"]*"/gi, 'href="/sales/budgetary-estimate.css?v=20"');
  out = out.replace(/href="sales-deck\.css[^"]*"/gi, 'href="/sales/sales-deck.css"');
  out = out.replace(/src="assets\//g, 'src="/sales/assets/');
  // Inline base64 logos bloat the file (~180KB) and slow Cursor remote indexing/chat.
  out = out.replace(/src="data:image\/[^"]+"/g, 'src="/assets/logos/luci-full-white.png"');
  // Source masters inline base64 fonts + link the same CSS — keep link only for Cursor.
  out = out.replace(/<style data-luci-fonts>[\s\S]*?<\/style>\s*/gi, '');
  out = injectCursorContext(out, templateId, fileName);
  return out;
}

function syncCustomizationBundles(copied) {
  const portalCustomization = path.join(reviewDir, 'internal-portal', 'customization');
  for (const { id, src } of CUSTOMIZATION_TEMPLATES) {
    const srcHtml = path.join(root, 'ui_kits', src);
    const fileName = path.basename(src);
    const destHtml = path.join(portalCustomization, id, fileName);
    if (!fs.existsSync(srcHtml)) {
      console.warn('Customization skip (missing):', src);
      continue;
    }
    fs.mkdirSync(path.dirname(destHtml), { recursive: true });
    const html = rewriteCustomizationHtml(fs.readFileSync(srcHtml, 'utf8'), id, fileName);
    fs.writeFileSync(destHtml, html);
    copySalesBundle(`sales/${fileName}`, copied);
    console.log('Customization template:', path.relative(reviewDir, destHtml));
  }
}

/** Copy HTML used as Customization Studio previews (not in the queue) so they resolve when hosted.
 *  Also writes studio-manifest.json mapping each template id -> source file's last-modified date,
 *  so the Customization Studio can show an accurate "Last updated" without manual bumps. */
function syncStudioPreviews(copied) {
  const studioPreviews = ['sales/capabilities-document.html', 'sales/sales-deck.html', 'sales/budgetary-estimate.html', 'sales/scope-of-work.html', 'sales/proposal.html', 'guides/lg-device-setup-guide.html'];
  const STUDIO_ID = {
    'sales/capabilities-document.html': 'capabilities',
    'sales/sales-deck.html': 'sales-deck',
    'sales/budgetary-estimate.html': 'budget-estimate',
    'sales/scope-of-work.html': 'scope-of-work',
    'sales/proposal.html': 'proposal',
    'guides/lg-device-setup-guide.html': 'lg-setup',
  };
  const updated = {};
  for (const rel of studioPreviews) {
    const srcHtml = path.join(root, 'ui_kits', rel);
    const destHtml = path.join(reviewDir, rel);
    if (!fs.existsSync(srcHtml)) continue;
    copyFile(srcHtml, destHtml, copied);
    copyLinkedAssets(srcHtml, destHtml, copied);
    copySalesBundle(rel, copied);
    rewritePreviewHtmlPaths(destHtml);
    const id = STUDIO_ID[rel];
    if (id) updated[id] = new Date(fs.statSync(srcHtml).mtimeMs).toISOString().slice(0, 10);
    console.log('Studio preview:', rel);
  }
  fs.writeFileSync(path.join(reviewDir, 'studio-manifest.json'), JSON.stringify(updated, null, 2) + '\n');
  console.log('Studio manifest: ui_kits/review/studio-manifest.json');
}

function copyLinkedAssets(htmlFile, destHtmlFile, copied) {
  const html = fs.readFileSync(htmlFile, 'utf8');
  const sourceDir = path.dirname(htmlFile);
  const destDir = path.dirname(destHtmlFile);

  function copyRef(rawRef) {
    const ref = rawRef.trim().split(/[?#]/)[0];
    if (!ref || ref.startsWith('/')) return;
    const sourceAsset = path.resolve(sourceDir, ref);
    if (!fs.existsSync(sourceAsset) || !sourceAsset.startsWith(root)) return;
    // Skip assets already inside the review output dir. Copying them back in
    // self-replicates into review/ui_kits/review/ (triggered by docs that link
    // into ../review/...). They're already at their published location.
    if (sourceAsset === reviewDir || sourceAsset.startsWith(reviewDir + path.sep)) return;
    const relFromRoot = path.relative(root, sourceAsset);
    if (relFromRoot.startsWith('..')) return;
    if (relFromRoot === 'index.html' || relFromRoot.startsWith('preview/')) return;

    const relFromSource = path.relative(sourceDir, sourceAsset);
    const destAsset =
      relFromSource && !relFromSource.startsWith('..') && !path.isAbsolute(relFromSource)
        ? path.join(destDir, relFromSource)
        : path.join(reviewDir, relFromRoot);

    const newlyCopied = copyFile(sourceAsset, destAsset, copied);
    if (!newlyCopied) return;
    if (fs.statSync(sourceAsset).isDirectory()) return;
    if (/\.html?$/i.test(sourceAsset)) {
      copyLinkedAssets(sourceAsset, destAsset, copied);
    }
  }

  let match;
  ASSET_REF.lastIndex = 0;
  while ((match = ASSET_REF.exec(html)) !== null) {
    copyRef(match[1]);
  }
  // Inline CSS url() refs (e.g. background textures in <style> blocks)
  CSS_URL_REF.lastIndex = 0;
  while ((match = CSS_URL_REF.exec(html)) !== null) {
    copyRef(match[1]);
  }
}

function syncEmailLibrary(copied) {
  const emailSrc = path.join(root, 'ui_kits', 'email');
  const emailDest = path.join(reviewDir, 'email');
  const files = [
    'customer-journey-tracker.html',
    'customer-journey-data.js',
    'email-subjects-preheaders.html',
  ];
  for (const name of files) {
    const src = path.join(emailSrc, name);
    const dest = path.join(emailDest, name);
    if (!fs.existsSync(src)) continue;
    copyFile(src, dest, copied);
    if (/\.html?$/i.test(name)) {
      copyLinkedAssets(src, dest, copied);
      rewritePreviewHtmlPaths(dest);
    }
    console.log('Email library:', path.relative(reviewDir, dest));
  }
}

function syncInternalPortal(copied) {
  const portalSrc = path.join(root, 'ui_kits', 'internal-portal');
  const portalDest = path.join(reviewDir, 'internal-portal');
  if (!fs.existsSync(portalSrc)) return;
  if (fs.existsSync(portalDest)) fs.rmSync(portalDest, { recursive: true, force: true });
  copyDirRecursive(portalSrc, portalDest, copied);
  console.log('Internal portal:', path.relative(reviewDir, portalDest));
}

function cleanGeneratedPreviews() {
  for (const name of ['case-studies', 'assets', 'newsletter', 'emails', 'website', 'sales']) {
    const dir = path.join(reviewDir, name);
    if (fs.existsSync(dir)) fs.rmSync(dir, { recursive: true, force: true });
  }
}

/** System diagram lives under messaging/ (not wiped by cleanGeneratedPreviews).
 *  Retired from canonical — messaging/diagrams/luci-system-diagram-v3.svg is now the
 *  source of truth. This no-ops when the canonical master is absent. */
function syncMessagingDiagram() {
  const canonical = path.join(root, 'assets', 'diagrams', 'luci-system-diagram-v3.svg');
  const destDir = path.join(reviewDir, 'messaging', 'diagrams');
  const dest = path.join(destDir, 'luci-system-diagram-v3.svg');
  fs.mkdirSync(destDir, { recursive: true });
  if (!fs.existsSync(canonical) && !fs.existsSync(dest)) return;
  if (!fs.existsSync(canonical)) return;
  if (!fs.existsSync(dest)) {
    fs.copyFileSync(canonical, dest);
    console.log('Messaging diagram:', path.relative(reviewDir, dest));
    return;
  }
  const canonMtime = fs.statSync(canonical).mtimeMs;
  const destMtime = fs.statSync(dest).mtimeMs;
  if (canonMtime >= destMtime) {
    fs.copyFileSync(canonical, dest);
    console.log('Messaging diagram:', path.relative(reviewDir, dest));
  }
}

function syncPreviewAssets(queue) {
  cleanGeneratedPreviews();
  const copied = new Set();
  let count = 0;

  syncSharedAssets(copied);
  syncSalesPdfs(copied);
  syncEmailLibrary(copied);
  syncInternalPortal(copied);
  syncStudioPreviews(copied);
  syncCustomizationBundles(copied);

  const previewQueueItems = [
    ...(queue.dueForReview || []),
    ...(queue.inProgress || []),
    ...(queue.approvedAssets || []).filter((item) => item.hubPreviewPath || item.previewUrl),
  ];
  for (const item of previewQueueItems) {
    if ((item.liveUrl || '').trim() && item.embedPreview !== true) continue;
    const srcHtml = sourceHtmlPath(item);
    const publishPath = publishPreviewPath(item);
    if (!srcHtml || !publishPath || !fs.existsSync(srcHtml)) continue;

    const destHtml = path.join(reviewDir, publishPath);
    copyFile(srcHtml, destHtml, copied);
    copyLinkedAssets(srcHtml, destHtml, copied);
    copySalesBundle(publishPath, copied);
    rewritePreviewHtmlPaths(destHtml);
    item.previewUrl = publishPath;
    count += 1;
    console.log('Preview asset:', publishPath);
  }

  const needsPreview = [...(queue.dueForReview || []), ...(queue.inProgress || [])].filter(
    (item) => !(item.liveUrl || '').trim() || item.embedPreview === true
  );
  if (needsPreview.length && count === 0) {
    console.error('Build failed: queue items need previews but nothing was copied.');
    process.exit(1);
  }
  for (const item of needsPreview) {
    const publishPath = publishPreviewPath(item);
    if (!publishPath) continue;
    const dest = path.join(reviewDir, publishPath);
    if (!fs.existsSync(dest)) {
      console.error('Build failed: missing preview file', dest);
      process.exit(1);
    }
  }

  return count;
}

/** Root redirect so static hosts (VM python/nginx) open the portal at /. */
function writePortalRootIndex() {
  const indexPath = path.join(reviewDir, 'index.html');
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=internal-portal/index.html">
  <title>Internal Marketing Portal</title>
  <script>location.replace('internal-portal/index.html');</script>
</head>
<body><p><a href="internal-portal/index.html">Internal Marketing Portal</a></p></body>
</html>
`;
  fs.writeFileSync(indexPath, html);
}

const queuePath = path.join(reviewDir, 'review-queue.json');
const queue = JSON.parse(fs.readFileSync(queuePath, 'utf8'));

try {
  syncMessagingDocs({ quiet: true });
} catch (e) {
  console.warn('Messaging sync skipped:', e.message || e);
}
applyMessagingDocsToQueue(queue);

syncMessagingDiagram();
const previewCount = syncPreviewAssets(queue);

if (syncReviewVersions(queue, queuePath)) {
  console.log('Updated review-queue.json (version history).');
}

writePortalRootIndex();

console.log('Build complete. Portal root: ui_kits/review/internal-portal/index.html');
console.log('Synced', previewCount, 'preview bundle(s) into ui_kits/review/');
