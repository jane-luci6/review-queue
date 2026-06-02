/**
 * Microsoft Teams Incoming Webhook — Office 365 MessageCard format.
 */
import fs from 'fs';

export function siteUrl() {
  return (process.env.REVIEW_SITE_URL || 'https://startling-fudge-f9965f.netlify.app').trim().replace(/\/$/, '');
}

export function assetReviewLink(assetId, reviewUrl) {
  const fromBody = (reviewUrl || '').trim();
  if (fromBody) return fromBody;
  if (!assetId) return siteUrl();
  return `${siteUrl()}/#/review/${encodeURIComponent(assetId)}`;
}

export function buildMessageCard({
  summary,
  activityTitle,
  activitySubtitle = '',
  facts = [],
  text = '',
  link = '',
  themeColor = '68E3BE',
}) {
  const card = {
    '@type': 'MessageCard',
    '@context': 'https://schema.org/extensions',
    themeColor,
    summary: summary || activityTitle,
    sections: [
      {
        activityTitle,
        ...(activitySubtitle ? { activitySubtitle } : {}),
        ...(facts.length ? { facts } : {}),
        ...(text ? { text, markdown: true } : {}),
      },
    ],
  };
  if (link) {
    card.potentialAction = [
      {
        '@type': 'OpenUri',
        name: 'Open in review queue',
        targets: [{ os: 'default', uri: link }],
      },
    ];
  }
  return card;
}

export async function postTeamsWebhook(webhookUrl, card) {
  const url = (webhookUrl || '').trim();
  if (!url) return { ok: false, skipped: true };
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(card),
    });
    const body = await res.text().catch(() => '');
    return { ok: res.ok, status: res.status, body };
  } catch (err) {
    return { ok: false, error: String(err.message || err) };
  }
}

export function loadDotEnv(envPath) {
  if (!envPath || !fs.existsSync(envPath)) return;
  const text = fs.readFileSync(envPath, 'utf8');
  for (const line of text.split('\n')) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const i = t.indexOf('=');
    if (i < 0) continue;
    const key = t.slice(0, i).trim();
    let val = t.slice(i + 1).trim();
    if (
      (val.startsWith('"') && val.endsWith('"')) ||
      (val.startsWith("'") && val.endsWith("'"))
    ) {
      val = val.slice(1, -1);
    }
    if (!process.env[key]) process.env[key] = val;
  }
}

export function ownerWebhookUrl() {
  return (
    process.env.REVIEW_TEAMS_WEBHOOK_OWNER ||
    process.env.REVIEW_TEAMS_WEBHOOK_URL ||
    ''
  ).trim();
}

export function stakeholdersWebhookUrl() {
  return (process.env.REVIEW_TEAMS_WEBHOOK_STAKEHOLDERS || '').trim();
}
