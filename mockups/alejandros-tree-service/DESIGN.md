> **Superseded on 2026-11-10.** Andrew asked for every site to be rebuilt in the shared house style (see the root `DESIGN.md`, section "All lead sites rebuilt in the house style"). The notes below describe Vincent's original concept, which is still in git history (last commit before the rebuild: `e69ee8b`). Screenshots in this folder show the original.

# Alejandros Tree Service — Canopy Light

## Audience and purpose

Homeowners considering palm trimming, tree trimming or removal. They need a calm, clear way to discuss a real tree and their property. The page converts to a phone call, not a visit to the listed residential-looking address or a fabricated online appointment.

## Three creative directions

1. **Canopy Light — recommended and selected.** Warm paper, deep forest green, large editorial serif, tall canopy photography and a fine tree-ring illustration. The residential scale of the Maps photograph (climber among palms beside a home) becomes an identity about space and care. This gives the portfolio a quiet, organic counterpoint to its automotive pages.
2. **Crew & Chipper.** High-visibility orange, dark equipment green, bold sans-serif and documentary work sequences. A useful direction once rights-cleared crew/truck photographs exist, but stock equipment would risk inventing the business's capabilities.
3. **Neighborhood Field Guide.** Cream/black botanical plates, scientific labels and an annotated service directory. Distinctive and informative, but too instructional for a homeowner who wants a conversation about one tree.

## Visual system

- Identity: a new typographic concept, not an assertion of the business's existing logo.
- Typography: Georgia serif display, normal 400 weight, italic emphasis; Helvetica Neue/Arial body; compact Menlo metadata. Desktop hero up to 112px; mobile 64px; body 17–18px. Type and spacing carry hierarchy, with no decorative icon grid.
- Palette: paper `#f4f1e8`, forest `#173e31`, muted green `#536657`, lime `#dce6b4`, line `#c6ccbd`. Forest on paper and paper on forest have strong reading contrast; pale lime is used as a background, not low-contrast text.
- Layout: 1320px maximum, 60px desktop side margins; hero 52/48 asymmetric editorial split. The image stands taller than the introductory copy, with a tree-ring seal over its lower edge. Service section is a ruled list; contact is a large green spread.
- Mobile: 20px side margins; copy and primary call action precede the photograph; services stack label/description within each row. Header uses a native details menu; mobile bottom call strip has safe-area padding and corresponding body clearance. At 390px, headings wrap deliberately without shrinking the body copy.
- Signature: thin concentric growth rings with an intentionally irregular outer contour. They refer to the actual subject, not a generic decorative badge. Text remains HTML outside the illustration.
- Motion: a single 650ms entrance; no endless marquees, parallax, animation loops or hidden-on-scroll content. Reduced motion disables it entirely.
- Accessibility: one h1, landmarks, skip link, visible focus, labelled native navigation, decorative SVG hidden, descriptive stock-photo alt text and explicit caption, working telephone links.

## Evidence and content boundaries

Supervisor inspected Google Maps on November 9, 2026 Pacific: Alejandros Tree Service, (909) 694-8945, 4.8 / 188 reviews. Maps address is 1073 N Sandalwood Ave, **Rialto CA 92376**, whereas the lead sheet estimates Fontana. The page uses Rialto and asks callers to discuss their location. No walk-in invitation or service-radius claim.

Maps has no hours. The page says call for availability and makes no 24-hour/emergency claim. Review topics support trimming, palms, removal and cleanup. Exact scope is a phone discussion; licensing, insurance, certification, years in business, warranties and free estimates are not established and are not advertised. No direct review quotes.

Yelp research found a candidate Fontana profile in Google snippets, but matching phone/address was not established and the names mentioned differ. Do not combine its rating/reviews with this business. Full Yelp access is restricted. See [research notes](../../docs/lead-batch-2026-11-09/RESEARCH.md).

Stock canopy photo: `https://images.unsplash.com/photo-1518495973542-4542c06a5843`, regular Unsplash image. Label it as illustrative stock, never actual crew work. No Maps/Yelp photographs copied. Obtain real owner-approved photographs before an official launch.

## Reference use and verification

Existing repository desktop/mobile screenshots informed clear hierarchy and phone visibility, not the layout or visual identity. Unlike the automotive concepts, this page uses serif typography, quiet spacing and a photographic editorial composition.

Browser verification and resulting adjustments are recorded in the batch VERIFICATION.md; this design document was written before HTML implementation.

## Mobile review — November 10, 2026

Retained the phone composition and matched page-bottom padding to the fixed call bar including the safe-area inset. Checked in touch-enabled Chrome at widths 320, 360, 390, 430, 768, plus 844×390 landscape. See ../../docs/lead-batch-2026-11-09/MOBILE-REVIEW.md for results and limits.
