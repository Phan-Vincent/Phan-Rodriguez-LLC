# Lead batch — November 10, 2026

Three new local concepts: 43's Mufflers & Brakes, Sinaloa Tires and With Pride Auto Air Conditioning. The workbook now shows 12 businesses with a mockup (13 concepts; El Rey has two) and 282 without. Nothing was committed, pushed, deployed or sent to a business. The connected Google Sheet was not edited in this batch; only `leads/West_IE_No_Website_Leads.xlsx`.

## Why these three

They were the easiest remaining High-priority leads: narrow service scope, phone-only conversion, and Google and Yelp agree on address, phone and hours. All three Yelp profiles are claimed by the owner, which also means someone there manages listings.

| Order | Business | Sheet row | Effort | Notes |
|---|---|---|---|---|
| 4 | 43's Mufflers & Brakes | 19 | Low | Hand-painted sign gives the identity for free. |
| 5 | Sinaloa Tires | 13 | Low | Seven-day hours, used tires, "in the back" wayfinding. |
| 10 | With Pride Auto Air Conditioning | 25 | Low–medium | Single specialty; owner's own description supplies the story. |

Next easiest, not yet researched: king tire shop (row 17), Basic Auto Repair (18), Bee Z Auto Care (15), Performance Lube & Oil (32), J C Auto Electric (36). ROYSAUTOREPAIR (10) needs its brand spelling confirmed first.

## Research (Google Maps and Yelp, read in a browser Nov 10)

Unlike Nov 9, Yelp pages loaded and were read directly.

**43's Mufflers & Brakes** — Maps: 4.5 / 105, 1717 and 1709 W Holt Ave, Pomona 91768, (909) 868-1997, Mon–Fri 9:30–5:30, Sat 9:30–1:30, Sun closed. Review topics: welds, muffler swap, knowledgeable and kind staff. Photos: black hand-painted sign with yellow "43's", white slanted MUFFLERS and the phone number; cream block building, rust-red door; a sixties Chevrolet on the lift. [Yelp](https://www.yelp.com/biz/43s-muffler-and-brakes-pomona): claimed, 4.8 / 98, same hours, "1717 W Holt Ave Ste 1709"; owner text lists exhaust systems, catalytic converters, mufflers, tow hitches, general welding, complete auto service. Yelp also lists a separate 43's in Whittier. BBB grades seen in search results are inconsistent and unused.

**Sinaloa Tires** — Maps: 4.3 / 161, 1542 S Garey Ave, Pomona 91766, (909) 620-1199, Mon–Fri 8–7, Sat 8–6, Sun 8–3. Topics: cash only, flat tire repair, used tires, brakes. A reviewer notes the shop is in the back and hard to see from the street. Photos: orange "used tires" feather flag with checkered tail, white building, blue sky. [Yelp](https://www.yelp.com/biz/sinaloa-tires-pomona-2): claimed, 3.6 / 31, same hours; owner text: tires to engine swaps, free air, free check-engine scan, used tires. **Flags for the pitch:** Google reviewers say cash or Zelle only while Yelp says cards accepted; two April 2026 Yelp reviews allege an odometer problem on a used car bought there. The mockup mentions neither car sales nor the Yelp rating.

**With Pride Auto Air Conditioning** — Maps: 4.7 / 97, 5438 Holt Blvd Unit F3, Montclair 91763, (909) 391-4894, Mon–Fri 8–5, Sat 9–3, Sun closed. Topics: leak repair, A/C compressor repair, fair pricing, no upselling; classic-car owners. Photos: red arched building with a white chevron mark. A Google post on the listing says 45+ years and price match with a written estimate. [Yelp](https://www.yelp.com/biz/with-pride-auto-air-conditioning-montclair): claimed, 4.4 / 95, same hours; owner text says over 40 years, Eddie and Elaine, family business. Reviews are mixed, including one detailed complaint. The mockup says "more than 40 years … according to the shop" and omits price match and warranty.

No review text is quoted on any page; no listing photographs were copied; all drawings are CSS or inline SVG.

## Delegation record (Reasonix)

- `lead-batch-20261110-sinaloa`: MCP `delegate_write`, Flash tier, `authorize_writes: true`, scope limited to `mockups/sinaloa-tires/index.html`. Ran 372 s, reported cost about $0.05. The engine returned `ok: false` / `INVALID_RESULT` (worker verdict "blocked") even though the worker's message said the file was written. Process group stopped, pipes drained. No retry or Pro escalation.
- Supervisor review: `git status` showed no files outside scope; the file was read, checked for banned content, rendered and accepted as a partial result. Supervisor then rebuilt the feather flag (it was about half height) and reduced its sway.
- Supervisor wrote all three DESIGN.md files, the 43's and With Pride pages, workbook, gallery, README and this file directly. A second delegation was not run because the first took over six minutes.

## Verification

Served at `http://127.0.0.1:8765/`, Playwright with installed Chrome, 1440×1000 and 390×844, full-page and first-screen PNGs in each `screenshots/` folder; results in `browser-results.json`. All six checks: no horizontal overflow, one h1, no broken fragment links, no unnamed links, no page errors, noindex present, zero running animations under reduced motion. With Pride was also captured at the hot and mid slider positions, and the slider's keyboard control and `aria-valuetext` were exercised.

Changes made after looking at screenshots:

- 43's: block-wall joints now stagger like real block; sign lettering enlarged on phones; phone number kept on one line.
- Sinaloa: flag redrawn to run most of the viewport height with larger lettering.
- With Pride: vent given a bezel and shaded louvres; airflow lines moved out of the vent face and shortened so they never cross text; phone header button no longer wraps.

Not done: testing on a physical phone, a screen reader pass, colour-contrast tooling beyond the ratios computed in each DESIGN.md, Excel desktop open of the workbook (cell values and styles were compared programmatically: 15 cells changed, all in rows 13, 19 and 25).
