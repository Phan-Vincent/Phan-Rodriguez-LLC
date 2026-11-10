# Auto shop site generator

`build.py` generates the Tri Auto, A C Tires and Moreno's Auto Repair sites (`mockups/<folder>/index.html`). `shot.py` takes Playwright screenshots at 1440px and 390px and checks for horizontal overflow and console errors.

```
python3 build.py <path-to-mockups-dir>
```

Notes:
- Photos are Unsplash free-license images, loaded by URL. IDs are in the `P` dict in `build.py` and listed in `DESIGN.md`.
- The committed pages also have `<meta name="robots" content="noindex">` added after generation. Add it to `page()` in `build.py` if you regenerate.
- Review quotes, hours and addresses are from public listings. Confirm with each owner before launch.
