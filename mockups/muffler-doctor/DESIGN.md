# Muffler Doctor — "Under the Lift"

Concept website for Muffler Doctor, 5436 Holt Blvd #A5, Montclair, CA 91763, inside
J & J Auto Services Center. Sales mockup, not the official site.

## Audience

Inland Empire drivers with an exhaust problem they can hear: a blown muffler, a
rusted pipe, a joint that has failed, or a vehicle they want to sound different.
They are deciding whether this is a real exhaust shop or a general mechanic. Most
will call rather than book. The owner needs to see a shop that looks technical and
specific, not another oil-change template.

## Three creative directions considered

1. **Under the Lift (selected).** A dark technical manual: blueprint grid, steel
   surfaces, one enormous condensed wordmark, and a bespoke exhaust-route drawing
   that behaves as the page's spine. The aesthetic comes from the underside of a car
   and the marks a fabricator makes on pipe, not from a garage cliché.
2. **Dyno neon.** Black plus acid green, dyno charts, speed lines, "performance"
   language. Visually exciting but would push promises the shop has not made and
   would misrepresent a repair shop as a tuning brand.
3. **Friendly service counter.** Bright cards, rounded tiles, smiling mechanic
   illustrations, online booking. Easy to scan but generic, and it would promise an
   appointment flow the business does not offer.

Direction 1 is chosen because custom exhaust work is fabrication: measurement,
bending, fitting, welding. The design shows that process. It is also structurally
different from the Tepa and Alejandros concepts — dark, horizontal, technical,
full-bleed — rather than an editorial paper page or a light botanical one.

## Selected art direction

**Concept:** the car is up on the lift. You are looking at the system from below,
with the fabricator's notes written on it.

**Palette**

| Token | Hex | Use | Contrast |
| --- | --- | --- | --- |
| Ink | `#0b0d0e` | page, type on yellow | 18:1 on paper |
| Steel | `#161b1e` | section fields | base |
| Steel 2 | `#1f262a` | raised panels, diagram grounds | — |
| Silver | `#c9d0d3` | body copy on dark, pipe metal | 11.5:1 on ink |
| Paper | `#eceae3` | headings on dark | 15.8:1 on ink |
| Signal yellow | `#f2c400` | wordmark, buttons, pin, today | 11.9:1 with ink |
| Muted | `#9aa5aa` | captions, metadata | 7.1:1 on ink |
| Line | `rgba(201,208,211,.24)` | rules, blueprint grid | decorative |

Yellow is a sign colour, not a background for body copy. The light "job sheet"
section uses cool gray `#d8dbd7` with ink text.

**Typography**

- Display: `Impact, Haettenschweiler, "Arial Narrow", "Helvetica Neue", sans-serif`,
  local only. H1 at `clamp(82px, 24vw, 310px)`, line-height 0.72, letter-spacing
  −0.02em, uppercase. It is the loudest type in the batch and deliberately so.
- Section display: `clamp(44px, 7vw, 96px)`, line-height 0.86.
- Body: `"Helvetica Neue", Helvetica, Arial, sans-serif`, 16–18px, line-height 1.6.
- Technical labels: `ui-monospace, Menlo, Consolas, monospace`, 9–12px, uppercase,
  letterspaced. Used for diagram annotations, dimensions, hours and plate numbers.
- Numerals: display face for the 4.8; mono for counts and times.

**Layout and breakpoints**

- Full-bleed dark canvas, 1360px content frame, 12-column grid.
- ≥1080px: H1 occupies its own band; a 7/5 foot row holds copy and the component
  drawing. The system drawing is full width in a framed plate. Service rows are
  90px / 1fr / 1.15fr. Visit is a yellow block split 1.05/0.95.
- 760–1079px: hero drawing moves below the copy; system diagram keeps its aspect
  and labels; service rows collapse to 64px / 1fr with the description beneath.
- <760px: single column, 18px margins, H1 spans the width in two lines, diagram
  labels reduce but remain legible, service rows become stacked blocks with the
  number inline. Mobile gets a fixed bottom call/directions bar; body reserves
  space for it.
- No horizontal scroll at 390px. The H1 is capped by `max-width:100%` and the SVG
  plates use `viewBox` + `width:100%`.

**Signature: the exhaust route**

A bespoke inline SVG of a full exhaust system — header primaries, collector,
flange, pipe run, muffler canister, hanger, weld points, tailpipe and tip. It is
drawn, not a stock diagram: silver pipe with a dark outline, a yellow dashed
centreline, dimension marks and mono annotations. The pipe animates as a single
stroke draw on first paint, like a fabricator tracing the run. It is labelled
"SCHEMATIC — NOT A SPECIFIC VEHICLE" so it reads as illustration, not a promise.

The hero carries a second, smaller technical plate: a muffler canister with inlet,
outlet, hangers, weld seams and a fit dimension. Together they make the page's
argument: this shop works on the whole route.

**Sections**

1. Yellow utility bar: address, weekday hours, phone.
2. Sticky dark header, compact wordmark, nav, call button, native `<details>` menu.
3. Hero: oversized MUFFLER / DOCTOR, positioning copy, actions, component plate.
4. Split band: stock rear-of-car photograph and a yellow "sound is a fit, not a
   promise" panel.
5. "The whole route" system drawing and three process notes (form, fit, weld).
6. Service rows: custom exhaust, muffler installation, welding and repair.
7. Proof: outlined 4.8, 165 Google reviews, review topics, outbound Maps link.
8. Visit: yellow block, address inside J & J, hours Mon–Fri 8–5, reticle location
   drawing, call and Maps.
9. Footer: disclaimer and stock-photo disclosure; mobile fixed call bar.

**Motion**

- H1 lines clip up once on load (300ms stagger).
- Exhaust route stroke-draws once; annotation labels fade in after it.
- Small hover lift on service rows, yellow rule expands.
- No parallax, no autoplay carousel, no marquee.
- `prefers-reduced-motion: reduce` removes all of it; drawing and content are
  visible immediately without JavaScript.

**Accessibility**

- Skip link, semantic landmarks, one H1, ordered headings.
- 3px yellow focus ring, offset, on every link/summary.
- Mobile menu is native `<details>`; the fixed call bar has real links, not buttons.
- Diagram is `role="img"` with a prose description; decorative grid is aria-hidden.
- Body text meets AA on both dark and yellow fields; yellow is never used for small
  text on light gray.
- Phone, Maps and hours are text, not images.

## Facts, evidence and gaps

**Sourced (Google Maps fresh check, Nov 9 2026; lead sheet Nov 8)**

- Muffler Doctor, 5436 Holt Blvd #A5, Montclair, CA 91763 — inside the J & J Auto
  Services Center.
- (909) 445-0024. Rating 4.8 from 165 reviews.
- Hours: Monday–Friday 8:00 AM–5:00 PM; Saturday and Sunday closed. Verified on
  Maps after the lead sheet.
- Review topics: custom exhaust, muffler installation, welds. One reviewer, Monica
  Serrano, praises the crew; the mockup does not reproduce or paraphrase her words,
  and links to the live listing instead.
- Physical cues: lift bay, blue/white walls, yellow equipment, red sign.

**Deliberate gaps**

- No prices, wait times, horsepower gains, sound-level promises, smog outcomes or
  legal claims. The page explicitly says the right system depends on the vehicle.
- No claim of certification, licensing, insurance or warranty.
- No direct review quotes and no invented testimonials.
- No online booking or quote form. Phone is the conversion.
- No "since 19xx", staff names or brand affiliations.
- Hours are a dated snapshot and the page tells visitors to call.

**Photography**

- One hotlinked Unsplash photo: rear of a car, used as a workshop/mood image and
  captioned "Stock photograph — not the shop." Source:
  `https://images.unsplash.com/photo-1503376780353-7e6692767b70` (Unsplash License).
- No Google Maps photos copied. Real bay and shopfront photos are a launch-time
  request. The page stands without the image: the SVG plates carry the identity.

## Why this is not a template

There is no card grid, no rounded service tiles, no gradient hero, no stock "auto
repair" icon set. The exhaust schematic is drawn for this page and drives its
structure; the giant wordmark and the yellow visit block are composed around it.
Swapping the palette would not produce either of the other two concepts.

## Supervisor iteration

Supervisor iteration: reduced the desktop masthead from 272px to 222px to bring the main phone action higher in the first screen; retained the separate mobile composition. Removed an unsupported directional description and simplified the booking copy.
See batch VERIFICATION.md for final browser checks.

## Mobile review — November 10, 2026

Repaired the rating selector and label markup that expanded the review grid on phones; added safe-area call-bar/page spacing and sticky-header anchor clearance; constrained short-screen navigation. Checked in touch-enabled Chrome at widths 320, 360, 390, 430, 768, plus 844×390 landscape. See ../../docs/lead-batch-2026-11-09/MOBILE-REVIEW.md for results and limits.
