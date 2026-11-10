# Sinaloa Tires — "La Bandera"

Concept website for Sinaloa Tires, 1542 S Garey Ave, Pomona, CA 91766.
Sales mockup, not the official site.

## Audience and job

South Pomona drivers, many Spanish-speaking, with a nail in a tire, a bald set to
replace on a budget, or a check-engine light. They want to know three things fast:
is it open (it is, seven days), do they have used tires (yes), and where exactly
is it — the top Google review says the shop sits in the back and is hard to see
from the street. The page answers those in that order and gets them to call or
navigate.

## Three directions considered

1. **La Bandera (selected).** The thing you actually see from Garey Ave is the
   tall orange feather flag with a checkered tail. The page hangs that flag down
   its left edge for the full scroll and sets everything else against open sky
   blue and white stucco, like the lot on a clear day. Bilingual headings.

   ```
   +----+---------------------------------------------+
   | F  |  Sinaloa Tires            open today 8–7    |
   | L  |  Used and new tires.      [Call] [Directions]|
   | A  |  Llantas usadas y nuevas.                   |
   | G  +---------------------------------------------+
   |    |  Find us: we're in the back  (site sketch)  |
   | ▚▚ |  What we do      | Free: air, engine scan   |
   +----+---------------------------------------------+
   ```
2. **Tread catalogue.** Black rubber textures, tread patterns as section
   dividers, a tire-size finder. Looks like a national chain, needs inventory
   data we do not have, and A C Tires and Tepa already lean on tire drawings.
3. **Mercado poster.** Hand-lettered rotulo style, hot pink and lime, papel
   picado. Lively, but it borrows a restaurant and market vernacular for a tire
   shop and trades on the name rather than the business.

Direction 1 wins because the flag is the shop's own wayfinding device and the
hardest problem in the reviews is finding the place.

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Flag orange | `#e8530e` | the flag, primary buttons (white text 3.6:1, so button text is 20px bold; black text 5.8:1 elsewhere) |
| Lot sky | `#1f6fd0` | hero and find-us fields; white text 4.9:1 |
| Stucco white | `#fbfaf6` | page ground |
| Asphalt | `#22252a` | text (15:1 on stucco), footer |
| Caution yellow | `#ffd21f` | "open now" chip, today row; asphalt text 11:1 |
| Checker | asphalt + stucco squares | flag tail, one divider |

**Type**

Archivo variable, using its width axis instead of a second family.

- Display: Archivo 800 at width 125 (expanded), `clamp(44px, 8.2vw, 128px)`,
  line-height 0.92, sentence case.
- Flag lettering: Archivo 900 at width 62 (condensed), vertical, uppercase
  because the real flag is.
- Body: Archivo 400/600 at width 100, 17–18px, line-height 1.55.
- Spanish lines are set in the same size as English at weight 500, marked
  `lang="es"`, never smaller or greyed.

**Layout**

Left-aligned. Desktop: a fixed 112px flag column on the left edge, content in a
1180px frame beside it on a 12-column grid; sections alternate sky and stucco
and are deliberately unequal in height. Mobile: the flag turns into a 56px
horizontal banner pinned under the header with the checker at its right end;
content is a single column with a fixed call/directions bar.

**Signature**

The feather flag: an inline SVG with a curved leading edge. It reads `USED TIRES`
then `LLANTAS USADAS` as two stacked vertical blocks, with a checkered tail below. It sways a few
degrees from its pole, slowly (the only ambient motion). Second, functional
drawing: a "we're in the back" site sketch — Garey Ave, the driveway, the
building at the rear with a pin — labelled as a sketch, not to scale, with no
cross streets or neighbours named.

**Motion**

Flag sway only (6s ease-in-out, 3 degrees). Off under reduced motion.

**Accessibility**

Skip link, landmarks, one h1, hours as a real table with today's row marked and
an open/closed line (America/Los_Angeles, works without JS as a plain table),
3px focus outlines, 48px targets, SVGs with role="img" and descriptions.

## Content and limits

Sourced Nov 10, 2026: Google Maps (4.3, 161 reviews; Mon–Fri 8–7, Sat 8–6,
Sun 8–3; (909) 620-1199; review topics: flat tire repair, used tires, brakes,
cash only) and the claimed Yelp profile (same hours; business description:
tires to engine swaps, free air, free check-engine scan, used tires; services
include balancing, installation, TPMS repair, tire repair, rotation).

- Payment: Google reviewers say cash or Zelle; Yelp says cards accepted. The
  page says "Bring cash or Zelle — ask about cards when you call."
- "Lowest prices in the Inland Empire" is the owner's Yelp wording and is not
  repeated as fact.
- Yelp's rating (3.6, 31 reviews) is not shown, and recent Yelp complaints
  about a used-car sale are an owner conversation, not page content. The page
  does not mention vehicle sales.
- No prices, brands, stock counts, warranties or review quotes. No listing
  photographs.

## Deliberately avoided

Tread-pattern dividers, tire icons in circles, a size-finder form, three equal
service cards, a Mexican-flag palette, stock photos of wheels.
