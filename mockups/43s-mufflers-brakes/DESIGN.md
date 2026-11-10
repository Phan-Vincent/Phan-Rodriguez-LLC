# 43's Mufflers & Brakes — "The Sign Out Front"

Concept website for 43's Mufflers & Brakes, 1717 W Holt Ave (Ste 1709), Pomona, CA 91768.
Sales mockup, not the official site.

## Audience and job

Pomona drivers with a loud, leaking or stolen exhaust part, a brake job, or an older
car other shops shrug at. Reviews mention a '63 Bel Air wagon, a Grand Marquis, an
'86 Nissan pickup and stolen catalytic converters. They are on a phone, comparing
quotes, and they will call. The page has one job: make the phone number the easiest
thing to hit and tell them what the shop welds, fits and fixes.

## Three directions considered

1. **The Sign Out Front (selected).** The shop's real identity is a hand-painted
   sign: black board, chrome-yellow "43's", white slanted MUFFLERS, and the phone
   number painted as large as the name. The page is that sign, hung on a painted
   block wall. The phone number is the hero, exactly as it is on the building.

   ```
   +--------------------------------------------------+
   | black sign board                                 |
   | 43's   MUFFLERS & BRAKES                         |
   | 909-868-1997  (tap to call, biggest thing here)  |
   +-----------------------------+--------------------+
   | cream block wall            | oxide-red bay door |
   | painted service list        | hours, open now    |
   +-----------------------------+--------------------+
   ```
2. **Lowrider pinstripe.** Candy paint colour, pinstripe flourishes, chrome script.
   Fits the classics in the photos, but it claims a custom-car culture the shop has
   not claimed, and most customers come for a catalytic converter.
3. **Parts-counter receipt.** Carbon-copy invoice with line items. Honest and
   quick to read, but it implies prices we do not have, and Tepa already uses a
   work-order document.

Direction 1 wins because it is already theirs. Nothing is invented: the owner
recognises the building, and the customer recognises the page when they pull up.

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Sign black | `#15130f` | sign board, body text on cream (15.6:1) |
| Chrome yellow | `#f5c518` | "43's", phone number, focus ring (12.4:1 on black) |
| Lettering white | `#ffffff` | sign lettering |
| Block cream | `#e8dfcb` | painted wall, page ground |
| Bay red | `#8f3a29` | roll-door panel; white text on it 7.2:1 |
| Mortar | `#cfc4ab` | block joints, rules |

**Type**

Barlow, a family drawn from California highway signs and plates, in two widths.

- Display: Barlow Condensed 800 italic, uppercase only where the real sign is
  uppercase. Sign name `clamp(64px, 24vw, 210px)`, phone `clamp(52px, 18vw, 190px)` on one line.
- Headings: Barlow Condensed 700 italic, `clamp(34px, 5vw, 64px)`, sentence case.
- Body: Barlow 400/600, 17–19px, line-height 1.55, max 62 characters.

**Layout**

Left-aligned throughout. 1280px frame, 12 columns, 8px spacing unit. The sign board
is full-bleed and hangs slightly off the left margin; the wall below splits 7/5
with the red bay door on the right, taller than its neighbour so the two edges
never line up. Mobile stacks sign, call bar, services, door; the phone number
keeps its full width and the door becomes a full-bleed band.

**Signature**

The phone number painted at sign scale, as a single tap target. Block-wall joints
are drawn with two repeating linear gradients so the cream reads as cinder block,
not paper.

**Motion**

One moment: on load the sign lettering is "painted" left to right with a clip
reveal (0.7s, once). Nothing else moves by itself. Reduced motion: lettering is
simply there.

**Accessibility**

Skip link, landmarks, one h1, real hours table with today marked and an
open/closed line (America/Los_Angeles; table still reads without JS), 3px yellow
or black focus outlines, 48px minimum targets, fixed call/directions bar on mobile.

## Content and limits

Sourced Nov 10, 2026: Google Maps (4.5, 105 reviews; hours Mon–Fri 9:30–5:30,
Sat 9:30–1:30, Sun closed; (909) 868-1997) and the claimed Yelp profile (4.8,
98 reviews; same hours; business description lists exhaust systems, catalytic
converters, mufflers, tow hitches, general welding and complete auto service;
services list includes drum and rotor brake repair). Reviewers name Jennifer and
Danny; names are not used on the page until the owner approves.

No prices, no quotes from reviews, no smog or legality claims, no founding year,
no photographs copied from listings. Reviews are summarised as topics with links
to both live profiles. Yelp also lists a separate 43's in Whittier; this page is
Pomona only.

## Deliberately avoided

Service cards, icon rows, gradient heroes, an exhaust schematic (Muffler Doctor
owns that), numbered steps, testimonial carousels, a booking form.
