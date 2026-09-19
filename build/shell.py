# Shared shell for the Rodgers Ski & Sport prototype: CSS, header, footer, modal, weather.
# Build flags
ONLINE_RESERVATIONS = False   # set True next season to expose the online rental reservation flow

LINCOLN = dict(name="Lincoln, NH", short="Lincoln", addr="5 Railroad St, Lincoln, NH 03251",
               tel="(603) 745-8347", teltag="6037458347", hours="Open every day 8:30–5",
               hours_today="Open today 8:30–5", email="office@rodgersskiandsport.com",
               maps="https://www.google.com/maps/dir/?api=1&destination=5+Railroad+St+Lincoln+NH+03251",
               embed="https://www.google.com/maps?q=5+Railroad+St,+Lincoln,+NH+03251&output=embed",
               lat="44.0364", lon="-71.6215", wx_label="Loon Mountain · Lincoln, NH")
SCARB = dict(name="Scarborough, ME", short="Scarborough", addr="332 US-1, Scarborough, ME 04074",
             tel="(207) 883-3669", teltag="2078833669",
             hours="Mon–Tue 10–6 · Wed closed · Thu–Fri 10–6 · Sat 10–5 · Sun 11–5",
             hours_today="Open today 10–6", email="scarborough@rodgersskiandsport.com",
             maps="https://www.google.com/maps/dir/?api=1&destination=332+US-1+Scarborough+ME+04074",
             embed="https://www.google.com/maps?q=332+US-1,+Scarborough,+ME+04074&output=embed",
             lat="43.5781", lon="-70.3217", wx_label="Scarborough, ME")

SOCIAL = dict(ig="https://www.instagram.com/rodgersski/", fb="https://www.facebook.com/RodgersSkiSport/",
              tt="https://www.tiktok.com/@rodgersskiandsport")

CSS = r"""
:root{
  --navy:#012D5D; --navy2:#0A2342; --deep:#071B33; --ink:#16283F; --body:#33475E;
  --ice:#EDF1F7; --ice2:#E2E9F2; --steel:#6B85A1; --line:#D5DEE9; --accent:#E8722C; --accent2:#C85E20;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:"Avenir Next","Helvetica Neue",Helvetica,"Segoe UI",Roboto,sans-serif;color:var(--body);background:#fff;font-size:15px;line-height:1.65}
img{max-width:100%}
a{color:inherit;text-decoration:none}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px}
h1,h2,h3,h4{color:var(--ink);line-height:1.15}
.display{font-weight:800;text-transform:uppercase;letter-spacing:-.5px;line-height:.98}
.kicker{font-size:11px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--steel);margin-bottom:12px}
.btn{display:inline-block;background:var(--navy);color:#fff;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:14px 28px;border-radius:0;border:1.5px solid var(--navy);transition:.15s;cursor:pointer;font-family:inherit}
.btn:hover{background:var(--navy2)}
.btn.ghost{background:transparent;color:var(--navy)}
.btn.ghost:hover{background:var(--ice)}
.btn.ondark{background:#fff;color:var(--navy);border-color:#fff}
.btn.ghost-d{background:transparent;color:#fff;border-color:rgba(255,255,255,.55)}
.btn.ghost-d:hover{border-color:#fff}
.btn.accent{background:var(--accent);border-color:var(--accent)}
.btn.accent:hover{background:var(--accent2)}
.btn.sm{padding:9px 18px;font-size:10.5px}
.skip{position:absolute;left:-999px;top:8px;background:var(--navy);color:#fff;padding:10px 16px;z-index:100}
.skip:focus{left:8px}
/* top bar */
.topbar{background:var(--deep);color:#B9C8DC;font-size:11.5px;letter-spacing:.4px;padding:8px 0}
.topbar .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
.topbar b{color:#fff;font-weight:600}
.topbar a:hover{color:#fff}
/* header */
header.site{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;padding-top:14px;padding-bottom:14px;gap:18px}
.logo img{height:34px;display:block}
nav.main{display:flex;align-items:center;gap:15px}
nav.main>div{position:relative}
nav.main a.top{font-size:11px;font-weight:700;letter-spacing:1px;white-space:nowrap;text-transform:uppercase;color:var(--ink);padding:8px 0;display:inline-block}
nav.main a.top:hover{color:var(--navy)}
nav.main a.top.on{box-shadow:inset 0 -2.5px 0 var(--accent)}
nav.main .dd:after{content:"\25BE";font-size:9px;color:var(--steel);margin-left:4px}
nav.main .menu{display:none;position:absolute;top:100%;left:-14px;background:#fff;border:1px solid var(--line);box-shadow:0 14px 34px rgba(7,27,51,.14);padding:8px;min-width:210px;z-index:60}
nav.main>div:hover .menu,nav.main>div:focus-within .menu{display:block}
nav.main .menu a{display:block;font-size:12.5px;font-weight:600;color:var(--body);padding:8px 12px}
nav.main .menu a:hover{background:var(--ice);color:var(--navy)}
nav.main .menu a.muted{color:var(--steel);font-weight:500}
#nt,.burger,.mobilenav,.mobilebar{display:none}
/* hero */
.hero{position:relative;color:#fff;overflow:hidden;background:var(--deep)}
.hero .wrap{position:relative;z-index:2;padding-top:84px;padding-bottom:64px}
.hero h1{color:#fff;font-size:clamp(40px,6vw,72px);max-width:820px}
.hero .sub{font-size:17px;color:#D7E2F0;max-width:560px;margin-top:18px}
.hero .ctas{margin-top:30px;display:flex;gap:12px;flex-wrap:wrap}
.hero .stats{position:absolute;right:32px;top:84px;text-align:right;z-index:3}
.hero .stats b{display:block;font-size:32px;font-weight:800;color:#fff;line-height:1}
.hero .stats span{font-size:10.5px;letter-spacing:2.5px;text-transform:uppercase;color:#AFC2DA}
.hero .stats>div{margin-bottom:26px}
.hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0}
.hero .shade{position:absolute;inset:0;background:linear-gradient(100deg,rgba(7,27,51,.9) 28%,rgba(7,27,51,.55) 62%,rgba(7,27,51,.25));z-index:1}
.hero.short .wrap{padding-top:64px;padding-bottom:48px}
.hero.short h1{font-size:clamp(34px,4.6vw,56px)}
.hero .credit{position:absolute;right:14px;bottom:10px;z-index:3;font-size:10px;color:rgba(255,255,255,.55);letter-spacing:.5px}
.crumbbar{background:var(--ice);border-bottom:1px solid var(--line);font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--steel)}
.crumbbar .wrap{padding-top:10px;padding-bottom:10px}
.crumbbar a:hover{color:var(--navy)}
/* photos */
.ph{position:relative;overflow:hidden;background:var(--ice2);display:block}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.ph.r43{aspect-ratio:4/3}.ph.r32{aspect-ratio:3/2}.ph.r169{aspect-ratio:16/9}.ph.r1{aspect-ratio:1/1}.ph.r34{aspect-ratio:3/4}.ph.r21{aspect-ratio:2/1}
.ph .lbl{position:absolute;left:12px;bottom:10px;background:rgba(7,27,51,.82);color:#fff;font-size:9.5px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:5px 10px;z-index:2}
.ph.pos-top img{object-position:center top}.ph.pos-bottom img{object-position:center bottom}
/* sections */
section{padding:76px 0}
section.tight{padding:52px 0}
.ice{background:var(--ice)}
.navy{background:var(--navy2);color:#C9D6E6}
.navy h2,.navy h3{color:#fff}
.sechead{display:flex;gap:44px;align-items:flex-end;margin-bottom:40px}
.sechead h2{flex:1.3;font-size:clamp(26px,3vw,34px);font-weight:800;text-transform:uppercase;letter-spacing:-.3px}
.sechead p{flex:1;color:var(--steel);font-size:14.5px}
.sechead .more{font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--navy);white-space:nowrap}
.navy .sechead p{color:#9FB4CE}
.grid{display:grid;gap:22px}
.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}.g5{grid-template-columns:repeat(5,1fr)}.g6{grid-template-columns:repeat(6,1fr)}
.split{display:flex;gap:48px;align-items:center}
.split>*{flex:1}
.split.rev{flex-direction:row-reverse}
.card{background:#fff;border:1px solid var(--line);padding:26px;transition:.15s;display:block}
a.card:hover{box-shadow:0 14px 34px rgba(7,27,51,.10);transform:translateY(-2px)}
.card.img{padding:0;overflow:hidden}
.card.img .body{padding:22px 24px 24px}
.navy .card{background:#12315A;border-color:#1D4470;color:#C9D6E6}
.navy .card h3,.navy .card b{color:#fff}
.card h3{font-size:17px;font-weight:800;text-transform:uppercase;letter-spacing:.4px}
.card p{margin-top:8px;font-size:14.5px}
.card .go{display:block;margin-top:14px;font-weight:700;color:var(--navy);font-size:11.5px;letter-spacing:1.5px;text-transform:uppercase}
.tagline{font-family:Georgia,"Times New Roman",serif;font-style:italic}
.tick{display:inline-block;width:34px;height:34px;background:var(--ice);color:var(--navy);font-weight:800;text-align:center;line-height:34px;margin-bottom:14px}
.pricelist{width:100%;border-collapse:collapse;font-size:14.5px}
.pricelist th{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--steel);text-align:left;padding:10px 12px;border-bottom:2px solid var(--navy)}
.pricelist td{padding:12px;border-bottom:1px solid var(--line);color:var(--ink)}
.pricelist td.p,.pricelist th.p{text-align:right;font-weight:700;white-space:nowrap;color:var(--navy)}
.pricelist td small{display:block;color:var(--steel);font-size:12.5px;font-weight:400}
.note{font-size:13px;color:var(--steel);margin-top:12px}
.brands{display:flex;flex-wrap:wrap;gap:10px}
.brands span{border:1.5px solid var(--line);color:var(--ink);font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:8px 16px;background:#fff}
.navy .brands span{background:transparent;border-color:#2A5182;color:#D7E2F0}
.credband{background:var(--navy);color:#fff;padding:22px 0}
.credband .wrap{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;font-size:11.5px;font-weight:700;letter-spacing:2px;text-transform:uppercase;align-items:center}
.credband i{color:#5B79A3;font-style:normal}
details.faq{background:#fff;border:1px solid var(--line);margin-bottom:10px;overflow:hidden}
details.faq summary{cursor:pointer;list-style:none;padding:18px 22px;font-weight:700;color:var(--ink);font-size:15px;display:flex;justify-content:space-between;align-items:center}
details.faq summary::-webkit-details-marker{display:none}
details.faq summary:after{content:"+";font-size:20px;color:var(--steel)}
details.faq[open] summary:after{content:"\2212"}
details.faq .a{padding:0 22px 18px;color:var(--body);font-size:14.5px}
.field{width:100%;border:1.5px solid var(--line);background:#fff;padding:12px 14px;font-size:13.5px;color:var(--ink);margin-bottom:12px;font-family:inherit}
.field::placeholder{color:var(--steel)}
label.f{display:block;font-size:10.5px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--ink);margin-bottom:6px}
.stagger{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;align-items:start}
.stagger .card:nth-child(even){margin-top:30px}
.qm{font-size:44px;font-weight:900;color:var(--navy);line-height:.6;margin-bottom:16px}
.avatar{width:38px;height:38px;background:var(--ice2);display:inline-flex;align-items:center;justify-content:center}
.pill{display:inline-block;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:4px 9px;background:var(--ice);color:var(--navy)}
.pill.orange{background:var(--accent);color:#fff}
.pill.dark{background:var(--navy);color:#fff}
.timeline{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.timeline div{border-top:3px solid var(--navy);padding-top:12px}
.timeline b{display:block;font-size:26px;font-weight:800;color:var(--navy);line-height:1;margin-bottom:6px}
.timeline p{font-size:13.5px}
/* seasonal cards */
.season .card.img .ph{aspect-ratio:4/3}
.season .card h3{font-size:15px}
/* staff picks */
.pick{display:grid;grid-template-columns:200px 1fr;gap:0;border:1px solid var(--line);background:#fff;overflow:hidden}
.pick .ph{aspect-ratio:auto;height:100%;min-height:260px}
.pick .body{padding:24px 26px}
.pick .who{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent2)}
.pick h3{font-size:19px;font-weight:800;text-transform:uppercase;margin:6px 0 10px;letter-spacing:.3px}
.pick blockquote{font-family:Georgia,"Times New Roman",serif;font-style:italic;font-size:15px;color:var(--ink);line-height:1.55}
.pick .meta{font-size:12px;color:var(--steel);margin-top:12px}
/* journal */
.post .ph{aspect-ratio:16/10}
.post .cat{font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent2)}
.post h3{font-size:17px;text-transform:none;letter-spacing:0;margin-top:6px;line-height:1.3}
.post .date{font-size:12px;color:var(--steel);margin-top:8px}
.feature{display:grid;grid-template-columns:1.1fr 1fr;gap:0;border:1px solid var(--line);background:#fff;overflow:hidden}
.feature .ph{aspect-ratio:auto;min-height:300px;max-height:460px;height:100%}
.feature .body{padding:34px 36px;display:flex;flex-direction:column;justify-content:center}
.feature h2{font-size:clamp(22px,2.6vw,30px);font-weight:800;text-transform:uppercase;letter-spacing:-.2px;margin:10px 0 12px}
.article{max-width:760px;margin:0 auto}
.article p{margin-bottom:18px;font-size:16px;line-height:1.7}
.article h2{font-size:24px;margin:34px 0 12px}
.article ul{margin:0 0 18px 22px}
.article li{margin-bottom:6px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:28px}
.chips a{font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:8px 14px;border:1.5px solid var(--line);color:var(--ink)}
.chips a.on,.chips a:hover{background:var(--navy);border-color:var(--navy);color:#fff}
/* weather */
.wx{display:flex;align-items:center;gap:22px;background:#fff;border:1px solid var(--line);padding:14px 20px;font-size:13px;color:var(--ink);flex-wrap:wrap}
.wx .now{display:flex;align-items:center;gap:12px;min-width:210px}
.wx .now svg{width:38px;height:38px;flex:none}
.wx .now b{display:block;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:var(--steel);font-weight:700}
.wx .now span{font-size:20px;font-weight:800;color:var(--navy);line-height:1.1}
.wx .stat{display:flex;flex-direction:column;min-width:74px}
.wx .stat i{font-style:normal;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--steel);font-weight:700}
.wx .stat b{font-size:15px;color:var(--ink)}
.wx .days{display:flex;gap:14px;margin-left:auto;border-left:1px solid var(--line);padding-left:18px}
.wx .day{text-align:center;min-width:52px}
.wx .day i{font-style:normal;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--steel);font-weight:700;display:block}
.wx .day svg{width:24px;height:24px;margin:3px 0}
.wx .day b{font-size:12px;display:block;color:var(--ink)}
.wx .day b small{color:var(--steel);font-weight:500}
.wx .src{width:100%;font-size:10px;color:var(--steel);letter-spacing:.5px;margin-top:-4px}
.wx.dark{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.18);color:#fff}
.wx.dark .now span,.wx.dark .stat b,.wx.dark .day b{color:#fff}
.wx.dark .days{border-color:rgba(255,255,255,.2)}
/* hours */
.hoursbox{background:#fff;border:1px solid var(--line);padding:22px 24px}
.hoursbox h4{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--steel);margin-bottom:10px}
.hoursbox table{width:100%;font-size:14px;border-collapse:collapse}
.hoursbox td{padding:5px 0;border-bottom:1px solid var(--ice2);color:var(--ink)}
.hoursbox td:last-child{text-align:right;font-weight:700}
.hoursbox .gbp{font-size:11px;color:var(--steel);margin-top:12px}
.map{aspect-ratio:16/9;background:var(--ice2);border:1px solid var(--line)}
.map iframe{width:100%;height:100%;border:0;display:block}
/* modal */
.modal{position:fixed;inset:0;background:rgba(7,27,51,.62);z-index:200;display:none;align-items:center;justify-content:center;padding:20px}
.modal.open{display:flex}
.modal .box{background:#fff;max-width:760px;width:100%;display:grid;grid-template-columns:1fr 1fr;overflow:hidden;position:relative;box-shadow:0 30px 80px rgba(0,0,0,.35)}
.modal .box .ph{aspect-ratio:auto;height:100%;min-height:300px}
.modal .body{padding:36px 34px}
.modal h2{font-size:26px;font-weight:800;text-transform:uppercase;letter-spacing:-.3px;margin:8px 0 10px;line-height:1.05}
.modal .off{font-size:64px;font-weight:900;color:var(--accent);line-height:.9;letter-spacing:-2px}
.modal .off small{font-size:14px;font-weight:700;letter-spacing:2px;color:var(--navy);display:block;margin-top:6px}
.modal .x{position:absolute;right:10px;top:8px;background:none;border:0;font-size:26px;color:var(--steel);cursor:pointer;line-height:1;padding:6px 10px}
.modal .fine{font-size:11px;color:var(--steel);margin-top:10px}
.modal .radios{display:flex;gap:14px;font-size:13px;margin-bottom:12px;color:var(--ink)}
/* footer */
footer.site{background:var(--deep);color:#9FB4CE;font-size:13.5px}
footer.site .cols{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:34px;padding:60px 0 40px}
footer.site h5{color:#fff;font-size:11px;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px}
footer.site a:hover{color:#fff}
footer.site .cols img{height:30px;margin-bottom:14px}
footer.site .band{border-top:1px solid #16355C;padding:26px 0;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
footer.site .band b{color:#fff;font-size:15px;flex:1.4;min-width:260px}
footer.site .band .field{margin:0;flex:1;background:#0E2A4D;border-color:#1D4470;color:#fff}
footer.site .band .field::placeholder{color:#7E96B5}
footer.site .band select.field{flex:.6}
footer.site .legal{border-top:1px solid #16355C;padding:18px 0;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;font-size:10.5px;letter-spacing:1px;text-transform:uppercase;color:#5B79A3}
.soc{display:flex;gap:10px;margin-top:14px}
.soc a{width:32px;height:32px;background:#12315A;display:inline-flex;align-items:center;justify-content:center;color:#9FB4CE;font-size:11px;font-weight:800}
.soc a:hover{background:var(--navy);color:#fff}
/* responsive */
@media (max-width:1080px){nav.main{gap:11px}nav.main a.top{font-size:10px}}
@media (max-width:940px){
  nav.main{display:none}
  .burger{display:flex;flex-direction:column;gap:5px;cursor:pointer;padding:8px}
  .burger i{display:block;width:24px;height:2.5px;background:var(--ink)}
  #nt:checked~.mobilenav{display:block}
  .mobilenav{background:#fff;border-top:1px solid var(--line);padding:8px 24px 18px}
  .mobilenav a,.mobilenav summary{display:block;padding:12px 0;border-bottom:1px solid var(--ice2);font-weight:700;color:var(--ink);font-size:14px;cursor:pointer;list-style:none}
  .mobilenav details a{padding-left:16px;font-weight:500}
  .mobilenav .cta{padding-top:14px}
  .mobilebar{display:flex;position:fixed;bottom:0;left:0;right:0;background:var(--navy);z-index:80}
  .mobilebar a{flex:1;text-align:center;color:#fff;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:14px 6px;border-right:1px solid #1D4470}
  .mobilebar a.res{background:var(--accent);border:0}
  body{padding-bottom:46px}
  .topbar .wrap{justify-content:center;font-size:11px}
  .hero .stats{position:static;text-align:left;display:flex;gap:28px;margin-top:24px}
  .hero .stats>div{margin:0}
  .hero .wrap{padding-top:52px;padding-bottom:44px}
  .sechead{flex-direction:column;align-items:flex-start;gap:10px;margin-bottom:26px}
  .g3,.g4,.g5,.g6{grid-template-columns:1fr 1fr}
  .stagger{grid-template-columns:1fr 1fr}
  .stagger .card:nth-child(even){margin-top:0}
  .split,.split.rev{flex-direction:column;align-items:stretch}
  .timeline{grid-template-columns:1fr 1fr}
  .feature{grid-template-columns:1fr}
  .feature .ph{min-height:220px}
  .modal .box{grid-template-columns:1fr}
  .modal .box .ph{min-height:160px;max-height:180px}
  footer.site .cols{grid-template-columns:1fr 1fr}
  section{padding:54px 0}
  .wx .days{margin-left:0;border-left:0;padding-left:0;width:100%;justify-content:flex-start}
}
@media (max-width:600px){
  .wrap{padding:0 16px}
  .g2,.g3,.g4,.g5,.g6,.stagger,.timeline{grid-template-columns:1fr}
  .pick{grid-template-columns:1fr}
  .pick .ph{min-height:0;aspect-ratio:4/3}
  footer.site .cols{grid-template-columns:1fr}
  footer.site .band .field,footer.site .band select.field{flex:1 1 100%}
  .hero h1{font-size:38px}
  .hero .stats{flex-wrap:wrap;gap:18px}
  .pricelist{font-size:13.5px}
  .modal .off{font-size:48px}
}
"""

WX_ICONS = {
 'sun':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5.3 5.3l1.7 1.7M17 17l1.7 1.7M5.3 18.7 7 17M17 7l1.7-1.7"/></svg>',
 'cloud':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 18.5h10a4 4 0 0 0 .6-7.95A5.5 5.5 0 0 0 7.2 9.6 4.5 4.5 0 0 0 7 18.5z"/></svg>',
 'partly':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 19h8.5a3.5 3.5 0 0 0 .5-6.96A4.8 4.8 0 0 0 8.2 11.3 3.9 3.9 0 0 0 8 19z"/><path d="M5.5 10.2A3.6 3.6 0 1 1 11 6.3"/><path d="M9 2.8v1.4M3.3 5.7l1 1M2.2 10.6h1.4"/></svg>',
 'rain':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 15h10a4 4 0 0 0 .6-7.95A5.5 5.5 0 0 0 7.2 6.1 4.5 4.5 0 0 0 7 15z"/><path d="M9 17.5l-1 3M13 17.5l-1 3M17 17.5l-1 3"/></svg>',
 'snow':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9"/><path d="M12 3l-2 2M12 3l2 2M12 21l-2-2M12 21l2-2M4.2 7.5l2.7.7M4.2 7.5l.7-2.7M19.8 16.5l-2.7-.7M19.8 16.5l-.7 2.7M4.2 16.5l2.7-.7M4.2 16.5l.7 2.7M19.8 7.5l-2.7.7M19.8 7.5l-.7-2.7"/></svg>',
 'fog':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 9h16M4 13h16M6 17h12"/></svg>',
 'storm':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 14h10a4 4 0 0 0 .6-7.95A5.5 5.5 0 0 0 7.2 5.1 4.5 4.5 0 0 0 7 14z"/><path d="M13 14l-2.5 4h3L11 22"/></svg>',
}

JS = r"""
(function(){
  // ---------- weather (Open-Meteo, no key; swap for the site's own /api/weather route in production) ----------
  var ICON = %s;
  function pick(code){
    if(code===0)return 'sun'; if(code<=2)return 'partly'; if(code===3)return 'cloud';
    if(code===45||code===48)return 'fog'; if(code>=71&&code<=77||code===85||code===86)return 'snow';
    if(code>=95)return 'storm'; return 'rain';
  }
  function label(code){
    var m={0:'Clear',1:'Mostly clear',2:'Partly cloudy',3:'Overcast',45:'Fog',48:'Fog',51:'Drizzle',53:'Drizzle',55:'Drizzle',56:'Freezing drizzle',57:'Freezing drizzle',61:'Light rain',63:'Rain',65:'Heavy rain',66:'Freezing rain',67:'Freezing rain',71:'Light snow',73:'Snow',75:'Heavy snow',77:'Snow grains',80:'Showers',81:'Showers',82:'Heavy showers',85:'Snow showers',86:'Snow showers',95:'Thunderstorm',96:'Thunderstorm',99:'Thunderstorm'};
    return m[code]||'—';
  }
  var DAYS=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'], MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  function dl(iso){var d=new Date(iso+'T12:00:00');return {dow:DAYS[d.getDay()],md:MON[d.getMonth()]+' '+d.getDate()};}
  document.querySelectorAll('.wx[data-lat]').forEach(function(el){
    var lat=el.getAttribute('data-lat'),lon=el.getAttribute('data-lon');
    var u='https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&daily=weather_code,temperature_2m_max,temperature_2m_min,wind_speed_10m_max,snowfall_sum&past_days=1&forecast_days=4&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%%2FNew_York';
    fetch(u).then(function(r){return r.json();}).then(function(j){
      var d=j.daily; var t=1; // index 0 = yesterday
      var today=dl(d.time[t]);
      var h='<div class="now">'+ICON[pick(d.weather_code[t])]+'<div><b>'+today.dow+' '+today.md+'</b><span>'+label(d.weather_code[t])+'</span></div></div>';
      h+='<div class="stat"><i>High / Low</i><b>'+Math.round(d.temperature_2m_max[t])+'&deg; / '+Math.round(d.temperature_2m_min[t])+'&deg;</b></div>';
      h+='<div class="stat"><i>Wind</i><b>'+Math.round(d.wind_speed_10m_max[t])+' mph</b></div>';
      h+='<div class="stat"><i>Snow 24 hr</i><b>'+(d.snowfall_sum[0]||0).toFixed(1)+'"</b></div>';
      h+='<div class="days">';
      for(var i=t+1;i<t+4&&i<d.time.length;i++){var x=dl(d.time[i]);h+='<div class="day"><i>'+x.dow+'</i>'+ICON[pick(d.weather_code[i])]+'<b>'+Math.round(d.temperature_2m_max[i])+'&deg; <small>'+Math.round(d.temperature_2m_min[i])+'&deg;</small></b></div>';}
      h+='</div><div class="src">'+el.getAttribute('data-label')+' &middot; forecast: Open-Meteo</div>';
      el.innerHTML=h;
    }).catch(function(){ el.innerHTML='<div class="src">'+el.getAttribute('data-label')+' &middot; weather unavailable</div>'; });
  });
  // ---------- email modal ----------
  var m=document.getElementById('signup');
  if(m){
    var shown=false;
    try{shown=sessionStorage.getItem('rsx')==='1';}catch(e){}
    function open(){ if(shown)return; shown=true; m.classList.add('open'); try{sessionStorage.setItem('rsx','1');}catch(e){} }
    function close(){ m.classList.remove('open'); }
    if(!shown){ setTimeout(open,7000); window.addEventListener('scroll',function(){ if(window.scrollY>document.body.scrollHeight*0.35)open(); },{passive:true}); }
    m.querySelectorAll('[data-close]').forEach(function(b){b.addEventListener('click',close);});
    m.addEventListener('click',function(e){ if(e.target===m)close(); });
    document.addEventListener('keydown',function(e){ if(e.key==='Escape')close(); });
    var f=m.querySelector('form'); if(f){ f.addEventListener('submit',function(e){ e.preventDefault(); m.querySelector('.body').innerHTML='<div class="kicker">You are on the list</div><h2>Check your inbox</h2><p>Your 10%% off code is on its way. Show it at the register in Lincoln or Scarborough.</p><p class="fine">Prototype: no email is sent from this page. In production the form posts to the email platform and the welcome flow delivers the code.</p>'; }); }
  }
})();
""" % (str({k:v for k,v in WX_ICONS.items()}).replace("'",'"'))


def nav_html(active=""):
    def on(k): return ' on' if active==k else ''
    lin = [("lincoln-nh.html","Overview"),("lincoln-nh-ski.html","Ski"),("lincoln-nh-snowboard.html","Snowboard"),
           ("lincoln-nh-bikes.html","Bikes"),("lincoln-nh-services.html","Services &amp; Tuning"),
           ("rentals.html","Rentals"),("lincoln-nh-accessories.html","Accessories"),("lincoln-nh-apparel.html","Apparel")]
    sca = [("scarborough-me.html","Overview"),("scarborough-me-ski.html","Ski"),("scarborough-me-bikes.html","Bikes"),
           ("scarborough-me-services.html","Services &amp; Tuning"),("lease.html","Junior Seasonal Lease"),
           ("scarborough-me-accessories.html","Accessories")]
    jou = [("journal.html","Latest"),("staff-picks.html","Staff Picks"),("journal-fall-tent-sale.html","Fall Tent Sale"),("partners.html","Partners &amp; Teams")]
    def menu(items): return '<div class="menu">'+''.join(f'<a href="{h}">{t}</a>' for h,t in items)+'</div>'
    desk = (f'<div><a class="top dd{on("lincoln")}" href="lincoln-nh.html">Lincoln, NH</a>{menu(lin)}</div>'
            f'<div><a class="top dd{on("scarb")}" href="scarborough-me.html">Scarborough, ME</a>{menu(sca)}</div>'
            f'<div><a class="top{on("boot")}" href="boot-lab.html">The Boot Lab</a></div>'
            f'<div><a class="top{on("race")}" href="race.html">Race</a></div>'
            f'<div><a class="top dd{on("journal")}" href="journal.html">Journal</a>{menu(jou)}</div>'
            f'<div><a class="top{on("about")}" href="about.html">About</a></div>'
            f'<div><a class="top{on("gift")}" href="gift-cards.html">Gift Cards</a></div>'
            f'<div><a class="top{on("contact")}" href="contact.html">Contact</a></div>'
            f'<a class="btn accent sm" href="boot-lab.html#book">Book a Boot Fit</a>')
    def mob(items): return ''.join(f'<a href="{h}">{t}</a>' for h,t in items)
    mobile = (f'<details><summary>Lincoln, NH</summary>{mob(lin)}</details>'
              f'<details><summary>Scarborough, ME</summary>{mob(sca)}</details>'
              f'<a href="boot-lab.html">The Boot Lab</a><a href="race.html">Race</a>'
              f'<details><summary>Journal</summary>{mob(jou)}</details>'
              f'<a href="about.html">About</a><a href="gift-cards.html">Gift Cards</a><a href="contact.html">Contact</a>'
              f'<div class="cta"><a class="btn accent" style="display:block;text-align:center" href="boot-lab.html#book">Book a Boot Fit</a></div>')
    return desk, mobile


def head(title, desc, canonical):
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{title}</title><meta name="description" content="{desc}"><link rel="icon" href="img/logo.png">'
            f'<link rel="stylesheet" href="site.css"></head>')


def topbar():
    return (f'<div class="topbar"><div class="wrap"><span><b>{LINCOLN["name"]}</b> &middot; {LINCOLN["hours_today"]} &middot; '
            f'<a href="tel:{LINCOLN["teltag"]}"><b>{LINCOLN["tel"]}</b></a> &middot; <a href="lincoln-nh.html">Store info &rarr;</a></span>'
            f'<span><b>{SCARB["name"]}</b> &middot; {SCARB["hours_today"]} &middot; <a href="tel:{SCARB["teltag"]}"><b>{SCARB["tel"]}</b></a> &middot; <a href="scarborough-me.html">Store info &rarr;</a></span></div></div>')


def header(active=""):
    desk, mobile = nav_html(active)
    return (f'<a class="skip" href="#main">Skip to content</a>{topbar()}<header class="site"><input type="checkbox" id="nt"><div class="wrap">'
            f'<a class="logo" href="index.html"><img src="img/logo.png" alt="Rodgers Ski &amp; Sport"></a><nav class="main">{desk}</nav>'
            f'<label class="burger" for="nt" aria-label="Menu"><i></i><i></i><i></i></label></div><div class="mobilenav">{mobile}</div></header>')


def modal():
    return ('<div class="modal" id="signup" role="dialog" aria-modal="true" aria-labelledby="signup-h"><div class="box">'
            '<div class="ph"><img src="img/lincoln-boot-wall.jpg" alt="The boot wall at the Lincoln store"></div>'
            '<div class="body"><button class="x" data-close aria-label="Close">&times;</button>'
            '<div class="kicker">Join the Rodgers list</div><div class="off">10% off<small>your next in-store purchase</small></div>'
            '<h2 id="signup-h">Sale dates, new arrivals, tune reminders</h2>'
            '<form><div class="radios"><label><input type="radio" name="store" checked> Lincoln, NH</label><label><input type="radio" name="store"> Scarborough, ME</label><label><input type="radio" name="store"> Both</label></div>'
            '<input class="field" type="email" placeholder="Email address" required><button class="btn accent" type="submit" style="width:100%">Send my code</button></form>'
            '<p class="fine">One code per customer, in store only. Unsubscribe anytime. Exclusions on the code apply to some new-season product; the register will say so.</p></div></div></div>')


def footer():
    return (f'<div class="mobilebar"><a href="tel:{LINCOLN["teltag"]}">&#9742; Lincoln</a><a href="tel:{SCARB["teltag"]}">&#9742; Scarborough</a><a class="res" href="boot-lab.html#book">Boot Fit</a></div>'
            f'<footer class="site"><div class="wrap"><div class="cols"><div><img src="img/logo.png" alt="Rodgers Ski &amp; Sport">'
            f'<p>Family-run ski and bike shops in Lincoln, New Hampshire and Scarborough, Maine. We don&rsquo;t just sell gear, we test it.</p>'
            f'<div class="soc"><a href="{SOCIAL["ig"]}" aria-label="Instagram @rodgersski">IG</a><a href="{SOCIAL["fb"]}" aria-label="Facebook RodgersSkiSport">FB</a><a href="{SOCIAL["tt"]}" aria-label="TikTok @rodgersskiandsport">TT</a></div></div>'
            f'<div><h5><a href="lincoln-nh.html">Lincoln, NH &rarr;</a></h5>{LINCOLN["addr"]}<br><a href="tel:{LINCOLN["teltag"]}"><b style="color:#fff">{LINCOLN["tel"]}</b></a><br>{LINCOLN["hours"]}<br>Ski &middot; Snowboard &middot; Bikes &middot; Rentals &middot; Boot Lab<br><a href="{LINCOLN["maps"]}">Directions</a></div>'
            f'<div><h5><a href="scarborough-me.html">Scarborough, ME &rarr;</a></h5>{SCARB["addr"]}<br><a href="tel:{SCARB["teltag"]}"><b style="color:#fff">{SCARB["tel"]}</b></a><br>Mon&ndash;Tue 10&ndash;6 &middot; Wed closed<br>Thu&ndash;Fri 10&ndash;6 &middot; Sat 10&ndash;5 &middot; Sun 11&ndash;5<br>Ski &middot; Bikes &middot; Junior Seasonal Lease<br><a href="{SCARB["maps"]}">Directions</a></div>'
            f'<div><h5>Shop &amp; Services</h5><a href="boot-lab.html">The Boot Lab</a><br><a href="race.html">Race</a><br><a href="rentals.html">Rentals (Lincoln)</a><br><a href="lease.html">Junior Seasonal Lease (Scarborough)</a><br><a href="gift-cards.html">Gift Cards</a><br><a href="journal.html">Journal</a> &middot; <a href="staff-picks.html">Staff Picks</a><br><a href="partners.html">Partners &amp; Teams</a><br><a href="about.html">About</a> &middot; <a href="contact.html">Contact</a><br><a href="mailto:{LINCOLN["email"]}">{LINCOLN["email"]}</a></div></div>'
            f'<div class="band"><b>Sale dates, new arrivals and tune reminders. 10% off your next in-store purchase when you join.</b><input class="field" placeholder="Email address"><select class="field"><option>Lincoln, NH</option><option>Scarborough, ME</option><option>Both</option></select><a class="btn ondark sm" href="#">Sign up</a></div>'
            f'<div class="legal"><span>Family-run since 1974 &middot; Ski Magazine Gold Medal Shop &middot; Lincoln, NH &middot; Scarborough, ME</span><span>&copy; 2026 Rodgers Ski &amp; Sport &middot; <a href="privacy-policy.html">Privacy</a> &middot; <a href="terms-of-use.html">Terms</a> &middot; <a href="accessibility.html">Accessibility</a></span></div></div></footer>'
            f'{modal()}<script src="site.js"></script></body></html>')


def page(active, title, desc, main_html, fname):
    return head(title, desc, fname) + '<body>' + header(active) + f'<main id="main">{main_html}</main>' + footer()


# ---------- reusable fragments ----------
def hero(h1, sub, img, ctas="", kicker="", stats="", short=False, credit="", pos="center"):
    st = f'<div class="stats">{stats}</div>' if stats else ''
    kk = f'<div class="kicker" style="color:#AFC2DA">{kicker}</div>' if kicker else ''
    cr = f'<div class="credit">{credit}</div>' if credit else ''
    return (f'<div class="hero{" short" if short else ""}"><div class="bg" style="background-image:url(img/{img});background-position:{pos}"></div><div class="shade"></div>{st}'
            f'<div class="wrap">{kk}<h1 class="display">{h1}</h1><p class="sub">{sub}</p>{"<div class=ctas>"+ctas+"</div>" if ctas else ""}</div>{cr}</div>')

def crumbs(*parts):
    items = [f'<a href="index.html">Home</a>'] + [f'<a href="{h}">{t}</a>' if h else t for t,h in parts]
    return f'<div class="crumbbar"><div class="wrap">{" &nbsp;/&nbsp; ".join(items)}</div></div>'

def ph(img, alt, ratio="r43", lbl="", extra=""):
    l = f'<span class="lbl">{lbl}</span>' if lbl else ''
    return f'<div class="ph {ratio} {extra}"><img src="img/{img}" alt="{alt}" loading="lazy">{l}</div>'

def weather(store, dark=False):
    return (f'<div class="wx{" dark" if dark else ""}" data-lat="{store["lat"]}" data-lon="{store["lon"]}" data-label="{store["wx_label"]}">'
            f'<div class="src">{store["wx_label"]} &middot; loading forecast&hellip;</div></div>')

def hours_box(store, rows):
    tr = ''.join(f'<tr><td>{d}</td><td>{h}</td></tr>' for d,h in rows)
    return (f'<div class="hoursbox"><h4>Hours &middot; {store["name"]}</h4><table>{tr}</table>'
            f'<p class="gbp">Hours and holiday changes sync from the store&rsquo;s Google Business Profile.</p>'
            f'<p style="margin-top:14px"><a class="btn sm" href="{store["maps"]}">Get directions</a> <a class="btn ghost sm" href="tel:{store["teltag"]}">Call {store["tel"]}</a></p></div>')

def map_embed(store):
    return f'<div class="map"><iframe src="{store["embed"]}" title="Map to Rodgers Ski &amp; Sport, {store["name"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>'

def pricelist(rows, cols=("Service","Price"), note=""):
    th = ''.join(f'<th{" class=p" if i else ""}>{c}</th>' for i,c in enumerate(cols))
    body = ''
    for r in rows:
        tds = ''.join(f'<td{" class=p" if i else ""}>{c}</td>' for i,c in enumerate(r))
        body += f'<tr>{tds}</tr>'
    n = f'<p class="note">{note}</p>' if note else ''
    return f'<table class="pricelist"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>{n}'

def faq(items):
    return ''.join(f'<details class="faq"><summary>{q}</summary><div class="a">{a}</div></details>' for q,a in items)

def sechead(h, p="", more=""):
    m = f'<a class="more" href="{more[1]}">{more[0]} &rarr;</a>' if more else ''
    return f'<div class="sechead"><h2>{h}</h2>{"<p>"+p+"</p>" if p else ""}{m}</div>'

def card(href, img, alt, h3, p, go="", ratio="r43"):
    g = f'<span class="go">{go} &rarr;</span>' if go else ''
    return f'<a class="card img" href="{href}">{ph(img, alt, ratio)}<div class="body"><h3>{h3}</h3><p>{p}</p>{g}</div></a>'

def credband(items):
    return '<div class="credband"><div class="wrap">' + '<i>&bull;</i>'.join(f'<span>{i}</span>' for i in items) + '</div></div>'
