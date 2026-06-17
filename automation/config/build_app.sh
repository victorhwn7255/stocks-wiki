#!/usr/bin/env bash
# Build "Stocks Wiki.app" — a minimal app bundle wrapping the automation runner so macOS
# displays the background item as "Stocks Wiki" (not python's signer). Compiles the launcher
# with clang, assembles the bundle in ~/Applications, and ad-hoc signs it for a stable identity.
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)/app"
APP="$HOME/Applications/Stocks Wiki.app"
MACOS="$APP/Contents/MacOS"

rm -rf "$APP"          # rebuild clean so no stale executable name lingers
mkdir -p "$MACOS"
cp "$SRC/Info.plist" "$APP/Contents/Info.plist"
clang -O2 -o "$MACOS/Stocks Wiki" "$SRC/launcher.c"
# ad-hoc sign the whole bundle → stable code identity (still "unidentified developer",
# but a consistent NAME in Login Items, and no quarantine churn).
codesign --force --deep --sign - "$APP" 2>/dev/null || true

echo "Built: $APP"
echo "Executable: $MACOS/Stocks Wiki"
