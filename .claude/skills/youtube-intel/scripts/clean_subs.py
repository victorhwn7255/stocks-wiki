#!/usr/bin/env python3
"""Clean a YouTube .srt/.vtt subtitle file into readable, de-duplicated plain text.

YouTube auto-captions are noisy: rolling 1-2 line cues where each cue repeats the
previous cue's tail line, inline <00:00:00.000> word-timing tags, cue settings,
and HTML entities. This strips all of that and collapses the rolling duplicates
into clean paragraphs.

The argument may be a FILE or a DIRECTORY. If a directory, the best caption file
is chosen by language preference (manual English first, Chinese last) — this keeps
the caller's shell out of glob-matching, which is brittle under zsh `nomatch`.

Usage:
    python3 clean_subs.py path/to/file.en.vtt > clean.txt
    python3 clean_subs.py path/to/workdir/      > clean.txt   # auto-picks best file
"""
import glob
import html
import os
import re
import sys

# caption-file preference, best first (suffix patterns, case-insensitive)
_PREF = (".en.vtt", ".en.srt", ".en-orig.vtt", ".en-orig.srt",
         ".en-", ".zh-hans", ".zh-hant", ".zh", ".vtt", ".srt")


def pick_best(directory: str) -> str | None:
    files = glob.glob(os.path.join(directory, "*.vtt")) + \
        glob.glob(os.path.join(directory, "*.srt"))
    if not files:
        return None

    def rank(f: str) -> int:
        low = os.path.basename(f).lower()
        for i, suf in enumerate(_PREF):
            if suf in low:
                return i
        return len(_PREF)

    return sorted(files, key=rank)[0]

TS_LINE = re.compile(r"-->")                       # timestamp cue line
CUE_INDEX = re.compile(r"^\d+\s*$")                # bare srt cue index
VTT_HEADER = re.compile(r"^(WEBVTT|Kind:|Language:|NOTE|STYLE|REGION)", re.I)
INLINE_TAG = re.compile(r"<[^>]+>")                # <c>, <00:00:00.000>, </c>, <i> ...
CUE_SETTINGS = re.compile(r"\b(align|position|line|size|region):\S+")


def clean(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
    except FileNotFoundError:
        sys.stderr.write(f"clean_subs: file not found: {path}\n")
        sys.exit(1)

    out: list[str] = []
    last = None
    for line in raw.splitlines():
        s = line.strip()
        if not s:
            continue
        if VTT_HEADER.match(s):
            continue
        if TS_LINE.search(s):
            continue
        if CUE_INDEX.match(s):
            continue
        # strip inline word-timing tags + cue settings + entities
        s = INLINE_TAG.sub("", s)
        s = CUE_SETTINGS.sub("", s)
        s = html.unescape(s)
        s = re.sub(r"\s+", " ", s).strip()
        if not s:
            continue
        # collapse the rolling-duplicate pattern: drop if identical to the
        # previous kept line, or if it is wholly contained in it.
        if last is not None:
            if s == last:
                continue
            if s in last:
                continue
            if last in s:
                # new line supersets the old partial line -> replace it
                out[-1] = s
                last = s
                continue
        out.append(s)
        last = s

    # Re-flow into paragraphs: join short caption lines, break on sentence ends.
    text = " ".join(out)
    text = re.sub(r"\s+", " ", text).strip()
    # soft paragraph breaks after sentence-ending punctuation for readability
    text = re.sub(r"(?<=[.!?]) (?=[A-Z(])", "\n\n", text)
    return text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("usage: clean_subs.py <file.srt|file.vtt|dir>\n")
        sys.exit(2)
    target = sys.argv[1]
    if os.path.isdir(target):
        target = pick_best(target)
        if not target:
            sys.stderr.write("clean_subs: no .vtt/.srt caption file in directory\n")
            sys.exit(1)
        sys.stderr.write(f"clean_subs: using {os.path.basename(target)}\n")
    print(clean(target))
