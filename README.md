![stocks-wiki — a source-grounded, agent-maintained research vault](design/stocks-wiki-banner.png)

# stocks-wiki

**A source-grounded, agent-maintained research vault for long-horizon investment analysis — and a working reference design for how to build durable, human-in-the-loop AI knowledge systems.**

stocks-wiki is a personal research vault that maps where durable value sits across three multi-year investment theses — the **AI-datacenter supply chain**, **Defense & Drones (unmanned systems)**, and **Humanoid Robots** — by finding the *chokepoints* each supply chain can't route around. It is ~135 interlinked Markdown pages (~700k words), grown one primary source at a time, and maintained by an AI agent (Claude Code) that operates under a strict, written constitution.

The interesting part isn't the stock analysis. It's the **system**: a design for using a large language model as a research partner *without* letting the model's confident-but-wrong tendencies pollute a knowledge base you actually trust. Every fact is tied to a primary source. Unverified signal is quarantined from verified knowledge. The agent's memory survives across sessions. And a human stays in the loop at every gate that matters.

> **This is a thinking tool, not a trading app.** It describes structural position and moat durability. It never gives buy/sell calls, price targets, or position sizing — *"what would have to be true"*, not *"you should buy."* Nothing here is investment advice.

---

## WHY — the problems this is built to solve

Anyone who has tried to do serious, long-running research *with* an LLM runs into the same five walls. stocks-wiki is an answer to each.

### 1. Source-grounded reasoning — LLMs hallucinate, and investment decisions can't be built on plausible fiction
Ask a model about a company's customer concentration and it will happily invent a number that *sounds* right. For research that informs real capital, "sounds right" is worthless. The system needs a hard rule that **every claim traces to a primary source**, and a way to keep the model's fluent guesses from ever being mistaken for fact.

### 2. Long-form, long-term context memory — the research is bigger than any context window
Years of accumulated analysis across 135+ pages is far larger than any model's context window, and it keeps growing. You cannot hold it all in a prompt, and you cannot afford to re-derive it every time. The knowledge has to live **outside** the model, in a form that is durable, searchable, and cheap to reload the relevant slice of.

### 3. Persistent memory across sessions — every conversation starts from zero
Each new session is a blank slate. Without deliberate design, the agent forgets what it concluded yesterday, re-litigates settled decisions, and loses the thread of a multi-quarter thesis. The system needs a way to **reconstruct full working context** — what's known, what changed, what's still open — at the start of every session.

### 4. Honest reasoning — models flatter, and so do we
LLMs lean agreeable; humans lean toward confirming what they already believe (especially about positions they hold). Left alone, that combination manufactures a bullish narrative for every name. A research vault is only useful if it will **tell you when your thesis is weak**, pre-register what would prove it *wrong*, and later grade whether it was right.

### 5. Automation & agentic workflow — manual research doesn't compound
Reading filings, transcribing interviews, sweeping the news, checking for stale pages — done by hand, none of it scales, and the insights don't accumulate. The system needs **agentic workflows** that do the mechanical work, surface leads, and feed a self-improving loop — *safely*, without a runaway agent rewriting the knowledge base overnight.

---

## WHAT — the system and its key design ideas

stocks-wiki is built on **[Claude Code](https://claude.com/claude-code)** operating over an **Obsidian Markdown vault** (plain files, wikilinks, git). The content is a knowledge graph; the machinery around it is what makes the graph trustworthy.

### The knowledge graph
- **~135 interlinked pages** across five page types: `companies/` (~84), `chokepoints/` (~15), `themes/` (~28), `trackers/` (~7, live status dashboards), and `relationships/` (cross-company dependency maps) — plus a macro `insights/` layer.
- Every page carries **YAML frontmatter** (type, tickers, value-capture layer, per-domain tier scores, `last_updated`) and links to related pages with `[[wikilinks]]`, so the vault renders as a navigable graph.
- Three **human-owned anchor documents** per domain (`_thesis*.md` + `frameworks*.md`) define the questions and the analytical scaffolding. The agent enriches the analysis; it never edits the anchors.

### The design ideas that make it work

| Idea | What it is |
|---|---|
| **Source hierarchy** | A five-tier ranking of every input — Tier 1 primary filings (10-K/10-Q/20-F) → Tier 2 earnings calls → Tier 3 independent analysis → Tier 4 news → Tier 5 social. Higher tier wins on facts; every number cites its source *and* period. |
| **Discovery vs. canon separation** | Verified knowledge ("canon") is walled off from raw signal ("discovery"). YouTube, Twitter, press releases, and news land in a quarantined discovery zone, tagged `[verify: …]`, and reach a canonical page **only** through a human-gated ingest. |
| **Externalized memory** | The vault *is* the model's long-term memory. A compressed `MEMORY.md`, an append-only `log.md`, a `refresh_log.md` (per-company quarter-over-quarter deltas), and a `conventions-ledger.md` mirror it — so any fresh session can reload exactly the slice it needs. |
| **A living constitution** | `CLAUDE.md` is a versioned (currently v10.2) operating manual the agent must follow — source rules, citation discipline, page conventions, the disciplines below. Recurring patterns get **codified into new rules at their third observed instance**, so the system's own methodology compounds. |
| **Skills as composable agent tools** | 23 slash-command **skills** (e.g. `/youtube-intel`, `/latest-alpha`, `/chokepoint-eval`, `/bear-case`, `/research-loop`) each encode a repeatable workflow with its own safety boundary. |
| **Deterministic scripts for cheap work** | 17 Python scripts do the LLM-free heavy lifting — fetch SEC filings, score co-mention clusters, run a reverse-DCF, check link integrity — so the model spends its judgment only where judgment is needed. |
| **Multi-agent workflows** | Broad tasks fan out to parallel sub-agents (read N subsystems at once, generate independent analyses, then adversarially verify) before a result is trusted. |
| **Calibration & falsifiability** | Theses ship with **pre-registered falsifiers and catalysts**; a calibration loop later grades them RIGHT / WRONG / PARTIAL — turning opinions into a scored track record. |
| **A self-learning automation layer** | A headless, *discovery-only + propose-only* automation harness runs background analysis and drops proposals into queues a human reviews. It fills the queues; the human empties them. |
| **A public terminal reading layer** | A zero-dependency static site generator renders the canon into a Bloomberg-terminal-style website (`web/` → Vercel) whose "tape" streams *structure* — layers, tiers, chokepoint grades — never prices. |

### The disciplines (the editorial voice, enforced in the constitution)
- **Describe, don't recommend** — analyze structural position; never prescribe a trade.
- **Honest-verdict** — when a company's thesis fit is weak, the page says so plainly and stays short.
- **Thesis tool, not portfolio tracker** — no P&L, no position sizes, ever. You can't tell what the author owns from reading it.
- **Host tensions honestly** — uncomfortable conclusions are the point, not a bug.

---

## HOW — how the design solves each problem, and how it's built

Each wall from the **WHY** section maps to a concrete mechanism:

### How it grounds reasoning (→ Problem 1)
The **source hierarchy** is enforced at every write. A page is created *because a source informed it*, not because a name came up. Every numerical or non-obvious claim names its source and period inline (`CoWoS capacity expansion (TSM Q1 2026 call)`). Facts flow up the tier ladder; when sources disagree, the higher tier wins and the disagreement is flagged rather than silently reconciled. The result is a vault where you can audit any sentence back to a filing.

### How it holds long-term context (→ Problem 2)
Knowledge lives in **plain Markdown files**, not in the model. Once a primary source is ingested and its analysis lands on a page, future sessions read the *page*, not the raw filing — the source stays in `raw/` as an audit trail. **Page-lifecycle rules** (rolling financial snapshots, an open-questions watch-list, third-refresh compaction) keep pages from growing without bound, so the vault stays dense instead of bloated as it ages.

### How it persists across sessions (→ Problem 3)
A dedicated **`/agent-onboarding`** skill gives any fresh agent a canonical read-order: anchors → current state (`MEMORY.md`, `log.md`, `index.md`) → substantive pages. `MEMORY.md` is auto-loaded every session as a time-stamped snapshot of vault state, open threads, and monitoring counts. The effect is that session *N+1* picks up with the full working context of session *N* — the break is invisible.

### How it stays honest (→ Problem 4)
Honesty is structural, not aspirational. The **honest-verdict** and **describe-don't-recommend** disciplines are written into the constitution and applied on every page. Theses carry **pre-registered falsifiers** ("what would prove this wrong"), collected in a vault-level `what-could-go-wrong` risk register and a `forward-edge-tracker` of where the vault's view *diverges* from consensus. A **calibration loop** later scores those pre-registered calls, so the vault grades its own accuracy instead of quietly forgetting its misses.

### How it automates safely (→ Problem 5)
This is the crux. Every automated or discovery-mode action runs under one contract: **discovery-only + propose-only**. Discovery skills (`/youtube-intel`, `/twitter-intel`, `/latest-alpha`, `/research-loop`) and the headless automation harness may *read* anything and *write* only to quarantined discovery zones — they **cannot** edit a canonical page, the human-owned anchors, or the index; they cannot run git; they cannot bump a `last_updated`. Enforcement is a **restricted tool allow-list** (`Read, Grep, Glob, Bash` + `Write` scoped to the discovery folder — no `Edit` on canon). When automation finds something worth keeping, it drops a proposal in a queue; a human reviews it and runs the normal, gated ingest. The machine surfaces leads at scale; the human remains the only path into canon.

### How the pieces fit together (the build)
```
raw/            # source material — read-only ground truth
  filings/  transcripts/  research/  news/  notes/  data/
wiki/           # canon — the agent's curated domain (write + interlink)
  _thesis*.md  companies/  chokepoints/  themes/  trackers/  relationships/  insights/
raw/notes/      # human frameworks + quarantined discovery logs (video-intel, twitter-intel, latest-alpha, …)
.claude/skills/ # 23 composable agent workflows
scripts/        # 17 deterministic Python tools (fetch, score, check — LLM-free)
automation/     # the headless self-learning loop (discovery-only + propose-only)
prompts/        # kickoff templates for the human-gated two-stop ingest
web/            # static-site generator → public Bloomberg-terminal reading layer
CLAUDE.md       # the living constitution every agent obeys
index.md log.md # catalog + append-only activity record
```
The core loop, end to end: a human **curates a source** → drafts a session kickoff from a template → the agent runs a **two-stop ingest** (plan → human approval → execute) → the analysis lands on a page with citations → trackers and related pages propagate → `log.md`, `MEMORY.md`, and the refresh log record the delta → discovery skills and the automation layer continuously surface the *next* thing to verify. The human curates and asks the questions; the agent maintains the wiki.

---

## WHO — who this is for

**Serious self-directed investors and research analysts** who want a durable "second brain" for long-horizon, source-heavy analysis — a place where a thesis is built up over quarters, every claim is auditable, and the system tells them when they're wrong. (The subject here is supply-chain chokepoints; the pattern fits any research-intensive domain.)

**Builders of agentic knowledge systems.** If you're designing a serious workflow on Claude Code or any LLM agent, this is a worked example of the hard parts: grounding output in sources, separating verified knowledge from raw signal, giving an agent memory that survives sessions, encoding a methodology as an enforceable constitution, and — most importantly — **letting an agent do real work without letting it corrupt the thing it's working on.**

**Anyone doing long-running, high-stakes research with an AI partner** who has hit the walls in the WHY section — hallucination, context limits, session amnesia, sycophancy, un-scalable manual work — and wants a concrete architecture rather than a prompt trick.

**Who it is *not* for:** anyone looking for stock tips, buy/sell signals, price targets, or a plug-and-play SaaS product. There are none here by design. It rewards people who want to *understand structure*, not be told what to trade.

---

## Status & disclaimer

The knowledge graph, the skills, the deterministic scripts, the constitution, and the public site are **actively maintained and working**. The headless nightly automation loop is **scaffolded and partly wired** — the contract, scripts, and orchestration design exist; the scheduler is being rolled out in phases. The Humanoid-Robots domain anchors are a deliberately *living* draft.

> **Not investment advice.** stocks-wiki describes structural position and moat durability for research purposes only. It contains no buy/sell recommendations, price targets, or position sizing, and reveals nothing about any actual holdings. Do your own diligence.
