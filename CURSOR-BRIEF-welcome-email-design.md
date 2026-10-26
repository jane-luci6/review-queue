# Brief (GLM, design): revised layout for customer journey Email 1 "Welcome to the LUCI family"

Build two NEW files in `LUCI Systems Design System/ui_kits/email/` (do not edit any existing file):
- `email-1a-welcome-v2.html` (recommended: no portal block)
- `email-1a-welcome-v2-with-portal.html` (identical, plus the optional portal block, for Jane to compare)

## Source of truth
- Shell and brand: copy the exact email shell from `ui_kits/email/email-1a-welcome.html`: the same `<head>` (fonts, resets, mobile media queries), 600px container on #E5E3DF, mint #68E3BE 4px accent line, navy #10232D header banner with the right-aligned LUCI logo, Space Grotesk body at 17px/27px #10232D, Syncopate small caps kicker style, the divider style, Mike's signature block (Michael Epstein – CEO, phones, email, LUCIsystems.com, environment line, Email Privacy Policy), and the navy footer. Keep the same image URLs, colors, fonts and spacing system. Do NOT invent a new look.
- Copy: use ONLY the `final` object, `subject_lines`, and `preheader` from `ui_kits/email/email-1a-welcome-revision.json` (read it; use the recommended final, not the three directions). Hidden preheader div = `preheader`. Put the first subject line in `<title>`.

## Design changes (lighter, warmer, fewer boxes)
1. Header banner: headline = final.header.headline in mint, subline = final.header.subline in #A6B0B6. Drop the "control, automate, execute" tagline.
2. Body: greeting and body paragraphs as plain paragraphs. No checklist, no mint stripe callout, no dark box (except the optional portal block below).
3. Make the line "We’ve never lost a client. I believe the reason is simple: we stay." gently prominent: its own paragraph, the first sentence in font-weight 600 (#10232D) and nothing louder (no box, no big pull quote).
4. Process walk-through: one thin divider, then a Syncopate kicker "HOW A LUCI PROJECT TYPICALLY GOES" (or similar neutral wording), then `final.process_lead_in` as a short paragraph, then the five `final.steps` as a simple neutral vertical sequence built in HTML tables (no image): each row = a small mint outlined circle or number cell (01–05 in #2b9e80, Syncopate 12–14px, exactly like the old numbered list style) + step name (600 weight) and descriptor (400, 15–16px, #535559). All five rows have identical styling: no highlighted step, no "you are here", no active/filled state, no dates, no durations, no arrows pointing at a current stage. Optional: a 1px #D9DEE1 left rule connecting the steps, only if Outlook-safe (use a table cell border, not CSS pseudo-elements).
5. Closing paragraphs and sign-off from `final.closing` and `final.signoff`, then the signature block unchanged (do not duplicate the name: the signature block already says "Michael Epstein – CEO", so render the sign-off line "Welcome aboard." only and let the signature carry the name).
6. Greeting is the literal text `Dear #Name#,` (merge tag TBD by Jane; leave it as text).
7. Portal block (ONLY in `-with-portal.html`): place it after the process sequence as a light block, not a dark box: #F5F8FA background, 1px #D9DEE1 border, 20–24px padding, the two `final.portal_block_optional.text` lines, and a bulletproof mint button "Request portal access" linking to https://app.smartsheet.com/b/form/3c05a169bfa14ae4ab834018381bc3a1 (table button + `<!--[if mso]>` v:roundrect VML fallback, as in the original). No "before your call" language.

## Outlook-safe rules (per the Signal shell rule)
Tables for all layout (role="presentation"), inline styles, no flexbox/grid, no CSS pseudo-elements, no background images without VML, bulletproof buttons with VML fallback, images with width/height/alt, max width 600px, mobile stacking via the existing media query classes (`px-side`, `body-lg`, `h1`, `header-pad`). Keep it light-mode only like the original.

When done, open both files in a headless browser if you can and fix any rendering problems. Report what you changed versus the original layout in a short list.
