# Comparable Ski/Bike Retailer Sites — Content & Organization Review

Reviewed 2026-09-19 via server-side page fetches (no JavaScript executed). Where a section is rendered client-side (e.g., email pop-ups, JS product grids), that is noted rather than inferred. All labels and copy are quoted as found.

---

## 1. SkiEssentials — https://www.skiessentials.com/

**Platform signals:** Klaviyo (email) and Okendo (reviews) scripts present in homepage source.

### Primary nav (verbatim, in order)
`SKI | CROSS-COUNTRY | SNOWBOARD | PACKAGES | APPAREL | ACCESSORIES | BIKE | BRANDS | CHAIRLIFT CHAT | 2026 PRICE DROPS | OUTLET`

Dropdown contents not rendered in fetched HTML. "BRANDS" links to `/activities/activity-all-brands`.

### Homepage section order
1. Hero banner (dual-image carousel)
2. Heading "2027 SKI & BINDING COMBO DEALS"
3. Four category tiles, each with a "SHOP NOW" button: "Shop Skis", "Shop Snowboards", "Shop XC", "Shop Ski Boots"
4. Four brand tiles, each with "SHOP NOW": Atomic, Volkl, Rossignol, Elan
5. Outlet banner (carousel)
6. "Chairlift Chat" promotional block (blog)
7. Loyalty program promotional block
8. Email signup: "SIGN UP FOR EXCLUSIVE DEALS" (embedded form, "Loading Form..." placeholder — Klaviyo-loaded)
9. Footer

### Seasonal featured categories/products
- Nav item "2026 PRICE DROPS"; homepage heading "2027 SKI & BINDING COMBO DEALS".
- Footer links "2027 Skis - Now Available" and "2027 Ski Test".
- Category page product cards carry a "2026 Price Drop" badge and "Outlet Sale" percent-off callout.
- Category page filter facets include "Year".

### Staff picks / staff reviews
No "staff picks" module on homepage or category page. Staff/tester content lives in the annual **Ski Test** hub (`/2025-ski-test`):
- Intro: "Welcome to our 2025 Alpine Ski Test! Now in its 8th year, this test continues to be the most comprehensive ski review out there."
- Organized by Brand (22 vendors), by Gender & Category (Men's/Women's × Frontside, All Mountain, Freeride), and by Tester ("SKI TESTERS" nav → `/2025-ski-test/tester`).
- Tester index card fields: name (linked), photo, "Age", "Height", "Weight", short skiing-style descriptor. ~130 testers.
- Tester profile page header fields: Age, Height, Weight, Years Skiing, Days Per Year, Ski Style, Ski Ability, Aggressiveness (1-11), Ski Testing Experience, Ski Origins/Current Home Mountain, Preferred Terrain, Current Ski(s) of Choice, Favorite Skier, Favorite Place to Ski. Below: list of skis tested (name, image, dimensions/radius, lengths, "Read More").
- Ski test page (e.g. `/2025-ski-test/skis/2025-volkl-blaze-104`): ski name, price, "Buy Now", spec table (Length, Side cut, Turn radius, Recommended terrain, Ability level, Rocker profile, Construction), video, aggregate scores across "Floatation, Stability, Quickness, Playfulness, Forgiveness, Edge Grip, Versatility, and Overall" (0–10 scale). Per-tester cards: name, photo, age, height, weight, days/year, years skiing, ability level, size tested, sizing impression, the 8 category scores, overall impression quote, appropriate terrain, appropriate skier level, additional thoughts. Sample quote: "So much fun!" Six "similar skis" listed at bottom.
- No staff role/title field appears on tester cards.

### Blog ("Chairlift Chat", `/chairlift-chat`)
- Page title "CHAIRLIFT CHAT | SkiEssentials"; no intro copy.
- Category filter row: `ALL | HELPFUL HINTS | INTERVIEWS | SKI COMPARISONS | SKI INDUSTRY NEWS | SKI REVIEWS | SKI STORIES | SKI TECHNOLOGY | TOP FIVE FRIDAYS | UNCATEGORIZED`
- Teaser card: featured image, linked title, date, linked category labels, excerpt, "SHOW MORE" link.
- Email form "SIGN UP FOR EXCLUSIVE DEALS" appears on the index.
- Article anatomy (example: "2025 Men's Mid 100mm All Mountain & Freeride Ski Comparison", Aug 29, 2024): H1 title, date, byline "Bob St.Pierre", category labels, lead image, intro ("You've been waiting patiently for it and it's finally here: comparison season is back!"), per-ski H2 sections with "At a Glance:" spec table and H3s "Overview", "Who it's For", "Price", "Buy Now" links (some with "Ski Review" link), "RELATED ARTICLES", "LEAVE A REPLY" comments, email form. No ratings/scores in the article.

### Email signup
- Footer/inline embedded form, headline "SIGN UP FOR EXCLUSIVE DEALS". No stated discount incentive. Pop-up modal behavior not observable server-side (Klaviyo present).

### Locations / hours
- Single location in footer and About page: "SkiEssentials 192 Thomas Lane Stowe, VT 05672", "(877) 812-6710", "Mon-Fri: 9:00 AM-5:00 PM". No dedicated location page found.
- About page: "ABOUT US"; "Our motto of 'Gear for Skiers by Skiers®' is about as real as it gets." History: founded 1984 as Bedside Tuners; first online sale Oct 2004; acquired Basin Sports (Killington) Aug 2022. No individual staff listed.

### Brands
- Homepage: four brand tiles (Atomic, Volkl, Rossignol, Elan) with "SHOP NOW".
- Brands page heading "SHOP ALL BRANDS": featured logo grid (Blizzard, K2, Völkl, Atomic) then alphabetical A–Z text list (150+ brands); brand URLs like `/collections/blizzard-skis`.
- Category page has "Brand" facet.

### Weather / snow report
None found.

### Category page notes (`/collections/alpine-skis`)
- Title "Skis | SkiEssentials"; intro "Here you'll find all the different alpine skis for sale on SkiEssentials.com, and simply put, there are a lot."
- Facets: `Category | Gender | Brand | Price | Year | Size | Waist Width | Ability Level | Bundle Size`
- Card fields: image, brand, title, regular price, sale price with discount amount, seasonal badge ("2026 Price Drop"), "Outlet Sale" callout.

---

## 2. Peter Glenn — https://peterglenn.com/

**Platform signals:** BigCommerce URL patterns (`search.php`, `giftcertificates.php`). Direct HTML fetch was blocked ("Request Blocked"); page data below comes from the fetch tool's rendered read.

### Primary nav (verbatim, in order)
`Footwear | Women | Men's | Women's | Kids' | Ski | Snowboard | Running | Travel and Trail | Wake and Waterski | Inline | Sailing | Brands | Blog | New | Sale`

### Homepage section order
1. Announcement bar: "Orders Over $75 Ship Free"
2. Hero: "Peter Glenn Over 65 Years Outdoors"
3. Featured category tiles: Ski Jackets, Ski Pants, Skis, Ski Boots, Winter Boots, Goggles, Snowboard Jackets, Snowboard Pants, Snowboards, Snowboard Boots, Luggage, Running Shoes
4. Promotional banner: Völkl / Dalbello / Marker (three linked brand sections)
5. Content/promo blocks: "Peter Glenn 2025 Holiday Gear Guide", "Pre-Season Sale", "Warren Miller's 'Days Off' Premiere", "Shop Gift Cards" / "Shop Gift Certificates", "Winter Sale: Save up to 60% Off!"
6. Embedded YouTube video
7. Staff review block: "Jonny Moseley Product Reviews" — "The official Peter Glenn Chief Testing Officer shares his personally tested gear and apparel." CTA "CHECK THEM OUT" (links to `search.php?search_query=JonnyReview`)
8. "Most Popular" product grid (14 products; badges "UP TO 46% OFF", "UP TO 40% OFF", etc.)
9. "New Items" product grid
10. Brand logo row: 686, Descente, Helly Hansen, Spyder, Bogner, Obermeyer, Roxy, Quiksilver, Hot Chillys, Burton, Smith, Nils, Rossignol, Giro, Karbon
11. Footer

### Seasonal featured categories/products
- "Pre-Season Sale", "Winter Sale: Save up to 60% Off!", "Peter Glenn 2025 Holiday Gear Guide", Warren Miller premiere promo.
- Category page facet "On Sale (YES/NO)"; product badges "UP TO [%] OFF".

### Staff picks / staff reviews
- Single named reviewer: Jonny Moseley, titled "Chief Testing Officer". Presented as a homepage block with copy above, CTA to a search-results page for products tagged "JonnyReview". The search results page is disallowed by robots.txt and could not be fetched; format of individual reviews not documented.
- About page does not list staff or mention Moseley.

### Blog (`/blog/`)
- Heading "Blog"; no intro; no categories, tags or filters.
- Teaser card: square image (640×640), linked title, "Posted by Peter Glenn Staff on [date]", excerpt with truncation, "[read more]" link.
- 5 posts per page, numbered pagination plus "Next".
- Recent titles: "Top Ski Jacket Brands: The North Face" (Sep 1, 2026), "Skiing in New Zealand: Queenstown, Coronet Peak, and What to Know Before You Go", "Top Ski Jacket Brands: Spyder", "Skiing in Chile: A Guide to Portillo, Valle Nevado, and the Andes", "Ski Storage Ideas: How to Store Your Skis and Gear at Home Between Seasons".
- Article anatomy (North Face example): title, "Posted by Peter Glenn Staff on Sep 1st 2026", hero image, italicized summary lead, H2/H3 sections (e.g. "Is The North Face a Good Ski Jacket Brand?", "Selection Guide" table), inline links to collection pages, two infographics, share buttons (Facebook, Email, Print, X, Pinterest), "Get Exclusive Offers" email block, closing paragraph CTA to shop. No comments, related posts, or byline name.

### Email signup
- Footer: "Get exclusive Peter Glenn offers" with consent text "We will not share your info with anyone." No discount stated. Modal not observable.

### Locations / hours
- Nav/footer "Store Locations" → `/locations/`: heading "Peter Glenn Store Locations", intro "Click on a location below for store hours and more information." Locations grouped by state (Florida, Georgia); each entry shows store name/city, street address, phone, link to a store detail page; "NOW OPEN!" badge on new stores; embedded Google Maps directory. Example entry: "South Miami, FL 11855 S. Dixie Hwy Miami, FL 33156 (305) 254-3309". Run Appeal specialty shops listed within Florida.
- Store detail page (Fort Lauderdale): heading "Peter Glenn Ski & Sports - Fort Lauderdale, FL"; address; phone; hours "Monday - Friday: 11am - 7pm / Saturday: 10am - 6pm / Sunday: Noon - 6pm"; holiday closures with dates; "Store Manager: Hans Erni"; store photo; embedded map; description ("...has been proudly serving the South Florida community for almost 40 years."); brand mentions; "Back to Store Directory".
- Hours are not shown on the index page, only on detail pages.

### Brands
- Nav "Brands"; homepage logo row before footer linking to brand pages (`/686/`, `/descente/`); category "Brand" facet.

### Weather / snow report
None found.

### Category page notes (`/ski/jackets/`)
- Breadcrumb Home > Ski > Jackets; intro "Explore our wide selection of ski jackets, designed for both performance and style."
- Subcategory links: Casual, Ski, Softshell.
- Facets: Product Gender, Size, Brand, Color Family, Options (Length), Fit, On Sale, Features, Insulation Type.
- Sort: Featured Items, Newest Items, Best Selling, A to Z, Z to A, By Review, Price Ascending/Descending.
- Card: image, brand, title, original/sale price, "UP TO [%] OFF" badge, quick view, compare.

---

## 3. Powder7 — https://www.powder7.com/

**Platform signals:** Judge.me (reviews) and Klaviyo (email) scripts present.

### Primary nav (verbatim, in order)
`Skis | Boots | Bindings | Poles | Clothing | Helmets | Goggles | Snowboard | Brands | More`

Mega-menu contents (from source):
- Skis: "Skis for Sale:" Used Demo Skis, Women's Skis, Men's Skis; clearance/closeout links.
- Boots: shop by "Men's US Shoe or Mondo Size" / "Women's US Shoe or Mondo Size".
- Bindings: "Shop By Category:", "Shop By Skier Weight:" (Over 210 lbs … Under 75 lbs), "Top Brands:", "Popular Models:" (with prices, e.g. "Salomon Strive 14 GW $279.95").
- Poles: "Shop By Your Height:", "Shop By Pole Length:", "Shop By Category".
- Clothing: Men's / Women's / Kids / Accessories, "Top Brands:" Arc'teryx, Flylow, Obermeyer, Patagonia.
- Helmets, Goggles, Gloves ("Shop by Style:" Our Warmest Gloves, 5-Finger, 3-Finger, Mittens, Casual, Work), Alpine Touring, Snowboard.
- Brands: "Our Top Picks:" followed by an A–Z brand list (130+ names).
- More: "Backcountry / AT Gear:", "Bags:", "Tunes & Mounts:" (Learn more about the services we offer, Shop all services, Shop wax and ski tuning supplies), "Powder7 Collection:" (New Arrivals and Favorites, The Full Collection), "Even More:" (Gift Certificates, Special Fun Stuff, Our Story, Lift Line Blog).

### Homepage section order
1. Announcement bar: "Equinox Sale - Click Here To Shop - Ends Tue, Sep 22nd"
2. Hero carousel: slides "Used Demo Skis", "Women's Skis", "Men's Skis", "Used Skis Under $400" / "SHOP CLEARANCE RACK", "Closeout New Skis" / "SHOP NOW"
3. "The Yard Sale Room" image link (`/the-yard-sale-room`)
4. Four featured product tiles with "Shop Now": Blizzard Rustler 9, Salomon QST 106, Powder7 Storm Day Gloves, Norrona Lofoten Gore-Tex Insulated Ski Jacket
5. Two "Explore" tiles (ski finder, boot buying guide)
6. "Powder7 Top Picks 2026" — 8 product images/names: Marker Squire 11, Salomon QST 94, Salomon Strive 14 GW, Salomon Strive 12 GW, Arcade Belts A2, ATK Freeraider 15 EVO, Rossignol Sender Free 110, Salomon QST 100 (no prices, quotes or staff names in the section)
7. "Buyers Guide" link
8. Email signup: "Sign Up For Our Emails" — "Ski deals, gear reviews, and stoke straight to your inbox"
9. Footer

### Seasonal featured categories/products
- Dated sale announcement bar; "Powder7 Top Picks 2026" grid; hero slides for used/demo/closeout; blog category "Brand Previews" for next-season gear ("2026-2027 Skis and Gear: Brand-by-Brand Insight").

### Staff picks / staff reviews
- Product-page module (example Salomon QST 94): label "This Ski Is A Staff Favorite:" then blocks "By: Caden", "By: Mo", "By: Dylan", each with staff photo, a mountain-icon image alt-texted "Staff Pick", and a paragraph review. First block shown; link "Read all of our Salomon QST 94 staff reviews" expands the rest. Fields: first name, photo, prose quote. No role, rating, height/weight or home mountain shown. Example quote: "This is a versatile, easy going ski that handles the whole mountain with confidence, but it really comes to life off piste."
- Below staff blocks: "Our Take On The 2027 Salomon QST 94:" shop-written paragraph.
- Product page also has spec table (Dimensions, Radius, Rocker, Ability Level, Construction), YouTube video, customer reviews.
- About page "Our Team" grid: 40+ staff with photo, name, hire year, role (e.g. "Zack / 2012 / VP of Merchandising and Inventory Planning"; "Chris T / 2015 / Controller"). Owners entry "Jordan & Amy / Owners / Founders" with multi-paragraph bio.

### Blog (`/ski-blog/`, "Lift Line Blog" in nav)
- Heading "Powder7 Ski Blog - Ski Culture, Trip Reports, and Skiing News".
- Category nav: `Blog Home | Gear Talk (Gear Reviews, Brand Previews) | The Ski Life (Ski Tips, News) | Places`; labels "Featured", "Trending", "Latest", "Gear Guide".
- Card: hero image, category tag(s), linked title, date (MM/DD/YYYY), linked author name, excerpt. Sidebar/sections: Featured Posts, The Ski Life, Gear Talk, Brand Previews.
- Recent: "Interview with a Badass: Heather Mullins of Après Ski Jewelry" (06/24/2026, Alex S); "How to Choose Ski Boots: A Ski Boot Buying Guide" (03/19/2026, Alex S); "2026-2027 Skis and Gear: Brand-by-Brand Insight" (01/28/2026, Powder7 Team).
- Article anatomy (brand preview): H1, publish date and "Last Modified" date, byline "Powder7 Team", hero image, lead ("Turns out, ski design isn't dead."), H2s "2027 Skis + Boots: Your First Look", "2027 Skis: Brand Previews", "Ski Boot Preview", 18 brand-preview links, related gear reviews (5) and destination articles (4), categories "Brand Previews, Trending, Gear Talk", CTA "Shop our selection of new and used skis". No author bio box, comments or inline email form.

### Email signup
- Footer: heading "Sign Up For Our Emails", subhead "Ski deals, gear reviews, and stoke straight to your inbox". No discount stated. Klaviyo present; modal not observable.

### Locations / hours
- Footer "Interact": "Call: (720) 674-5443", "Email", "Visit: Powder7 Ski Shop 880 Brickyard Cir. #150 Golden, CO 80403". Footer "Shop Info": "Hours + Golden, CO Shop Info", "Book An Appointment", "Ski Tunes + Binding Mounts", "Gift Certificates". Also "Online Bootfitting", "Live Help", "After Hours Assistance".
- Store page (`/golden-denver-ski-shop`): hours table (9:00am–7:00pm daily, closed July 4th, Thanksgiving, Christmas), address, phone, embedded Google Map, written drive times from Denver/Boulder/DIA, services list, appointment note ("To book your appointment, click here."), copy "you'll reach a real, live ski expert on-site in our Golden, Colorado headquarters."
- Services page (`/ski-tunes-binding-mounts-denver`): price/turnaround tables (e.g. "Ski Tune $75 2 days", "Mount (with both purchases) Free"), booking link `/appointments/hub`, "Wintersteiger automated tuning machine".

### Brands
- Nav "Brands" mega-menu: "Our Top Picks:" then A–Z text list. No logo row on homepage.

### Weather / snow report
None found.

---

## 4. Peak Performance Ski Shop — https://www.peakskishop.com/ (blog: `/blogs/the-edge/`)

**Platform signals:** "Powered by Lightspeed - Theme by Dyvelopment" in footer.

### Primary nav (verbatim, in order, with sub-labels)
`Home | Race Gear | Race Accessories | Luggage | All Mountain Gear | Clothing | Eyeware | Wax & Tuning Supplies | Service / Rentals | Sale | The Edge: Peak Performance Ski Shop Blog`
- Race Gear: Race Skis (Atomic, Dynastar, Fischer, Head, Nordica, Rossignol, Stockli, Volkl, VAN DEER-Red Bull Sports, Speed Skis (DH / SG)); Race Boots (by brand, Lifts, Accessories); Race Bindings (by brand); Race Poles & Pole Guards
- Race Accessories: Race Helmet (GS Helmet, Slalom Helmet, Chin Guards); Protection/Gloves (Back Protection, Stealth Top, Forearm Guards, Race Gloves/Mitts, Shin Guards); Race Suits / Clothing (Cut Protection, GS Race Suit, Rain Jackets, Side Zip Pants, Training Shorts)
- Luggage: Boot Bag, Ski Bag, Backpack
- All Mountain Gear: All Mountain Skis (by brand); Accessories; Skins; Ski Boots (by brand, Heaters); Ski Bindings (All Mountain Bindings, AT Bindings, Parts); Helmet; Gloves/Mitts; Ski Poles
- Clothing: Belts, Lifestyle, Jacket, Snow Pants / Bibs, Base Layers, Mid Layers, Socks (Unisex, Womens, Junior, Heated Socks), Shoes/Boots, Hats/Clavas
- Eyeware: Goggles (Poc, Atomic, Oakley, Shred, Smith, Sweet Protection, Revo), Replacement Lens
- Wax & Tuning Supplies: Wax, Tuning Tools
- Service / Rentals: Boot Work, Tuning/Wax, Race Base Structures, Mounting Services, Ski Rentals
- Sale: Skis - Demo, Skis - Race, Skis - All Mountain, Junior Skis, Race Ski Boots, Retail Ski Boots

### Homepage section order
1. Announcement bar: "End of Season Sale & 2027 Gear Arriving"
2. Header line: "Hours: Fri-Sun 10AM - 5PM"
3. Header line: "2027 Gear is Arriving" / "Get Ready for 26/27 Season"
4. Hero: "2027 VAN DEER" / "WELCOME TO A NEW ERA OF SKIING" / "SHOP NOW"
5. Banner: "2027 STOCKLI IN STOCK" / "EXPERIENCE THE DIFFERENCE" / "SHOP NOW"
6. Banner: "SKI RENTALS" / "MAKE YOUR RESERVATION TODAY" / "RESERVE NOW"
7. Banner: "GIFT CARDS" / "GIVE THE GIFT OF PERFORMANCE" / "BUY NOW"
8. "Our brands" logo row: Atomic, Energiapura, Fischer, Head, Lange, Nordica, POC, Rossignol, Stockli, Volkl
9. "CONTACT US" / "LOOK FORWARD TO HEARING FROM YOU" / "Click here"
10. About paragraph: "Peak Performance Ski Shop, a renowned ski retailer passionate about skiing. Named to the SKI Magazine Top 50 list of ski shops for multiple years…"
11. Newsletter: "Subscribe to our newsletter" / "And stay up to date with our latest offers"
12. Footer: address, phone, email; "Information" links; "My account" links; payment icons; social (Facebook, YouTube, Instagram)

### Seasonal featured categories/products
- Announcement bar and header lines reference "2027 Gear" and "26/27 Season"; hero banners are model-year-specific ("2027 VAN DEER", "2027 STOCKLI IN STOCK"). Category product names carry the year ("2027 REDSTER S9 FIS SL"); product badge "RACE PRICE".

### Staff picks / staff reviews
None found on homepage, category, blog or about pages. About page shows family/owner photos (Coriell family, Bair family) and a group team photo; no individual names/roles except owners. Boot Work page mentions "Certified Pedorthist on staff".

### Blog ("The Edge", `/blogs/the-edge/`)
- Heading "The Edge: A blog to elevate your Killington ski experience"; intro "Visit our blog, The Edge, where we share the latest developments and trends in skiing, ski racing, race skis, and race ski equipment so you can stay sharp on the slopes!"
- Reverse-chronological list, 5 per page, "Older posts" link. No category filters on the index; sidebar "Recent articles" (10 links).
- Card: featured image, linked title, date ("27 August 2026"), comment count, excerpt, "Continue reading article »".
- Recent titles: "Do Atomic Bindings Work on Stockli and Head Race Skis?", "Atomic Race Bindings Explained: Icon vs. X Series vs. Colt", "How to Choose the Right DIN Setting for Race Bindings", "FIS Back Protector Regulations: What Speed-Event Racers Need to Know", "How to Size a Ski Race Back Protector: C7 to Tailbone Method".
- Article anatomy: title, "Posted on 27 August 2026", no byline, hero graphic, lead ("Atomic splits its race bindings into three lines."), H2 sections ending in "Which Atomic Binding Should You Choose?" and "Frequently Asked Questions" with H3 questions, links to category pages, product images, Facebook Like plugin, "Recent articles" list, closing CTA "Stop by the shop or browse our full range of Atomic race bindings and we will help match the right model to your racer."

### Email signup
- Footer: "Subscribe to our newsletter" / "And stay up to date with our latest offers". No discount. No pop-up vendor detected in source.

### Locations / hours
- Single location. Header line "Hours: Fri-Sun 10AM - 5PM" on every page; footer "2808 Killington Road / Killington, VT 05751 / 802-422-9447". Boot Work page lists seasonal appointment hours ("Mon-Thu 1pm-5pm; Fri-Sun 12pm-5pm", summer by request) and "Make a Boot Fitting Appointment" button. About page: "Hours: By Appointment". No map found.

### Brands
- Homepage "Our brands" logo row; nav sub-menus are brand-organized (e.g. "Atomic Race Skis"); category sidebar "Brand" filter.

### Weather / snow report
None found.

### Category page notes (`/race-gear/race-skis/atomic-race-skis/`)
- Breadcrumb Home / Race Gear / Race Skis / Atomic Race Skis; "13 Products"; filters Price range, Brand, Categories; sort: Default, Most viewed, Newest products, Lowest price, Highest price, Name ascending, Name descending. Card: "RACE PRICE" badge, brand, model/year, price, "Quick shop", "Add to cart". Sibling brand links listed.

---

## 5. The Lost Co — https://thelostco.com/ (mountain-bike shop, Bellingham, WA)

**Platform signals:** Shopify (`/collections/`, `/pages/`, `/blogs/blog`); Klaviyo present. Collection product grids render client-side (not in fetched HTML).

### Primary nav (verbatim, in order, with sub-labels)
`Components | Accessories | Bikes | Brands | Tech | Blog | Service | Rentals | SALE`
- Components: Cockpit & Brakes (Grips, Handlebars, Headsets, Stems, Brakes, Brake Adapters, Brake Pads, Rotors); Suspension (Forks, Fork Parts, Rear Shocks, Rear Shock Parts, Coil Springs, Service Kits); Tires & Wheels; Drivetrain; Saddle & Seatpost; Small Parts; Frames (Full Suspension)
- Accessories: Things You Wear (Lost Co Merch, Backpacks & Hip Packs, Gloves, Goggles & Glasses, Helmets, Knee Pads); Bike Accessories; Maintenance; Tools

### Homepage section order
1. Top bar: "Welcome to the World's Local Bike Shop!" with country/currency selector
2. Announcement bar: "FREE USA Shipping over $75"
3. Hero carousel: "SHOP 2027 ORBEA WILD", RockShox suspension, Fox 38, "SHOP CABLE T-TYPE", "SHOP REVERB AXS", "SHOP 2026 X2 SHOCKS" (buttons "SHOP NOW")
4. "Best-Selling MTB Gear" product carousel: full product title, price, compare-at price struck, "Add to cart" or "Choose options", "View details" (e.g. "SRAM Maven Brake Lever Tuning Kit … $ 71.20 / $ 89.00")
5. "TOP CATEGORIES": "SHOP FORKS", "SHOP SHOCKS", "SHOP TIRES"
6. "OUR NEWEST VIDEO": "2027 RockShox Products Explained" (play button)
7. "New Blog Posts": eight linked titles (titles only, no images/dates in source)
8. Trust row: "5 STAR CUSTOMER SERVICE", "FAST FULFILLMENT", "45 DAY RETURNS"
9. Email signup: "STAY UP TO DATE WITH THE LATEST DEALS!" (Email field, "Subscribe")
10. Footer: "THE WORLDS LOCAL BIKE SHOP", "(360) 306-8827 // sales@thelostco.com", social (Facebook, YouTube, Instagram, TikTok), "MEDIA" (YouTube, Blog), "SUPPORT" (Returns, FAQ, Shock Hardware Database, Fox Spring Fitment, Spring Calculator, Fork Oil Volumes), "COMPANY" (About Us, Contact Us, Hours and Location, Service Center, Mail-In Service, Careers, Sponsorships, Terms & Conditions), payment icons

### Seasonal featured categories/products
- Model-year hero slides ("2027 ORBEA WILD", "2026 X2 SHOCKS"); "Best-Selling MTB Gear" carousel; nav "SALE". No season-labeled category section.

### Staff picks / staff reviews
- No site-wide staff picks module. Staff content is a blog post: "The Lost Co Bike Checks | What We Ride" (`/blogs/blog/lost-co-staff-bike-checks`, June 15, 2026, byline Tor Weiland). Lead: "With all these fancy new bike parts flying through The Lost Co every day, it's time we take a look at what's caught our attention and made its way onto our personal rigs." Structure: "Intro", then H3 per staff member ("Mindy", "Adam", "Chris", "Colton", "Will"), each with name, role, bike photos, bike model/year, parts spec list, setup notes; then "Conclusion", "Shop Now!" product cards, "About the Rider/Writer", "Got questions?".
- About page (`/pages/about-us-the-lost-co`): heading "THE STORY OF THE LOST CO"; lead "The Lost Co was started back in 2016 as Mister Lost's Mobile Bike Shop with a retired Uhaul truck."; team cards with name, title, photo, bio: Steve – Co-Owner & Buyer; Mindy – Co-Owner & Strategizer; Colton – Sales, Service & Demo Specialist; Mike – Marketing Director; Alex – Tech Advisor & Expert Mechanic; Adam – Fulfillment Specialist; Chris – Customer Service; Tor – Content Creator. CTA "ARE YOU INTERESTED IN JOINING OUR TEAM?"

### Blog (`/blogs/blog`)
- Heading "The Lost Co Blog". List view: linked title, author ("Tor Weiland"), date; no excerpt, image or tags in fetched list. "Showing 12 of 243" with "Show more". Sidebar: email box, trust badges, contact, social.
- Article anatomy ("Signature MTB Grip Shootout", July 24, 2026): title, date, byline "Tor Weiland", hero image, lead ("It seems like every pro rider has their own signature grips these days…"), sections "Watch the Video!" (YouTube embed), "Shop Now!" (product cards: name, price, e.g. "OneUp Jackson Goldstone Lock-On Grips (Black) - $29.99"), "About the Rider/Writer" (author box: "Tor Weiland | Age 27 | 5'11" | Bellingham, WA", "Rides: Transition Sentinel, Transition TR11"), "Got questions?", previous/next post links. No tags, comments or share buttons observed.

### Email signup
- Footer/sidebar: "STAY UP TO DATE WITH THE LATEST DEALS!" — Email field + "Subscribe". No discount stated. Klaviyo present; modal not observable.

### Locations / hours
- `/pages/hours-and-location`: heading "Hours and Location"; "Local Store Hours: Monday - Friday: 10 am - 6 pm PT Saturday & Sunday: CLOSED"; "Phone and Live Chat Hours: Monday - Friday: 10 am - 5 pm PT Saturday & Sunday: CLOSED"; "2106 Pacific St Ste 101, Bellingham, WA 98229"; phone; email. No map, no seasonal notes, single location.
- Service page (`/pages/mtb-full-service-suspension-shop`): heading "MTB Full Service & Suspension Shop"; lead "While we are renowned for our industry-leading suspension service offerings, The Lost Co is a full-service mountain bike shop."; three-tier comparison table (Hot Lap Tune, Session Tune, Full Send Tune) without prices; mail-in five-step process ("Fill out the form HERE"); "our shop is staffed by elite mechanics who live and breathe MTB performance".

### Brands
- Nav "Brands" item; collection intro copy links brands inline ("Shop forks from top brands like Fox Racing Shox, RockShox, Marzocchi, Ohlins, MRP, DVO and more!"). No logo row observed in homepage source.

### Weather / snow report
None (bike shop; no trail-condition element found).

### Category page notes (`/collections/forks`)
- Heading "MTB Suspension Forks"; breadcrumb Home > MTB Suspension Forks; intro "The quality of the suspension fork on the front of your mountain bike can make or break your ride." Product grid, filters and sort are JS-rendered and not present in fetched HTML; product cards elsewhere on site use title, price, struck compare-at price, "Add to cart"/"Choose options", "View details".

---

## Comparison table

| Site | Nav pattern | Seasonal featured cards | Staff picks format | Blog structure | Email capture | Locations/hours | Brands display |
|---|---|---|---|---|---|---|---|
| SkiEssentials | 11 top-level: SKI, CROSS-COUNTRY, SNOWBOARD, PACKAGES, APPAREL, ACCESSORIES, BIKE, BRANDS, CHAIRLIFT CHAT, 2026 PRICE DROPS, OUTLET | "2027 SKI & BINDING COMBO DEALS" heading; 4 category tiles + 4 brand tiles with "SHOP NOW"; "2026 Price Drop" badges; "Year" facet | Annual Ski Test hub: tester cards (name, photo, age, height, weight, style), per-ski tester cards with 8 scored categories (0–10) + quote; no roles | "Chairlift Chat": 10 category filters; card = image, title, date, categories, excerpt, "SHOW MORE"; article has byline, spec tables, "Buy Now", related, comments | Footer embedded form "SIGN UP FOR EXCLUSIVE DEALS"; no incentive stated | One store; address/phone/"Mon-Fri: 9:00 AM-5:00 PM" in footer; no location page | Homepage 4 brand tiles; "SHOP ALL BRANDS" page = featured logo grid + A–Z list |
| Peter Glenn | 16 top-level by sport/gender/footwear + Brands, Blog, New, Sale | "Pre-Season Sale", "Winter Sale: Save up to 60% Off!", holiday gear guide; "UP TO [%] OFF" badges | Single celebrity reviewer block: "Jonny Moseley Product Reviews", "Chief Testing Officer", CTA "CHECK THEM OUT" to tagged search results | Flat list, no categories; 5/page paginated; card = square image, title, "Posted by Peter Glenn Staff on [date]", excerpt, "[read more]"; share buttons in article | Footer "Get exclusive Peter Glenn offers" + "We will not share your info with anyone." | Locations page grouped by state with address/phone + detail pages showing hours, closures, manager, map, photo | Homepage logo row (15 logos) linking to brand pages; Brand facet |
| Powder7 | 10 top-level product types + Brands, More; mega-menus with size/weight/height shopping | Dated sale bar; hero slides used/demo/closeout; "Powder7 Top Picks 2026" 8-product grid (no copy) | Product page "This Ski Is A Staff Favorite:" — "By: [first name]", photo, "Staff Pick" icon, prose review; expand link "Read all of our … staff reviews"; then "Our Take On…" | Categories: Gear Talk (Gear Reviews, Brand Previews), The Ski Life (Ski Tips, News), Places; card = image, tag, title, date, author, excerpt; article has related posts, last-modified date | Footer "Sign Up For Our Emails" / "Ski deals, gear reviews, and stoke straight to your inbox" | One store; footer address/phone; store page with hours table, map, drive times, appointment link; services price tables | Nav "Brands" mega-menu: "Our Top Picks:" + A–Z list; no logo row |
| Peak Performance | Race-first: Race Gear, Race Accessories, Luggage, All Mountain Gear, Clothing, Eyeware, Wax & Tuning Supplies, Service / Rentals, Sale, blog; sub-menus by brand | Header "2027 Gear is Arriving / Get Ready for 26/27 Season"; hero "2027 VAN DEER", "2027 STOCKLI IN STOCK"; "RACE PRICE" badge | None; owner/family photos on About; "Certified Pedorthist" mention | "The Edge": flat reverse-chron, 5/page, "Older posts"; card = image, title, date, comment count, excerpt, "Continue reading article »"; no byline; FAQ H3s; "Recent articles" sidebar | Footer "Subscribe to our newsletter" / "And stay up to date with our latest offers" | One store; "Hours: Fri-Sun 10AM - 5PM" in header on every page; footer address/phone; appointment hours on Boot Work page | "Our brands" logo row (10) on homepage; brand-named sub-categories |
| The Lost Co | 9 top-level: Components, Accessories, Bikes, Brands, Tech, Blog, Service, Rentals, SALE; deep component sub-menus | Model-year hero slides ("2027 ORBEA WILD"); "Best-Selling MTB Gear" carousel; "TOP CATEGORIES" 3 tiles | Blog post "The Lost Co Bike Checks | What We Ride": H3 per staff (name, role, bike, parts list, notes); About team cards (name, title, photo, bio) | Flat list, "Showing 12 of 243" + "Show more"; list = title, author, date; article = video, "Shop Now!" product cards, "About the Rider/Writer" box (age, height, city, bikes) | Footer/sidebar "STAY UP TO DATE WITH THE LATEST DEALS!" | One store; "Hours and Location" page with store hours and phone/chat hours; no map | Nav "Brands"; brands linked inline in collection intro copy; no logo row |

Weather/snow report element: none found on any of the five sites.
