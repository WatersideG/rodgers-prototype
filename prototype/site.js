(function(){
  // ---------- weather (Open-Meteo, no key; swap for the site's own /api/weather route in production) ----------
  var ICON = {"sun": "<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5.3 5.3l1.7 1.7M17 17l1.7 1.7M5.3 18.7 7 17M17 7l1.7-1.7"/></svg>", "cloud": "<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 18.5h10a4 4 0 0 0 .6-7.95A5.5 5.5 0 0 0 7.2 9.6 4.5 4.5 0 0 0 7 18.5z"/></svg>", "partly": "<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 19h8.5a3.5 3.5 0 0 0 .5-6.96A4.8 4.8 0 0 0 8.2 11.3 3.9 3.9 0 0 0 8 19z"/><path d="M5.5 10.2A3.6 3.6 0 1 1 11 6.3"/><path d="M9 2.8v1.4M3.3 5.7l1 1M2.2 10.6h1.4"/></svg>", "rain": "<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 15h10a4 4 0 0 0 .6-7.95A5.5 5.5 0 0 0 7.2 6.1 4.5 4.5 0 0 0 7 15z"/><path d="M9 17.5l-1 3M13 17.5l-1 3M17 17.5l-1 3"/></svg>", "snow": "<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9"/><path d="M12 3l-2 2M12 3l2 2M12 21l-2-2M12 21l2-2M4.2 7.5l2.7.7M4.2 7.5l.7-2.7M19.8 16.5l-2.7-.7M19.8 16.5l-.7 2.7M4.2 16.5l2.7-.7M4.2 16.5l.7 2.7M19.8 7.5l-2.7.7M19.8 7.5l-.7-2.7"/></svg>", "fog": "<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 9h16M4 13h16M6 17h12"/></svg>", "storm": "<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 14h10a4 4 0 0 0 .6-7.95A5.5 5.5 0 0 0 7.2 5.1 4.5 4.5 0 0 0 7 14z"/><path d="M13 14l-2.5 4h3L11 22"/></svg>"};
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
    var u='https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&daily=weather_code,temperature_2m_max,temperature_2m_min,wind_speed_10m_max,snowfall_sum&past_days=1&forecast_days=4&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York';
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
    var f=m.querySelector('form'); if(f){ f.addEventListener('submit',function(e){ e.preventDefault(); m.querySelector('.body').innerHTML='<div class="kicker">You are on the list</div><h2>Check your inbox</h2><p>Your 10% off code is on its way. Show it at the register in Lincoln or Scarborough.</p><p class="fine">Prototype: no email is sent from this page. In production the form posts to the email platform and the welcome flow delivers the code.</p>'; }); }
  }
})();
