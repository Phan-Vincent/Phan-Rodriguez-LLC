# With Pride Auto Air Conditioning — "Turn it to cold"

Concept website for With Pride Auto Air Conditioning, 5438 Holt Blvd Unit F3,
Montclair, CA 91763. Sales mockup, not the official site.

## Audience and job

Inland Empire drivers whose A/C blows warm, plus classic-car owners (reviews
mention gauges, radiators, fans and "best A/C shop for classics"). They have
often been quoted a large repair elsewhere and are looking for someone who will
diagnose before selling. The word that repeats across both review sites is
honest. The page's job: say what the shop fixes, show it is a long-running
family shop run by Eddie and Elaine, and get a call.

## Three directions considered

1. **Turn it to cold (selected).** The page is a dashboard climate panel. A
   single temperature slider sits in the hero; drag it and the whole page moves
   from the shop's building red to cold blue. It is the feeling the customer is
   paying for, delivered as an interaction. Type is the wide technical face
   found on gauge clusters of the cars in the shop's photos.

   ```
   +---------------------------------------------------+
   | With Pride Auto Air Conditioning        Call      |
   |                                                   |
   | Your A/C should                 ||||||||  vents   |
   | be cold.                        ||||||||          |
   | [ hot ●--------------------- cold ]   <- slider   |
   +----------------------+----------------------------+
   | what we fix (list)   | Eddie & Elaine, 40+ years  |
   +----------------------+----------------------------+
   ```
2. **Red barn.** Build the page out of the shop's red arched building and white
   chevron mark: big red field, white arch shapes, retro service-station type.
   Recognisable, but red-hot is the wrong temperature for an A/C page.
3. **Service bulletin.** A technical bulletin with a refrigerant-circuit diagram
   (compressor, condenser, drier, expansion valve, evaporator). Credible, but
   it is the same idea as Muffler Doctor's schematic and it explains the system
   rather than selling the relief.

Direction 1 wins: it is the only one that is about cold air, and it keeps the
building red as the "before".

## System

**Palette**

| Name | Hex | Role |
| --- | --- | --- |
| Building red | `#c22a1e` | hot end of the slider; page ground at "hot" |
| Cold blue | `#0b4f7a` | cold end; page ground at "cold"; white text 8.6:1 |
| Frost | `#e6f3f8` | light sections, vent highlights |
| Gauge white | `#ffffff` | type on the coloured ground |
| Dash black | `#101418` | vent housing, text on frost (17:1) |
| Needle amber | `#ffb000` | focus ring, slider thumb mark, today's row |

The hero ground is `color-mix(in oklab, red, blue var(--t))`. White text passes
AA at every position of the slider (lowest contrast 5.1:1 at the red end).

**Type**

- Display and numerals: Michroma (wide, Eurostile-like gauge lettering),
  sentence case, `clamp(34px, 5.6vw, 84px)`, line-height 1.08. Used for the h1,
  section heads and the hours figures only.
- Body: Hanken Grotesk 400/600, 17–18px, line-height 1.6, max 64 characters.

**Layout**

Left-aligned. 1240px frame. Hero is a 7/5 split: statement and slider left,
dashboard vent right, vent bleeding off the right edge. Below, a frost section
with a two-column unequal list (A/C work wide, cooling and gauges narrow), then
a dark "about the shop" band, then visit and hours. Mobile: statement, slider,
then a half-height vent; fixed call/directions bar.

**Signature**

The temperature slider. A native `input type="range"` styled as a dash lever,
labelled "Cabin temperature", hot on the left, cold on the right. It drives one
custom property; the ground colour, the vent's airflow lines and the hero
sentence ("Right now it's blowing hot." → "That's better.") follow it.

**Motion**

One orchestrated moment: after load the lever travels from hot to cold by
itself once (1.6s) so nobody misses that it moves. Airflow lines from the vent
drift only while the setting is on the cold half. Under reduced motion the page
loads cold and still; the slider still works.

**Accessibility**

Native range input with visible label and `aria-valuetext` ("hot", "warm",
"cool", "cold"); amber 3px focus ring; skip link; one h1; real hours table with
today marked and an open/closed line (America/Los_Angeles); the page is
complete and readable at any slider position and without JS (defaults to cold).

## Content and limits

Sourced Nov 10, 2026: Google Maps (4.7, 97 reviews; Mon–Fri 8–5, Sat 9–3, Sun
closed; (909) 391-4894; topics: leak repair, A/C compressor repair, fair
pricing, no upselling) and the claimed Yelp profile (same hours; owner text:
over 40 years serving the Inland Empire, Eddie and Elaine, family business;
services: auto HVAC repair, routine maintenance).

- "Over 40 years" and the names Eddie and Elaine come from the owner's own Yelp
  description, so the page attributes them to the shop. A Google post on the
  listing says 45+ years and price match with a written estimate; because the
  two figures differ, the page says "more than 40 years" and leaves price match
  out until the owner confirms.
- No temperatures, refrigerant types, prices, warranty terms or review quotes.
  One Yelp reviewer mentions a warranty; unverified, so omitted.
- Yelp has mixed reviews (4.4); the page shows the Google snapshot with a link
  and does not claim a perfect record.
- No listing photographs. The vent and lever are drawn in CSS/SVG.

## Deliberately avoided

Snowflake icons, a blue-to-purple gradient, frosted glass panels, a refrigerant
diagram, stock photos of dashboards, numbered process steps, service cards.
