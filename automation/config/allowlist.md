# automation/config/allowlist.md — the locked tool allow-list

The enforcement layer of the `automation/README.md` contract. Any **headless** run the
automation launches (`claude -p` / Agent SDK) is constrained to this tool set. The
restriction is what makes unattended runs safe — **do not loosen it.**

## Allowed (read + write-to-automation only)
```
Read, Grep, Glob, Bash(python3 scripts/*), Write
```
- `Read / Grep / Glob` — read canon + scan (no mutation).
- `Bash(python3 scripts/*)` — run the deterministic scanners only.
- `Write` — used ONLY to write inside `automation/` (the prompts instruct this; the path
  discipline is reinforced in every prompt and in the runner instruction).

## Disallowed (hard)
```
Edit, MultiEdit, NotebookEdit
```
No in-place editing of any existing file — which means **canon (`wiki/`, `index.md`,
`log.md`, `_thesis*`, `frameworks*`, `CLAUDE.md`) cannot be mutated**, even by accident.
A headless run that tries to edit a wiki page is blocked by the harness, not just by
convention.

## Reflected in code
`automation/scripts/run.py` sets:
```python
ALLOWED_TOOLS    = "Read,Grep,Glob,Bash(python3 scripts/*),Write"
DISALLOWED_TOOLS = "Edit,MultiEdit,NotebookEdit"
```
and passes them via `--allowedTools` / `--disallowedTools` to every `claude -p` it builds.

## Note on the two canon-writing skills
`latest-alpha` (on-page digest block) and `spread-watch` (tracker + index) write to canon
by design. They are therefore **never run headlessly** under this allow-list:
- `spread-watch` stays **interactive** (Vic runs it); the automation uses only its
  underlying `spread_watch.py` data pull for the digest and flags "tracker needs update".
- `latest-alpha` headless = **note-only mode** (skip the on-page block; write only the
  `raw/notes/latest-alpha/` note) — see its SKILL.md.
