# Verification — November 9, 2026 Pacific

Follow-up: the November 10 [mobile review](MOBILE-REVIEW.md) found and repaired clipped review content and a 320px table-width issue missed by the original document-overflow check. Its broader geometry checks and mobile screenshots supersede the initial mobile-fit result below.

## Delivered scope

Three local standalone HTML concepts: Tepa Tire & Auto Care, Muffler Doctor and Alejandros Tree Service. Each has a DESIGN.md written before its HTML, with audience, three directions, recommendation, typography, palette, layout, signature and content boundaries. Integrated into the existing gallery and README. These remain noindex sales concepts, not owner-approved official sites.

## Browser checks performed

Served the repository locally at `http://127.0.0.1:8765/`. Supervisor used Playwright with installed Chrome, real external images and no image placeholders. Captured full-page and first-screen PNGs at **1440×1000** and **390×844** in each new site's `screenshots/` directory. Browser results are recorded in `browser-results.json`.

All six viewport checks: zero horizontal overflow, one h1, no broken internal fragment targets, no unnamed links, no missing images, no JavaScript page errors, correct telephone targets and noindex metadata. Reduced-motion checks found zero running animations. This is a focused accessibility check, not a comprehensive conformance certification.

At 390px, keyboard Tab reached each skip link. Each native mobile menu opened, its first section link navigated, and the menu closed afterward. No h1/h2/h3 had a wider scroll area than its visible area. See `interaction-results.json`. Mid-page and footer screenshots were also captured and inspected.

## Visual critique and changes

- **Tepa:** strong work-order hierarchy and self-contained tire diagram. Retained the ruled service document and mobile call-first composition. Disabled continuous marquee motion. Removed an unverified cross street and parking instruction from the schematic/location copy. Replaced lengthy implementation/disclaimer copy in the body with direct service and current-feedback language. Kept stock and concept disclosure in the footer.
- **Muffler Doctor:** initial desktop masthead at 272px pushed the phone action too low; reduced maximum to 222px and refreshed screenshots. The exhaust schematic remains the signature. Mobile uses a separate vertical route diagram. Simplified repetitive negative copy and used “Exhaust work. Fitted to your car.” as the offer. Primary phone/directions actions remain visible, with a fixed mobile bar and footer clearance.
- **Alejandros:** serif hierarchy and a tall canopy photograph provide a materially different visual identity. Inspected the 1440px split, mobile stacked composition, overlapping growth-ring illustration, lower green editorial section and final contact spread. Mobile body and footer remain clear of the fixed call strip. No hours or residential walk-in invitation were invented.

## Lead workbook and Google Sheet

294 records reconciled. Existing six businesses/seven concepts plus three new businesses = **nine covered businesses, ten concepts and 285 lead rows without a mockup**. Mockup existence is separate from outreach Status/Notes. Twelve recommended build-order entries; only the first three received fresh listing research. Other leads explicitly say their listing was not rechecked.

Added L–Q: Mockup exists, Mockup location, Build order, Build effort, Research notes, Last checked. Preserved A–K and the existing Summary formulas/values, all 294 Maps hyperlinks, original cell styles and original sheets. Expanded the local native Leads table to A1:Q295 so sorting does not detach tracking. Froze the identifying first two columns alongside the existing frozen header, and applied a matching filter to the live sheet. Dates are typed dates. Existing category counts still total 294.

Artifact Tool authored the added XLSX ranges and rendered previews. Its documented interface did not expose native-table resizing and its full export normalized some original style metadata. A bounded XML merge preserved the original workbook parts/styles while adding the authored cells, validation and conditional formatting and extending the table. Independent readback compared every original cell's value/formula and style, plus hyperlinks and table bounds. No original data cells changed. Excel desktop was not used for verification.

The existing native Google Sheet was edited in place, not replaced. All 294 row identities were checked against the local source before writing L:Q. Readback matched tracking values and counts. The sheet was inspected in its native browser at 100% zoom; paths, concise notes and dates fit. The first two columns stay visible while browsing tracking. No sharing settings changed.

## Remaining limits

Fresh Google Maps profiles and photographs were inspected. Yelp full profiles could not be inspected: search tool robots restrictions and a browser device check. Indexed Yelp evidence is explicitly distinguished from direct inspection; the candidate Alejandro’s Yelp identity is not confirmed. Stock imagery is labelled and no listing photographs were copied. Owner confirmation of services, hours/contact discrepancies, credentials and real imagery remains an official-launch task. Nothing in this batch was committed, pushed or deployed.
