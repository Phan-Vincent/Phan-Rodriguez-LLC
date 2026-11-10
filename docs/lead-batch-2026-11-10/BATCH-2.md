# Lead batch 2 — November 10, 2026

Three more local concepts: King Tire Shop, J C Auto Electric and Performance Lube & Oil. The workbook now shows 15 businesses with a mockup and 279 without. Not committed, pushed or sent to a business at the time of writing. The connected Google Sheet was not edited; only `leads/West_IE_No_Website_Leads.xlsx`.

## Why these three

Next on the Nov 9 build order with a narrow, clear offer and Google and Yelp in agreement on address and phone. Basic Auto Repair (row 18) was skipped: directories disagree on 803 vs 810 E Holt Blvd. Bee Z Auto Care (row 15) is a general shop and needs more service discovery.

| Business | Sheet row | Effort | Concept |
|---|---|---|---|
| King Tire Shop, Montclair | 17 | Low | Till nine |
| J C Auto Electric, Montclair | 36 | Low–medium | Find the fuse |
| Performance Lube & Oil, Chino | 32 | Low | Oil in, car washed |

## Research (Google Maps and Yelp, read in a browser Nov 10)

**King Tire Shop** — Maps: 4.5 / 135, 8939 Rose Ave, Montclair 91763, (909) 952-9219, Mon–Sat 9 AM–9 PM, Sun closed. Topics: flat tire repair, air valve repair, budget friendly, clean place. Photo: red block-letter sign on a tan stucco parapet, yellow A-frame "flat tire repair" boards. [Yelp](https://www.yelp.com/biz/king-tire-shop-montclair): claimed, 4.3 / 59, same hours; manager's text: alignment, oil change, brakes, new and used tires; accepts cards. **Flags:** one Google reviewer says "open 24 hours", one Yelp reviewer describes a Sunday visit, Birdeye shows 9–8 and "established 2011 … Pomona". A recent Google review complains about tire quality; the owner replied.

**J C Auto Electric** — Maps: 4.7 / 83, category "auto electrical service", **unclaimed**, 10640 Ramona Ave, Montclair 91763, (909) 625-9181, Mon–Sat 8–5:30, Sun closed. Topics: honest mechanic, friendly staff. [Yelp](https://www.yelp.com/biz/jc-auto-electric-montclair): **unclaimed**, 4.2 / 12, Mon–Fri 8–5:30, Sat 8–4. Reviewers say the shop does general repair and A/C, not alignments. **Flags:** Saturday closing differs; one 2022 Yelp review is a serious complaint about a transmission job; neither listing is claimed, so nobody there may be managing listings. The eight symptom read-outs on the page are generic draft copy, labelled as such in the footer.

**Performance Lube & Oil** — Maps: 4.3 / 87, "Located in: Chevron ExtraMile", 5288 Riverside Dr, Chino 91710, (909) 364-1197, every day 8–5. "Free car wash" is the top review topic (27 mentions). [Yelp](https://www.yelp.com/biz/performance-lube-and-oil-chino-2): claimed, 4.2 / 129, oil change station and car wash, same hours; manager's text lists oil changes, transmission fluid, coolant flushes, tune-ups, brakes, belts and a free complete car wash with every service. **Flags:** recent reviews on both sites complain about being rushed into extra services and, once, about oil quantity. The page promises no speed, price or "no upsell".

Wednesday Nov 11 is Veterans Day; Google's Wednesday rows were labelled as holiday hours and were not read separately.

No review text is quoted, no staff names are used, no listing photographs were copied.

## Delegation record (Reasonix)

All three pages were written by Reasonix Flash workers through MCP `delegate_write` (`authorize_writes: true`, one file each, 900 s limit). Supervisor wrote the DESIGN.md files and contracts first.

| Task ID | Run time | Reported cost | Engine result |
|---|---|---|---|
| `lead-batch-20261110b-king-tire` | 458 s | $0.064 | `ok: false`, `INVALID_RESULT`, verdict "blocked" |
| `lead-batch-20261110b-jc-auto-electric` | 483 s | $0.066 | same |
| `lead-batch-20261110b-performance-lube` | 371 s | $0.049 | same |

Each worker's own message said its file was written; each run also logged one denied `browser_act` call. No retries, no Pro escalation. `git status` showed only the three new folders. Each file was scanned for banned content and rendered before acceptance.

Supervisor changes after screenshots:

- King: sandwich board enlarged and moved between the name and the buttons (it first covered them), larger name on mobile, shorter stucco band on mobile.
- J C: hours and find-us share a row on desktop to remove dead space.
- Performance Lube: worker capped the headline at 68px; changed to a staggered headline up to 112px, larger hero buttons.

## Verification

Playwright with installed Chrome against `http://127.0.0.1:8765/`, 1440×1000 and 390×844; PNGs in each `screenshots/` folder; results in `browser-results-batch2.json`. All six checks: no horizontal overflow, one h1, no page errors, noindex present, correct `tel:` links, zero running animations under reduced motion. Also loaded at 1024×768 (no overflow, looked at King and Performance Lube). J C: clicking the fourth fuse left exactly one pressed fuse and swapped the read-out.

Not checked: physical phone, screen reader, Safari or Firefox, keyboard walk-through beyond the fuse click, the pages with JavaScript disabled, workbook opened in desktop Excel.

## House style note

`docs/design-system/ui-changes-playbook.md` (added Nov 10) says no "Open now" badges and no section numbers. These three pages follow that. The six earlier lead-batch pages still show an open/closed line, and none of the lead-batch pages use the playbook's system font stack or gray-card look, because the brief for these was a distinct identity per shop.
