# Mobile review — November 10, 2026

Scope: the three new concepts, Tepa Tire, Muffler Doctor and Alejandros Tree Service. Existing workbook and outreach data were not changed.

## Defects found and repaired

- Muffler Doctor's review-count label inherited the giant rating font because a descendant selector matched both bold elements. Its intrinsic width expanded the grid and clipped review content on phones. Restricted the display styling to the rating's direct child, used valid block markup for the label, allowed metadata to wrap, and removed the grid's implicit minimum width.
- Auto-shop menu links previously landed section starts under the sticky headers. Added header clearance to scroll positioning.
- Tepa's hours table expanded the actual touch viewport beyond a 320px screen, despite a zero document-overflow reading. Shortened hour formatting without changing hours, tightened narrow-screen cell padding, and let the visit grid shrink correctly.
- Kept Tepa's primary phone number on one line and made the compact call button fit narrow phones.
- Added safe-area bottom padding and matching page clearance to Muffler Doctor's fixed call bar. Reduced header gaps on narrow phones.
- Made the two sticky-header menus scroll within short landscape screens. Matched Alejandro’s page-bottom clearance to its call bar’s safe-area padding; its static header and visual composition were retained.

## Verification

`tools/mobile-qa.mjs` checks touch-enabled Chrome at 320×740, 360×800, 390×844, 430×932, 768×1024 and 844×390: 18 site/viewport combinations. It measures requested versus actual viewport width, visible content bounds (including content clipped by a parent), image loading, JavaScript errors, menu open/close behavior and anchor clearance. Raw results are in `mobile-audit.json`.

Updated full-page and first-screen screenshots for 320px, 390px and 430px are saved inside each site's `screenshots/` directory as `mobile-<width>.png` and `mobile-<width>-fold.png`. Muffler Doctor also has `mobile-review-section.png` documenting the repaired rating section.

The broader checks supersede the earlier narrow overflow-only result: hiding overflow does not prove that content fits. Browser checks are Chrome emulation, not physical iPhone/Android tests. The WebKit browser engine is not installed, so no Safari verification is claimed. Safe-area support is implemented in CSS; emulated Chrome supplies a zero inset.

Final result: all 18 combinations passed, with no expanded viewport, clipped text/content, missing images or JavaScript errors. All tested mobile menus closed after navigation and section starts cleared sticky headers. The footer clears both fixed call bars. The last 320px Tepa check also captured the hours table after shortening its time labels.

## Delegation

An optional read-only Reasonix Flash review (`mobile-review-20261110`) timed out after its bounded 120-second run without returning findings. The tool confirmed its owned process group stopped and pipes drained. No retry or escalation was launched. All accepted findings and fixes came from supervisor source inspection and direct browser checks.

No commit, push or deployment was performed.
