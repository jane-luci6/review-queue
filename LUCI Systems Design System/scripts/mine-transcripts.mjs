#!/usr/bin/env node
/**
 * mine-transcripts.mjs — surface social-content insights from past Cursor agent transcripts.
 *
 * Reads the .jsonl agent transcripts for this project, extracts human-readable
 * text from user and assistant turns, filters for signal (Mike on record,
 * variable-reduction moments, field & case-study moments, recurring themes),
 * and writes a markdown report + a JSON of candidate ideas into the Content Lab
 * so they can be curated into the source log / ideas backlog.
 *
 * Output:
 *   ui_kits/content-marketing/mined-insights.md   (readable report)
 *   ui_kits/content-marketing/mined-insights.json (structured candidate ideas)
 *
 * Usage:
 *   node scripts/mine-transcripts.mjs
 *   node scripts/mine-transcripts.mjs --transcripts=<path> --out-dir=<path>
 *   node scripts/mine-transcripts.mjs --audit   (counts only, no write)
 */
import fs from 'fs';
import path from 'path';
import os from 'os';
import { execFileSync } from 'child_process';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(path.join(__dirname, '..'));

const DEFAULT_TRANSCRIPTS = path.join(
  os.homedir(),
  '.cursor/projects/Users-janehaynie-Documents-Cursor-Projects-luci-design/agent-transcripts'
);
const DEFAULT_CALL_RECORDINGS = path.join(
  os.homedir(),
  'Library/CloudStorage/OneDrive-LUCISystems/Marketing - Documents/Call Recordings'
);
const DEFAULT_OUT_DIR = path.join(root, 'ui_kits', 'content-marketing');

function arg(name, fallback) {
  const m = process.argv.find((a) => a.startsWith(`--${name}=`));
  return m ? m.slice(name.length + 3) : fallback;
}

const transcriptsDir = arg('transcripts', DEFAULT_TRANSCRIPTS);
const callRecordingsDir = arg('call-recordings', DEFAULT_CALL_RECORDINGS);
const skipCallRecordings = process.argv.includes('--no-call-recordings');
const outDir = arg('out-dir', DEFAULT_OUT_DIR);
const auditOnly = process.argv.includes('--audit');

// --- Signal patterns -----------------------------------------------------
// Keyword buckets. A snippet scores into a bucket when it contains any term.
const BUCKETS = {
  mike: /\b(mike|epstein)\b/i,
  variableReduction: /\b(variable reduction|shorter list|fewer things|one interface|one rack|consolidat|reduces? the number|subtract|accumulation)\b/i,
  field: /\b(field|on[- ]site|on site|crew|before.and.after|before\/after|install|go.live|deployment|floor)\b/i,
  caseStudy: /\b(ameristar|council bluffs|tachi|palace|case study|bingo hall|riverboat)\b/i,
  audience: /\b(casino|gaming|hospitality|resort|CIO|IT director|COO|CFO|CMO|GM|general manager|director|VP|c.?suite)\b/i,
  partner: /\b(q.?sys|qsc|partner|integration|backend|routing|zone logic)\b/i,
};

// Themes we count across all snippets for the recurring-themes tally.
const THEME_TERMS = [
  'one interface', 'orchestrat', 'variable reduction', 'one rack', 'consolidat',
  'mike', 'field', 'before/after', 'case study', 'ameristar', 'tachi',
  'casino', 'gaming', 'hospitality', 'CIO', 'IT director', 'COO',
  'q-sys', 'partner', 'integration', 'LED wall', 'rack', 'guest experience',
  'align teams', 'visibility', 'control', 'appreciat',
];

// --- Text extraction -----------------------------------------------------
function stripTags(s) {
  return s
    .replace(/<system_reminder>[\s\S]*?<\/system_reminder>/gi, ' ')
    .replace(/<user_query>/gi, ' ')
    .replace(/<\/user_query>/gi, ' ')
    .replace(/<system-communication>[\s\S]*?<\/system-communication>/gi, ' ')
    .replace(/<attached_files>[\s\S]*?<\/attached_files>/gi, ' ')
    .replace(/<git_status>[\s\S]*?<\/git_status>/gi, ' ')
    .replace(/<user_info>[\s\S]*?<\/user_info>/gi, ' ')
    .replace(/<timestamp>[\s\S]*?<\/timestamp>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function textBlocks(content) {
  if (!Array.isArray(content)) return [];
  return content
    .filter((b) => b && b.type === 'text' && typeof b.text === 'string')
    .map((b) => b.text);
}

function cleanSnippet(raw) {
  const s = stripTags(raw);
  // Drop pure tool-call narration noise and very short fragments.
  if (s.length < 40) return '';
  if (/^(searching|reading|running|grep|glob|let me|i'll|i will|now )/i.test(s) && s.length < 80) return '';
  return s;
}

function readTranscript(file) {
  const lines = fs.readFileSync(file, 'utf8').split('\n').filter(Boolean);
  const turns = [];
  for (const line of lines) {
    let obj;
    try { obj = JSON.parse(line); } catch { continue; }
    const role = obj.role || '';
    const blocks = textBlocks(obj.message && obj.message.content);
    for (const b of blocks) {
      const text = cleanSnippet(b);
      if (!text) continue;
      turns.push({ role, text });
    }
  }
  return turns;
}

function findTranscriptFiles(dir) {
  if (!fs.existsSync(dir)) return [];
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const sub = path.join(dir, entry.name);
    for (const f of fs.readdirSync(sub)) {
      if (f.endsWith('.jsonl')) out.push(path.join(sub, f));
    }
  }
  return out;
}

// --- Call recording (.docx) extraction -----------------------------------
// Meeting transcripts Jane keeps in OneDrive. Each .docx is a zip; we pull
// word/document.xml and split it into <w:p> paragraphs, collecting <w:t> runs.
function extractDocxParagraphs(file) {
  let xml;
  try {
    xml = execFileSync('unzip', ['-p', file, 'word/document.xml'], { encoding: 'utf8' });
  } catch {
    return [];
  }
  const paragraphs = [];
  // Split on </w:p> boundaries; within each, grab all <w:t>…</w:t> text.
  const chunks = xml.split('</w:p>');
  for (const chunk of chunks) {
    const texts = [];
    const re = /<w:t[^>]*>([\s\S]*?)<\/w:t>/g;
    let m;
    while ((m = re.exec(chunk)) !== null) {
      texts.push(m[1].replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&apos;/g, "'"));
    }
    if (texts.length) {
      const para = texts.join('').replace(/\s+/g, ' ').trim();
      if (para) paragraphs.push(para);
    }
  }
  return paragraphs;
}

function findCallRecordings(dir) {
  if (!fs.existsSync(dir)) return [];
  const out = [];
  for (const name of fs.readdirSync(dir)) {
    if (name.toLowerCase().endsWith('.docx')) out.push(path.join(dir, name));
  }
  return out;
}

// --- Scoring / bucketing -------------------------------------------------
function snippetBuckets(text) {
  const hits = [];
  for (const [name, re] of Object.entries(BUCKETS)) {
    if (re.test(text)) hits.push(name);
  }
  return hits;
}

function countTerms(text, tally) {
  const lower = text.toLowerCase();
  for (const term of THEME_TERMS) {
    const t = term.toLowerCase();
    // count non-overlapping occurrences
    let idx = 0, count = 0;
    while ((idx = lower.indexOf(t, idx)) !== -1) { count += 1; idx += t.length; }
    if (count) tally[t] = (tally[t] || 0) + count;
  }
}

function truncate(s, n) {
  if (s.length <= n) return s;
  return s.slice(0, n - 1) + '…';
}

// Dedupe near-identical snippets (same first 80 chars) within a bucket.
function dedupe(snippets) {
  const seen = new Set();
  const out = [];
  for (const s of snippets) {
    const key = s.text.slice(0, 80).toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(s);
  }
  return out;
}

// --- Main ----------------------------------------------------------------
const files = findTranscriptFiles(transcriptsDir);
const recordingsPresent = !skipCallRecordings && callRecordingsDir && fs.existsSync(callRecordingsDir) && findCallRecordings(callRecordingsDir).length > 0;
if (!files.length && !recordingsPresent) {
  console.error(`No transcripts found at ${transcriptsDir} and no call recordings at ${callRecordingsDir || '(none)'}`);
  process.exit(1);
}
if (!files.length) console.warn(`No agent transcripts at ${transcriptsDir} — mining call recordings only.`);

const allTurns = [];
const themeTally = {};
const buckets = { mike: [], variableReduction: [], field: [], caseStudy: [], audience: [], partner: [] };
let transcriptCount = 0;
let callRecordingCount = 0;
const callRecordingFiles = [];

for (const f of files) {
  transcriptCount += 1;
  const turns = readTranscript(f);
  for (const t of turns) {
    allTurns.push(t);
    countTerms(t.text, themeTally);
    const hits = snippetBuckets(t.text);
    for (const h of hits) {
      buckets[h].push({ from: path.basename(path.dirname(f)), sourceType: 'agent', role: t.role, text: truncate(t.text, 600) });
    }
  }
}

// --- Call recordings (.docx meeting transcripts from OneDrive) -----------
if (!skipCallRecordings && callRecordingsDir) {
  const recordings = findCallRecordings(callRecordingsDir);
  for (const f of recordings) {
    callRecordingCount += 1;
    const base = path.basename(f);
    callRecordingFiles.push(base);
    const paragraphs = extractDocxParagraphs(f);
    for (const para of paragraphs) {
      const text = cleanSnippet(para);
      if (!text) continue;
      allTurns.push({ role: 'call', text });
      countTerms(text, themeTally);
      const hits = snippetBuckets(text);
      for (const h of hits) {
        buckets[h].push({ from: base, sourceType: 'call', role: 'call', text: truncate(text, 600) });
      }
    }
  }
}

for (const k of Object.keys(buckets)) {
  let arr = dedupe(buckets[k]);
  // Call-recording snippets first (richer raw material — real meeting audio),
  // then agent-transcript snippets. Stable sort keeps within-group order.
  arr.sort((a, b) =>
    a.sourceType === 'call' && b.sourceType !== 'call' ? -1
    : b.sourceType === 'call' && a.sourceType !== 'call' ? 1 : 0
  );
  buckets[k] = arr.slice(0, 40);
}

const sortedThemes = Object.entries(themeTally)
  .sort((a, b) => b[1] - a[1])
  .filter(([, c]) => c >= 2);

if (auditOnly) {
  console.log(`Agent transcripts scanned: ${transcriptCount}`);
  console.log(`Call recordings scanned: ${callRecordingCount}`);
  console.log(`Text turns extracted: ${allTurns.length}`);
  console.log(`Top themes (>=2 hits):`);
  for (const [t, c] of sortedThemes.slice(0, 25)) console.log(`  ${c}\t${t}`);
  console.log(`Bucket counts:`);
  for (const [k, v] of Object.entries(buckets)) console.log(`  ${k}: ${v.length}`);
  process.exit(0);
}

// --- Candidate ideas (channel-tagged, Content Lab format) ----------------
// buckets.mike is already ordered call-first (real Mike quotes from meetings
// before agent-transcript mentions), so the first N are the strongest
// thought-leadership raw material.
const candidateIdeas = [];
let sIdx = 5; // S1–S4 already exist in Content Lab; start at S5
for (const s of buckets.variableReduction.slice(0, 6)) {
  candidateIdeas.push({
    id: `S${sIdx++}`,
    channel: 'Social',
    title: 'The Shorter List — variable-reduction moment',
    body: truncate(s.text, 200),
    source: `${s.sourceType}:${s.from}`,
    status: 'Idea',
  });
}
for (const s of buckets.caseStudy.slice(0, 4)) {
  candidateIdeas.push({
    id: `S${sIdx++}`,
    channel: 'Social',
    title: 'Case-study snippet candidate',
    body: truncate(s.text, 200),
    source: `${s.sourceType}:${s.from}`,
    status: 'Idea',
  });
}
for (const s of buckets.mike.slice(0, 6)) {
  candidateIdeas.push({
    id: `S${sIdx++}`,
    channel: 'Social',
    title: 'Thought leadership — Mike on record',
    body: truncate(s.text, 200),
    source: `${s.sourceType}:${s.from}`,
    status: 'Needs Mike sign-off',
  });
}

// --- Markdown report -----------------------------------------------------
const md = [];
md.push(`# Mined insights — transcripts & call recordings`);
md.push('');
md.push(`Scanned **${transcriptCount}** agent transcripts from \`${path.relative(os.homedir(), transcriptsDir)}\` and **${callRecordingCount}** call recordings from \`${path.relative(os.homedir(), callRecordingsDir)}\`, extracted **${allTurns.length}** text turns. This is a raw input for the Content Lab — review with Jane, then curate the keepers into the source log (\`SRC-NN\`) and ideas backlog (\`S/B/N\` ids).`);
md.push('');
md.push(`Snippets are tagged by source: **[agent]** = Cursor agent transcript, **[call]** = OneDrive meeting recording. Call-recording snippets are the richer raw material (real meeting audio), especially for Mike thought leadership.`);
md.push('');
md.push(`Generated by \`scripts/mine-transcripts.mjs\`. Re-run any time; overwrite-safe. Add \`--no-call-recordings\` to skip OneDrive.`);
md.push('');
if (callRecordingFiles.length) {
  md.push(`## Call recording sources (${callRecordingCount})`);
  md.push('');
  md.push(`Meeting transcripts read from OneDrive — \`Marketing - Documents/Call Recordings\`.`);
  md.push('');
  for (const name of callRecordingFiles) md.push(`- ${name}`);
  md.push('');
}
md.push(`## Recurring themes (mention count)`);
md.push('');
md.push('| Term | Hits |');
md.push('|---|---|');
for (const [t, c] of sortedThemes.slice(0, 25)) md.push(`| ${t} | ${c} |`);
md.push('');
md.push(`## Mike on record`);
md.push('');
md.push(`Snippets that mention Mike or quote him. These are the only safe raw material for first-person thought-leadership posts — and every one still needs Mike's direct sign-off before it ships.`);
md.push('');
for (const s of buckets.mike) {
  md.push(`- **[${s.sourceType}]** *${s.from}* — ${s.text}`);
}
md.push('');
md.push(`## Variable-reduction moments`);
md.push('');
md.push(`The strongest raw material for the weekly series candidate B ("The Shorter List"). Each is a place where the variable-reduction principle already showed up in conversation.`);
md.push('');
for (const s of buckets.variableReduction) {
  md.push(`- **[${s.sourceType}]** *${s.from}* — ${s.text}`);
}
md.push('');
md.push(`## Field & case-study moments`);
md.push('');
md.push(`Raw material for client in-the-field posts and case-study snippets. Remember: anonymize field posts (no client names, no identifiable signage); named case-study posts need the client's OK on file.`);
md.push('');
md.push(`### Field / on-site`);
md.push('');
for (const s of buckets.field.slice(0, 15)) {
  md.push(`- **[${s.sourceType}]** *${s.from}* — ${s.text}`);
}
md.push('');
md.push(`### Case-study named (Ameristar / Tachi / etc.)`);
md.push('');
for (const s of buckets.caseStudy) {
  md.push(`- **[${s.sourceType}]** *${s.from}* — ${s.text}`);
}
md.push('');
md.push(`## Audience & partner mentions`);
md.push('');
md.push(`Useful for checking which buyer roles and integrations already show up in the conversation — informs which persona line a post should close on.`);
md.push('');
md.push(`### Audience (casino / IT / Dir / VP / C-suite)`);
md.push('');
for (const s of buckets.audience.slice(0, 10)) {
  md.push(`- **[${s.sourceType}]** *${s.from}* — ${s.text}`);
}
md.push('');
md.push(`### Partner / integration (Q-SYS / QSC / backend)`);
md.push('');
for (const s of buckets.partner.slice(0, 10)) {
  md.push(`- **[${s.sourceType}]** *${s.from}* — ${s.text}`);
}
md.push('');
md.push(`## Candidate ideas (drop into Content Lab backlog)`);
md.push('');
md.push(`Pre-tagged in the Content Lab's \`S\` (social) id space, starting at S5 (S1–S4 already exist). Review each, rewrite the title/body, and set the real status before promoting to the backlog on \`index.html\`.`);
md.push('');
for (const idea of candidateIdeas) {
  md.push(`### ${idea.id} — ${idea.title}`);
  md.push(`- **Channel:** ${idea.channel}`);
  md.push(`- **Status:** ${idea.status}`);
  md.push(`- **Source:** ${idea.source}`);
  md.push(`- **Body:** ${idea.body}`);
  md.push('');
}
md.push(`---`);
md.push('');
md.push(`**Next step:** Jane + agent review this together. Pick the weekly-series format (Property Playbook vs. The Shorter List vs. hybrid) based on what's actually on record here. Then curate the keepers into \`index.html\`.`);

fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(path.join(outDir, 'mined-insights.md'), md.join('\n') + '\n');
fs.writeFileSync(
  path.join(outDir, 'mined-insights.json'),
  JSON.stringify({ generatedAt: new Date().toISOString(), transcriptCount, callRecordingCount, callRecordingFiles, turnCount: allTurns.length, themes: sortedThemes, candidateIdeas }, null, 2) + '\n'
);

console.log(`Mined ${transcriptCount} agent transcripts + ${callRecordingCount} call recordings, ${allTurns.length} turns.`);
console.log(`Report: ${path.relative(root, path.join(outDir, 'mined-insights.md'))}`);
console.log(`JSON:  ${path.relative(root, path.join(outDir, 'mined-insights.json'))}`);
