#!/usr/bin/env node
/**
 * Inlines review-queue.json + review-comments.json into stakeholder-review.html,
 * copies queue-linked preview assets into ui_kits/review/ for Netlify publish,
 * and writes stakeholder-review-webflow-embed.html (same content).
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, '..');
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
  if (!src || !fs.existsSync(src) || copied.has(src)) return;
  ensureDir(dest);
  fs.copyFileSync(src, dest);
  copied.add(src);
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
    const destAsset = path.join(reviewDir, relFromRoot);
    copyFile(sourceAsset, destAsset, copied);
    if (fs.statSync(sourceAsset).isDirectory()) continue;
    if (/\.html?$/i.test(sourceAsset)) {
      copyLinkedAssets(sourceAsset, destAsset, copied);
    }
  }
}

function cleanGeneratedPreviews() {
  for (const name of ['case-studies', 'assets', 'newsletter', 'emails', 'website']) {
    const dir = path.join(reviewDir, name);
    if (fs.existsSync(dir)) fs.rmSync(dir, { recursive: true, force: true });
  }
}

function syncPreviewAssets(queue) {
  cleanGeneratedPreviews();
  const copied = new Set();
  let count = 0;

  for (const item of queueItems(queue)) {
    if ((item.liveUrl || '').trim() && item.embedPreview !== true) continue;
    const srcHtml = sourceHtmlPath(item);
    const publishPath = publishPreviewPath(item);
    if (!srcHtml || !publishPath || !fs.existsSync(srcHtml)) continue;

    const destHtml = path.join(reviewDir, publishPath);
    copyFile(srcHtml, destHtml, copied);
    copyLinkedAssets(srcHtml, destHtml, copied);
    item.previewUrl = publishPath;
    count += 1;
    console.log('Preview asset:', publishPath);
  }

  return count;
}

const queue = JSON.parse(fs.readFileSync(path.join(reviewDir, 'review-queue.json'), 'utf8'));
const commentsFile = JSON.parse(fs.readFileSync(path.join(reviewDir, 'review-comments.json'), 'utf8'));

const previewCount = syncPreviewAssets(queue);

const data = {
  queue,
  comments: commentsFile.comments || [],
  commentsUpdated: commentsFile.updated || '',
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
