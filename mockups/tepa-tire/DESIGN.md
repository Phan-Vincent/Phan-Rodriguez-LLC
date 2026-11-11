> **Superseded on 2026-11-10.** Andrew asked for every site to be rebuilt in the shared house style (see the root `DESIGN.md`, section "All lead sites rebuilt in the house style"). The notes below describe Vincent's original concept, which is still in git history (last commit before the rebuild: `e69ee8b`). Screenshots in this folder show the original.

# Tepa Tire & Auto Care — "Work Order"

Concept website for Tepa Tire & Auto Care, 705 S Mountain Ave, Ontario, CA 91762.
This is a sales mockup, not the shop's official site.

## Audience

Ontario drivers on a phone, often mid-problem: a tire losing air, a brake pedal that
feels wrong, a used-car purchase that needs rubber. Many are price-sensitive and
compare two or three independent shops. They need three answers in the first screen:
what the shop does, whether it is open, and how to call. The second audience is the
owner, who should recognise the blue-and-white shop, the tire stacks and the
red/blue canopies immediately.

## Three creative directions considered

1. **Work Order (selected).** The page is built like a shop's paper trail: ruled
   sheets, carbon-copy cobalt, date stamps, itemised service write-ups, a giant tire
   used as a compositional object rather than an icon. Warm ivory paper keeps it
   editorial instead of "garage dark." It fits a business whose promise is
   practical, in-person work.
2. **Highway billboard.** Full-bleed photography, 8-foot condensed type, phone number
   repeated at every fold. Loud and fast, but it flattens the shop into a generic
   tire ad and gives no room for the brake and patching work that differentiates it.
3. **Neighbourhood almanac.** Small-town newspaper columns, halftone photos, hand-set
   type. Warm and trustworthy, but too quiet for a tire shop whose customers decide
   in seconds at the roadside.

Work Order wins because it turns the shop's actual method — write it up, do the
work, hand back the keys — into the layout. It also gives three distinct type sizes
and an asymmetric grid a tire photo cannot provide on its own.

## Selected art direction

**Concept:** a service counter, not a showroom. Paper, stamps, cobalt carbon,
safety-orange marks.

**Palette**

| Token | Hex | Use | Contrast |
| --- | --- | --- | --- |
| Paper | `#f2ede1` | page background | base |
| Ink | `#171a1f` | body and headings | 15.4:1 on paper |
| Cobalt | `#173a8f` | bands, stamp, tire | 8.2:1 with paper |
| Cobalt deep | `#0f275f` | hovers, shadow | 12:1 with paper |
| Safety orange | `#e2571e` | small accents, today marker | 3.3:1 on paper — never body text |
| Rule | `#c7bfab` | hairlines, ticket edges | decorative |
| Muted ink | `#5d5a50` | captions, metadata | 6.2:1 on paper |

Orange is restricted to marks, rules and the "today" flag. All reading text is ink
or paper on cobalt.

**Typography**

- Display: `Impact, Haettenschweiler, "Arial Narrow", "Helvetica Neue", sans-serif`
  — local fonts only. TEPA at `clamp(76px, 18.5vw, 236px)`, line-height 0.76,
  letter-spacing −0.035em, slightly scaled on wide screens.
- Body: `"Helvetica Neue", Helvetica, Arial, sans-serif`, 17–19px, line-height 1.6.
- Metadata: `ui-monospace, Menlo, Consolas, monospace`, 10–12px, uppercase,
  letterspaced 0.14em. Used for dates, ticket numbers, hours and labels.
- Section headings: condensed caps at `clamp(34px, 5vw, 64px)`, with a hairline and
  a two-digit index.

**Layout and breakpoints**

- 1360px outer frame, asymmetric 12-column grid, 24px gutters.
- ≥1100px: hero is 7/5 split (type / tire). Service write-up is a true table with
  dotted leaders. Visit is 7/5 (address / hours). Sticky section labels.
- 760–1099px: hero stacks, tire becomes a half-bleed object; ticket rows reflow but
  keep the ruled-document feel.
- <760px: single column, 20px margins, 48px tap targets, hero wordmark spans the
  viewport width, ticket becomes labelled rows (not a scrolling table). Hours table
  keeps date/value alignment.
- No horizontal overflow at 390px: the display word is clipped inside its own
  container, the tire SVG is `max-width:100%`, and no element exceeds the page
  padding box.

**Signature elements**

1. **The tire as a diagram.** A large inline SVG tire: cobalt carcass, ivory tread
   blocks, orange hub mark, fine technical ring labels. It reads as print, not a
   clip-art icon, and carries the "4.6 / 205" evidence at its centre.
2. **The carbon-copy ticket.** The service list is a real `<table>` styled as a
   triplicate work order, with numbered lines, dotted leaders and a stamped footer.
   It replaces the usual rounded service-card grid entirely.
3. **A drawn corner map.** Cross streets `Mountain Ave` / unlabelled schematic grid in hairlines,
   an orange pin and the address, linking to Google Maps. No map API, no iframe.

**Inventory of sections**

1. Utility strip: address · open 7 days · phone.
2. Header with compact nav and mobile `<details>` menu.
3. Hero: work-order masthead, TEPA wordmark, tire diagram, call/directions.
4. Service marquee (one line, slow).
5. "The shop" editorial split, stock photo with explicit label.
6. Service write-up table.
7. Evidence band: 4.6 rating, 205 reviews, review topics, outbound Google listing.
8. Visit: address, drawn map, phone, seven-day hours with today highlighted.
9. Footer: disclaimer, stock-photo disclosure, concept credit.

**Motion**

- One page-load rise for the TEPA letters (staggered 45ms).
- IntersectionObserver reveal on section blocks, 500ms, 20px travel.
- Static service strip; no continuous marquee.
- Tire rotates 4° on hover only; no scroll hijacking.
- All of the above removed under `prefers-reduced-motion: reduce`; content is visible
  without JS.

**Accessibility**

- Skip link to `#main`, visible 3px focus ring on every interactive element.
- Semantic landmarks, one `h1`, ordered headings, real table headers with `scope`.
- Mobile menu uses native `<details>`/`<summary>`, so keyboard and screen-reader
  behaviour come for free.
- Decorative SVGs `aria-hidden="true"`; the rating is written as text, not stars only.
- Phone and directions are links with descriptive text; map has an accessible name.

## Facts, evidence and gaps

**Sourced (Google Maps via lead sheet + supervisor check, Nov 9 2026)**

- Name, address, phone: Tepa tire & auto care, 705 S Mountain Ave, Ontario, CA 91762,
  (909) 458-9200.
- Rating 4.6 from 205 reviews. Displayed as a dated snapshot.
- Hours: all seven days, 8:00 AM–6:00 PM. This supersedes older Sunday hours found
  elsewhere.
- Review topics: new and used tires, patching, brakes.
- Rough Country dealer locator lists Tepa and confirms mount/balance; its phone
  (909) 458-9197 is an alternate and is not used. The Maps phone is used everywhere.

**Deliberate gaps**

- No prices, financing, warranties, wait times or "best price" claims.
- No direct review quotes: the mockup links to the live listing instead.
- No founding year, staff names, certifications or brand inventory beyond the
  Rough Country mount/balance listing.
- No online booking, quote form or appointment promise. Phone is the conversion.
- Hours are labelled as a Maps snapshot and the visitor is told to call ahead.

**Photography**

- One hotlinked Unsplash photo (tire stack) on the shop section, explicitly captioned
  as stock. Source: `https://images.unsplash.com/photo-1578844251758-2f71da64c96f`
  (Unsplash License). It is decorative support; the tire diagram and ticket carry the
  design if the image fails.
- No Google Maps business photos are copied. The real shop front is a launch-time
  asset to request from the owner.

## Why this is not a template

No rounded cards, no icon grid, no gradient hero. The composition depends on the
ticket table, the oversized wordmark and the tire diagram; removing any one changes
the page. The layout is built from the shop's physical paperwork rather than a
generic service-site skeleton.

## Supervisor iteration

Supervisor iteration: disabled the continuous marquee; removed an unverified cross street and parking instruction; simplified the hero copy. Location diagram is illustrative, with real directions delegated to Google Maps.
See batch VERIFICATION.md for final browser checks.

## Mobile review — November 10, 2026

Tightened 320px hours-table spacing, shortened time labels without changing hours, kept the primary phone on one line, removed visit-grid minimum-width overflow, and cleared the sticky header on section navigation. Checked in touch-enabled Chrome at widths 320, 360, 390, 430, 768, plus 844×390 landscape. See ../../docs/lead-batch-2026-11-09/MOBILE-REVIEW.md for results and limits.
