#!/usr/bin/env python3
"""check_html.py — deterministic QA for a /build-HTML reading-layer page.

The MECHANICAL half of the skill's QA (the subjective fidelity/no-distortion
half is the audit subagent's job, not this script's). It runs the exact checks
that were done by hand while building the first four Slock explainers:

  1. parses          — the file is well-formed HTML (Python html.parser)
  2. location        — saved under raw/HTML/ with a .html extension
  3. slock_theme     — the Slock design tokens are present
                       (Space Grotesk + Space Mono, --yellow #FFD700,
                        2px solid #000 borders, 2px 2px 0 hard shadow,
                        border-radius:0 reset) AND zero glassmorphism
                        (no backdrop-filter / atmospheric-glass navy)
  4. jargon_leak     — the VISIBLE TEXT contains no vault-insider terms
                       (Tier, chokepoint, neocloud, CLEC, MFU, FCF, capex,
                        book-to-bill, wikilink, falsifier, …) — the page is
                        for outsiders, so these must be translated away
  5. discipline      — no obvious price-target / buy-sell language slipped in
  6. takeaways       — a KEY TAKEAWAYS section is present, and the added
                       "our read / our take" block is provenance-labeled

Emits a JSON object (default) or a human summary (--human). Exit code is 0
when there are no hard failures, 1 otherwise — so the skill can gate on it.

Usage:
  python3 .claude/skills/build-HTML/scripts/check_html.py raw/HTML/<slug>.html [--human]
"""

import sys
import re
import json
import argparse
from html.parser import HTMLParser
from pathlib import Path


# ── visible-text extraction ────────────────────────────────────────────────
class _TextExtractor(HTMLParser):
    """Collect the rendered visible text; skip <style>/<script> contents."""

    _SKIP = {"style", "script", "head"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._skip_depth = 0
        self.parts: list[str] = []
        self.ok = True
        self.error = ""

    def handle_starttag(self, tag, attrs):
        if tag in self._SKIP:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self._SKIP and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            self.parts.append(data)

    def text(self) -> str:
        return " ".join(" ".join(self.parts).split())


# ── the checks ─────────────────────────────────────────────────────────────
# Insider vocabulary that must NOT reach an outsider reader. Matched
# case-insensitively as whole words against the VISIBLE text only.
JARGON = [
    "tier", "chokepoint", "neocloud", "neoclouds", "CLEC", "CLECs",
    "MFU", "goodput", "book-to-bill", "FCF", "capex", "opex",
    "wikilink", "falsifier", "falsify", "describe-don't-recommend",
    "primary-grounded", "Tier-3", "Tier 3", "hyperscaler-capex",
    "LGD", "take-or-pay",
]
# "Layer" is handled specially: the vault term is a capitalized standalone
# word; the common word "players"/"layer of glass" is fine. We only flag the
# capitalized standalone "Layer".
LAYER_RE = re.compile(r"\bLayer\b")

# price-target / recommendation language the disciplines forbid.
# NOTE: bare "buy"/"sell" are intentionally NOT flagged — the explainers
# legitimately carry the disclaimer "doesn't tell you what to buy or sell".
# We flag only imperative recommendations + valuation calls.
DISCIPLINE_BAD = [
    r"\bprice target\b", r"\bprice targets\b",
    r"\bshould buy\b", r"\bshould sell\b", r"\bwe'?d? buy\b", r"\bwe'?d? sell\b",
    r"\boverweight\b", r"\bunderweight\b",
    r"\bwe recommend\b", r"\bwe rate\b", r"\bstrong buy\b", r"\bstrong sell\b",
    r"\bbuy the\b", r"\bsell the\b",
]

# Slock design tokens that should be present
SLOCK_TOKENS = {
    "Space Grotesk": r"Space\+?Grotesk",
    "Space Mono": r"Space\+?Mono",
    "yellow #FFD700": r"#FFD700",
    "cream #FFF8E7": r"#FFF8E7",
    "2px black border": r"2px\s+solid\s+#000",
    "hard shadow 2px 2px 0": r"2px\s+2px\s+0",
    "radius-0 reset": r"border-radius\s*:\s*0",
}
# glassmorphism markers that must be ABSENT (that's the other, unused theme)
GLASS_MARKERS = {
    "backdrop-filter": r"backdrop-filter",
    "atmospheric navy #0b1326": r"#0b1326",
}


def _whole_word(term: str, haystack_lower: str) -> int:
    return len(re.findall(r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])",
                          haystack_lower))


def run_checks(path: Path) -> dict:
    res: dict = {"file": str(path), "checks": {}, "hard_fail": [], "warn": []}

    if not path.exists():
        res["checks"]["exists"] = False
        res["hard_fail"].append(f"file not found: {path}")
        return res
    res["checks"]["exists"] = True

    raw = path.read_text(encoding="utf-8", errors="replace")

    # 2. location + extension
    loc_ok = ("raw/HTML/" in str(path).replace("\\", "/")) and path.suffix == ".html"
    res["checks"]["location_raw_html"] = loc_ok
    if not loc_ok:
        res["warn"].append("file is not saved under raw/HTML/ with a .html extension")

    # 1. parses + extract visible text
    ex = _TextExtractor()
    try:
        ex.feed(raw)
        res["checks"]["parses"] = True
    except Exception as e:  # pragma: no cover
        res["checks"]["parses"] = False
        res["hard_fail"].append(f"HTML failed to parse: {e}")
        return res
    text = ex.text()
    text_lower = text.lower()

    # 3. Slock theme tokens present
    missing_tokens = [name for name, pat in SLOCK_TOKENS.items()
                      if not re.search(pat, raw, re.I)]
    res["checks"]["slock_tokens_present"] = not missing_tokens
    if missing_tokens:
        res["hard_fail"].append("missing Slock design tokens: " + ", ".join(missing_tokens))
    # glass markers absent
    glass_hits = [name for name, pat in GLASS_MARKERS.items() if re.search(pat, raw, re.I)]
    res["checks"]["no_glassmorphism"] = not glass_hits
    if glass_hits:
        res["hard_fail"].append("glassmorphism markers found (wrong theme): " + ", ".join(glass_hits))

    # 4. jargon leak (visible text only)
    leaks = {}
    for term in JARGON:
        n = _whole_word(term, text_lower)
        if n:
            leaks[term] = n
    layer_hits = LAYER_RE.findall(text)
    if layer_hits:
        leaks["Layer"] = len(layer_hits)
    res["checks"]["jargon_clean"] = not leaks
    res["jargon_leaks"] = leaks
    if leaks:
        res["hard_fail"].append("insider jargon in visible text: "
                                + ", ".join(f"{k}×{v}" for k, v in leaks.items()))

    # 5. discipline (price-target / buy-sell language).
    # Skip matches that sit inside a NEGATED / disclaimer context — the
    # explainers legitimately say "names no price targets" / "not advice",
    # which mentions the forbidden term precisely to disclaim it.
    NEG = re.compile(r"\b(no|not|never|without|doesn'?t|don'?t|zero|nor|"
                     r"names no|carries no|free of)\b")
    disc = []
    for pat in DISCIPLINE_BAD:
        for m in re.finditer(pat, text_lower):
            window = text_lower[max(0, m.start() - 45):m.start()]
            if not NEG.search(window):
                disc.append(m.group(0))
    res["checks"]["discipline_clean"] = not disc
    if disc:
        res["hard_fail"].append("advice / price-target language found: " + ", ".join(sorted(set(disc))))

    # 6. KEY TAKEAWAYS present + labeled "our read/take"
    has_takeaways = bool(re.search(r"key\s+takeaways", raw, re.I))
    res["checks"]["key_takeaways_present"] = has_takeaways
    if not has_takeaways:
        res["hard_fail"].append("no KEY TAKEAWAYS section found")
    labeled = bool(re.search(r"our\s+(read|take)", raw, re.I)) and \
        bool(re.search(r"not\s+the\s+(report|page|source)'?s?", raw, re.I))
    res["checks"]["our_read_labeled"] = labeled
    if has_takeaways and not labeled:
        res["warn"].append("the 'our read' block should be clearly labeled as opinion, "
                            "e.g. \"our take — not the report's finding\"")

    # not-advice framing present somewhere (about box / footer)
    res["checks"]["not_advice_framing"] = bool(
        re.search(r"not\s+(investment\s+)?advice", raw, re.I))
    if not res["checks"]["not_advice_framing"]:
        res["warn"].append("no 'not investment advice' framing found")

    res["passed"] = not res["hard_fail"]
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic QA for a build-HTML page.")
    ap.add_argument("path", help="path to the generated raw/HTML/<slug>.html")
    ap.add_argument("--human", action="store_true", help="human-readable summary instead of JSON")
    args = ap.parse_args()

    res = run_checks(Path(args.path))

    if args.human:
        mark = {True: "✅", False: "❌"}
        print(f"check_html — {res['file']}")
        for k, v in res["checks"].items():
            print(f"  {mark.get(v, '•')} {k}: {v}")
        if res.get("jargon_leaks"):
            print("  jargon leaks:", res["jargon_leaks"])
        for f in res["hard_fail"]:
            print("  ❌ HARD:", f)
        for w in res["warn"]:
            print("  ⚠️  warn:", w)
        print("  VERDICT:", "PASS ✅" if res.get("passed") else "FAIL ❌")
    else:
        print(json.dumps(res, indent=2))

    return 0 if res.get("passed") else 1


if __name__ == "__main__":
    sys.exit(main())
