# Vendor imagery + Loon weather widget + weather API research

Researched 2026-09-19 via HTTP fetch / web search only (no browser automation, nothing downloaded). Every URL below was seen in fetched page content or a search result. Where a site blocked fetching, that is stated rather than guessed.

---

## TASK 1 — Vendor imagery resources

### Atomic (priority)

**Official press / media resources**
| Resource | URL | Login? | Notes |
|---|---|---|---|
| Atomic newsroom (Mynewsdesk) | https://press.atomic.com/ | No login to browse | Sections: `/latest_news`, `/latest_media` (media library), `/documents`, `/events`, `/contact_people`. Site prompts "Do you work in the press or media?" and asks for an email to follow. |
| Atomic media library | https://press.atomic.com/latest_media | No login to browse | Items on the documents page are tagged "Media Use" or "Non-commercial use". Page states: "This page is intended for journalists, press and media." |
| Atomic documents / press releases | https://press.atomic.com/documents | No | Includes 2024/25 Redster-adjacent PRs: Bent skis, Maverick/Maven, Backland FR (PDF). |
| Amer Sports media contacts (parent co.) | https://www.amersports.com/newsroom/media/ | No | Lists media@atomic.com. Also links a "Salomon media bank" behind an Auth0 login at `b2b-salomon-prod.eu.auth0.com` (login required). |
| Amer Sports "materials for media" | https://www.amersports.com/newsroom/materials-for-media/ | No (link seen, not fetched) | |
| Dealer/B2B portal | Not found publicly. Atomic.com nav only exposes a store finder (`/en-us/pages/store-finder`). The Amer Sports B2B bank above is the only dealer-type asset login seen. | Login | |

**Atomic.com hero / lifestyle images** (Shopify; site is atomic.com/en-us/…, image CDN is `www.atomic.com/cdn/shop/files/…` for lifestyle and `cdn.amersports.com/…` for product cutouts; Shopify `?width=` param resizes)

Homepage — https://www.atomic.com/en-us/ (og:image is a generic 1200x630 `og-default.jpg`; the real hero imagery is inline)
- `https://www.atomic.com/cdn/shop/files/ATOMIC-BLANCHARD-5590.jpg?crop=center&height=2850&v=1787732195&width=3800` — alt "Skier, Piste, All-Mountain"; 3800x2850.
- `https://www.atomic.com/cdn/shop/files/MIKA-BLANCHARD-9944.jpg?crop=center&height=4500&v=1786393073&width=3375` — Mika Vermeulen in racing suit on red Redster skis, on snow; 3375x4500 (portrait).
- `https://www.atomic.com/cdn/shop/files/Atomic_Redster25_Alpine_SilvanoZeiter_11-1200x1200.jpg?crop=center&height=1200&v=1785489410&width=800` — skier in black/red suit on snowy slope under blue sky holding red Redster skis; 800x1200.
- `https://www.atomic.com/cdn/shop/files/Atomic_Redster25_Alpine_SilvanoZeiter_4-1200x1200.jpg?crop=center&height=1200&v=1785489432&width=960` — close-up on snow, black pants, bright red race boots, skis/poles; 960x1200.
- `https://www.atomic.com/cdn/shop/files/24A1498_0112_1.jpg?v=1786368463&width=3840` — two skiers descending a slope, foreground skier in red jacket; 3840x2880.
- `https://www.atomic.com/cdn/shop/files/FACTORY_REDSTER_27_ce73f31f-a57c-4a8c-9bae-7d8f7a2d391d.jpg?v=1785417520&width=4500` — person behind glass display holding a Redster ski (factory series); 4500x3600. Other FACTORY_REDSTER_* shots (5, 9, 11, 12, 21) are factory/manufacturing detail images 3375–3600 x 4500.

Redster race collection — https://www.atomic.com/en-us/collections/ato-featured-family-redster (title: "Atomic Redster Race Collection | World Cup Race Skis & Gear")
- Product cutouts only (PNG on transparent, 800x1000), e.g. `https://cdn.amersports.com/cb6ce34f-0771-44f7-9b69-b49c0145108f/ATP_AASS03626_3_GHO_REDSTER_G9_RVSK_S_I12_GW_FullImageWebOptimized.png?width=800&height=1000&fit=bounds&format=auto&quality=80` (Redster G9 Revoshock S), and same pattern for S9, Q9.8, Q9, Q7.8, Q7, Q6, Q5, Q4. No on-snow hero on this page.

Maverick — https://www.atomic.com/en-us/collections/ato-men-skis-all-mountain — product cutouts 800x1000 (Maverick 115/105/96/88 CTI, 86 C, 84), e.g. `https://cdn.amersports.com/965fe28f-4885-4610-99ca-b49f00f0bdba/ATP_AA0030928_3_GHO_Maverick_96CTI_FullImageWebOptimized.png?width=800&height=1000&fit=bounds&format=auto&quality=80`.

Bent — https://www.atomic.com/en-us/collections/ato-men-skis-freeride — product cutouts 800x1000 (Bent Chetler 120, Bent 110/100/90/85), e.g. `https://cdn.amersports.com/44f81d47-68ca-47a8-a2cc-b49f00f10a64/ATP_AA0030954_3_GHO_Bent_Chetler_120_FullImageWebOptimized.png?width=800&height=1000&fit=bounds&format=auto&quality=80`.

Alpine race athletes — https://www.atomic.com/en-us/pages/athletes/alpine-race — studio athlete portraits 600x720–900 (Shiffrin, Pinheiro Braathen, Kilde, Goggia, Feller, Schwarz, Vinatzer, Nullmeyer), e.g. `https://www.atomic.com/cdn/shop/files/Athlete_portrait_Shiffrin_Mikaela.jpg?v=1784546443&width=600`.

Note: the old `/en-us/redster`, `/en-us/skis/racing` style URLs 404; Atomic's US site is now Shopify with `/collections/ato-…` slugs.

**Dealer image-usage terms:** none stated on atomic.com for dealers. Press site labels assets "Media Use" / "Non-commercial use" and says it is "intended for journalists, press and media."

---

### Van Deer – Red Bull Sports

- Official site: https://vandeer-redbull-sports.com/en (vandeer.com redirects here). Images served from Cloudinary `res.cloudinary.com/redbull-van-deer/…` with `f_auto,c_limit,w_3840,q_75` transforms.
- **Press/dealer portal:** none found. Only a retailer map (`/en/retailer-map`). Search surfaced `https://augment-sports.com/pages/download-1` ("Downloads – VAN DEER") but it redirects to the homepage. Red Bull Content Pool (redbullcontentpool.com) appeared in search but was not verified as carrying Van Deer assets.
- **Homepage hero images** (https://vandeer-redbull-sports.com/en):
  - `https://res.cloudinary.com/redbull-van-deer/image/upload/f_auto,c_limit,w_3840,q_75/v1788872091/Season%2026_27/Product/Hardgoods/26-27_%20HP68/GGGG1586-Bearbeitet.jpg` — 26/27 H-Power 68 hero; source 11382x8537.
  - `https://res.cloudinary.com/redbull-van-deer/image/upload/f_auto,c_limit,w_3840,q_75/v1780384442/Season%2026_27/Product/Hardgoods/Freisteller/RB_VD_SKI_MainComp_HP68_v20.png` — ski cutout; 2880x3840.
  - `https://res.cloudinary.com/redbull-van-deer/image/upload/f_auto,c_limit,w_3840,q_75/v1789644641/Stories/MARCEL%20HIRSCHER:%20%22ENDLICH%20WIEDER%20SKIFAHREN%22/Marcel_Skihalle_Wittenburg_Aug26__AndreasPutz_87-background-` — Marcel Hirscher skiing (indoor hall, Aug 2026); 4879x3254.
  - `https://res.cloudinary.com/redbull-van-deer/image/upload/f_auto,c_limit,w_3840,q_75/v1765538394/VDRBS_HQ_SCHEFFAU_NOV25__c_Philipp_Reiter-133_1_cooa0y.png` — HQ/Scheffau (Nov 25); size not given.
- **H-Power 68 race ski page** (https://vandeer-redbull-sports.com/en/products/h-power-68):
  - og:image `https://res.cloudinary.com/redbull-van-deer/image/upload/v1788248427/Season%2026_27/Product/Hardgoods/26-27_%20HP68/GGGG0103-Bearbeitet-2.jpg` — 11648x8736.
  - `…/v1788865463/Season%2026_27/Product/Hardgoods/26-27_%20HP68/H-POWER68_crop.jpg` — 4018x5359.
  - `…/v1760360938/Season%2025_26/Brand/Pictures/JM_20230808_Van_Deer_0551.jpg` — brand lifestyle; 3200x2133.
  - Front/back/side cutouts `…/Freisteller/HP68_RB_VD_SKI_MainComp_{Frontview,Backview,Sideview}_v19.png` — 1920x2560.
- **Usage terms:** none found.

---

### Head

- head.com (both `/en-us/` and `/en_US/…`) returned **HTTP 429 "Vercel Security Checkpoint"** to every fetch, so no og:image / hero URLs from head.com could be captured. Known page URLs from search: race skis https://www.head.com/en_US/ski/skis/race.html ; WCR e-GS Rebel FIS https://www.head.com/en_US/product/wcr-e-gs-rebel-fis-313005-set ; Raptor WCR 140S https://www.head.com/en_US/product/raptor-wcr-140s-pv-605030.
- **Press/media library (Mynewsdesk):** https://www.mynewsdesk.com/com/head (newsroom), https://www.mynewsdesk.com/com/head/latest_media (media library), https://www.mynewsdesk.com/com/head/pressreleases. No login to browse; images have direct `fl_attachment` download links (e.g. `https://mnd-assets.mynewsdesk.com/image/upload/fl_attachment/qmy0ilepqoad7y2aimvy1y`, source 5120x2880). Press release "THE HEAD WINTER SPORTS HIGHLIGHTS 26/27" (https://www.mynewsdesk.com/head/pressreleases/the-head-winter-sports-highlights-26-strich-27-power-your-progression-3429659) attaches "HEAD winter sports highlights 26:27.jpg", 5333x3000, 11.2 MB, license "Media Use".
- **Dealer portal:** not found publicly.
- **Usage terms:** assets labelled "Media Use" (Mynewsdesk license label).

---

### Rossignol

- US site: https://www.rossignol.com/us-en/ (Salesforce Commerce Cloud; catalog images at `www.rossignol.com/dw/image/v2/BJJZ_PRD/on/demandware.static/-/Sites-rossignol-catalog/default/…/images/large/<SKU>_72DPI_01_v00.jpg?sh=300` — `sw`/`sh` params resize; lifestyle content from `mediastorage.livestory.io/rossignol/posts/orig/<id>.jpg?width=…`, seen up to width=2000).
- **Press/media:** https://www.rossignol.com/mediacoverage.html is a page of press clippings (links out to retailers/reviews), not an asset library. No press-kit or dealer portal link found on the site.
- **Race skis category** — https://www.rossignol.com/us-en/sports/alpine-ski/skis/race — product thumbs only, e.g. `https://www.rossignol.com/dw/image/v2/BJJZ_PRD/on/demandware.static/-/Sites-rossignol-catalog/default/dwa0cf2a0d/images/large/RANAL01000_72DPI_01_v00.jpg?sh=300` (HERO FIS SL FAC 165 R22) and `…/dw1dfe9480/images/large/RAPAL01000_72DPI_01_v00.jpg?sh=300` (HERO ATHLETE FIS SL FACTORY 165 R22).
- **"Calling All Heroes" (Hero line landing)** — https://www.rossignol.com/us-en/calling-all-heroes.html — on-snow lifestyle images (append `?width=1500` etc.):
  - `https://mediastorage.livestory.io/rossignol/posts/orig/696e42e2143e02b31115a60b.jpg` — Federica Brignone celebrating, tiger helmet (seen at width=1500).
  - `https://mediastorage.livestory.io/rossignol/posts/orig/696e4503c088b8eed920b349.jpg` — racer in suit making a high-speed turn, spray of snow, mountains behind.
  - `https://mediastorage.livestory.io/rossignol/posts/orig/68ecc32c3b5be70158dc5d20.jpg` — Federica Brignone in full descent.
  - `https://mediastorage.livestory.io/rossignol/posts/orig/68ecc32b3b5be70158dc5d1c.jpg` — close-up of Hero Elite ST Ti skis in snow.
  - `https://mediastorage.livestory.io/rossignol/posts/orig/696bbb1071e7e3bf4458592a.jpg` — Brignone holding the new Hero ST TI 26/27 ski.
  - `https://mediastorage.livestory.io/rossignol/posts/orig/6968e854a06b3d727cd98ecc.jpg` — Hero ST TI 26/27 skis on red background (product hero).
- **Usage terms:** none stated for dealers.

---

### Fischer

- US site: https://www.fischersports.com/us_en (image CDN `www.fischersports.com/media/<WxH>/…`, sized folders like `2880x1700`, `1072x1366`, `2144x1366`).
- **Media database (public):** https://mediadb.fischersports.com/ — "MediaDatabase | Fischer Sports". Has a Log in / Sign up, but the start page, categories, and the Photo Credit terms are public. Categories seen: `/media/category/58252`, `62109`, `62473`, `62771`, `62823`, `63195`.
- **Photo-credit / usage terms** (https://mediadb.fischersports.com/page/Photo%20Credit): "You can use our images for a large variety of personal and commercial projects: advertising, catalogs, website, social media…" — "Picture credits (© Fischer Sports GmbH) obligatory." Prohibited: logos/trademarks, obscene/libelous works, sale to third parties, other media databases.
- **B2B dealer portal:** https://us.b2b.fischersports.com/ ("Home 26|27 | Fischer Skis US") — **login required** (`/profile/login`). Also links dealer locator.
- **RC4 Noize page** — https://www.fischersports.com/us_en/rc4-noize (note: og:image is just the 512px app icon):
  - `https://www.fischersports.com/media/2880x1700/48/29/e9/1787657106/stage_banner_noize_35-37_2880x1700.jpg` — stage banner, 2880x1700 (also used on the homepage).
  - `https://www.fischersports.com/media/2880x1200/4e/30/28/1736342691/250108_Noize_Ski_Visual_Header_2880x1200_01.jpg` — RC4 Noize ski visual header, 2880x1200.
  - `https://www.fischersports.com/media/1072x1366/74/e8/3f/1733759005/241209_Noize_Keyvisual_1I3_Card_1072x1366_03.jpg` — key visual card, 1072x1366.
  - `https://www.fischersports.com/media/2144x1366/06/cc/56/1735480651/241229_Noize_Technology_2I3_Card_2144x1366_04.jpg` — technology card, 2144x1366.
  - Product cutouts 1620x2160: `…/media/640x854/40/5f/20/1783391253/p06826_rc4_noize_01.png` (RC4 Noize + RC4 Z13 GW FF), `p06626_rc4_noize_st_pro_01.png`, `p06126_rc4_noize_lt_pro_01.png`.
- Homepage also has `https://www.fischersports.com/media/2880x1700/ab/29/25/1787657106/stage_banner_speedmax_35-37_2880x1700_en.jpg` (Speedmax nordic, 2880x1700).

---

### Dynastar

- US site: https://www.dynastar-lange.com/us-en/ (dynastar.com redirects). Same SFCC platform as Rossignol; catalog images `www.dynastar-lange.com/dw/image/v2/BJJZ_PRD/on/demandware.static/-/Sites-rossignol-catalog/default/…`.
- **Press/media:** https://www.dynastar-lange.com/mediacoverage.html — press clippings only, not an asset library. No dealer portal link found.
- Category pages (https://www.dynastar-lange.com/us-en/skis/men/racing, `/skis/men/on-piste`) render product grids client-side; no hero image URLs were present in the fetched HTML.
- **Speed Omeglass WC SL 150 R22 product page** — https://www.dynastar-lange.com/us-en/unisex-racing-skis-speed-omeglass-wc-sl-150-r22-DAMAI01000.html — product images (append `?sw=800`):
  - `https://www.dynastar-lange.com/dw/image/v2/BJJZ_PRD/on/demandware.static/-/Sites-rossignol-catalog/default/dw18a0a4c1/images/large/DAMAI01_SPEED_OMEGLASS_WC_SL_150_R22_RGB72DPI_03.jpg?sw=800`
  - `…/dw7dd605d7/images/large/DAMAI01_SPEED_OMEGLASS_WC_SL_150_R22_RGB72DPI_02.jpg?sw=800`
  - `…/dwa3e9263a/images/large/DAMAI01_SPEED_OMEGLASS_WC_SL_150_R22_RGB72DPI_05.jpg?sw=800`
- Other Speed race URLs from search: Speed Course WC GS 170-182 R22 `…/unisex-racing-skis-speed-course-wc-gs-170-182-r22-DAMDP01000.html`; Speed Course WC GS Factory 188 `…-DAMGL01000.html`; Speed 550 Konect `…/dynastar-speed-550-konect-skis-DAOZ502000.html`.
- **Usage terms:** none stated.

---

### Salomon

- salomon.com returned **HTTP 403 "Access to this page has been denied"** to direct fetches; the WebFetch proxy got the homepage (og:image `https://images.ctfassets.net/7iktyqnb7v9e/NaCUCROLT7JdUHR1DbdLz/7300b544936b592ba95df22734c19460/Hiking-shoes.jpg`; hero is a summer gravel-running banner from `images.ctfassets.net` — Contentful) but product pages came back without image URLs.
- Known page URLs from search: Alpine racing skis https://www.salomon.com/en-us/c/sports/alpine-skiing/skis/racing ; S/Race Prime GS 183 https://www.salomon.com/en-us/product/s-race-prime-gs-183-24m-li6459 ; S/Race Prime SL 165 https://www.salomon.com/en-us/product/s-race-prime-sl-165-12m-li6461.
- **Media bank / dealer:** "Salomon media bank" link on https://www.amersports.com/newsroom/media/ goes to an Auth0 login (`https://b2b-salomon-prod.eu.auth0.com/u/login/identifier?…`) — **login required**. Amer Sports newsroom lists media contacts (media@amersports.com, media@atomic.com).
- **Usage terms:** none seen.

---

### Summary table

| Brand | Public media library | Dealer/B2B portal | Hero images captured from brand site |
|---|---|---|---|
| Atomic | press.atomic.com (Mynewsdesk, no login; "Media Use") | Amer Sports B2B (Auth0 login) | Yes — several on-snow Redster shots, 3000–4500px |
| Van Deer | none found | none (retailer map only) | Yes — Cloudinary originals up to 11k px |
| Head | mynewsdesk.com/com/head (no login; "Media Use") | not found | No — head.com blocked (429) |
| Rossignol | none (mediacoverage = clippings) | not found | Yes — Hero lifestyle via livestory CDN |
| Fischer | mediadb.fischersports.com (public; credit "© Fischer Sports GmbH" required, commercial use allowed) | us.b2b.fischersports.com (login) | Yes — RC4 Noize banners 2880px |
| Dynastar | none (mediacoverage = clippings) | not found | Product-only (SFCC catalog) |
| Salomon | Salomon media bank (Auth0 login) | same | No — salomon.com blocked (403) |

Practical note: only Fischer publishes terms that explicitly permit dealer/commercial website use (with credit). For the others, ask the rep for dealer asset access (Amer Sports B2B covers Atomic + Salomon; Rossignol Group covers Rossignol + Dynastar).

---

## TASK 2 — Loon Mountain weather / snow-report widget

### Pages
- Homepage: https://www.loonmtn.com/ — nav item "Mountain Report" → https://www.loonmtn.com/mountain-report (also the "Web Cams" nav item). The header has a "conditions/trails" flyout menu labelled **"Open Trails"** (`overrideNavLabel`) with filter areas "Loon Peak", "West Basin", "South Peak", "North Peak".
- The site is Next.js; every stat is rendered client-side, so the fetched HTML only shows section headings and spinners. The site was in **summer mode** on 2026-09-19 (bike-park report, no snowfall stats populated). Field labels below were taken verbatim from the site's JavaScript bundles and its live weather JSON, not from a rendered winter page.

### Mountain Report page sections (in order, `data-name` in HTML)
1. "What's Happening" (updates/blog)
2. "Bike Park Report" (summer) / trail status — `showStats: ["Trails open"]`, grouped by difficulty ("Novice", "Intermediate", "Advanced")
3. "Bike Park Trail Status"
4. **"Current Weather"** (section `weatherConditions`, aria-label "Weather Stations"), station name **"Loon Peak"** (lat 44.0377, lon −71.6278)
5. **"Mountain Cams"** — 4 CamStreamer iframes (e.g. "Loon Peak Webcam / Octagon Base Area")

### "Current Weather" block — exact layout from the component code
Left column (h3 = station name "Loon Peak"):
- Weather icon (64x64 SVG from the feed's `iconLegend`) beside the current temperature as an h3, e.g. "50°F" (unit toggle °F/°C, `showUnitToggle: false` on Loon)
- Short condition text (`conditionsSummaryShort`, e.g. "Clear")
- Subheading **"Today's Forecast"** followed by the sentence forecast (`conditionsSummary.imperial`, e.g. "Clear. High 55°F, Low 37°F. Winds NW at 9 mph.")

Right column, a bordered list (`<ul>`; each `<li>` is a 2-col grid: icon + label | value), in this order:
1. ↑ (icon `arrow-up`, orange accent) **"High"** — `55°F`
2. ↓ (icon `arrow-down`) **"Low"** — `37°F`
3. (icon `wind`) **"Wind"** — `"{speed} mph {dir}"`, direction from 8-point compass N/NE/E/SE/S/SW/W/NW (e.g. "9 mph NW")
4. (icon `droplet-percent`) **"Precipitation"** — `"{n}%"` (chance of precip)

Compact header/flyout variant (`statItem: "current-weather"`): icon + big temp (h2 style), then inline ↑ High and ↓ Low with the words "High"/"Low" as screen-reader-only (`aria-label="High temperature"`/`"Low temperature"`).
Error state text: "We've had an issue loading our weather feed. Please check back later."

### Snowfall / conditions stat labels (defaults in the code; CMS can override each label)
"Overnight", "Since 5am", "12 Hour Total", **"24 Hour Total"**, "48 Hour Total", "72 Hour Total", "7 Day Total", "Season Total", **"Base Depth"**, "Min Base", "Max Base", "Primary Surface", "Secondary Surface", **"Lifts Open"**, **"Trails Open"**, "Road Conditions", "Road Restrictions". Stat tiles come in `largeStats` / `smallStats` groups and can also be a webcam or parking-lot tile. Which of these Loon shows in winter is a CMS choice (`snowfallStat` was empty in summer mode).

### Icon style
- Weather icons: **Font Awesome Pro 6.6.0 solid (filled) SVGs**, served from `https://feed-icons-dbgxg7hrccgddubp.a03.azurefd.net/Weather/fa/<name>.svg`. Legend keys: `clear-day`, `clear-night`, `partly-cloudy-day`, `partly-cloudy-night`, `cloudy`, `rain`, `sleet`, `snow`, `wind`, `fog` (labels "Clear Day", "Clear Night", "Partly Cloudy Day", …). Rendered 48–64px; inverted via CSS filter on dark backgrounds.
- Stat-row icons: small inline icon set (`arrow-up`, `arrow-down`, `wind`, `droplet-percent`) in the site's orange accent color (`#E07200` appears as the accent). No emoji.
- Trail/lift status: 20x20 status icons per row.

### Data source
- Weather: **Tomorrow.io** (`weatherAPI: "TomorrowIOWeather"`), proxied through the site's own endpoint `https://www.loonmtn.com/api/weather?weatherAPI=TomorrowIOWeather&latitude=…&longitude=…&location=&resortCode=…`. Response fields: `lastUpdate`, `expires`, `currentConditions{temperature{fahrenheit,celsius}, conditionsSummary{imperial,metric}, conditionsSummaryShort, windSpeed{milesPerHour,kilometersPerHour}, windDirection(deg), icon}`, `forecasts[15]{startDate, temperatureHigh, temperatureLow, chancePrecipitation, conditionsSummary, conditionsSummaryShort, windSpeed, windDirection, icon}`, `iconLegend`. The UI shows only `forecasts[0]` — no multi-day strip on this page.
- Snow/trail/lift stats: resort-reported CMS data (Sanity-style document IDs); road data via a "ReportPal" roads feed. No NOAA/OpenSnow/OnTheSnow credit anywhere on the page.
- Webcams: CamStreamer embeds.

---

## Weather API comparison (for a shop widget: day name, icon, high/low, wind, last-24h snowfall, 3-day forecast)

Targets: Lincoln NH / Loon (44.0364, −71.6215) and Scarborough ME (43.5781, −70.3217).

### Open-Meteo — https://open-meteo.com/en/docs
- Endpoint `https://api.open-meteo.com/v1/forecast`; **no API key** for non-commercial use ("Only required to commercial use…"). Commercial use goes through `customer-api.open-meteo.com` with a key.
- Daily variables confirmed: **`snowfall_sum`** (cm), **`weather_code`** (WMO code), `temperature_2m_max`, `temperature_2m_min`, `wind_speed_10m_max`, `wind_gusts_10m_max`, `precipitation_sum`.
- `past_days` 0–92 (use `past_days=1` for last-24h snowfall), `forecast_days` 0–16 (default 7).
- Units: `temperature_unit=fahrenheit`, `wind_speed_unit=mph`, `precipitation_unit=inch`.
- Free limits (https://open-meteo.com/en/pricing): 600 calls/min, 5,000/hour, 10,000/day, 300,000/month. Paid tiers listed as API Standard 1M calls/mo, Professional 5M, Enterprise 50M+ (prices not shown on page; Stripe checkout).
- Terms (https://open-meteo.com/en/terms): non-commercial = "private or non-profit websites or apps that do not have subscriptions or advertising"; commercial = "websites or apps that have subscriptions or display advertisements" and integration into commercial products. A retail shop's site is a judgement call; the safe reading is that it needs the commercial plan.
- No icons supplied — map `weather_code` to your own icon set.

### NWS api.weather.gov — https://www.weather.gov/documentation/services-web-api
- Free, **no API key**; a `User-Agent` header identifying the app and a contact is required, e.g. `User-Agent: (myweatherapp.com, contact@myweatherapp.com)`.
- Rate limit "is not public information, but allows a generous amount for typical use"; retry after ~5 s if limited.
- `/points/{lat},{lon}` → grid endpoints. Resolved on 2026-09-19:
  - Loon/Lincoln NH: office **GYX**, grid **24,67** → `https://api.weather.gov/gridpoints/GYX/24,67/forecast`, `/forecast/hourly`, raw `https://api.weather.gov/gridpoints/GYX/24,67`, stations `…/24,67/stations`.
  - Scarborough ME: office **GYX**, grid **71,54** → `https://api.weather.gov/gridpoints/GYX/71,54/forecast`, `/forecast/hourly`, raw `https://api.weather.gov/gridpoints/GYX/71,54`.
- `/forecast` returns 12-hour periods for 7 days with `name` ("Today", "Tonight", "Saturday"…), `temperature` + `temperatureUnit` (F), `windSpeed` ("5 mph"), `windDirection` ("NW"), `icon` URL (`https://api.weather.gov/icons/land/day/few?size=medium`), `shortForecast`, `probabilityOfPrecipitation`. High/low come as alternating day/night periods, not a single high/low pair.
- The raw gridpoint JSON (`/gridpoints/GYX/24,67`) includes a **`snowfallAmount`** series (forecast, not observed) alongside `maxTemperature`, `minTemperature`, `windSpeed`, `weather`, `quantitativePrecipitation`, `iceAccumulation`, `snowLevel`. Observed last-24h snowfall is not a forecast field; nearest-station observations (`/stations/{id}/observations`) do not reliably carry snowfall, so "24-hr snowfall" would need Open-Meteo `past_days=1` or the resort's own report. The docs page itself says nothing about `snowfallAmount` or the icons endpoint; the field names above come from a live call.

### OpenWeatherMap — https://openweathermap.org/full-price
- Free plan: **60 calls/minute, 1,000,000 calls/month**; includes Current weather API, 3-hourly forecast for 5 days, Air Pollution, Geocoding, weather widgets. **One Call API is not included** in Free.
- One Call API 3.0 (https://openweathermap.org/api/one-call-3): "1,000 free daily API calls" on a pay-as-you-call plan (requires a card on file); per-call overage price and the daily-snow field were not shown in the fetched content — verify on the page before relying on it.
- API key required for all plans.

### Quick recommendation (from the above)
- Cheapest robust combo: NWS `/gridpoints/GYX/{x,y}/forecast` for the 3-day day-name/icon/high-low/wind (free, no key, official icons) + Open-Meteo daily `snowfall_sum` with `past_days=1` for the 24-hr snowfall number (confirm commercial-use status or budget for the Standard plan). Cache server-side (Loon's own feed caches ~30 min per `expires`).
