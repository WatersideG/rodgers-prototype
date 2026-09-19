# Buyer's Guide and Outdoor Guide pages. Product positioning verified against brand and
# retailer pages Sept 19, 2026 (see resources/research/guides-sources.md). Trail data verified
# against NH State Parks, US Forest Service, AMC, Maine Trail Finder, resort sites and NEMBA.
import json
from shell import *
from data import *
from pages import prod, brands

GMAPS_KEY = ""   # Google Maps JavaScript API key. Empty = the page renders the same data on Leaflet/OpenStreetMap.

# ---------------------------------------------------------------- Buyer's Guide
PROFILES = [
 ("first", "First-timer", "New to the sport or back after years away. Wants forgiveness, easy turn initiation and a fit that does not hurt."),
 ("prog", "Progressing intermediate", "Links parallel turns on blue runs and is starting to ski faster and in more places. Wants gear that rewards better technique without punishing mistakes."),
 ("adv", "Advanced all-mountain", "Skis or rides the whole mountain in most conditions: groomers, bumps, trees, the occasional powder day. One setup that does it all."),
 ("pow", "Powder and freeride", "Chases soft snow, glades and off-piste terrain, sometimes with a skin track involved."),
 ("carve", "Groomer carver", "Lives on corduroy and hardpack and wants edge grip, rebound and a race feel without a race license."),
 ("race", "Racer", "Gate training, USSA and FIS events, masters racing. Discipline-specific skis, race boots and full prep."),
 ("junior", "Junior", "Growing kids from first lessons to the race team. Fit and cost per season matter most."),
]

# (profile, picks[(name, why, source)], image, image_label, brands_note)
SKI_GUIDE = {
 "first": (["Rossignol Experience 82 Ti", "Atomic Maverick 88 CTI"],
           "Rossignol calls the Experience 82 Ti a high-performance all-resort ski and rates it from beginner to expert; Atomic rates the Maverick 88 CTI the same way and describes stable control with a playful all-mountain feel. Most first-timers should rent or lease for a season first, then buy boots before skis.",
           "p-atomic-maverick", "Atomic Maverick"),
 "prog": (["Elan Ripstick 88", "Nordica Unleashed 90", "Blizzard Black Pearl 88 (women)"],
          "Elan builds the Ripstick 88 with a shorter turn radius and narrower waist for grip and control on typical resort conditions. Nordica designs the Unleashed 90 for up-and-coming rippers. Blizzard positions the Black Pearl 88 for women who want confidence and strength along with forgiveness; it is Avery&rsquo;s staff pick.",
          "p-nordica-unleashed", "Nordica Unleashed"),
 "adv": (["Elan Ripstick 96 Black Edition", "Atomic Maverick 96 CTI", "Head Kore 94 Ti", "V&ouml;lkl M7 Mantra", "Nordica Unleashed 98"],
         "The Ripstick 96 Black Edition is Robbie&rsquo;s staff pick and is aimed at advanced and expert skiers who want more muscle than the standard Ripstick. Head calls the Kore 94 Ti its most purely all-mountain ski. V&ouml;lkl&rsquo;s M7 Mantra suits skiers with solid technique who like to lay a ski over at speed. All sit in the 94 to 98 mm waist range.",
         "p-elan-ripstick", "Elan Ripstick 96 Black Edition"),
 "pow": (["Salomon QST 100", "Salomon QST 106", "Atomic Maverick 105 CTI", "Nordica Unleashed 106"],
         "Salomon redesigned the QST line for 2026: the QST 100 is described as the most progressive and versatile ski in the collection for the assertive freerider, and the QST 106 is built for soft snow and off-piste. Atomic&rsquo;s Maverick 105 CTI replaces the Maverick 100 Ti as its playful freeride ski.",
         "p-salomon-qst", "Salomon QST"),
 "carve": (["Atomic Redster Q9 Revoshock S", "Atomic X9S Retro Arc 735 RS"],
           "The Redster Q9 is Atomic&rsquo;s frontside carver for advanced and expert groomer skiers, at a 75 mm waist. The X9S Retro Arc 735 RS, Jamie&rsquo;s staff pick, is a 70th-anniversary limited edition of the Redster X9S with the 1991 ARC graphics, built for skiers who want to rail turns on groomers and hardpack.",
           None, ""),
 "race": (["Atomic Redster S9 and G9 Revoshock S", "Van Deer SL World Cup and GS World Cup", "Rossignol Hero, Head, Fischer and Dynastar race skis"],
          "Atomic describes the Redster S9 as a slalom machine built on race-winning technology and the G9 as race-inspired GS power. Van Deer&rsquo;s World Cup models are built for competitive athletes. All seven race brands are on the wall in Lincoln, with FIS and USSA prep in the tune room.",
          None, ""),
 "junior": (["Junior Seasonal Lease (Scarborough)", "Junior rentals (Lincoln)", "Van Deer GS-JR Pro"],
            "The Scarborough store leases skis, bindings and boots for the season for $159 with pick-ups from October 1; Lincoln rents junior packages from $20 a day. For the race team, Van Deer&rsquo;s GS-JR Pro is a 65 mm FIS-legal junior GS ski.",
            None, ""),
}

SNOWBOARD_GUIDE = {
 "first": (["Nidecker Play", "Nidecker Merc", "Salomon Faction BOA boots"],
           "Nidecker builds the Play, a soft directional twin with CamRock, to give entry-level riders a reliable platform for progression, and describes the Merc as building confidence from the first ride. Salomon&rsquo;s Faction BOA is a soft boot for riders working on linking smooth turns.",
           "p-nidecker", "Nidecker"),
 "prog": (["Lib Tech Skate Banana", "Deeluxe ID boots"],
          "Lib Tech&rsquo;s Skate Banana is a true twin with rocker between the feet and camber at tip and tail; the brand calls it supremely easy riding and rates it from beginner to advanced. Deeluxe positions the ID for the progressing intermediate exploring new runs.",
          "p-lib-tech", "Lib Tech Skate Banana"),
 "adv": (["Never Summer Proto Type 3", "Rome Katana bindings", "ThirtyTwo TM-2 boots"],
         "Never Summer rates the Proto Type 3, a true twin with Triple Camber Recurve and a 6/10 flex, for intermediate to expert riders as a do-it-all board. Rome&rsquo;s Katana is a lightweight, responsive binding for trees and hard carves. ThirtyTwo calls the TM-2 the most versatile boot in its line.",
         "p-never-summer", "Never Summer Proto Type 3"),
 "pow": (["Nidecker Supermatic LT or Carbon bindings", "Ask the Mothership about directional and powder shapes"],
         "Nidecker&rsquo;s Supermatic step-in bindings come in three flexes; LT and Carbon are the stiff, responsive options. Powder-specific board recommendations depend on the current wall in the Mothership, so ask in the store.",
         "p-nidecker-binding", "Nidecker Supermatic"),
 "carve": (["Nidecker Sensor Pro", "Deeluxe Deemon Pro boots"],
           "Nidecker calls the Sensor Pro, a true twin on full camber with a 4/5 flex, the weapon of choice for rippers. Deeluxe&rsquo;s Deemon Pro is a dual-BOA 8/10 boot for advanced and expert riders. Camber and a stiff boot are what hold an edge on hardpack.",
           "p-deeluxe", "Deeluxe"),
 "junior": (["Snowboard rentals (Lincoln)"],
            "Lincoln rents snowboard packages from $45 a day. Snowboards and snowboard rentals are a Lincoln program; the Scarborough store sells skis only.",
            "p-salomon-sb-boot", "Salomon BOA boot"),
}

BOOT_GUIDE = {
 "first": (["Atomic Hawx Prime 90"],
           "Atomic calls the Hawx Prime the most forgiving all-mountain boot in the Prime range, built for confidence and control on a 100 mm medium last. Every boot we sell starts on the Boot Lab bench with a shell fit, so the flex number matters less than the fit.",
           "p-atomic-hawx", "Atomic Hawx"),
 "prog": (["Atomic Hawx Prime 100 and 120", "Tecnica Mach1 110 and 120", "Nordica Unlimited 130"],
          "Tecnica offers the Mach1 in three widths (97, 100 and 103 mm) and three flexes, which makes it easy to match a foot. Nordica positions the Unlimited for skiers charging at the resort and touring on the same boot.",
          "p-nordica-unlimited", "Nordica Unlimited"),
 "adv": (["Atomic Hawx Ultra 130 S", "Salomon S/Pro Alpha 130", "Nordica Promachine 3 130 S", "Tecnica Mach1 130"],
         "All four are 98 mm all-mountain boots at a 130 flex. Salomon describes the S/Pro Alpha 130 as a very stiff flex for aggressive expert skiers; Nordica positions the Promachine 3 130 S for advanced and expert skiers who want precision and power.",
         "p-nordica-machine", "Nordica Promachine"),
 "pow": (["Atomic Hawx Ultra XTD 130 BOA", "Salomon Shift Alpha BOA 130", "Nordica Unlimited 130 DYN"],
         "Atomic calls the Hawx Ultra XTD the ultimate all-mountain crossover boot for skiing in and outside the boundaries. Salomon&rsquo;s Shift Alpha BOA is built for skiers who charge the steepest lines and skin to reach them. Nordica&rsquo;s Unlimited 130 DYN covers resort days, all-day tours and dawn patrols.",
         "p-atomic-hawx-xtd", "Atomic Hawx Ultra XTD"),
 "carve": (["Atomic Redster TX 130", "Nordica Promachine 3 130 S"],
           "Atomic describes the Redster TX as bred on the race course but built for on-piste skiing, on a 96 mm last. A frontside boot like the Promachine 3 gives the same precision with a slightly friendlier fit.",
           "p-salomon-spro", "Salomon S/Pro"),
 "race": (["Rossignol Hero World Cup 130", "Lange RS 130", "Atomic Redster CS 130"],
          "Rossignol&rsquo;s Hero World Cup is race-engineered for competitive racing and on-trail performance. Lange builds the RS 130 for expert skiers, instructors and racers looking for speed, power and precision. Denis&rsquo;s staff pick is the Atomic Redster 130. Race boots are fitted and prepped in the Lincoln Boot Lab.",
          "p-rossignol-boot", "Rossignol Hero World Cup"),
 "junior": (["Lease boots (Scarborough)", "Junior rental boots (Lincoln)", "Boot Lab junior fittings"],
            "Lease and rental packages include boots. For kids on a race program, the Boot Lab fits junior race boots the same way it fits adults: shell fit first, then footbeds and adjustments.",
            None, ""),
}

def _guide_rows(guide, kind):
    out = ''
    for key, name, who in PROFILES:
        if key not in guide: continue
        picks, why, img, lbl = guide[key]
        pic = f'<div class="gpic"><img src="img/{img}.jpg" alt="{lbl}" loading="lazy"><span>{lbl}</span></div>' if img else '<div class="gpic none"></div>'
        chips = ''.join(f'<span>{p}</span>' for p in picks)
        out += (f'<div class="grow" id="{kind}-{key}"><div class="gwho"><div class="kicker">{name}</div><p>{who}</p></div>'
                f'<div class="gbody"><div class="chips">{chips}</div><p>{why}</p></div>{pic}</div>')
    return out

def buyers_guide():
    h = hero("Buyer&rsquo;s guide", "Which skis, snowboards and boots fit which skier. Every recommendation below is a product we stock, matched to the use its maker states for it. The Boot Lab and the sales floor make the final call with you.",
             "hero-ski-carving.jpg", kicker="Skis &middot; Snowboards &middot; Boots", short=True, pos="center 40%",
             ctas='<a class="btn accent" href="#skis">Skis</a><a class="btn ghost-d" href="#snowboards">Snowboards</a><a class="btn ghost-d" href="#boots">Boots</a>')
    h += crumbs(("Guides","buyers-guide.html"), ("Buyer&rsquo;s Guide",""))
    h += (f'<section><div class="wrap"><p style="max-width:720px">Seven skier profiles run through each category. Find yourself in the left column, then read across. Prices, sizes and this season&rsquo;s stock are in the store; call either location or book a fitting.</p>'
          f'<div class="chips" style="margin-top:18px">' + ''.join(f'<span>{n}</span>' for _,n,_ in PROFILES) + '</div></div></section>')
    h += (f'<section class="ice" id="skis"><div class="wrap">{sechead("Skis", "Twelve ski brands in Lincoln and Scarborough.")}{brands(SKI_BRANDS)}<div class="guide">{_guide_rows(SKI_GUIDE,"ski")}</div></div></section>')
    h += (f'<section id="snowboards"><div class="wrap">{sechead("Snowboards", "The Mothership, inside the Lincoln store. Scarborough does not sell snowboards.")}{brands(SNOWBOARD_BRANDS)}<div class="guide">{_guide_rows(SNOWBOARD_GUIDE,"sb")}</div></div></section>')
    h += (f'<section class="ice" id="boots"><div class="wrap">{sechead("Ski boots", "Fitted in the Boot Lab. Eleven boot brands.")}{brands(BOOT_BRANDS)}<div class="guide">{_guide_rows(BOOT_GUIDE,"boot")}</div>'
          f'<div style="margin-top:28px"><a class="btn" href="boot-lab.html#book">Book a boot fitting</a> <a class="btn ghost" href="rentals.html">Rentals in Lincoln</a> <a class="btn ghost" href="lease.html">Junior lease in Scarborough</a></div></div></section>')
    h += (f'<section><div class="wrap"><p class="note">Positioning statements are paraphrased from each brand&rsquo;s product page or its authorized retailers as of September 2026. Models change each season; this page is a Payload collection (profile, category, picks, image) so the shop can update it without a developer.</p></div></section>')
    return page("guides", "Buyer&rsquo;s Guide | Rodgers Ski &amp; Sport", "Which skis, snowboards and ski boots fit first-timers, intermediates, all-mountain skiers, powder skiers, carvers, racers and juniors, from the brands Rodgers Ski & Sport carries.", h, "buyers-guide.html")

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
 dict(n="Franconia Ridge Loop", t="hike", lv="expert", lat=44.1420, lon=-71.6811, town="Franconia Notch, NH", s="8.3&ndash;8.5 mi loop &middot; about 3,600&ndash;3,800 ft gain", d="Falling Waters up, Old Bridle Path down: the signature above-treeline traverse over Little Haystack, Lincoln and Lafayette.", u="https://www.nhstateparks.org/find-parks-trails/franconia-notch-state-park"),
 dict(n="Mount Lafayette via Old Bridle Path", t="hike", lv="difficult", lat=44.1420, lon=-71.6812, town="Franconia Notch, NH", s="About 8 mi round trip &middot; about 3,500 ft gain", d="Past AMC Greenleaf Hut to the 5,249 ft summit.", u="https://www.outdoors.org/destinations/new-hampshire/greenleaf-hut/"),
 dict(n="Flume Gorge", t="hike", lv="easy", lat=44.1020, lon=-71.6775, town="Lincoln, NH", s="2.0 mi loop &middot; timed tickets, seasonal", d="Boardwalk through an 800 ft granite chasm; the full loop is required.", u="https://www.nhstateparks.org/find-parks-trails/flume-gorge"),
 dict(n="Mount Pemigewasset (Indian Head)", t="hike", lv="moderate", lat=44.1020, lon=-71.6775, town="Lincoln, NH", s="3.4 mi round trip &middot; about 1,250 ft gain", d="Short climb from the Flume lot to a cliff-top view over the notch.", u="https://www.cannonmt.com/attractions/hiking-hiker-parking"),
 dict(n="Lonesome Lake", t="hike", lv="moderate", lat=44.1419, lon=-71.6840, town="Franconia Notch, NH", s="3.1 mi loop &middot; about 1,000 ft gain", d="Family favorite from Lafayette Place to AMC Lonesome Lake Hut.", u="https://www.cannonmt.com/attractions/hiking-hiker-parking"),
 dict(n="North and South Kinsman", t="hike", lv="difficult", lat=44.1419, lon=-71.6840, town="Franconia Notch, NH", s="10 mi round trip &middot; about 3,150 ft gain", d="Two 4,000-footers via Lonesome Lake and the Fishin&rsquo; Jimmy Trail.", u="https://www.outdoors.org"),
 dict(n="Welch&ndash;Dickey Loop", t="hike", lv="moderate", lat=43.9046, lon=-71.5890, town="Thornton, NH", s="4.4 mi loop", d="Open granite ledges with big views for modest effort.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/welch-dickey-trailhead"),
 dict(n="Mount Moosilauke, Gorge Brook Trail", t="hike", lv="difficult", lat=43.9772, lon=-71.8172, town="Benton, NH", s="7.2 mi round trip &middot; about 2,350 ft gain", d="Bald 4,802 ft summit from Dartmouth&rsquo;s Ravine Lodge.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/ravine-lodge-trailhead"),
 dict(n="Lincoln Woods Trail", t="hike", lv="easy", lat=44.0639, lon=-71.5883, town="Lincoln, NH", s="Flat railroad grade, 3 mi each way &middot; closed for restoration June 15 to November 2026", d="Old logging railroad along the East Branch into the Pemigewasset Wilderness; Franconia Falls spur.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/lincoln-woods-trailhead"),
 dict(n="Arethusa Falls", t="hike", lv="moderate", lat=44.1477, lon=-71.3696, town="Hart&rsquo;s Location, NH", s="About 3 mi round trip &middot; about 900 ft gain", d="New Hampshire&rsquo;s tallest single-drop waterfall in Crawford Notch State Park.", u="https://www.nhstateparks.org/find-parks-trails/crawford-notch-state-park"),
 dict(n="Mount Washington via Tuckerman Ravine", t="hike", lv="expert", lat=44.2575, lon=-71.2531, town="Pinkham Notch, NH", s="8.4 mi round trip &middot; 4,250 ft gain", d="The classic route up the Northeast&rsquo;s highest peak from AMC Pinkham Notch.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/pinkham-notch-trailhead"),
 dict(n="Artist&rsquo;s Bluff and Bald Mountain", t="hike", lv="easy", lat=44.1798, lon=-71.7020, town="Franconia, NH", s="1.5 mi loop &middot; about 535 ft gain", d="Short scramble to the postcard view of Echo Lake and Cannon.", u="https://www.cannonmt.com/attractions/hiking-hiker-parking"),
 dict(n="Mount Willard", t="hike", lv="moderate", lat=44.2173, lon=-71.4127, town="Crawford Notch, NH", s="About 3 mi round trip &middot; about 880 ft gain", d="Easy grade from Crawford Depot to a cliff view straight down the notch.", u="https://www.nhstateparks.org/find-parks-trails/crawford-notch-state-park"),
 dict(n="Champney Falls and Mount Chocorua", t="hike", lv="difficult", lat=43.9899, lon=-71.2991, town="Albany, NH", s="Falls about 3 mi, 500 ft &middot; summit 7.6 mi, 2,250 ft", d="Kancamagus trailhead to a waterfall and the rocky Chocorua summit.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/champney-falls-trailhead"),
 dict(n="Mount Osceola", t="hike", lv="difficult", lat=43.9835, lon=-71.5592, town="Livermore, NH", s="6.4 mi round trip &middot; Tripoli Road closed November to late May", d="Ledge summit above Waterville Valley.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/osceola-trailhead"),
 dict(n="Zealand Falls", t="hike", lv="easy", lat=44.2247, lon=-71.4791, town="Bethlehem, NH", s="4.6&ndash;5 mi round trip &middot; about 450 ft gain", d="Gentle walk past beaver ponds to AMC Zealand Falls Hut.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/zealand-trailhead-forest-rd-16"),
 dict(n="Sabbaday Falls", t="hike", lv="easy", lat=43.9972, lon=-71.3929, town="Waterville Valley, NH", s="15-minute walk from the Kancamagus", d="Flume-and-pool waterfall walk.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/sabbaday-falls-observation-site"),
 dict(n="Diana&rsquo;s Baths", t="hike", lv="easy", lat=44.0747, lon=-71.1630, town="Bartlett, NH", s="1.5 mi round trip &middot; fee lot", d="Cascades and pools near North Conway.", u="https://www.fs.usda.gov/r09/whitemountain/recreation/dianas-baths"),
 dict(n="Georgiana Falls", t="hike", lv="moderate", lat=44.0671, lon=-71.6888, town="Lincoln, NH", s="2.2&ndash;2.6 mi round trip &middot; about 730 ft gain", d="The closest waterfall hike to the Lincoln store, off Hanson Farm Road.", u="https://www.fs.usda.gov/r09/whitemountain"),
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
 dict(n="Franconia Notch Recreation Path", t="path", lv="easy", lat=44.1300, lon=-71.6900, town="Lincoln to Franconia, NH", s="8.8 mi paved, Flume to Skookumchuck &middot; about 800 ft south to north", d="State-park bike path through the notch past the Basin, Profile Lake and Echo Lake.", u="https://www.cannonmt.com/attractions/franconia-notch-recreation-path"),
]

POINTS_SCA = [
 dict(n="Eastern Trail, Scarborough Marsh", t="path", lv="easy", lat=43.5700, lon=-70.3500, town="Scarborough, ME", s="8.4 mi off-road Saco to Scarborough &middot; crushed stone, accessible", d="Flat rail trail across Maine&rsquo;s largest salt marsh; gravel bikes welcome.", u="https://www.easterntrail.org"),
 dict(n="Pleasant Hill Preserve", t="hike", lv="easy", lat=43.5960, lon=-70.3080, town="Scarborough, ME", s="2.4 mi of trails, 244 acres &middot; no bikes", d="Scarborough Land Trust preserve a mile from the store.", u="https://scarboroughlandtrust.org/slt-trails/pleasant-hill-preserve/"),
 dict(n="Libby River Farm Preserve", t="hike", lv="easy", lat=43.566, lon=-70.301, town="Scarborough, ME", s="1.3 mi, 153 acres &middot; no bikes", d="Fields and river frontage on the Libby River.", u="https://scarboroughlandtrust.org"),
 dict(n="Scarborough Marsh Audubon Center", t="hike", lv="easy", lat=43.5643, lon=-70.3732, town="Scarborough, ME", s="0.3 mi nature trail &middot; canoe rentals", d="Maine Audubon&rsquo;s marsh center on Pine Point Road.", u="https://maineaudubon.org/visit/scarborough-marsh/"),
 dict(n="Fuller Farm Preserve", t="hike", lv="easy", lat=43.5880, lon=-70.4130, town="Scarborough, ME", s="4 mi of loops, 224 acres &middot; cross-country ski and snowshoe", d="Fields, woods and the Nonesuch River.", u="https://scarboroughlandtrust.org/slt-trails/fuller-farm-preserve/"),
 dict(n="Crescent Beach and Kettle Cove", t="hike", lv="easy", lat=43.5648, lon=-70.2227, town="Cape Elizabeth, ME", s="2.2 mi combined trail network", d="State park beach and shore loops.", u="https://www.maine.gov/dacf/parks"),
 dict(n="Two Lights State Park", t="hike", lv="easy", lat=43.5602, lon=-70.2049, town="Cape Elizabeth, ME", s="1.9 mi, 41 acres of headlands", d="Rocky headlands and two lighthouses.", u="https://www.maine.gov/dacf/parks"),
 dict(n="Fort Williams Park", t="hike", lv="easy", lat=43.6235, lon=-70.2102, town="Cape Elizabeth, ME", s="0.4 mi Cliff Walk plus park paths", d="Portland Head Light and the shore.", u="https://www.fortwilliams.org"),
 dict(n="Fore River Sanctuary", t="hike", lv="easy", lat=43.6672, lon=-70.3177, town="Portland, ME", s="About 2 mi of trails &middot; Jewell Falls", d="Portland Trails&rsquo; 85-acre sanctuary with the city&rsquo;s only waterfall.", u="https://trails.org"),
 dict(n="Baxter Woods", t="hike", lv="easy", lat=43.6767, lon=-70.2895, town="Portland, ME", s="1.5 mi network", d="City woodland off Forest Avenue.", u="https://www.mainetrailfinder.com/trails/trail/baxter-woods"),
 dict(n="Saco Heath Preserve", t="hike", lv="easy", lat=43.5462, lon=-70.4711, town="Saco, ME", s="2.1 mi round trip boardwalk, 1,223 acres", d="Nature Conservancy boardwalk across a raised peat bog.", u="https://www.nature.org/en-us/get-involved/how-to-help/places-we-protect/saco-heath-preserve/"),
 dict(n="Ferry Beach State Park", t="hike", lv="easy", lat=43.4782, lon=-70.3875, town="Saco, ME", s="1.7 mi trail network plus beach", d="Woods, tupelo swamp and sand.", u="https://www.maine.gov/dacf/parks"),
 dict(n="Presumpscot River Preserve", t="hike", lv="moderate", lat=43.7220, lon=-70.2818, town="Portland, ME", s="3.5 mi network with Oat Nuts Park", d="River gorge trails on the Portland and Falmouth line.", u="https://www.mainetrailfinder.com/trails/trail/presumpscot-river-preserve-and-oat-nuts-park"),
 dict(n="Mackworth Island", t="hike", lv="easy", lat=43.6893, lon=-70.2305, town="Falmouth, ME", s="1.5 mi shore loop", d="Causeway island in Casco Bay.", u="https://www.maine.gov/dacf/parks"),
 dict(n="Blackstrap Hill Community Forest", t="mtb", lv="difficult", lat=43.7775, lon=-70.3234, town="Falmouth, ME", s="24 mi, 38 trails: 7 green / 5 blue / 24 black / 2 double black &middot; grades over 20%", d="Greater Portland&rsquo;s main technical mountain-bike destination; Flow Creek from Hurricane Road.", u="https://falmouthlandtrust.org/properties/blackstrap-hill-preserve"),
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
  function popup(p){return '<b>'+p.n+'</b>'+TYPE[p.t]+' &middot; '+p.town+'<br><span style="color:'+COLOR[p.lv]+';font-weight:700">'+NAME[p.lv]+'</span> &middot; '+p.s+'<br>'+p.d+'<br><a href="'+p.u+'" target="_blank" rel="noopener">Website</a>';}
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
                f'<a class="go" href="{p["u"]}" target="_blank" rel="noopener">Website &rarr;</a></div>')
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
             "hero-hiker-ridge.jpg", kicker="Mountains &middot; Trails &middot; Bike parks", short=True, pos="center 45%",
             ctas='<a class="btn accent" href="#lincoln">Lincoln, NH</a><a class="btn ghost-d" href="#scarborough">Scarborough, ME</a>')
    h += crumbs(("Guides","buyers-guide.html"), ("Outdoor Guide",""))
    nearest = ''.join(f'<tr><td><a href="{u}" target="_blank" rel="noopener" style="color:var(--navy);font-weight:700">{n}</a><small>{t} &middot; {s}</small></td><td class="p">{d}</td></tr>' for n,t,d,s,u in NEAREST_ALPINE_SCA)
    h += (f'<section id="lincoln"><div class="wrap">{sechead("Lincoln, New Hampshire", "50-mile radius from 5 Railroad Street.")}'
          + _mapblock("map-lin", LIN, POINTS_LIN, "Thirteen alpine areas, six Nordic centers, twenty hikes, eight mountain-bike networks and the notch bike path. Filter by type; click a pin for the numbers and a link to the official site. Trail mixes and vertical are as published by each area.")
          + '</div></section>')
    h += (f'<section class="ice" id="scarborough"><div class="wrap">{sechead("Scarborough, Maine", "15-mile radius from 332 US Route 1.")}'
          + _mapblock("map-sca", SCA, POINTS_SCA, "Coastal walking and hiking preserves, the Eastern Trail, Blackstrap Hill for mountain biking and Harris Farm for groomed cross-country. There is no alpine ski area inside 15 miles; the nearest are listed below the map.")
          + f'<div style="margin-top:28px;max-width:640px"><div class="kicker">Nearest alpine skiing from Scarborough</div><table class="pricelist" style="margin-top:10px"><tbody>{nearest}</tbody></table></div></div></section>')
    h += (f'<section><div class="wrap"><p class="note">Distances are straight-line from each store. Ski-area figures are from the resorts; hike lengths and gains from the US Forest Service, NH State Parks, AMC and Cannon Mountain hiker pages; bike networks from NEMBA chapters and Trailforks; Maine trails from Maine Trail Finder and the land trusts. Lincoln Woods Trail is closed for restoration through November 2026. Map pins are a Payload collection (name, type, level, coordinates, stats, link) so the shop can add or retire a location without a developer.</p></div></section>')
    h += f'<style>{MAP_CSS}</style>' + loader + f'<script>{js}</script>'
    return page("guides", "Outdoor Guide | Rodgers Ski &amp; Sport", "Ski areas, Nordic centers, hiking trails and mountain-bike networks within 50 miles of Lincoln, NH and 15 miles of Scarborough, ME, mapped and color-coded by difficulty.", h, "outdoor-guide.html")
