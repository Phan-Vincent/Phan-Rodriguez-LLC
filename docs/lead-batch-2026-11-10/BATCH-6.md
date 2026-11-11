# Lead batch 6 — November 10, 2026 (night)

Two new sites for the last two businesses on the Nov 11 call list that had none. Built by `tools/auto-shop-generator/build_flagship.py`.

## Basic Auto Repair, Ontario (sheet row 18, "call 11/11")

- **Google Maps, read in a browser Nov 10:** 803 E Holt Blvd, Ontario, CA 91764 · (909) 984-8011 · 4.8 / 115 · Mon–Fri 8–5, Sat 8–1, Sun closed · listing is unclaimed. Review topics: honest mechanic (7), battery, radiator repair, starter replacement. A review summary line reads "New location, same great service."
- **Address conflict settled:** MapQuest, Superpages, Birdeye and BBB still show 810 E Holt Blvd. Google shows 803, and a Yelp review says "Correct address is 803 E. Holt Blvd." The site uses 803 and tells visitors older listings show 810. **Ask the owner to confirm on the call.**
- **Services** come from the business's own directory text (MapQuest/Superpages): full-service auto repair, smog inspection, brake repair, tune-ups, routine maintenance, belt replacement, emission testing, serving Ontario since 1995.
- **Reviews on the site:** three Yelp reviews, each linked by its own id (Angie G., Raena S., Stephanie W.). One available review named a staff member and was not used.

## A Tech Automotive, Chino (sheet row 20, "msg left, call 11/11")

- **Google Maps, read in a browser Nov 10:** 12365 Central Ave Unit A, Chino, CA 91710 · (909) 590-0123 · 4.5 / 104 · Mon–Fri 8–5, Sat 8–3, Sun closed. Review topics: professional team, kind staff, repair time, oil change. Birdeye shows a different address (12512 Central Ave); the site uses Google's.
- **Thin on services.** No owner-written service list was found, so the site lists only oil changes, maintenance and repairs, worded from review topics. **Ask the owner for the real list.**
- **Reviews on the site:** two short Google review-summary lines that link to the Google listing. No per-review links found. Staff names in reviews were not used.

## Not done

Photos are stock (Pexels ids already used elsewhere in the repo). Neither live page has been viewed with photos and the map loaded. Hours on Veterans Day (Nov 11) may differ; Google flags it.

## Added from Vincent's session (same night)

Vincent's session researched the same two shops in parallel and built its own pages for them with the older generator. Those duplicates were dropped in favour of the flagship pages above. What that research adds:

- **A Tech Automotive has a claimed Yelp page** with a service list, which answers the "thin on services" note: [yelp.com/biz/a-tech-automotive-chino-3](https://www.yelp.com/biz/a-tech-automotive-chino-3), 4.5 / 118, categories auto repair, tires and transmission repair; services listed include brakes, engine repair, exhaust, battery and electrical, fluids and filters (21 more behind "See more"). Yelp hours are Mon–Fri 8–6, Sat 8–4, later than Google's. The live page was not changed; this is for the call and for a later edit.
- **Basic Auto Repair on Yelp:** [unclaimed](https://www.yelp.com/biz/basic-auto-repair-ontario), 4.5 / 36, same hours as Google, still at 810 E Holt; categories include smog check stations; listing text adds alternators, water pumps and electrical wiring.
- **Purrfect Auto Services** was skipped for the same reason (Yelp shows four locations).

## Prime Truck and Trailer Repair, Fontana (sheet row 22)

Batch 7's notes skipped this one for lack of a listing. Its Google Maps listing does load and was read in a browser on Nov 10: truck repair shop, 9978 Cherry Ave, Fontana 92335, (909) 644-3029, 4.4 / 102, Mon–Fri 8:30–6, Sat 8:30–3:30, Sun closed. Review topics: quality of work (6), trailer repair (4), alignment (4), suspension work, engine rebuild, customer supplied parts, owner operator friendly.

- **Built** as `prime-truck-trailer-repair` in `build_flagship.py` (photo hero, services as rows). No review quotes or staff names.
- **Google only.** No matching Yelp page; the nearest result, Prime Diesel Repair at 10025 Hemlock Ave, has different hours and was treated as a different business. Confirm hours and services on the call.
- **Photos:** Pexels 6720519 and 7019376, free license.
- **Checked:** Playwright at 1440px and 390px with photos loading: no horizontal overflow, no script errors, one h1, no missing images, no motion under reduced-motion. Not checked: keyboard tab order, the embedded map, other browsers.
- **Lead workbook:** rows 18, 20 and 22 are now marked as having a mockup (27 Yes, 267 No; Tri Auto, Moreno's and Muffler Doctor are still marked Yes although their sites were removed). `leads/google-sheet-paste-L2.tsv` carries the same columns for pasting into the Google Sheet.
