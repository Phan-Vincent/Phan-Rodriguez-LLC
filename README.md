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
| `ac-tires/` | A C Tires (tire shop) | Ontario |
| `tepa-tire/` | Tepa Tire & Auto Care — Work Order | Ontario |
| `alejandros-tree-service/` | Alejandros Tree Service — Canopy Light | Rialto (Maps; lead-sheet area estimates Fontana) |
| `43s-mufflers-brakes/` | 43's Mufflers & Brakes — The Sign Out Front | Pomona |
| `sinaloa-tires/` | Sinaloa Tires — La Bandera | Pomona |
| `with-pride-auto-air/` | With Pride Auto Air Conditioning — Turn it to cold | Montclair |
| `king-tire-shop/` | King Tire Shop — Till nine | Montclair |
| `jc-auto-electric/` | J C Auto Electric — Find the fuse | Montclair |
| `performance-lube-oil/` | Performance Lube & Oil — Oil in, car washed | Chino |
| `toy-shop-transmissions/` | Toy Shop Transmissions — Back in drive | Pomona |
| `diesel-injection-service/` | Diesel Injection Service — Bring the part or bring the truck | Fontana |
| `jc-bumper-repair/` | JC Bumper Repair & Auto Body — Slide to fix | Fontana |
| `county-brake-alignment/` | County Brake, Alignment & Mufflers Plus | Montclair |
| `hocks-japanese-car-specialists/` | Hock's Japanese Car Specialists | Pomona |
| `j-s-auto-center-smog/` | J & S Auto Center & Smog | Fontana |
| `basic-auto-repair/` | Basic Auto Repair | Ontario |
| `a-tech-automotive/` | A Tech Automotive | Chino |
| `johns-auto-repair/` | John's Auto Repair | Fontana |
| `ceres-collision/` | Ceres Collision | Fontana |
| `freddies-auto-repair/` | Freddie's Auto Repair | Pomona |
| `bates-auto-service/` | Bates Auto Service | Upland |
| `express-transmissions/` | Express Transmissions | Pomona |
| `menas-brake-suspension/` | Menas Brake & Suspension | Ontario |
| `the-auto-clinic/` | The Auto Clinic | Chino |
| `auto-technik-carcare/` | Auto Technik Carcare | Chino |
| `diamond-auto-center/` | Diamond Auto Center | Ontario |
| `claremont-auto-care/` | Claremont Auto Care | Pomona |
| `l-r-auto-repair/` | L & R Auto Repair | Ontario |
| `baja-auto-center/` | Baja Auto Center Smog & Lamp | Ontario |
| `ie-automotive/` | I.E Automotive | Ontario |
| `v-tech-auto-care/` | V Tech Auto Care | Pomona |
| `prime-truck-trailer-repair/` | Prime Truck and Trailer Repair | Fontana |
| `mailos-auto-repair/` | Mailo's Auto Repair | Fontana |
| `bee-z-auto-care/` | Bee Z Auto Care | Upland |
| `quality-auto-complete-auto-repair/` | Quality Auto Complete Auto Repair | Rancho Cucamonga |

These are mockups for sales pitches, not the businesses' official websites. Content comes from each business's public listings (Google Maps, Yelp excerpts, Facebook reviews, SureCritic). Review quotes name their source. Confirm services and hours with the owner before a site goes live.

The November 9 batch adds three local concepts. Each folder contains `DESIGN.md` with three creative directions and the recommended direction. Research and listing limitations are documented in `docs/lead-batch-2026-11-09/RESEARCH.md`; build order is in `RANKING.md`. The November 10 batch adds three more (43's Mufflers & Brakes, Sinaloa Tires, With Pride Auto Air Conditioning), each with its own `DESIGN.md`; research, build order and verification are in `docs/lead-batch-2026-11-10/BATCH.md`. A second November 10 batch adds King Tire Shop, J C Auto Electric and Performance Lube & Oil; see `docs/lead-batch-2026-11-10/BATCH-2.md`. The lead workbook tracks mockup existence separately from outreach status in columns L–Q. Local mockup paths do not imply publication to GitHub Pages. A third batch the same day (Toy Shop Transmissions, Diesel Injection Service, JC Bumper Repair & Auto Body) is recorded in `docs/lead-batch-2026-11-10/BATCH-3.md`. A fourth batch (County Brake, Hock's, J & S) was added through `tools/auto-shop-generator/build_leads.py` in the house style; see `docs/lead-batch-2026-11-10/BATCH-4.md`. A fifth batch (Mailo's, Bee Z, Quality Auto) was added the same way; see `BATCH-5.md` in the same folder. `leads/google-sheet-paste-L2.tsv` holds the mockup columns for pasting into the Google Sheet at cell L2.

## docs/ and tools/
- `docs/HANDOFF.md`: full project context (business data, sources, decisions, open items) for anyone, or any Claude session, picking this up.
- `docs/screenshots/`: contact sheets of the three auto shop concepts.
- `DESIGN.md`: design directions and system for the three auto shop concepts.
- `tools/auto-shop-generator/`: the script that builds those three sites.

- `docs/design-system/`: Astryx (Meta, MIT) token values and design rules we borrow, plus our UI changes playbook.
