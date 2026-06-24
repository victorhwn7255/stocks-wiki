#!/usr/bin/env python3
"""
build.py — generate the "Stocks Wiki" Bloomberg-terminal static site from the Markdown vault.

Renders wiki/companies, chokepoints, themes, trackers, relationships + wiki/_thesis*.md +
raw/notes/frameworks*.md into web/dist/ using the Jinja2 templates + the design tokens in
web/assets/. Markdown stays the single source of truth (read-only); web/dist/ is a build
artifact (gitignored). Reuses scripts/vault_parsers.py for frontmatter/wikilink parsing.

Usage:
    python web/build.py              # build the whole site
    python web/build.py --only NVDA  # build one page (+ shell/nav/search) for review
"""
import argparse, json, re, shutil, sys
from html import unescape
from pathlib import Path
import yaml  # noqa: E402  (present via vault tooling)

WEB = Path(__file__).resolve().parent
ROOT = WEB.parent
sys.path.insert(0, str(ROOT / "scripts"))
import vault_parsers as vp          # noqa: E402
import markdown as md               # noqa: E402
from jinja2 import Environment, FileSystemLoader, select_autoescape  # noqa: E402

DOMAIN_HEX = {"ai": "#2f9bff", "def": "#f7a21b", "hum": "#4defc4", "mat": "#ff8a3c", "none": "#646c75"}
LAYER_SCALE = ["#5ab0ff", "#4defc4", "#9bd64f", "#f7a21b", "#ff7a3c", "#ff5a4a"]  # L1..L6
LAYER_TITLES = ["Platform definers", "Foundry / fabrication", "Components / IP",
                "Systems / equipment", "Infrastructure / power", "Raw materials"]
GRAPH_HEX = {"ai": "#2f9bff", "def": "#f7a21b", "hum": "#4defc4", "mat": "#ff8a3c",
             "choke": "#ff4d42", "theme": "#a98bf5", "tracker": "#ff8a3c", "none": "#646c75"}
GROUP_ORDER = [("companies", "Companies", "company"), ("chokepoints", "Chokepoints", "chokepoint"),
               ("themes", "Themes", "theme"), ("trackers", "Trackers", "tracker"),
               ("relationships", "Relationships", "relationship"), ("thesis", "Thesis", "thesis"),
               ("frameworks", "Frameworks", "framework")]

# content sources: (group_key, list-of-md-paths)
def sources():
    s = {}
    for sub in ("companies", "chokepoints", "themes", "trackers", "relationships"):
        s[sub] = sorted((ROOT / "wiki" / sub).glob("*.md"))
    s["thesis"] = sorted((ROOT / "wiki").glob("_thesis*.md"))
    s["frameworks"] = sorted((ROOT / "raw" / "notes").glob("frameworks*.md"))
    return s


def raw_tickers(path):
    """Read the inline `tickers: [A, B, C]` list straight from the frontmatter text. Avoids
    PyYAML (YAML 1.1) coercing a ticker like ON / NO / YES / Y / N into a boolean (e.g. ON→True→
    'TRUE'). Falls back to the parsed list for block-style frontmatter."""
    m = re.search(r"^tickers:\s*\[([^\]]*)\]", path.read_text(), re.M)
    if not m:
        return None
    return [t.strip().strip('"\'') for t in m.group(1).split(",") if t.strip()]


AI_TIERS = ("photonics_tier", "energy_power_tier", "equipment_tier", "materials_tier", "memory_tier")


def layer_ints(layer):
    """Layer can be an int (1), a comma straddle ('1, 2'), a hyphen RANGE ('4-6' = 4,5,6),
    or 'outside' — return the ints. A hyphen range is inclusive (else '4-6' drops layer 5)."""
    if isinstance(layer, int):
        return [layer]
    if isinstance(layer, str):
        nums = [int(x) for x in re.findall(r"\d+", layer)]
        if "-" in layer and len(nums) == 2 and nums[0] < nums[1]:
            return list(range(nums[0], nums[1] + 1))
        return nums
    return []


def domain_of(fm, body=""):
    if fm.get("defense_tier"):
        return "def"
    if fm.get("humanoid_tier"):
        return "hum"
    # A real numeric layer/tier means a placed AI-supply-chain name (NVDA, INTC straddle, etc.).
    if layer_ints(fm.get("layer")) or any(isinstance(fm.get(k), int) for k in AI_TIERS):
        return "ai"
    # 'outside'-placed names carry no numeric layer/tier (humanoid cohort + demand-side
    # hyperscalers, by design). Classify them by the thesis they anchor to in prose, so
    # an AI name that merely cross-links the humanoid theme isn't miscolored.
    if "humanoid-robot-value-chain" in body:
        return "hum"
    if any(t in body for t in ("hyperscaler-capex", "AI-demand", "AI-datacenter", "AI-buildout",
                               "software-AI-moat", "AI-implementation", "AI-application", "AI-data-supply")):
        return "ai"
    return "none"


def title_and_body(body):
    """Pull the first H1 as the title; return (title, subtitle, rest-of-body)."""
    lines = body.splitlines()
    title, sub, start = None, None, 0
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            title = re.sub(r"\s+", " ", ln[2:].strip())
            start = i + 1
            break
    # an italic *subtitle* line right after the H1
    j = start
    while j < len(lines) and not lines[j].strip():
        j += 1
    sl = lines[j].strip() if j < len(lines) else ""
    if len(sl) > 1 and sl.startswith("*") and sl.endswith("*"):
        sub = sl[1:-1].strip()   # drop only the single italic wrapper; keep inner **bold** + [[links]]
        start = j + 1
    return title, sub, "\n".join(lines[start:])


WL = re.compile(r"\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]")
LIST_RE = re.compile(r"^\s*([-*+]|\d+[.)])\s")
FOOTNOTE_RE = re.compile(r"^\*[^*\s]")   # leading single-* footnote marker (not **bold, not "* bullet")
MD_EXT = ["tables", "fenced_code", "sane_lists"]


def resolve_wikilinks(text, slugmap, rel):
    """[[Target]] / [[Target|alias]] → an <a> link (amber if resolved, dimmed if a forward-ref).
    Code regions are masked first so a [[link]] inside `backticks` or a fenced block stays literal."""
    def repl(m):
        target, alias = m.group(1).strip(), (m.group(2) or "").strip()
        label = alias or target
        out = slugmap.get(target) or slugmap.get(target.upper())
        if out:
            return f'<a class="wl" href="{rel}{out}">{label}</a>'
        return f'<a class="wl dead" title="forward-reference (page not yet created)">{label}</a>'
    stash = []
    def mask(m):
        stash.append(m.group(0))
        return f"\x00{len(stash) - 1}\x00"
    text = re.sub(r"```.*?```", mask, text, flags=re.S)   # fenced code first
    text = re.sub(r"`[^`\n]*`", mask, text)               # then inline code
    text = WL.sub(repl, text)
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


def _is_table_sep(s):
    """A markdown table separator row, e.g. |---|---| or | :-- | --: |."""
    s = s.strip()
    return bool(s) and "|" in s and "-" in s and bool(re.match(r"^[\s|:-]+$", s))


def preprocess_md(body):
    """Canon-safe line fixes before markdown (all skip fenced code):
    (1) insert the blank line sane_lists needs before a LIST that abuts a paragraph — the vault
        writes `**Lead-in:**` directly above its bullets, so markers leak as literal '- ' text;
    (2) insert the blank line the tables extension needs before a TABLE that abuts a paragraph
        (a `**Lead-in:**` directly above the header row, else the table leaks as literal pipes);
    (3) escape a DANGLING leading single-* footnote marker (no partner '*') so it doesn't open a
        stray <em> that mis-pairs with a later **bold**;
    (4) the vault indents nested bullets by 2 spaces but python-markdown needs 4 to nest, so
        double the leading indent of an indented list item (2→4, 4→8, …) — else sub-bullets flatten."""
    lines = body.splitlines()
    out, fence, doubled = [], False, set()   # `doubled` = original indices whose indent we grew
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fence = not fence
            out.append(line); continue
        if not fence:
            prev = lines[i - 1] if i > 0 else ""
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            prev_set = prev.strip()
            is_table_head = ("|" in line) and _is_table_sep(nxt)
            if LIST_RE.match(line) and prev_set and not LIST_RE.match(prev):
                out.append("")
            elif is_table_head and prev_set and not LIST_RE.match(prev) and "|" not in prev:
                out.append("")
            if FOOTNOTE_RE.match(line) and line.replace("**", "").count("*") == 1:
                line = "\\" + line
            # (4) double an indented list item's indent — but ONLY when it genuinely continues a
            #     list (a shallower list-item parent, or a doubled same-level sibling). Doubling a
            #     stray indented bullet that follows a paragraph would make an indented code block.
            mi = re.match(r"^( +)([-*+]|\d+[.)])\s", line)
            if mi:
                n = len(mi.group(1))
                pj = i - 1
                while pj >= 0 and not lines[pj].strip():
                    pj -= 1
                pl = lines[pj] if pj >= 0 else ""
                pind = len(pl) - len(pl.lstrip(" "))
                if (LIST_RE.match(pl) and pind < n) or (pj in doubled and pind == n):
                    line = " " * (2 * n) + line[n:]
                    doubled.add(i)
        out.append(line)
    return "\n".join(out)


def render_body(body, slugmap, rel):
    """Resolve [[wikilinks]] then convert markdown → HTML. Build TOC from h2s."""
    body = preprocess_md(resolve_wikilinks(body, slugmap, rel))
    html = md.markdown(body, extensions=MD_EXT)
    # TOC: h2s (add ids). unescape() the harvested label so the autoescaped template doesn't
    # double-escape entities (&amp; → &amp;amp;) in the right rail.
    toc = []
    def addid(m):
        text = unescape(re.sub("<[^>]+>", "", m.group(1))).strip()
        hid = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40] or "s"
        toc.append({"id": hid, "text": text[:64]})
        return f'<h2 id="{hid}">{m.group(1)}</h2>'
    html = re.sub(r"<h2>(.*?)</h2>", addid, html, flags=re.S)
    return html, toc


def render_inline(text, slugmap, rel):
    """Render a single inline string (the subtitle) — wikilinks + emphasis — with no block wrapper."""
    if not text:
        return ""
    html = md.markdown(resolve_wikilinks(text, slugmap, rel), extensions=MD_EXT)
    m = re.match(r"^<p>(.*)</p>$", html.strip(), re.S)
    return m.group(1) if m else html


def badges_for(fm, domain):
    out = []
    layer = fm.get("layer")
    lis = layer_ints(layer)
    if lis and all(1 <= x <= 6 for x in lis):
        nums = "·".join(str(x) for x in lis)
        c = LAYER_SCALE[lis[0] - 1]
        out.append({"text": f"L{nums}", "label": "Layer " + nums + (" — straddles" if len(lis) > 1 else ""),
                    "sub": "value-capture position",
                    "style": f"background:rgba({int(c[1:3],16)},{int(c[3:5],16)},{int(c[5:7],16)},.16);color:{c};border-color:{c}"})
    elif isinstance(layer, str) and layer.strip().lower() == "outside":
        out.append({"text": "OUT", "label": "Outside framework", "sub": "assessed, not placed",
                    "style": "background:rgba(100,108,117,.14);color:var(--text-2);border-color:var(--border-2)"})
    dh = DOMAIN_HEX[domain]
    for key, lab in (("photonics_tier", "PHO"), ("energy_power_tier", "PWR"), ("defense_tier", "DEF"),
                     ("equipment_tier", "EQP"), ("memory_tier", "MEM"), ("materials_tier", "MAT"),
                     ("humanoid_tier", "HUM")):
        t = fm.get(key)
        if isinstance(t, int):
            if t <= 2:
                style = f"background:{dh};color:#000;border-color:{dh}"
            else:
                a = max(.2, .9 - (t - 1) * .15)
                style = f"background:rgba({int(dh[1:3],16)},{int(dh[3:5],16)},{int(dh[5:7],16)},.10);color:{dh};border-color:rgba({int(dh[1:3],16)},{int(dh[3:5],16)},{int(dh[5:7],16)},{a:.2f})"
            out.append({"text": f"{lab}·{t}", "label": f"{lab} Tier {t}",
                        "sub": "structural chokepoint" if t <= 2 else "tier " + str(t), "style": style})
    return out


def index_pages():
    """Pass 1: index every page → (pages, slugmap, src). Shared by the build + the audit path."""
    src = sources()
    pages, slugmap = {}, {}
    for gkey, _, ptype in GROUP_ORDER:
        for p in src[gkey]:
            fm, body = vp.read_page(p)
            slug = p.stem
            title, sub, rest = title_and_body(body)
            out = f"{gkey}/{slug}.html"
            wl = [t for (t, _a) in WL.findall(body)]
            dom = domain_of(fm, body)
            # thesis/framework docs have no frontmatter — the slug names the domain authoritatively
            # (the defense/humanoid docs mention AI terms in prose, so don't trust the body here)
            if ptype in ("thesis", "framework"):
                sl = slug.lower()
                dom = ("def" if ("defense" in sl or "drone" in sl) else
                       "hum" if ("humanoid" in sl or "robot" in sl) else "ai")
            pages[slug] = {"slug": slug, "type": ptype, "group": gkey, "path": p,
                           "title": title or slug, "subtitle": sub, "body": rest,
                           "fm": fm, "tickers": raw_tickers(p) or vp.extract_tickers_from_frontmatter(fm),
                           "last_updated": vp.get_last_updated(fm), "domain": dom,
                           "out": out, "wikilinks": wl}
            slugmap[slug] = out
    # backlinks
    for rec in pages.values():
        rec["backlinks"] = []
    for slug, rec in pages.items():
        for tgt in set(rec["wikilinks"]):
            if tgt in pages and tgt != slug:
                pages[tgt]["backlinks"].append(slug)
    return pages, slugmap, src


def audit(ticker, as_json=False):
    """Print deterministic QA facts for ONE company page (engine for /build-company-html)."""
    slug = ticker.strip().upper()
    cdir = ROOT / "wiki" / "companies"
    if not (cdir / f"{slug}.md").exists():
        near = sorted(p.stem for p in cdir.glob("*.md") if p.stem[:2] == slug[:2])[:8]
        res = {"ticker": slug, "exists": False, "near_matches": near}
        print(json.dumps(res) if as_json else
              f"✗ no company page wiki/companies/{slug}.md" + (f"\n  near: {', '.join(near)}" if near else ""))
        return 1

    pages, slugmap, _ = index_pages()
    if slug not in pages:
        print(json.dumps({"ticker": slug, "exists": True, "indexed": False}) if as_json
              else f"✗ {slug}.md exists but failed to index"); return 1
    r, fm = pages[slug], pages[slug]["fm"]

    total = len(r["wikilinks"])
    dead = sorted({t for t in r["wikilinks"] if not (slugmap.get(t) or slugmap.get(t.upper()))})
    rel = "../" * r["out"].count("/")
    _html, toc = render_body(r["body"], slugmap, rel)
    placement = {k: fm.get(k) for k in (("layer",) + AI_TIERS + ("defense_tier", "humanoid_tier"))
                 if fm.get(k) is not None}
    badges = [b["text"] for b in badges_for(fm, r["domain"])]

    built = WEB / "dist" / r["out"]
    render = {"built": built.exists()}
    if built.exists():
        html = built.read_text()
        render.update(company_pill=">COMPANY<" in html,
                      breadcrumb_ok='#companies">companies</a>' in html, file=str(built))

    res = {"ticker": slug, "exists": True, "frontmatter_ok": True, "type": r["type"],
           "title": r["title"], "tickers": r["tickers"], "last_updated": r["last_updated"],
           "domain": r["domain"], "placement": placement, "badges": badges, "badge_count": len(badges),
           "wikilinks": {"total": total, "resolved": total - len(dead), "dead": len(dead), "dead_list": dead},
           "backlinks": len(set(r["backlinks"])), "toc_sections": len(toc), "render": render}

    if as_json:
        print(json.dumps(res, ensure_ascii=False))
    else:
        print(f"AUDIT {slug} — {r['title']}")
        print(f"  domain        {res['domain']}")
        print(f"  placement     {placement}")
        print(f"  badges        {badges or '(none)'}")
        print(f"  wikilinks     {res['wikilinks']['resolved']}/{total} resolved"
              + (f", dead: {dead}" if dead else ", 0 dead"))
        print(f"  backlinks     {res['backlinks']}")
        print(f"  toc sections  {res['toc_sections']}")
        print(f"  tickers       {r['tickers']}")
        print(f"  render        {render}")
    return 0


# ── site presentation data + tracker parsers ──────────────────────────────
SECTION_COLOR = {"companies": "#2f9bff", "chokepoints": "#ff4d42", "themes": "#a98bf5",
                 "trackers": "#ff8a3c", "thesis": "#4defc4", "frameworks": "#7d8aa0",
                 "relationships": "#f7a21b", "home": "#f7a21b"}
# the top-bar section tabs (label, group-key) — HOME first, then the content sections
SECTION_TABS = [("HOME", "home"), ("COMPANIES", "companies"), ("CHOKEPOINTS", "chokepoints"),
                ("THEMES", "themes"), ("TRACKERS", "trackers"), ("THESIS", "thesis"),
                ("FRAMEWORKS", "frameworks")]
DATE_RE = re.compile(r"(20\d\d)-(\d\d)-(\d\d)")
MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}


def load_site():
    p = WEB / "data" / "site.yaml"
    return yaml.safe_load(p.read_text()) if p.exists() else {}


def freshness_flag(asof, stale_days, today):
    """From an 'as of' string → (flag_text, flag_class). Honors the vault's never-hide-stale rule."""
    if not asof or asof.strip() in ("—", "(not yet read)", ""):
        return ("UNREAD", "unread")
    m = DATE_RE.search(asof)
    if m:
        y, mo, d = (int(x) for x in m.groups())
    else:
        m2 = re.search(r"([A-Z][a-z]{2})[a-z]*\.?\s+(\d{1,2}),?\s+(20\d\d)", asof)  # "Mar 31, 2026"
        if not m2:
            return ("", "")
        mo = MONTHS.get(m2.group(1), 1); d = int(m2.group(2)); y = int(m2.group(3))
    age = (today - (y * 365 + mo * 30 + d))            # cheap day-ish delta; exactness not needed
    if age > stale_days:
        return (f"STALE >{stale_days}d", "stale")
    return ("", "")


def _status_state(text):
    """Map a register/dial status phrase → (LABEL, state-class). state ∈ calm|nominal|watch|fired."""
    t = text.upper()
    if "FIRED" in t and "NOT FIRED" not in t:
        return ("FIRED", "fired")
    if "PENDING" in t:
        return ("PENDING", "watch")
    if "NOT FIRED" in t or "NOMINAL" in t:
        return ("NOT FIRED", "nominal")
    return ("—", "calm")


WCGW_DOMAIN = {"ai datacenter supply chain": "ai", "defense & drones": "def", "humanoid robots": "hum"}


def parse_wcgw(body, slugmap, rel):
    """what-could-go-wrong → the tripwire register grouped by domain."""
    entries, domain, cur = [], "ai", None
    for line in body.splitlines():
        m2 = re.match(r"^## (.+)", line)
        if m2:
            domain = WCGW_DOMAIN.get(re.sub(r"<[^>]+>", "", m2.group(1)).strip().lower(), domain)
            continue
        m3 = re.match(r"^### (\d+)\.\s+(.+)", line)
        if m3:
            cur = {"n": m3.group(1).zfill(2), "domain": domain, "title": _md_text(m3.group(2)),
                   "tripwire": "", "home": "", "home_out": None, "status": "NOT FIRED", "state": "nominal"}
            entries.append(cur); continue
        if not cur:
            continue
        mh = re.match(r"^- \*\*Canonical home:\*\*\s+(.+)", line)
        if mh:
            wl = WL.search(mh.group(1))
            if wl:
                cur["home"] = wl.group(1)
                o = slugmap.get(wl.group(1)) or slugmap.get(wl.group(1).upper())
                cur["home_out"] = (rel + o) if o else None
            else:
                # plain-text home (e.g. a `wiki/_thesis.md` code path) — keep the label, no link
                mc = re.search(r"`([^`]+)`", mh.group(1))
                cur["home"] = (mc.group(1) if mc else _md_text(mh.group(1)).split("(")[0].strip())[:60]
            continue
        mt = re.match(r"^- \*\*Tripwire:\*\*\s+(.+)", line)
        if mt:
            txt = _md_text(mt.group(1))
            cur["tripwire"] = (txt[:300].rstrip() + "…") if len(txt) > 300 else txt
            continue
        ms = re.match(r"^- \*\*Status:\*\*\s+(.+)", line)
        if ms:
            cur["status"], cur["state"] = _status_state(ms.group(1))
    order = [("ai", "AI datacenter supply chain"), ("def", "Defense & Drones"), ("hum", "Humanoid Robots")]
    groups = [{"key": k, "label": lab, "color": DOMAIN_HEX[k],
               "entries": [e for e in entries if e["domain"] == k]} for k, lab in order]
    return {"kind": "register", "groups": [g for g in groups if g["entries"]],
            "fired": sum(1 for e in entries if e["state"] == "fired"), "total": len(entries)}


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _md_text(s):
    """Markdown → plain compact text: drop **/*/`, [[Target|alias]] → alias-or-target."""
    s = WL.sub(lambda m: (m.group(2) or m.group(1)).strip(), s)
    return re.sub(r"\*\*|\*|`", "", s).strip()


def _emoji_state(status):
    """spread-watch status emoji → state class. ⚪ calm · 🟢 nominal · 🟡 watch · 🔴 fired."""
    if "🔴" in status:
        return "fired"
    if "🟡" in status:
        return "watch"
    if "🟢" in status:
        return "nominal"
    return "calm"


def _dial_flag(status, asof, stale_days, today):
    t = status.upper()
    if "STALE" in t:
        return (f"STALE >{stale_days}d", "stale")
    if "NOT YET READ" in t or "UNREAD" in t or "NEEDS FIRST" in t or asof.strip() in ("—", ""):
        return ("UNREAD", "unread")
    return freshness_flag(asof, stale_days, today)


def parse_spread(body, slugmap, rel, stale_days, today):
    """AI-credit-spread-watch → the 9-dial board."""
    dials, in_tbl = [], False
    for line in body.splitlines():
        if line.startswith("## Current readings"):
            in_tbl = True; continue
        if in_tbl and line.startswith("## "):
            break
        if in_tbl and line.startswith("|"):
            c = _cells(line)
            if len(c) >= 5 and c[0].isdigit():
                status = c[4]
                flag, fcls = _dial_flag(status, c[3], stale_days, today)
                dials.append({"n": c[0], "name": _md_text(c[1]),
                              "reading": render_inline(c[2], slugmap, rel),
                              "asof": _md_text(c[3]), "status": _md_text(status).lstrip("⚪🟢🟡🔴 ").strip(),
                              "state": _emoji_state(status), "flag": flag, "fcls": fcls})
    return {"kind": "dials", "dials": dials}


def parse_short(body, slugmap, rel, stale_days, today):
    """short-interest → the sortable screener (from the fenced auto-refresh table)."""
    rows = []
    for line in body.splitlines():
        if not line.startswith("|"):
            continue
        c = _cells(line)
        if len(c) >= 7 and c[0] not in ("ticker", "---") and not c[0].startswith("---"):
            tk = _md_text(c[0])
            if not re.match(r"^[A-Z]{1,6}$", tk):
                continue
            read = _md_text(c[5]).upper()
            vstate = "confirm" if "CONFIRM" in read else "challenge" if "CHALLENGE" in read else "none"
            try:
                pct = float(re.sub(r"[^\d.]", "", c[2]) or 0)
            except ValueError:
                pct = 0.0
            try:
                dtc = float(re.sub(r"[^\d.]", "", c[3]) or 0)
            except ValueError:
                dtc = 0.0
            delta = _md_text(c[4])
            rising = delta.startswith("+")
            mp = slugmap.get(tk)
            rows.append({"ticker": tk, "out": (rel + mp) if mp else None, "shortInt": _md_text(c[1]),
                         "pctOut": c[2].replace("**", "").strip(), "pct": pct, "dtc": dtc,
                         "daysCover": _md_text(c[3]), "delta": delta, "rising": rising,
                         "vaultRead": read if vstate != "none" else "—", "vstate": vstate,
                         "thesis": _md_text(c[6])})
    rows.sort(key=lambda r: r["pct"], reverse=True)
    return {"kind": "screener", "rows": rows}


def parse_capex(body, slugmap, rel, stale_days, today):
    """hyperscaler-capex → the 7-payer matrix."""
    rows = []
    for line in body.splitlines():
        if not line.startswith("| [["):
            continue
        c = _cells(line)
        if len(c) < 7:
            continue
        wl = WL.search(c[0])
        tk = wl.group(1) if wl else _md_text(c[0]).split()[0]
        kind = "RENT" if tk in ("CRWV", "NBIS") else "BUILD"
        mp = slugmap.get(tk)
        rows.append({"payer": tk, "out": (rel + mp) if mp else None, "kind": kind,
                     "fy25": _md_text(c[1]), "guidance": _md_text(c[2]), "latestQ": _md_text(c[3]),
                     "style": _md_text(c[4]), "silicon": _md_text(c[5]), "backlog": _md_text(c[6]),
                     "note": _md_text(c[7]) if len(c) > 7 else ""})
    return {"kind": "matrix", "rows": rows}


CHINA_MAG = {"ultra": "#ff4d42", "high": "#ff8a3c", "med": "#f7a21b", "medium": "#f7a21b", "low": "#7d8aa0"}


def parse_china(body, slugmap, rel, stale_days, today):
    """china-exposure → the 8-axis (A–H) heatmap."""
    rows, AXES = [], list("ABCDEFGH")
    for line in body.splitlines():
        if not line.startswith("| [["):
            continue
        c = _cells(line)
        if len(c) < 4:
            continue
        tk = _md_text(c[0])
        # axes cell = comma/space-separated single letters (A–H); a parenthetical note like
        # "(none-direct)" is NOT axes — only count standalone A–H tokens.
        have = set(t for t in re.split(r"[,\s]+", _md_text(c[1]).upper()) if re.fullmatch(r"[A-H]", t))
        magfull = _md_text(c[2]).lower()
        magword = re.match(r"\s*([a-z-]+)", magfull)
        mag = magword.group(1) if magword else magfull   # "high (domiciled)" → "high"; "low-med" → "low-med"
        color = CHINA_MAG.get(mag, CHINA_MAG.get(mag.split("-")[0], "#646c75"))
        mp = slugmap.get(tk)
        rows.append({"ticker": tk, "out": (rel + mp) if mp else None, "mag": magfull.upper(), "color": color,
                     "cells": [{"ax": a, "on": a in have} for a in AXES],
                     "evidence": _md_text(c[3])[:200]})
    return {"kind": "heatmap", "rows": rows,
            "axis_key": [("A", "China revenue"), ("B", "Supply / sourcing"), ("C", "Taiwan-fab / China-assembly"),
                         ("D", "Outbound export-control"), ("E", "Inbound export-control"), ("F", "Chinese competitor"),
                         ("G", "Adversary-demand (defense)"), ("H", "China operations")],
            "legend": [("ULTRA", "#ff4d42"), ("HIGH", "#ff8a3c"), ("MED", "#f7a21b"), ("LOW", "#7d8aa0")]}


FE_DOMAIN = {"ai datacenter": "ai", "humanoid robots": "hum", "defense & drones": "def"}


def parse_forward(body, slugmap, rel, stale_days, today):
    """forward-edge → the 12 consensus-vs-vault cards."""
    cards, domain, cur = [], None, None

    def flush():
        if cur and cur.get("consensus") and cur.get("vaultView"):
            cards.append(cur)
    for line in body.splitlines():
        m2 = re.match(r"^## (.+)", line)
        if m2:
            flush(); cur = None
            domain = FE_DOMAIN.get(re.sub(r"<[^>]+>", "", m2.group(1)).strip().lower())
            continue
        if domain is None:
            continue
        m3 = re.match(r"^### (.+)", line)
        if m3:
            flush()
            title = _md_text(m3.group(1))
            cur = {"domain": domain, "title": title, "subjects": "", "durability": "",
                   "inverse": "inverse div" in m3.group(1).lower(), "consensus": "", "vaultView": "",
                   "catalyst": "", "falsifier": "", "lastMoved": "", "hex": DOMAIN_HEX[domain]}
            continue
        if not cur:
            continue
        ms = re.match(r"^\*\*Subjects?:\*\*\s+(.+)", line)
        if ms:
            parts = re.split(r"—\s*\*\*Durability:\*\*", ms.group(1))
            cur["subjects"] = _md_text(parts[0])
            if len(parts) > 1:
                cur["durability"] = _md_text(parts[1])
            continue
        for key, lab in (("consensus", "Consensus"), ("vaultView", "Vault view"),
                         ("catalyst", "Catalyst"), ("falsifier", "Falsifier"), ("lastMoved", "Last moved")):
            mm = re.match(r"^- \*\*" + lab + r"[^:*]*:?\*\*[:\s]+(.+)", line)
            if mm:
                cur[key] = _md_text(mm.group(1))[:300]
                break
    flush()
    return {"kind": "cards", "cards": cards,
            "counts": {d: sum(1 for c in cards if c["domain"] == d) for d in ("ai", "hum", "def")}}


def tracker_hero(slug, body, slugmap, rel, stale_days, today):
    """Dispatch to the per-tracker parser. Unknown slug → None (prose-only fallback)."""
    fn = {"what-could-go-wrong": parse_wcgw, "AI-credit-spread-watch": parse_spread,
          "short-interest": parse_short, "hyperscaler-capex": parse_capex,
          "china-exposure": parse_china, "forward-edge-tracker": parse_forward}.get(slug)
    if not fn:
        return None
    if fn is parse_wcgw:
        return fn(body, slugmap, rel)
    return fn(body, slugmap, rel, stale_days, today)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", help="build just one page by slug (e.g. NVDA)")
    ap.add_argument("--audit", metavar="TICKER", help="print QA facts for one company page (no build)")
    ap.add_argument("--json", action="store_true", help="machine-readable audit output (with --audit)")
    args = ap.parse_args()
    if args.audit:
        return audit(args.audit, args.json)

    dist = WEB / "dist"
    pages, slugmap, src = index_pages()
    SITE = load_site()
    from datetime import date as _date
    _t = _date.today()
    today_int = _t.year * 365 + _t.month * 30 + _t.day
    stale_days = (SITE.get("freshness") or {}).get("stale_days", 45)
    counts = {g: len(src.get(g, [])) for g, _l, _t2 in GROUP_ORDER}
    section_tabs = [{"label": lab, "key": k, "color": SECTION_COLOR[k],
                     "out": ("index.html" if k == "home" else f"{k}/index.html"),
                     "count": counts.get(k)} for lab, k in SECTION_TABS]

    # nav groups + search index
    nav_groups, search = [], []
    for gkey, label, ptype in GROUP_ORDER:
        items = []
        for p in src[gkey]:
            r = pages[p.stem]
            items.append({"slug": r["slug"], "title": r["title"][:40], "out": r["out"],
                          "ticker": r["tickers"][0] if r["tickers"] else "",
                          "domain": r["domain"], "domain_hex": DOMAIN_HEX[r["domain"]]})
            search.append({"title": r["title"], "type": r["type"], "out": r["out"], "tickers": r["tickers"]})
        if items:
            nav_groups.append({"label": label, "items": items})

    # structural tape (from layer/tier — never prices)
    tape = []
    for slug in list(pages)[:40]:
        r = pages[slug]; fm = r["fm"]; toks = []
        if fm.get("layer"):
            toks.append(f"L{fm['layer']}")
        for k, lab in (("photonics_tier", "PHO"), ("humanoid_tier", "HUM"), ("defense_tier", "DEF"),
                       ("energy_power_tier", "PWR"), ("memory_tier", "MEM"), ("materials_tier", "MAT")):
            if isinstance(fm.get(k), int):
                toks.append(f"{lab}{fm[k]}"); break
        if r["type"] == "chokepoint":
            toks.append("CHOKE")
        if toks:
            tape.append({"tk": (r["tickers"][0] if r["tickers"] else slug)[:8],
                         "meta": "·".join(toks), "hex": DOMAIN_HEX[r["domain"]]})
    tape = tape[:22] or [{"tk": "VAULT", "meta": f"{len(pages)} PAGES", "hex": "#f7a21b"}]

    # ── render ──
    env = Environment(loader=FileSystemLoader(str(WEB / "templates")), autoescape=select_autoescape(["html"]))
    shared = {"nav_groups": nav_groups, "tape_items": tape, "total": len(pages),
              "section_tabs": section_tabs}

    def rel_for(out):                # ../ depth from a page to dist root
        return "../" * out.count("/")

    targets = [pages[args.only]] if args.only else list(pages.values())
    if args.only and args.only not in pages:
        print(f"✗ no page slug '{args.only}'"); return 1

    # build the requested page(s)
    for r in targets:
        rel = rel_for(r["out"])
        body_html, toc = render_body(r["body"], slugmap, rel)
        subtitle_html = render_inline(r["subtitle"], slugmap, rel)
        bl = [{"title": pages[s]["title"][:34], "type": pages[s]["type"], "out": pages[s]["out"],
               "domain_hex": DOMAIN_HEX[pages[s]["domain"]]} for s in sorted(set(r["backlinks"]))]
        # member tickers (themes/chokepoints/trackers list companies) → links to their pages
        members = []
        for tk in (r["tickers"] if r["type"] != "company" else []):
            mp = pages.get(tk) or pages.get(str(tk).upper())
            if mp and mp["type"] == "company":
                members.append({"tk": tk, "out": mp["out"], "hex": DOMAIN_HEX[mp["domain"]]})
            else:
                members.append({"tk": tk, "out": None, "hex": DOMAIN_HEX["none"]})
        route_label = (r["tickers"][0] + " US" if r["type"] == "company" and r["tickers"] else r["slug"])
        accent = {"chokepoint": "#ff4d42", "tracker": SECTION_COLOR["trackers"]}.get(r["type"], DOMAIN_HEX[r["domain"]])
        page = dict(r, badges=badges_for(r["fm"], r["domain"]), body_html=body_html,
                    subtitle_html=subtitle_html, toc=toc, backlinks=bl, members=members, accent_hex=accent,
                    pill=r["type"].upper(), pattern=r["fm"].get("pattern"), active_tab=r["group"],
                    members_label={"theme": "Companies in this theme", "chokepoint": "Companies exposed",
                                   "tracker": "Tickers tracked",
                                   "relationship": "Companies in this relationship"}.get(r["type"], "Companies"))
        if r["type"] == "tracker":
            page["meta"] = (SITE.get("trackers") or {}).get(r["slug"], {})
            page["hero"] = tracker_hero(r["slug"], r["body"], slugmap, rel, stale_days, today_int)
        ctx = dict(shared, rel=rel, route_label=route_label, active_tab=r["group"],
                   route_kind={"company": "equity", "chokepoint": "chokepoint"}.get(r["type"], r["type"]),
                   page=page)
        tpl = {"company": "company.html", "theme": "theme.html", "relationship": "theme.html",
               "chokepoint": "theme.html", "thesis": "document.html", "framework": "document.html",
               "tracker": "tracker.html"}.get(r["type"], "company.html")
        html = env.get_template(tpl).render(**ctx)
        op = dist / r["out"]; op.parent.mkdir(parents=True, exist_ok=True); op.write_text(html)

    # ── Home (dist/index.html) + section-index pages (dist/<group>/index.html) ──
    if not args.only:
        home = SITE.get("home", {})
        # resolve recently-updated + chokepoint-board links to built out-paths
        recent = []
        for it in home.get("recently_updated", []):
            mp = pages.get(it["slug"])
            recent.append(dict(it, out=("" if not mp else mp["out"]),
                               hex=DOMAIN_HEX.get({"company": "ai"}.get(it["type"], "none")) if not mp else DOMAIN_HEX[mp["domain"]]))
        GRADE_HEX = {"physics": "#ff4d42", "precision": "#f7a21b", "integration": "#2f9bff"}
        board = []
        for b in (SITE.get("chokepoint_board") or []):
            mp = pages.get(b["slug"])
            board.append(dict(b, out=(mp["out"] if mp else ""), color=GRADE_HEX.get(b["grade"], "#646c75")))
        grade_legend = {"physics": {"color": "#ff4d42", "label": "Physics / yield-grade — hardest"},
                        "precision": {"color": "#f7a21b", "label": "Precision-manufacturing — middle"},
                        "integration": {"color": "#2f9bff", "label": "Integration / assembly — easiest"}}
        html = env.get_template("home.html").render(
            **dict(shared, rel="", route_label="HOME", route_kind="vault", active_tab="home",
                   home=home, stat_total=len(pages), counts=counts, recent=recent,
                   board=board, grade_legend=grade_legend))
        (dist / "index.html").write_text(html)
        for gkey, label, ptype in GROUP_ORDER:
            sitems = [{"slug": pages[p.stem]["slug"], "title": pages[p.stem]["title"], "out": pages[p.stem]["out"],
                       "hex": DOMAIN_HEX[pages[p.stem]["domain"]], "ticker": (pages[p.stem]["tickers"][0] if pages[p.stem]["tickers"] else "")}
                      for p in src[gkey]]
            smeta = (SITE.get("sections") or {}).get(gkey, {})
            html = env.get_template("section-index.html").render(
                **dict(shared, rel="../", route_label=label.upper(), route_kind="index", active_tab=gkey,
                       sec_key=gkey, sec_label=label, sec_color=SECTION_COLOR.get(gkey, "#f7a21b"),
                       sec_desc=smeta.get("desc", ""), sec_count=len(sitems), sec_items=sitems))
            (dist / gkey / "index.html").write_text(html)

        # ── Structure page (dist/structure.html) — 3 views: board · layer map · graph ──
        # View 1: chokepoint board (already resolved above as `board`, ranked by durability).
        # View 2: value-chain map — group companies by layer 1–6.
        layer_map = []
        for L in range(1, 7):
            chips = []
            for slug, rec in pages.items():
                if rec["type"] != "company":
                    continue
                if L in layer_ints(rec["fm"].get("layer")):
                    tk = rec["tickers"][0] if rec["tickers"] else slug
                    chips.append({"tk": tk, "out": rec["out"], "hex": DOMAIN_HEX[rec["domain"]]})
            chips.sort(key=lambda c: c["tk"])
            layer_map.append({"n": L, "color": LAYER_SCALE[L - 1],
                              "title": LAYER_TITLES[L - 1], "chips": chips})
        # View 3: connection graph — center on the highest-backlink node, 2 rings of neighbors.
        deg = {s: len(set(r["backlinks"])) for s, r in pages.items()}
        # every ranking carries the slug as a deterministic tiebreaker (set iteration order is
        # hash-randomized per process, so degree-ties alone would make the build non-deterministic).
        center = max(deg, key=lambda s: (deg[s], s)) if deg else "NVDA"
        cset = set(pages[center]["wikilinks"]) | set(pages[center]["backlinks"])
        ring1 = sorted([s for s in cset if s in pages and s != center],
                       key=lambda s: (-deg.get(s, 0), s))[:11]
        r1set = set(ring1)
        cand2 = set()
        for s in ring1:
            cand2 |= set(pages[s]["wikilinks"]) | set(pages[s]["backlinks"])
        ring2 = sorted([s for s in cand2 if s in pages and s != center and s not in r1set],
                       key=lambda s: (-deg.get(s, 0), s))[:14]
        placed = [center] + ring1 + ring2
        pset = set(placed)
        ringof = {center: 0, **{s: 1 for s in ring1}, **{s: 2 for s in ring2}}
        DOM_OF_TYPE = {"chokepoint": "choke", "theme": "theme", "tracker": "tracker"}
        gnodes = []
        for s in placed:
            r = pages[s]
            dom = DOM_OF_TYPE.get(r["type"], r["domain"])
            # companies → their own ticker; chokepoints/themes/trackers → their own slug
            # (their tickers[0] is a RELATED company, which would mislabel + collide on the graph)
            label = (r["tickers"][0] if r["type"] == "company" and r["tickers"] else s)
            gnodes.append({"id": s, "label": label[:16],
                           "ring": ringof[s], "deg": deg.get(s, 0), "type": r["type"],
                           "hex": GRAPH_HEX.get(dom, DOMAIN_HEX.get(dom, "#646c75")),
                           "out": r["out"]})
        # keep the hub-and-spoke readable: draw an edge only if at least one endpoint is the
        # center or ring1 — this drops the ring2↔ring2 cross-links that turn it into a hairball.
        hub = {center} | r1set
        gedges = []
        seen_e = set()
        for s in placed:                                  # placed is an ordered list (deterministic)
            for t in sorted(set(pages[s]["wikilinks"])):  # sort targets so edge order is stable
                if t in pset and t != s and (t, s) not in seen_e and (s in hub or t in hub):
                    seen_e.add((s, t)); gedges.append({"a": s, "b": t})
        html = env.get_template("structure.html").render(
            **dict(shared, rel="", route_label="STRUCTURE", route_kind="analytics", active_tab="structure",
                   board=board, grade_legend=grade_legend, layer_map=layer_map,
                   graph={"nodes": gnodes, "edges": gedges, "center": center}))
        (dist / "structure.html").write_text(html)

    # assets + search index
    adst = dist / "assets"; adst.mkdir(parents=True, exist_ok=True)
    for f in (WEB / "assets").glob("*.*"):
        shutil.copy(f, adst / f.name)
    (dist / "search-index.json").write_text(json.dumps(search))
    print(f"✓ built {len(targets)} page(s) → web/dist/  ({len(pages)} indexed, {len(search)} in search)")
    if args.only:
        print(f"  open: file://{(dist / targets[0]['out']).resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
