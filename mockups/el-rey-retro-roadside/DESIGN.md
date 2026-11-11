> **Superseded on 2026-11-10.** Andrew asked for every site to be rebuilt in the shared house style (see the root `DESIGN.md`, section "All lead sites rebuilt in the house style"). The notes below describe Vincent's original concept, which is still in git history (last commit before the rebuild: `e69ee8b`). Screenshots in this folder show the original.

# El Rey de las Tortas — a stop worth making

## Audience and the page’s job
Hungry Chino locals and Riverside Drive commuters, often on a phone and often bilingual. Help them choose something to eat, check today’s hours, find the restaurant **inside the 7-Eleven**, and call or get directions. The secondary audience is the owner: this concept should demonstrate a memorable, useful restaurant identity without inventing a history or making operational promises.

The existing index.html is the factual source. Ratings and review counts are preserved snapshots, not a live feed. The Uber Eats URL is the existing generic homepage; this concept does not imply a verified restaurant ordering destination.

## Three creative directions

### Retro Roadside — recommended and built
A warm yellow field, forest-green lettering and tomato-red sign hardware make a compact roadside invitation. A carefully drawn Cubana replaces photography; the arrow sign earns the page’s one moment of motion. A painted menu board and a separate challenge ticket give food and appetite a clear hierarchy. It fits the supplied reference and a restaurant discovered on a busy road, while a practical location and hours section makes the visual pitch useful.

Palette: mustard, forest, tomato, cream, bread brown. Type: soft, heavy Fraunces with plain DM Sans. Layout: an asymmetric two-column opening, wide menu board, compact practical close.

```text
[El Rey]                   [Menu  Visit  Call]
[Worth the]           [arrow >                ]
[stop. + actions]        [illustrated Cubana   ]
================ checker ====================
[Pull up hungry.                             ]
[ TORTAS / CUBANA       | tacos, burritos      ]
[ weekend barbacoa      | drinks              ]
[             El Reto challenge ticket        ]
[voices / rating]       [address | hours       ]
```

Risk: nostalgia can become costume. Keep ornament purposeful: the arrow, food illustration, one checker seam, a single headline brush stroke, a single-ink flag row and the challenge ticket. Keep practical information straightforward.

### La Mesa — the everyday neighborhood table
A quiet cream page with dark brown type, hand-drawn green salsa bowls and a few tomato-red rules. A broad editorial menu, generous margins and conversational bilingual copy evoke a well-used printed takeout menu. Illustration would focus on a shared tabletop rather than a monumental sandwich. This direction gives the owner a calm, credible identity with less spectacle.

Palette: cream #FFF5DE, dark brown #3B281F, herb #28543C, brick #A83525. Type: Libre Baskerville headings and DM Sans body. Layout: left-aligned reading column with a wide illustrated tabletop interrupting the menu.

```text
[El Rey]                      [Call  Directions]
[Your next lunch stop.         | address        ]
[------------- shared tabletop ---------------]
[Tortas                     | rest of menu     ]
[weekends                   | hours            ]
[review quote / accessibility                  ]
```

Risk: quieter food illustration and typography may not have enough roadside energy or match the supplied reference closely enough.

### The Counter Window — urban painted lettering
A cream-and-black typographic storefront with one saturated red panel. Oversized condensed headings, thick horizontal rules and a small cutaway sandwich create the feel of ordering at a counter. The menu reads almost like a broadside; the challenge becomes a detachable coupon. This is direct and efficient for repeat visitors, with the phone and location occupying a persistent utility rail.

Palette: cream #FFF5DE, ink #242D22, tomato #B72F1E, ochre #F6CB62. Type: Barlow Condensed black and DM Sans. Layout: strong horizontal strips with an offset desktop utility column.

```text
[EL REY DE LAS TORTAS            | Call         ]
[big type / cutaway torta        | Directions   ]
[TORTAS ---------------------------------------]
[tacos / burritos / drinks       | hours        ]
[challenge coupon] [weekend notice             ]
```

Risk: a hard utility rail can feel industrial and squeeze the mobile menu. It also offers less warmth than the reference. Retro Roadside is the stronger fit.

## Built direction: visual system

### Palette and contrast
| Token | Hex | Role and contrast |
| --- | --- | --- |
| Mustard | #F6CB62 | Hero field and bulbs; forest text is about 7.89:1. |
| Forest | #123D2B | Primary text, menu field, footer; cream text is about 11.21:1. |
| Tomato | #B72F1E | Buttons, basket, challenge ticket; cream text is about 5.63:1. Never small red text on mustard (about 3.97:1). |
| Cream | #FFF5DE | Reading surface, paper and reversed type. |
| Ink | #242D22 | Bread outlines and illustration details; cream pairing about 13.14:1. |
| Bread | #C47A35 | Illustration only; never information-bearing text. |
| Lettuce | #59913C | Added food ink: ruffled lettuce, salsa herbs and lime rind; no text. |
| Avocado | #DADD86 | Added food ink: avocado flesh, cheese and lime; no text. |

The six core inks remain unchanged. Exactly two food-only inks are added: lettuce and avocado/cheese. Illustration uses solid fills, patterns and negative space. No gradients. Decorative food texture need not carry text contrast. Focus uses an offset forest outline on light fields and a mustard outline on dark fields.

### Typography
Fraunces at 700–900 with its soft, full shapes provides a Cooper-like friendliness without imitating a commercial logo. DM Sans at 400–700 handles directions, descriptions, navigation and hours. System Georgia and Arial fallbacks preserve readable content when Google Fonts cannot load.

| Role | Size / line height |
| --- | --- |
| Hero h1 | clamp(76px, 8.7vw, 126px) / .91 |
| Section heading | clamp(42px, 5.2vw, 76px) / 1.02 |
| Menu Cubana | clamp(54px, 7.5vw, 108px) / .95; mobile clamp(52px, 16vw, 90px) |
| Challenge payoff | clamp(68px, 8vw, 112px) / 1; mobile clamp(46px, 14vw, 68px) |
| Subheading | clamp(25px, 2.7vw, 34px) / 1.12 |
| Body | 16px / 1.6; hero intro 18px |
| Utility | 13–14px / 1.5 |

Sentence case for editorial headings and actions. The brand’s painted capitals are a single identity treatment. No repeated eyebrow labels or decorative letter spacing.

### Layout and spacing
Maximum content width 1240px with 40px desktop gutters and 22px mobile gutters. Base spacing scale: 4, 8, 12, 16, 24, 32, 48, 64, 88px. Text aligns left; shared rules tie the menu’s columns together. The hero is intentionally 44/56, with the basket extending about 55px beyond the right content edge. A 650px bracket-mounted arrow bridges the columns above the food, roughly 2.5 times the previous sign width. It has a hard forest-ink offset silhouette, rather than a soft shadow. Menu typography assigns most weight to tortas; other dishes use subordinate ruled rows, not cards.

At 700px and below, the hero is recomposed: location, headline, large sign, illustration, supporting copy, actions. At 390px the sign is 340px wide before rotation (87% of the viewport), comfortably above the 55% minimum. The caption has positive spacing below the entire food SVG, with no negative margin. The illustration has its own portrait reading moment. The bottom action bar always exposes Call and Directions; safe-area padding and extra footer clearance keep content clear. The menu follows an intentional reading sequence from tortas to tacos, burritos, weekends and drinks. Hours remain a real two-column table.

### The one signature element
A bracket-mounted tomato marquee arrow with a forest edge, cream keyline, hard offset shadow, “Tortas” lettering and 35 chasing bulbs around its full border points directly at the torta. It is the only automatically animated object. The basket, checked paper, sandwich and lettering stay static; no other component competes for motion. The two halves now show golden, flour-scored telera, ruffled fresh lettuce, rounded tomato slices, avocado crescents, a continuous crumb-textured milanesa layer, folded ham and melted cheese. These requested illustration details are not presented as a verified ingredient list in the menu copy.

### Painted menu, challenge ticket and character section
The torta panel now has a full-width tomato stripe with cream “Tortas, first.” lettering, larger Cubana typography and a related whole-torta spot illustration. On desktop the spot sits alongside the supporting copy; on mobile it has its own space beneath the title. Other menu categories retain their subordinate ruled hierarchy.

El Reto is a substantial tomato ticket, rotated -1.5 degrees on desktop, with concave end notches and a dashed perforation separating a stub reading “2 Tortas Cubanas / 1 persona”. “No pagas.” is the dominant payoff; the full challenge rule and unchanged Spanish flyer quote remain below it. It is the second-loudest designed object after the marquee. At narrow widths it is unrotated and the stub moves above the payoff, which fits on one line at 390px.

A static, single-ink papel-picado row spans the top of the character section. A smaller, more compact heading and vertically centered text rebalance its lower half without adding copy. No real crests or logos are drawn.

The hero adds tomato only to the primary menu button and one SVG brush-stroke path below the whole “the stop.” line. Existing food and sign inks remain; no new red hero decoration is introduced. Cream text on the tomato button is approximately 5.63:1, meeting AA.

### Motion policy
Only bulb fill changes, in a slow 2.4-second sequence with staggered phases. No flashes, moving text, scrolling tickers, entrance effects or automatic transforms. Under `prefers-reduced-motion: reduce`, animation is removed and every bulb remains lit. Link feedback uses underline or color, without movement.

### Accessibility and behavior
Semantic header, nav, main, sections and footer; skip link; one h1. The food SVG has a title and description, while the marquee and repeated ornament are decorative. No color-only information: today also has a text label, and open/closed status has words. Every interactive target is at least 44px tall. Focus rings are visible on light and dark surfaces. Spanish phrases carry `lang="es"`. Links retain the original phone, Maps and Uber Eats destinations.

Hours are calculated in `America/Los_Angeles`, with 7 AM opening, 10 PM closing Sunday–Thursday and 11 PM Friday–Saturday. The display refreshes every minute; closing time is exclusive. Without JS, the weekly table and a clear local-time fallback remain useful. The concept disclaimer and search-engine noindex/nofollow stay visible/present. No form, tracking, ordering backend or verified live review feed is implied.

### What we deliberately avoided
- Fictional founding stories, prices, ingredients as menu promises, or live claims about reviews.
- Photographs, borrowed logos, team crests or generic cartoon mascots.
- Equal menu-card grids, soft shadows, decorative gradients and glass effects.
- Repeated labels, decorative counters, mixed-color headline words and button arrows.
- Animation beyond the sign bulbs or essential information that requires JavaScript.

## Verification
Rendered and visually inspected full-page Chrome screenshots at 1440px and 390px in `screenshots/`. After the creative-director review, redrew the food and sign and strengthened the menu/ticket composition. Inspected both refreshed full-page renders plus exact 1440×900 and 390×844 crops (`1440-fold.png`, `390-fold.png`). Corrected clipped flag artwork and a cramped mobile payoff wrap during this pass. Both target widths have matching viewport/document widths and no overflowing elements. All visible mobile links have targets at least 44px high; the bottom actions are 48px. Browser checks confirm zero animations with reduced motion and all 35 bulbs lit. With JavaScript disabled, seven hours rows and the weekly-hours fallback remain visible. Ten deterministic time cases cover opening/closing boundaries, Friday/Saturday, summer offset and the daylight-saving transition. Original external destination sets, key facts, menu items and exact review quotes were checked; HTML nesting and one h1 were checked. Text palette contrasts are listed above. Revised HTML is about 35 KB, below the 60 KB limit.

Reasonix Flash was attempted for implementation but the tool call timed out without artifacts. The task’s process group was stopped and its exit verified before supervisor implementation. No commit, push or deployment.

The creative-director revisions were implemented and checked directly by the supervisor, with no delegation.

Final measured revision: 650px nominal sign width on desktop (678px rotated bounding box), 340px nominal / 349px rotated at 390px; 10px caption clearance at both sizes. Document scroll width equals 1440px and 390px respectively. Crops are exactly 1440×900 and 390×844. Only the `chase` animation runs, on 35 sign bulbs. Final HTML is 34,617 bytes. No recipe claims were added to visible menu copy; all original destinations, hours and exact review quotations remain unchanged.
