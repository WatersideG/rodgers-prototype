from shell import *
from data import *

def prod(items):
    return f'<div class="prod n{len(items)}">' + ''.join(f'<div><img src="img/{i}.jpg" alt="{n}" loading="lazy"><b>{n}</b>{"<span>"+s+"</span>" if s else ""}</div>' for i,n,s in items) + '</div>'

def brands(lst): return brand_wall(lst)

def pick_card(p, compact=False):
    return (f'<div class="pick"><div class="ph"><img src="img/{p["img"]}" alt="{p["who"]} with the {p["product"]} outside the Lincoln store" loading="lazy"></div>'
            f'<div class="body"><div class="who">Staff pick &middot; {p["who"]}, {p["store"]}</div><h3>{p["product"]}</h3>'
            f'<blockquote>&ldquo;{p["quote"]}&rdquo;</blockquote><div class="meta">{p["tag"]} &middot; posted {p["date"]} &middot; <a href="{p["link"]}" style="color:var(--navy);font-weight:700">on Instagram</a></div></div></div>')

def post_card(p):
    return (f'<a class="card img post" href="{p["slug"]}">{ph(p["img"], p["alt"], "r169")}<div class="body"><div class="cat">{p["cat"]}</div><h3>{p["title"]}</h3>'
            f'<p>{p["teaser"]}</p><div class="date">{p["date"]}</div></div></a>')

def store_cta(store):
    return (f'<a class="btn" href="{store["maps"]}">Get directions</a> <a class="btn ghost" href="tel:{store["teltag"]}">Call {store["tel"]}</a>')

def find_store(store, rows, img, alt):
    return (f'<section class="ice"><div class="wrap">{sechead("Find the store", store["addr"])}'
            f'<div class="grid g3"><div style="grid-column:span 2">{map_embed(store)}</div>{hours_box(store, rows)}</div>'
            f'<div style="margin-top:22px">{ph(img, alt, "r21")}</div></div></section>')

LIN_HOURS = [("Every day","8:30 – 5:00")]
SCA_HOURS = [("Monday – Tuesday","10 – 6"),("Wednesday","Closed"),("Thursday – Friday","10 – 6"),("Saturday","10 – 5"),("Sunday","11 – 5")]

TENT = next(x for x in POSTS if x["slug"]=="journal-fall-tent-sale.html")
def journal_teaser():
    p = TENT
    return (f'<section class="tight" style="padding-top:0"><div class="wrap"><div class="feature">'
            f'<div class="ph"><img src="img/{p["img"]}" alt="{p["alt"]}" loading="lazy"></div>'
            f'<div class="body"><span class="pill orange">Now on &middot; through October 12</span><h2>{p["title"]}</h2>'
            f'<p>{p["teaser"]}</p><p style="margin-top:8px;font-size:13.5px;color:var(--steel)">5 Railroad St, Lincoln, NH &middot; open every day 8:30&ndash;5. Scarborough shoppers: the sale is at the Lincoln store this fall.</p>'
            f'<div style="margin-top:20px"><a class="btn accent" href="{p["slug"]}">Tent sale details</a> <a class="btn ghost" href="staff-picks.html">Staff picks</a></div></div></div></div></section>')

# =====================================================================================
def home():
    h = hero("Skis, boards, bikes and boots.",
             "Two family-run ski and bike shops: Lincoln, New Hampshire, first exit off I-93 before Loon, and Scarborough, Maine, off I-95 on Route 1. Gear, fitting and tuning from people who use what they sell.",
             "skier-powder-gondola",
             ctas='<a class="btn accent" href="lincoln-nh.html">Lincoln, NH</a><a class="btn ondark" href="scarborough-me.html">Scarborough, ME</a>',
             pos="center 45%")
    h += (f'<div class="wxband"><div class="wrap"><div class="grid g2">{weather(LINCOLN, mini=True)}{weather(SCARB, mini=True)}</div></div></div>')
    h += '<div style="height:26px"></div>' + journal_teaser()
    # two stores
    h += (f'<section style="padding-top:20px"><div class="wrap">{sechead("Two stores. One standard.", "Each store has its own departments and its own programs. Pick yours; hours and phone numbers stay at the top of every page.")}'
          f'<div class="grid g2">'
          f'<a class="card img" href="lincoln-nh.html">{ph("lincoln-roadside-sign.jpg","The Lincoln, NH store on Railroad Street, with the I-93 sign","r169","Lincoln, NH")}<div class="body"><h3>Lincoln, New Hampshire</h3>'
          f'<p>First shop off I-93, minutes from Loon. Skis, snowboards (the Mothership), bikes, rentals, the Boot Lab and the tune room. Open every day 8:30&ndash;5 &middot; {LINCOLN["tel"]}</p><span class="go">Visit the Lincoln store</span></div></a>'
          f'<a class="card img" href="scarborough-me.html">{ph("scarborough-storefront-sunny-wide.jpg","The Scarborough, ME store on Route 1","r169","Scarborough, ME")}<div class="body"><h3>Scarborough, Maine</h3>'
          f'<p>Southern Maine&rsquo;s ski and bike shop since 1986, off I-95 on Route 1. Skis, boots, bikes, tuning, boot work and the Junior Seasonal Lease. No rentals or snowboards at this store. Mon&ndash;Tue and Thu&ndash;Fri 10&ndash;6, Sat 10&ndash;5, Sun 11&ndash;5, closed Wednesday &middot; {SCARB["tel"]}</p><span class="go">Visit the Scarborough store</span></div></a>'
          f'</div></div></section>')
    h += credband(["Family-run since 1974","Ski Magazine Gold Medal Shop","Seven race brands under one roof","Masterfit and Sidas certified boot fitters"])
    # seasonal cards
    import datetime
    season = SEASON_OF[datetime.date.today().month]
    cards = SEASON_CARDS[season]
    h += (f'<section><div class="wrap">{sechead(SEASON_TITLE[season], "The products and services most people come in for at this time of year.", ("All departments","lincoln-nh.html"))}'
          f'<div class="grid g4 season">' + ''.join(card(*c) for c in cards) + '</div></div></section>')
    # boot lab + tune
    h += (f'<section class="ice"><div class="wrap split"><div>{ph("tuning-montana.jpg","Race skis on the Montana grinder","r43","Lincoln tune room")}</div>'
          f'<div><div class="kicker">The Boot Lab &amp; tune bench</div><h2 class="display" style="font-size:32px">Watch a fresh edge come to life</h2>'
          f'<p style="margin-top:16px">Our techs hand-tune every pair on a Montana stone grinder, with race-room standards and every service itemized and priced. Boot fitting runs the same way: certified fitters, custom insoles, punches, grinds, stance and alignment, and full FIS and USSA race prep in Lincoln.</p>'
          f'<div style="margin-top:24px"><a class="btn" href="boot-lab.html">The Boot Lab</a><a class="btn ghost" style="margin-left:10px" href="lincoln-nh-services.html">Tuning menus</a></div></div></div></section>')
    # staff picks
    # story band
    h += ('<section class="navy"><div class="wrap" style="text-align:center;max-width:760px"><div class="qm" style="color:#fff">&ldquo;</div>'
          '<h2 class="display" style="font-size:clamp(26px,3.4vw,38px)">Family-run since 1974</h2>'
          '<p style="margin-top:14px;color:#9FB4CE">A few pairs of skis sold from a Datsun pickup at Plymouth State in 1974. The first Rodgers Ski Outlet in Lincoln in 1981, Scarborough in 1986, snowboarding brought east in &rsquo;88. The same family standard, fifty years on.</p>'
          '<a class="btn ondark" style="margin-top:24px" href="about.html">Our story</a></div></section>')
    # journal + instagram
    h += (f'<section><div class="wrap">{sechead("From the journal", "News, promotions, new brands, racing and what the local mountains are up to.", ("All posts","journal.html"))}'
          f'<div class="grid g3">{"".join(post_card(p) for p in [x for x in POSTS if x is not TENT][:3])}</div></div></section>')
    ig = [("staffpick-robbie-elan-ripstick-96.jpg","Robbie with the Elan Ripstick 96 Black"),("lincoln-race-wall-alt.jpg","Race wall at Lincoln"),("staffpick-avery-blizzard-black-pearl.jpg","Avery with the Blizzard Black Pearl"),
          ("smith-goggle-case.jpg","Smith goggle case"),("staffpick-jamie-atomic-arc-735.jpg","Jamie with the Atomic Arc 735 RS"),("scarborough-atomic-boot-bench.jpg","Scarborough binding bench")]
    h += (f'<section class="ice tight"><div class="wrap">{sechead("@rodgersski", "Follow along on Instagram: staff picks, deal reveals, new gear, and race days at Loon.", ("Instagram", SOCIAL["ig"]))}'
          f'<div class="grid g6">' + ''.join(f'<a class="ph r1" href="{SOCIAL["ig"]}"><img src="img/{i}" alt="{a}" loading="lazy"></a>' for i,a in ig) + '</div>'
          f'</div></section>')
    return page("", "Rodgers Ski &amp; Sport | Ski, Bike &amp; Boot Fitting &mdash; Lincoln NH &amp; Scarborough ME",
                "Family-run ski and bike shops in Lincoln, NH and Scarborough, ME. Skis, boots, bikes, the Boot Lab, tuning, race gear from seven brands, and the annual Fall Tent Sale.", h, "index.html")

# =====================================================================================
def lincoln():
    h = hero("Lincoln, New Hampshire", "5 Railroad St, first exit off I-93, minutes from Loon. Skis, the Mothership snowboard shop, bikes, rentals, the Boot Lab and the tune room. Open every day 8:30&ndash;5.",
             "skier-carving-red-jacket", kicker="Rodgers Ski &amp; Sport &middot; Lincoln", short=True, pos="center 40%",
             ctas=f'<a class="btn accent" href="{LINCOLN["maps"]}">Directions</a><a class="btn ghost-d" href="tel:{LINCOLN["teltag"]}">Call {LINCOLN["tel"]}</a>')
    h += crumbs(("Lincoln, NH",""))
    h += f'<section class="tight"><div class="wrap">{weather(LINCOLN)}</div></section>'
    h += (f'<section style="padding-top:10px"><div class="wrap split"><div><div class="kicker">The location advantage</div><h2 class="display" style="font-size:32px">First shop skiers reach off I-93</h2>'
          f'<p style="margin-top:16px">Heading to Loon, Cannon or anywhere in the Whites: stop here first, gear up, and skip the base-area lines. New Hampshire has no sales tax, and our staff spends its days off on the same hills you&rsquo;re driving to.</p>'
          f'<p style="margin-top:10px">This is the store for rentals, snowboards and full race prep. Scarborough, our Maine store, runs a different program: no rentals or snowboards there, but the Junior Seasonal Lease and a full ski and bike shop.</p>'
          f'<div style="margin-top:22px"><a class="btn" href="rentals.html">Rental rates</a><a class="btn ghost" style="margin-left:10px" href="boot-lab.html#book">Book a boot fit</a></div></div>'
          f'<div>{ph("lincoln-service-desk.jpg","The Lincoln service desk with the tuning menu boards","r43","Service desk")}</div></div></section>')
    deps = [("lincoln-nh-ski.html","lincoln-ski-wall-armada-salomon.jpg","Armada and Salomon skis on the Lincoln wall","Ski","Skis, boots and bindings from thirteen brands, staffed by people who ski Loon and Cannon weekly."),
            ("lincoln-nh-snowboard.html","mothership-snowboard-wall.jpg","Snowboards on the Mothership wall","Snowboard","The Mothership: riding east since &rsquo;88. Boards, boots and bindings."),
            ("lincoln-nh-bikes.html","hero-mtb-pan.jpg","A mountain biker on a forest trail","Bikes","Mountain, road, hybrid, e-bikes and kids&rsquo; bikes, with tunes from $50."),
            ("lincoln-nh-services.html","tuning-montana.jpg","Skis on the Montana grinder","Services &amp; Tuning","Tunes from $40 to the Full Monty, mounting, race day tunes."),
            ("rentals.html","hero-lincoln-family.jpg","A family on skis at the base of Loon","Rentals","Junior packages from $20 a day, demo skis, snowboards, snowshoes and cross-country."),
            ("lincoln-nh-accessories.html","accessories-flatlay.jpg","Gloves, goggles, beanie and socks laid out on a bench","Accessories","Helmets, goggles, gloves, heated gear, hats, bags. Forgot something on the way up? We&rsquo;re the first exit."),
            ("lincoln-nh-apparel.html","lincoln-apparel-floor.jpg","The apparel floor at the Lincoln store","Apparel","Outerwear from twenty-two brands, layers, and sweaters for East Coast conditions."),
            ("boot-lab.html","boot-lab-bench.jpg","Race boots on the Boot Lab bench","The Boot Lab","Custom fitting, insoles, canting, stance and alignment, and FIS and USSA race prep.")]
    h += (f'<section class="ice"><div class="wrap">{sechead("Departments", "Everything in the Lincoln store, each on its own page.")}<div class="grid g4 season">' + ''.join(card(*d, go="") for d in deps) + '</div></div></section>')
    h += (f'<section><div class="wrap">{sechead("Staff picks from Lincoln", "", ("All staff picks","staff-picks.html"))}<div class="grid g2">{pick_card(STAFF_PICKS[2])}{pick_card(STAFF_PICKS[3])}</div></div></section>')
    h += find_store(LINCOLN, LIN_HOURS, "lincoln-roadside-sign.jpg", "The Rodgers Ski & Sport sign on Railroad Street in Lincoln, with the I-93 sign")
    return page("lincoln", "Lincoln, NH | Rodgers Ski &amp; Sport", "Rodgers Ski & Sport in Lincoln, NH: skis, snowboards, bikes, rentals, the Boot Lab and tuning, first exit off I-93 before Loon. Open every day 8:30–5.", h, "lincoln-nh.html")

def scarborough():
    h = hero("Scarborough, Maine", "332 US Route 1, off I-95. Southern Maine&rsquo;s ski and bike shop since 1986: skis, boots, bikes, tuning, boot work and the Junior Seasonal Lease.",
             "mountain-bikers-ridge-view", kicker="Rodgers Ski &amp; Sport &middot; Scarborough", short=True, pos="center 40%",
             ctas=f'<a class="btn accent" href="{SCARB["maps"]}">Directions</a><a class="btn ghost-d" href="tel:{SCARB["teltag"]}">Call {SCARB["tel"]}</a>')
    h += crumbs(("Scarborough, ME",""))
    h += f'<section class="tight"><div class="wrap">{weather(SCARB)}</div></section>'
    h += (f'<section style="padding-top:10px"><div class="wrap split"><div><div class="kicker">Southern Maine</div><h2 class="display" style="font-size:32px">The area ski and bike shop</h2>'
          f'<p style="margin-top:16px">Serving Portland-area skiers, riders and cyclists since 1986. Day-tripping to Sunday River, Sugarloaf or Pleasant Mountain, or driving to the Whites: stop on Route 1 first.</p>'
          f'<p style="margin-top:10px">What&rsquo;s different here: Scarborough sells skis, not snowboards, and does not rent equipment. Families use the Junior Seasonal Lease instead, and the bike shop runs year-round. Rentals and snowboards are at the Lincoln, NH store.</p>'
          f'<div style="margin-top:22px"><a class="btn" href="lease.html">Junior Seasonal Lease</a><a class="btn ghost" style="margin-left:10px" href="scarborough-me-services.html">Service menu</a></div></div>'
          f'<div>{ph("scarborough-atomic-ski-wall.jpg","The ski wall under the lit Atomic and Salomon signs in Scarborough","r43","Scarborough ski wall")}</div></div></section>')
    deps = [("scarborough-me-ski.html","scarborough-ski-rows.jpg","Skis on the Scarborough wall","Ski","Skis, boots and bindings for Maine day-trips and weekends in the Whites."),
            ("scarborough-me-bikes.html","hero-road-coast.jpg","A cyclist on the Maine coast road","Bikes","Mountain, cruisers, gravel, hybrids, e-bikes and kids&rsquo; bikes, with service and builds."),
            ("scarborough-me-services.html","scarborough-atomic-boot-bench.jpg","A race boot on the bench in Scarborough","Services &amp; Tuning","Ski and board tunes, stone grinding, race tunes, mounting and boot work."),
            ("lease.html","hero-lincoln-family.jpg","Kids on skis","Junior Seasonal Lease","Skis, bindings and boots for the season, $159, pick-ups from October 1."),
            ("scarborough-me-accessories.html","accessories-flatlay.jpg","Gloves, goggles, beanie and socks laid out on a bench","Accessories","Helmets, goggles, gloves, heated gear, hats and bags, stocked for Maine winters."),
            ("boot-lab.html","scarborough-race-wall.jpg","Race skis under the Atomic sign in Scarborough","Boot work","Shell and liner heat molding, punches, spot grinds and heel lifts at the Maine store.")]
    h += (f'<section class="ice"><div class="wrap">{sechead("Departments", "Everything in the Scarborough store, each on its own page.")}<div class="grid g3 season">' + ''.join(card(*d, go="") for d in deps) + '</div></div></section>')
    h += (f'<section><div class="wrap split rev"><div>{ph("rodgers-ski-outlet-sign.jpg","The original Rodgers Ski Outlet sign inside the Scarborough store","r43","Since 1986")}</div>'
          f'<div><div class="kicker">Community</div><h2 class="display" style="font-size:30px">Group rides and the trails out back</h2>'
          f'<p style="margin-top:16px">The Scarborough shop hosts social, no-drop group rides on the railroad-track trails off Highland Avenue: flat terrain, all ages and skill levels, the Rodgers van at the entrance so you won&rsquo;t miss the turn. Ride dates are posted on Instagram and in the journal.</p>'
          f'<p style="margin-top:10px">In 2024 SEDCO gave the Scarborough store its Legacy Business Award for serving the town and its neighbors since 1986.</p>'
          f'<div style="margin-top:22px"><a class="btn ghost" href="journal.html">Journal</a></div></div></div></section>')
    h += find_store(SCARB, SCA_HOURS, "scarborough-storefront-sunny-wide.jpg", "The Scarborough store on Route 1")
    return page("scarb", "Scarborough, ME | Rodgers Ski &amp; Sport", "Rodgers Ski & Sport in Scarborough, ME: skis, boots, bikes, tuning, boot work and the Junior Seasonal Lease on Route 1 since 1986. Closed Wednesdays.", h, "scarborough-me.html")

# =====================================================================================
def dept(fname, active, store, crumb_store, title, sub, img, pos, body, meta):
    h = hero(title, sub, img, kicker=f'Rodgers Ski &amp; Sport &middot; {store["short"]}', short=True, pos=pos)
    h += crumbs((crumb_store[0], crumb_store[1]), (title, ""))
    h += body
    return page(active, f'{title} &middot; {store["name"]} | Rodgers Ski &amp; Sport', meta, h, fname)

def lin_ski():
    b = (f'<section><div class="wrap">{sechead("Skis", "We can&rsquo;t list them all, but we&rsquo;ve skied them all. Stop by and talk gear with a staff that spends its time off on snow.")}'
         f'<div class="split"><div>{ph("lincoln-ski-wall-armada-salomon.jpg","Armada and Salomon skis on the Lincoln wall","r43")}</div><div>'
         f'<h3 style="font-size:20px;margin-bottom:10px">Twelve ski brands, one wall</h3><p>Rossignol, Dynastar, Head, K&auml;stle, Elan, Atomic, Van Deer, Salomon, Armada, V&ouml;lkl, Fischer and Blizzard. The full 2027 Atomic lineup, skis, bindings, boots and race skis, arrived in late August; 2026/27 demos and pre-mounted skis from nine of these brands are on the floor for the Fall Tent Sale.</p>'
         f'<div style="margin-top:14px">{brands(SKI_BRANDS)}</div></div></div>'
         f'<div style="margin-top:40px"><div class="kicker">Top sellers</div>{prod([("p-salomon-qst","Salomon QST","All-mountain freeride"),("p-nordica-unleashed","Nordica Unleashed","Freestyle, all-mountain"),("p-atomic-maverick","Atomic Maverick","All-mountain"),("p-elan-ripstick","Elan Ripstick","Lightweight all-mountain")])}<p class="note">Also on the wall: the Atomic Bent freeride line.</p></div></div></section>')
    b += (f'<section class="ice"><div class="wrap split rev"><div>{ph("lincoln-boot-wall.jpg","The boot wall at the Lincoln store","r43","Boot wall")}</div><div><div class="kicker">Boots</div><h2 class="display" style="font-size:30px">Boots, fitted by the Boot Lab</h2>'
          f'<p style="margin-top:14px">Eleven boot brands, from Lange, Atomic and Nordica race boots to the Atomic Hawx and Salomon hybrid lines. Masterfit and Sidas certified boot fitters are on staff every day, and buying boots here includes the fitting behind them.</p>'
          f'<div style="margin:18px 0">{brands(BOOT_BRANDS)}</div><div class="kicker">Bindings</div>{brands(BINDING_BRANDS)}<div style="margin-top:22px"><a class="btn" href="boot-lab.html#book">Book a boot fit</a></div></div></div>'
          f'<div class="wrap" style="margin-top:40px"><div class="kicker">Top-selling boots</div>{prod([("p-atomic-hawx","Atomic Hawx","All-mountain"),("p-nordica-unlimited","Nordica Unlimited","All-mountain"),("p-nordica-machine","Nordica Machine","Resort"),("p-atomic-hawx-xtd","Atomic Hawx XTD","Hybrid"),("p-salomon-spro","Salomon S/Pro","Resort"),("p-salomon-shift","Salomon Shift","Hybrid"),("p-rossignol-boot","Rossignol Hero World Cup","All-mountain")])}</div></section>')
    b += (f'<section><div class="wrap split"><div>{ph("lincoln-race-wall.jpg","Race skis on the Lincoln wall","r43","Race corner")}</div><div><div class="kicker">Race corner</div><h2 class="display" style="font-size:30px">Seven race brands, all in one spot</h2>'
          f'<p style="margin-top:14px">Atomic, Van Deer, Head, Rossignol, Fischer, Dynastar and Salomon race skis, with FIS and USSA boot prep, canting, stance and alignment in the Boot Lab. Whether you&rsquo;re gate training or chasing PRs, we have the setup to match your program.</p>'
          f'<div style="margin-top:22px"><a class="btn" href="race.html">Race at Rodgers</a></div></div></div></section>')
    b += (f'<section class="ice"><div class="wrap"><div class="grid g2">{pick_card(STAFF_PICKS[0])}{pick_card(STAFF_PICKS[2])}</div></div></section>')
    b += (f'<section><div class="wrap" style="max-width:820px">{sechead("Questions we hear")}' + faq([
          ("Do you mount bindings?","Yes. Mount and test is $75, free with the purchase of a ski and binding; adjustment and test is $40. Mounting is not included with race skis."),
          ("Do you carry race skis?","Yes: Atomic, Van Deer, Head, Rossignol, Fischer, Dynastar and Salomon. Race prep and boot work run through the Boot Lab."),
          ("Can I rent before I buy?","Yes. Demo skis (pro) rent from $60 a day at the Lincoln store, and we&rsquo;ll talk you through what you liked afterward.")]) + '</div></section>')
    return dept("lincoln-nh-ski.html","lincoln",LINCOLN,("Lincoln, NH","lincoln-nh.html"),"Ski","Skis, boots and bindings from twelve brands, staffed by people who ski Loon and Cannon weekly, with the Boot Lab down the hall.","atomic-ski-display","center",b,
                "Skis, boots and bindings at Rodgers Ski & Sport in Lincoln, NH: Atomic, Salomon, Nordica, Elan, Blizzard, Rossignol, Fischer, Völkl, Dynastar, Armada, Kästle, Head and Van Deer.")

def lin_snowboard():
    b = (f'<section><div class="wrap split"><div><div class="kicker">The Mothership</div><h2 class="display" style="font-size:30px">Riding east since &rsquo;88</h2>'
         f'<p style="margin-top:14px">Rodgers brought the &ldquo;snowboarding fad&rdquo; to the East in 1988 and opened the Mothership Snowboard Shop in 1996, focused on small, American-made brands. It lives inside the Lincoln store, with its own wall of boards, boots and bindings. Snowboards are a Lincoln-only department; the Scarborough store does not carry them.</p>'
         f'<h3 style="font-size:18px;margin:22px 0 10px">Boards</h3>{brands(SNOWBOARD_BRANDS)}<h3 style="font-size:18px;margin:18px 0 10px">Boots</h3>{brands(SB_BOOT_BRANDS)}<h3 style="font-size:18px;margin:18px 0 10px">Bindings</h3>{brands(SB_BINDING_BRANDS)}</div>'
         f'<div>{ph("mothership-snowboard-wall.jpg","Snowboards on the Mothership wall","r43","Mothership")}</div></div></div></section>')
    b += (f'<section class="ice"><div class="wrap"><div class="grid g2">{ph("snowboard-boot-wall.jpg","Snowboard boots from ThirtyTwo, Salomon, Deeluxe and Nidecker","r32","Boots")}{ph("mothership-counter.jpg","The Mothership counter","r32","The counter")}</div>'
          f'<div style="margin-top:34px"><div class="kicker">On the wall</div>{prod([("p-lib-tech","Lib Tech",""),("p-never-summer","Never Summer",""),("p-nidecker","Nidecker",""),("p-deeluxe","Deeluxe","Boots"),("p-32-boot","ThirtyTwo","Boots"),("p-salomon-sb-boot","Salomon","Boots"),("p-rome-binding","Rome","Bindings"),("p-nidecker-binding","Nidecker","Bindings")])}</div>'
          f'<p style="margin-top:22px">Board tunes and mounting run through the same tune room as skis: basic board tune, stone grind, P-tex and base welds. See the <a href="lincoln-nh-services.html" style="color:var(--navy);font-weight:700">Lincoln service menu</a>. Snowboard rental packages are $45 a day at the Lincoln store.</p></div></section>')
    return dept("lincoln-nh-snowboard.html","lincoln",LINCOLN,("Lincoln, NH","lincoln-nh.html"),"Snowboard","The Mothership Snowboard Shop inside the Lincoln store: boards, boots and bindings from nine brands, plus tunes and rentals.","snowboarder-powder-turn","center 45%",b,
                "The Mothership Snowboard Shop at Rodgers Ski & Sport, Lincoln, NH: boards, boots and bindings from Yes, Never Summer, Lib Tech, GNU, Rome, Bataleon, Nidecker, ThirtyTwo and Arbor.")

def lin_bikes():
    rows = [(f'{n}<small>{d}</small>', p) for n,p,d in LIN_BIKE]
    b = (f'<section><div class="wrap split"><div><div class="kicker">Lincoln bike shop</div><h2 class="display" style="font-size:30px">Bikes, accessories, performance</h2>'
         f'<p style="margin-top:14px">Mountain bikes for Loon&rsquo;s bike park and the Franconia Notch trails, cruisers, road, hybrids and e-bikes, and kids&rsquo; bikes. E-bikes are a summer staple here: Electra Townie Go! setups with throttle, full light kits and integrated blinkers have been rolling out the door all season.</p>'
         f'<p style="margin-top:10px">Bike tune-ups run all spring and summer, no appointment needed, with quick turnarounds and reasonable rates.</p></div>'
         f'<div>{ph("hero-mtb-jump.jpg","A mountain biker jumping on a forest trail","r43")}</div></div>'
         f'<div style="margin-top:40px"><div class="kicker">Brands and bikes</div>{brands(BIKE_BRANDS)}<div style="margin-top:16px">{prod([("bike-jamis-dakar","Jamis Dakar","Mountain"),("bike-jamis-hybrid","Jamis hybrid","Hybrid"),("p-scott-road","Scott","Road"),("bike-cruiser-beach","Electra cruiser","Cruiser"),("bike-trek-kids","Trek kids&rsquo; bike","Kids")])}</div></div></div></section>')
    b += (f'<section class="ice"><div class="wrap split rev"><div>{ph("lincoln-bike-service.jpg","A road bike in the repair stand","r43")}</div><div>{sechead("Bike services")}{pricelist(rows)}</div></div></section>')
    return dept("lincoln-nh-bikes.html","lincoln",LINCOLN,("Lincoln, NH","lincoln-nh.html"),"Bikes","Mountain, cruisers, road, hybrids and e-bikes, kids&rsquo; bikes, and a service bench that runs all summer.","mountain-biker-forest-trail","center",b,
                "The Lincoln, NH bike shop at Rodgers Ski & Sport: mountain, road, hybrid, e-bikes and kids' bikes, with bike tunes from $50.")

def lin_services():
    b = (f'<section><div class="wrap"><p style="max-width:720px;margin-bottom:34px">Five tune levels from a $40 clean-up to the $99 Full Monty, binding work priced by the job, and a race department with its own menu. Every tune is done by hand on the Montana machines you can see from the service desk. Not sure what you need? Ask your ski tech which tune is right for you.</p><div class="grid g2"><div>{sechead("Ski &amp; board tuning")}{pricelist(LIN_TUNES, note="For core shots and other repairs, ask for a quote. P-tex by the linear inch. A la carte services and add-ons available.")}</div>'
         f'<div>{sechead("Binding mounting &amp; servicing")}<p class="note" style="margin:-16px 0 14px">Every mount, adjustment and test checks compatibility and forward pressure, sets DIN, and is tested on the Montana Jetbond 2.</p>{pricelist(LIN_MOUNT_REC)}<div style="margin-top:18px"><div class="kicker">Race</div>{pricelist(LIN_MOUNT_RACE)}</div></div></div></div></section>')
    b += (f'<section class="ice"><div class="wrap split"><div>{ph("lincoln-tune-room-machines.jpg","The tuning machines and race ski rack in the Lincoln tune room","r43","Tune room")}</div>'
          f'<div><div class="kicker">The tune room</div><h2 class="display" style="font-size:30px">Montana machines, race-room standards</h2><p style="margin-top:14px">Every tune is done by hand on the machines you can see from the service desk. Race day tunes get their own line on the menu, and post-season race prep is a specialty: quick turnarounds so you are ready for race day.</p>'
          f'<p style="margin-top:10px">Turnaround depends on the season. Holiday weeks run longer, and we say so at drop-off.</p></div></div></section>')
    b += (f'<section><div class="wrap split rev"><div>{ph("boot-lab-bench.jpg","Race boots on the Boot Lab bench","r43","Boot Lab")}</div><div>{sechead("Race department")}{pricelist(RACE_SKI[1:], cols=("Service","Rodgers ski","Outside ski"))}<p class="note">Full race ski, boot and binding menus, including the Podium Club season tuning, are on the <a href="race.html" style="color:var(--navy);font-weight:700">Race page</a>. Boot Lab menu on the <a href="boot-lab.html" style="color:var(--navy);font-weight:700">Boot Lab page</a>.</p></div></div></section>')
    b += (f'<section class="ice"><div class="wrap" style="max-width:820px">{sechead("Drop-off questions")}' + faq([
          ("How long does a tune take?","It depends on the season. We state current turnaround at drop-off. Holiday weeks run longer, and day-of race tunes need an appointment."),
          ("Do you tune snowboards?","Yes. Board tunes run through the same tune room. Ask at the desk for the board rate."),
          ("Do you service bikes?","Yes, all summer. Bronze, Silver and Gold bike tunes are on the <a href=\"lincoln-nh-bikes.html\">Bikes page</a>.")]) + '</div></section>')
    return dept("lincoln-nh-services.html","lincoln",LINCOLN,("Lincoln, NH","lincoln-nh.html"),"Services &amp; Tuning","Tunes from $40 to the Full Monty, binding mounting, race prep and the Boot Lab menu, with prices in the open.","atomic-blanchard-5590.jpg","center 22%",b,
                "Ski and snowboard tuning, binding mounting and Boot Lab services at Rodgers Ski & Sport in Lincoln, NH, with prices.")

def lin_accessories(store=LINCOLN, fname="lincoln-nh-accessories.html", active="lincoln", crumb=("Lincoln, NH","lincoln-nh.html")):
    sets = [("Helmets &amp; goggles",HELMET_GOGGLE,"goggle-display.jpg","The goggle display"),("Gloves &amp; mittens",GLOVES,"accessories-flatlay.jpg","Gloves, goggles, beanie and socks"),
            ("Heated accessories",HEATED,"smith-goggle-case.jpg","Smith goggle display"),("Hats &amp; neckwear",HATS,"giro-helmet-wall.jpg","Giro helmets on the wall"),("Bags &amp; backpacks",BAGS,"atomic-bag-wall.jpg","Atomic bags on the wall")]
    cards = ''
    for t,bl,img,alt in sets:
        cards += f'<div class="card">{(ph(img,alt,"r32")+"<div style=height:16px></div>") if img else ""}<h3>{t}</h3><div style="margin-top:12px">{brands(bl)}</div></div>'
    intro = ("Forgot something on the way up? We&rsquo;re the first exit." if store is LINCOLN else "Stocked for Maine winters, minutes off I-95.")
    b = (f'<section><div class="wrap">{sechead("Accessories", intro)}<div class="grid g3">{cards}</div>'
         f'<div style="margin-top:40px"><div class="kicker">On the shelf</div>{prod([("p-atomic-helmet","Atomic helmet",""),("p-giro","Giro helmet",""),("p-atomic-goggles","Atomic goggles",""),("p-hestra","Hestra gloves",""),("p-swany","Swany gloves",""),("p-hotronics","Hotronic heated socks",""),("p-lenz","Lenz heated socks",""),("p-eisbar","Eisb&auml;r hat",""),("p-turtle-fur","Turtle Fur",""),("p-blackstrap","Blackstrap",""),("p-athalon","Athalon boot bag",""),("p-mammut","Mammut pack","")])}</div></div></section>')
    return dept(fname,active,store,crumb,"Accessories","Helmets, goggles, gloves and mittens, heated accessories, hats and neckwear, bags and backpacks.","ski-poles-display","center",b,
                f"Ski accessories at Rodgers Ski & Sport, {store['name']}: helmets and goggles from Smith, Giro, POC and Oakley, gloves from Hestra and Swany, heated gear, hats and bags.")

def lin_apparel():
    b = (f'<section><div class="wrap split"><div>{ph("lincoln-apparel-floor.jpg","The apparel floor at the Lincoln store","r43","Apparel floor")}</div><div><div class="kicker">Outerwear</div><h2 class="display" style="font-size:30px">Jackets and pants for East Coast conditions</h2>'
         f'<p style="margin-top:14px">Men&rsquo;s, women&rsquo;s and kids&rsquo; outerwear from race-team shells to town jackets, plus layers and sweaters.</p>'
         f'<h3 style="font-size:17px;margin:18px 0 8px">Men</h3>{brands(MENS_OUTERWEAR)}<h3 style="font-size:17px;margin:18px 0 8px">Women</h3>{brands(WOMENS_OUTERWEAR)}<h3 style="font-size:17px;margin:18px 0 8px">Kids</h3>{brands(KIDS_OUTERWEAR)}</div></div></div></section>')
    b += (f'<section class="ice"><div class="wrap"><div class="grid g2"><div class="card"><h3>Layers</h3><p>Fleeces, base layers and insulators.</p><div style="margin-top:12px">{brands(LAYERS)}</div></div><div class="card"><h3>Sweaters &amp; lifestyle</h3><p>Wool for the lodge and the drive home.</p><div style="margin-top:12px">{brands(SWEATERS)}</div></div></div>'
          f'<div style="margin-top:34px"><div class="kicker">On the floor</div>{prod([("p-arcteryx","Arc&rsquo;teryx shell",""),("p-helly-hansen","Helly Hansen jacket",""),("p-snowpants","Bib pants",""),("p-dale","Dale of Norway",""),("p-sweater","Ski sweater",""),("p-hot-chillys","Hot Chillys base layer",""),("p-uyn","UYN base layer","")])}</div></div></section>')
    return dept("lincoln-nh-apparel.html","lincoln",LINCOLN,("Lincoln, NH","lincoln-nh.html"),"Apparel","Men&rsquo;s, women&rsquo;s and kids&rsquo; outerwear, layers and sweaters at the Lincoln store.","snowboarder-mountain-portrait","center 40%",b,
                "Ski apparel at Rodgers Ski & Sport in Lincoln, NH: outerwear from Arc'teryx, Norrøna, Helly Hansen, Bogner, Kjus, Descente and more; layers from Smartwool and Kari Traa.")

def rentals():
    rows = [tuple(r) for r in LIN_RENTALS]
    form = ('<section class="ice tight"><div class="wrap"><div class="card" style="display:flex;gap:24px;align-items:center;flex-wrap:wrap"><div style="flex:2;min-width:280px"><h3>Reserve ahead or walk in</h3>'
            '<p>Send a reservation request with your dates, package and sizes and the Lincoln rental counter stages the gear before you arrive. Walk-ins are welcome every day the store is open.</p></div>'
            f'<a class="btn accent" href="reserve-rental.html">Reserve a rental</a><a class="btn ghost" href="tel:{LINCOLN["teltag"]}">Call {LINCOLN["tel"]}</a></div></div></section>')
    h = hero("Rentals in Lincoln", "Junior packages from $20 a day, performance and advanced skis, demos, snowboards, snowshoes, cross-country and helmets. Rentals are a Lincoln, NH program; the Scarborough store does not rent equipment.",
             "snowboarder-green-purple", kicker="Lincoln, NH &middot; Rentals", short=True, pos="center 45%")
    h += crumbs(("Lincoln, NH","lincoln-nh.html"),("Rentals",""))
    h += form
    h += (f'<section><div class="wrap">{sechead("Rental rates", "Rates are valid with consecutive daily use. Damage waiver available at $2 a day.")}{pricelist(rows, cols=("Package","1 day","2 days","3 days","4 days","5 days"))}</div></section>')
    h += (f'<section class="ice"><div class="wrap split"><div>{ph("hero-lincoln-family.jpg","A family on skis at the base of Loon","r43")}</div><div><div class="kicker">Why rent here</div><h2 class="display" style="font-size:30px">Skip the line at the base</h2>'
          f'<p style="margin-top:14px">Lincoln is the first shop off I-93 and minutes from Loon. Rent here on the way up and you walk past the base-lodge rental counter. Bring your own boots if you have them; the package price stays the same.</p>'
          f'<p style="margin-top:10px">Looking for the season-long option for kids? That&rsquo;s the <a href="lease.html" style="color:var(--navy);font-weight:700">Junior Seasonal Lease</a> at our Scarborough, Maine store.</p></div></div></section>')
    h += (f'<section><div class="wrap" style="max-width:820px">{sechead("Rental questions")}' + faq([
          ("What&rsquo;s included in a package?","Skis or board, boots and poles. Helmets rent separately at $10 a day."),
          ("How does sizing work?","Height, weight, shoe size and skier type. The counter sets bindings and tests them before you leave."),
          ("What is the damage waiver?","$2 a day; it covers normal rental damage."),
          ("Do multi-day rates require consecutive days?","Yes. Rates are only valid with consecutive daily use."),
          ("Can I reserve online?","Yes. Send a reservation request with your dates, packages and sizes and the counter confirms by email or phone and stages the gear before you arrive. Nothing is charged online.")]) + '</div></section>')
    return page("lincoln","Rentals &middot; Lincoln, NH | Rodgers Ski &amp; Sport","Ski, snowboard, snowshoe and cross-country rentals at Rodgers Ski & Sport in Lincoln, NH. Junior packages from $20 a day. First shop off I-93 before Loon.", h, "rentals.html")

# ---------------- Scarborough departments ----------------
def sca_ski():
    b = (f'<section><div class="wrap split"><div>{ph("scarborough-atomic-ski-wall.jpg","The ski wall under the lit Atomic and Salomon signs","r43","Scarborough")}</div><div>{sechead("Skis, boots and bindings")}'
         f'<p>Alpine skis for Maine day-trips and weekends in the Whites, from all-mountain to race. Top sellers include the Salomon QST, Nordica Unleashed, Atomic Maverick, Elan Ripstick and Atomic Bent. Boots from Atomic, Nordica, Salomon, Dalbello, Tecnica and Lange, fitted at the bench in the back.</p>'
         f'<p style="margin-top:10px">Scarborough is a ski store: no snowboards and no rentals here. For growing kids there is the <a href="lease.html" style="color:var(--navy);font-weight:700">Junior Seasonal Lease</a>.</p><div style="margin-top:16px">{brands(SKI_BRANDS)}</div></div></div></section>')
    b += (f'<section class="ice"><div class="wrap"><div class="grid g3">{ph("scarborough-ski-rows-alt.jpg","Atomic and Völkl skis on the Scarborough wall","r43")}{ph("scarborough-race-wall.jpg","Race skis under the Atomic sign","r43")}{ph("salomon-lit-sign.jpg","The Salomon sign on the wood wall","r43")}</div>'
          f'<div class="split" style="margin-top:34px"><div><div class="kicker">Race</div><h3 style="font-size:20px">Race skis and race tunes in Maine</h3><p style="margin-top:8px">Race skis under the Atomic sign, a $100 race tune on the menu, and boot work for race boots: shell and liner molding, punches and spot grinds. Full FIS and USSA boot prep is done at the Lincoln Boot Lab.</p></div>'
          f'<div><div class="kicker">Bindings</div>{brands(BINDING_BRANDS)}<div style="margin-top:16px"><a class="btn" href="race.html">Race at Rodgers</a> <a class="btn ghost" href="scarborough-me-services.html">Service menu</a></div></div></div></div></section>')
    return dept("scarborough-me-ski.html","scarb",SCARB,("Scarborough, ME","scarborough-me.html"),"Ski","Skis, boots and bindings for Southern Maine skiers heading to Sunday River, Sugarloaf, Pleasant Mountain and the Whites.","skier-carving-red-jacket","center 40%",b,
                "Skis, boots and bindings at Rodgers Ski & Sport in Scarborough, ME: Atomic, Salomon, Nordica, Elan, Blizzard, Rossignol, Fischer, Völkl and more.")

def sca_bikes():
    rows = [(f'{n}<small>{d}</small>', p) for n,p,d in SCA_BIKE]
    b = (f'<section><div class="wrap split"><div><div class="kicker">Scarborough bike shop</div><h2 class="display" style="font-size:30px">Bikes, accessories, services</h2>'
         f'<p style="margin-top:14px">Mountain, cruisers, gravel, hybrids and e-bikes, and kids&rsquo; bikes. Trek arrived in Scarborough in 2024. The shop runs social no-drop group rides on the railroad-track trails off Highland Avenue: flat terrain, all ages and skill levels welcome.</p>'
         f'<p style="margin-top:10px">Bike tune-ups from spring on, no appointment needed, with quick turnarounds and reasonable rates.</p><div style="margin-top:14px">{brands(BIKE_BRANDS)}</div></div><div>{ph("bike-maine-storefront.jpg","An Electra cruiser outside the Scarborough store","r43","Scarborough")}</div></div></div></section>')
    b += (f'<section class="ice"><div class="wrap" style="max-width:820px">{sechead("Bike services")}{pricelist(rows, note="We provide professional assembly for bikes purchased elsewhere or shipped to our location.")}</div></section>')
    return dept("scarborough-me-bikes.html","scarb",SCARB,("Scarborough, ME","scarborough-me.html"),"Bikes","Mountain, cruisers, gravel, hybrids and e-bikes, kids&rsquo; bikes, service and custom builds.","mountain-bike-forest-jump","center",b,
                "The Scarborough, ME bike shop at Rodgers Ski & Sport: mountain, gravel, cruiser, hybrid and e-bikes, safety checks from $50, builds and group rides.")

def sca_services():
    b = (f'<section><div class="wrap"><div class="grid g2"><div>{sechead("Ski &amp; board tuning")}{pricelist(SCA_TUNES)}</div><div>{sechead("Mount &amp; test")}{pricelist(SCA_MOUNT)}<div style="margin-top:30px">{sechead("Boot work")}{pricelist(SCA_BOOTLAB, note="Full FIS and USSA race boot prep is done at the Lincoln Boot Lab.")}</div></div></div></div></section>')
    b += (f'<section class="ice"><div class="wrap split"><div>{ph("scarborough-atomic-boot-bench.jpg","A race boot on the bench under the Atomic sign","r43","Mount &amp; test")}</div><div><div class="kicker">Binding mounting and testing</div><h2 class="display" style="font-size:30px">Mounted, adjusted, tested</h2>'
          f'<p style="margin-top:14px">Every pair is checked before it leaves our hands. Mounting is free with the purchase of two of the three (ski, boot, binding) and half price with one of the three.</p></div></div></section>')
    return dept("scarborough-me-services.html","scarb",SCARB,("Scarborough, ME","scarborough-me.html"),"Services &amp; Tuning","Ski and board tunes, stone grinding, race tunes, mounting and boot work at the Maine store, with prices in the open.","snowy-ski-trail","center",b,
                "Ski and snowboard tuning, stone grinding, race tunes, binding mounting and boot work at Rodgers Ski & Sport in Scarborough, ME, with prices.")

def sca_accessories():
    return lin_accessories(SCARB, "scarborough-me-accessories.html", "scarb", ("Scarborough, ME","scarborough-me.html"))

def lease():
    h = hero("Junior Seasonal Lease", "Skis, bindings and boots for the whole season at the Scarborough, Maine store. $159. Pick-ups begin October 1, no appointment needed.",
             "skiers-snowy-mountain", kicker="Scarborough, ME &middot; Families", short=True, pos="center 55%")
    h += crumbs(("Scarborough, ME","scarborough-me.html"),("Junior Seasonal Lease",""))
    h += (f'<section><div class="wrap"><div class="grid g3"><div class="card"><div class="tick">$</div><h3>Cost</h3><p><b style="font-size:28px;color:var(--navy)">{LEASE["price"]}</b><br>for the season. Includes {LEASE["includes"].lower()}.</p></div>'
          f'<div class="card"><div class="tick">1</div><h3>Pick-up</h3><p>{LEASE["pickup"]}</p></div><div class="card"><div class="tick">2</div><h3>Return</h3><p>{LEASE["end"]}</p></div></div>'
          f'<div class="split" style="margin-top:44px"><div>{ph("scarborough-ski-rows.jpg","Skis on the Scarborough wall","r43")}</div><div><div class="kicker">Who it fits</div><h2 class="display" style="font-size:28px">Kids grow. Leases fit.</h2><p style="margin-top:14px">{LEASE["fit"]}</p>'
          f'<p style="margin-top:10px">The lease is a Scarborough program. The Lincoln, NH store sells junior packages and rents by the day instead.</p><div style="margin-top:20px"><a class="btn accent" href="mailto:{SCARB["email"]}">Inquire by email</a> <a class="btn ghost" href="tel:{SCARB["teltag"]}">Call {SCARB["tel"]}</a></div></div></div></div></section>')
    h += (f'<section class="ice"><div class="wrap" style="max-width:820px">{sechead("Lease questions")}' + faq([
          ("Do I need an appointment?","No. Walk in from October 1 and one of our staff will get your skier outfitted."),
          ("What if we&rsquo;re still skiing in May?","Call and let us know so you avoid late fees. Drop-offs after the month of May are subject to a $159 charge."),
          ("Can I reserve the lease online?","Not this season. Online lease sign-up is planned for next year; for now, email or call the Scarborough store.")]) + '</div></section>')
    return page("scarb","Junior Seasonal Lease &middot; Scarborough, ME | Rodgers Ski &amp; Sport","Junior seasonal ski lease at Rodgers Ski & Sport in Scarborough, ME: skis, bindings and boots for $159, ages 2 to 13, pick-ups from October 1.", h, "lease.html")

# =====================================================================================
def boot_lab():
    h = hero("The Boot Lab", "Custom fitting and race prep from Masterfit and Sidas certified fitters. Full fitting and FIS and USSA prep in Lincoln; heat molding, punches and grinds at both stores.",
             "rossignol-hero-2.jpg", kicker="Lincoln, NH &amp; Scarborough, ME", short=True, pos="center 40%", credit="Photo: Rossignol",
             ctas='<a class="btn accent" href="#book">Book a fitting</a><a class="btn ghost-d" href="#menu">Service menu</a>')
    h += crumbs(("The Boot Lab",""))
    steps = [("Assess","Feet, stance, and how you actually ski."),("Select","Shell fit first, from Atomic, Nordica, Salomon, Dalbello, Fischer, Head, Tecnica and Lange."),("Build","Footbeds, heat molding, punches, canting, lifters."),("Prove","Ski it. Come back and we adjust until it&rsquo;s right.")]
    h += (f'<section><div class="wrap">{sechead("Why fit is everything", "A boot that fits is the difference between a good day and a great one. Here is how a fitting runs.")}<div class="grid g4">' +
          ''.join(f'<div class="card"><div class="tick">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(steps)) + '</div></div></section>')
    h += (f'<section class="ice" id="menu"><div class="wrap"><div class="grid g2"><div>{sechead("Lincoln Boot Lab")}{pricelist(LIN_BOOTLAB, note="Race boot purchase does not include service.")}</div><div>{sechead("Scarborough boot work")}{pricelist(SCA_BOOTLAB, note="Full FIS and USSA race boot prep is done in Lincoln.")}'
          f'<div style="margin-top:26px">{ph("boot-lab-red.jpg","Red race boots on the Boot Lab bench","r32","Lincoln Boot Lab")}</div></div></div>'
          f'<div style="margin-top:40px">{sechead("Race boot service", "Prices for boots bought at Rodgers, and for boots bought elsewhere.")}{pricelist(RACE_BOOT, cols=("Service","Rodgers boot","Outside boot"))}</div></div></section>')
    h += (f'<section><div class="wrap split"><div>{ph("staffpick-denis-atomic-redster-130.jpg","Denis holding the Atomic Redster 130 race boot outside the Lincoln store","r34")}</div><div><div class="kicker">Race corner</div><h2 class="display" style="font-size:30px">Race boots, fitted by people who race</h2>'
          f'<p style="margin-top:14px">FIS boot prep, USSA boot prep, canting, stance and alignment and lifters, on race boots from every brand we carry. Denis&rsquo;s pick this fall: the Atomic Redster 130 World Cup. &ldquo;A race-focused shell and narrow World Cup fit that delivers exceptional power, precision, and edge control for aggressive skiing.&rdquo;</p>'
          f'<div style="margin-top:20px"><a class="btn" href="race.html">Race at Rodgers</a></div></div></div></section>')
    h += (f'<section class="ice" id="book"><div class="wrap"><div class="grid g2"><div><div class="kicker">Book a fitting</div><h2 class="display" style="font-size:30px">Appointments recommended</h2><p style="margin-top:14px">Plan on 60 to 90 minutes for a full fit; race builds run longer. Appointments are required for custom race work. Bring your current boots, footbeds if you have them, and the socks you ski in.</p>'
          f'<p style="margin-top:14px"><a class="btn accent" href="tel:{LINCOLN["teltag"]}">Lincoln {LINCOLN["tel"]}</a> <a class="btn ghost" href="tel:{SCARB["teltag"]}">Scarborough {SCARB["tel"]}</a></p></div>'
          f'<div class="card"><h3>Request a fitting</h3><form style="margin-top:14px"><label class="f">Store</label><select class="field"><option>Lincoln, NH</option><option>Scarborough, ME</option></select><label class="f">Name</label><input class="field"><label class="f">Phone or email</label><input class="field"><label class="f">What are we working on?</label><select class="field"><option>New boots</option><option>Fit problem with current boots</option><option>Race prep (FIS / USSA)</option><option>Custom insoles</option></select><button class="btn" type="button">Send request</button></form></div></div></div></section>')
    h += (f'<section><div class="wrap" style="max-width:820px">{sechead("Before you book")}' + faq([
          ("How long does a fitting take?","Plan on 60 to 90 minutes for a full fit; race builds run longer."),
          ("What should I bring?","Your current boots, footbeds if you have them, and the socks you actually ski in."),
          ("Do race boots include service?","No. Race boot purchase does not include service; the race-prep menu above covers the work. Outside boots add $100 to FIS or USSA prep."),
          ("Which store for what?","Lincoln: full fitting, custom insoles, canting, stance and alignment, FIS and USSA prep. Scarborough: shell and liner heat molding, punches, spot grinds and heel lifts.")]) + '</div></section>')
    return page("boot","The Boot Lab | Rodgers Ski &amp; Sport","Custom boot fitting and race boot prep at Rodgers Ski & Sport: Masterfit and Sidas certified fitters, custom insoles, canting, FIS and USSA prep in Lincoln, NH; heat molding and punches in Scarborough, ME.", h, "boot-lab.html")

def race():
    h = hero("Race at Rodgers", "Seven race brands under one roof: Atomic, Van Deer, Head, Rossignol, Fischer, Dynastar and Salomon. Race skis, boots, bindings and full FIS and USSA prep, whether you&rsquo;re gate training or chasing PRs.",
             "atomic-mika-blanchard-9944.jpg", kicker="Race skis &middot; boots &middot; prep", short=False, pos="65% 12%", credit="Photo: Atomic",
             ctas='<a class="btn accent" href="boot-lab.html#book">Book race boot prep</a><a class="btn ghost-d" href="lincoln-nh-services.html">Race day tunes</a>')
    h += crumbs(("Race",""))
    h += (f'<section><div class="wrap">{sechead("The race wall", "Every race brand we carry, in one spot at the Lincoln store, with race skis and race tunes in Scarborough too.")}'
          f'<div class="split"><div>{ph("lincoln-race-wall.jpg","Fischer, Rossignol, Head and Dynastar race skis on the Lincoln wall","r43","Lincoln race wall")}</div>'
          f'<div>{brands(RACE_BRANDS)}<p style="margin-top:18px">Slalom, GS, speed and junior race skis from all seven brands, with race bindings and plates. Salomon&rsquo;s race line returned to the U.S. market in 2026 and Rodgers is, in the shop&rsquo;s words, the only East Coast dealer. Van Deer, the Red Bull ski brand, is on the wall in Lincoln.</p>'
          f'<div style="margin-top:14px"><div class="kicker">Race boots</div>{brands(RACE_BOOT_BRANDS)}</div><div style="margin-top:14px"><div class="kicker">Race bindings</div>{brands(RACE_BINDING_BRANDS)}</div><div style="margin-top:14px"><div class="kicker">Race poles</div>{brands(RACE_POLE_BRANDS)}</div></div></div></div></section>')
    h += (f'<section class="ice"><div class="wrap"><p style="max-width:720px;margin-bottom:34px">The race department in Lincoln preps skis on a Montana Crystal Rock robot that makes the ski flat before applying a race-specific structure used by World Cup athletes, and waxes with the Wax Future for base saturation without the heat of a hot box. Two prices on every line: one for gear bought at Rodgers, one for gear bought elsewhere.</p>'
          f'<div class="grid g2"><div>{sechead("Race ski service")}{pricelist(RACE_SKI, cols=("Service","Rodgers ski","Outside ski"))}</div><div>{sechead("Race binding service")}{pricelist(RACE_BINDING, cols=("Service","Rodgers","Outside"))}<div style="margin-top:26px">{sechead("Scarborough")}{pricelist([("Race tune","$100"),("Shell heat mold","$50"),("Liner heat mold","$40"),("Punch out","$25 each"),("Spot grind","$15 each")], note="Full FIS and USSA prep is done in Lincoln.")}</div></div></div>'
          f'<p class="note" style="margin-top:18px">Race boot service, from the FIS setup to lifters and heaters, is on the <a href="boot-lab.html#menu" style="color:var(--navy);font-weight:700">Boot Lab page</a>. Race boot purchase does not include service. Mounting is not included with race skis.</p></div></section>')
    h += (f'<section><div class="wrap">{sechead("Race staff picks", "", ("All staff picks","staff-picks.html"))}<div class="grid g2">{pick_card(STAFF_PICKS[1])}{pick_card(STAFF_PICKS[2])}</div></div></section>')
    h += (f'<section class="ice"><div class="wrap"><div class="grid g3">{ph("fischer-noize-stage.jpg","A racer in the start gate on Fischer RC4 Noize skis","r32","Fischer")}{ph("rossignol-hero-2.jpg","A racer on Rossignol Hero skis","r32","Rossignol")}{ph("atomic-24A1498.jpg","Two skiers on Atomic race skis","r32","Atomic")}</div>'
          f'<p class="note">Brand imagery courtesy of Atomic, Fischer and Rossignol.</p></div></section>')
    h += (f'<section><div class="wrap split"><div><div class="kicker">Teams, clubs and schools</div><h2 class="display" style="font-size:30px">Coaches, parents, athletes</h2><p style="margin-top:14px">Whether you&rsquo;re an athlete, coach, parent or recreational skier, we have the equipment and the knowledge you need to enjoy your day and perform your best. Race teams, ski clubs and school programs: talk to the Lincoln store directly and we&rsquo;ll set gear and bench time aside.</p>'
          f'<div style="margin-top:20px"><a class="btn" href="partners.html">Partners &amp; teams</a> <a class="btn ghost" href="tel:{LINCOLN["teltag"]}">Call Lincoln</a></div></div><div>{ph("lincoln-race-wall-alt.jpg","Race boots and race skis on the Lincoln wall","r43")}</div></div></section>')
    return page("race","Race | Rodgers Ski &amp; Sport","Race skis, race boots, race tunes and FIS/USSA boot prep at Rodgers Ski & Sport: Atomic, Van Deer, Head, Rossignol, Fischer, Dynastar and Salomon, in Lincoln, NH and Scarborough, ME.", h, "race.html")

# =====================================================================================
def staff_picks():
    h = hero("Staff picks", "What our people are skiing this season, in their own words. Every pick is a Rodgers post from Instagram, quoted as written.",
             "snowboarder-orange-pants", kicker="From the shop floor", short=True, pos="center 40%")
    h += crumbs(("Journal","journal.html"),("Staff Picks",""))
    h += (f'<section><div class="wrap"><div class="grid g2">{"".join(pick_card(p) for p in STAFF_PICKS)}</div>'
          f'</div></section>')
    h += (f'<section class="ice"><div class="wrap">{sechead("Shop favorites from the reels", "Quick takes from the TikTok and Instagram reels this year.")}<div class="grid g3">'
          '<div class="card"><h3>Rossignol Forza 70</h3><p class="tagline">&ldquo;One of the shop favorites: carve like a mad man, manage ski&rsquo;d off chop like a mad man, and can handle the occasional bump run with ease.&rdquo;</p></div>'
          '<div class="card"><h3>Atomic Maverick 88</h3><p class="tagline">&ldquo;The perfect east coast ski?&rdquo;</p></div>'
          '<div class="card"><h3>Salomon S/Lab QST Blank</h3><p class="tagline">&ldquo;With a 112 waist these things charge in new snow but are powerful and responsive on crud and groomers. Wicked versatile!&rdquo;</p></div>'
          '<div class="card"><h3>Elan Playmaker 91</h3><p class="tagline">&ldquo;Hero laps and sunshine. Slashing moguls like nobody&rsquo;s business.&rdquo;</p></div>'
          '<div class="card"><h3>Blizzard Canvas 100</h3><p class="tagline">&ldquo;Team rider Devon calls the &rsquo;26/&rsquo;27 Blizzard Canvas 100 the ski of the day at Waterville demo day.&rdquo;</p></div>'
          '<div class="card"><h3>Booster straps</h3><p class="tagline">&ldquo;Booster Straps kill the dead zone at the start of your flex so your shin connects instantly with the boot instead of smashing into it later.&rdquo;</p></div>'
          '</div></div></section>')
    return page("journal","Staff Picks | Rodgers Ski &amp; Sport","Staff picks from Rodgers Ski & Sport: the skis and boots our staff are riding this season, in their own words.", h, "staff-picks.html")

def journal():
    h = hero("The journal", "News from both stores, sale dates, racing, new brands and gear, and what the local mountains are up to.",
             "snowboarder-mountain-view", kicker="Rodgers Ski &amp; Sport", short=True, pos="center 45%")
    h += crumbs(("Journal",""))
    p = POSTS[0]
    h += (f'<section><div class="wrap"><div class="chips">' + ''.join(f'<a href="#" class="{"on" if c=="All" else ""}">{c}</a>' for c in CATEGORIES) + '</div>'
          f'<div class="feature"><div class="ph"><img src="img/{p["img"]}" alt="{p["alt"]}"></div><div class="body"><span class="pill orange">{p["cat"]}</span><h2>{p["title"]}</h2><p>{p["teaser"]}</p><div class="date" style="font-size:12px;color:var(--steel);margin-top:10px">{p["date"]}</div><div style="margin-top:18px"><a class="btn" href="{p["slug"]}">Read the post</a></div></div></div>'
          f'<div class="grid g3" style="margin-top:22px">{"".join(post_card(x) for x in POSTS[1:])}</div>'
          f'</div></section>')
    return page("journal","Journal | Rodgers Ski &amp; Sport","News, promotions, racing, brands and local mountain updates from Rodgers Ski & Sport in Lincoln, NH and Scarborough, ME.", h, "journal.html")

def tent_sale_article():
    h = hero("The Fall Tent Sale is on", "September 18 to October 12, 2026, under the tent at 5 Railroad Street in Lincoln. Our biggest deals of the year on skis, snowboards, boots, apparel and helmets.",
             "riverside-autumn-aerial", kicker="Promotions &middot; September 18, 2026", short=True, pos="center 45%")
    h += crumbs(("Journal","journal.html"),("Fall Tent Sale",""))
    h += ('<section><div class="wrap article">'
          '<p>The Fall Tent Sale is the shop&rsquo;s annual tradition on Railroad Street, and this year&rsquo;s runs from Friday, September 18 through Monday, October 12 at the Lincoln, New Hampshire store, open every day 8:30 to 5. It is the biggest sale of the year: skis, snowboards, boots, bindings, apparel, helmets and accessories, with staff picks and deal reveals posted through the sale.</p>'
          '<h2>What&rsquo;s under the tent</h2><ul>' + ''.join(f'<li>{d}.</li>' for d in TENT_DEALS) + '<li>Robbie&rsquo;s pick, the Elan Ripstick 96 Black, at $699 including bindings.</li><li>Jamie&rsquo;s pick, the Atomic Arc 735 RS with the limited-edition 1990-91 Arc graphic.</li></ul>'
          '<h2>What else is on the floor</h2><p>The full 2027 Atomic lineup landed in late August: skis, bindings, boots and race skis. The new K&auml;stle Paragon 93 and the 2027 Smith goggle wall arrived in September. The race wall is stocked from all seven race brands: Atomic, Van Deer, Head, Rossignol, Fischer, Dynastar and Salomon.</p>'
          '<h2>Scarborough shoppers</h2><p>The fall sale is at the Lincoln store. Scarborough ran its own &ldquo;Tent-Less Tent Sale&rdquo; this summer, July 24 through August 9, with the same markdowns under an actual roof. Watch the journal and Instagram for the next Maine sale dates.</p>'
          '<h2>Before you come</h2><p>Bring your boots if you are shopping for skis, and your current skis if you want a tune while you are here. Boot fittings during the sale: appointments recommended, call the Lincoln store.</p>'
          f'<p style="margin-top:26px"><a class="btn accent" href="{LINCOLN["maps"]}">Directions to Lincoln</a> <a class="btn ghost" href="staff-picks.html">Staff picks</a></p></div></section>')
    h += (f'<section class="ice"><div class="wrap">{sechead("More from the journal")}<div class="grid g3">{"".join(post_card(x) for x in POSTS[1:4])}</div></div></section>')
    return page("journal","Fall Tent Sale 2026 | Rodgers Ski &amp; Sport","The Rodgers Ski & Sport Fall Tent Sale runs September 18 to October 12, 2026 at the Lincoln, NH store: skis, snowboards, boots, apparel and helmets at the year's lowest prices.", h, "journal-fall-tent-sale.html")

def black_ridge_article():
    h = hero("Loon&rsquo;s Black Ridge", "272 acres of expert-only glades east of North Peak, opening winter 2027-28. What Loon announced on September 1, and the gear that makes sense for it.",
             "skier-powder-gondola", kicker="Local mountains &middot; September 20, 2026", short=True, pos="center 40%")
    h += crumbs(("Journal","journal.html"),("Loon&rsquo;s Black Ridge",""))
    h += ('<section><div class="wrap article">'
          '<p>On September 1, Loon Mountain announced Black Ridge, a 272-acre expansion of in-bounds tree skiing on the east side of North Peak, inside the White Mountain National Forest. It opens for the 2027-28 season, with on-mountain work starting in early 2027. When it does, Loon goes from 403 skiable acres to 675, a 67 percent increase, and becomes the largest ski area in New Hampshire. Bretton Woods, the current leader, lists about 468.</p>'
          '<h2>What Loon is building</h2>'
          '<p>Loon has 35 acres of glades today; Black Ridge brings that to 307. The terrain is rated expert only: dense softwood, steep gullies and open hardwood glades, with a 1,350-foot vertical drop from a 2,850-foot high point. Tree cutting is being kept to a minimum, so there are a few loosely defined routes rather than trails.</p>'
          '<p>There is no lift inside Black Ridge. You ride the North Peak Express Quad, pass through a controlled entry gate at the top and traverse up to 1.25 miles east; Loon says hiking or pushing may be required. There is no snowmaking and no grooming, so the zone opens and closes on natural snow. Ski Patrol will cover it, with slower response times. Brian Norton, Loon&rsquo;s president and general manager, put it plainly: &ldquo;Black Ridge isn&rsquo;t for everyone, and that&rsquo;s the point.&rdquo;</p>'
          '<h2>The gear that fits this terrain</h2>'
          '<p><strong>Skis.</strong> For a New Hampshire skier who wants one pair for both the groomers and Black Ridge, a 95 to 105 mm waist with tip and tail rocker is the range to shop. Rocker floats in soft snow and releases the tail in tight trees. The Salomon QST 100, Elan Ripstick 96 Black Edition and Atomic Maverick 105 CTI are where we start; for a storm-day second pair, the Atomic Bent 110 or QST 106.</p>'
          '<p><strong>Boots.</strong> A 1.25-mile traverse is where a walk mode pays off. The Atomic Hawx Ultra XTD, Salomon Shift Alpha and Nordica Unlimited keep a 98 to 99 mm downhill fit and open up for the flats. Fit matters more than flex; the Boot Lab in Lincoln handles both.</p>'
          '<p><strong>Snowboards.</strong> A stiffer directional board with a setback stance floats best in untracked snow and holds a line through gullies. Never Summer, Lib Tech, Arbor and Nidecker are all on the wall.</p>'
          '<p><strong>Poles, head and hands.</strong> Powder baskets from Leki, Swix or Komperdell. A helmet is not optional in trees: Smith, Giro, POC and Sweet Protection, with a low-light goggle lens for the shade under softwoods. Hestra gloves with a long cuff keep snow out.</p>'
          '<p><strong>A small pack.</strong> Water, a spare layer and a strap for a lost ski. Db, Dakine and POC packs sized for a lift day are in both stores. Ski with a partner; the patrol response time is Loon&rsquo;s own warning.</p>'
          '<p><strong>Tuning.</strong> Natural snow over rock and stumps means base repair. The Lincoln tune room handles p-tex, edges and stone grinding all winter.</p>'
          '<p>Black Ridge is more than a year out. The gear above is in the stores now, and the tent sale in Lincoln runs through October 12.</p>'
          '<p style="margin-top:26px"><a class="btn" href="https://www.loonmtn.com/black-ridge" target="_blank" rel="noopener">Read Loon&rsquo;s announcement</a> <a class="btn" href="buyers-guide.html">Buyer&rsquo;s Guide</a> <a class="btn" href="boot-lab.html#book">Book a boot fit</a></p></div></section>')
    h += (f'<section class="ice"><div class="wrap">{sechead("More from the journal")}<div class="grid g3">{"".join(post_card(x) for x in POSTS[1:4])}</div></div></section>')
    return page("journal","Loon&rsquo;s Black Ridge expansion and the gear for it | Rodgers Ski &amp; Sport","Loon Mountain's Black Ridge adds 272 acres of expert-only tree skiing for winter 2027-28. What was announced and the skis, boots, boards and accessories that suit it, from Rodgers Ski & Sport.", h, "journal-loon-black-ridge.html")

def partners():
    h = hero("Partners and teams", "The mountains, organizations and programs Rodgers works with, and how to reach us if you run a team, club or school program.",
             "south-peak-winter-aerial", kicker="Community", short=True, pos="center 45%")
    h += crumbs(("About","about.html"),("Partners &amp; Teams",""))
    cards = ''.join(f'<a class="card" href="{p["url"]}" target="_blank" rel="noopener"><div class="kicker" style="margin-bottom:6px">{p["kind"]}</div><h3>{p["name"]}</h3><p>{p["blurb"]}</p><span class="go">Website</span></a>' for p in PARTNERS)
    h += (f'<section><div class="wrap">{sechead("Partners", "Mountains and organizations in the Lincoln area.")}<div class="grid g3">{cards}</div></div></section>')
    h += (f'<section class="ice"><div class="wrap split"><div><div class="kicker">Schools, clubs &amp; teams</div><h2 class="display" style="font-size:30px">Run a program? Talk to us.</h2>'
          f'<p style="margin-top:14px">Race teams, ski clubs, school programs and bike clubs: whether you&rsquo;re an athlete, coach or parent, we have the equipment and the knowledge you need. Contact the store nearest your program and we&rsquo;ll set gear and bench time aside.</p>'
          f'<p style="margin-top:14px"><a class="btn" href="tel:{LINCOLN["teltag"]}">Lincoln {LINCOLN["tel"]}</a> <a class="btn ghost" href="tel:{SCARB["teltag"]}">Scarborough {SCARB["tel"]}</a></p>'
          f'<p class="note">Teams and clubs will be listed here as they sign on.</p></div><div>{ph("lincoln-race-wall.jpg","The race wall at the Lincoln store","r43")}</div></div></section>')
    return page("about","Partners, Schools, Clubs &amp; Teams | Rodgers Ski &amp; Sport","Rodgers Ski & Sport partners and programs: South Peak Resort, Loon Mountain, Cannon Mountain, Bretton Woods, the Western White Mountains Chamber of Commerce, and how race teams, clubs and schools can work with the shop.", h, "partners.html")

# =====================================================================================
def about():
    h = hero("Our story", "A few pairs of skis sold from a Datsun pickup at Plymouth State in 1974. Today, two stores and one of the largest specialty ski retailers in the East.",
             "hiker-summit-overlook", kicker="Est. 1974", short=True, pos="center 60%")
    h += crumbs(("About",""))
    tl = [("1974","A few pairs of skis sold out of a Datsun pickup at Plymouth State College."),("1981","David and Helen open the first Rodgers Ski Outlet in Lincoln, NH."),("1986","The Scarborough, Maine store opens on Route 1."),("1988","Rodgers brings the &ldquo;snowboarding fad&rdquo; to the East."),
          ("1996","The Mothership Snowboard Shop launches, focused on small, American-made brands."),("2006","Ski Magazine recognizes Rodgers as a Gold Medal Shop."),("2008","The state-of-the-art Lincoln flagship is built."),("2026","New ownership, the same experts, and a bigger vision for both stores.")]
    h += (f'<section><div class="wrap">{sechead("Our story, year by year")}<div class="timeline">' + ''.join(f'<div><b>{y}</b><p>{t}</p></div>' for y,t in tl) + '</div></div></section>')
    mission = [("The hardware","We only sell the best products, curated for quality, performance and mechanical precision."),("The service","Our technicians work to exceed expectations. We don&rsquo;t just fix gear; we optimize it for your specific run."),
               ("The access","Through family-focused programs, we make skiing and riding accessible and affordable for the next generation."),("The culture","We are active in our communities, pushing people to the peaks.")]
    h += (f'<section class="ice"><div class="wrap">{sechead("The people behind the counter", "From a kid&rsquo;s first turns on snow to chasing singletrack or FIS race gates, our team lives the gear we stock.")}<div class="grid g4">' +
          ''.join(f'<div class="card"><div class="tick">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(mission)) + '</div></div></section>')
    h += (f'<section><div class="wrap">{sechead("The people who fit your boots", "Meet the staff through their picks; the full staff wall, with names and roles, is being photographed this fall.", ("Staff picks","staff-picks.html"))}<div class="grid g4">' +
          ''.join(f'<a class="card img" href="staff-picks.html">{ph(p["img"], p["who"], "r34", "", "pos-top")}<div class="body"><h3>{p["who"]}</h3><p>{p["store"]} &middot; {p["product"]}</p></div></a>' for p in STAFF_PICKS) + '</div></div></section>')
    h += credband(["Family-run since 1974","Ski Magazine Gold Medal Shop","Scarborough since 1986","SEDCO Legacy Business Award 2024"])
    h += (f'<section class="ice"><div class="wrap split"><div>{ph("scarborough-storefront-sunny-portrait.jpg","The Scarborough store","r34")}</div><div><div class="kicker">Two stores</div><h2 class="display" style="font-size:30px">Lincoln and Scarborough</h2>'
          f'<p style="margin-top:14px">The Lincoln, New Hampshire flagship carries skis, the Mothership snowboard shop, bikes, rentals, the Boot Lab and the tune room. The Scarborough, Maine store is a ski and bike shop with tuning, boot work and the Junior Seasonal Lease; it does not rent equipment or sell snowboards.</p>'
          f'<div style="margin-top:20px"><a class="btn" href="lincoln-nh.html">Lincoln, NH</a> <a class="btn ghost" href="scarborough-me.html">Scarborough, ME</a></div></div></div></section>')
    return page("about","About | Rodgers Ski &amp; Sport","The story of Rodgers Ski & Sport: from skis sold out of a Datsun pickup at Plymouth State in 1974 to the Ski Magazine Gold Medal Shop in Lincoln, NH and the Scarborough, ME store since 1986.", h, "about.html")

def gift_cards():
    h = hero("Gift cards", "Good at both stores, for gear, service, tuning and boot fitting. Pick one up at either register.",
             "south-peak-sunrise-panorama", kicker="Lincoln, NH &amp; Scarborough, ME", short=True, pos="center 60%")
    h += crumbs(("Gift Cards",""))
    h += (f'<section><div class="wrap split"><div>{ph("gift-cards.jpg","Rodgers Ski & Sport gift cards fanned on the counter","r34")}</div><div><h2 class="display" style="font-size:30px">The gift that fits</h2>'
          f'<p style="margin-top:14px">A Rodgers gift card works at the Lincoln and Scarborough registers on anything in the store: skis, boots, a bike tune, a boot fitting, a season lease.</p>'
          f'<p style="margin-top:10px">Buy in store today. Online gift cards, delivered by email with a printable card, are planned as the first item in the online shop.</p>'
          f'<div style="margin-top:20px"><a class="btn" href="tel:{LINCOLN["teltag"]}">Lincoln {LINCOLN["tel"]}</a> <a class="btn ghost" href="tel:{SCARB["teltag"]}">Scarborough {SCARB["tel"]}</a></div></div></div></section>')
    return page("about","Gift Cards | Rodgers Ski &amp; Sport","Rodgers Ski & Sport gift cards, good at the Lincoln, NH and Scarborough, ME stores for gear, tuning and boot fitting.", h, "gift-cards.html")

def contact():
    h = hero("Contact", "Two stores, two phone numbers, and a short form that goes to the right one.", "south-peak-winter-mountain", kicker="Lincoln, NH &amp; Scarborough, ME", short=True, pos="center 60%")
    h += crumbs(("Contact",""))
    h += (f'<section><div class="wrap"><div class="grid g2">'
          f'<div class="stack">{hours_box(LINCOLN, LIN_HOURS)}<div style="margin-top:16px">{map_embed(LINCOLN)}</div><p class="note"><a href="mailto:{LINCOLN["email"]}" style="color:var(--navy);font-weight:700">Email the Lincoln store</a></p></div>'
          f'<div class="stack">{hours_box(SCARB, SCA_HOURS)}<div style="margin-top:16px">{map_embed(SCARB)}</div><p class="note"><a href="mailto:{SCARB["email"]}" style="color:var(--navy);font-weight:700">Email the Scarborough store</a></p></div></div>'
          f'<div class="card" style="max-width:720px;margin:44px auto 0"><h3>Send a message</h3><form style="margin-top:14px"><label class="f">Store</label><select class="field"><option>Lincoln, NH</option><option>Scarborough, ME</option></select><label class="f">Name</label><input class="field"><label class="f">Email</label><input class="field" type="email"><label class="f">Message</label><textarea class="field" rows="4"></textarea><button class="btn" type="button">Send</button></form></div>'
          f'<div style="margin-top:34px">{weather(LINCOLN)}</div><div style="margin-top:12px">{weather(SCARB)}</div></div></section>')
    return page("about","Contact | Rodgers Ski &amp; Sport","Contact Rodgers Ski & Sport: Lincoln, NH (603) 745-8347 and Scarborough, ME (207) 883-3669, with hours, maps and directions.", h, "contact.html")

def legal(fname, title, body):
    h = f'<div class="crumbbar"><div class="wrap"><a href="index.html">Home</a> &nbsp;/&nbsp; {title}</div></div><section><div class="wrap article"><h1 class="display" style="font-size:36px;margin-bottom:22px">{title}</h1>{body}</div></section>'
    return page("", f"{title} | Rodgers Ski &amp; Sport", f"{title} for rodgersskiandsport.com.", h, fname)

def not_found():
    h = hero("Wrong turn", "That page isn&rsquo;t here. The stores are.", "lincoln-river-valley", kicker="404", short=True,
             ctas='<a class="btn accent" href="index.html">Home</a><a class="btn ghost-d" href="lincoln-nh.html">Lincoln, NH</a><a class="btn ghost-d" href="scarborough-me.html">Scarborough, ME</a>')
    return page("","Page not found | Rodgers Ski &amp; Sport","Page not found.", h, "404.html")


def employment():
    h = hero("Work at Rodgers", "Sales associates and ski technicians at both stores, full-time and part-time, seasonal and year-round. No experience required; we&rsquo;ll train. A love for outdoor activities is the requirement.",
             "hiker-rocky-ridge", kicker="Employment", short=True, pos="center 40%")
    h += crumbs(("About","about.html"),("Employment",""))
    jobs = ''.join(f'<div class="job"><div><h3>{j["title"]}</h3><div class="meta">{j["store"]} &middot; {j["type"]}</div></div><p>{j["blurb"]}</p><a class="btn sm" href="#apply">Apply</a></div>' for j in JOBS)
    h += (f'<section><div class="wrap"><p style="max-width:720px;margin-bottom:30px">Rodgers hires for the winter season in Lincoln, New Hampshire and Scarborough, Maine: people who ski, ride or bike and want to help others do the same. Openings are posted here and on Indeed; you can also stop in at either store and fill out an application.</p>{sechead("Open positions")}<div>{jobs}</div>'
          f'</div></section>')
    h += (f'<section class="ice" id="apply"><div class="wrap"><div class="grid g2"><div><div class="kicker">Why work here</div><h2 class="display" style="font-size:30px">Same experts, bigger vision</h2>'
          f'<p style="margin-top:14px">A family-run shop since 1974, a Ski Magazine Gold Medal Shop, and the first stop for skiers coming off I-93. You will learn boot fitting from Masterfit and Sidas certified fitters, tuning on Montana machines, and the race business from techs who prep FIS skis. Rodgers Ski &amp; Sport is an equal opportunity employer.</p>'
          f'<p style="margin-top:14px"><a class="btn ghost" href="tel:{LINCOLN["teltag"]}">Lincoln {LINCOLN["tel"]}</a> <a class="btn ghost" href="tel:{SCARB["teltag"]}">Scarborough {SCARB["tel"]}</a></p></div>'
          f'<div class="card"><h3>Apply</h3><form style="margin-top:14px"><label class="f">Position</label><select class="field"><option>Sales associate</option><option>Ski technician</option><option>Other</option></select><label class="f">Store</label><select class="field"><option>Lincoln, NH</option><option>Scarborough, ME</option><option>Either</option></select><label class="f">Name</label><input class="field"><label class="f">Email</label><input class="field" type="email"><label class="f">Phone</label><input class="field" type="tel"><label class="f">Availability and a few lines about you</label><textarea class="field" rows="4"></textarea><button class="btn" type="button">Send application</button></form></div></div></div></section>')
    return page("about","Employment | Rodgers Ski &amp; Sport","Jobs at Rodgers Ski & Sport in Lincoln, NH and Scarborough, ME: sales associates and ski technicians, full-time and part-time. No experience required.", h, "employment.html")


# =====================================================================================
def reserve_rental():
    pk = ''.join(f'<option>{n}</option>' for n in ["Junior ski package","Performance ski package","Advanced ski package","Demo skis","Snowboard package","Cross-country package","Snowshoes","Helmet only"])
    person = lambda i: (f'<div class="card" style="padding:18px 20px;margin-top:12px"><h4 style="font-size:15px">Person {i}</h4><div class="grid g2" style="gap:12px;margin-top:8px">'
                        f'<div><label class="f">Package</label><select class="field">{pk}</select></div><div><label class="f">Height</label><input class="field" placeholder="5 ft 9 in"></div>'
                        f'<div><label class="f">Weight</label><input class="field" placeholder="lb"></div><div><label class="f">Shoe size</label><input class="field" placeholder="US 10"></div></div>'
                        f'<label class="f">Ability</label><select class="field"><option>First time</option><option>Beginner: green runs</option><option>Intermediate: blue runs</option><option>Advanced: black runs</option></select></div>')
    h = hero("Reserve a rental", "Tell us your dates, packages and sizes and the Lincoln rental counter will have everything staged when you arrive. We confirm every request by email or phone; nothing is charged online.",
             "skiers-snowy-mountain", kicker="Lincoln, NH &middot; Rentals", short=True, pos="center")
    h += crumbs(("Lincoln, NH","lincoln-nh.html"),("Rentals","rentals.html"),("Reserve",""))
    h += (f'<section><div class="wrap"><div class="grid g3"><div style="grid-column:span 2"><div class="card"><h3>Reservation request</h3>'
          f'<form style="margin-top:14px"><div class="grid g2" style="gap:12px"><div><label class="f">Name</label><input class="field" required></div><div><label class="f">Email</label><input class="field" type="email" required></div>'
          f'<div><label class="f">Phone</label><input class="field" type="tel"></div><div><label class="f">Number of people</label><select class="field"><option>1</option><option>2</option><option>3</option><option>4</option><option>5 or more</option></select></div>'
          f'<div><label class="f">Pick-up date</label><input class="field" type="date"></div><div><label class="f">Return date</label><input class="field" type="date"></div></div>'
          f'{person(1)}{person(2)}<p class="note">Add a person for everyone in your party.</p>'
          f'<label class="f">Notes</label><textarea class="field" rows="3" placeholder="Boot size questions, a helmet for a child, anything else"></textarea>'
          f'<button class="btn accent" type="button">Send reservation request</button></form></div></div>'
          f'<div><div class="card"><h3>Good to know</h3><p style="margin-top:10px">Rentals are a Lincoln, NH program. The Scarborough, ME store does not rent equipment; it offers the <a href="lease.html" style="color:var(--navy);font-weight:700">Junior Seasonal Lease</a> instead.</p>'
          f'<p style="margin-top:10px">Rates are per day with consecutive use; a damage waiver is available at the counter. Full rate table on the <a href="rentals.html" style="color:var(--navy);font-weight:700">Rentals page</a>.</p>'
          f'<p style="margin-top:10px">Bring the boots and socks you ski in if you own them; the counter fits the rest.</p><div style="margin-top:16px">{hours_box(LINCOLN, LIN_HOURS)}</div></div></div></div></div></section>')
    return page("lincoln", "Reserve a Rental | Rodgers Ski &amp; Sport", "Request ski, snowboard, cross-country and snowshoe rentals at the Lincoln, NH store: dates, packages and sizes, confirmed by the rental counter.", h, "reserve-rental.html")
