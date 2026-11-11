# Fact check of 21 built sites — November 10, 2026

This compares the 21 built concept sites that also have a Google Maps record against what Google Maps and Yelp currently say. The three inputs are `docs/handoffs/data/site-facts.json` (what each site says, dumped from the generator), `docs/handoffs/data/google-facts.json` and `docs/handoffs/data/yelp-facts.json` (listings read on November 10, 2026). The listings were read in a browser on November 10 by Vincent's session and the comparison was done by a Reasonix worker from those files. Nothing here was confirmed with an owner, and no site was changed.

## Act on these first

| Site folder | Business | Problem | Site says | Google says | Yelp says | Suggested fix |
|---|---|---|---|---|---|---|
| `the-auto-clinic` | The Auto Clinic | Website exists; the lead was chosen as having none | no website | website: none | theautorepairclinic.com | Open the domain. If it is live and belongs to this shop, drop the lead and the site. |
| `ie-automotive` | I.E Automotive | Website exists | no website | website: none | ieautomotive.com | Same check before the site is pitched. |
| `diamond-auto-center` | Diamond Auto Center | Website exists | no website | website: none | diamondautoc.com | Same check. This one was already flagged in the open-leads handoff. |
| `baja-auto-center` | Baja Auto Center Smog & Lamp | Saturday hours | Sat 8 AM–1 PM | Sat 8 AM–5 PM | no hours listed | Confirm the Saturday closing time, then correct the site or the Google listing. |
| `ceres-collision` | Ceres Collision | Weekday closing time | Mon–Fri 8 AM–5 PM | Mon–Fri 8 AM–4:30 PM | Mon–Fri 8 AM–5 PM | The site and Yelp agree; check whether 4:30 PM on Google is stale and fix that listing. |
| `express-transmissions` | Express Transmissions | Weekday closing time | Mon–Fri 8 AM–6 PM | Mon–Fri 8 AM–5 PM | Mon–Fri 8 AM–6 PM | Site and Yelp agree; verify 6 PM with the shop and correct Google if needed. |
| `l-r-auto-repair` | L & R Auto Repair | Weekday and Saturday hours | Mon–Fri 8 AM–6 PM, Sat 8 AM–4 PM | Mon–Fri 9 AM–5 PM, Sat 10 AM–3 PM | Mon–Fri 8 AM–6 PM, Sat 8 AM–4 PM | Site and Yelp agree; Google looks out of date. Verify and fix Google. |
| `mendiola-diesel-auto` | Mendiola Diesel & Auto | Every day | 8 AM–6 PM all week | Mon–Sun 9 AM–7 PM | 8 AM–6 PM all week | Site and Yelp agree; confirm and correct Google. |
| `molinas-tire-towing` | Molina's Tire & Towing | Monday, Saturday and Sunday | Mon–Fri 8 AM–6 PM, Sat 8 AM–4 PM, Sun closed | Mon 7 AM–6 PM, Tue–Fri 8 AM–6 PM, Sat 8 AM–6 PM, Sun 8 AM–5 PM | Mon–Fri 8 AM–6 PM, Sat 8 AM–6 PM, Sun 8 AM–6 PM | Biggest gap: the site says closed Sunday while both listings show it open. Verify Sunday, Saturday and the Monday 7 AM opening. |
| `rudys-auto-works-paint` | Rudy's Auto Works and Paint | Saturday hours | Sat 9 AM–2 PM | Sat 9 AM–12 PM | Sat 9 AM–2 PM | Site and Yelp agree; correct Google or the site after checking. |
| `auto-technik-carcare` | Auto Technik Carcare | Weekday opening time | Mon–Fri 9:30 AM–6 PM | Mon–Fri 9 AM–6 PM | 9:30 AM–6 PM on the day checked | Confirm 9 or 9:30 AM; Yelp agrees with the site. |
| `diamond-auto-center` | Diamond Auto Center | Sunday hours | Sun 9 AM–2 PM | Closed | Sun 9 AM–2 PM | Two of three say open; verify and fix the Google listing if it is wrong. |

No phone number on any site differs from either listing, and no site address differs from Google in street number, street name, street type, suite, city or ZIP.

### Supervisor follow-up on the three websites

After the worker's report, Vincent's session opened each domain in a browser on Nov 10:

| Domain | What loads | What it means |
|---|---|---|
| theautorepairclinic.com | Browser refuses it: the TLS certificate has expired | The Auto Clinic has a domain and probably an old site, but visitors get a security warning. Keep the lead; this is the pitch |
| ieautomotive.com | A "Coming Soon, under construction" placeholder | I.E Automotive owns the domain and has nothing on it. Keep the lead |
| diamondautoc.com | Browser refuses it: the certificate is for a different address | Diamond Auto Center's domain is misconfigured. Keep the lead |

So none of the three has a working website, and none of the built sites needs to be dropped. Each owner already has a domain, which is worth saying on the call: the new site can go on the address they own.

### How to read the hours rows

Nobody here can edit a shop's Google listing, so "fix Google" in the table means "tell the owner". Until an owner confirms, the safer choice on the site is the shorter of the two sets of hours plus a line telling visitors to call. The one row where the site is clearly wrong on its own is `molinas-tire-towing`: the site says closed Sunday while both Google and Yelp show it open.

The supervisor recomputed the site-versus-Google hours comparison with a separate script and got the same nine sites the worker lists.

## Summary table

| Site folder | Hours vs Google | Google vs Yelp hours | Phone | Address | Google rating on site vs now | Website found | Yelp rating |
|---|---|---|---|---|---|---|---|
| `johns-auto-repair` | match | match | match | match (Yelp omits unit) | 4.6 (93) vs 4.6 (93) | none | 4.5 (92) |
| `ceres-collision` | DIFFERS (Mon–Fri close) | differs (Mon–Fri close) | match | site adds #1 | 4.8 (50) vs 4.8 (50) | none | 4.9 (80) |
| `freddies-auto-repair` | match | match | match | site matches Google; Yelp says St | 4.6 (71) vs 4.6 (72), stale by 1 | none | 4.8 (40) |
| `bates-auto-service` | match | match | match | match | 4.7 (69) vs 4.7 (69) | none | 4.9 (128) |
| `express-transmissions` | DIFFERS (Mon–Fri close) | differs (Mon–Fri close) | match | match | 4.7 (48) vs 4.7 (48) | none | 3.8 (8) |
| `menas-brake-suspension` | match | match | match | site matches Google; Yelp ZIP 91762 | 4.6 (47) vs 4.6 (47) | none | 3.6 (9) |
| `the-auto-clinic` | match | match | match | match | 4.9 (55) vs 4.9 (55) | Yelp: theautorepairclinic.com | 4.9 (64) |
| `l-r-auto-repair` | DIFFERS (Mon–Fri, Sat) | differs (Mon–Fri, Sat) | match | match | 4.4 (72) vs 4.4 (72) | none | 4.5 (24) |
| `baja-auto-center` | DIFFERS (Sat) | Yelp has none | match | match (Yelp omits suite) | 4.5 (70) vs 4.5 (70) | none | 4.4 (24) |
| `ie-automotive` | match | match | match | site matches Yelp; Google omits unit | 4.8 (65) vs 4.8 (65) | Yelp: ieautomotive.com | 4.6 (19) |
| `v-tech-auto-care` | match | match | match | match | 4.7 (50) vs 4.7 (50) | none | 4.6 (73) |
| `japanese-auto-tech` | match | match | match | match | 4.6 (46) vs 4.6 (46) | none | 4.9 (32) |
| `german-and-japanese-auto-pro` | match | match | match | match | 4.9 (60) vs 4.9 (60) | none | 4.9 (59) |
| `mendiola-diesel-auto` | DIFFERS (all week) | differs (all week) | match | match | 4.8 (58) vs 4.8 (58) | none | 4.0 (4) |
| `molinas-tire-towing` | DIFFERS (Mon, Sat, Sun) | differs (Mon, Sun) | match | match | 4.5 (58) vs 4.5 (58) | none | 3.5 (15) |
| `williams-independent-auto` | match | differs (Mon–Fri close, Sat close) | match | match | 4.5 (54) vs 4.5 (54) | none | 3.2 (17) |
| `rudys-auto-works-paint` | DIFFERS (Sat) | differs (Sat close) | match | match | 4.8 (51) vs 4.8 (52), stale by 1 | none | 4.4 (10) |
| `auto-technik-carcare` | DIFFERS (Mon–Fri open) | Yelp not fully read | match | match (Yelp omits suite) | 4.8 (83) vs 4.8 (84), stale by 1 | none | 4.8 (471) |
| `diamond-auto-center` | DIFFERS (Sun) | differs (Sun) | match | match | 4.8 (78) vs 4.8 (78) | Yelp: diamondautoc.com | 4.2 (10) |
| `claremont-auto-care` | match | match | match | site matches Google; Yelp says St | 4.5 (75) vs 4.5 (75) | none | 3.9 (67) |
| `auto-repair-foreign-domestic-vw` | match | match | match | match | 4.3 (94) vs 4.3 (94) | none | 4.1 (91) |

## Per-site notes

### `johns-auto-repair`
- Names differ: site "John's Auto Repair", Google "John's Auto Repair - BMW, Mercedes Benz And Mini Cooper Experts", Yelp "Johns Auto Repair Specialist".
- Yelp address is "16566 Ceres Ave" without Unit 1 and 2; site and Google both carry the unit.
- Hours, phone and rating all match.

### `ceres-collision`
- Hours: site and Yelp close at 5 PM Monday to Friday; Google says 4:30 PM.
- Site address adds suite "#1"; Google and Yelp show no suite.
- Yelp name is "Ceres Auto Body and Paint" against "Ceres Collision" on the site and Google; Yelp's own note says same address and phone.

### `freddies-auto-repair`
- Google review count on the site is 71; Google now shows 72. Stale by 1.
- Yelp address is "915 E Mission St"; site and Google say Blvd.

### `express-transmissions`
- Hours: site and Yelp 8 AM–6 PM Monday to Friday; Google 8 AM–5 PM. Saturday matches at 8 AM–2 PM.
- Yelp name is "Express Transmission" (singular).
- Yelp rating 3.8 against Google 4.7, a drop of 0.9. Pitch risk, though Yelp has only 8 reviews.

### `menas-brake-suspension`
- Yelp rating 3.6 against Google 4.6, a drop of 1.0, from 9 reviews. Pitch risk.
- Yelp ZIP is 91762; site and Google say 91761 for the same Holt Blvd address.
- Yelp name pluralises to "Menas Brakes & Suspensions". Hours match on all three.

### `the-auto-clinic`
- Yelp lists a business website, theautorepairclinic.com. Google lists none and the site shows none. This invalidates the "no website" premise unless the domain is dead.
- Hours, phone, address and Google rating match.

### `l-r-auto-repair`
- Hours: site and Yelp 8 AM–6 PM Monday to Friday and 8 AM–4 PM Saturday; Google 9 AM–5 PM and 10 AM–3 PM.
- Phone, address and rating match.

### `baja-auto-center`
- Hours: site closes Saturday at 1 PM; Google says 5 PM. Yelp lists no hours at all, so only two values to compare.
- Yelp address omits "Ste B", which site and Google both carry.

### `ie-automotive`
- Yelp lists a business website, ieautomotive.com. Google lists none and the site shows none.
- Google address omits "Unit B"; site and Yelp both have it. Hours and rating match.

### `v-tech-auto-care`
- Google name adds "Inc"; site and Yelp say "V Tech Auto Care". Hours, including the split Tuesday and Thursday 3 PM close, match on all three.

### `german-and-japanese-auto-pro`
- Site and Yelp say "German and Japanese Auto Pro"; Google says "German and Japanese Auto Repair". Hours and rating match.

### `mendiola-diesel-auto`
- Hours: site and Yelp 8 AM–6 PM every day including Sunday; Google 9 AM–7 PM every day. Opening and closing differ by an hour at both ends.
- Yelp rating 4.0 against Google 4.8, a drop of 0.8, but only 4 Yelp reviews.

### `molinas-tire-towing`
- Monday: site 8 AM–6 PM, Google 7 AM–6 PM, Yelp 8 AM–6 PM.
- Saturday: site 8 AM–4 PM, Google 8 AM–6 PM, Yelp 8 AM–6 PM.
- Sunday: site closed, Google 8 AM–5 PM, Yelp 8 AM–6 PM. The site is the only one of the three saying closed.
- Yelp rating 3.5 against Google 4.5, a drop of 1.0. Pitch risk.

### `williams-independent-auto`
- Site hours match Google; Yelp differs, closing 5:30 PM Monday to Friday and 3 PM Saturday.
- Yelp name is "Williams Independent Automotive Service" against "Williams Independent Auto Repair & Smog" on site and Google.
- Yelp rating 3.2 against Google 4.5, a drop of 1.3. The largest gap in the set and a pitch risk.

### `rudys-auto-works-paint`
- Saturday: site and Yelp 9 AM–2 PM; Google 9 AM–12 PM.
- Google review count on the site is 51; Google now shows 52. Stale by 1.

### `auto-technik-carcare`
- Weekday opening: site 9:30 AM; Google 9 AM. Yelp, read only for the day checked, says it opens 9:30 AM and closes 6 PM, which matches the site.
- Google review count on the site is 83; Google now shows 84. Stale by 1.
- Yelp shows 471 reviews for this shop against 84 on Google; the site carries only the Google figure.
- Yelp address omits "Suite A and B"; site and Google both carry it.

### `diamond-auto-center`
- Yelp lists a business website, diamondautoc.com. Google lists none and the site shows none.
- Sunday: site and Yelp 9 AM–2 PM; Google says closed.
- Yelp rating 4.2 against Google 4.8, a drop of 0.6. Pitch risk.
- Google name adds "/ Propane"; site and Yelp say "Diamond Auto Center".

### `claremont-auto-care`
- Yelp address is "3624 Lynoak St"; site and Google say Dr.
- Yelp rating 3.9 against Google 4.5, a drop of 0.6. Pitch risk.

### `auto-repair-foreign-domestic-vw`
- Site and Yelp say "Auto Repair Foreign Domestic & VW"; Google drops "& VW". Hours, phone, address and rating match.

Clean against all three sources, with no notes: `bates-auto-service` and `japanese-auto-tech`.

## Method and limits

- Sources: `docs/handoffs/data/site-facts.json`, `docs/handoffs/data/google-facts.json` and `docs/handoffs/data/yelp-facts.json`, all dated November 10, 2026. The Google and Yelp files were read from the live listings in a browser that day; the site values come from the generator's dump.
- `site-facts.json` has no `_note` key, so there was no dump-specific caveat to apply. It holds 45 sites; the 21 that also appear in the Google file were checked.
- Wednesday November 11 is Veterans Day. Google flagged that day's row as "hours might differ" on every listing, and in every case it matched the other weekdays, so it is not reported as a separate difference.
- Google ownership is only known where the listing showed "Claim this business". That was the case for `freddies-auto-repair`, `express-transmissions`, `menas-brake-suspension` and `molinas-tire-towing`; for the other 17, claimed status is unknown. Yelp has a claimed flag on each page but it was not part of this comparison.
- Yelp hours for `auto-technik-carcare` were not fully read: the page showed only the day checked (opens 9:30 AM, closes 6 PM), so no week-long Google-to-Yelp comparison is possible there.
- `baja-auto-center` has no hours on Yelp, so its Google-to-Yelp column says "Yelp has none".
- Times were normalised before comparing ("8:00 AM – 5:00 PM" equals "8 AM - 5 PM"); address and name comparisons ignore punctuation and Ste/Suite/Unit/# spelling.
- The comparison used the generator's data, not a rendering of each built page. No site, listing or file under `mockups/` or `tools/` was changed, and no owner was contacted.
