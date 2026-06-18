#!/usr/bin/env bash
# PostToolUse guardrail (Phase 4): after an Edit/Write to a wiki/ page, run the FAST
# single-file hygiene check (the edited page's links resolve + it's in index.md) and log it.
#
# READ-ONLY: never edits canon, never writes outside automation/logs/. Non-blocking —
# always exits 0 (a guardrail must never break the user's edit).
# Disable by removing the PostToolUse hook from .claude/settings.json.
set -uo pipefail

ROOT="/Users/victor_he/Projects/stocks-wiki"
LOG="$ROOT/automation/logs/hook.log"
mkdir -p "$ROOT/automation/logs"

INPUT="$(cat)"
FILE="$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null || true)"

case "$FILE" in
  *"/wiki/"*.md)
    RESULT="$(cd "$ROOT" && python3 scripts/vault_hygiene.py --quick-check "$FILE" 2>/dev/null || true)"
    printf '%s  %s\n' "$(date +%FT%T)" "$RESULT" >> "$LOG"
    # Surface only a problem to the session (PASS stays silent to avoid noise).
    case "$RESULT" in
      "⚠️"*) printf '%s\n' "$RESULT" ;;
    esac
    ;;
esac
exit 0
