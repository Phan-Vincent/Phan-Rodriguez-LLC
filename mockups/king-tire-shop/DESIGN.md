# King Tire Shop — "Till nine"

Concept website for King Tire Shop, 8939 Rose Ave, Montclair, CA 91763.
Sales mockup, not the official site.

## Audience and job

Montclair and Pomona drivers who find a nail in a tire after work, when the
chains have a four-hour wait or are already closed. Reviews are about flats,
patches, air, used tires bought in a hurry, and oil changes done on the same
visit. They are on a phone in a parking lot. The page has to say three things
in order: we fix flats, we are open until 9 PM, here is the number.

## Three directions considered

1. **Till nine (selected).** The shop's edge is its hours: 9 AM to 9 PM,
   Monday to Saturday, long after other tire shops lock up. The page is the
   shop at dusk: evening-blue sky, the tan stucco parapet with the red block
   letters, and one yellow A-frame "flat tire repair" sign out front.

   ```
   +--------------------------------------------------+
   | dusk sky                                         |
   | KING TIRE SHOP          (red block letters)      |
   | Flat at 8 PM? We're open till nine.              |
   | [Call (909) 952-9219]  [Directions]     /\       |
   |                                        /  \ sign |
   +=========== tan stucco parapet ===================+
   | 9 AM |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■| 9 PM   |
   | what we do (list)          | hours table         |
   +--------------------------------------------------+
   ```
2. **Crown and royalty.** Gold crown mark, purple, "the king of tires".
   Trades on the name, says nothing true about the shop, and looks like a
   franchise logo kit.
3. **Tire wall.** Stacks of used tires as a black graphic field with white
   price-tag type. Sinaloa, Tepa and A C Tires already draw tires, and it
   needs stock and prices we do not have.

Direction 1 wins because late hours are the one fact every source agrees on
and the one a stranded driver cares about.

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Dusk | `#1c2444` | hero sky, footer; white text 14.6:1 |
| Sign red | `#d3202a` | wordmark on stucco, primary button (white text 5.3:1) |
| Stucco | `#e3d0b0` | parapet band, section ground; ink text 12:1 |
| Board yellow | `#ffd400` | A-frame sign, today row, focus ring; ink text 13:1 |
| Ink | `#17171a` | body text |
| Paper | `#fbf8f1` | light sections |

**Type**

- Display: Anton 400, uppercase only for the shop name (the real sign is
  block capitals). Name `clamp(56px, 13vw, 190px)`, line-height 0.9.
- Headings: Anton, sentence case, `clamp(34px, 5vw, 68px)`.
- Body: Figtree 400/600, 17–19px, line-height 1.55, max 60 characters.

**Layout**

Left-aligned. 1240px frame. Hero is dusk blue and 86vh on desktop; the name
sits low and overlaps the stucco parapet band so the red letters cross from
sky to wall. The A-frame sign stands on the wall between the name and the
call buttons (bottom right on narrower desktops). Below, an
uneven two-column split (7/5): services list left, hours right and lower.
Mobile: name on three lines, call button full width, A-frame shrinks and
sits right of the tagline, hours before services, fixed call/directions bar.

**Signature**

The "day bar": one horizontal bar from 9 AM to 9 PM filled in board yellow,
with a thin marker at 6 PM labelled "when most tire shops close". It is the
argument of the page as a drawing. Second: the CSS A-frame sign reading
"Flat tire repair".

**Motion**

One moment: on load the day bar fills left to right (0.9s, once). Nothing
else moves. Reduced motion: bar is simply full.

**Accessibility**

Skip link, landmarks, one h1, real hours table with today's row marked
(America/Los_Angeles; plain table without JS), 3px yellow focus outlines,
48px targets, day bar has a text equivalent.

## Content and limits

Sourced Nov 10, 2026: Google Maps (4.5, 135 reviews; Mon–Sat 9 AM–9 PM, Sun
closed; (909) 952-9219; topics: flat tire repair, air valve repair, budget
friendly, clean place) and the claimed Yelp profile (4.3, 59 reviews; same
hours; manager's text: alignment, oil change, brakes, new and used tires;
services: balancing, installation, TPMS repair, tire repair, rotation;
accepts credit cards).

- Hours conflicts: one Google reviewer says "open 24 hours", one Yelp
  reviewer describes a Sunday visit, and Birdeye shows 9–8. The page uses
  9–9 Mon–Sat, Sunday closed (Google and Yelp agree) and tells people to
  call if it is close to nine.
- A reviewer got free air; it is not promised on the page.
- Birdeye text says "established 2011" and mentions Pomona; unverified, unused.
- No prices, brands, warranties, review quotes or listing photographs.
- No "Open now" badge (house style, docs/design-system/ui-changes-playbook.md).

## Deliberately avoided

Crowns, gold, tread patterns, tire icons, service cards, a tire-size finder,
night-sky stars or gradients (the sky is one flat colour).
