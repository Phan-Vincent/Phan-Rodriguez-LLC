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
