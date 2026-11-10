# Lead batch 3 — November 10, 2026

Three more local concepts: Toy Shop Transmissions, Diesel Injection Service and JC Bumper Repair & Auto Body. The workbook now shows 18 businesses with a mockup and 276 without. Not committed, pushed or sent to a business at the time of writing. The connected Google Sheet was not edited; only `leads/West_IE_No_Website_Leads.xlsx`.

## Why these three

Each has one narrow specialty in its name, which makes the page short and the identity obvious, and each differs from the tire, muffler and oil shops already built. Considered and left for later: Hock's Japanese Car Specialists (row 50, general repair, needs service discovery) and County Brake, Alignment & Mufflers Plus (row 23, close in subject to 43's and Muffler Doctor).

| Business | Sheet row | Effort | Concept |
|---|---|---|---|
| Toy Shop Transmissions, Pomona | 46 | Low | Back in drive |
| Diesel Injection Service, Fontana | 37 | Low–medium | Bring the part or bring the truck |
| JC Bumper Repair & Auto Body, Fontana | 24 | Low–medium | Slide to fix |

## Research (Google Maps and Yelp, read in a browser Nov 10)

**Toy Shop Transmissions** — Maps: 4.9 / 67, transmission shop, **unclaimed**, 1292 E 3rd St, Pomona 91766, (909) 620-5849, Mon, Tue, Thu, Fri 9–6, Sat and Sun closed (Wednesday row not readable, see below). Topics: knowledgeable staff (13), hot rods (5), honesty, transparency. [Yelp](https://www.yelp.com/biz/toy-shop-transmissions-pomona): **unclaimed**, 4.9 / 36, no hours listed, services: transmission repair, leak inspection. Reviews describe full rebuilds, a rear differential rebuild and hard-to-find parts for older vehicles. **Flags:** nobody manages either listing; no second source for hours.

**Diesel Injection Service** — Maps: 4.9 / 83, diesel engine repair service, 8482 Cherry Ave, Fontana 92335, (909) 885-0590, Mon–Fri 7–5, weekends closed. Topics: injector replacement (12), turbo repair, timely repairs. [Yelp](https://www.yelp.com/biz/diesel-injection-service-fontana): claimed, 4.6 / 39, same hours; manager's text: diesel fuel injection systems, rebuild and test pumps and injectors, turbochargers, maintenance and diagnostics for fleets and consumers. **Flags:** "Since 1951" rests on an [Alliant Power partner page](https://alliantpower.com/diesel-injection-service/) and one reviewer's "75 years"; a [Banks Power article](https://official.bankspower.com/?p=22080) gives a Colton address and a [MapQuest listing](https://startpage.mapquest.com/us/california/diesel-injection-service-634597303) shows Fontana as closed, while Google and Yelp show it open with 2026 reviews. A business this old may have a website the Google listing does not link; a web search found none.

**JC Bumper Repair & Auto Body** — Maps: 4.7 / 98, auto body shop, **unclaimed**, 16620 Ceres Ave, Fontana 92335, (909) 349-0343, Mon–Fri 9–5:30, Sat 10–2. Topics: bumper repair (17), affordability, crack repair. [Yelp](https://www.yelp.com/biz/jc-bumper-repair-and-auto-body-fontana): claimed, updated two weeks ago, 4.9 / 32, **Ste 6**, Mon–Fri 9–5, Sat 10:30–2; services verified by the business: bumper repair, collision repair, dent removal, chrome delete, auto body restoration. **Flags:** hours differ (the page uses Yelp's and says to call); a few one-star reviews on both sites, including a 2026 door-alignment complaint; a directory places another body shop at the same street number (#5), and row 11 of the sheet (RC Auto concept) is that neighbour.

Wednesday Nov 11 is Veterans Day; Google's Wednesday rows were labelled as holiday hours. For Toy Shop the row could not be read and is assumed to match the other weekdays.

No review text is quoted, no staff names are used, no listing photographs were copied.

## Delegation record (Reasonix)

All three pages were written by Reasonix Flash workers through MCP `delegate_write` (`authorize_writes: true`, one file each, 900 s limit). Supervisor wrote the DESIGN.md files and contracts first. Unlike the earlier batches, the contracts told workers not to use browser tools, and all three runs returned `ok: true` with no permission denials.

| Task ID | Run time | Reported cost | Engine result |
|---|---|---|---|
| `lead-batch-20261110c-toy-shop` | 155 s | $0.021 | success, verdict "partial" |
| `lead-batch-20261110c-diesel-injection` | 168 s | $0.022 | success, verdict "partial" |
| `lead-batch-20261110c-jc-bumper` | 130 s | $0.017 | success, verdict "complete" |

No retries, no Pro escalation. `git status` showed only the three new folders. Each file was scanned for banned content and rendered before acceptance.

Supervisor changes after screenshots:

- Toy Shop: the worker used one class name for both the needle and the mobile call bar, which hid the needle's stem. Needle rebuilt as a single arrow under D and enlarged.
- JC Bumper: the bumper drawing was a plain rounded bar. Redrawn with wrapped ends, step pad, plate recess, reflectors and exhaust cut-out; the damaged layer now has the hanging corner split at the crack, and is clipped so nothing of it shows past the slider.
- Diesel Injection: accepted as written.

## Verification

Playwright with installed Chrome against `http://127.0.0.1:8765/`, 1440×1000 and 390×844; PNGs in each `screenshots/` folder; results in `browser-results-batch3.json`. All six checks: no horizontal overflow, one h1, no page errors, noindex present, correct `tel:` links, zero running animations under reduced motion. Also loaded at 1024×768 (no overflow). JC Bumper: ten right-arrow presses on the focused slider moved the repair line from 35% to 45%, and at 100% only the repaired bumper shows.

Not checked: physical phone, touch-dragging the slider, screen reader, Safari or Firefox, the pages with JavaScript disabled, workbook opened in desktop Excel (18 cells changed, all in rows 24, 37 and 46, compared programmatically).
