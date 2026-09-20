# Content data pulled from Rodgers' own channels (verbatim quotes) and the live site.
# Sources: resources/research/social-instagram-index.md, social-tiktok-facebook-index.md, live-site-index.md

STAFF_PICKS = [
 dict(who="Robbie", store="Lincoln, NH", product="Elan Ripstick 96 Black", img="staffpick-robbie-elan-ripstick-96.jpg",
      quote="In the days of the 1 ski quiver, the Elan Ripstick 96 Black stood out from the rest as a lightweight, agile platform that hard charges on the downhill, and performs when you want to play and get creative. Those days are over, but the Ripstick is still here. This would be a great addition to a quiver, or could be that one ski that you drive daily, and at $699 including bindings, someone's going home with an absolute steal on this ski.",
      date="September 16, 2026", tag="Fall Tent Sale pick &middot; $699 with bindings", link="https://www.instagram.com/rodgersski/p/DdVzn18Fd-4/"),
 dict(who="Denis", store="Lincoln, NH", product="Atomic Redster 130 World Cup Race Boot", img="staffpick-denis-atomic-redster-130.jpg",
      quote="The Atomic Redster 130 World Cup Race Boot offers a race-focused shell and narrow World Cup fit that delivers exceptional power, precision, and edge control for aggressive skiing.",
      date="September 9, 2026", tag="Race boot &middot; fitted in the Boot Lab", link="https://www.instagram.com/rodgersski/p/DdEYmUwHG6V/"),
 dict(who="Jamie", store="Lincoln, NH", product="Atomic Arc 735 RS", img="staffpick-jamie-atomic-arc-735.jpg",
      quote="One of the most enjoyable mid-radius carvers on the market in the X9S &mdash; the limited edition 1990-91 Arc graphic will make all your friends jealous and be a conversation starter in the lift line.",
      date="September 2, 2026", tag="Carving ski &middot; limited-edition graphic", link="https://www.instagram.com/rodgersski/p/DcydGjmoAxY/"),
 dict(who="Avery", store="Lincoln, NH", product="Blizzard Black Pearl", img="staffpick-avery-blizzard-black-pearl.jpg",
      quote="The two-piece Titanal layup gives you real edge hold on the hardpack, but the women's-specific wood core keeps it light and playful enough to throw around all day.",
      date="August 27, 2026", tag="Women&rsquo;s all-mountain", link="https://www.instagram.com/rodgersski/p/DcjXRPmznBl/"),
]

# Journal posts. Content drawn from Rodgers' posts, July–September 2026. `img` from the in-house library or vendor.
POSTS = [
 dict(slug="journal-fall-tent-sale.html", cat="Promotions", date="September 18, 2026", title="The Fall Tent Sale is on: September 18 to October 12 in Lincoln",
      img="lincoln-service-desk-ski-front.jpg", alt="Race skis lining the front of the Lincoln service desk",
      teaser="Our biggest deals of the year are back under the tent on Railroad Street: skis, snowboards, boots, apparel, helmets and everything in between. Staff picks and deal reveals all sale long."),
 dict(slug="#", cat="New arrivals", date="September 14, 2026", title="The 2027 Smith goggles just landed at Rodgers Lincoln",
      img="smith-goggle-case.jpg", alt="Smith goggles in the lit display case",
      teaser="ChromaPop clarity, dialed-in fit, colorways for days. Come see the wall for yourself."),
 dict(slug="#", cat="Services", date="September 11, 2026", title="Inside binding mounting and testing at the Scarborough shop",
      img="scarborough-atomic-boot-bench.jpg", alt="Race boot on the bench under the Atomic sign in Scarborough",
      teaser="Mounted, adjusted, tested. Every pair is checked before it leaves our hands. Get your setup ready for the season."),
 dict(slug="#", cat="New arrivals", date="September 4, 2026", title="Unwrapping the new K&auml;stle Paragon 93",
      img="lincoln-ski-wall-armada-salomon.jpg", alt="New-season skis on the Lincoln wall",
      teaser="The Paragon 93 is in the store now. Come check them out."),
 dict(slug="#", cat="Brands", date="August 27, 2026", title="Atomic Day recap: the full 2027 lineup is on the floor",
      img="atomic-factory-redster.jpg", alt="Atomic Redster race skis on the factory line",
      teaser="Skis, bindings, boots and race skis just hit the shop floor. Stop in and get your hands on next year&rsquo;s gear first."),
 dict(slug="race.html", cat="Racing", date="August 24, 2026", title="Race gear walkthrough: seven race brands, all in one spot",
      img="lincoln-race-wall.jpg", alt="Race skis from Fischer, Rossignol, Head and Dynastar on the Lincoln wall",
      teaser="Avery gives the full lineup at the Lincoln shop: Atomic, Fischer, Head, Rossignol, Dynastar, Van Deer and Salomon race skis. Whether you&rsquo;re gate training or chasing PRs, we have the setup to match your program."),
 dict(slug="#", cat="Services", date="August 6, 2026", title="Off-season tune-ups: our techs are servicing gear all summer",
      img="montana-stone-grinder.jpg", alt="Skis on the Montana stone grinder in the Lincoln tune room",
      teaser="Summer&rsquo;s here, but your gear still needs love. Off-season tune-ups mean your skis and boards are ready to rip the second the snow flies. Don&rsquo;t wait till November."),
 dict(slug="#", cat="Promotions", date="July 20, 2026", title="The Tent-Less Tent Sale: Scarborough gets its own summer sale",
      img="scarborough-storefront-sunny-wide.jpg", alt="The Scarborough store on Route 1",
      teaser="Same markdowns as the Lincoln tent sale, just under an actual roof. Skis, boots, bindings, complete junior packages and helmets, July 24 through August 9."),
]

CATEGORIES = ["All","News","Promotions","Racing","Brands","New arrivals","Services","Local mountains"]

PARTNERS = [
 dict(name="South Peak Resort", kind="Resort community &middot; Lincoln, NH", url="https://www.southpeakresort.com/",
      blurb="A 360-acre slopeside community on Loon Mountain in Lincoln, with homesites, townhomes, condos and rentals. Rodgers is minutes from the resort on Railroad Street."),
 dict(name="Loon Mountain Resort", kind="Ski area &middot; Lincoln, NH", url="https://www.loonmtn.com/",
      blurb="Year-round adventure in New Hampshire&rsquo;s White Mountains. The Lincoln store is right down the street: gear up, rent, or tune before you reach the base lodge."),
 dict(name="Cannon Mountain", kind="Ski area &middot; Franconia, NH", url="https://www.cannonmt.com/",
      blurb="The state-run ski area in Franconia Notch State Park, a short drive north of Lincoln on I-93."),
 dict(name="Bretton Woods", kind="Ski area &middot; Bretton Woods, NH", url="https://www.brettonwoods.com/",
      blurb="New Hampshire&rsquo;s largest ski area, with alpine and Nordic skiing at the Omni Mount Washington Resort."),
 dict(name="Western White Mountains Chamber of Commerce", kind="Chamber &middot; Lincoln &amp; Woodstock, NH", url="https://www.westernwhitemtns.com/",
      blurb="Promotes the Lincoln and Woodstock area as a basecamp for the White Mountains: lodging, dining, events and seasonal activities."),
]

RACE_BRANDS = ["Atomic","Van Deer","Head","Rossignol","Fischer","Dynastar","Salomon"]
# From the shop's handwritten brand sheet (Sept 2026)
SKI_BRANDS = ["Rossignol","Dynastar","Head","K&auml;stle","Elan","Atomic","Van Deer","Salomon","Armada","V&ouml;lkl","Fischer","Blizzard"]
BOOT_BRANDS = ["Lange","Salomon","Atomic","Rossignol","Head","Van Deer","Tecnica","Nordica","Fischer","Dalbello","Armada"]
RACE_BOOT_BRANDS = ["Rossignol","Lange","Atomic","Nordica","Head","Fischer","Salomon"]
RACE_BINDING_BRANDS = ["Marker","Look","Atomic","Head","Fischer","Salomon"]
RACE_POLE_BRANDS = ["Komperdell","Swix","Leki","Atomic"]
FREERIDE_BRANDS = ["Rossignol","Armada","Atomic","V&ouml;lkl","Fischer","Elan"]
BINDING_BRANDS = ["Atomic","Marker","Salomon","Look","Tyrolia"]
SNOWBOARD_BRANDS = ["Academy","Never Summer","Arbor","Rome","ThirtyTwo","Lib Tech","GNU","Bataleon","Nidecker","Yes","Salomon"]
SB_BOOT_BRANDS = ["Nidecker","Salomon","Deeluxe","ThirtyTwo","Bataleon"]
SB_BINDING_BRANDS = ["Union","Rome","Bataleon","Salomon","Nidecker","Yes","Flow"]
HELMET_GOGGLE = ["Atomic","Smith","Giro","Oakley","POC","Sweet Protection"]
GLOVES = ["Hestra","Swany","Gordini","Dakine"]
HEATED = ["Hestra","Lenz","Hotronic"]
HATS = ["Seirus","Turtle Fur","Coal","Starling","Eisb&auml;r"]
BAGS = ["POC","Atomic","Energiapura","Rossignol","Db","Athalon","Kulkea","Cotopaxi","Mammut","Dakine"]
MENS_OUTERWEAR = ["Arc&rsquo;teryx","Descente","Karbon","Mammut","Salomon","Scott","Norr&oslash;na","Kjus","Flylow","Quiksilver","RH+","686","Helly Hansen","Picture","Armada"]
WOMENS_OUTERWEAR = ["Arc&rsquo;teryx","Toni Sailer","Karbon","Mammut","Scott","Norr&oslash;na","Goldbergh","Flylow","Roxy","Jorde","686","Bogner","Fera","Picture"]
KIDS_OUTERWEAR = ["Helly Hansen","Karbon","Flylow"]
LAYERS = ["Kari Traa","Smartwool","Hot Chillys","Krimson Klover","UYN"]
SWEATERS = ["Dale of Norway","Meister","Krimson Klover","Almgwand"]
BIKE_BRANDS = ["Trek","Electra","Jamis","Scott"]

# Lincoln tune board (photographed Sept 2026)
LIN_TUNES = [("Bronze tune<small>Quick clean-up tune before hitting the slopes</small>","$40"),("Silver tune<small>Routine maintenance for the weekend warrior</small>","$60"),
             ("Gold tune<small>Been a while? Skis need a little extra love; brings them back to their former glory</small>","$75"),
             ("Platinum tune<small>The best of the best: highest performance rec tune and the perfect beer-league race tune</small>","$85"),
             ("The Full Monty<small>The works: Platinum tune with minor P-tex base welds</small>","$99")]
# Lincoln binding board
LIN_MOUNT_REC = [("Binding mount or re-mount","$100"),("System binding mounting","$75"),("Binding adjustment and function test","$50")]
LIN_MOUNT_RACE = [("Race mount with purchase","$25"),("Race binding transfer","$75"),("Race binding lifter install<small>Toe and heel height set to FIS regulation, to the athlete&rsquo;s, coach&rsquo;s or race tech&rsquo;s request</small>","$100")]
# Race department board and price list (Rodgers purchase / outside purchase)
RACE_SKI = [("Podium Club<small>Season ski tuning, one ski, unlimited, includes prep</small>","$350/pair","n/a"),
            ("FIS race ski prep<small>Shaped sidewalls, World Cup structure, Trione edges, race wax</small>","$200","$250"),
            ("USSA race ski prep<small>Sidewall pull, World Cup structure, belt edge and base, race wax</small>","ask","$200"),
            ("Junior race ski prep (U10/U12)<small>Stone grind flat, belt edge angles, one wax cycle</small>","$60","$75"),
            ("Race ski grind only<small>Flat ski, World Cup structure, no edge bevels</small>","$85","n/a"),
            ("Race day tune<small>Trione edges, race wax; sidewall must be cut to qualify, no grind</small>","$65","$75")]
RACE_BOOT = [("FIS race boot setup<small>Custom footbeds, grind, alignment, plane, cant, lift, router</small>","$300","$400"),
             ("USSA race boot setup<small>Sidas drop-in footbed, alignment, plane, cant, lift, router</small>","$150","$250"),
             ("Custom footbed<small>Build and install</small>","$175","$200"),
             ("Cant analysis<small>Laser alignment with cuff adjustment</small>","$50","$100"),
             ("Boot sole plane<small>0 to 5 degrees in quarter-degree increments, one pair</small>","$75","$150"),
             ("Boot lifter install with router<small>Pre-drill, fit, router toes and heels to DIN spec</small>","$75","$125"),
             ("Shell molding<small>Custom shell / Memory Fit oven heat molding</small>","varies","varies"),
             ("Shell grind or stretch","varies","varies"),
             ("Heater install<small>New or transfer; may require additional parts</small>","$35","$50"),
             ("Labor rate","$60/hr","$80/hr")]
RACE_BINDING = [("Binding install, new pre-drill<small>Mount, test binding and lifters (parts not included)</small>","$25","$50"),
                ("Binding transfer, pre-drill<small>Remove, remount, test</small>","$50","$75"),
                ("Race plate optimization<small>Drill plate, mount, test</small>","$100","$150"),
                ("Binding lifters<small>Manufacturer specific, measured for optimization</small>","$100","$150")]
LIN_BOOTLAB = [("FIS boot prep","$300"),("USSA boot prep","$200"),("Outside boot (add)","+$100"),("Custom insoles","$200"),("Punch or grind","$35"),("Stance &amp; alignment","$50"),("Canting","$75 per foot"),("Lifters installed","$65"),("Labor rate","$60/hr")]
# Rental rates (handwritten sheet, Sept 2026): 1 to 5 days
LIN_RENTALS = [("Junior package","$20","$35","$50","$65","$75"),("Performance shape skis","$45","$87","$129","$168","$200"),("Advanced shape skis","$50","$97","$144","$188","$235"),
               ("Demo skis","$75","$145","$210","$275","$325"),("Snowboard package","$45","$87","$129","$168","$200"),("Cross-country package","$25","$45","$65","$85","$105"),
               ("Snowshoes","$25","$45","$65","$85","$105"),("Helmet","$10","$10","$10","$10","$10")]
LIN_BIKE = [("Bronze bike tune","$50","Adjust brakes and shifting, check bolts, lube moving parts, wipe down, inflate tires"),
            ("Silver bike tune","$99","Bronze, plus: chain, rear cogs and front crank cleaned, wheels trued, braking surfaces cleaned"),
            ("Gold bike tune","$149","Silver and Bronze, plus: replace and adjust shifting and brake cables and housing, hydraulic brake bleed, inspect bearings")]
SCA_TUNES = [("Basic ski tune","$40"),("Basic board tune","$50"),("Stone grind","$60"),("Race tune","$100"),("Add premium wax","$20"),("P-tex repair","$5+"),("Base weld","$15+")]
SCA_BOOTLAB = [("Shell heat mold","$50"),("Liner heat mold","$40"),("Punch out","$25 each"),("Spot grind","$15 each"),("Heel lifts","$200"),("Misc. boot work","$50/hr")]
SCA_MOUNT = [("Mount","$90"),("Free with purchase of two of three (ski, boot, binding)",""),("Half price with purchase of one of three",""),("Adjustment &amp; test","$40")]
SCA_BIKE = [("The safety check","$50","20-point inspection of the frame and component system; every bolt, bearing and alignment verified"),
            ("The standard tune","$100","Safety check, plus: gear indexing and derailleur alignment, pad and cable tension, housing, tire and tube inspection"),
            ("Standard build","$75","Professional assembly for bikes purchased elsewhere or shipped to the store"),
            ("E-bike build","$175","Assembly for e-bikes purchased elsewhere or shipped to the store")]
LEASE = dict(price="$159", includes="Skis, bindings and boots", pickup="Lease pick-ups begin October 1. No appointment needed; walk in and one of our staff will get you outfitted.",
             end="Latest drop-off is May 1, unless you are still skiing (call to let us know and avoid late fees). Drop-offs after the month of May are subject to a $159 charge.",
             fit="For kids age 2 to 13, up to 130 lbs. Beginner to intermediate. Ski sizes 70 to 150 cm; boot sizes 14.5 to 26.5.")
# Fall Tent Sale notes (shop sheet, Sept 2026)
TENT_DEALS = ["2026/27 demos and pre-mounted skis from Atomic, Blizzard, V&ouml;lkl, Head, Elan, Rossignol, Nordica, Fischer and Salomon",
              "Nordica men&rsquo;s and women&rsquo;s alpine boots from $199","Rossignol Alltrack 110 W and 130 M boots, $499","Prior-year Head boots 50% off","Left-over boots up to 70% off","All helmets from $69"]
# Employment (from the shop's hiring posts, Sept 2025)
JOBS = [dict(title="Sales associate", store="Lincoln, NH and Scarborough, ME", type="Full-time or part-time, seasonal",
             blurb="Help skiers, riders and families find the right gear and get them out the door happy. No experience required; we&rsquo;ll train. A love for outdoor activities is the requirement."),
        dict(title="Ski technician", store="Lincoln, NH and Scarborough, ME", type="Full-time or part-time, seasonal",
             blurb="Tunes, mounts and race prep on the Montana machines, alongside techs who have been doing this for years. No experience required; we&rsquo;ll train.")]


# ---- homepage seasonal call-outs (four per season; chosen by build month, a Payload list in production)
SEASON_OF = {12:"winter",1:"winter",2:"winter",3:"winter",4:"spring",5:"spring",6:"summer",7:"summer",8:"summer",9:"fall",10:"fall",11:"fall"}
SEASON_TITLE = {"fall":"This fall","winter":"This winter","spring":"This spring","summer":"This summer"}
SEASON_CARDS = {
 "fall": [
  ("journal-fall-tent-sale.html","scarborough-tent-sale.jpg","The Fall Tent Sale in Lincoln","Fall Tent Sale","Skis, snowboards, boots, apparel and helmets under the tent in Lincoln, September 18 to October 12.","Sale details"),
  ("boot-lab.html","lincoln-boot-lab-room.jpg","The Boot Lab in Lincoln","Boot fitting","Book a fitting before the first cold weekend: shell fit, footbeds, punches and grinds at both stores.","The Boot Lab"),
  ("lincoln-nh-services.html","lincoln-tune-room-machines.jpg","Montana machines in the Lincoln tune room","Pre-season tune","Bring last winter&rsquo;s skis and boards in now and skip the December line.","Tuning menu"),
  ("lease.html","scarborough-ski-rows.jpg","Skis at the Scarborough store","Junior Seasonal Lease","Skis, bindings and boots for the season at the Scarborough store; pick-ups start October 1.","Lease details"),
 ],
 "winter": [
  ("rentals.html","lincoln-service-desk.jpg","The rental and service desk in Lincoln","Rentals","Junior, performance, advanced and demo skis, snowboards, cross-country and snowshoes at the Lincoln store.","Rates and reservations"),
  ("boot-lab.html","lincoln-boot-lab-room.jpg","The Boot Lab in Lincoln","Boot fitting","Cold feet, shin bang and heel lift are fixable; book a fitting.","The Boot Lab"),
  ("race.html","lincoln-race-wall.jpg","The race wall in Lincoln","Race department","Seven race brands, race day tunes and FIS and USSA prep.","Race gear"),
  ("lincoln-nh-accessories.html","giro-helmet-wall.jpg","Helmets on the wall","Helmets, goggles and gloves","Warm hands and clear lenses from Hestra, Smith, Giro, Oakley and more.","Accessories"),
 ],
 "spring": [
  ("lincoln-nh-bikes.html","lincoln-bike-service.jpg","Bike service in Lincoln","Bike tunes","Bronze, silver and gold tunes in Lincoln; safety checks and standard tunes in Scarborough.","Bike service"),
  ("lincoln-nh-bikes.html","bike-jamis-dakar.jpg","A Jamis mountain bike","Bikes","Mountain, road, gravel, hybrid, cruiser, kids&rsquo; and e-bikes from Trek, Jamis, Scott and Electra.","Bikes"),
  ("lincoln-nh-services.html","tuning-montana.jpg","Skis on the Montana grinder","End-of-season tune","A tune and storage wax now means sharp edges on opening day.","Tuning menu"),
  ("lincoln-nh-apparel.html","lincoln-apparel-floor.jpg","The apparel floor in Lincoln","Spring apparel","Shells, layers and lifestyle pieces for the shoulder season.","Apparel"),
 ],
 "summer": [
  ("lincoln-nh-bikes.html","bike-mtb-trail.jpg","A mountain biker on a forest trail","Mountain and e-bikes","Trail, road, gravel and e-bikes in both stores.","Bikes"),
  ("scarborough-me-bikes.html","scarborough-bike-shop.jpg","The bike shop in Scarborough","Bike service","Tunes, safety checks and custom builds, including bikes bought elsewhere.","Bike service"),
  ("outdoor-guide.html","hero-hiker-ridge.jpg","A hiker on a ridge in the White Mountains","Outdoor guide","Trails, bike networks and mountains within reach of either store.","Outdoor guide"),
  ("lincoln-nh-apparel.html","lincoln-apparel-floor.jpg","The apparel floor in Lincoln","Summer apparel","Packs, layers and sun-ready pieces.","Apparel"),
 ],
}
