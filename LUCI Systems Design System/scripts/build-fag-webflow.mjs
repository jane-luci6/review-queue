#!/usr/bin/env node
// Splits field-activation-guide-web-published.html into Webflow custom-code embeds:
//   *-webflow-head.html  -> paste into Webflow Page Settings > "Before </head>" tag
//   *-webflow-body.html  -> paste into Webflow Page Settings > "Before </body>" tag
// Minimal-viable scoping: the .fag-* classnames are unique and won't clash with the
// Webflow site, so we only neutralize the rules that WOULD leak globally — :root vars,
// the universal *, html, and body — by re-homing them under a .luci-fag wrapper that
// also wraps the body markup. Fonts load via Google Fonts <link> (lightweight; fits Webflow's
// custom-code char limit). Also emits a combined *-webflow-preview.html for local review.

import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const sales = join(here, '..', 'ui_kits', 'sales');
const src = join(sales, 'field-activation-guide-web-published.html');
const base = 'field-activation-guide-web-published';
const html = readFileSync(src, 'utf8');

// --- 1. extract <style id="fag-web-css"> ... </style> ---
const styleMatch = html.match(/<style id="fag-web-css">([\s\S]*?)<\/style>/);
if (!styleMatch) throw new Error('no fag-web-css style block found');
let css = styleMatch[1];

// --- 2. scope the leaking rules under .luci-fag ---
css = css.replace(/^  :root \{/gm, '  .luci-fag {');           // both :root blocks -> .luci-fag
css = css.replace(/^  \* \{ box-sizing: border-box; \}/m, '  .luci-fag * { box-sizing: border-box; }');
css = css.replace(/^  html \{ scroll-behavior: smooth; \}\n/m, ''); // drop global html rule
css = css.replace(/ html \{ scroll-behavior: auto; \}/m, '');      // drop html inside @media
css = css.replace(/^  body \{/m, '  .luci-fag {');               // body styles -> wrapper

// --- 3. extract <body> ... </body> inner ---
const bodyMatch = html.match(/<body>([\s\S]*?)<\/body>/);
if (!bodyMatch) throw new Error('no body found');
let bodyInner = bodyMatch[1];

// pull the <script> out of the body so we can place it after the markup in the body embed
const scriptMatch = bodyInner.match(/(\s*)(<script>[\s\S]*?<\/script>)/);
let script = '';
if (scriptMatch) {
  script = scriptMatch[2];
  bodyInner = bodyInner.replace(scriptMatch[2], '').replace(/\s+$/, '');
}

// wrap markup in the scope wrapper
const wrappedBody = `<div class="luci-fag">\n${bodyInner.trim()}\n</div>`;

// --- 4. fonts: Google Fonts <link> (Space Grotesk + Inter + Syncopate) ---
const fontsLink = `<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Inter:wght@400;600;700&family=Syncopate:wght@400;700&display=swap">`;

// --- 5. write head + body embeds ---
const headEmbed = `<!-- LUCI Field Activation Guide — Webflow "Before </head>" embed.
     Paste into: Webflow Page Settings > Custom Code > "Before </head>" tag.
     Self-contained: scoped CSS + Google Fonts. No global body/html styles leak. -->
${fontsLink}
<style>
${css.trim()}
</style>`;

const bodyEmbed = `<!-- LUCI Field Activation Guide — Webflow "Before </body>" embed.
     Paste into: Webflow Page Settings > Custom Code > "Before </body>" tag.
     Everything is wrapped in .luci-fag so the scoped CSS above applies only here. -->
${wrappedBody}
${script}
`;

writeFileSync(join(sales, `${base}-webflow-head.html`), headEmbed, 'utf8');
writeFileSync(join(sales, `${base}-webflow-body.html`), bodyEmbed, 'utf8');

// --- 6. combined preview for local review ---
const preview = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>LUCI — Field Activation Guide (Webflow embed preview)</title>
${fontsLink}
<style>
${css.trim()}
</style>
</head>
<body>
${wrappedBody}
${script}
</body>
</html>
`;
writeFileSync(join(sales, `${base}-webflow-preview.html`), preview, 'utf8');

console.log('wrote:');
console.log('  ' + join(sales, `${base}-webflow-head.html`));
console.log('  ' + join(sales, `${base}-webflow-body.html`));
console.log('  ' + join(sales, `${base}-webflow-preview.html`));
