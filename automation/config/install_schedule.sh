#!/usr/bin/env bash
# Install the "Stocks Wiki" background automation as a launchd LaunchAgent.
#
# Schedules the AUTONOMOUS self-X loop weekly (Mondays 08:00): deterministic scan +
# agentic calibration scoring + briefing. The agentic steps run `claude -p` under your
# logged-in Claude Max subscription (NOT API billing), behind the locked tool allow-list
# (discovery-only — writes ONLY to automation/, never edits canon).
#
# After install it appears in System Settings → Login Items & Extensions → Allow in the
# Background as "Stocks Wiki".  Reverse with: automation/config/uninstall_schedule.sh
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PLIST="StocksWiki.plist"
SRC="$HERE/$PLIST"
DEST="$HOME/Library/LaunchAgents/$PLIST"

# Build the "Stocks Wiki.app" bundle first (gives the background item its display name).
bash "$HERE/build_app.sh"

mkdir -p "$HOME/Library/LaunchAgents"
cp "$SRC" "$DEST"
launchctl unload "$DEST" 2>/dev/null || true
launchctl load "$DEST"

echo "Installed + loaded: $DEST  (Label: \"Stocks Wiki\")"
echo "Scheduled: DAILY 02:30 local (Singapore) — free deterministic scan Tue-Sun; full agentic loop on Mondays (Max subscription)."
echo "Verify:        launchctl list | grep -i 'Stocks Wiki'"
echo "Run once now:  python3 automation/scripts/run.py --full --run-llm"
echo "Remove:        automation/config/uninstall_schedule.sh"
