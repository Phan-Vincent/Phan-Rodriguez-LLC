# Design decisions — Tri Auto, A C Tires, Moreno's Auto Repair

Three concept sites for West Inland Empire shops with no website. Each is one standalone `index.html` (the repo's existing stack: no build step, no external fonts or scripts), so a shop owner can open it from a text message.

## Audience

Local drivers on a phone, usually with a problem right now: a flat, a warning light, a dealer quote that hurts. They want to know three things fast: can you fix my car, are you open, where are you. The second audience is the shop owner, who has to recognize their own shop in the first screen.

## Three directions considered

1. **Storefront as brand (chosen).** Build each identity from the shop's real signage and building: Tri Auto's italic wordmark and red/orange/yellow slashes, A C Tires' royal-blue wall and hand-painted red sign, Moreno's white wall, red trim and stack of banners. Poster-scale type, one physical object per site.
2. **Dark performance garage.** Black pages, neon accents, carbon textures. Looks impressive but would make all three shops look the same, and none of them look like that in person.
3. **Clean service-app.** White cards, rounded corners, icon grid, booking form. Easy to use, but reads as a franchise template and promises online booking the shops don't offer.

Direction 1 wins because the pitch is "this is *your* shop, online". An owner who sees their own sign in the first second is easier to sell than one looking at a template.

## Shared system

- **Layout:** 1180px max column, large asymmetric heroes, hard section breaks (no floating rounded cards).
- **Type:** poster display face from local fonts (Impact / Arial Black chain, no downloads), Arial body, monospace eyebrows.
- **Motion, used sparingly:** headline words rise in once; sections reveal on scroll; ratings count up; one marquee per site; one scroll-linked object per site. All of it is switched off under `prefers-reduced-motion`.
- **Function:** live "Open now / Closed" status and today's row highlighted, computed in Pacific time; tap-to-call phone; Google Maps directions link.
- **Accessibility:** skip link, visible focus rings, semantic headings and tables, decorative art hidden from screen readers.
- **Texture:** a light film grain and directional light on every page so flat color doesn't look flat.

## Per site

| | Tri Auto (Chino) | A C Tires (Ontario) | Moreno's Auto Repair (Ontario) |
| --- | --- | --- | --- |
| Catchphrase | "Bye-bye, dealership." | "Flat at 7 PM? We're still open." | "If it's on the banner, we fix it." |
| Other lines | "Three makes. Nothing else." | "Tires. That's it. That's the shop." / "Look for the blue building." | "Read the wall. That's the menu." |
| Palette | Stucco cream `#efe6d3`, ink `#141414`, slashes `#d7261e` `#f26b1d` `#f7b51c` | Royal blue `#1f3fae`, sign white `#fdfbf4`, sign red `#d62b1f`, badge yellow `#ffd23c` | Wall `#f4f1ea`, trim red `#c81f25`, banner yellow `#ffd21f`, banner blue `#1d4fb8` |
| Type voice | Heavy italic, like the sign | Condensed block capitals, like the painted sign | Block capitals on banner colors |
| Signature element | Three slashes dropping along a slanted photo of a mechanic's hands | A round, wheel-shaped photo of a tire being fitted, with the "Open til 8" badge | The shop's banners unfurling over a wide shop-floor photo |
| Logo | Redrawn from the shop's own sign | Redrawn from the shop's own sign | No logo found; wordmark set in the banner style |

## What we borrowed from other shop sites

From Zarla's review of auto repair websites and similar round-ups (Colorlib, Freshy):

- Name the specialty in the headline (Tri Auto: three makes only).
- Lead with work photography, not illustration.
- Put the rating next to the call button, where doubt shows up.
- Show a strip of makes serviced so drivers know "do you work on mine?".
- Keep phone and hours visible, since most repairs are still booked by phone.
- Bright blue for fast tire service; warm, darker tones for specialist repair.

## Photography

All photos are hotlinked from Unsplash's free library (Unsplash License: free for commercial use, no attribution required). None are Unsplash+ images. Each page's footer says they are stock photos. Photo page: `https://unsplash.com/photos/<id>` using the last part of each ID below.

| Site | Use | Unsplash photo ID |
| --- | --- | --- |
| Tri Auto | Hero (hands with wrench) | photo-1619642751034-765dfdf7c58e |
| Tri Auto | Oil change / engine bay / car on lift | photo-1487754180451-c456f719a1fc, photo-1686082307524-c89fb0bfadde, photo-1791419542289-693087bd1044 |
| A C Tires | Hero (fitting a tire) | photo-1645445522156-9ac06bc7a767 |
| A C Tires | Service tiles | photo-1763584357116-31a7d0bf389d, photo-1527266258038-6ae3e089a609, photo-1601739722627-f00a99138ea1, photo-1444947295498-07f60c19a4ff |
| A C Tires | Photo strip | photo-1786489623872-2ebdfe51297c, photo-1578844251758-2f71da64c96f, photo-1675034743372-672c3c3f8377 |
| Moreno's | Hero (shop floor, red lifts) | photo-1792793176006-a7b35e29c7e1 |
| Moreno's | Service cards | photo-1429772011165-0c2e054367b8, photo-1444947295498-07f60c19a4ff, photo-1542399204-b8dd4af5113d, photo-1614447428943-52ec0bdbc7aa, photo-1557411255-28ebcc0fdd54, photo-1625047509248-ec889cbff17f |

Because the photos load from Unsplash, the pages need an internet connection to show them. Before launch, download the chosen photos into the repo or replace them with the shop's own.

## Content sources

Address, phone, Google rating and review count: the lead sheet (Google Maps, Nov 8 2026). Hours: Birdeye and SureCritic listings. Review quotes: Yelp excerpts (as shown on MapQuest), Facebook reviews (as shown on Birdeye) and SureCritic; each quote names its source. Services: Tri Auto from review themes, A C Tires from its sign and listings, Moreno's from the banners on its building.

## Verified in a browser

Layout rendered with Playwright (Chrome) at 1440px and 390px, with placeholder blocks standing in for the photos because the build machine cannot reach Unsplash. The photo crops themselves were checked separately in a real browser. Defects found in screenshots and fixed: missing poster font fallback, A C Tires headline wrapping to three lines, the tire disappearing on mobile, a badge covering a button, uneven bay doors, 1–3px horizontal overflow on mobile, headline colliding with the Tri Auto slashes.

## Open items before any site goes live

- Real photos from each owner (shop front, bays, staff). Current photos are stock images, not these shops.
- Owner sign-off on services, hours and the quoted reviews.
- Tri Auto's address: Google shows 6108 Schaefer Ave; older directories show 5203 G St.

## Tri Auto modern refresh (2026-11-10)

Requested by Andrew: rounder, more modern, better type, reviews that rotate on their own.

- **Reference:** sbdautomotive.com (the Awwwards page for it blocks automated reading, so the live site was inspected directly). Borrowed: geometric sans in sentence case, heavy headings, pill buttons, rounded panels, lots of white space, soft shadows. Tri Auto's own red, orange and yellow stripe colors are kept.
- **Type:** Manrope (variable, weights 200 to 800), self-hosted in `mockups/tri-auto/fonts/` under the SIL Open Font License. This replaces Arial Black italic capitals. Tri Auto is no longer a single file: it needs the `fonts/` folder beside it.
- **Shape:** 24px to 32px radius on cards, photo, rating badge and the dark section; pill buttons, phone link and marquee; paper grain and hard 2px rules removed; sticky blurred header.
- **Reviews:** the Pause/Resume button, arrows and helper text are gone. The row scrolls continuously, stops while a visitor touches, holds, hovers or keyboard-focuses it, and continues about a third of a second after they let go. Swiping and arrow keys still work. With reduced motion turned on it does not auto-scroll.
- **Checked:** Playwright at 1440px and 390px, no horizontal overflow, no console errors, auto-scroll, hold and release confirmed by script. Photos were placeholders in that check (the sandbox cannot load Unsplash).
- `tools/auto-shop-generator/build.py` does not produce this version. Edit `mockups/tri-auto/index.html` directly.
- **Follow-up (same day):** removed the section numbers (01 to 04), the 01/02/03 row numbers and the A/B/C card labels; removed the green "Open now" status line from the hero; set every piece of text, including the Tri-Auto wordmark, in Manrope. Today's row is still highlighted in the hours table.

## A C Tires and Moreno's: same refresh (2026-11-10)

Andrew asked for the Tri Auto design changes on the other two sites. Each keeps its own colors and signature element (blue wall and tire for A C Tires; bay banners and '09 for Moreno's).

- Manrope everywhere in sentence case, self-hosted in each site's own `fonts/` folder, so each folder still stands alone.
- Pill buttons, phone link and marquee; 24px to 32px rounded cards, photos, stat tiles, hours rows and dark panels; grain overlay removed; sticky header.
- The green "Open now" status line is removed. Neither site had section numbers.
- Reviews stay as static rounded cards. These sites have only two and three quotes, too few for a rotating row without visible repeats. Add the Tri Auto carousel once more quotes are collected.
- Checked with Playwright at 1440px and 390px: no horizontal overflow, no console errors. Photos were placeholders in that check.
- `tools/auto-shop-generator/build.py` no longer matches any of the three pages. Edit the `index.html` files directly.

## Astryx layer on all three auto shop sites (2026-11-10)

Andrew asked for the three sites to use the Astryx UI values (see `docs/design-system/`). Each page got an "Astryx layer" block at the end of its stylesheet.

- **Neutral palette:** Tri Auto and Moreno's backgrounds moved from warm cream to Astryx's cool gray `#F1F4F7`, with white surfaces, `#0A1317` text, `#4E606F` secondary text and `#CCD3DB` borders. A C Tires keeps its blue; its cream panels became `#F1F4F7` and white. Brand reds, yellows and blues are unchanged.
- **Radius roles:** 12px for small parts (table rows, banners, sign), 20px for cards, 28px for panels and hero photos, pills for buttons. Astryx's own 12px container radius is scaled up for cards because these are marketing pages.
- **Shadows:** Astryx low on cards, high on hover and on the Tri Auto rating badge.
- **Focus ring:** 2px solid, 3px offset.
- **Motion:** 175ms hover feedback, 410ms reveals, easing `cubic-bezier(.24,1,.4,1)`.
- **Type weights:** headings 700 (was 800), quotes and addresses 600, labels 600. Still Manrope; Astryx's default is the system font.
- **Badges:** section labels ("What we fix", "Services", "Find us") are now small pill badges.
- **Not used:** Astryx's React components and its 14px app text sizes.
- Checked with Playwright at 1440px and 390px: no overflow, no console errors, Tri Auto carousel still scrolls, holds and resumes. Photos were placeholders in that check.

## Feed-style look and muted colors on all three sites (2026-11-10)

Andrew asked for the sites to mirror Facebook's UI look and for logos and designs to be less bright with good contrast. Style cues only: no Facebook logo, name, blue brand color or layout is copied, and each shop keeps its own identity.

- **Look:** light gray canvas `#F0F2F5`, white cards, 8px corners (12px on large panels), thin card shadow, white header with a hairline shadow, flat 6px buttons (gray secondary, brand-colored primary), gray pill labels, system font (Segoe UI on Windows). Manrope files remain in each `fonts/` folder but are no longer used.
- **Light sections:** Tri Auto's dark "Why" band and A C Tires' all-blue page became light sections with white cards. A C Tires keeps blue for the hero and visit panels; Moreno's keeps the red '09 panel and dark visit panel.
- **Muted brand colors:** red `#B3261E` on all three (was `#d7261e`, `#d62b1f`, `#c81f25`); Tri Auto stripes `#C8642A` and `#D9A53A`; A C Tires blue `#1E3A8A` and gold `#E9B949`; Moreno's gold `#E9B949`, blue `#1E4A9C`, panel red `#8C1D18`. Logos use the same muted values.
- **Contrast (WCAG ratio, 4.5 needed for normal text):** red on canvas 5.8, red on white 6.5, gray text on canvas 5.1, gray label on chip 4.5, white on A C blue 10.4, dark on gold 10.3, gold '09 on red panel 5.0, white on red 6.5, Moreno's blue on white banner 8.0. Tri Auto's orange logo stripe is 3.9 on white; it is decoration, not text.
- Checked with Playwright at 1440px and 390px: no overflow, no console errors, Tri Auto carousel still works. Photos were placeholders in that check.

## Three different layouts, new hero photos (2026-11-10)

Andrew asked that the sites stop sharing one layout, stay professional and clean, not too vibrant, with good contrast. He also sent `ai-image-handoff.zip`.

- **Rebuilt from scratch** with `tools/auto-shop-generator/build_v2.py`. The stacked override layers from earlier today are gone.
- **Tri Auto:** split hero (text left, photo right), three make tiles, zigzag photo rows, rotating reviews, one visit card.
- **A C Tires:** navy header, wide photo banner, an info bar overlapping it (open late, phone, address), service list beside a sticky heading, navy stats band, hours as a seven-day strip.
- **Moreno's:** profile-style page. Cover photo, a sticky shop card on the left (ratings, call, directions, address, hours) and content cards on the right (headline with banner-colored service chips, services with thumbnails, the '09 family card, reviews list). No top nav.
- **Shared on purpose:** system font, 8px cards, 6px buttons, muted palette, footer note, noindex, today highlighted in hours.
- **Palette:** red `#B3261E` (Moreno's `#A32420`), A C navy `#16295E`, gold `#E9B949`, neutrals near `#F0F2F5` with `#050505` text and gray secondary text around 5:1.
- **Image pack:** the zip held no image files, only four links and notes. Three were viewed in the browser and are now the hero photos: wrench close-up (Unsplash, Bengkel Mobil Matic Bandung) for Tri Auto, tire mounting (Mustafa Sheikhmouss) for A C Tires, clean workshop (Dextar Studio) for Moreno's. The Pexels brake photo was not used because brake work is not confirmed for Tri Auto.
- **Removed:** marquees, the A C Tires spinning tire and yellow badge, Moreno's bay banners over the photo, Manrope font files.
- **Checked:** Playwright at 1440px and 390px, no overflow, no console errors, Tri Auto carousel scrolls, holds and resumes. Photos were placeholders in that check.

## Quality check before cold calls (2026-11-10)

Checked against Google Maps, Birdeye, SureCritic, Yelp and MapQuest on Nov 10, 2026.

| Item | Tri Auto | A C Tires | Moreno's |
| --- | --- | --- | --- |
| Address (Google Maps) | 6108 Schaefer Ave, Chino 91710. Confirmed; Birdeye's "5203 G St" is wrong or old | 301 W California St, Ontario 91762 | 527 E Holt Blvd, Ontario 91761 |
| Phone (Google Maps) | (909) 465-6422 | (909) 391-4636 | (909) 418-6955 |
| Google rating | 4.9, 333 reviews | 4.4, 324 reviews (was 322) | 4.7, 284 reviews |
| Hours (Google Maps) | Mon to Fri 8 to 5. **Changed from 6 PM.** Birdeye still says 6 PM; ask the owner | Mon to Fri 8 to 8, Sat 8 to 7, Sun 8 to 6 | Mon to Fri 8 to 6 |
| Other | Atly lists Toyota, Honda and Lexus only; reviews name Danny | | SureCritic 4.9 from 661 reviews; opened 2009, family owned |

- **Reviews:** all three sites now have the rotating review row. Every card is a short excerpt from a real review and links to it. Tri Auto: six Facebook reviews via Birdeye (Vincent's links, each phrase re-checked on the page). A C Tires: four Yelp reviews linked by Yelp review ID plus one Google review via Birdeye. Moreno's: five SureCritic reviews (text-fragment links to the listing page) and two Yelp reviews by ID. Two Yelp links were opened and showed the right business and review. Earlier quotes that no longer had a findable source link (Kristina G., James S., G O.) were dropped. SureCritic links point at the recent-reviews page, so older reviews will scroll off it over time.
- **Holiday hours:** none of the three shops publishes holiday hours. Google Maps only says Veterans Day hours "might differ". Each site has a Holiday hours note telling visitors to call first. Replace with real hours once an owner provides them.
- **Wording:** removed hedges ("according to reviews", "Hours from public listings", "On the banner / From reviews" tags, building descriptions). Claims that remain need owner sign-off: Tri Auto "prices well below the dealer's" and "Three makes. Nothing else."; A C Tires "Wheels"; Moreno's service list.
- **Footer:** the short "Concept website by Phan-Rodriguez LLC. Not the official site of this business." line stays while the pages are public.
- **Motion:** every block is hidden until scrolled to, then fades in and slides up, with siblings staggered. Skipped when reduced motion is on; without JavaScript everything is visible.
- **Layout:** A C Tires service list and photo column now match in height; Tri Auto visit card columns are vertically centered.
- **Photos:** all 13 Unsplash URLs load (checked in a browser). They are still hotlinked.
- **Tests:** Playwright at 1440px and 390px on all three: no horizontal overflow, no script errors, reveal hides below-the-fold blocks and shows them on scroll, carousels scroll, hold and resume.

## All lead sites rebuilt in the house style (2026-11-10)

Andrew asked for every site in the repo to be redesigned to match Tri Auto, A C Tires and Moreno's, with real photos, and chose to replace the pages on `main`. Vincent's 16 originals are in git history (last commit before the rebuild: `e69ee8b`); each site's own `DESIGN.md` and `screenshots/` still describe the original and are marked superseded.

- **Generator:** `tools/auto-shop-generator/build_leads.py` (imports the shared base from `build_v2.py`). One data entry per site; three layouts rotated so neighbors differ.

| Layout | Sites |
| --- | --- |
| A, split hero and tiles (like Tri Auto) | Alejandros Tree Service, El Rey "Retro Roadside", J C Auto Electric, Muffler Doctor, Sinaloa Tires, With Pride Auto Air |
| B, photo banner and info bar (like A C Tires) | Diesel Injection Service, El Rey, King Tire Shop, Lockworx, Toy Shop Transmissions |
| C, profile page with sticky shop card (like Moreno's) | 43's Mufflers & Brakes, Don Cortez Tire Shop, JC Bumper Repair, Performance Lube & Oil, Tepa Tire |

- **Shared style:** gray canvas, white 8px cards, system font, flat buttons, each shop's own accent color (muted), scroll reveals, today highlighted in hours, Holiday hours note, noindex, concept-site footer.
- **Facts:** names, addresses, phones, hours, ratings, services and quotes were carried over from Vincent's pages (checked by him Nov 9 to 10). No new facts were added and they were not re-verified in this pass. Dropped because they were flagged as unconfirmed: Diesel Injection Service "Since 1951". Wording such as "according to the shop" was removed, so these need owner sign-off: With Pride "more than 40 years", Performance Lube "free car wash with every service", Lockworx "key copies from $1.50".
- **Removed features:** the interactive pieces of the originals (JC Bumper before/after slider, J C Auto fuse-box picker, King Tire clock, Toy Shop gear selector, location sketches, illustrated storefronts).
- **Reviews:** rating tiles link to the Google or Yelp listing. Unnamed "From Google reviews" quotes are kept only where Vincent had them (El Rey, Lockworx, Don Cortez). No rotating review row on these sites because there are no named, linkable reviews yet.
- **Photos (free license, hotlinked, all confirmed loading from the GitHub Pages address):** Pexels IDs 8986100, 6870299, 12596112, 31127615, 7564861, 6720532, 6870311, 30179627, 14006131, 35020122, 28992999, 8985448, 10490631, 8470881, 6870314, 8985660, 31097241, 18101862, 6565048, 10827691, 32662276, 13065690, 4876645, 29181492, 15489247, 6074540, 10490621; Unsplash 1578844251758. The auto ones come from Andrew's `Company_Image_Research.zip`; food, key and tree photos were found on Pexels the same day. They illustrate the service and are not photos of the businesses.
- **From the research zip, not used:** `moreno_logo.png` is not an image (it contains a "request blocked" message). Tepa Tire: the pack flags a dealer listing with different hours (weekdays 7 to 5); the page keeps Google's 8 to 6 daily, so confirm with the owner.
- **Checked:** Playwright at 1440px and 390px on all 16: no horizontal overflow, no script errors, reveals hide below-the-fold blocks, today's hours highlighted. Photos were placeholders in that check.

## Energy layer on all 19 sites (2026-11-10)

Andrew said the sites looked too boring to sell and sent the first Tri Auto version (`tri-auto (1).html`) as the reference for how lively they should feel, while staying professional. The layouts, colors, facts and photos are unchanged; this adds motion and stronger hero treatment through the shared base in `build_v2.py`, so both generators pick it up.

- **Headline:** larger and heavier (800 weight), words rise in one after another on load, with a gold marker highlight under the accent phrase on light heroes.
- **Moving band:** a dark band of the shop's services scrolls under the hero (at the very top on profile-layout sites).
- **Stripes:** three slanted stripes in the shop's accent color, gold and white drop into banner and cover photos, echoing the Tri Auto sign. Split-layout heroes get offset color blocks behind the photo.
- **Rating badge:** a tilted dark badge with the rating counting up, which drifts slightly with the mouse. Ratings elsewhere count up when scrolled into view.
- **Hover:** tiles fill with the accent color, cards lift with an offset accent shadow, list rows slide, the main button fills and its arrow nudges, photos gain saturation.
- **Other:** a thin progress bar across the top while scrolling, section labels in the accent color with a short rule, a soft accent glow behind the top of the page.
- **Astryx values used:** 175ms and 410ms durations, `cubic-bezier(.24,1,.4,1)` easing, 8px radius, low and high shadow roles, scarce emphasis (one primary button per group).
- **Restraint:** no autoplay video or sound, no flashing, stripes fade to 30% on phones so they never fight the text, and every animation is off when the visitor's device asks for reduced motion.
- **Checked:** Playwright at 1440px and 390px on all 19: no horizontal overflow, no script errors, reveals and today-highlight working, A C Tires carousel scrolls, holds and resumes. Photos were placeholders in that check. Two bugs found and fixed during the check: a broken regular expression that stopped the page script, and a class name clash that turned Moreno's headline blue.

## Tri Auto rebuilt by hand; calmer, more varied templates for the rest (2026-11-10, evening)

Feedback relayed by Andrew: the sites looked nice but like a presentation, the same design and stripes repeated on every site, and they did not look as good as Awwwards sites. He asked for simpler navigation, less clutter, different designs per site, and work modeled on https://www.awwwards.com/websites/honorable/.

**Research limits, stated plainly.** Awwwards blocks automated reading, so its pages were not scanned. Search results gave the names of current honorees (Creative Reference Library, ZIRKA Interceptor, Extrafazant, Agrumea Farm, Grids, Mubien, Fitosauna and others). One honoree's live site (mubien.com) was inspected; another (obys.agency) only showed a loader. The patterns below come from that plus general knowledge of award-level sites, not from a full scan.

**Why the template sites fall short of that standard.** Award sites are designed one at a time around their own photography or film, a chosen typeface and a single idea. Ours were 19 pages from one shared stylesheet with stock photos and the system font, restyled several times in one day.

**Tri Auto (`tools/auto-shop-generator/build_tri.py`, hand-designed, no longer built by `build_v2.py`).**
- Type: Archivo (variable width and weight) for display and text, Instrument Serif italic as the accent. Both self-hosted in `mockups/tri-auto/fonts/` under the SIL Open Font License.
- Full-screen photo hero with the headline set on it, navigation and phone on top, rating in the corner. The photo eases back as you scroll.
- One statement paragraph and three facts (hours, address, phone) directly under the hero, so the essentials are found without hunting.
- The three makes as full-width words on hairlines; a photo follows the mouse over each row.
- A dark section with a heading that stays in place while three photo blocks scroll past and wipe in.
- Large serif pull quote, then Vincent's rotating review row (same links).
- The phone number as the closing headline, then address, hours with today highlighted and the holiday note. Outlined wordmark in the footer.
- Navigation: a slim bar with section links and the phone appears after the hero; phones get a fixed Call / Directions / Hours bar.
- The three-stripe motif now appears only in the Tri Auto logo, where it comes from the real sign.
- Checked with Playwright at 1440px and 390px: no overflow, no script errors, all reveals fire, carousel moves, fonts load. Photos were placeholders in that check.

**The other 18 (still templates, so they will not reach the Tri Auto standard).**
- Stripes and the moving band removed (band kept on El Rey and King Tire only). Headlines smaller, sections tighter.
- Three more layouts added, six in total: poster (Diesel Injection, El Rey Retro Roadside, Lockworx), framed photo (Alejandros, JC Bumper, Toy Shop), service desk with an at-a-glance card (Don Cortez, J C Auto Electric, Sinaloa), alongside split, banner and profile.
- Services are shown differently per site: tabs (Diesel, Lockworx, El Rey menu), accordion (J C Auto symptoms, Toy Shop), chips, lists, tiles or two-column items.
- Every site has the phone action bar and an anchor for hours.
- Next step proposed to Andrew: redo the remaining sites one at a time by hand, like Tri Auto, starting with the leads most likely to buy.

## Three more lead sites added to the generator (2026-11-10, night)

Vincent's fourth lead batch went into `build_leads.py` instead of hand-built pages, so the new sites match the house style: County Brake, Alignment & Mufflers Plus (banner layout, service list), Hock's Japanese Car Specialists (profile layout, service list) and J & S Auto Center & Smog (service desk layout, tiles). The generator now builds 19 lead sites; rebuilding left the other 16 byte-identical.

- **Facts:** read from each shop's Google Maps and Yelp pages on Nov 10; details and open questions are in `docs/lead-batch-2026-11-10/BATCH-4.md`. No review quotes or staff names.
- **Photos:** six Pexels free-license stock images, picked from a contact sheet. One with a visible car-maker badge was swapped out.
- **Checked:** Playwright at 1440px and 390px with the real photos loading: no horizontal overflow, no script errors, one h1, no missing images, no motion under reduced-motion. Not checked: keyboard tab order, physical phone, other browsers.


## 2026-11-10 — Lead sheet cleanup and flagship rebuild

**Removed (lead sheet status "not interested"):** Tri Auto, Moreno's Auto Repair, Muffler Doctor. Their folders, landing cards and README rows are gone; the generators skip them. ROYSAUTOREPAIR IN UPLAND and RC Auto concept also declined but never had a site.

**Still in play, rebuilt by `tools/auto-shop-generator/build_flagship.py`:** Lockworx (gave an email), El Rey, Don Cortez, A C Tires, Alejandros Tree Service, Sinaloa Tires, King Tire Shop, 43's Mufflers & Brakes, Tepa Tire.

**On the call list with no site yet (need research first):** Mailo's Auto Repair, Bee Z Auto Care, Quality Auto Complete Auto Repair, Basic Auto Repair, A Tech Automotive.

**Design direction** (from Andrew's Awwwards captures and the honoree sites we could open): giant tight uppercase grotesk headlines mixed with serif italic, one idea per screen, image cards with small captions, almost no decoration. Fonts are Archivo (variable width) and Instrument Serif, self-hosted in each site's `fonts/` folder (SIL OFL).

Each site has its own art direction, set in `ART` in `build_flagship.py`:

| Site | Hero | Type | Palette | Services |
|---|---|---|---|---|
| lockworx | split (type left, photo right) | wide caps | charcoal, blue, key yellow | grouped index on dark |
| el-rey | colour block with tilted photo card | condensed caps | red, navy, gold | giant menu rows with cursor photo |
| don-cortez-tires | centred poster over photo card | wide caps | royal blue | index on dark |
| alejandros-tree-service | split | serif display | forest green | giant serif rows |
| sinaloa-tires | colour block | wide caps | orange, charcoal | index on dark |
| king-tire-shop | full photo | condensed caps | night navy, red | index on dark |
| 43s-mufflers-brakes | centred poster | wide caps | black, rust, yellow | index on dark |
| tepa-tire | split | condensed caps | cobalt, orange | giant rows |
| ac-tires | full photo | wide caps | navy, red | index, linked review carousel |

Shared behaviour: line-by-line headline reveal, scroll reveals, photo wipe-ins, slim nav bar after the hero, today's hours highlighted, holiday-hours note, giant tap-to-call number, footer wordmark sized by script to span the page, mobile Call / Directions / Hours bar, reduced-motion support. Facts are unchanged from `build_leads.py` / `build_v2.py`; nothing new was claimed. Only A C Tires has per-review links; the others show ratings with a link to the listing and short Google excerpts carried over from Vincent's pages.

Tested with Playwright at 1440 and 390 px: no horizontal overflow, no script errors, all reveals fire. Photos could not be loaded in the test sandbox, so check each live page once after deploy.

## Three more lead sites and a sheet sync (2026-11-10, late)

Vincent's fifth batch, again through `build_leads.py`: Mailo's Auto Repair (split layout, two-column services), Bee Z Auto Care (framed photo layout, accordion) and Quality Auto Complete Auto Repair (poster layout, tabs). These were chosen because the Google Sheet's Status column has them down for calls on Nov 11 and they had no mockup. After rebasing onto the flagship rebuild, `build_leads.py` builds 13 sites (the nine flagship sites and Muffler Doctor are skipped); a rebuild reproduces all 13 byte for byte.

- **Sheet sync:** the Status and Notes entries from the Google Sheet (rows 2 to 20) were copied into `leads/West_IE_No_Website_Leads.xlsx`. The mockup columns could not be written back to the Google Sheet from this session; `leads/google-sheet-paste-L2.tsv` is ready to paste at L2.
- **Facts and photos:** Google Maps and Yelp, read Nov 10; six Pexels free-license photos. Details in `docs/lead-batch-2026-11-10/BATCH-5.md`.
- **Checked:** Playwright at 1440px and 390px with real photos: no horizontal overflow, no script errors, one h1, no missing images, no motion under reduced-motion. Not checked: keyboard tab order, physical phone, other browsers.

### 2026-11-10 (evening) — Real linked reviews and tighter spacing

- **Reviews.** Six sites now rotate real customer reviews, each card linking to that exact review on Yelp (by the review's own id): Lockworx (5), 43's (5), A C Tires (4), El Rey (3), Sinaloa (3), Tepa (2). The reviews and ids were read from each shop's MapQuest listing, which shows its Yelp reviews, on 2026-11-10. Excerpts are short and word-for-word.
- **No per-review links found** for King Tire Shop, Don Cortez (Fontana) and Alejandros Tree Service. Those show the rating with a link to the Google/Yelp listing; Don Cortez's two Google excerpts link to the listing. Birdeye pages do not show the Google review text in a normal browser, so Birdeye links were dropped (including the one on A C Tires).
- **Spacing.** Split heroes are now as tall as their content, the "good to know" block is two even columns, the rating sits beside its summary text, sections are closer together, and a Google map fills the space under the address.

### 2026-11-10 (night) — All 21 lead sites on the flagship generator

Sheet re-checked: the only "not interested" rows are still Tri Auto, Moreno's, Roy's Auto Repair, RC Auto concept and Muffler Doctor; none has a site in the repo. The twelve remaining pages (Mailo's, Bee Z, Quality Auto, County Brake, JC Bumper, With Pride, Performance Lube, J & S, J C Auto Electric, Diesel Injection, Toy Shop, Hock's) were rebuilt by `build_flagship.py` from the facts already in `build_leads.py`. `build_leads.py` no longer writes pages; it only holds the facts. These twelve have no per-review links yet.

### 2026-11-10 (late night) — Batch 7: John's Auto Repair and Ceres Collision

Sheet re-read: the "not interested" rows are unchanged (Tri Auto, Moreno's, Roy's Auto Repair, RC Auto concept, Muffler Doctor) and none has a site. Continued down the sheet from the first row without a site.

- **Built:** `johns-auto-repair` (full photo hero, five Yelp reviews linked by review id) and `ceres-collision` (split hero, no per-review links found). Facts come from each shop's MapQuest listing read on 2026-11-10 (address, hours, description, Yelp reviews); Google rating and phone come from the lead sheet. Not checked against Google Maps directly.
- **Ceres Collision phone conflict:** Google (sheet) lists (909) 251-4447; MapQuest lists (909) 349-2880. The site uses the Google number. Confirm on the call.
- **Skipped, with reasons:** Purrfect Auto Services (part of a multi-location chain that has its own website), A-1 Auto Expert (its MapQuest listing shows a Website button; check before building), Prime Truck and Trailer (no listing found to confirm hours or services), Ontario Mills Tire Pros (Tire Pros is a national dealer network; likely has a site).
- **Next rows without a site:** Auto Repair Foreign Domestic (Chino), Star Hi-Tech Auto (Claremont), Jujubuilt (Upland), 2Man Moving Services, Auto Technik Carcare, Diamond Auto Center, Claremont Auto Care, L & R Auto Repair, Freddie's Auto Repair.

### 2026-11-10 (late night) — Prime Truck and Trailer Repair added

Vincent's session added `prime-truck-trailer-repair` to `build_flagship.py` (photo hero, rows) from its Google Maps listing, which batch 7 had not been able to load. Its own Basic Auto Repair and A Tech Automotive pages, built in parallel with the older generator, were dropped in favour of the flagship ones. Extra findings, including a claimed Yelp page with a service list for A Tech, are at the end of `docs/lead-batch-2026-11-10/BATCH-6.md`. Checked with Playwright at 1440px and 390px; tab order and the map were not checked.
### 2026-11-10 — Every site gets its own mix of details

So that no owner looks at another of our sites and sees a copy of theirs, `vary()` in `build_flagship.py` gives each site a different combination, on top of its own hero, type and palette:

- button and card shape (round, square, soft corners)
- label mark (dot, line, square) and logo mark (two dots, bar, none)
- footer wordmark (outlined, solid accent, tone-on-tone, none)
- facts strip (plain columns or a dark band) and statement alignment (left or centred)
- section order (three orders) and review heading size
- visit section colour (dark, accent colour, or light), with accent only used when the text contrast is at least 4.5:1
- services layout (giant rows, index list, or a card grid)

The mix is fixed by the site's position in `SITES`, so rebuilds are stable and adding a site at the end does not change the others. A check in this session confirmed no two of the 25 sites share the same combination.

### 2026-11-10 — Batch 8: Freddie's, Bates, Express Transmissions, Menas, The Auto Clinic

- **Built:** `freddies-auto-repair`, `bates-auto-service`, `express-transmissions`, `menas-brake-suspension`, `the-auto-clinic`. Address, hours, description and Yelp reviews come from each shop's MapQuest listing (read in a browser on 2026-11-10); every listing's phone matches the lead sheet. Google rating and count are the lead sheet's. Not checked against Google Maps directly.
- **Reviews:** four of the five rotate Yelp reviews linked by review id (Freddie's 5, The Auto Clinic 5, Bates 4, Express 3). Menas had no reviews on its listing, so it links to the Google listing.
- **Service lists are thin on purpose** for Freddie's, Bates and The Auto Clinic: the listings name little beyond auto repair and oil changes, so nothing more is claimed.
- **Express Transmissions warranty:** the listing mentions a three-year, 100,000-mile warranty. The site says so and tells visitors to ask for the terms. Confirm with the owner.
- **Held back:** Kikas Tires. MapQuest shows 1589 E Mission Blvd and (909) 203-0801; the sheet shows 1587 and (909) 643-9998. Needs a check before building.
- **How leads are found cheaply:** search DuckDuckGo's HTML page in the browser for "mapquest <name> <address>", take the MapQuest listing id, then read hours, description and review ids from that page.
- Tested with Playwright at 1440 and 390 px: no overflow, no script errors. Photos reuse ids already confirmed loading on other sites; not viewed live.

### 2026-11-10 — Batch 9: seven more lead sites

- **Built:** `auto-technik-carcare`, `diamond-auto-center`, `claremont-auto-care`, `l-r-auto-repair`, `baja-auto-center`, `ie-automotive`, `v-tech-auto-care`. Same sources and checks as batch 8. All seven rotate Yelp reviews linked by review id; only positive reviews are quoted, word for word.
- **Claremont Auto Care address:** the sheet says 3624 Lynoak Dr, Claremont; MapQuest says 3624 Lynoak St, Pomona, CA 91767. The site shows "3624 Lynoak Dr, Pomona, CA 91767". Confirm street suffix and city with the owner.
- **Held back:** Star Hi-Tech Auto (listing text is about a different business and most recent Yelp reviews are negative), Huerta Smog & Repair (four of five recent Yelp reviews are negative; decide whether to pitch), Sergio's Auto Repair & Tires (no hours on its listing).
- **Not yet researched from the High rows:** Auto Repair Foreign Domestic, Jujubuilt, 2Man Moving, AutoTech's, QUINONEZ Mobile, Arredondo's, German and Japanese Auto, Mendiola Diesel, Molinas Tire & Towing, Williams Independent, HVAC Assistance, Rudy's Auto Works, Gil's Tire Shop, Diaz Landscape, Nino's Lawnmower Shop, Valencia Handyman, JR Truck Tire, Japanese Auto Tech, Sal's Auto Care, and everything below row 70.

### 2026-11-10 — Batch 10: seven more lead sites

- **Built:** `japanese-auto-tech`, `german-and-japanese-auto-pro`, `mendiola-diesel-auto`, `molinas-tire-towing`, `williams-independent-auto`, `rudys-auto-works-paint`, `auto-repair-foreign-domestic-vw`. Same sources and checks as batches 8 and 9. Six rotate Yelp reviews linked by review id; Williams had none on its listing and links to Google.
- **Rudy's address:** the listing title and the sheet say 14597 Arrow Route; the listing's description mentions 8265 Juniper Avenue. The site uses 14597 Arrow Route. Confirm with the owner.
- **German and Japanese Auto Pro:** the sheet's name is cut off ("German and Japanese Au..."); the site uses the name on the MapQuest and Yelp listings.
- **Not found on MapQuest:** Sal's Auto Care (search returned a different shop), Gil's Tire Shop (search returned a different shop).
- **Still to research in the High rows:** Jujubuilt, 2Man Moving, AutoTech's, QUINONEZ Mobile, Arredondo's, HVAC Assistance, Diaz Landscape, Nino's Lawnmower Shop, Valencia Handyman, JR Truck Tire, Kikas Tires (address and phone conflict), then rows 70 to 295.
