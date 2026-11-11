# Lead batch 5 and sheet sync — November 10, 2026

Three more local concepts: Mailo's Auto Repair, Bee Z Auto Care and Quality Auto Complete Auto Repair. The workbook now shows 24 businesses with a mockup and 270 without. Not committed, pushed or sent to a business at the time of writing.

## Google Sheet sync

- **Sheet to workbook (done):** Vincent's Status and Notes entries, 21 cells in rows 2 to 20, were copied into `leads/West_IE_No_Website_Leads.xlsx`. Columns A to H matched on all 294 rows, so rows line up. Nothing else in the workbook changed in that step.
- **Workbook to sheet (not done):** the Google Sheet still has the Nov 9 mockup columns. The Drive connector cannot edit cells and the browser used here opens the sheet view-only (not signed in). `leads/google-sheet-paste-L2.tsv` holds columns L to Q for rows 2 to 295: open it, copy everything, click cell L2 on the Leads tab and paste. Fifteen rows change (13, 14, 15, 16, 17, 19, 23, 24, 25, 32, 33, 36, 37, 46, 50).
- **What the notes say:** rows 5, 7, 10, 11 and 12 are marked not interested (Tri Auto, Moreno's, ROYSAUTOREPAIR, RC Auto concept, Muffler Doctor). Calls are planned for Nov 11 on rows 4 and 13 to 20.

## Why these three

They are on the Nov 11 call list and had no mockup. Still without one on that list: Basic Auto Repair (row 18, address conflict 803 vs 810 E Holt Blvd found earlier) and A Tech Automotive (row 20).

| Business | Sheet row | Sheet status | Layout | Services shown as |
|---|---|---|---|---|
| Mailo's Auto Repair, Fontana | 14 | call again 11/11 | A, split hero | two columns |
| Bee Z Auto Care, Upland | 15 | msg left 11/10, call again 11/11 | E, framed photo | accordion |
| Quality Auto Complete Auto Repair, Rancho Cucamonga | 16 | call 11/11 | D, poster | tabs |

## Research (Google Maps and Yelp, read in a browser Nov 10)

**Mailo's Auto Repair** — Maps: 4.4 / 153, **unclaimed**, 16624 Ceres Ave, Fontana 92335, (909) 427-9202, Mon–Sat 8–6, Sun closed. Topics: mechanics (8), truck (6), honest mechanic (5), trustworthy, affordability, check engine light, spark plug replacement, tow. [Yelp](https://www.yelp.com/biz/mailos-auto-repair-fontana): claimed, 4.0 / 34, **Mon–Sat 7:30–7**, services: oil changes, routine maintenance; highlights mention a radiator and a serpentine belt. A separate Yelp listing, "Mailos auto and towing", exists. **Flags:** hours differ; the page uses Google's shorter hours and says to call. Towing is offered only as "ask about a tow". The owner is named in reviews and in the business name; no other names used.

**Bee Z Auto Care** — Maps: 4.7 / 145, 231 E Arrow Hwy, Upland 91786, (909) 982-4321, Mon–Fri 7:30–5, Sat 7:30–12, Sun closed. Topics: brakes (9), kind staff (9), honest mechanics, efficient work, quotes, no upsell. [Yelp](https://www.yelp.com/biz/bee-z-auto-care-upland-3): claimed, 4.3 / 82, same hours; categories auto repair, transmission repair, oil change stations; owner text says domestic and foreign vehicles; online appointments. **Flags:** one of the three review snippets Google shows is a warning from an unhappy customer; the owner text gives a number of years in business that was cut off and is not used.

**Quality Auto Complete Auto Repair** — Maps: 4.4 / 142, 8160 Masi Dr B, Rancho Cucamonga 91730, (909) 466-1919, Mon–Fri 8–5, Sat 8–2, Sun closed. Topics: smog issues (8), brakes (4), honest guys, clutch. [Yelp](https://www.yelp.com/biz/quality-auto-complete-auto-repair-rancho-cucamonga-2): claimed, 4.1 / 151, same hours; categories auto repair and smog check stations; owner text lists diesel service, exhaust systems, brake repairs, alignments, driveshafts and axles, engine repair, clutch service, manual and automatic transmissions. **Flags:** the headline is about failed smog tests because that is the top review topic; confirm with the owner that smog repair, and not only testing, is something they want to lead with.

No review text is quoted, no staff names are used, no listing photographs were copied.

## Delegation record (Reasonix)

One Reasonix Flash worker through MCP `delegate_write` (`authorize_writes: true`, one file, 900 s limit), task `lead-batch-20261110e-generator-entries`: add the three entries to `SITES` in `build_leads.py` from supervisor-supplied facts and copy, then prove the file parses and builds into a throwaway directory. Ran 58 s, reported cost $0.021, `ok: true`, no permission denials. No retries, no Pro escalation. The worker left out keys the chosen layouts never read (`addr_short`, `bar`, `chips`) and said so.

Supervisor review: `git diff` showed only the three entries and the docstring count. Supervisor rebuilt into `mockups/` (the other 19 lead pages came out byte-identical) and changed one thing after screenshots: Bee Z's accent, which made the hero call button nearly invisible on the photo, from `#4A3F12` to `#8A6A00`.

Photos: six Pexels free-license images (IDs 3807517, 4116221, 6870313, 30470930, 5276374, 8985712), chosen from a contact sheet.

## Verification

Playwright with installed Chrome against `http://127.0.0.1:8765/`, 1440×1000 and 390×844, real photos loading; PNGs in each `screenshots/` folder; results in `browser-results-batch5.json`. All six checks: no horizontal overflow, one h1, no missing images, no page errors, noindex present, correct `tel:` links, zero running animations under reduced motion.

Not checked: keyboard tab order, 1024px width, physical phone, screen reader, Safari or Firefox, workbook opened in desktop Excel (39 cells changed in total: 21 Status/Notes cells and 18 mockup cells in rows 14 to 16, compared programmatically).
