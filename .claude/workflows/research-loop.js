export const meta = {
  name: 'research-loop',
  description: 'Vault-aware deep research for the stocks-wiki vault: scope a topic into 15 angles, research (two-sided) + verify each, run 8 grounded vault-connection agents, then synthesize one cited Tier-3 report. The interactive sibling of automation/scripts/research_loop.py (which uses 10 angles — the interactive path runs 15 for breadth since it is attended; uses the Workflow tool, not headless claude -p).',
  whenToUse: 'When the user runs /research-loop <topic> — research a topic AND ground it in the existing vault (connections), interactively.',
  phases: [
    { title: 'Scope', detail: 'topic → 15 research angles' },
    { title: 'Research', detail: 'each angle: two-sided research → verify (concurrent)' },
    { title: 'Connect', detail: '8 grounded agents tie findings to the vault' },
    { title: 'Synthesize', detail: 'one cited report with a Vault connections section' },
  ],
}

// The 10 vault-connection specs — MIRROR of automation/scripts/research_loop.py `_connection_specs`.
// Keep in sync with that file (the headless source of truth). Each agent greps ONLY its slice and
// reports CONFIRM / CHALLENGE / EXTEND links (wikilink only verified pages); honest-verdict.
const CONNECTION_SPECS = [
  { label: 'companies-A', dir: 'the FIRST half of wiki/companies/*.md (A–M-ish)',
    lens: 'which companies/tickers named in the findings ALREADY have a page here, and what each finding adds or challenges about them' },
  { label: 'companies-B', dir: 'the SECOND half of wiki/companies/*.md (N–Z-ish)',
    lens: 'which companies/tickers named in the findings ALREADY have a page here, and what each finding adds or challenges about them' },
  { label: 'themes-A', dir: 'roughly the first half of wiki/themes/*.md',
    lens: 'do the findings CONFIRM / CHALLENGE / EXTEND any of these themes?' },
  { label: 'themes-B', dir: 'roughly the second half of wiki/themes/*.md',
    lens: 'do the findings CONFIRM / CHALLENGE / EXTEND any of these themes?' },
  { label: 'chokepoints-confirm', dir: 'all of wiki/chokepoints/*.md',
    lens: 'where do the findings CONFIRM or EXTEND a chokepoint thesis — reinforce the moat, durability, or value-capture story?' },
  { label: 'chokepoints-challenge', dir: 'all of wiki/chokepoints/*.md',
    lens: 'the ADVERSARIAL lens — where do the findings CHALLENGE or THREATEN a chokepoint thesis (faster substitution, quicker supply-response, a demand miss, a new entrant)?' },
  { label: 'trackers-relationships', dir: 'wiki/trackers/*.md + wiki/relationships/*.md',
    lens: 'does any finding FIRE a falsifier/catalyst/tripwire (what-could-go-wrong, forward-edge-tracker) or touch hyperscaler-capex / china-exposure / a bilateral relationship?' },
  { label: 'thesis-frameworks', dir: 'wiki/_thesis*.md + raw/notes/frameworks*.md',
    lens: 'does this FIT / EXTEND / CHALLENGE the vault worldview — the thesis or the analytical scaffolding (value-capture layers, chokepoint-quality gradient, tier frameworks)?' },
]

const ANGLES_SCHEMA = {
  type: 'object',
  properties: { angles: { type: 'array', items: { type: 'string' }, minItems: 15, maxItems: 15 } },
  required: ['angles'],
}

const topic = (args && args.topic) ? String(args.topic) : ''
if (!topic) {
  return { error: 'no topic — invoke as Workflow({ name: "research-loop", args: { topic: "..." } })' }
}

// ─── ① SCOPE ─────────────────────────────────────────────────────────────────
phase('Scope')
const scoped = await agent(
  `You are scoping a research plan. Topic:\n«${topic}»\n\n` +
  'Produce EXACTLY 15 focused, DISTINCT, non-overlapping research angles a stock analyst would ' +
  'investigate to answer it (value chain, chokepoint quality, competitors, demand, ' +
  'who-captures-value, risks/falsifiers, etc.). Never pad ' +
  'with overlapping angles; 15 means 15 genuinely distinct facets. Each angle a short phrase.',
  { schema: ANGLES_SCHEMA, label: 'scope', phase: 'Scope' },
)
const angles = (scoped && scoped.angles ? scoped.angles : []).slice(0, 15)
if (!angles.length) {
  return { error: 'scope produced no angles' }
}
log(`scope: ${angles.length} angles`)

// ─── ② RESEARCH (two-sided) → VERIFY (pipelined; angles run concurrently) ─────
// The old separate "challenge" stage was folded into the research prompt (it now researches
// two-sided), freeing the per-angle budget to run 15 angles for breadth (vs the headless 10).
// Verify stays 1:1 + independent — the hallucination catch we keep.
phase('Research')
const lbl = (a) => a.slice(0, 32)
const researched = await pipeline(
  angles,
  (a) => agent(
    `Research ONLY this angle of «${topic}»:\n«${a}»\n\n` +
    'Do focused web searches (5-8 reputable sources; prefer primary/company/industry over blogs). ' +
    'Tag each claim Tier 3 (independent analysis) or Tier 4 (news). Write 300-500 words of findings ' +
    'with inline source links. Be TWO-SIDED: for every load-bearing claim, also surface the strongest ' +
    'DISCONFIRMING evidence or counter-case (do a counter-search; don\'t write a one-sided pitch); flag ' +
    'any claim the counter-evidence weakens with [contested]. End with two lines: "Key number:" (the ' +
    'single most load-bearing figure + its source + a confidence tag high/med/low) and "Falsifier:" ' +
    '(the concrete evidence that would prove this angle\'s thesis WRONG). Output ONLY the findings ' +
    'markdown — no preamble.',
    { label: `research:${lbl(a)}`, phase: 'Research' },
  ),
  (research, a) => agent(
    `Findings on «${a}»:\n\n${research}\n\n` +
    'Sanity-check each load-bearing claim: is it supported by the cited source, and is any ' +
    'number/share plausibly correct? Flag unsupported or Tier-5/rumor claims inline with ' +
    '[unverified]. Output the same findings, lightly corrected/annotated. Markdown only.',
    { label: `verify:${lbl(a)}`, phase: 'Research' },
  ),
)
const findingsMd = angles
  .map((a, i) => `## Angle ${i + 1}: ${a}\n\n${researched[i] || '(this angle failed)'}`)
  .join('\n\n')

// ─── ③ CONNECTIONS — 8 grounded agents (barrier: all need the full findings) ─
phase('Connect')
const connections = (await parallel(CONNECTION_SPECS.map((s) => () =>
  agent(
    'You are finding connections between NEW research findings and an existing investment research ' +
    'vault (stocks-wiki). Be GROUNDED: use Read/Grep/Glob to check the ACTUAL vault files — NEVER ' +
    `invent a page you have not confirmed exists.\n\nTOPIC: «${topic}»\n\nFINDINGS:\n${findingsMd}\n\n` +
    `YOUR SLICE: ${s.dir}.\nYOUR LENS: ${s.lens}\n\n` +
    'For each REAL connection: name the vault page as a [[wikilink]] ONLY after verifying it exists ' +
    '(grep/glob first); say CONFIRM / CHALLENGE / EXTEND and cite the specific finding + the page ' +
    'claim it touches. ' + (s.tag ? s.tag + ' ' : '') +
    'HONEST-VERDICT: report ONLY meaningful connections. "(no material connection in this slice)" is ' +
    'a valid, good answer — do NOT manufacture links or list trivial co-mentions. Output ONLY a short ' +
    'markdown bullet list (or the no-material line). No preamble.',
    { label: `connect:${s.label}`, phase: 'Connect' },
  ).then((text) => ({ label: s.label, text })),
))).filter(Boolean)
const connectionsMd = connections
  .map((c) => `## Vault connection: ${c.label}\n\n${c.text}`)
  .join('\n\n')

// ─── ④ SYNTHESIS ─────────────────────────────────────────────────────────────
phase('Synthesize')
const report = await agent(
  `You are writing a Tier-3 discovery research anchor for an investment vault. Topic:\n«${topic}»\n\n` +
  `Here are the accumulated per-angle findings AND the vault-connection notes:\n\n${findingsMd}\n\n${connectionsMd}\n\n` +
  'Synthesize into a single cited report in this format:\n' +
  '1. One-paragraph verdict (nuanced, CEO-brief style).\n' +
  '2. Cross-angle insight — 2-3 SECOND-ORDER findings that only emerge when the angles are read TOGETHER ' +
  '(a constraint in one angle that relieves/worsens another, a value shift one tier up/down), and explicitly ' +
  'FLAG any CONTRADICTIONS between angles. This is the highest-value section — do not skip it or pad it with ' +
  'single-angle restatements.\n' +
  '3. The value chain (downstream → upstream).\n' +
  '4. The analysis by angle (who owns what, where the durable value sits; surface the [contested] / [unverified] flags honestly).\n' +
  '5. Vault connections — consolidate the `## Vault connection:` blocks into ONE section: which existing ' +
  'vault pages the findings CONFIRM / CHALLENGE / EXTEND (MERGE duplicates across lenses — one mention per ' +
  'page, not three), and any candidate NEW pages the findings imply the vault is missing. Do not concatenate.\n' +
  '6. "What to verify at primary sources" — concrete, numbered leads.\n' +
  'Open with a one-line Tier-3 disclaimer (discovery-only, web-sourced, verify before treating as canon). ' +
  'Output ONLY the report markdown — no preamble, no "here is".',
  { label: 'synthesis', phase: 'Synthesize' },
)

log(`done: ${angles.length} angles · ${connections.length}/${CONNECTION_SPECS.length} connections`)
return { topic, report, angles: angles.length, connections: connections.length }
