/* Stocks Wiki — launcher.
 *
 * A tiny native binary that lives inside "Stocks Wiki.app" and exec()s the automation
 * runner. Its only purpose is the DISPLAY NAME: macOS attributes a background LaunchAgent
 * to the app bundle that contains the launched binary, so this makes the item show as
 * "Stocks Wiki" instead of "Python Software Foundation" (python's code-signing team).
 *
 * Environment (PATH / CLAUDE_BIN / HOME) is supplied by the LaunchAgent plist and is
 * preserved across execv, so the Max-authenticated `claude` CLI is found at run time.
 */
#include <unistd.h>

int main(void) {
    char *py =
        "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3";
    char *args[] = {
        py,
        "/Users/victor_he/Downloads/Code/stocks-wiki/automation/scripts/run.py",
        "--auto", "--quiet",   /* daily: free scan Tue-Sun, full agentic loop on Mondays */
        (char *)0
    };
    execv(py, args);
    return 1; /* only reached if exec fails */
}
