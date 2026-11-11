> **Superseded on 2026-11-10.** Andrew asked for every site to be rebuilt in the shared house style (see the root `DESIGN.md`, section "All lead sites rebuilt in the house style"). The notes below describe Vincent's original concept, which is still in git history (last commit before the rebuild: `e69ee8b`). Screenshots in this folder show the original.

# JC Bumper Repair & Auto Body — "Slide to fix"

Concept website for JC Bumper Repair & Auto Body, 16620 Ceres Ave Ste 6,
Fontana, CA 92335. Sales mockup, not the official site.

## Audience and job

Drivers with a cracked, scraped or hanging bumper who are paying out of
pocket. Reviews say the same thing over and over: other body shops quoted
too much, this one fixed or replaced the bumper for a fair price. They want
to know it can look right again and that it is worth a call. The page shows
a bumper going from cracked to fixed, lists what the shop does, and gives
the number.

## Three directions considered

1. **Slide to fix (selected).** The first screen is one drawn rear bumper in
   primer grey with a crack and a scrape. A slider wipes across it and
   leaves it painted and whole. The visitor does the repair with a thumb.

   ```
   +--------------------------------------------------+
   | JC Bumper Repair & Auto Body      (909) 349-0343 |
   | Cracked bumper? Slide.                           |
   | +----------------------------------------------+ |
   | |  painted, whole   ||   primer, cracked       | |
   | +-------------------||-------------------------+ |
   |   [=====o-------------------]  slider            |
   | [Call] [Directions]                              |
   +--[tape]------------------------------------------+
   | What we fix (wide list)        | hours (narrow)  |
   | Find us                        |                 |
   +--------------------------------------------------+
   ```
2. **Paint chip card.** A fan of colour swatches, "we match yours". Looks
   good, but colour matching is not something either listing states.
3. **Impact starburst.** Comic-book "crunch" graphics. The default for
   collision shops, and it celebrates the accident, not the repair.

Direction 1 wins because the shop's whole reputation is one outcome, a
bumper that looks right again, and this shows it without borrowing anyone's
before-and-after photographs.

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Paint blue | `#1c49b8` | repaired bumper, primary button (white text 7.6:1), links |
| Primer grey | `#9aa0a6` | damaged bumper; never text |
| Masking tape | `#e9d79a` | section labels drawn as torn tape strips; ink text 12:1 |
| Ink | `#14171c` | text |
| Booth white | `#f6f6f2` | page ground |

**Type**

One family: Archivo. Display at weight 800 with width 125 (expanded),
sentence case, h1 `clamp(44px, 7.6vw, 112px)`, line-height 0.95. Body
400/600 at normal width, 17–19px, line-height 1.55, max 60 characters.

**Layout**

Left-aligned, 1200px frame. Hero on booth white: headline, then the bumper
drawing full frame width, the slider directly under it, buttons under
that. Section headings sit on short strips of masking tape rotated one or
two degrees. "What we fix" is wide (7 columns); hours are narrow (5) and
start lower. Mobile: bumper stays full width, slider thumb 44px, hours
before the list, fixed call/directions bar.

**Signature**

The slide-to-fix bumper. Two stacked inline SVGs of the same bumper: grey
with a crack, scrape and one hanging corner underneath; blue and whole on
top, clipped by a CSS variable that a native `input type="range"` sets.
Starts at 35%. Labelled "Drag to repair the bumper"; the drawings are
`aria-hidden` and a sentence below says the same thing in words. Without
JavaScript the page shows the repaired bumper only.

**Motion**

None on load. The wipe follows the slider directly; nothing else moves.

**Accessibility**

Skip link, landmarks, one h1, native range input (keyboard arrows work),
3px focus outlines, 48px targets, real hours table with today's row marked
(America/Los_Angeles; plain table without JS).

## Content and limits

Sourced Nov 10, 2026: the claimed Yelp profile (4.9, 32 reviews; Ste 6;
Mon–Fri 9 AM–5 PM, Sat 10:30 AM–2 PM, Sun closed; services verified by the
business: bumper repair, collision repair, dent removal, chrome delete,
auto body restoration; customer shuttle and online appointments listed) and
Google Maps (4.7, 98 reviews; unclaimed; Mon–Fri 9–5:30, Sat 10–2;
(909) 349-0343; topics: bumper repair, affordability, crack repair).

- Hours differ. The page uses the owner-managed Yelp hours (the narrower
  ones) and says to call first.
- The sheet has no suite; Yelp says Ste 6. Another body shop is listed at
  16620 Ceres Ave #5. The page says Ste 6.
- Both sites carry a few one-star reviews, including a door alignment job
  in 2026. That is an owner conversation. The page promises no price, no
  turnaround and no insurance handling.
- Reviewers name staff; not used until the owner approves.
- No before-and-after photographs, review quotes, prices or warranties.
- No "Open now" badge (house style, docs/design-system/ui-changes-playbook.md).

## Deliberately avoided

Crash starbursts, wrench icons, glossy car renders, red (three recent
concepts already use it), service cards, an estimate form.
