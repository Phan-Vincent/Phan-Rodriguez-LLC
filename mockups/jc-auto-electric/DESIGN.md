# J C Auto Electric — "Find the fuse"

Concept website for J C Auto Electric, 10640 Ramona Ave, Montclair, CA 91763.
Sales mockup, not the official site.

## Audience and job

Drivers with a problem other mechanics could not pin down: a car that will
not start, a gauge that reads wrong after a part was replaced, a battery
light, dead windows. Many are sent by another shop or a friend. They do not
know the name of the fault, only the symptom. The page lets them find their
symptom, see that this shop traces it, and call. Reviews also say the shop
does general repair, not only electrical.

## Three directions considered

1. **Find the fuse (selected).** The first screen is a fuse box. Each fuse
   is a symptom in plain words. Pick one and a panel says what the shop
   checks for it. It is the diagnostic conversation, started before the call.

   ```
   +--------------------------------------------------+
   | J C Auto Electric          (909) 625-9181        |
   | What's it doing?                                 |
   | +------+ +------+ +------+ +------+              |
   | |won't | |batt. | |gauge | |windows|   panel:    |
   | |start | |light | |wrong | |locks  |   what we   |
   | +------+ +------+ +------+ +------+   check      |
   | +------+ +------+ +------+ +------+              |
   +--red wire runs down the left margin--------------+
   | o  Not only electrical     | hours               |
   | o  Find us                 |                     |
   +--------------------------------------------------+
   ```
2. **Wiring diagram poster.** Whole page as a schematic with component
   symbols. Handsome, but Muffler Doctor already uses a labelled schematic,
   and symbols mean nothing to someone whose car will not start.
3. **Lightning-bolt energy brand.** Yellow bolt, black ground, "we bring the
   spark". The default for every auto-electric logo; says nothing specific.

Direction 1 wins because customers arrive with a symptom, not a part name.

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Panel black | `#16181b` | fuse box ground, text on paper (16:1) |
| Paper | `#f3efe6` | page ground |
| Live red | `#d42a20` | the wire, 10 A fuses, primary button (white text 4.9:1) |
| Fuse blue | `#2c6fd6` | 15 A fuses; white text 4.9:1 |
| Fuse yellow | `#f4c20d` | 20 A fuses, focus ring; black text 11:1 |
| Fuse green | `#2f8f4e` | 30 A fuses; white text 4.1:1, so label is 18px bold |
| Copper | `#b5672b` | terminals, rules |

Fuse colours follow the real blade-fuse colour code (10 A red, 15 A blue,
20 A yellow, 30 A green), so the colour is not decoration.

**Type**

- Display and headings: Space Grotesk 700, sentence case. h1
  `clamp(44px, 8vw, 116px)`, line-height 0.95.
- Fuse labels: Space Grotesk 700, 18–22px.
- Amp ratings and wire labels: Space Mono 700, 13–14px. These are real
  ratings printed on fuses, the one place a monospace belongs.
- Body: Space Grotesk 400/500, 17–19px, line-height 1.55.

**Layout**

Left-aligned, 1200px frame. Hero is a black fuse-box panel: heading top
left, a 4×2 grid of fuses, and to the right a wider read-out panel that
changes with the selected fuse. Below the hero the page is paper; a 4px red
wire runs down the left margin with copper terminal dots where each section
starts. Sections are unequal: "Not only electrical" is wide and short, hours
is narrow and tall. Mobile: fuses in a 2×4 grid, read-out directly beneath,
wire stays at the left edge (16px in), fixed call/directions bar.

**Signature**

The fuse box. Eight fuses, each a real button (`aria-pressed`), each with an
amp rating and a symptom. The read-out has `aria-live="polite"`. The first
fuse is selected on load, and without JavaScript all eight read-outs show as
a plain list.

**Motion**

Only in response to a tap: the chosen fuse seats 4px down and the read-out
text swaps (150ms). No ambient or load animation.

**Accessibility**

Skip link, landmarks, one h1, fuses are buttons in DOM order, visible 3px
yellow focus ring, 56px minimum fuse height, real hours table with today's
row marked (America/Los_Angeles; plain table without JS).

## Content and limits

Sourced Nov 10, 2026: Google Maps (4.7, 83 reviews; category "auto
electrical service"; listing is unclaimed; Mon–Sat 8 AM–5:30 PM, Sun closed;
(909) 625-9181; topics: honest mechanic, friendly staff; reviews mention a
fuel gauge fault traced after another mechanic replaced the pump, and a
Silverado that shut off on the freeway) and Yelp (unclaimed, 4.2, 12
reviews; Mon–Fri 8–5:30, **Sat 8–4**; reviewers say the shop does more than
electrical, including A/C, but not wheel alignments).

- Saturday closing time differs (Google 5:30, Yelp 4:00). The page shows
  "8:00 AM – 4:00 PM, call to confirm" for Saturday.
- Reviewers name Juan; not used until the owner approves.
- One 2022 Yelp review is a serious complaint about a transmission job. It
  is an owner conversation, not page content. The page lists no
  transmission work.
- Symptom read-outs describe what an auto electrician normally checks. They
  are draft copy for the owner to correct, and the page says a diagnosis
  needs the car in the shop.
- No prices, warranties, certifications, years in business, review quotes or
  listing photographs.
- No "Open now" badge (house style, docs/design-system/ui-changes-playbook.md).

## Deliberately avoided

Lightning bolts, circuit-board background textures, glowing neon, a schematic
with component symbols, service cards, a contact form.
