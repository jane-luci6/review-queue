#!/usr/bin/env bash
set -euo pipefail

# Stable bridge from Grok Bot roles to Cursor's local CLI agent.
# Grok writes a task brief, then calls this script. Cursor reads the live repo,
# applies its .cursor/rules, and returns the result to Grok on stdout.

DESIGN_REPO="$HOME/Documents/Cursor Projects/luci-design"
WEBSITE_REPO="$HOME/Documents/Cursor Projects/luci-website"
HANDBOOK="$DESIGN_REPO/LUCI Systems Design System/agent-handbook"
LOG_DIR="$HOME/.cursor/grok-delegations"

ROLE=""
REPO=""
BRIEF=""
MODEL=""
EXECUTE=false

usage() {
  cat <<'EOF'
Usage:
  run-cursor-delegation.sh --role ROLE --repo REPO --brief FILE [--execute] [--model MODEL_ID]

Roles:
  chief-of-staff | design-direction | design-direction-open
  strategic-marketer | maker | review-mechanical | review-taste

Repos:
  design | website | both

Design Direction starts on GLM (role design-direction). Use
design-direction-open for open visual planning, or when a GLM pass has already
been tried and did not get there.

Default is read-only planning/review. Add --execute only when the brief
authorizes Cursor to edit files. An explicit --model overrides the role default.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --role) ROLE="${2:-}"; shift 2 ;;
    --repo) REPO="${2:-}"; shift 2 ;;
    --brief) BRIEF="${2:-}"; shift 2 ;;
    --model) MODEL="${2:-}"; shift 2 ;;
    --execute) EXECUTE=true; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

[[ -n "$ROLE" && -n "$REPO" && -n "$BRIEF" ]] || {
  echo "Missing --role, --repo, or --brief." >&2
  usage >&2
  exit 2
}
[[ -f "$BRIEF" ]] || { echo "Brief not found: $BRIEF" >&2; exit 2; }
command -v agent >/dev/null 2>&1 || {
  echo "Cursor CLI is not installed or is not on PATH." >&2
  exit 127
}

case "$ROLE" in
  chief-of-staff)
    ROLE_FILE="roles/chief-of-staff.md"
    DEFAULT_MODEL="glm-5.2-high"
    ROLE_BOUNDARY="Route and sequence the work. Do not take over strategy, visual taste, or implementation."
    ;;
  design-direction)
    ROLE_FILE="roles/design-direction.md"
    DEFAULT_MODEL="glm-5.2-max"
    ROLE_BOUNDARY="Lock visual direction only, working from the existing locked visual system. Do not implement production unless Jane's brief explicitly authorizes it. If the brief genuinely needs a new visual thesis, say so and stop rather than guessing."
    ;;
  design-direction-open)
    ROLE_FILE="roles/design-direction.md"
    DEFAULT_MODEL="claude-opus-5-thinking-medium"
    ROLE_BOUNDARY="Open visual planning escalation. Set a new visual thesis or genuine variant axes. Do not implement production. Output a lock that GLM can apply."
    ;;
  strategic-marketer)
    ROLE_FILE="roles/strategic-marketer.md"
    DEFAULT_MODEL="gpt-5.6-sol-high"
    ROLE_BOUNDARY="Lock message, argument, channel, and claims. Do not implement visual production."
    ;;
  maker)
    ROLE_FILE="roles/maker.md"
    DEFAULT_MODEL="glm-5.2-max"
    ROLE_BOUNDARY="Implement the locked brief faithfully. Do not invent strategy, claims, visual direction, or rule scope."
    ;;
  review-mechanical)
    ROLE_FILE="roles/review.md"
    DEFAULT_MODEL="glm-5.2-max"
    ROLE_BOUNDARY="Review mechanical correctness only. Return severity, evidence, and required fixes; do not rebuild."
    ;;
  review-taste)
    ROLE_FILE="roles/review.md"
    DEFAULT_MODEL="claude-opus-5-thinking-medium"
    ROLE_BOUNDARY="Perform Jane-level brand, layout, voice, and taste review. Return issues and fixes; do not rebuild."
    ;;
  *)
    echo "Unknown role: $ROLE" >&2
    usage >&2
    exit 2
    ;;
esac

case "$REPO" in
  design)
    WORKSPACE="$DESIGN_REPO"
    ;;
  website)
    WORKSPACE="$WEBSITE_REPO"
    ;;
  both)
    WORKSPACE="$DESIGN_REPO"
    ;;
  *)
    echo "Unknown repo: $REPO" >&2
    usage >&2
    exit 2
    ;;
esac

MODEL="${MODEL:-$DEFAULT_MODEL}"
mkdir -p "$LOG_DIR"
STAMP="$(date +%Y%m%d-%H%M%S)"
LOG_FILE="$LOG_DIR/${STAMP}-${ROLE}.txt"

BRIEF_CONTENT="$(cat "$BRIEF")"
printf -v PROMPT '%s\n' \
  "You are Cursor executing a delegated LUCI task from the $ROLE Grok Bot." \
  "You are the leading brain for this task. Make the decisions. The Grok Bot will follow your direction unless you clearly go off the brief." \
  "" \
  "Read these first:" \
  "- $HANDBOOK/README.md" \
  "- $HANDBOOK/shared/CURRENT-WORK-BOARD.md" \
  "- $HANDBOOK/shared/CURSOR-AND-MODEL-PROTOCOL.md" \
  "- $HANDBOOK/shared/SHARED-OPERATING-PROTOCOL.md" \
  "- $HANDBOOK/$ROLE_FILE" \
  "" \
  "The live local repositories and their .cursor/rules are the source of truth." \
  "Do not use GitHub as the source. Preserve unrelated user changes." \
  "" \
  "Role boundary:" \
  "$ROLE_BOUNDARY" \
  "" \
  "For any implementation:" \
  "- inspect git status before editing;" \
  "- make the smallest coherent change;" \
  "- follow the repository's commit cadence and never commit secrets or scratch;" \
  "- verify in proportion to risk;" \
  "- deploy only when the brief explicitly requires it;" \
  "- return changed paths, verification, review URL when applicable, and anything not done." \
  "" \
  "Delegated brief:" \
  "$BRIEF_CONTENT"

echo "Cursor delegation"
echo "  role:  $ROLE"
echo "  repo:  $REPO"
echo "  model: $MODEL"
echo "  mode:  $([[ "$EXECUTE" == true ]] && echo execute || echo read-only)"
echo "  log:   $LOG_FILE"
echo

if [[ "$EXECUTE" == true ]]; then
  AGENT_ARGS=(--print --force --trust --model "$MODEL" --workspace "$WORKSPACE")
else
  AGENT_ARGS=(--print --mode plan --trust --model "$MODEL" --workspace "$WORKSPACE")
fi

if [[ "$REPO" == "both" ]]; then
  AGENT_ARGS+=(--add-dir "$WEBSITE_REPO")
fi

agent "${AGENT_ARGS[@]}" "$PROMPT" | tee "$LOG_FILE"
