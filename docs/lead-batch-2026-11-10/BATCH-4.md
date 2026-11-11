# Lead batch 4 — November 10, 2026

Three more local concepts: County Brake, Alignment & Mufflers Plus, Hock's Japanese Car Specialists and J & S Auto Center & Smog. The workbook now shows 21 businesses with a mockup and 273 without. Not committed, pushed or sent to a business at the time of writing. The connected Google Sheet was not edited; only `leads/West_IE_No_Website_Leads.xlsx`.

## What changed in how these are built

Before this batch, three commits from Andrew's session rebuilt every lead site, including the nine hand-designed pages from batches 1 to 3, in the shared house style, generated from `tools/auto-shop-generator/build_leads.py` with stock photos. The per-shop identities (shift indicator, fuse box, bumper slider and so on) are no longer on the live pages; their `DESIGN.md` files and old screenshots remain in each folder and no longer match the pages.

This batch follows the repo as it now stands: the three sites are entries in `build_leads.py`, not hand-built pages, and have no per-site `DESIGN.md`. A note was added to the root `DESIGN.md`, as the playbook asks.

| Business | Sheet row | Layout | Services shown as |
|---|---|---|---|
| County Brake, Alignment & Mufflers Plus, Montclair | 23 | B, photo banner with info bar | grouped list |
| Hock's Japanese Car Specialists, Pomona | 50 | C, profile with sticky shop card | list |
| J & S Auto Center & Smog, Fontana | 33 | F, service desk with at-a-glance card | tiles |

## Research (Google Maps and Yelp, read in a browser Nov 10)

**County Brake, Alignment & Mufflers Plus** — Maps: 4.7 / 101, wheel alignment service, **unclaimed**, 10602 Ramona Ave, Montclair 91763, (909) 482-0594, Mon–Fri 8–5, Sat 8–4, Sun closed. Topics: brakes (5), polite staff, family owned, pickup truck repair. [Yelp](https://www.yelp.com/biz/county-brake-and-alignment-plus-mufflers-montclair): **unclaimed**, 4.1 / 28, no hours, services: tire rotation, wheel alignment; the name is ordered differently there. **Flags:** nobody manages either listing; the Yelp rating is noticeably lower than Google's; two doors from J C Auto Electric (10640 Ramona Ave).

**Hock's Japanese Car Specialists** — Maps: 4.7 / 64, 45 Rio Rancho Rd Ste 2b, Pomona 91766, in the Rio Rancho Towne Center, (909) 620-9761, Tue–Fri 8–5, Sat 8–4, Sun and Mon closed. Topics: honesty (6), communication, Prius. [Yelp](https://www.yelp.com/biz/hocks-japanese-car-specialists-pomona): claimed, 4.6 / 106, same hours; services verified by the business include brakes, engine repair, fluids and filters, HVAC, battery and electrical; owner text says family owned and operated, serving for over 15 years; online appointments. **Flags:** the most recent Google review shown is a complaint about not being called back; which makes are covered is not stated anywhere, so the page says "Japanese makes" and names none; "over 15 years" was not used.

**J & S Auto Center & Smog** — Maps: 4.9 / 85, 8807 Sierra Ave, Fontana 92335, (909) 822-3055, Mon–Sat 8–5, Sun closed, closed on Veterans Day. Topics: auto maintenance (6), honest mechanics (5), smog check (4), oil change (4), check engine light. [Yelp](https://www.yelp.com/biz/j-and-s-auto-center-fontana-2): claimed, 4.4 / 25, same hours; categories auto repair **and used car dealers**; owner text says 30 years in business and that fluids are checked on every visit. **Flags:** the used-car side is not on the page; ask the owner whether it should be. "30 years" is attributed to the owner's Yelp profile on the page.

No review text is quoted, no staff names are used, no listing photographs were copied.

## Delegation record (Reasonix)

One Reasonix Flash worker through MCP `delegate_write` (`authorize_writes: true`, one file, 900 s limit), task `lead-batch-20261110d-generator-entries`: add the three entries to `SITES` in `build_leads.py` from supervisor-supplied facts and copy, then prove the file parses and builds into a throwaway directory. Ran 56 s, reported cost $0.019, `ok: true`, verdict "complete", no permission denials. No retries, no Pro escalation.

Supervisor review: `git diff` showed 36 added lines and the docstring count, nothing else; the three entries were read against the contract. Supervisor then rebuilt into `mockups/` (the other 16 lead pages came out byte-identical) and made two changes to the J & S entry after looking at screenshots: replaced a hero photo that showed a car-maker's badge, and merged two services so the tiles fill two rows.

Photos: six Pexels free-license images (IDs 6870319, 20408753, 8478259, 8478228, 33814734, 37177070), chosen from a contact sheet and loaded by URL like the rest of the generator's photos.

## Verification

Playwright with installed Chrome against `http://127.0.0.1:8765/`, 1440×1000 and 390×844, real photos loading; PNGs in each `screenshots/` folder; results in `browser-results-batch4.json`. All six checks: no horizontal overflow, one h1, no missing images, no page errors, noindex present, correct `tel:` links, zero running animations under reduced motion.

Not checked: keyboard tab order (the playbook asks for it), 1024px width, physical phone, screen reader, Safari or Firefox, workbook opened in desktop Excel (18 cells changed, all in rows 23, 33 and 50, compared programmatically).
