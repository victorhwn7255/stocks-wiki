# web/ — the public static site

A static website generated from the vault canon (`wiki/*.md`) by a Python generator. Fully
self-contained: self-hosted fonts, **zero external/CDN requests**, deterministic output.

## Build locally
```bash
pip install -r web/requirements.txt
python3 web/build.py            # → web/dist/  (136+ pages, sitemap, robots, 404, favicon)
# open web/dist/index.html
```
`web/dist/` is a build artifact (gitignored) — never commit it; the host rebuilds it.

## What the build produces
- All page types (companies / chokepoints / themes / trackers / relationships / thesis / frameworks)
  + Home + Structure views + `search-index.json`.
- **SEO/production files** (added by `_write_seo` in `build.py`): `sitemap.xml`, `robots.txt`
  (public — allows all crawlers), `404.html`; plus `<head>` meta/OG/canonical and `favicon.svg`.

## Deploy (Vercel)
Config lives in `/vercel.json` at the repo root:
- **Build command:** `pip install -r web/requirements.txt && python3 web/build.py`
- **Output directory:** `web/dist`
- Vercel rebuilds + redeploys on every push to the default branch.

**Setup (one-time):** import the repo in Vercel → it reads `vercel.json` → deploy. Vercel assigns a
`*.vercel.app` URL immediately; add the custom domain in the dashboard when it's ready.

### Base URL (canonical / OG / sitemap)
Absolute URLs need the production domain. Set it as a Vercel **Environment Variable**:
```
SITE_BASE_URL = https://your-domain.com
```
`build.py` reads `SITE_BASE_URL` (→ falls back to `site.yaml: base_url` → root-relative). Until set,
local/preview builds use root-relative SEO, which is correct for a `*.vercel.app` preview.

### Fallback (if Vercel's Python build is finicky)
Build in CI instead: a GitHub Action runs `python3 web/build.py` and deploys `web/dist` to Vercel via
the Vercel CLI/Action. (Not needed for the default path above.)

## Source layout
- `build.py` — the generator (reuses `scripts/vault_parsers.py`).
- `templates/` — Jinja templates (`base.html` is the shell with the `<head>`/meta).
- `assets/` — `style.css`, `app.js`, self-hosted IBM Plex Mono `.woff2`, `favicon.svg`.
- `data/site.yaml` — non-canon presentation data (section copy, tracker metadata, optional `base_url`).
