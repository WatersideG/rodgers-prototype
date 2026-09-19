#!/usr/bin/env python3
"""Builds the Rodgers Ski & Sport prototype into ../prototype/.
Run: python3 build/build.py   (from the repo root)
Edit content in pages.py / data.py; shared shell, CSS, JS and flags in shell.py.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from shell import CSS, JS
import pages as P
import guides as G

OUT = os.path.join(os.path.dirname(HERE), 'prototype')
os.makedirs(OUT, exist_ok=True)

LEGAL = {
 'privacy-policy.html': ("Privacy Policy", """
<p><em>Effective date: at launch. Plain-language draft for counsel review.</em></p>
<h2>What we collect</h2><p>When you join our email list, request a boot fitting, or send a message through the site, we collect what you type into the form: your name, email address, phone number, the store you chose, and your message. We also use standard website analytics (Google Analytics 4) that record how visitors use the site without identifying you by name.</p>
<h2>How we use it</h2><p>To answer your request, to send the emails you signed up for (sale dates, new arrivals, service reminders and your 10% code), and to understand which pages are useful. We do not sell your information.</p>
<h2>Email</h2><p>Every email we send has an unsubscribe link. Unsubscribing removes you from marketing email; we may still reply to a message you sent us.</p>
<h2>Third parties</h2><p>Our email platform, analytics provider and map provider process data on our behalf under their own policies. Links to Instagram, Facebook, TikTok, partner websites and Google Maps leave this site.</p>
<h2>Your choices</h2><p>Ask us to see, correct or delete what we hold about you at office@rodgersskiandsport.com or by calling either store.</p>"""),
 'terms-of-use.html': ("Terms of Use", """
<p><em>Effective date: at launch. Plain-language draft for counsel review.</em></p>
<h2>Using this site</h2><p>The site describes our stores, services and prices. Prices, hours and availability can change; the store is the final word on what is in stock and what a service costs today.</p>
<h2>Gift cards</h2><p>Gift cards are redeemable at the Lincoln, NH and Scarborough, ME stores. Terms printed on the card apply.</p>
<h2>Rentals and leases</h2><p>Rental rates are valid with consecutive daily use; a damage waiver is available. Junior Seasonal Lease terms, including pick-up and return dates and late charges, are stated on the lease page and at sign-up.</p>
<h2>Content</h2><p>Text and photographs on this site belong to Rodgers Ski &amp; Sport or are used with the permission of the brands shown. Please ask before reusing them.</p>"""),
 'accessibility.html': ("Accessibility Statement", """
<p><em>Effective date: at launch. Plain-language draft for counsel review.</em></p>
<h2>Our standard</h2><p>We aim to meet WCAG 2.1 AA: readable contrast, keyboard navigation with visible focus, text alternatives on images, and forms with labels.</p>
<h2>Known limitations</h2><p>Embedded maps and the Instagram feed are provided by third parties and may not meet the same standard. Some brand photographs are decorative.</p>
<h2>Tell us</h2><p>If something on the site is hard to use, email office@rodgersskiandsport.com or call the Lincoln store at (603) 745-8347 and we will fix it or help you another way.</p>"""),
}

import re
LEDE_RE = re.compile(r'<!--LEDE-->(<div class="lede">.*?</p></div></div>)(<div class="crumbbar">.*?</div></div>)', re.S)
def write(name, html):
    html = LEDE_RE.sub(lambda m: m.group(2)+m.group(1), html).replace('<!--LEDE-->','')
    with open(os.path.join(OUT, name), 'w') as f: f.write(html)
    print(f'{name:36s} {len(html)//1024:4d} KB')

write('site.css', CSS.strip()+'\n')
write('site.js', JS.strip()+'\n')
write('index.html', P.home())
write('lincoln-nh.html', P.lincoln())
write('lincoln-nh-ski.html', P.lin_ski())
write('lincoln-nh-snowboard.html', P.lin_snowboard())
write('lincoln-nh-bikes.html', P.lin_bikes())
write('lincoln-nh-services.html', P.lin_services())
write('lincoln-nh-accessories.html', P.lin_accessories())
write('lincoln-nh-apparel.html', P.lin_apparel())
write('rentals.html', P.rentals())
write('scarborough-me.html', P.scarborough())
write('scarborough-me-ski.html', P.sca_ski())
write('scarborough-me-bikes.html', P.sca_bikes())
write('scarborough-me-services.html', P.sca_services())
write('scarborough-me-accessories.html', P.sca_accessories())
write('lease.html', P.lease())
write('boot-lab.html', P.boot_lab())
write('race.html', P.race())
write('staff-picks.html', P.staff_picks())
write('journal.html', P.journal())
write('journal-fall-tent-sale.html', P.tent_sale_article())
write('partners.html', P.partners())
write('employment.html', P.employment())
write('buyers-guide.html', G.buyers_guide())
write('outdoor-guide.html', G.outdoor_guide())
write('about.html', P.about())
write('gift-cards.html', P.gift_cards())
write('contact.html', P.contact())
write('404.html', P.not_found())
for fname,(title,body) in LEGAL.items():
    write(fname, P.legal(fname, title, body))
