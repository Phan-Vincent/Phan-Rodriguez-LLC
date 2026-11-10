# Phan-Rodriguez LLC

Web design for local Inland Empire businesses.

## leads/
`West_IE_No_Website_Leads.xlsx` lists 294 West Inland Empire businesses (Ontario, Rancho Cucamonga, Fontana, Upland, Chino, Pomona, Montclair) whose Google Maps listing has no website. They are ranked High, Medium or Low priority by rating and review count. The list was built Nov 8, 2026.

## mockups/
Concept websites for the top leads. Each is a single standalone `index.html`, styled after the business's real signage and Google Maps photos.

Live (GitHub Pages): https://phan-vincent.github.io/Phan-Rodriguez-LLC/

| Folder | Business | Location |
| --- | --- | --- |
| `el-rey/` | El Rey (Mexican restaurant) | Chino |
| `el-rey-retro-roadside/` | El Rey, alternate "Retro Roadside" concept (see its `DESIGN.md`) | Chino |
| `lockworx/` | Lockworx Locksmith Services | Fontana |
| `don-cortez-tires/` | Don Cortez Tire Shop | Fontana |
| `tri-auto/` | Tri Auto (Toyota, Honda and Lexus repair) | Chino |
| `ac-tires/` | A C Tires (tire shop) | Ontario |
| `morenos-auto-repair/` | Moreno's Auto Repair LLC | Ontario |
| `tepa-tire/` | Tepa Tire & Auto Care — Work Order | Ontario |
| `muffler-doctor/` | Muffler Doctor — Under the Lift | Montclair |
| `alejandros-tree-service/` | Alejandros Tree Service — Canopy Light | Rialto (Maps; lead-sheet area estimates Fontana) |
| `43s-mufflers-brakes/` | 43's Mufflers & Brakes — The Sign Out Front | Pomona |
| `sinaloa-tires/` | Sinaloa Tires — La Bandera | Pomona |
| `with-pride-auto-air/` | With Pride Auto Air Conditioning — Turn it to cold | Montclair |

These are mockups for sales pitches, not the businesses' official websites. Content comes from each business's public listings (Google Maps, Yelp excerpts, Facebook reviews, SureCritic). Review quotes name their source. Confirm services and hours with the owner before a site goes live.

The November 9 batch adds three local concepts. Each folder contains `DESIGN.md` with three creative directions and the recommended direction. Research and listing limitations are documented in `docs/lead-batch-2026-11-09/RESEARCH.md`; build order is in `RANKING.md`. The November 10 batch adds three more (43's Mufflers & Brakes, Sinaloa Tires, With Pride Auto Air Conditioning), each with its own `DESIGN.md`; research, build order and verification are in `docs/lead-batch-2026-11-10/BATCH.md`. The lead workbook tracks mockup existence separately from outreach status in columns L–Q. Local mockup paths do not imply publication to GitHub Pages.

## docs/ and tools/
- `docs/HANDOFF.md`: full project context (business data, sources, decisions, open items) for anyone, or any Claude session, picking this up.
- `docs/screenshots/`: contact sheets of the three auto shop concepts.
- `DESIGN.md`: design directions and system for the three auto shop concepts.
- `tools/auto-shop-generator/`: the script that builds those three sites.
