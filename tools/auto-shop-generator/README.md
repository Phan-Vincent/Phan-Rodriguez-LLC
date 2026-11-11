# Portfolio generator

Run from the repository root:

```
python3 tools/auto-shop-generator/build_flagship.py mockups
```

This supported entry point builds all 46 catalog pages. Optional folder arguments
limit the build, for example `mockups el-rey-retro-roadside`.

- `build_flagship.py` owns the 45 flagship compositions and per-site overrides.
- `build_leads.py` retains shared business data and the maintained layout D renderer
  for El Rey Retro Roadside. The flagship entry point calls that renderer and
  `build_v2.page` for the alternate; do not hand-edit its generated HTML.
- `build_v2.py` supplies the alternate's shared CSS/JS and review helpers.
  The older scripts' standalone build loops remain disabled.
- Keep the existing `fonts/` and `tri_reviews/` assets alongside these scripts.
  Fonts are copied to flagship outputs; images remain the existing stock URLs.
- Edit facts in their owning data definitions. `HOURS_NOTES` records unresolved
  listing differences beside the hours table and marks Today as unconfirmed.
  It is not owner verification. Molina's weekend values intentionally request a call.
- Generated pages retain `noindex`, concept disclaimers, contacts and review sources.

## QA after regeneration

With an existing Playwright installation and the repository served on loopback:

```
node tools/portfolio-qa.test.mjs
node tools/lead-batch-qa.mjs --base http://127.0.0.1:8765/ --out /tmp/portfolio-qa
node tools/mobile-qa.mjs --base http://127.0.0.1:8765/ --out /tmp/portfolio-qa
```

Both runners discover pages from `index.html`. Each creates a unique child directory
under `--out`; historical reports are never overwritten. Defaults are loopback port
8765 and `qa-runs/`. `QA_BASE_URL` and `QA_OUTPUT_DIR` are equivalent defaults.
Set `PLAYWRIGHT_MODULE` to an existing module path if necessary, and optionally
`QA_BROWSER_CHANNEL=chrome` (or another installed Chromium channel).

The portfolio runner covers 305, 320, 390 and 1440px; 305 explicitly exercises
usable width on hosts with overlay scrollbars. The mobile runner also covers
360, 430 and 768px. Checks scroll the full page, inspect element and text bounds,
load HTML/image/CSS-background assets, detect console/page/request errors, validate
anchors, check footer/dock overlap and sticky focus, and sample carousel positions
under initial and dynamically enabled reduced motion. Third-party failures are
reported, not silently waived. Review the JSON and manually inspect keyboard flow,
no-JavaScript/failed-observer rendering, and screenshots in the target browsers.
