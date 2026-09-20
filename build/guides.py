# Buyer's Guide and Outdoor Guide pages. Product positioning verified against brand and
# retailer pages Sept 19, 2026 (see resources/research/guides-sources.md). Trail data verified
# against NH State Parks, US Forest Service, AMC, Maine Trail Finder, resort sites and NEMBA.
import json
from shell import *
from data import *
from pages import prod, brands

GMAPS_KEY = ""   # Google Maps JavaScript API key. Empty = the page renders the same data on Leaflet/OpenStreetMap.

# ---------------------------------------------------------------- Buyer's Guide
# Guidance verified against retailer buying guides (evo, REI, Powder7, Switchback Travel, Tactics, The Ski Monster),
# brand fit pages (Atomic, Rossignol, Nordica, Lib Tech, Never Summer), bootfitter sources (Bootfitters.com, Wayfinder),
# SkiTalk forum threads, US Ski & Snowboard equipment rules and The Pro Ski & Ride junior racing guide. Sources listed in
# resources/research/guides-sources.md.

RULES = [
 ("Ski length by ability", ("Ability","Length"), [
   ("First-timer / beginner","Tip at the chin"),
   ("Intermediate","Between the chin and the nose"),
   ("Advanced / expert","Top of the head or longer")],
  "Go shorter if you are lighter, groomer-focused or carving; longer if heavier, faster, off-piste, or on a powder ski with a lot of rocker. Longer is not automatically more stable."),
 ("Ski waist width", ("Width","Use"), [
   ("Under 80 mm","Carving and firm snow"),
   ("80&ndash;89 mm","Frontside; the East Coast all-day width"),
   ("90&ndash;99 mm","All-mountain"),
   ("100&ndash;109 mm","All-mountain with a soft-snow lean"),
   ("110 mm and up","Powder")],
  "Turn radius: under 16 m is a short, carving turn; 17 to 22 m is the all-mountain middle; over 22 m is a long, big-mountain turn."),
 ("Ski boot flex", ("Ability","Men / Women"), [
   ("First-timer to beginner","60&ndash;80 / 50&ndash;60"),
   ("Intermediate to advanced","85&ndash;100 / 65&ndash;80"),
   ("Advanced to expert","110&ndash;120 / 85&ndash;100"),
   ("Expert and race","130 and up / 110 and up")],
  "Weight moves the number: a lighter skier needs a softer boot to flex it, a heavier skier a stiffer one. When in doubt, go softer. Fit matters more than any flex number."),
 ("Boot last (width)", ("Last","Foot"), [
   ("97&ndash;98 mm","Narrow, low-volume"),
   ("100 mm","Average"),
   ("102&ndash;106 mm","Wide or high-volume")],
  "Last numbers describe a neighborhood, not a guarantee. The shell fit on the bench decides."),
 ("Snowboard length by weight", ("Rider weight","All-mountain / Freestyle"), [
   ("80&ndash;120 lb","140 / 135 cm"),
   ("110&ndash;140 lb","147 / 142 cm"),
   ("125&ndash;155 lb","150 / 145 cm"),
   ("145&ndash;170 lb","156 / 151 cm"),
   ("160&ndash;190 lb","160 / 155 cm"),
   ("175&ndash;205 lb","163 / 158 cm"),
   ("185 lb and up","165 / 160 cm")],
  "Weight and boot size decide board size; the old nose-to-chin rule does not. Boot size 11 and up should look at a wide board."),
]

SKIER_TYPES = [
 dict(k="first", n="First-time adult", who="New to the sport or back after a long gap.",
  skis="Length at the chin, or about 10 to 15 cm below your height. A carving or frontside width of 78 to 88 mm, which is where most rental skis sit, with a short 13 to 14 m radius, a little tip and tail rocker over traditional camber, and a soft flex. Wood cores give more life than foam; either is fine for a first ski.",
  boots="Flex in the 60 to 80 range for men and 50 to 60 for women, at your measured Mondopoint or slightly longer. Do not buy the roomiest boot in the store because it feels best in the shop; liners pack out and every boot gets looser. Boots come before skis.",
  board="See the snowboard section: soft flex, rocker or flat profile, a true twin.",
  mistakes="Buying skis first and boots last. Sizing boots for shop comfort. Choosing a stiff expert ski because it was on sale.",
  examples="Rossignol Experience 78 and 82 Ti, Elan Wingman 78 C. Rossignol Evo 70 boot (104 mm last, 70 flex). Or rent for a season at the Lincoln counter and buy boots first."),
 dict(k="cruise", n="Leisurely adult on greens and easy blues", who="Happy to be on the mountain, in no hurry to ski faster or steeper.",
  skis="The same chin-to-nose length and frontside width as a first-timer, with a short radius so the ski turns on its own. Lighter, no-metal constructions suit cruisers who never push into refrozen chop; the trade is less grip when the groomers turn to ice, which is worth a conversation on the floor before buying.",
  boots="A beginner-to-intermediate flex and a fit chosen for warmth and ease of entry. Softer boots forgive imperfect technique. If your feet run cold, ask about insulated liners and heated socks before sizing up.",
  board="",
  mistakes="Being talked into a two-sheet-metal ski meant for speed. Choosing a 130 flex boot for status.",
  examples="Rossignol Experience 82 Ti, Elan Ripstick 88, Nordica Unleashed 90; K&auml;stle&rsquo;s lighter TX line for the weight-conscious. Boots: Atomic Hawx Prime 90 or 100, Nordica Sportmachine, Tecnica Mach1 110."),
 dict(k="older", n="Older adult", who="Fifty-five and up, with warmth, easy entry and low effort at the top of the list.",
  skis="A relatively soft flex so the sidecut engages with little effort, in a frontside width, sized chin to nose. Lighter skis reward the athletic skier who now prefers to take it easier; demo before buying.",
  boots="Look at ease of entry and exit first: rear-entry designs, wide-opening shells and walk modes make a difference on a cold morning. Padded, insulated liners and grippy walkable soles matter. Nordica&rsquo;s HF rear-entry line (102 mm, flex 75 to 120) and Sportmachine (102 mm with a soft-flap entry) and Atomic&rsquo;s Hawx Magna 100 (102 mm) are built for this. No maker publishes an age-specific flex; use the weight table and go softer.",
  board="Riders with joint concerns tend to do better on a softer, forgiving profile than on full camber.",
  mistakes="Assuming the boot that was right at 40 is right at 65. Skipping the demo.",
  examples="Nordica HF, Nordica Sportmachine, Atomic Hawx Magna, Tecnica Mach1 HV. Skis: Rossignol Experience 82 Ti, Elan Ripstick 88."),
 dict(k="prog", n="Progressing intermediate", who="Parallel turns on blues, starting to ski faster and in more places.",
  skis="Chin-to-nose length, 80 to 95 mm for Eastern snow, a 16 to 20 m all-round radius, moderate stiffness for stability at speed, a stronger wood core and sidewall construction, and a hybrid rocker-camber profile. Metal is optional: it adds damping and edge hold on ice, not much weight, and some intermediates prefer it.",
  boots="Flex 85 to 100 for men and 65 to 80 for women, and a closer fit than the first pair. This is the stage where a proper footbed pays for itself.",
  board="",
  mistakes="Staying on a chin-height beginner ski and a soft boot after the technique has moved on. Assuming metal is required.",
  examples="Elan Ripstick 88, Nordica Unleashed 90, Salomon QST 94, Blizzard Black Pearl 88 (women), V&ouml;lkl M7 Mantra for the stronger intermediate. Boots: Atomic Hawx Prime 100 and 120, Tecnica Mach1 110 and 120."),
 dict(k="adv", n="Advanced all-mountain", who="Skis the whole mountain in most conditions and wants one setup that does it all.",
  skis="Nose-to-head length or longer, 88 to 102 mm, a full range of rocker profiles with rocker-camber-rocker the most common, and one or two sheets of Titanal at the top end for damping and grip.",
  boots="Flex 110 to 120 for men and 85 to 100 for women, downsized in length and volume with a fitter. Stiffer is not better: a 2,510-skier poll found 39 percent in 130-plus boots and the editors questioned whether most need them.",
  board="Stiffer directional or directional-twin boards; see the snowboard section.",
  mistakes="Chasing the 130 flex. Going wide for one powder day a year.",
  examples="Elan Ripstick 96 Black Edition, Atomic Maverick 96 CTI, Head Kore 94 Ti, V&ouml;lkl M7 Mantra, Nordica Unleashed 98, Rossignol Sender 104 Ti. Boots: Atomic Hawx Ultra 130 S, Salomon S/Pro Alpha 130, Nordica Promachine 3, Tecnica Mach1 130."),
 dict(k="pow", n="Powder, freeride and sidecountry", who="Chases soft snow, glades and off-piste terrain, sometimes with a skin track.",
  skis="For an Eastern skier a 95 to 105 mm daily driver or a 105 to 110 mm powder-day ski; the broad sweet spot for dedicated powder skis is 105 to 120 mm. Tip and tail rocker for float and easy release, a radius over 22 m, and a longer length than the chart to offset the rocker.",
  boots="A touring-capable boot with a walk mode and tech inserts if the skin track is part of the plan; the Atomic Hawx XTD, Salomon Shift Alpha and Nordica Unlimited all keep a 98 to 99 mm downhill fit.",
  board="Stiffer, longer, directional boards with setback stance float best.",
  mistakes="Buying a 112 mm ski as the only ski in New Hampshire.",
  examples="Salomon QST 100 and 106, Atomic Maverick 105 CTI, Atomic Bent 110, Nordica Unleashed 106. Boots: Atomic Hawx Ultra XTD 130 BOA, Salomon Shift Alpha BOA 130, Nordica Unlimited 130 DYN."),
 dict(k="carve", n="Groomer carver", who="Lives on corduroy and hardpack and wants grip, rebound and a race feel.",
  skis="Under 80 to 82 mm, a radius under 16 m, sized shorter than an all-mountain ski, with camber underfoot and metal for edge hold when the groomers refreeze.",
  boots="A performance fit on a narrow or medium last, downsized with the fitter, and a flex at the top of your band.",
  board="Full camber and a stiff boot are what hold an edge on hardpack.",
  mistakes="Buying an all-mountain ski for a skier who never leaves the groomers.",
  examples="Atomic Redster Q9 and Q9.8, Atomic Redster Q5 and Blizzard Thunderbird SP 7.2 for the newer carver, Rossignol Forza, Salomon Stance 80, Atomic X9S Retro Arc 735 RS. Boots: Atomic Redster TX 130, Nordica Promachine 3."),
 dict(k="kids", n="Kids: first lessons", who="From the first magic-carpet day to linking turns.",
  skis="Length between the chest and the nose: chest for beginners, cautious or light kids, nose for confident ones. No more than about 10 cm over the suggested length for growth. If the child is at the top of a binding&rsquo;s DIN range, the binding gets upgraded with the skis.",
  boots="Fit for the current season. Oversized boots bought for growth are the most common reason a child cannot steer.",
  board="A short, soft, forgiving board; the Lincoln counter rents snowboard packages for kids.",
  mistakes="Buying two sizes up. Hand-me-down boots with packed-out liners.",
  examples="Junior rentals at the Lincoln counter from $20 a day; the Junior Seasonal Lease at the Scarborough store ($159 for skis, bindings and boots, ages 2 to 13, up to 130 lb, skis 70 to 150 cm)."),
 dict(k="team", n="Kids on a ski team", who="Junior racers from U8 to U16, and the parents buying for them.",
  skis="Discipline and age class set the ski. Rough lengths: U8 slalom 100 to 120 cm and GS 120 to 130; U10 SL 115 to 130 and GS 125 to 140; U12 SL 130 to 140 and GS 135 to 150; U14 SL 140 to 150 (130 minimum) and GS 150 to 170; U16 SL 150 to 165 and GS 170 to 183. US Ski &amp; Snowboard sets a 130 cm slalom minimum and a 188 cm GS maximum with a 17 m minimum radius for U14 and U16, and a 50 mm stand-height limit. Bindings must match the plate. On used gear, check binding indemnification and boot-sole compatibility, because rule changes retire old equipment.",
  boots="Junior race flex by age: U8 60 to 65, U10 65 to 70, U12 70 to 90, U14 90 to 110, U16 110 to 130, on a race last. Fit for this season, not next.",
  board="",
  mistakes="A full-height GS ski for a U10. A 130 flex boot on a 100 lb U14. Skipping the plate-to-binding check.",
  examples="Van Deer GS-JR Pro, Atomic Redster junior race skis, Rossignol Hero and Head junior race. Boots: Lange RSJ 50 and 60, RS 70 SC, RS 110 SC. Race prep and plate mounting in the Lincoln Boot Lab; a waxed ski with a decent edge is race-ready at the younger ages, and a diamond stone on the side edges every outing or two keeps it that way."),
 dict(k="women", n="Women-specific fit", who="What actually changes in a women&rsquo;s boot and ski, and when unisex is the better buy.",
  skis="Women&rsquo;s skis are usually lighter, softer and shorter, with the mount point a centimeter or so forward; lengths can run 20 cm shorter than a men&rsquo;s chart. A strong female skier can ski a men&rsquo;s ski without penalty.",
  boots="The real differences are a shorter cuff that sits below the widest point of the calf, more cuff flare and a narrower heel pocket. Flex needs track weight and strength more than gender; a women&rsquo;s advanced boot runs about 105 to 115 against a men&rsquo;s 120 to 130. Warmer liners are mostly marketing. Above about a 27.5 Mondo, or for a stiffer flex, a unisex boot is often the better fit.",
  board="",
  mistakes="Assuming a women&rsquo;s boot is just a softer men&rsquo;s boot, or that every woman needs one.",
  examples="Blizzard Black Pearl 88 (Avery&rsquo;s staff pick). Boots: Tecnica Mach1 95 MV W, Nordica Sportmachine 3 95 W BOA for wider feet."),
]

SB_TYPES = [
 dict(n="First-timer", skis="Soft flex (1 to 2 on most brand scales), a rocker, flat or hybrid profile that resists catching an edge, and a true twin so either foot can lead. Size from the weight table, then a few centimeters shorter.",
  boots="Soft boots with a quick-pull or BOA closure; toes gently grazing the toecap, heel locked. Soft bindings to match.",
  examples="Nidecker Play and Merc, Lib Tech Skate Banana. Boots: Salomon Faction BOA, Deeluxe ID."),
 dict(n="Progressing rider", skis="A hybrid camber such as Lib Tech C2 or Never Summer&rsquo;s Rocker Camber that adds edge hold as speed goes up, medium flex, twin or directional twin.",
  boots="Medium flex (3 to 5) boots and bindings that match each other; a soft boot in a stiff binding works against itself.",
  examples="Lib Tech Skate Banana, Nidecker Merc, Never Summer Proto Type 3 for the stronger rider. Boots: Deeluxe ID, ThirtyTwo TM-2. Bindings: Rome Katana, Nidecker Supermatic OG."),
 dict(n="All-mountain and freeride", skis="Stiffer (6 to 10), longer, directional or directional twin, with camber for grip and a setback stance for float.",
  boots="Stiff (6 to 8) to very stiff (9 to 10) boots and responsive bindings.",
  examples="Never Summer Proto Type 3, Nidecker Sensor Pro. Boots: ThirtyTwo TM-2, Deeluxe Deemon Pro. Bindings: Rome Katana, Nidecker Supermatic LT or Carbon."),
 dict(n="Park", skis="Jibbing: short, soft, flat or rocker, soft bindings. Jumps: camber, moderate to stiff, stiffer boots. Freestyle boards run 3 to 5 cm shorter than the all-mountain size.",
  boots="Flex to match the job: soft for rails, stiffer for jumps. Check 2&times;4 and 4&times;4 hole patterns against the binding.",
  examples="Ask the Mothership; the park wall changes every season."),
]

MYTHS = [
 ("Boots first.", "Fit is what gives control; a boot only ever gets looser. Buy boots before skis and get them fitted."),
 ("Do not size up boots.", "Liners pack out within days. A beginner buys at the measured Mondopoint or slightly longer, never roomy."),
 ("Stiffer is not better.", "Bootfitters, brands and the magazines agree: when unsure, flex down."),
 ("Metal is for grip, not weight.", "A sheet of Titanal is about half a millimeter thick. It adds damping and edge hold on ice; a 150 lb intermediate can prefer it."),
 ("Longer is not more stable.", "Stability comes from construction, width and technique. Size from weight, speed and terrain."),
 ("Rocker versus camber for a first snowboard.", "Most guides favor flat or hybrid profiles for beginners; some brands say camber suits every level. Ride what you can control."),
 ("Used race skis for kids are fine, with a check.", "Hand-downs are common on the team; verify binding indemnification and boot-sole compatibility, because rule changes retire old gear."),
 ("A women&rsquo;s boot is not just a softer men&rsquo;s boot.", "Cuff height, flare and heel pocket are real. Warmer liners are marketing."),
]

def _rules():
    out=''
    for h,cols,rows,note in RULES:
        t = pricelist(rows, cols, note).replace('class="pricelist"','class="pricelist rules"',1)
        out += f'<div><div class="kicker">{h}</div>{t}</div>'
    return f'<div class="grid g2" style="gap:28px 40px">{out}</div>'

def _type(t):
    parts = [("Skis", t["skis"]), ("Boots", t["boots"])]
    if t.get("board"): parts.append(("Snowboard", t["board"]))
    parts += [("Common mistakes", t["mistakes"]), ("On our wall", t["examples"])]
    body = ''.join(f'<div class="gk"><div class="kicker">{k}</div><p>{v}</p></div>' for k,v in parts)
    return f'<div class="gtype" id="t-{t["k"]}"><h3>{t["n"]}</h3><p class="who">{t["who"]}</p><div class="gk-grid">{body}</div></div>'

def buyers_guide():
    h = hero("Buyer&rsquo;s guide", "How to choose skis, boots and snowboards for the way you actually ski or ride: the rules of thumb, what to look for at each stage, and where the wall in Lincoln and Scarborough fits in. Boots come first at every level.",
             "skier-carving-red-jacket", kicker="Skis &middot; Boots &middot; Snowboards", short=True, pos="center 40%",
             ctas='<a class="btn accent" href="#rules">Rules of thumb</a><a class="btn ghost-d" href="#types">Find your type</a><a class="btn ghost-d" href="#snowboards">Snowboards</a>')
    h += crumbs(("Guides","buyers-guide.html"), ("Buyer&rsquo;s Guide",""))
    chips = '<div class="chips" style="margin-top:18px">' + ''.join(f'<a href="#t-{t["k"]}">{t["n"]}</a>' for t in SKIER_TYPES) + '</div>'
    h += (f'<section><div class="wrap"><p style="max-width:760px">Start with the rules of thumb, then find the description that sounds like you. Each one says what to look for in a ski, a boot and, where it applies, a snowboard, the mistakes we see most, and the products on our wall that fit. Sizes, this season&rsquo;s stock and the final call happen in the store with a fitter.</p>{chips}</div></section>')
    h += (f'<section class="ice" id="rules"><div class="wrap">{sechead("Rules of thumb", "The charts every fitter starts from. They narrow the field; the bench decides.")}{_rules()}</div></section>')
    h += (f'<section id="types"><div class="wrap">{sechead("Find your type", "Eleven kinds of skier we fit every week.")}<div class="gtypes">{"".join(_type(t) for t in SKIER_TYPES)}</div></div></section>')
    sb = ''.join(f'<div class="gtype"><h3>{t["n"]}</h3><div class="gk-grid"><div class="gk"><div class="kicker">Board</div><p>{t["skis"]}</p></div><div class="gk"><div class="kicker">Boots and bindings</div><p>{t["boots"]}</p></div><div class="gk"><div class="kicker">On our wall</div><p>{t["examples"]}</p></div></div></div>' for t in SB_TYPES)
    h += (f'<section class="ice" id="snowboards"><div class="wrap">{sechead("Snowboards", "The Mothership, inside the Lincoln store. Scarborough sells skis only.")}{brands(SNOWBOARD_BRANDS)}<div class="gtypes" style="margin-top:22px">{sb}</div></div></section>')
    myths = ''.join(f'<div class="card"><h3 style="font-size:17px">{a}</h3><p>{b}</p></div>' for a,b in MYTHS)
    h += (f'<section><div class="wrap">{sechead("Eight things worth knowing", "The questions that come up on every forum and at every counter.")}<div class="grid g4">{myths}</div>'
          f'<div style="margin-top:32px"><a class="btn" href="boot-lab.html#book">Book a boot fitting</a> <a class="btn ghost" href="reserve-rental.html">Reserve a rental</a> <a class="btn ghost" href="lease.html">Junior lease in Scarborough</a></div></div></section>')
    h += (f'<section class="ice"><div class="wrap">{sechead("The brands", "Skis, boots and snowboards on the walls in Lincoln and Scarborough.")}<div class="kicker">Skis</div>{brands(SKI_BRANDS)}<div class="kicker" style="margin-top:22px">Ski boots</div>{brands(BOOT_BRANDS)}</div></section>')
    h += (f'<section><div class="wrap"><p class="note">Guidance paraphrased from evo, REI, Powder7, Switchback Travel, Tactics and The Ski Monster buying guides, brand fit pages, Bootfitters.com, Wayfinder, SkiTalk, US Ski &amp; Snowboard equipment rules and The Pro Ski &amp; Ride junior racing guide, as of September 2026.</p></div></section>')
    return page("guides", "Buyer&rsquo;s Guide | Rodgers Ski &amp; Sport", "How to choose skis, ski boots and snowboards by ability, style and skier type, from first-timers and leisurely skiers to junior racers and freeriders, with the rules of thumb fitters use.", h, "buyers-guide.html")

# ---------------------------------------------------------------- Outdoor Guide
# level: easy / moderate / difficult / expert / mixed (ski areas whose trail mix is not published)
LIN = dict(lat=44.0468, lon=-71.6740, mi=50, name="Lincoln, NH")
SCA = dict(lat=43.5860, lon=-70.3335, mi=15, name="Scarborough, ME")

POINTS_LIN = [
 # alpine
 dict(n="Loon Mountain Resort", t="alpine", lv="moderate", lat=44.0361, lon=-71.6217, town="Lincoln, NH", s="19% beginner / 53% intermediate / 28% advanced &middot; 2,190 ft vertical &middot; 73 trails", d="Lincoln&rsquo;s home mountain: three peaks, the Kancamagus 8 and the largest snowmaking system in New Hampshire.", u="https://www.loonmtn.com"),
 dict(n="Cannon Mountain", t="alpine", lv="difficult", lat=44.1578, lon=-71.6989, town="Franconia, NH", s="21% / 47% / 32% &middot; 2,230 ft vertical &middot; 73 trails", d="State-owned Franconia Notch classic with an aerial tramway and steep New England terrain.", u="https://www.cannonmt.com"),
 dict(n="Waterville Valley Resort", t="alpine", lv="moderate", lat=43.9653, lon=-71.5278, town="Waterville Valley, NH", s="15% / 59% / 26% &middot; 2,020 ft vertical &middot; 62 trails", d="Intermediate-friendly resort village at the end of Route 49 with a strong terrain-park heritage.", u="https://www.waterville.com"),
 dict(n="Bretton Woods", t="alpine", lv="difficult", lat=44.2597, lon=-71.4622, town="Carroll, NH", s="25% / 29% / 46% &middot; 1,500 ft vertical &middot; 102 trails", d="New Hampshire&rsquo;s largest ski area by acreage, glade-heavy, facing Mount Washington.", u="https://www.brettonwoods.com"),
 dict(n="Attitash Mountain Resort", t="alpine", lv="moderate", lat=44.0822, lon=-71.2297, town="Bartlett, NH", s="29% / 44% / 27% &middot; 1,750 ft vertical &middot; 68 trails", d="Two peaks, Attitash and Bear Peak, on Route 302 in Bartlett.", u="https://www.attitash.com"),
 dict(n="Wildcat Mountain", t="alpine", lv="difficult", lat=44.2631, lon=-71.2383, town="Pinkham Notch, NH", s="25% / 45% / 30% &middot; 2,112 ft vertical &middot; 49 trails", d="Long, north-facing runs directly across from Tuckerman Ravine.", u="https://www.skiwildcat.com"),
 dict(n="Black Mountain", t="alpine", lv="mixed", lat=44.1683, lon=-71.1644, town="Jackson, NH", s="1,100 ft vertical &middot; 45 trails &middot; trail mix not published", d="Ninety-year-old, sunny, wind-sheltered Jackson ski hill, now run by Indy Pass.", u="https://www.blackmt.com"),
 dict(n="Cranmore Mountain Resort", t="alpine", lv="moderate", lat=44.0538, lon=-71.1060, town="North Conway, NH", s="28% / 45% / 27% &middot; 1,200 ft vertical &middot; 56 trails", d="In-town North Conway resort with a mountain coaster and a learn-to-ski focus.", u="https://www.cranmore.com"),
 dict(n="King Pine Ski Area", t="alpine", lv="easy", lat=43.8714, lon=-71.0894, town="East Madison, NH", s="350 ft vertical &middot; 17 trails &middot; 100% snowmaking", d="Small family hill at Purity Spring Resort with tubing and a 20 km cross-country network.", u="https://www.kingpine.com"),
 dict(n="Tenney Mountain", t="alpine", lv="mixed", lat=43.7378, lon=-71.7836, town="Plymouth, NH", s="1,500 ft vertical &middot; 53 trails &middot; 2026&ndash;27 passes on sale", d="Independently owned mountain outside Plymouth; confirm operating dates each season.", u="https://www.skitenney.com"),
 dict(n="Gunstock Mountain Resort", t="alpine", lv="mixed", lat=43.5414, lon=-71.3675, town="Gilford, NH", s="1,340 ft vertical &middot; 44 trails and 5 glades", d="County-owned Lakes Region resort above Lake Winnipesaukee.", u="https://www.gunstock.com"),
 dict(n="Ragged Mountain Resort", t="alpine", lv="mixed", lat=43.4844, lon=-71.8422, town="Danbury, NH", s="1,250 ft vertical &middot; 57 trails, 17 glades", d="Two-peak resort with New Hampshire&rsquo;s only six-person high-speed lift.", u="https://www.raggedmountainresort.com"),
 dict(n="Pleasant Mountain", t="alpine", lv="mixed", lat=44.0583, lon=-70.8153, town="Bridgton, ME", s="1,300 ft vertical &middot; 44 trails &middot; night skiing", d="Boyne-owned Maine mountain, renamed from Shawnee Peak in 2022.", u="https://www.pleasantmountain.com"),
 # nordic
 dict(n="Bretton Woods Nordic Center", t="nordic", lv="moderate", lat=44.2648, lon=-71.4408, town="Bretton Woods, NH", s="About 100 km of trails with warming cabins", d="One of the largest groomed cross-country networks in the East.", u="https://www.brettonwoods.com/nordic"),
 dict(n="Waterville Valley Nordic Center", t="nordic", lv="moderate", lat=43.9505, lon=-71.5075, town="Waterville Valley, NH", s="70+ km groomed classic and skate", d="Town Square center whose trails run into the national forest.", u="https://www.waterville.com/nordic-center"),
 dict(n="Franconia Village Cross-Country", t="nordic", lv="easy", lat=44.1962, lon=-71.7529, town="Franconia, NH", s="30 km, 25 km groomed", d="Franconia Inn touring center under the Kinsman Range.", u="https://www.franconiainn.com/xc-ski"),
 dict(n="Bear Notch Ski Touring", t="nordic", lv="moderate", lat=44.0730, lon=-71.3028, town="Bartlett, NH", s="70 km total, 60 km groomed", d="Family-run touring center along the Saco River on Route 302.", u="https://www.bearnotchskitouring.com"),
 dict(n="Jackson Ski Touring Foundation", t="nordic", lv="moderate", lat=44.1466, lon=-71.1867, town="Jackson, NH", s="100 km total, 85 km groomed, 40 km snowshoe", d="Nonprofit village-wide network and one of the best-known Nordic destinations in the East.", u="https://www.jacksonxc.org"),
 dict(n="Great Glen Trails", t="nordic", lv="moderate", lat=44.2885, lon=-71.2258, town="Gorham, NH", s="20+ km groomed, 25 km ungroomed", d="At the base of the Mount Washington Auto Road; fat bikes and snowcoach too.", u="https://greatglentrails.com"),
 # hiking
 dict(n="Franconia Ridge Loop", a="https://www.alltrails.com/trail/us/new-hampshire/mount-lafayette-and-franconia-ridge-trail-loop", t="hike", lv="expert", lat=44.1420, lon=-71.6811, town="Franconia Notch, NH", s="8.3&ndash;8.5 mi loop &middot; about 3,600&ndash;3,800 ft gain", d="Falling Waters up, Old Bridle Path down: the signature above-treeline traverse over Little Haystack, Lincoln and Lafayette.", u="https://www.nhstateparks.org/find-parks-trails/franconia-notch-state-park"),
 dict(n="Mount Lafayette via Old Bridle Path", a="https://www.alltrails.com/trail/us/new-hampshire/mount-lafayette-via-old-bridle-path--2", t="hike", lv="difficult", lat=44.1420, lon=-71.6812, town="Franconia Notch, NH", s="About 8 mi round trip &middot; about 3,500 ft gain", d="Past AMC Greenleaf Hut to the 5,249 ft summit.", u="https://www.outdoors.org/destinations/new-hampshire/greenleaf-hut/"),
 dict(n="Flume Gorge", a="https://www.alltrails.com/trail/us/new-hampshire/the-flume-gorge-trail", t="hike", lv="easy", lat=44.1020, lon=-71.6775, town="Lincoln, NH", s="2.0 mi loop &middot; timed tickets, seasonal", d="Boardwalk through an 800 ft granite chasm; the full loop is required.", u="https://www.nhstateparks.org/find-parks-trails/flume-gorge"),
 dict(n="Mount Pemigewasset (Indian Head)", a="https://www.alltrails.com/trail/us/new-hampshire/mount-pemigewasset-trail-indian-head", t="hike", lv="moderate", lat=44.1020, lon=-71.6775, town="Lincoln, NH", s="3.4 mi round trip &middot; about 1,250 ft gain", d="Short climb from the Flume lot to a cliff-top view over the notch.", u="https://www.cannonmt.com/attractions/hiking-hiker-parking"),
 dict(n="Lonesome Lake", a="https://www.alltrails.com/trail/us/new-hampshire/lonesome-lake-trail", t="hike", lv="moderate", lat=44.1419, lon=-71.6840, town="Franconia Notch, NH", s="3.1 mi loop &middot; about 1,000 ft gain", d="Family favorite from Lafayette Place to AMC Lonesome Lake Hut.", u="https://www.cannonmt.com/attractions/hiking-hiker-parking"),
 dict(n="North and South Kinsman", a="https://www.alltrails.com/trail/us/new-hampshire/north-kinsman-and-south-kinsman-trail-via-lonesome-lake-and-appalachian-trail", t="hike", lv="difficult", lat=44.1419, lon=-71.6840, town="Franconia Notch, NH", s="10 mi round trip &middot; about 3,150 ft gain", d="Two 4,000-footers via Lonesome Lake and the Fishin&rsquo; Jimmy Trail.", u="https://www.outdoors.org"),
 dict(n="Welch&ndash;Dickey Loop", a="https://www.alltrails.com/trail/us/new-hampshire/welch-and-dickey-loop-trail--4", t="hike", lv="moderate", lat=43.9046, lon=-71.5890, town="Thornton, NH", s="4.4 mi loop", d="Open granite ledges with big views for modest effort.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/welch-dickey-trailhead"),
 dict(n="Mount Moosilauke, Gorge Brook Trail", a="https://www.alltrails.com/trail/us/new-hampshire/mount-moosilauke-via-gorge-brook-trail", t="hike", lv="difficult", lat=43.9772, lon=-71.8172, town="Benton, NH", s="7.2 mi round trip &middot; about 2,350 ft gain", d="Bald 4,802 ft summit from Dartmouth&rsquo;s Ravine Lodge.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/ravine-lodge-trailhead"),
 dict(n="Lincoln Woods Trail", a="https://www.alltrails.com/trail/us/new-hampshire/lincoln-woods-trail", t="hike", lv="easy", lat=44.0639, lon=-71.5883, town="Lincoln, NH", s="Flat railroad grade, 3 mi each way &middot; closed for restoration June 15 to November 2026", d="Old logging railroad along the East Branch into the Pemigewasset Wilderness; Franconia Falls spur.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/lincoln-woods-trailhead"),
 dict(n="Arethusa Falls", a="https://www.alltrails.com/trail/us/new-hampshire/arethusa-falls-via-bemis-brook-and-arethusa-falls-trails", t="hike", lv="moderate", lat=44.1477, lon=-71.3696, town="Hart&rsquo;s Location, NH", s="About 3 mi round trip &middot; about 900 ft gain", d="New Hampshire&rsquo;s tallest single-drop waterfall in Crawford Notch State Park.", u="https://www.nhstateparks.org/find-parks-trails/crawford-notch-state-park"),
 dict(n="Mount Washington via Tuckerman Ravine", a="https://www.alltrails.com/trail/us/new-hampshire/tuckerman-ravine-trail-to-mount-washington", t="hike", lv="expert", lat=44.2575, lon=-71.2531, town="Pinkham Notch, NH", s="8.4 mi round trip &middot; 4,250 ft gain", d="The classic route up the Northeast&rsquo;s highest peak from AMC Pinkham Notch.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/pinkham-notch-trailhead"),
 dict(n="Artist&rsquo;s Bluff and Bald Mountain", a="https://www.alltrails.com/trail/us/new-hampshire/artist-bluff-trail", t="hike", lv="easy", lat=44.1798, lon=-71.7020, town="Franconia, NH", s="1.5 mi loop &middot; about 535 ft gain", d="Short scramble to the postcard view of Echo Lake and Cannon.", u="https://www.cannonmt.com/attractions/hiking-hiker-parking"),
 dict(n="Mount Willard", a="https://www.alltrails.com/trail/us/new-hampshire/mount-willard", t="hike", lv="moderate", lat=44.2173, lon=-71.4127, town="Crawford Notch, NH", s="About 3 mi round trip &middot; about 880 ft gain", d="Easy grade from Crawford Depot to a cliff view straight down the notch.", u="https://www.nhstateparks.org/find-parks-trails/crawford-notch-state-park"),
 dict(n="Champney Falls and Mount Chocorua", a="https://www.alltrails.com/trail/us/new-hampshire/champney-brook-trail-to-mount-chocorua", t="hike", lv="difficult", lat=43.9899, lon=-71.2991, town="Albany, NH", s="Falls about 3 mi, 500 ft &middot; summit 7.6 mi, 2,250 ft", d="Kancamagus trailhead to a waterfall and the rocky Chocorua summit.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/champney-falls-trailhead"),
 dict(n="Mount Osceola", a="https://www.alltrails.com/trail/us/new-hampshire/mount-osceola-summit", t="hike", lv="difficult", lat=43.9835, lon=-71.5592, town="Livermore, NH", s="6.4 mi round trip &middot; Tripoli Road closed November to late May", d="Ledge summit above Waterville Valley.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/osceola-trailhead"),
 dict(n="Zealand Falls", a="https://www.alltrails.com/trail/us/new-hampshire/zealand-hut-trail", t="hike", lv="easy", lat=44.2247, lon=-71.4791, town="Bethlehem, NH", s="4.6&ndash;5 mi round trip &middot; about 450 ft gain", d="Gentle walk past beaver ponds to AMC Zealand Falls Hut.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/zealand-trailhead-forest-rd-16"),
 dict(n="Sabbaday Falls", a="https://www.alltrails.com/trail/us/new-hampshire/sabbaday-falls", t="hike", lv="easy", lat=43.9972, lon=-71.3929, town="Waterville Valley, NH", s="15-minute walk from the Kancamagus", d="Flume-and-pool waterfall walk.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/sabbaday-falls-observation-site"),
 dict(n="Diana&rsquo;s Baths", a="https://www.alltrails.com/trail/us/new-hampshire/dianas-baths", t="hike", lv="easy", lat=44.0747, lon=-71.1630, town="Bartlett, NH", s="1.5 mi round trip &middot; fee lot", d="Cascades and pools near North Conway.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/dianas-baths"),
 dict(n="Georgiana Falls", a="https://www.alltrails.com/trail/us/new-hampshire/georgiana-and-harvard-falls-trail", t="hike", lv="moderate", lat=44.0671, lon=-71.6888, town="Lincoln, NH", s="2.2&ndash;2.6 mi round trip &middot; about 730 ft gain", d="The closest waterfall hike to the Lincoln store, off Hanson Farm Road.", u="https://www.fs.usda.gov/r09/whitemountain"),
 dict(n="Mount Tecumseh", t="hike", lv="difficult", lat=43.9661, lon=-71.5271, town="Waterville Valley, NH", s="About 5 mi round trip from the ski-area lot", d="The lowest of the 4,000-footers, straight up from the Waterville Valley parking lot.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/mt-tecumseh-trailhead", a="https://www.alltrails.com/trail/us/new-hampshire/mount-tecumseh-trail"),
 dict(n="Mount Pierce via Crawford Path", t="hike", lv="difficult", lat=44.2238, lon=-71.4118, town="Crawford Notch, NH", s="About 6.2 mi round trip &middot; about 2,450 ft gain &middot; $5 day fee", d="The oldest continuously maintained hiking trail in America, past AMC Mizpah Spring Hut.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/crawford-connector-trailhead", a="https://www.alltrails.com/trail/us/new-hampshire/mount-pierce-via-crawford-path"),
 dict(n="Mount Cardigan, West Ridge Trail", t="hike", lv="moderate", lat=43.6442, lon=-71.9349, town="Orange, NH", s="3 mi round trip &middot; about 1,200 ft gain", d="Bald granite summit with a fire tower and views in every direction; lot road closed in winter.", u="https://www.nhstateparks.org/find-parks-trails/cardigan-mountain-state-park", a="https://www.alltrails.com/trail/us/new-hampshire/mount-cardigan-trail"),
 dict(n="Boulder Loop Trail", t="hike", lv="moderate", lat=44.0050, lon=-71.2391, town="Albany, NH", s="About 2.7 mi loop &middot; day-use fee &middot; open mid-May to mid-October", d="Ledges above the Kancamagus with views of Mount Chocorua.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/boulder-loop-trailhead", a="https://www.alltrails.com/trail/us/new-hampshire/boulder-loop-trail"),
 dict(n="North and Middle Sugarloaf", t="hike", lv="moderate", lat=44.2542, lon=-71.5047, town="Bethlehem, NH", s="About 3.6 mi round trip for both summits", d="Two open ledge summits off Zealand Road with big views for a short climb.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/sugarloaf-trailhead", a="https://www.alltrails.com/trail/us/new-hampshire/north-and-middle-sugarloaf-via-sugarloaf-trail"),
 dict(n="Mount Liberty via Liberty Spring Trail", t="hike", lv="difficult", lat=44.1005, lon=-71.6814, town="Franconia Notch, NH", s="About 8 mi round trip", d="A 4,000-footer with a rocky summit at the south end of Franconia Ridge, from the Whitehouse hiker lot.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/liberty-springs-tentsite", a="https://www.alltrails.com/trail/us/new-hampshire/mount-liberty-via-liberty-spring-trail"),
 # mtb
 dict(n="Loon Bike Park", t="mtb", lv="moderate", lat=44.0361, lon=-71.6217, town="Lincoln, NH", s="15+ mi, 1,000 ft vertical, lift-served &middot; skills zone to jump and tech lines", d="Lift-accessed downhill park plus the 3 mi Mainline flow trail.", u="https://www.loonmtn.com/summer-activities/biking/bike-park"),
 dict(n="Franconia Area NEMBA trails", t="mtb", lv="moderate", lat=44.2071, lon=-71.7374, town="Franconia, NH", s="40+ mi &middot; mostly blue with black options", d="Volunteer-built singletrack at Fox Hill, Profile and Cooley-Jericho, north of the notch.", u="https://www.nemba.org/chapters/franconia-nemba"),
 dict(n="Bethlehem Trails Association", t="mtb", lv="moderate", lat=44.2826, lon=-71.6823, town="Bethlehem, NH", s="25+ mi, 1,200 ft &middot; blue to black, family loops", d="Connected network with true descending lines and beginner loops.", u="https://www.bethlehemtrails.org"),
 dict(n="PRKR MTN Trails", t="mtb", lv="difficult", lat=44.3164, lon=-71.7593, town="Littleton, NH", s="59 trails: 2 green / 17 blue / 22 black / 17 double black", d="Free, community-built network on Parker Mountain with downhill-only flow trails.", u="https://www.prkrmtn.org"),
 dict(n="Fox Park Trails", t="mtb", lv="difficult", lat=43.7514, lon=-71.6973, town="Plymouth, NH", s="About 3 mi, 16 trails, mostly technical", d="Pemi Valley NEMBA&rsquo;s hand-built switchbacks and skills area.", u="https://www.nemba.org/chapters/pemi-valley-nemba"),
 dict(n="Marshall Conservation Area", t="mtb", lv="easy", lat=44.0091, lon=-71.1486, town="North Conway, NH", s="12 mi, 28 trails &middot; green and blue flow, limited black", d="Machine-built flow trails on Town of Conway land.", u="https://ridenoco.org"),
 dict(n="Waterville Valley mountain biking", t="mtb", lv="mixed", lat=43.9653, lon=-71.5278, town="Waterville Valley, NH", s="Lift-served on Snow&rsquo;s Mountain plus forest cross-country loops", d="Fire roads to technical singletrack; mileage not published.", u="https://www.visitwatervillevalley.com/biking"),
 dict(n="Highland Mountain Bike Park", t="mtb", lv="expert", lat=43.4015, lon=-71.5512, town="Northfield, NH", s="44 trails: 2 green / 10 blue / 10 black / 8 double black &middot; lift only", d="Bike-dedicated gravity park with an indoor training facility, 45 miles south.", u="https://highlandmountain.com"),
 # path
 dict(n="Franconia Notch Recreation Path", a="https://www.alltrails.com/trail/us/new-hampshire/franconia-notch-path", t="path", lv="easy", lat=44.1300, lon=-71.6900, town="Lincoln to Franconia, NH", s="8.8 mi paved, Flume to Skookumchuck &middot; about 800 ft south to north", d="State-park bike path through the notch past the Basin, Profile Lake and Echo Lake.", u="https://www.cannonmt.com/attractions/franconia-notch-recreation-path"),
]

POINTS_SCA = [
 dict(n="Eastern Trail, Scarborough Marsh", a="https://www.alltrails.com/trail/us/maine/eastern-trail-scarborough-to-saco", t="path", lv="easy", lat=43.5700, lon=-70.3500, town="Scarborough, ME", s="8.4 mi off-road Saco to Scarborough &middot; crushed stone, accessible", d="Flat rail trail across Maine&rsquo;s largest salt marsh; gravel bikes welcome.", u="https://www.easterntrail.org"),
 dict(n="Pleasant Hill Preserve", a="https://www.alltrails.com/trail/us/maine/pleasant-hill-preserve", t="hike", lv="easy", lat=43.5960, lon=-70.3080, town="Scarborough, ME", s="2.4 mi of trails, 244 acres &middot; no bikes", d="Scarborough Land Trust preserve a mile from the store.", u="https://scarboroughlandtrust.org/slt-trails/pleasant-hill-preserve/"),
 dict(n="Libby River Farm Preserve", a="https://www.alltrails.com/trail/us/maine/camp-ketcha-and-libby-river-loop", t="hike", lv="easy", lat=43.566, lon=-70.301, town="Scarborough, ME", s="1.3 mi, 153 acres &middot; no bikes", d="Fields and river frontage on the Libby River.", u="https://scarboroughlandtrust.org"),
 dict(n="Scarborough Marsh Audubon Center", t="hike", lv="easy", lat=43.5643, lon=-70.3732, town="Scarborough, ME", s="0.3 mi nature trail &middot; canoe rentals", d="Maine Audubon&rsquo;s marsh center on Pine Point Road.", u="https://maineaudubon.org/visit/scarborough-marsh/"),
 dict(n="Fuller Farm Preserve", a="https://www.alltrails.com/trail/us/maine/fuller-farm-trails--2", t="hike", lv="easy", lat=43.5880, lon=-70.4130, town="Scarborough, ME", s="4 mi of loops, 224 acres &middot; cross-country ski and snowshoe", d="Fields, woods and the Nonesuch River.", u="https://scarboroughlandtrust.org/slt-trails/fuller-farm-preserve/"),
 dict(n="Crescent Beach and Kettle Cove", a="https://www.alltrails.com/trail/us/maine/kettle-cove-to-crescent-beach-state-park-loop", t="hike", lv="easy", lat=43.5648, lon=-70.2227, town="Cape Elizabeth, ME", s="2.2 mi combined trail network", d="State park beach and shore loops.", u="https://www.maine.gov/dacf/parks"),
 dict(n="Two Lights State Park", a="https://www.alltrails.com/trail/us/maine/two-lights-state-park-loop", t="hike", lv="easy", lat=43.5602, lon=-70.2049, town="Cape Elizabeth, ME", s="1.9 mi, 41 acres of headlands", d="Rocky headlands and two lighthouses.", u="https://www.maine.gov/dacf/parks"),
 dict(n="Fort Williams Park", a="https://www.alltrails.com/trail/us/maine/fort-williams-park-loop", t="hike", lv="easy", lat=43.6235, lon=-70.2102, town="Cape Elizabeth, ME", s="0.4 mi Cliff Walk plus park paths", d="Portland Head Light and the shore.", u="https://www.fortwilliams.org"),
 dict(n="Fore River Sanctuary", a="https://www.alltrails.com/trail/us/maine/fore-river-sanctuary-white-trail", t="hike", lv="easy", lat=43.6672, lon=-70.3177, town="Portland, ME", s="About 2 mi of trails &middot; Jewell Falls", d="Portland Trails&rsquo; 85-acre sanctuary with the city&rsquo;s only waterfall.", u="https://trails.org"),
 dict(n="Baxter Woods", a="https://www.alltrails.com/trail/us/maine/baxter-woods-park-loop", t="hike", lv="easy", lat=43.6767, lon=-70.2895, town="Portland, ME", s="1.5 mi network", d="City woodland off Forest Avenue.", u="https://www.mainetrailfinder.com/trails/trail/baxter-woods"),
 dict(n="Saco Heath Preserve", a="https://www.alltrails.com/trail/us/maine/saco-heath-preserve-trail", t="hike", lv="easy", lat=43.5462, lon=-70.4711, town="Saco, ME", s="2.1 mi round trip boardwalk, 1,223 acres", d="Nature Conservancy boardwalk across a raised peat bog.", u="https://www.nature.org/en-us/get-involved/how-to-help/places-we-protect/saco-heath-preserve/"),
 dict(n="Ferry Beach State Park", a="https://www.alltrails.com/trail/us/maine/ferry-beach-state-park-loop", t="hike", lv="easy", lat=43.4782, lon=-70.3875, town="Saco, ME", s="1.7 mi trail network plus beach", d="Woods, tupelo swamp and sand.", u="https://www.maine.gov/dacf/parks"),
 dict(n="Presumpscot River Preserve", a="https://www.alltrails.com/trail/us/maine/presumpscot-river-preserve-trail", t="hike", lv="moderate", lat=43.7220, lon=-70.2818, town="Portland, ME", s="3.5 mi network with Oat Nuts Park", d="River gorge trails on the Portland and Falmouth line.", u="https://www.mainetrailfinder.com/trails/trail/presumpscot-river-preserve-and-oat-nuts-park"),
 dict(n="Mackworth Island", a="https://www.alltrails.com/trail/us/maine/mackworth-island-hiking-trail", t="hike", lv="easy", lat=43.6893, lon=-70.2305, town="Falmouth, ME", s="1.5 mi shore loop", d="Causeway island in Casco Bay.", u="https://www.maine.gov/dacf/parks"),
 dict(n="Back Cove Trail", t="path", lv="easy", lat=43.6714, lon=-70.2650, town="Portland, ME", s="3.6 mi loop, mostly flat", d="Portland Trails&rsquo; loop around Back Cove; walking, running and bikes.", u="https://trails.org/our-trails/back-cove-trail/", a="https://www.alltrails.com/trail/us/maine/back-cove-trail"),
 dict(n="Cascade Falls", t="hike", lv="easy", lat=43.5430, lon=-70.4068, town="Saco, ME", s="Short network under half a mile", d="Saco Bay Trails&rsquo; waterfall walk off Route 1.", u="https://www.sacobaytrails.org/trails/cascadefalls", a="https://www.alltrails.com/trail/us/maine/cascade-falls-trail"),
 dict(n="Blackstrap Hill Community Forest", a="https://www.alltrails.com/trail/us/maine/blackstrap-hill-preserve", t="mtb", lv="difficult", lat=43.7775, lon=-70.3234, town="Falmouth, ME", s="24 mi, 38 trails: 7 green / 5 blue / 24 black / 2 double black &middot; grades over 20%", d="Greater Portland&rsquo;s main technical mountain-bike destination; Flow Creek from Hurricane Road.", u="https://falmouthlandtrust.org/properties/blackstrap-hill-preserve"),
 dict(n="Harris Farm Cross-Country", t="nordic", lv="easy", lat=43.548, lon=-70.570, town="Dayton, ME", s="40 km, 30 km skate-groomed, 35 km track-set", d="Working dairy farm with groomed trails, 12 miles west.", u="https://www.harrisfarm.com/x-c-skiing.html"),
]

NEAREST_ALPINE_SCA = [
 ("Lost Valley", "Auburn, ME", "38 mi", "240 ft vertical, 31 trails", "https://www.lostvalleyski.com"),
 ("Pleasant Mountain", "Bridgton, ME", "41 mi", "1,300 ft vertical, 44 trails, night skiing", "https://www.pleasantmountain.com"),
 ("Mt. Abram", "Greenwood, ME", "58 mi", "Independent, two-base mountain", "https://www.mtabram.com"),
 ("Sunday River", "Newry, ME", "67 mi", "Eight peaks", "https://www.sundayriver.com"),
]

LEVELS = [("easy","Easy","#2E8B57"),("moderate","Moderate","#1E63B8"),("difficult","Difficult","#111111"),("expert","Expert","#C62828"),("mixed","All levels / see resort","#7A8797")]
TYPES = [("alpine","Alpine ski area"),("nordic","Nordic center"),("hike","Hiking trail"),("mtb","Mountain biking"),("path","Multi-use path")]

MAP_CSS = r"""
.omap{height:560px;border:1px solid var(--line);background:var(--ice)}
.legend{display:flex;flex-wrap:wrap;gap:14px 22px;margin-top:14px;font-size:12.5px;color:var(--ink)}
.legend i{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:7px;vertical-align:-1px}
.legend .t{letter-spacing:1.5px;text-transform:uppercase;font-size:11px;color:var(--steel);margin-right:4px}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 12px}
.filters button{border:2px solid var(--navy);background:#fff;color:var(--navy);padding:8px 14px;font-size:11px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;cursor:pointer;min-height:36px}
.filters button.on{background:var(--navy);color:#fff}
.plist{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:24px}
.plist .card{padding:18px 20px}
.plist .card b.n{font-size:16px;display:block;color:var(--ink)}
.plist .card .lv{display:inline-block;font-size:10.5px;letter-spacing:1.5px;text-transform:uppercase;color:#fff;padding:3px 8px;margin:8px 0 6px}
.plist .card p{font-size:14px;margin-top:6px}
.plist .card small{display:block;color:var(--steel);font-size:12.5px;margin-top:6px}
.leaflet-popup-content{font-family:"Source Serif 4",Georgia,serif;font-size:14px;line-height:1.45}
.leaflet-popup-content b{display:block;font-size:15px;color:#012D5D}
.gm-style .gm-style-iw-d{font-family:"Source Serif 4",Georgia,serif}
@media (max-width:900px){.plist{grid-template-columns:1fr 1fr}.omap{height:440px}}
@media (max-width:640px){.plist{grid-template-columns:1fr}.omap{height:380px}}
"""

MAP_JS = r"""
(function(){
  var DATA=%s, LEVELS=%s, KEY=%s;
  var COLOR={}; LEVELS.forEach(function(l){COLOR[l[0]]=l[2];});
  var NAME={}; LEVELS.forEach(function(l){NAME[l[0]]=l[1];});
  var TYPE={alpine:'Alpine ski area',nordic:'Nordic center',hike:'Hiking',mtb:'Mountain biking',path:'Multi-use path'};
  function popup(p){return '<b>'+p.n+'</b>'+TYPE[p.t]+' &middot; '+p.town+'<br><span style="color:'+COLOR[p.lv]+';font-weight:700">'+NAME[p.lv]+'</span> &middot; '+p.s+'<br>'+p.d+'<br><a href="'+p.u+'" target="_blank" rel="noopener">Website</a>'+(p.a?' &middot; <a href="'+p.a+'" target="_blank" rel="noopener">AllTrails</a>':'');}
  var maps={};
  function build(id, cfg, pts){
    var el=document.getElementById(id); if(!el)return;
    var state={type:'all'};
    var api;
    if(KEY && window.google && google.maps){
      var m=new google.maps.Map(el,{center:{lat:cfg.lat,lng:cfg.lon},zoom:cfg.mi>20?9:11,mapTypeControl:false,streetViewControl:false,styles:[{featureType:'poi',stylers:[{visibility:'off'}]}]});
      new google.maps.Circle({map:m,center:{lat:cfg.lat,lng:cfg.lon},radius:cfg.mi*1609.34,strokeColor:'#012D5D',strokeOpacity:.6,strokeWeight:1.5,fillColor:'#012D5D',fillOpacity:.04});
      new google.maps.Marker({map:m,position:{lat:cfg.lat,lng:cfg.lon},title:'Rodgers Ski & Sport, '+cfg.name,icon:{path:google.maps.SymbolPath.CIRCLE,scale:7,fillColor:'#E8722A',fillOpacity:1,strokeColor:'#fff',strokeWeight:2}});
      var iw=new google.maps.InfoWindow();
      var marks=pts.map(function(p){var mk=new google.maps.Marker({map:m,position:{lat:p.lat,lng:p.lon},title:p.n,icon:{path:google.maps.SymbolPath.CIRCLE,scale:6.5,fillColor:COLOR[p.lv],fillOpacity:1,strokeColor:'#fff',strokeWeight:1.5}});mk.addListener('click',function(){iw.setContent(popup(p));iw.open(m,mk);});return mk;});
      api={show:function(t){marks.forEach(function(mk,i){mk.setMap(t==='all'||pts[i].t===t?m:null);});}};
    } else {
      var m=L.map(el,{scrollWheelZoom:false}).setView([cfg.lat,cfg.lon],cfg.mi>20?9:11);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,attribution:'&copy; OpenStreetMap contributors'}).addTo(m);
      L.circle([cfg.lat,cfg.lon],{radius:cfg.mi*1609.34,color:'#012D5D',weight:1.5,opacity:.6,fillColor:'#012D5D',fillOpacity:.04}).addTo(m);
      L.circleMarker([cfg.lat,cfg.lon],{radius:8,color:'#fff',weight:2,fillColor:'#E8722A',fillOpacity:1}).addTo(m).bindPopup('<b>Rodgers Ski &amp; Sport</b>'+cfg.name);
      var marks=pts.map(function(p){return L.circleMarker([p.lat,p.lon],{radius:7,color:'#fff',weight:1.5,fillColor:COLOR[p.lv],fillOpacity:1}).addTo(m).bindPopup(popup(p));});
      api={show:function(t){marks.forEach(function(mk,i){if(t==='all'||pts[i].t===t){mk.addTo(m);}else{m.removeLayer(mk);}});}};
    }
    document.querySelectorAll('[data-map="'+id+'"] .filters button').forEach(function(b){
      b.addEventListener('click',function(){
        document.querySelectorAll('[data-map="'+id+'"] .filters button').forEach(function(x){x.classList.remove('on');});
        b.classList.add('on'); var t=b.getAttribute('data-t'); api.show(t);
        document.querySelectorAll('[data-map="'+id+'"] .plist .card').forEach(function(c){c.style.display=(t==='all'||c.getAttribute('data-t')===t)?'':'none';});
      });
    });
  }
  window.initOutdoorMaps=function(){ build('map-lin',DATA.lin.cfg,DATA.lin.pts); build('map-sca',DATA.sca.cfg,DATA.sca.pts); };
  if(!KEY){ if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',window.initOutdoorMaps);}else{window.initOutdoorMaps();} }
})();
"""

def _plist(pts, mapid):
    out=''
    for p in pts:
        col = dict((l[0],l[2]) for l in LEVELS)[p["lv"]]
        nm = dict((l[0],l[1]) for l in LEVELS)[p["lv"]]
        ty = dict(TYPES)[p["t"]]
        out += (f'<div class="card" data-t="{p["t"]}"><b class="n">{p["n"]}</b><small>{ty} &middot; {p["town"]}</small>'
                f'<span class="lv" style="background:{col}">{nm}</span><p>{p["d"]}</p><small>{p["s"]}</small>'
                f'<a class="go" href="{p["u"]}" target="_blank" rel="noopener">Website &rarr;</a>' + (f'<a class="go" style="margin-top:6px" href="{p["a"]}" target="_blank" rel="noopener">AllTrails &rarr;</a>' if p.get("a") else '') + '</div>')
    return f'<div class="plist">{out}</div>'

def _mapblock(mapid, cfg, pts, intro):
    filt = '<div class="filters"><button class="on" data-t="all">All</button>' + ''.join(f'<button data-t="{k}">{v}</button>' for k,v in TYPES) + '</div>'
    leg = '<div class="legend"><span class="t">Difficulty</span>' + ''.join(f'<span><i style="background:{c}"></i>{n}</span>' for k,n,c in LEVELS) + '<span><i style="background:#E8722A"></i>Rodgers store</span></div>'
    return (f'<div data-map="{mapid}"><p style="max-width:760px">{intro}</p>{filt}<div id="{mapid}" class="omap" role="region" aria-label="Map of ski areas and trails near {cfg["name"]}"></div>{leg}{_plist(pts, mapid)}</div>')

def outdoor_guide():
    data = json.dumps({"lin":{"cfg":LIN,"pts":POINTS_LIN},"sca":{"cfg":SCA,"pts":POINTS_SCA}})
    js = MAP_JS % (data, json.dumps(LEVELS), json.dumps(GMAPS_KEY))
    loader = (f'<script async src="https://maps.googleapis.com/maps/api/js?key={GMAPS_KEY}&callback=initOutdoorMaps"></script>' if GMAPS_KEY else
              '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"><script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>')
    h = hero("Outdoor guide", "Where to ski, ride, hike and bike from either store: every alpine area, Nordic center, trailhead and bike network within 50 miles of Lincoln and 15 miles of Scarborough, color-coded by difficulty.",
             "hiker-autumn-foliage", kicker="Mountains &middot; Trails &middot; Bike parks", short=True, pos="center 45%",
             ctas='<a class="btn accent" href="#lincoln">Lincoln, NH</a><a class="btn ghost-d" href="#scarborough">Scarborough, ME</a>')
    h += crumbs(("Guides","buyers-guide.html"), ("Outdoor Guide",""))
    nearest = ''.join(f'<tr><td><a href="{u}" target="_blank" rel="noopener" style="color:var(--navy);font-weight:700">{n}</a><small>{t} &middot; {s}</small></td><td class="p">{d}</td></tr>' for n,t,d,s,u in NEAREST_ALPINE_SCA)
    h += (f'<section id="lincoln"><div class="wrap">{sechead("Lincoln, New Hampshire", "50-mile radius from 5 Railroad Street.")}'
          + _mapblock("map-lin", LIN, POINTS_LIN, "Thirteen alpine areas, six Nordic centers, twenty-six hikes, eight mountain-bike networks and the notch bike path. Filter by type; click a pin for the numbers and a link to the official site. Trail mixes and vertical are as published by each area.")
          + '</div></section>')
    h += (f'<section class="ice" id="scarborough"><div class="wrap">{sechead("Scarborough, Maine", "15-mile radius from 332 US Route 1.")}'
          + _mapblock("map-sca", SCA, POINTS_SCA, "Coastal walking and hiking preserves, the Eastern Trail, Blackstrap Hill for mountain biking and Harris Farm for groomed cross-country. There is no alpine ski area inside 15 miles; the nearest are listed below the map.")
          + f'<div style="margin-top:28px;max-width:640px"><div class="kicker">Nearest alpine skiing from Scarborough</div><table class="pricelist" style="margin-top:10px"><tbody>{nearest}</tbody></table></div></div></section>')
    h += (f'<section><div class="wrap"><p class="note">Distances are straight-line from each store. Ski-area figures are from the resorts; hike lengths and gains from the US Forest Service, NH State Parks, AMC and Cannon Mountain hiker pages; bike networks from NEMBA chapters and Trailforks; Maine trails from Maine Trail Finder, Portland Trails, Saco Bay Trails and the land trusts. AllTrails links go to the community page for each trail. Lincoln Woods Trail is closed for restoration through November 2026.</p></div></section>')
    h += f'<style>{MAP_CSS}</style>' + loader + f'<script>{js}</script>'
    return page("guides", "Outdoor Guide | Rodgers Ski &amp; Sport", "Ski areas, Nordic centers, hiking trails and mountain-bike networks within 50 miles of Lincoln, NH and 15 miles of Scarborough, ME, mapped and color-coded by difficulty.", h, "outdoor-guide.html")
