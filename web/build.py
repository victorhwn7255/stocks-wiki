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

WEB = Path(__file__).resolve().parent
ROOT = WEB.parent
sys.path.insert(0, str(ROOT / "scripts"))
import vault_parsers as vp          # noqa: E402
import markdown as md               # noqa: E402
from jinja2 import Environment, FileSystemLoader, select_autoescape  # noqa: E402

DOMAIN_HEX = {"ai": "#2f9bff", "def": "#f7a21b", "hum": "#4defc4", "mat": "#ff8a3c", "none": "#646c75"}
LAYER_SCALE = ["#5ab0ff", "#4defc4", "#9bd64f", "#f7a21b", "#ff7a3c", "#ff5a4a"]  # L1..L6
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


AI_TIERS = ("photonics_tier", "energy_power_tier", "equipment_tier", "materials_tier", "memory_tier")


def layer_ints(layer):
    """Layer can be an int (1), a straddle string ('1, 2'), or 'outside' — return the ints."""
    if isinstance(layer, int):
        return [layer]
    if isinstance(layer, str):
        return [int(x) for x in re.findall(r"\d+", layer)]
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
    """[[Target]] / [[Target|alias]] → an <a> link (amber if resolved, dimmed if a forward-ref)."""
    def repl(m):
        target, alias = m.group(1).strip(), (m.group(2) or "").strip()
        label = alias or target
        out = slugmap.get(target) or slugmap.get(target.upper())
        if out:
            return f'<a class="wl" href="{rel}{out}">{label}</a>'
        return f'<a class="wl dead" title="forward-reference (page not yet created)">{label}</a>'
    return WL.sub(repl, text)


def preprocess_md(body):
    """Two canon-safe line fixes before markdown (both skip fenced code):
    (1) sane_lists needs a blank line before a list that abuts a paragraph — the vault writes
        `**Lead-in:**` directly above its bullets, so the markers leak as literal '- ' / '1.' text.
    (2) a leading single-* footnote marker (e.g. `*FY2025 COGS …`) opens a stray <em> that
        mis-pairs with a later **bold**; escape it so the '*' stays literal. Skip a *fully
        italic-wrapped* line (ends with '*') and '** bold' lead-ins (handled by FOOTNOTE_RE)."""
    out, prev, fence = [], "", False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
            out.append(line); prev = line; continue
        if not fence:
            if LIST_RE.match(line) and prev.strip() and not LIST_RE.match(prev):
                out.append("")
            # escape a DANGLING leading footnote '*' (no partner '*' to close it) so it doesn't
            # open a stray <em>; leave real italic spans (which have a closing '*') alone.
            elif FOOTNOTE_RE.match(line) and line.replace("**", "").count("*") == 1:
                line = "\\" + line
        out.append(line); prev = line
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
            pages[slug] = {"slug": slug, "type": ptype, "group": gkey, "path": p,
                           "title": title or slug, "subtitle": sub, "body": rest,
                           "fm": fm, "tickers": vp.extract_tickers_from_frontmatter(fm),
                           "last_updated": vp.get_last_updated(fm), "domain": domain_of(fm, body),
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
    shared = {"nav_groups": nav_groups, "tape_items": tape, "total": len(pages)}

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
        ctx = dict(shared, rel=rel, route_label=(r["tickers"][0] + " US" if r["tickers"] else r["slug"]),
                   route_kind={"company": "equity", "chokepoint": "chokepoint"}.get(r["type"], r["type"]),
                   fkey={"company": "company", "chokepoint": "chokepoint"}.get(r["type"], "home"),
                   page=dict(r, badges=badges_for(r["fm"], r["domain"]), body_html=body_html,
                             subtitle_html=subtitle_html, toc=toc, backlinks=bl))
        tpl = {"company": "company.html"}.get(r["type"], "company.html")  # phase 1: company template
        html = env.get_template(tpl).render(**ctx)
        op = dist / r["out"]; op.parent.mkdir(parents=True, exist_ok=True); op.write_text(html)

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
