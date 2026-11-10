# Diesel Injection Service — "Bring the part or bring the truck"

Concept website for Diesel Injection Service, 8482 Cherry Ave, Fontana, CA 92335.
Sales mockup, not the official site.

## Audience and job

Two customers who need different things. One carries a part to the counter:
a mechanic, a farmer with a tractor pump, a contractor with a dead
generator. The other drives a truck in: a Cummins, Duramax or Power Stroke
pickup owner, or a fleet manager. Reviews mention both, and the manager's
own Yelp text lists both (rebuild and test pumps and injectors, turbos;
maintenance and diagnostics for fleets and consumers). The page lets each
person find their half in one glance, then call.

## Three directions considered

1. **Bring the part or bring the truck (selected).** A fine spray fan, the
   pattern an injector makes on a test bench, crosses the first screen from
   a nozzle at the left. Under it the page forks into two uneven columns:
   "Bring the part" and "Bring the truck".

   ```
   +--------------------------------------------------+
   | Diesel Injection Service          (909) 885-0590 |
   | o====>  - - - - - - - - - - - - - - - - - - -    |
   | nozzle    - - - - spray fan - - - - - - - - -    |
   | Diesel pumps, injectors and turbos,              |
   | rebuilt and tested in Fontana.                   |
   | [Call] [Directions]                Since 1951    |
   +--------------------------------------------------+
   | Bring the part (wide)     | Bring the truck      |
   | pumps / injectors / turbo | diagnostics / fleets |
   +--------------------------------------------------+
   | hours (Mon–Fri 7–5)       | find us              |
   +--------------------------------------------------+
   ```
2. **Since 1951 heritage.** Sepia, badge lockup, a timeline. The founding
   date comes from a supplier's page and one reviewer; too thin to build a
   whole identity on, and every old shop does it.
3. **Big-rig chrome.** Black, chrome type, stacks and smoke. Says "truck
   show", not "we test injectors to spec", and most customers here drive
   pickups.

Direction 1 wins because it answers the first question on every phone call
to this shop: are you bringing the part or the vehicle?

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Pump green | `#1b6b38` | hero ground, links; white text 6.5:1. Diesel pump handles are green |
| Bench black | `#141614` | text, footer (white text 18:1) |
| Shop white | `#f3f5ef` | page ground |
| Brass | `#b98a2e` | nozzle fittings, rules, today row tint; never text on white |
| Spray | `#dfe9d8` | the fan lines on green |

**Type**

- Display: Big Shoulders Display 800, sentence case. h1
  `clamp(44px, 7vw, 104px)`, line-height 0.95.
- Body: IBM Plex Sans 400/600, 17–19px, line-height 1.55, max 62 characters.

**Layout**

Left-aligned, 1240px frame. Hero is pump green, about 82vh: nozzle and
spray fan across the top third, headline lower left, "Since 1951" set small
at lower right. Then the fork: "Bring the part" takes 7 columns, "Bring the
truck" 5 and starts lower. Then hours (narrow) beside find us (wide).
Mobile: fan shrinks to a 120px band above the headline, the two columns
stack with part first, fixed call/directions bar.

**Signature**

The spray fan: one inline SVG, a brass-and-steel nozzle at the left and
eleven thin lines fanning out at about 18 degrees total, each a dashed
stroke. `aria-hidden`, purely a drawing.

**Motion**

One moment: on load the fan lines draw outward from the nozzle (0.9s,
once). Reduced motion: lines are simply drawn.

**Accessibility**

Skip link, landmarks, one h1, real hours table with today's row marked
(America/Los_Angeles; plain table without JS), 3px focus outlines, 48px
targets.

## Content and limits

Sourced Nov 10, 2026: Google Maps (4.9, 83 reviews; category diesel engine
repair service; Mon–Fri 7 AM–5 PM, Sat and Sun closed; (909) 885-0590;
topics: injector replacement, turbo repair, timely repairs) and the claimed
Yelp profile (4.6, 39 reviews; same hours; manager's text: diesel fuel
injection systems, rebuild and test pumps and injectors, turbochargers,
basic maintenance and engine diagnostics and repairs for fleets and
consumers; accepts credit cards).

- "Since 1951": an Alliant Power partner page gives 1951 and a 2026 Yelp
  reviewer says 75 years. Shown once, small. Owner must confirm.
- A Banks Power article lists a Colton address; MapQuest shows the Fontana
  listing as closed. Google and Yelp both show Fontana open with reviews
  from this year. Ask the owner about the move.
- A reviewer mentions a courtesy shuttle and Yelp lists a military
  discount; neither is promised on the page.
- Reviewers name staff; not used until the owner approves.
- No engine brands as claims of specialty, no prices, warranties, review
  quotes or listing photographs.
- No "Open now" badge (house style, docs/design-system/ui-changes-playbook.md).

## Deliberately avoided

Smoke stacks, flames, chrome type, piston icons, a sepia heritage look,
service cards.
