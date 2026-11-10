# Astryx reference for Phan-Rodriguez LLC sites

Source: [meta/astryx](https://github.com/meta/astryx), Meta's open source design system (beta), MIT License. Read at commit `3505a30` on 2026-11-10. License text: `ASTRYX-LICENSE.txt`.

## What we took and what we did not

Astryx is a React 19 + StyleX component library. Our mockups are plain HTML and CSS with no build step, so its components cannot be dropped in. What carries over:

- **Tokens:** all 211 default token values, in `astryx-tokens.css` (color, spacing, radius, shadow, motion, type).
- **Design rules:** summarized below from `docs/design/` in the Astryx repo. Those records are marked draft upstream.
- **Component inventory:** a checklist of the 107 component folders in `packages/core/src`, for naming and for deciding what a page needs.

Not copied: component source code, the seven theme packages (neutral, butter, chocolate, matcha, stone, gothic, y2k), the CLI, charts. If a client project ever becomes a React app, install `@astryxdesign/core` instead of hand-copying.

## Token cheat sheet

| Group | Values |
| --- | --- |
| Spacing | 4px base: 2, 4, 6, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48px |
| Radius by role | inner 4px, element 8px, container 12px, page 28px, full 9999px |
| Control height | 28, 32, 36px |
| Border and focus | 1px border; focus ring 2px solid accent, 3px offset |
| Shadow | low `0 1px 1px, 0 2px 8px`; med `0 1px 2px, 0 2px 12px`; high `0 2px 2px, 0 8px 24px`; all black at 10% in light mode |
| Duration | fast 175ms, medium 410ms, slow 975ms; exits use fast |
| Easing | standard, entrance and move `cubic-bezier(.24,1,.4,1)`; exit `cubic-bezier(.3,0,.6,.6)` |
| Type scale | 14px base, 1.2 ratio: 10, 12, 14, 17, 20, 24, 29, 35, 42px |
| Type weights | 400 body, 500 labels, 600 headings and titles, 700 strong emphasis |
| Type roles | body 14/20; label 14/20 medium; supporting 12/20; headings 24, 20, 17, 14 semibold; display 42, 35, 29 regular |
| Neutral colors (light) | body `#F1F4F7`, surface `#FFFFFF`, text `#0A1317`, secondary text `#4E606F`, border `#CCD3DB`, accent `#0064E0` |
| Status (light) | success `#0D8626`, error `#E3193B`, warning `#E9AF08`, info `#0064E0` |

Astryx sizes are tuned for dense app screens. Our pages are marketing sites, so we keep its ratios and roles but scale up: body 17px, headings 32 to 88px, card radius 24 to 32px.

## Design rules we follow

1. **Type roles.** Pick a text role by its job (page heading, section heading, body, label, supporting). Neighboring roles must look clearly different in size or weight. Body text keeps roomy line height.
2. **Spacing shows grouping.** Related things sit closer; gaps grow from item to group to section. Use space and alignment before adding another box.
3. **Radius follows role.** Small radius for inner parts, larger for containers, largest for page panels, full for pills. A rounded shape inside another should look parallel to it (inner radius is roughly outer radius minus the gap). Accent borders follow the curve.
4. **Quiet depth.** Shadows are soft and low. A surface uses either a border or a shadow as its main edge, not both at full strength. Focus rings are not shadows.
5. **Scarce emphasis.** One primary action per group. Check each text color against the surface it sits on. Status never relies on color alone. Hover and press tint the surface instead of swapping in an unrelated block of color.
6. **Aligned controls.** Buttons and inputs in one row share a height and baseline. A control can look compact but keeps a comfortable tap target (44px on phones).
7. **Motion with a reason.** Short for small feedback, longer for large moves, quick exits. With reduced motion turned on: cross-fade on touch interactions, otherwise change at once.
8. **States.** Cover rest, hover, press, focus, selected, disabled, loading, empty and error for anything interactive.

## Component inventory (names only)

AlertDialog, AppShell, AspectRatio, Avatar, AvatarGroup, Badge, Banner, Blockquote, BottomSheet, Breadcrumbs, Button, ButtonGroup, Calendar, Card, Carousel, Center, Chat, CheckboxInput, CheckboxList, Citation, ClickableCard, Code, CodeBlock, Collapsible, CommandPalette, ComplexSelector, ContextMenu, DateInput, DateRangeInput, DateTimeInput, Dialog, Divider, Drawer, DropdownMenu, EmptyState, Field, FieldStatus, FileInput, FormLayout, Grid, HStack, Heading, HoverCard, Icon, IconButton, Indicator, InfoTip, InputGroup, Item, Kbd, Layer, Layout, Lightbox, Link, List, Markdown, MetadataList, MobileNav, MoreMenu, MultiSelector, NavIcon, NavItem, NavMenu, NumberInput, Outline, OverflowList, Overlay, Pagination, Popover, PowerSearch, ProgressBar, RadioList, Resizable, ScrollableArea, Section, SegmentedControl, SelectableCard, Selector, SideNav, Skeleton, Slider, SnapPaging, Spinner, Stack, StatusDot, Stepper, Switch, TabList, Table, Text, TextArea, TextInput, Thumbnail, TimeInput, Timer, Timestamp, Toast, ToggleButton, Token, Tokenizer, Toolbar, Tooltip, TopNav, TreeList, Typeahead, VStack, VisuallyHidden

## How to use this on a site

See `ui-changes-playbook.md` in this folder.
