#!/usr/bin/env bash
# Pre-commit hook: refuse to commit a page-locked sales document whose content
# is clipped.
#
# .doc-page is locked to 1056px with overflow:hidden, so a page that runs long
# loses its tail and its footer with no scrollbar and no warning — a clipped
# page renders as a plausible finished page. The only reliable check is to
# measure. See ui_kits/internal-portal/customization/_brand/SKILL.md →
# "The page-count invariant".
#
# Install:
#   cp "LUCI Systems Design System/scripts/pre-commit-fit-check.sh" .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit
#
# Bypass for one commit (use sparingly, and say why in the commit message):
#   LUCI_SKIP_FIT_CHECK=1 git commit ...

set -uo pipefail

if [ -n "${LUCI_SKIP_FIT_CHECK:-}" ]; then
  echo "fit check: skipped via LUCI_SKIP_FIT_CHECK"
  exit 0
fi

ROOT="$(git rev-parse --show-toplevel)"
DS="$ROOT/LUCI Systems Design System"
FIT="$DS/scripts/fit-check.py"
BASELINE="$DS/scripts/fit-check-baseline.txt"

[ -f "$FIT" ] || exit 0

# Documents that were already clipped before this hook existed. They are being
# reflowed one at a time; until then the hook must not block unrelated edits to
# them. Delete a line as soon as that document is fixed — the hook then guards
# it like everything else.
is_baselined() {
  [ -f "$BASELINE" ] || return 1
  grep -qxF "$1" "$BASELINE"
}

STAGED=$(git diff --cached --name-only --diff-filter=ACM \
  | grep -E '^LUCI Systems Design System/(ui_kits/sales|clients)/.*\.html$' || true)

[ -z "$STAGED" ] && exit 0

FAILED=""
SKIPPED=""

while IFS= read -r rel; do
  [ -z "$rel" ] && continue
  abs="$ROOT/$rel"
  # Only page-model documents have .doc-page sheets to measure.
  git show ":$rel" 2>/dev/null | grep -q 'class="doc-page' || continue

  if is_baselined "$rel"; then
    SKIPPED="$SKIPPED  $rel\n"
    continue
  fi

  # Measure the staged content, not the working tree, and keep it beside the
  # original so relative CSS/font paths still resolve.
  tmp="$(dirname "$abs")/_precommit_$$_$(basename "$abs")"
  git show ":$rel" > "$tmp" 2>/dev/null || { rm -f "$tmp"; continue; }
  out=$(python3 "$FIT" "$tmp" 2>&1)
  status=$?
  rm -f "$tmp"

  if [ $status -eq 1 ]; then
    FAILED="$FAILED\n=== $rel\n$(echo "$out" | grep -E 'OVERFLOW')\n"
  elif [ $status -ne 0 ]; then
    echo "fit check: could not measure $rel — not blocking the commit."
    echo "$out" | sed 's/^/    /'
  fi
done <<< "$STAGED"

if [ -n "$SKIPPED" ]; then
  printf "fit check: known-clipped, not yet reflowed (baseline):\n%b" "$SKIPPED"
fi

if [ -n "$FAILED" ]; then
  printf "\n*** COMMIT BLOCKED — clipped page(s) detected ***%b" "$FAILED"
  cat <<'EOF'

The sheet stays 8.5x11 and content is never cut: add a page instead of
trimming. Split the section onto a new .doc-page with a "continued" band
header and its own footer, then renumber downstream footers and page markers.
`scripts/pack-content.py --mode sow|lineitems` does this automatically.

Re-run to confirm:  python3 "LUCI Systems Design System/scripts/fit-check.py" <file>
Bypass this commit: LUCI_SKIP_FIT_CHECK=1 git commit ...
EOF
  exit 1
fi

exit 0
