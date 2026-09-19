# Rodgers Ski & Sport — Website Prototype

Clickable, responsive prototype for the rodgersskiandsport.com rebuild (Waterside stack: Next.js / Vercel / Payload).
Brand navy #012D5D from the supplied logo; the orange accent is a stand-in pending the branding pass.

Share link (GitHub Pages): https://watersideg.github.io/rodgers-prototype/

## Branches

- `design-prototype` — the August 2026 layout prototype with photo-direction placeholders (22 pages, inline CSS).
- `content-build` — this branch: real copy, real photography, staff picks, journal, partners, race, weather, email modal. 28 pages.

## Layout

```
prototype/          the site (open prototype/index.html; GitHub Pages serves it)
  img/              web-sized photos (≤1800px) used by the pages
  site.css, site.js shared styles and behaviour (weather widget, email modal)
build/              generator: python3 build/build.py rewrites everything in prototype/
  shell.py          shared header, nav, footer, modal, CSS, JS, store data, build flags
  data.py           staff picks, journal posts, partners, brand lists, price lists
  pages.py          one function per page
  shots.py          QA screenshots of every page at 1440 and 390 px (Playwright)
resources/          project resources
  docs/             spec wireframes, prototype design PDF, marketing plan (v3.1), project plan (xlsx)
  research/         live-site index, comparable-site review, social indexes (IG/TikTok/FB), vendor imagery + weather API notes
  photos/           onedrive-web/ (selected shots from Kaelyn's "Website Pictures" library), social/ (staff-pick portraits),
                    vendor/ (Atomic, Fischer, Rossignol, Van Deer brand imagery), onedrive-review-notes.md (ratings for all 1,707 photos)
```

## Build flags (build/shell.py)

- `ONLINE_RESERVATIONS = False` — rentals page shows rates and the walk-in note; set `True` next season to expose the reservation form.

## Content sources

- Prices, hours, addresses, brand lists, lease terms: rodgersskiandsport.com (Squarespace) as of Sept 19, 2026.
- Staff picks and post copy: @rodgersski (Instagram), @rodgersskiandsport (TikTok), RodgersSkiSport (Facebook), quoted verbatim.
- Weather: Open-Meteo (no key) in the prototype; production should proxy through the site's own API route.
- Maps and directions: Google Maps embeds and direction links; hours are to sync from each store's Google Business Profile in Payload.
