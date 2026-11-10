# UI changes playbook

How we make look-and-feel changes to the concept sites in `mockups/`. The same text is saved as a Claude skill for Andrew; this copy is for anyone on the team.

## Before changing anything

1. `git pull --rebase origin main`. Vincent edits these pages too. Read the latest commits for the page and keep his work.
2. Edit the page's `index.html` directly. `tools/auto-shop-generator/build.py` is out of date for the three auto shop pages.
3. Each site is separate: its own folder, colors, signature element and `fonts/` folder. Never share CSS or scripts between sites.

## House style (set 2026-11-10)

- **Type:** system font stack (`Segoe UI`, system-ui, Helvetica, Arial). Sentence case. Headings 700, body 400, small labels 600 to 700 in capitals.
- **Shape:** 8px cards, 12px large panels, 6px buttons and table rows, pill labels.
- **Depth:** soft, low shadows or a 1.5px hairline border, not both heavy. No paper grain.
- **Color:** gray canvas `#F0F2F5`, white cards, text `#050505`, secondary `#65676B`. Each business keeps its own brand colors, muted, and every text color must reach 4.5:1 on its background.
- **Spacing:** 4px steps. Gaps grow from item to card to section (about 14px, 24px, 96px).
- **Motion:** 175ms for hover feedback, about 400ms for reveals, easing `cubic-bezier(.24,1,.4,1)`. Always include a `prefers-reduced-motion` rule.
- **Not on the pages:** section numbers, A/B/C labels, "Open now" status badges, carousel Pause/Resume buttons or arrows.
- **Reviews:** with four or more quotes, a continuous row that stops while touched, held, hovered or keyboard-focused and resumes on release. With fewer, static rounded cards. Quotes are real, short and name their source.
- **Always on the pages:** `<meta name="robots" content="noindex">`, the concept-site footer note, tap-to-call phone link, directions link, hours table with today highlighted.

## Checks before pushing

1. Screenshot at 1440px and 390px (Playwright). Look for overlap, wrapping and cut-off text.
2. No horizontal scroll, no console errors.
3. Tab through the page: visible focus ring, sensible order.
4. Say plainly what was not checked (for example, photos that would not load in the test environment).

## After pushing

Add a dated note to `DESIGN.md`: what changed, why, what reference was used, what was checked. Update `docs/HANDOFF.md` if business facts changed.
