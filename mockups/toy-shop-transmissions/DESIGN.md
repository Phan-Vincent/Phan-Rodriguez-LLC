# Toy Shop Transmissions — "Back in drive"

Concept website for Toy Shop Transmissions, 1292 E 3rd St, Pomona, CA 91766.
Sales mockup, not the official site.

## Audience and job

Two kinds of owner, both in reviews: people with a hot rod or custom whose
transmission no chain shop will touch, and daily drivers whose automatic has
started slipping. Both have been quoted a scary number elsewhere and want
someone who will explain what is wrong before taking it apart. The page
says: transmissions and differentials, rebuilt in Pomona, old cars welcome,
call and describe it.

## Three directions considered

1. **Back in drive (selected).** The first screen is a sixties column-shift
   indicator, the strip on the dash that reads P R N D L. The needle starts
   on N and settles on D. Everything else is quiet.

   ```
   +--------------------------------------------------+
   | Toy Shop Transmissions            (909) 620-5849 |
   |                                                  |
   |  +--------------------------------------------+  |
   |  |   P      R      N     [D]      L           |  |
   |  +----------------------|---------------------+  |
   |  Back in drive.                                  |
   |  Transmissions and differentials, rebuilt in     |
   |  Pomona. [Call] [Directions]                     |
   +--------------------------------------------------+
   | What comes in (wide list)      | hours (narrow)  |
   | Hot rods to daily drivers      | find us         |
   +--------------------------------------------------+
   ```
2. **Toy box.** Play on the name: toy-car packaging, blister cards, primary
   colours. Funny once, and it makes a serious rebuild shop look like a
   hobby store.
3. **Exploded diagram.** A transmission drawn in parts across the page.
   Muffler Doctor already uses a labelled schematic, and a believable gear
   train in SVG is a week of drawing.

Direction 1 wins: a shifter strip is the one part of a transmission every
driver has looked at, and it belongs to the era of the cars this shop is
known for.

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Dash turquoise | `#1f7d7c` | hero ground; white text 4.9:1, large text only below 24px bold |
| Enamel cream | `#f1e9d6` | page ground, indicator face |
| Fluid red | `#a5142b` | needle, primary button (white text 8:1). Transmission fluid is dyed red |
| Chrome | `#c8cdd0` | indicator bezel, rules |
| Ink | `#1d1a17` | text (15:1 on cream) |

**Type**

- Display: Alfa Slab One 400, sentence case. h1 `clamp(52px, 9vw, 132px)`,
  line-height 0.95. Indicator letters in the same face.
- Body: Karla 400/700, 17–19px, line-height 1.55, max 60 characters.

**Layout**

Left-aligned, 1200px frame. Hero is turquoise, about 84vh; the indicator
strip spans the frame width near the top, headline under it, buttons under
that. Below, cream: a wide "What comes in" list (7 columns) with the hours
table narrower and set lower (5 columns), then "Find us". Mobile: indicator
keeps all five letters on one row, call button full width, hours before the
list, fixed call/directions bar.

**Signature**

The shift indicator: a chrome-bezelled cream strip with P R N D L, a red
needle under it. It is a drawing (`role="img"`, labelled), not a control.

**Motion**

One moment: on load the needle slides from N to D (0.8s, once, slight
overshoot). Reduced motion: needle is simply on D.

**Accessibility**

Skip link, landmarks, one h1, real hours table with today's row marked
(America/Los_Angeles; plain table without JS), 3px focus outlines, 48px
targets.

## Content and limits

Sourced Nov 10, 2026: Google Maps (4.9, 67 reviews; category transmission
shop; unclaimed; Mon, Tue, Thu, Fri 9 AM–6 PM, Sat and Sun closed; the
Wednesday row was not readable on Veterans Day week and is assumed 9–6;
(909) 620-5849; topics: knowledgeable staff, hot rods, honesty,
transparency) and Yelp (unclaimed, 4.9, 36 reviews; no hours listed;
services: transmission repair, leak inspection; accepts credit cards).
Reviews describe full rebuilds, a rear differential rebuild, hard-to-find
parts for an older truck, and being shown the broken parts afterwards.

- Neither listing is claimed. Nobody there may be managing listings.
- Reviewers name Kendall; not used until the owner approves.
- "Shown the old parts" is reviewer experience, not a promise on the page.
- No prices, turnaround times, warranties, years in business, review quotes
  or listing photographs.
- No "Open now" badge (house style, docs/design-system/ui-changes-playbook.md).

## Deliberately avoided

Gears and cog icons, toy imagery, flames, pinstripes, checkered flags,
chrome gradients (the bezel is one flat grey with a 1px highlight).
