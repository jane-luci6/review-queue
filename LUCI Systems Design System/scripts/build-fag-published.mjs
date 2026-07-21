#!/usr/bin/env node
// Derives field-activation-guide-web-published.html from the detailed
// field-activation-guide-web.html: swaps each "How to do it" accordion for
// a per-use-case "Learn more in the support portal" link (or a portal
// fallback where no KB article exists), and adds a per-section
// "Need a hand? Contact your FDE / browse the support portal" line.
// Re-run after any change to the detailed page or the links JSON.

import fs from 'node:fs';
import path from 'node:path';

const dir = 'LUCI Systems Design System/ui_kits/sales';
const htmlPath = path.join(dir, 'field-activation-guide-web.html');
const linksPath = path.join(dir, 'field-activation-links.json');
const outPath = path.join(dir, 'field-activation-guide-web-published.html');

const html = fs.readFileSync(htmlPath, 'utf8');
const links = JSON.parse(fs.readFileSync(linksPath, 'utf8'));
const portal = links.supportPortal;
const bySlug = Object.fromEntries(links.links.map(l => [l.slug, l]));

// panel-id prefix (e.g. "m1") -> use-case slug
const panelToSlug = {
  m1: 'marketing-push-message', m2: 'marketing-daypart-promotions', m3: 'marketing-zone-content', m4: 'marketing-event-campaign',
  g1: 'gaming-floor-audio', g2: 'gaming-jackpot-event', g3: 'gaming-reconfigure-property', g4: 'gaming-new-game-launch',
  a1: 'av-property-schedule', a2: 'av-service-requests', a3: 'av-find-problems', a4: 'av-private-event',
  i1: 'it-add-endpoint', i2: 'it-config-docs', i3: 'it-permissions', i4: 'it-kiosk',
  gm1: 'gm-walk-floor-ipad', gm2: 'gm-morning-reset', gm4: 'gm-team-adoption',
};

// Return index just past the </div> that closes the <div class="fag-acc"> at startIdx.
function blockEnd(h, startIdx) {
  let i = h.indexOf('>', startIdx) + 1;
  let depth = 1;
  while (i < h.length && depth > 0) {
    const o = h.indexOf('<div', i);
    const c = h.indexOf('</div>', i);
    if (c === -1) return -1;
    if (o !== -1 && o < c) { depth++; i = o + 4; }
    else { depth--; i = c + 6; }
  }
  return i;
}

function learnBlock(link) {
  const ind = '      ';
  const chev = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 6 15 12 9 18"/></svg>';
  if (link && link.url) {
    return `${ind}<div class="fag-learn"><a href="${link.url}" target="_blank" rel="noopener"><span>Learn more</span>${chev}</a><span class="fag-learn__article">${link.article}</span></div>\n`;
  }
  return `${ind}<div class="fag-learn"><a href="${portal}" target="_blank" rel="noopener"><span>Browse the support portal</span>${chev}</a></div>\n`;
}

// 1) Replace each fag-acc accordion with a learn-more link.
let out = '';
let cursor = 0;
let accStart = html.indexOf('<div class="fag-acc">', cursor);
const report = [];
while (accStart !== -1) {
  out += html.slice(cursor, accStart);
  const end = blockEnd(html, accStart);
  const block = html.slice(accStart, end);
  const idMatch = block.match(/id="([^"]+)-panel"/);
  const panelId = idMatch ? idMatch[1] : null;
  const slug = panelToSlug[panelId];
  const link = slug ? bySlug[slug] : null;
  out += learnBlock(link);
  report.push(`${panelId || '?'} -> ${slug || '?'} -> ${link && link.url ? link.article : 'PORTAL FALLBACK'}`);
  cursor = end;
  accStart = html.indexOf('<div class="fag-acc">', cursor);
}
out += html.slice(cursor);

// 2) Add a per-section "Need a hand?" line before each fag-sec </section>.
const helpLine = `    <p class="fag-sec__help"><strong>Need a hand?</strong> Your FDE can walk you through any of this &mdash; or <a href="${portal}" target="_blank" rel="noopener">browse the support portal</a> for the step-by-step guides.</p>`;
out = out.replace(/(<\/aside>)(\s*?)(<\/section>)/g, `$1$2${helpLine}$2$3`);

// 2b) Drop the floating "Need a hand?" pill — the per-section help line + the
// conclusion's FDE line already cover contact; the pill is now redundant.
out = out.replace(/<a class="fag-fab"[\s\S]*?<\/a>/, '');

// 2c) Replace the whole <script> block: drop the dead accordion JS and the
// FAB-visibility JS (no .fag-acc__btn or .fag-fab remain); keep the scroll-spy
// that highlights the active persona in the sticky nav.
const cleanScript = `<script>
  (function () {
    // Scroll-spy: highlight the active persona link in the sticky nav
    var links = Array.prototype.slice.call(document.querySelectorAll('.fag-nav__link'));
    var sections = links.map(function (l) { return document.querySelector(l.getAttribute('href')); }).filter(Boolean);
    if ('IntersectionObserver' in window && sections.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            var id = e.target.id;
            links.forEach(function (l) { l.classList.toggle('is-active', l.getAttribute('href') === '#' + id); });
          }
        });
      }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
      sections.forEach(function (s) { io.observe(s); });
    }
  })();
</script>`;
out = out.replace(/<script>[\s\S]*?<\/script>/, cleanScript);

// 2d) Normalize to LF for a clean generated artifact.
out = out.replace(/\r\n/g, '\n');

// 3) Inject CSS for the new classes (after the first <style> open).
const css = `
    /* published-variant: learn-more pill (matches hub "Jump to your team" CTA) + section help line */
    .fag-learn{margin-top:20px;padding-top:16px;border-top:1px solid rgba(104,227,190,.18);}
    .fag-learn a{display:inline-flex;align-items:center;gap:10px;padding:13px 26px;background:linear-gradient(100deg,var(--gold-deep) 0%,var(--mint) 78%);color:var(--navy-deep);border-radius:9999px;font-family:var(--font-head);font-weight:700;font-size:13px;letter-spacing:0.06em;text-transform:uppercase;text-decoration:none;transition:transform .18s ease-out,box-shadow .18s ease-out;}
    .fag-learn a:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(206,176,110,.32);}
    .fag-learn a svg{width:16px;height:16px;}
    .fag-learn__article{display:block;margin-top:10px;font-family:'Inter',sans-serif;font-size:13px;color:var(--ink-mute,#7d8e97);line-height:1.5;}
    .fag-sec__help{margin:28px 0 0;padding:14px 0 0;border-top:1px solid rgba(104,227,190,.14);font-family:'Inter',sans-serif;font-size:14px;color:var(--ink-mute,#7d8e97);line-height:1.6;}
    .fag-sec__help strong{color:var(--ink-strong,#0A161C);font-weight:600;}
    .fag-sec__help a{color:var(--mint,#68E3BE);font-weight:600;text-decoration:none;}
    .fag-sec__help a:hover{text-decoration:underline;}
    .fag-sec--light .fag-sec__help strong{color:var(--ink-strong,#1A1A1A);}
`;
out = out.replace(/(<style[^>]*>)/, `$1${css}`);

fs.writeFileSync(outPath, out);
console.log(`wrote ${outPath}`);
console.log(`replaced ${report.length} accordions:`);
report.forEach(r => console.log('  ' + r));
