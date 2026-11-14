# Lead research handoff 1 — rows 27 to 39

For Andrew. Written Nov 10, 2026 from Vincent's session.

**Status when this was finished:** while this was being researched, Andrew's session pushed batches 8 to 10 (19 more sites). Four of the eight leads below already have a site, so for those this file is a fact check, not a brief:

| Row | Business | State in repo | What to do with this file |
|---|---|---|---|
| 38 | Diamond Auto Center | built (`diamond-auto-center`) | **Yelp lists a website, diamondautoc.com.** Open it; if it is live, drop the site and the lead |
| 35 | Auto Technik Carcare | built (`auto-technik-carcare`) | Check the MapQuest Website button; compare hours and the 471-review Yelp figure |
| 27 | Auto Repair Foreign Domestic | built (`auto-repair-foreign-domestic-vw`) | Compare hours, ratings and the newest-review flag |
| 39 | Claremont Auto Care | built (`claremont-auto-care`) | It is in Pomona; Yelp rating is 3.9 |
| 31 | Jujubuilt Engineered Performance | not built | Brief below |
| 29 | A-1 Auto Expert | not built | Brief below |
| 34 | 2Man Moving Services | not built | Brief below |
| 30 | Star Hi-Tech Auto | not built | Brief below, low priority |

The built pages were not compared line by line against these notes.

**Division of work from here:** Vincent's session researches leads and writes these handoffs. Andrew's session builds the sites in `tools/auto-shop-generator/build_flagship.py`. Vincent's session will not add or edit anything under `mockups/` or in the generators unless asked.

**How this was gathered:** each Google Maps listing and each Yelp page was opened in a browser on Nov 10, 2026. Hours, ratings, review counts and review topics are copied from those pages. "Topics" are Google's review-topic chips with their mention counts. Nothing here was confirmed with an owner. Wednesday Nov 11 is Veterans Day and Google marks that day's hours as possibly different.

**Not included:** linkable Yelp review ids (Andrew's session reads those from MapQuest) and photos.

## Triage

| Row | Business | Verdict | Why |
|---|---|---|---|
| 31 | Jujubuilt Engineered Performance | Build first | 4.9 on both sites, clear niche (Honda and Acura performance), open till 11 PM, no website found |
| 35 | Auto Technik Carcare | Check for a website, then build | 471 Yelp reviews and AAA approved; MapQuest shows a Website button that was not followed |
| 29 | A-1 Auto Expert | Check for a website, then build | Same MapQuest Website button; Google and Yelp list none |
| 27 | Auto Repair Foreign Domestic | Build | Claimed on Yelp, VW work is the angle, hours agree |
| 39 | Claremont Auto Care | Build | Hours agree; Yelp rating is lower than Google's |
| 34 | 2Man Moving Services | Build, needs different treatment | Not an auto shop; phone numbers differ; address looks residential |
| 30 | Star Hi-Tech Auto | Low priority | Google 4.4 but Yelp 2.6 from 32 reviews, Yelp unclaimed |
| 38 | Diamond Auto Center / Propane | Skip | Yelp lists a website, diamondautoc.com |

Already skipped by Andrew, agreed: Purrfect Auto Services (row 21, chain) and Ontario Mills Tire Pros (row 26, dealer network; not researched here).

---

## Row 31 — Jujubuilt Engineered Performance (Upland)

| | Google Maps | Yelp |
|---|---|---|
| Name | Jujubuilt Engineered Performance | Juju Built Engineered Performance |
| Rating | 4.9 from 88 | 4.9 from 78, claimed |
| Address | 1133 W 9th St, Upland, CA 91786, in Mountain Avenue Business Park | same |
| Phone | (661) 492-4309 | same |
| Hours | Mon–Fri 11 AM–11 PM, Sat and Sun closed | none listed |
| Category | Auto repair shop | Auto Repair, Auto Customization |
| Website | none | none |

- **Google topics:** fair pricing (6), quality work (5), pre-purchase exam (3), head gasket job (2), faster turnarounds (2), late hours (2), OEM parts (2), diagnostics (2).
- **Yelp services:** engine repair, oil changes, routine maintenance, electronics installation.
- **Owner's Yelp text:** automotive repair and diagnostics, also performance upgrades and modifications.
- **Yelp review highlights mention:** Honda and Acura Type R and Si owners, a clutch job on a 350Z, a 1993 Acura with fluid seals and suspension parts.
- **Angle:** the Honda and Acura performance shop that is open until 11 at night. Pre-purchase inspections are a second hook.
- **Flags:** the 661 area code is not local, so it is probably a mobile number. A shop like this likely runs on Instagram; not checked. Weekend closure and the 11 AM start are unusual, so confirm hours.
- **Yelp page:** https://www.yelp.com/biz/juju-built-engineered-performance-upland

```python
short="Jujubuilt Engineered Performance", kicker="Repair and performance · W 9th St, Upland",
phone="(661) 492-4309", addr="1133 W 9th St<br>Upland, CA 91786", find="In the Mountain Avenue Business Park.",
hours=["11:00 AM – 11:00 PM"] * 5 + ["Closed", "Closed"],
ratings=[("4.9", "Google · 88 reviews", GM + "Jujubuilt+Engineered+Performance+1133+W+9th+St+Upland+CA"), ("4.9", "Yelp · 78 reviews", "https://www.yelp.com/biz/juju-built-engineered-performance-upland")],
services=[("", [("Repair and diagnostics", ""), ("Performance upgrades and modifications", ""), ("Engine work", "Reviewers mention head gasket jobs."), ("Pre-purchase inspections", "Mentioned in three Google reviews."), ("Oil changes and routine maintenance", ""), ("Electronics installation", "")])],
```

## Row 35 — Auto Technik Carcare (Chino)

| | Google Maps | Yelp |
|---|---|---|
| Rating | 4.8 from 84 | 4.8 from 471, claimed, "Verified License" badge |
| Address | 5260 Las Flores Dr, Suite A and B, Chino, CA 91710 | same |
| Phone | (909) 393-2679 | same |
| Hours | Mon–Fri 9 AM–6 PM, Sat and Sun closed | opens 9:30 AM on the day checked |
| Website | none | none |

- **Google topics:** honest staff (7), detailed diagnostic (5), quick work (3), respectful staff (3), clear estimate (2), clear explanations (2), oil change (2).
- **Yelp services:** battery and electrical, brakes, engine repair, general diagnosis, HVAC repair, 13 more behind "See more".
- **Owner's Yelp text:** an affordable and dependable family owned auto repair shop; call or message to set up an appointment.
- **Other listings:** AAA lists it as an approved repair shop (https://www.aaa.com/autorepair/shop/auto-technik-car-care-inc-76526). MapQuest describes brake, engine and suspension work.
- **Angle:** diagnosis explained clearly before any work. 471 Yelp reviews is the largest review base on the sheet after El Rey.
- **Flags:** **check the MapQuest Website button before building** (https://www.mapquest.com/us/california/auto-technik-carcare-11116856). A shop with this many reviews and AAA approval may already have a site that Google does not link. Opening time differs by 30 minutes between Google and Yelp.
- **Yelp page:** https://www.yelp.com/biz/auto-technik-carcare-chino-2

```python
short="Auto Technik Carcare", kicker="Auto repair · Las Flores Dr, Chino",
phone="(909) 393-2679", addr="5260 Las Flores Dr, Suite A and B<br>Chino, CA 91710",
hours=["9:00 AM – 6:00 PM"] * 5 + ["Closed", "Closed"],
ratings=[("4.8", "Yelp · 471 reviews", "https://www.yelp.com/biz/auto-technik-carcare-chino-2"), ("4.8", "Google · 84 reviews", GM + "Auto+Technik+Carcare+5260+Las+Flores+Dr+Chino+CA")],
services=[("", [("Diagnostics", "Google reviewers mention detailed diagnostics and clear estimates."), ("Brakes", ""), ("Engine repair", ""), ("Air conditioning and heating", ""), ("Battery and electrical", ""), ("Oil changes", "")])],
```

## Row 29 — A-1 Auto Expert (Chino)

| | Google Maps | Yelp |
|---|---|---|
| Rating | 4.8 from 93 | 4.5 from 188, claimed |
| Address | 14580 Central Ave, Chino, CA 91710, "Located in: Central Park" | same |
| Phone | (909) 393-0777 | same |
| Hours | Mon–Fri 8 AM–5 PM, Sat and Sun closed | same |
| Website | none | none |

- **Google topics:** quality of work (4), trustworthy (4), oil change (3), respectful (3), family business (2), honest work (2), appointment required (2), transmission (2), battery change (2).
- **Yelp services:** battery and electrical, brakes, engine repair, exhaust repair, general diagnosis, 14 more.
- **Yelp amenities:** waiting room, service observation window, ASL proficient, accepts credit cards.
- **Angle:** family business where you can watch the work. "ASL proficient" is unusual and worth asking the owner about before using it.
- **Flags:** Andrew's batch 7 notes say MapQuest shows a Website button; neither Google nor Yelp lists a site. Check it. **Checked Nov 13:** the MapQuest button links to autoexpertonline.com, a different business (a car-buying service in Riverside); a web search found only directory listings and BBB shows no website, so A-1 has no site of its own and the verdict is now Build. Appointments appear to be required. Two staff members are named in many reviews; not used here.
- **Yelp page:** https://www.yelp.com/biz/a-1-auto-expert-chino

```python
short="A-1 Auto Expert", kicker="Auto repair · Central Ave, Chino",
phone="(909) 393-0777", addr="14580 Central Ave<br>Chino, CA 91710", find="In the Central Park center. Call ahead; reviewers say appointments are needed.",
hours=["8:00 AM – 5:00 PM"] * 5 + ["Closed", "Closed"],
ratings=[("4.8", "Google · 93 reviews", GM + "A-1+Auto+Expert+14580+Central+Ave+Chino+CA"), ("4.5", "Yelp · 188 reviews", "https://www.yelp.com/biz/a-1-auto-expert-chino")],
services=[("", [("Diagnosis", ""), ("Brakes", ""), ("Engine repair", ""), ("Transmission", "Mentioned in Google reviews."), ("Exhaust", ""), ("Battery and electrical", ""), ("Oil changes", "")])],
```

## Row 27 — Auto Repair Foreign Domestic (Chino)

| | Google Maps | Yelp |
|---|---|---|
| Name | Auto Repair Foreign Domestic | Auto Repair Foreign Domestic & VW |
| Rating | 4.3 from 94 | 4.1 from 91, claimed |
| Address | 12949 Central Ave, Chino, CA 91710 | same |
| Phone | (909) 627-5018 | same |
| Hours | Mon–Fri 8 AM–5 PM, Sat 8 AM–1:30 PM, Sun closed | same |
| Category | Auto repair shop | Auto Repair, Smog Check Stations |
| Website | none | none |

- **Google topics:** pricing (23), truck (7), friendly owner (6), honest mechanic (4), honest staff (4), diagnosis (4), smog check (3), oil change (3), warranty (2).
- **Yelp services:** battery and electrical, brakes, engine repair, light repair, oil changes, 2 more.
- **Yelp review highlights mention:** a fault traced to the car's main computer, and long-running problems fixed on a 2013 VW Passat. Yelp's "people also searched" list is all VW repair.
- **Angle:** Volkswagen work is what sets it apart; pricing is what reviewers talk about most.
- **Flags:** the newest Google review shown is a complaint about waiting an hour with an appointment. The owner is named in 55 Yelp reviews; not used here. The Google name has no "VW"; ask which name the owner uses.
- **Yelp page:** https://www.yelp.com/biz/auto-repair-foreign-domestic-and-vw-chino-3

```python
short="Auto Repair Foreign Domestic", kicker="Auto repair and smog · Central Ave, Chino",
phone="(909) 627-5018", addr="12949 Central Ave<br>Chino, CA 91710",
hours=["8:00 AM – 5:00 PM"] * 5 + ["8:00 AM – 1:30 PM", "Closed"],
ratings=[("4.3", "Google · 94 reviews", GM + "Auto+Repair+Foreign+Domestic+12949+Central+Ave+Chino+CA"), ("4.1", "Yelp · 91 reviews", "https://www.yelp.com/biz/auto-repair-foreign-domestic-and-vw-chino-3")],
services=[("", [("Volkswagen repair", "Yelp reviewers mention VW work; the Yelp listing name includes VW."), ("Diagnosis", ""), ("Smog check", ""), ("Brakes", ""), ("Engine repair", ""), ("Battery, electrical and lights", ""), ("Oil changes", "")])],
```

## Row 39 — Claremont Auto Care (Pomona)

| | Google Maps | Yelp |
|---|---|---|
| Rating | 4.5 from 75 | 3.9 from 67, claimed |
| Address | 3624 Lynoak Dr, Pomona, CA 91767 | 3624 Lynoak St, Pomona, CA 91767 |
| Phone | (909) 621-3872 | same |
| Hours | Mon–Sat 8 AM–5 PM, Sun closed | same |
| Website | none | none |

- **Google topics:** honesty (5), smog test (3), oil change (3), knowledgeable mechanics (3), great work (3), coolant check (2), clear explanations (2), fairness (2).
- **Yelp services:** oil changes, routine maintenance.
- **Manager's Yelp text:** new and used vehicle maintenance, minor and major repairs.
- **Angle:** plain neighbourhood shop, six days a week; honesty and smog tests.
- **Flags:** the sheet says Claremont but both listings say Pomona, on the Claremont border. Street is "Dr" on Google and "St" on Yelp. Yelp rating is 0.6 below Google's, so lead with Google.
- **Yelp page:** https://www.yelp.com/biz/claremont-auto-care-pomona

```python
short="Claremont Auto Care", kicker="Auto repair · Lynoak Dr, Pomona",
phone="(909) 621-3872", addr="3624 Lynoak Dr<br>Pomona, CA 91767",
hours=["8:00 AM – 5:00 PM"] * 6 + ["Closed"],
ratings=[("4.5", "Google · 75 reviews", GM + "Claremont+Auto+Care+3624+Lynoak+Dr+Pomona+CA"), ("3.9", "Yelp · 67 reviews", "https://www.yelp.com/biz/claremont-auto-care-pomona")],
services=[("", [("Maintenance", "New and used vehicles."), ("Minor and major repairs", ""), ("Smog test", "Mentioned in Google reviews."), ("Oil changes", ""), ("Cooling system", "Reviewers mention coolant checks.")])],
```

## Row 34 — 2Man Moving Services (Ontario)

| | Google Maps | Yelp |
|---|---|---|
| Rating | 4.8 from 85 | 4.7 from 258, claimed |
| Address | 1372 E 5th St Spc 104, Ontario, CA 91764 | not read |
| Phone | (818) 964-3103 | (747) 340-9007 |
| Hours | Open 24 hours | Open 24 hours, seven days |
| Category | Moving and storage service | Movers, Packing Services, Self Storage |
| Website | none | none |

- **Google topics:** polite staff (10), friendly crew (7), on time (4), fast move (3), timeliness (3), stress-free move (3), furniture protection (3), rescheduling (2).
- **Yelp services, verified by the business:** in-state moving, out-of-state moving, international moving.
- **Owner's Yelp posts:** 15 years of experience; international moves; open 24 hours every day; 10% off for new customers; an expired 5% offer from 2024.
- **Other listings:** Three Best Rated lists it among Ontario movers and adds junk removal.
- **Angle:** movers who answer at any hour. The owner is active on Yelp, which suggests someone who would use a site.
- **Flags:** **two different phone numbers**; ask which one to publish. "Spc 104" reads like a home address, so show a service area, not the address, until the owner says otherwise. This is the first non-auto lead, so the auto photos and service wording in the generator will not fit. Discount offers change; leave them off.
- **Yelp page:** https://www.yelp.com/biz/2man-moving-services-ontario-4

```python
short="2Man Moving Services", kicker="Movers · Ontario, California",
phone="(818) 964-3103",  # Google's number; Yelp shows (747) 340-9007
hours=["Open 24 hours"] * 7,
ratings=[("4.8", "Google · 85 reviews", GM + "2Man+Moving+Services+Ontario+CA"), ("4.7", "Yelp · 258 reviews", "https://www.yelp.com/biz/2man-moving-services-ontario-4")],
services=[("", [("Local and in-state moves", ""), ("Out-of-state moves", ""), ("International moves", ""), ("Packing", ""), ("Storage", "")])],
```

## Row 30 — Star Hi-Tech Auto (Pomona)

| | Google Maps | Yelp |
|---|---|---|
| Rating | 4.4 from 89 | 2.6 from 32, **unclaimed** |
| Address | 609 E Arrow Hwy, Pomona, CA 91767 | same |
| Phone | (909) 399-9330 | same |
| Hours | Mon–Sat 7 AM–6 PM, Sun closed | none listed |
| Website | none | none |

- **Google topics:** honesty (9), mechanic (7), work (5), engine repair (3), quality of work (3), electrical repair (2), dealership alternative (2), diagnose (2).
- **Yelp:** only "routine automotive maintenance" listed. The most common review highlight is about slow turnaround and poor communication.
- **Flags:** the 1.8-point gap between Google and Yelp makes this a weak pitch and a risky page to put a rating on. The sheet says Claremont; both listings say Pomona. If built, show the Google rating only and do not link Yelp.
- **Yelp page:** https://www.yelp.com/biz/star-hi-tech-auto-pomona

## Row 38 — Diamond Auto Center / Propane (Ontario) — skip

Yelp's claimed page for Diamond Auto Center at 105 W California St lists a business website, **diamondautoc.com** (the site itself was not opened). Google shows no website link, which is why it is on the sheet. Google 4.8 from 78; Yelp 4.2 from 10; Mon–Fri 8–5, Sat 8–4, and Yelp adds Sun 9–2. Mark as "has website" unless the site turns out to be dead.

---

## Sheet corrections found along the way

- Rows 30 and 39 are in Pomona, not Claremont.
- Row 28 (John's Auto Repair) and the Ceres Collision row have sites in the repo; the workbook now marks them Yes.
- Tri Auto, Moreno's and Muffler Doctor are still marked Yes in the workbook although their sites were removed. Left for Vincent to decide.

## Next

Most of rows 40 to 59 were built in batches 8 to 10, so further research briefs for those rows would arrive late. More useful from Vincent's side: checking the built sites' facts against Google Maps and Yelp, and website checks like the Diamond Auto Center one.
