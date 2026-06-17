#!/usr/bin/env bash
# Remove the "Stocks Wiki" background automation LaunchAgent.
set -euo pipefail
PLIST="StocksWiki.plist"
DEST="$HOME/Library/LaunchAgents/$PLIST"
launchctl unload "$DEST" 2>/dev/null || true
rm -f "$DEST"
echo "Uninstalled: $DEST  (\"Stocks Wiki\" background item removed)"
