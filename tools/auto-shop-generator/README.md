# Auto shop site generator

`build_v2.py` builds Tri Auto, A C Tires and Moreno's. `build_leads.py` builds the other 16 lead sites in the same style (run it the same way). Both write to `mockups/<folder>/index.html`.

| Site | Layout |
| --- | --- |
| Tri Auto | Split hero, three make tiles, zigzag photo rows, rotating reviews, visit card |
| A C Tires | Photo banner with an info bar, service list beside a sticky heading, stats band, week strip |
| Moreno's | Profile page: cover photo, sticky shop card on the left, content cards on the right |

```
python3 tools/auto-shop-generator/build_v2.py mockups
```

- `tri_reviews/` holds Tri Auto's review markup and carousel script (Vincent's Birdeye links). Edit reviews there.
- If you hand-edit a page in `mockups/`, also change `build_v2.py`, or the next build overwrites it.
- `build_v1_old.py` is the first generator, kept for history. `shot.py` takes Playwright screenshots.
- Photos are Unsplash free-license images loaded by URL. Quotes, hours and addresses come from public listings; confirm with each owner before launch.
