#!/usr/bin/env python3
"""Builds the Rodgers Ski & Sport prototype into ../prototype/.
Run: python3 build/build.py   (from the repo root)
Edit content in pages.py / data.py; shared shell, CSS, JS and flags in shell.py.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from shell import CSS, JS
import glob
import shell
shell.HERO_SET.update(os.path.basename(f)[len('rodgers-'):-len('-desktop-2400x1000.jpg')] for f in glob.glob(os.path.join(os.path.dirname(HERE),'prototype','img','hero','*-desktop-2400x1000.jpg')))
for f in glob.glob(os.path.join(os.path.dirname(HERE),'prototype','img','logos','*.png')):
    b=os.path.basename(f); shell.LOGO_FILES[b[:-4]]=b
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
<h2>Your choices</h2><p>Ask us to see, correct or delete what we hold about you by emailing the Lincoln store through the Contact page or by calling either store.</p>"""),
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
<h2>Tell us</h2><p>If something on the site is hard to use, email the Lincoln store through the Contact page or call the Lincoln store at (603) 745-8347 and we will fix it or help you another way.</p>"""),
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
write('reserve-rental.html', P.reserve_rental())
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

# ---- site search: index every page, then the results page
import re as _re, json as _json, html as _html
def _text(h):
    h=_re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=_re.S)
    h=_re.sub(r'<header class="site">.*?</header>|<footer class="site">.*?</footer>|<div class="modal".*?</div></div></div>|<div class="topbar">.*?</div></div>','',h,flags=_re.S)
    return _re.sub(r'\s+',' ',_html.unescape(_re.sub(r'<[^>]+>',' ',h))).strip()
index=[]
for f in sorted(os.listdir(OUT)):
    if not f.endswith('.html') or f in ('search.html','404.html'): continue
    h=open(os.path.join(OUT,f)).read()
    t=_re.search(r'<title>(.*?)</title>',h); d=_re.search(r'name="description" content="(.*?)"',h)
    heads=' '.join(_re.findall(r'<h[123][^>]*>(.*?)</h[123]>',h,flags=_re.S))
    index.append({"u":f,"t":_html.unescape(t.group(1)).split(' | ')[0] if t else f,"d":_html.unescape(d.group(1)) if d else '',"h":_text(heads),"b":_text(h)[:6000]})
write('search-index.json', _json.dumps(index, ensure_ascii=False))
SEARCH_JS = r"""
(function(){
  var q=new URLSearchParams(location.search).get('q')||''; var box=document.getElementById('sq'); var out=document.getElementById('results'); var hd=document.getElementById('sh');
  if(box)box.value=q;
  if(!q.trim()){hd.textContent='Search the site';return;}
  fetch('search-index.json').then(function(r){return r.json();}).then(function(ix){
    var terms=q.toLowerCase().split(/\s+/).filter(Boolean);
    var hits=ix.map(function(p){var s=0,lt=p.t.toLowerCase(),lh=p.h.toLowerCase(),lb=p.b.toLowerCase();
      terms.forEach(function(w){ if(lt.indexOf(w)>-1)s+=8; if(lh.indexOf(w)>-1)s+=4; var m=lb.split(w).length-1; s+=Math.min(m,6); });
      return [s,p];}).filter(function(x){return x[0]>0;}).sort(function(a,b){return b[0]-a[0];});
    hd.textContent=hits.length?hits.length+' result'+(hits.length>1?'s':'')+' for \u201c'+q+'\u201d':'No results for \u201c'+q+'\u201d';
    out.innerHTML=hits.slice(0,30).map(function(x){var p=x[1];var i=p.b.toLowerCase().indexOf(terms[0]);var snip=i>-1?p.b.slice(Math.max(0,i-80),i+160):p.d;
      return '<div class="result"><a href="'+p.u+'">'+p.t+'</a><p>'+snip.replace(new RegExp('('+terms.map(function(w){return w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}).join('|')+')','ig'),'<mark>$1</mark>')+'</p><small>'+p.u+'</small></div>';}).join('');
  });
})();
"""
sh=('<div class="crumbbar"><div class="wrap"><a href="index.html">Home</a> &nbsp;/&nbsp; Search</div></div>'
    '<section><div class="wrap" style="max-width:820px"><h1 class="display" id="sh" style="font-size:32px">Search the site</h1>'
    '<form class="search" action="search.html" role="search" style="margin-top:18px;height:48px;max-width:520px"><input id="sq" type="search" name="q" placeholder="Skis, boot fitting, rentals, tune prices" aria-label="Search the site" style="width:100%;font-size:15px"><button type="submit" aria-label="Search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="18" height="18"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.8-3.8"/></svg></button></form>'
    '<div id="results" style="margin-top:20px"></div><p class="note" style="margin-top:24px">Prototype search runs in the browser over a page index built with the site. Production search runs against Payload content and products.</p></div></section>'
    f'<script>{SEARCH_JS}</script>')
write('search.html', shell.page("", "Search | Rodgers Ski &amp; Sport", "Search Rodgers Ski & Sport: products, services, prices and pages.", sh, "search.html"))
