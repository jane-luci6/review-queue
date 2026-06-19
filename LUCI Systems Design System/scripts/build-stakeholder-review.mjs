#!/usr/bin/env node
/**
 * Inlines review-queue.json + review-comments.json into stakeholder-review.html,
 * copies queue-linked preview assets into ui_kits/review/ for Netlify publish,
 * and writes stakeholder-review-webflow-embed.html (same content).
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { syncMessagingDocs, applyMessagingDocsToQueue } from './sync-messaging-docs.mjs';
import { buildLibrary } from './build-library-manifest.mjs';
import { syncReviewVersions } from './sync-review-versions.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(path.join(__dirname, '..'));
const reviewDir = path.join(root, 'ui_kits', 'review');
const templatePath = path.join(reviewDir, 'stakeholder-review.template.html');

const ASSET_REF =
  /(?:src|href)=["'](?!https?:|#|mailto:|tel:|data:)([^"']+)["']/gi;

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

function copySalesBundle(publishPath, copied) {
  if (!publishPath.startsWith('sales/')) return;
  const salesAssetsSrc = path.join(root, 'ui_kits', 'sales', 'assets');
  const salesAssetsDest = path.join(reviewDir, 'sales', 'assets');
  copyDirRecursive(salesAssetsSrc, salesAssetsDest, copied);
}

function syncSharedAssets(copied) {
  for (const rel of ['assets/logos', 'assets/diagrams']) {
    const srcDir = path.join(root, rel);
    const destDir = path.join(reviewDir, rel);
    copyDirRecursive(srcDir, destDir, copied);
  }
}

function copyLinkedAssets(htmlFile, destHtmlFile, copied) {
  const html = fs.readFileSync(htmlFile, 'utf8');
  const sourceDir = path.dirname(htmlFile);
  const destDir = path.dirname(destHtmlFile);
  let match;
  ASSET_REF.lastIndex = 0;
  while ((match = ASSET_REF.exec(html)) !== null) {
    const ref = match[1].trim();
    if (!ref || ref.startsWith('/')) continue;
    const sourceAsset = path.resolve(sourceDir, ref);
    if (!fs.existsSync(sourceAsset) || !sourceAsset.startsWith(root)) continue;
    const relFromRoot = path.relative(root, sourceAsset);
    if (relFromRoot.startsWith('..')) continue;
    if (relFromRoot === 'index.html' || relFromRoot.startsWith('preview/')) continue;

    const relFromSource = path.relative(sourceDir, sourceAsset);
    const destAsset =
      relFromSource && !relFromSource.startsWith('..') && !path.isAbsolute(relFromSource)
        ? path.join(destDir, relFromSource)
        : path.join(reviewDir, relFromRoot);

    const newlyCopied = copyFile(sourceAsset, destAsset, copied);
    if (!newlyCopied) continue;
    if (fs.statSync(sourceAsset).isDirectory()) continue;
    if (/\.html?$/i.test(sourceAsset)) {
      copyLinkedAssets(sourceAsset, destAsset, copied);
    }
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

function cleanGeneratedPreviews() {
  for (const name of ['case-studies', 'assets', 'newsletter', 'emails', 'website', 'sales']) {
    const dir = path.join(reviewDir, name);
    if (fs.existsSync(dir)) fs.rmSync(dir, { recursive: true, force: true });
  }
}

/** System diagram lives under messaging/ (not wiped by cleanGeneratedPreviews). */
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
  syncEmailLibrary(copied);

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

const queuePath = path.join(reviewDir, 'review-queue.json');
const queue = JSON.parse(fs.readFileSync(queuePath, 'utf8'));
const commentsFile = JSON.parse(fs.readFileSync(path.join(reviewDir, 'review-comments.json'), 'utf8'));
const approvalsPath = path.join(reviewDir, 'review-approvals.json');
const approvalsFile = fs.existsSync(approvalsPath)
  ? JSON.parse(fs.readFileSync(approvalsPath, 'utf8'))
  : { byAsset: {} };

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

const manifestPath = path.join(reviewDir, 'library-manifest.json');
const library = buildLibrary(manifestPath, queue);

const data = {
  queue,
  library,
  comments: commentsFile.comments || [],
  commentsUpdated: commentsFile.updated || '',
  approvals: approvalsFile.byAsset || {},
  approvalsUpdated: approvalsFile.updated || '',
};

let template = fs.readFileSync(templatePath, 'utf8');
const marker = '/*__REVIEW_DATA__*/';
const injection = 'const REVIEW_DATA = ' + JSON.stringify(data, null, 2) + ';';
if (!template.includes(marker)) {
  console.error('Template missing marker', marker);
  process.exit(1);
}
template = template.replace(marker, injection);

const outMain = path.join(reviewDir, 'stakeholder-review.html');
const outEmbed = path.join(reviewDir, 'stakeholder-review-webflow-embed.html');
const outIndex = path.join(reviewDir, 'index.html');
fs.writeFileSync(outMain, template);
fs.writeFileSync(outEmbed, template);
fs.writeFileSync(outIndex, template);
console.log('Wrote', outMain);
console.log('Wrote', outEmbed);
console.log('Wrote', outIndex);
console.log('Synced', previewCount, 'preview bundle(s) into ui_kits/review/');
