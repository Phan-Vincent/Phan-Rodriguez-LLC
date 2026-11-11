> **Superseded on 2026-11-10.** Andrew asked for every site to be rebuilt in the shared house style (see the root `DESIGN.md`, section "All lead sites rebuilt in the house style"). The notes below describe Vincent's original concept, which is still in git history (last commit before the rebuild: `e69ee8b`). Screenshots in this folder show the original.

# Performance Lube & Oil — "Oil in, car washed"

Concept website for Performance Lube & Oil, 5288 Riverside Dr, Chino, CA 91710.
Sales mockup, not the official site.

## Audience and job

Chino drivers due for an oil change who would rather not give a dealer
their Saturday. The thing reviewers repeat (27 Google mentions) is that the
car comes back washed, free. Two more facts matter: it is open every day,
and it is tucked behind the Chevron on Riverside Drive, so first-timers miss
it. The page says: oil change, free car wash with it, seven days, here is
where to turn in.

## Three directions considered

1. **Oil in, car washed (selected).** One visit, two jobs. The first screen
   is cut in two fields that meet on a slant: motor-oil amber on the left,
   wash-water blue on the right. The headline reads straight across both.

   ```
   +------------------------/-------------------------+
   | amber                 /  water blue              |
   | Oil change.          /   Free car wash.          |
   | Open every day 8–5  /    with every service      |
   | [Call] [Directions]/                             |
   +-------------------/------------------------------+
   | What we do (two lists: under the hood | outside) |
   | Find us: behind the Chevron (sketch)  | hours    |
   +--------------------------------------------------+
   ```
2. **Dipstick.** A tall dipstick down the page whose oil level tracks the
   scroll. Clever, but it is about oil only and hides the car wash, which is
   why people choose this shop.
3. **Pit-lane racing.** Checkered flags, speed stripes, "performance" taken
   literally. Sinaloa already has a checkered flag, and a lube shop is not a
   race team.

Direction 1 wins because the free wash is the shop's own stated offer and
the most repeated thing in its reviews.

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Oil amber | `#e8a200` | left field, today row; petrol text 8.6:1 |
| Wash blue | `#1596bd` | right field; petrol text 5.6:1 (text on blue is petrol, not white) |
| Petrol | `#0d2730` | all text, primary button ground (white text 15:1), footer |
| Foam | `#f7fbfc` | page ground |
| Tile blue | `#1d5aa6` | the building's tile stripe, used as one 10px rule and link colour (7:1 on foam) |

**Type**

- Display and headings: Bricolage Grotesque 800, sentence case. Hero lines
  `clamp(56px, 7.4vw, 112px)` on desktop, `clamp(40px, 5.6vw, 68px)` below 800px, line-height 0.92.
- Body: Instrument Sans 400/600, 17–19px, line-height 1.55, max 60 characters.

**Layout**

Left-aligned, 1240px frame. Hero: two colour fields split by a slanted edge
(clip-path, about 12 degrees) at roughly 54% across; "Oil change." sits high on
amber, "Free car wash." lower on blue, stepping down along the slant (the
two lines would not fit side by side at poster size). Below, a 10px tile
stripe made of small blue squares, as on the building. Then two unequal
lists ("Under the hood" wider, "Outside" narrower and set lower), then a
"Find us" sketch beside the hours table. Mobile: the slant turns horizontal
(amber on top, blue below, edge still slanted a few degrees), lists stack,
fixed call/directions bar.

**Signature**

The slanted two-colour split with one sentence running across it. Second: a
"behind the Chevron" site sketch (Riverside Dr, the gas station in front,
the shop behind with a pin), labelled as a sketch, not to scale.

**Motion**

One moment: on load the blue field wipes in from the right along the slant
(0.7s, once). Reduced motion: both fields are simply there.

**Accessibility**

Skip link, landmarks, one h1 ("Oil change. Free car wash." as one heading),
real hours table with today's row marked (America/Los_Angeles; plain table
without JS), 3px petrol focus outlines, 48px targets, sketch has role="img"
and a text description.

## Content and limits

Sourced Nov 10, 2026: Google Maps (4.3, 87 reviews; "Located in: Chevron
ExtraMile"; every day 8 AM–5 PM; (909) 364-1197; top topic: free car wash)
and the claimed Yelp profile (4.2, 129 reviews; categories oil change
station and car wash; same hours; manager's text: oil changes, transmission
fluids, coolant flushes, tune-ups, brakes, belts, and a free complete car
wash with every service; services list adds detailing and hand washing;
accepts credit cards).

- "Free car wash with every service" is the manager's own wording on Yelp
  and is attributed that way on the page.
- A Yelp reviewer was given a rain check for the wash; the page says to ask
  about the wash on rainy days.
- Recent reviews on both sites include complaints about feeling rushed into
  extra services and one about oil quantity. That is an owner conversation.
  The page promises no speed, no price and no "no upsell".
- Reviewers name Omar; not used until the owner approves.
- No prices, oil brands, minute counts, warranties, review quotes or
  listing photographs.
- No "Open now" badge (house style, docs/design-system/ui-changes-playbook.md).

## Deliberately avoided

Oil-drop icons, bubbles, checkered flags, speed lines, gradients between the
two colours (the split is a hard edge), service cards, coupons.
