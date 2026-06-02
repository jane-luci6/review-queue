#!/usr/bin/env node
/**
 * Inlines review-queue.json + review-comments.json into stakeholder-review.html
 * and writes stakeholder-review-webflow-embed.html (same content).
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, '..');
const reviewDir = path.join(root, 'ui_kits', 'review');
const templatePath = path.join(reviewDir, 'stakeholder-review.template.html');

const queue = JSON.parse(fs.readFileSync(path.join(reviewDir, 'review-queue.json'), 'utf8'));
const commentsFile = JSON.parse(fs.readFileSync(path.join(reviewDir, 'review-comments.json'), 'utf8'));

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
