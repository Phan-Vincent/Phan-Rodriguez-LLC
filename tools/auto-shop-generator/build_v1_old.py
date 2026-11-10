#!/usr/bin/env python3
"""Builds the three standalone mock sites. Usage: build.py <mockups_dir>"""
import sys, os

BASE_CSS = """
@font-face{font-family:Poster;src:local('Impact'),local('Haettenschweiler'),local('Anton'),local('Arial Black'),local('Arial-Black'),local('Roboto Black'),local('Arial Bold'),local('Arial-BoldMT'),local('Liberation Sans Bold'),local('DejaVu Sans Bold')}
body:after{content:'';position:fixed;inset:0;pointer-events:none;z-index:50;opacity:.09;mix-blend-mode:multiply;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .9 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:20px}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.6;overflow-x:hidden}
h1,h2,h3,p,blockquote,figure{margin:0}a{color:inherit;text-decoration:none}
a:focus-visible,button:focus-visible{outline:3px solid var(--focus,var(--accent));outline-offset:5px}
svg{display:block;max-width:100%}
.wrap{width:min(1180px,calc(100% - 72px));margin:auto}
.mono{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;letter-spacing:2px;text-transform:uppercase;font-weight:700}
.skip{position:absolute;left:16px;top:-80px;z-index:9;background:#fff;color:#000;padding:10px}.skip:focus{top:10px}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:24px;min-height:92px}
nav{display:flex;gap:28px;font-size:13px;font-weight:700}
nav a{position:relative;padding:4px 0}
nav a:after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:currentColor;transform:scaleX(0);transform-origin:left;transition:transform .3s cubic-bezier(.2,.8,.2,1)}
nav a:hover:after{transform:scaleX(1)}
.phone{font-family:ui-monospace,Menlo,Consolas,monospace;font-weight:700;font-size:15px;white-space:nowrap}
.btn{display:inline-flex;align-items:center;gap:16px;min-height:54px;padding:14px 24px;font-size:14px;font-weight:800;border:2px solid currentColor;position:relative;overflow:hidden;isolation:isolate;transition:color .3s}
.btn:before{content:"";position:absolute;inset:0;background:var(--btn-fill,var(--ink));transform:translateY(101%);transition:transform .35s cubic-bezier(.2,.8,.2,1);z-index:-1}
.btn:hover:before{transform:none}.btn:hover{color:var(--btn-hover,var(--bg))}
.btn i{font-style:normal;transition:transform .3s}.btn:hover i{transform:translateX(6px)}
.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:34px}
.status{display:inline-flex;align-items:center;gap:10px}
.status b{width:9px;height:9px;border-radius:50%;background:#9a9a9a}
.status.open b{background:#22b455;animation:pulse 1.8s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 #22b45599}100%{box-shadow:0 0 0 12px #22b45500}}
h1 .w{display:inline-block;overflow:hidden;vertical-align:top;padding:.08em .06em .08em 0;margin:-.08em 0}
h1 .w>span{display:inline-block;transform:translateY(110%);transition:transform .9s cubic-bezier(.2,.8,.2,1);transition-delay:calc(var(--i)*70ms)}
.ready h1 .w>span{transform:none}
.reveal{opacity:0;transform:translateY(34px);transition:opacity .8s,transform .8s cubic-bezier(.2,.8,.2,1);transition-delay:calc(var(--d,0)*90ms)}
.reveal.in{opacity:1;transform:none}
.marquee{overflow:hidden;white-space:nowrap}
.marquee div{display:inline-block;animation:slide 28s linear infinite;padding:16px 0}
.marquee span{margin:0 26px}
@keyframes slide{to{transform:translateX(-50%)}}
section{padding:96px 0}
h2{font-family:var(--display);font-size:clamp(38px,5vw,66px);line-height:1;text-transform:uppercase}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:46px}
.head p:last-child{max-width:300px;font-size:14px;color:var(--muted)}
.quotes{display:grid;grid-template-columns:repeat(var(--qcols,3),1fr);gap:22px}
.quote{padding:28px;border:1px solid var(--line);display:flex;flex-direction:column;justify-content:space-between;gap:26px;transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s}
.quote:hover{transform:translateY(-6px) rotate(-.6deg);box-shadow:8px 8px 0 var(--accent)}
.quote p{font-size:21px;line-height:1.35;font-weight:700}
.quote cite{font-style:normal;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:11px;letter-spacing:1px;color:var(--muted);text-transform:uppercase}
.stars{letter-spacing:4px;color:var(--star,var(--accent))}
.visit-grid{display:grid;grid-template-columns:1fr 1fr;gap:80px}
address{font-style:normal;font-size:24px;line-height:1.45;font-weight:700;margin:22px 0 8px}
.bigphone{display:inline-block;font-family:var(--display);font-size:clamp(36px,5vw,58px);line-height:1.1;margin-top:26px}
table{border-collapse:collapse;width:100%;font-size:15px}
th,td{padding:13px 14px;border-bottom:1px solid var(--line)}th{text-align:left;font-weight:400}td{text-align:right;white-space:nowrap}
tr.today{background:var(--accent);color:var(--on-accent,#fff)}tr.today th,tr.today td{font-weight:800}
.tag{font:9px ui-monospace,Menlo,monospace;text-transform:uppercase;margin-left:10px;border:1px solid currentColor;padding:2px 5px;letter-spacing:1px}
.ph{display:block;width:100%;object-fit:cover;background:#2a2a2a;filter:saturate(.85) contrast(1.05);transition:filter .5s,transform .8s cubic-bezier(.2,.8,.2,1)}.phw{overflow:hidden}.phw:hover .ph,.card:hover .ph,.s:hover .ph{filter:none;transform:scale(1.05)}.proof{margin-top:18px;display:block}
.note{font-size:12px;color:var(--muted);margin-top:14px}
footer{padding:30px 0;border-top:1px solid var(--line);font-size:12px;color:var(--muted)}
footer .wrap{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap}
@media(max-width:900px){.wrap{width:calc(100% - 44px)}nav{display:none}.quotes{grid-template-columns:1fr}.visit-grid{grid-template-columns:1fr;gap:50px}.head{display:block}.head p:last-child{margin-top:16px;max-width:none}section{padding:64px 0}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*:before,*:after{animation:none!important;transition:none!important}.reveal{opacity:1;transform:none}h1 .w>span{transform:none}}
"""

JS = r"""
(()=>{
const reduce=matchMedia('(prefers-reduced-motion:reduce)').matches,root=document.documentElement;
// headline: split into words that rise in
document.querySelectorAll('h1').forEach(h=>{let i=0;const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/([ \n\t]+)/).forEach(t=>{if(!t.trim()){f.append(t);return}const w=document.createElement('span');w.className='w';const s=document.createElement('span');s.style.setProperty('--i',i++);s.textContent=t;w.append(s);f.append(w)});c.replaceWith(f)}else if(c.tagName!=='BR')walk(c)})};walk(h)});
requestAnimationFrame(()=>requestAnimationFrame(()=>root.classList.add('ready')));
// scroll reveals + counters
const count=el=>{const end=parseFloat(el.dataset.count),dec=(el.dataset.count.split('.')[1]||'').length;if(reduce){el.textContent=end.toFixed(dec);return}const t0=performance.now();const step=t=>{const p=Math.min((t-t0)/1400,1),e=1-Math.pow(1-p,3);el.textContent=(end*e).toFixed(dec);if(p<1)requestAnimationFrame(step)};requestAnimationFrame(step)};
const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;e.target.classList.add('in');e.target.querySelectorAll('[data-count]').forEach(count);if(e.target.dataset.count)count(e.target);io.unobserve(e.target)}),{threshold:.18});
document.querySelectorAll('.reveal,[data-count]:not(.reveal [data-count])').forEach(el=>io.observe(el));
// scroll + pointer driven motion
if(!reduce){let tick=false;const upd=()=>{root.style.setProperty('--scroll',scrollY);tick=false};addEventListener('scroll',()=>{if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});
addEventListener('pointermove',e=>{root.style.setProperty('--mx',(e.clientX/innerWidth-.5).toFixed(3));root.style.setProperty('--my',(e.clientY/innerHeight-.5).toFixed(3))},{passive:true})}
// hours: highlight today and show open/closed in shop's time zone
const p=Object.fromEntries(new Intl.DateTimeFormat('en-US',{weekday:'short',hour:'numeric',minute:'numeric',hour12:false,timeZone:'America/Los_Angeles'}).formatToParts(new Date()).map(x=>[x.type,x.value]));
const d=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(p.weekday),now=(+p.hour%24)+(+p.minute)/60,row=document.querySelector('tr[data-day="'+d+'"]');
if(row){row.classList.add('today');const t=document.createElement('span');t.className='tag';t.textContent='Today';row.querySelector('th').append(t);
const open=row.dataset.open&&now>=+row.dataset.open&&now<+row.dataset.close;document.querySelectorAll('.status').forEach(s=>{s.classList.toggle('open',!!open);s.querySelector('em').textContent=(open?'Open now · until '+row.dataset.label:'Closed right now')+' · '+s.querySelector('em').textContent})}
})();
"""

def hours_table(rows):
    # rows: list of (dayIndex, name, open, close, label) ; open None => closed
    out = ['<table><caption class="mono" style="text-align:left;padding-bottom:14px">Hours</caption>']
    for d, name, o, c, label in rows:
        if o is None:
            out.append(f'<tr data-day="{d}"><th scope="row">{name}</th><td>Closed</td></tr>')
        else:
            out.append(f'<tr data-day="{d}" data-open="{o}" data-close="{c}" data-label="{label.split("–")[1].strip()}"><th scope="row">{name}</th><td>{label}</td></tr>')
    out.append('</table>')
    return ''.join(out)

DAYS = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
def week(spec):
    order = [1,2,3,4,5,6,0]
    return hours_table([(d, DAYS[d], *spec[d]) for d in order])

def quotes(items):
    return ''.join(f'<blockquote class="quote reveal" style="--d:{i}"><div><div class="stars" aria-hidden="true">★★★★★</div><p style="margin-top:14px">“{q}”</p></div><cite>{who}</cite></blockquote>' for i,(q,who) in enumerate(items))

def marquee(items, sep):
    row = ''.join(f'<span>{t}</span><span aria-hidden="true">{sep}</span>' for t in items)
    return f'<div class="marquee" aria-hidden="true"><div>{row}{row}</div></div>'

def page(title, desc, theme, css, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="{theme}">
<meta name="description" content="{desc}">
<title>{title}</title>
<style>{BASE_CSS}{css}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{body}
<script>{JS}</script>
</body>
</html>
'''

def U(pid, w, h, q=70):
    return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}&h={h}&q={q}"
P = dict(hands='1619642751034-765dfdf7c58e', oil='1487754180451-c456f719a1fc', bay='1686082307524-c89fb0bfadde', lift='1791419542289-693087bd1044',
 mount='1645445522156-9ac06bc7a767', tread='1763584357116-31a7d0bf389d', used='1527266258038-6ae3e089a609', flat='1601739722627-f00a99138ea1', alloy='1444947295498-07f60c19a4ff',
 piles='1578844251758-2f71da64c96f', wall='1786489623872-2ebdfe51297c', store='1675034743372-672c3c3f8377',
 shop='1792793176006-a7b35e29c7e1', cam='1429772011165-0c2e054367b8', gears='1614447428943-52ec0bdbc7aa', vent='1542399204-b8dd4af5113d', inspect='1557411255-28ebcc0fdd54', diag='1625047509248-ec889cbff17f')
DISCLAIMER = 'Concept website by Phan-Rodriguez LLC. Not the official site of this business. Details and reviews come from public listings; reviews are quoted from the sources named. Photos are stock images from Unsplash, not photos of this shop.'

# ───────────────────────── TRI AUTO ─────────────────────────
TRI_LOGO = '''<svg viewBox="0 0 330 60" role="img" aria-label="Tri-Auto" {attr}><text x="0" y="47" font-family="'Arial Black',Impact,Arial,sans-serif" font-weight="900" font-style="italic" font-size="50" letter-spacing="-1" fill="currentColor">TRI-AUTO</text><g transform="skewX(-18)"><rect x="286" y="8" width="11" height="41" fill="#d7261e"/><rect x="301" y="8" width="11" height="41" fill="#f26b1d"/><rect x="316" y="8" width="11" height="41" fill="#f7b51c"/></g></svg>'''

tri_css = """
:root{--bg:#efe6d3;--ink:#141414;--accent:#d7261e;--a2:#f26b1d;--a3:#f7b51c;--muted:#5d564a;--line:#c9bda3;--display:'Arial Black',Impact,'Arial Narrow',sans-serif;--on-accent:#fff;--focus:#141414}
header{border-bottom:2px solid var(--ink)}
.hero{position:relative;overflow:hidden;border-bottom:2px solid var(--ink);background:linear-gradient(112deg,#f6eedd 0,#efe6d3 38%,#e2d6bd 100%)}.hero:after{content:'';position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(112deg,transparent 0 52%,#3b2a1422 52.2%,#3b2a1400 78%)}
.hero .wrap{position:relative;z-index:2;padding:90px 0 110px}
h1{font-family:var(--display);font-style:italic;font-size:clamp(52px,7.6vw,104px);line-height:.9;letter-spacing:-.04em;text-transform:uppercase;margin-top:26px}
h1 em{font-style:italic;color:var(--accent)}
.lede{max-width:520px;font-size:19px;margin-top:30px}
.stripes{position:absolute;inset:0;z-index:1;pointer-events:none}
.hero-photo{position:absolute;top:0;right:0;bottom:0;width:44%;z-index:1;background:#2a1c12 var(--img) center/cover;clip-path:polygon(32% 0,100% 0,100% 100%,0 100%)}.hero-photo:after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,#1a0f0888,#0000 45%)}
.stripes{z-index:2}.stripes i{position:absolute;top:-20%;height:140%;width:2.6vw;transform:skewX(-18deg) translateY(calc(var(--scroll,0)*-.12px));right:calc(var(--n)*3.6vw + 36vw);background:linear-gradient(90deg,#fff3 0,#fff0 18%,#0000 70%,#0003 100%),var(--c);box-shadow:14px 0 30px -8px #2a160055;animation:drop 1.1s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--n)*120ms + 300ms);opacity:.95}
@keyframes drop{from{clip-path:inset(0 0 100% 0)}to{clip-path:inset(0)}}
.gauge{position:absolute;right:6vw;bottom:46px;z-index:3;box-shadow:0 24px 40px -12px #000a,inset 0 1px 0 #fff3;background:linear-gradient(160deg,#2a2a2a,#0c0c0c);color:var(--bg);padding:20px 26px;transform:rotate(-4deg) translate(calc(var(--mx,0)*-18px),calc(var(--my,0)*-18px));transition:transform .2s}
.gauge strong{font-family:var(--display);font-style:italic;font-size:64px;line-height:1;display:block}
.marquee{background:var(--ink);color:var(--bg);font-family:var(--display);font-style:italic;text-transform:uppercase;font-size:20px}
.marquee span:nth-child(even){color:var(--a3)}
.makes{border-top:2px solid var(--ink)}
.make{display:grid;grid-template-columns:90px 1fr auto;align-items:center;gap:24px;border-bottom:2px solid var(--ink);padding:26px 0;position:relative;overflow:hidden}
.make:before{content:"";position:absolute;inset:0;background:var(--c);transform:translateX(-101%) skewX(-18deg);transform-origin:left;transition:transform .55s cubic-bezier(.2,.8,.2,1);z-index:0}
.make:hover:before{transform:translateX(-12%) skewX(-18deg) scaleX(1.4)}
.make>*{position:relative;z-index:1}
.make h3{font-family:var(--display);font-style:italic;font-size:clamp(44px,9vw,128px);line-height:.9;letter-spacing:-.04em;text-transform:uppercase;transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.make:hover h3{transform:translateX(26px)}
.make p{max-width:260px;font-size:14px;text-align:right}
.why{background:var(--ink);color:var(--bg)}.why .head p:last-child{color:#b9b09c}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:1px solid #444}
.card{background:linear-gradient(180deg,#1d1d1d,#141414);padding:34px 28px 40px;border-right:1px solid #444;border-top:8px solid var(--c)}
.card:last-child{border-right:0}.card .phw{margin:-34px -28px 26px}.card .ph{height:210px}.card h3{font-family:var(--display);font-style:italic;text-transform:uppercase;font-size:26px;line-height:1.05;margin:18px 0 14px}
.card p{color:#cfc6b2;font-size:15px}
.quote{background:#fff8ea;border:2px solid var(--ink);box-shadow:0 18px 30px -20px #3b2a14}
.bigquote{font-family:var(--display);font-style:italic;text-transform:uppercase;font-size:clamp(34px,6.4vw,92px);line-height:.95;letter-spacing:-.03em;margin-bottom:54px}
.bigquote cite{display:block;font:700 12px ui-monospace,Menlo,monospace;letter-spacing:2px;margin-top:20px;color:var(--muted)}
.visit{border-top:2px solid var(--ink)}
@media(max-width:900px){.cards{grid-template-columns:1fr}.card{border-right:0}.card h3{margin-top:28px}.make{grid-template-columns:1fr}.make p{text-align:left}.gauge{position:relative;right:auto;bottom:auto;display:inline-block;margin:0 22px 40px}.stripes{display:none}.hero-photo{position:relative;width:100%;height:240px;clip-path:polygon(0 14%,100% 0,100% 100%,0 100%);margin-top:-10px}.gauge{margin-top:-70px!important;z-index:4}.hero .wrap{padding:60px 0 50px}}
"""

tri_body = f'''
<header><div class="wrap"><a href="#" style="width:190px">{TRI_LOGO.format(attr='')}</a>
<nav aria-label="Main"><a href="#makes">What we fix</a><a href="#why">Why Tri Auto</a><a href="#reviews">Reviews</a><a href="#visit">Visit</a></nav>
<a class="phone" href="tel:+19094656422">(909) 465-6422</a></div></header>
<main id="main">
<section class="hero" style="padding:0">
<div class="hero-photo" role="img" aria-label="Mechanic's hands working on an engine with a wrench" style="--img:url({U(P['hands'],1100,1000)})"></div>
<div class="stripes" aria-hidden="true"><i style="--n:2;--c:#d7261e"></i><i style="--n:1;--c:#f26b1d"></i><i style="--n:0;--c:#f7b51c"></i></div>
<div class="wrap">
<p class="mono status"><b></b><em style="font-style:normal">Chino, California</em></p>
<h1>Bye-bye,<br><em>dealership.</em></h1>
<p class="lede">Tri Auto is Chino's independent shop for <strong>Toyota, Honda and Lexus</strong>. Three makes, known inside out, at prices customers say run far below the dealer's.</p>
<div class="actions"><a class="btn" href="tel:+19094656422" style="background:var(--ink);color:var(--bg);--btn-fill:var(--accent);--btn-hover:#fff">Call Danny's shop <i>→</i></a><a class="btn" href="#visit">Hours &amp; directions <i>↓</i></a></div>
</div>
<div class="gauge"><span class="mono">Google rating</span><strong><span data-count="4.9">4.9</span>★</strong><span class="mono"><span data-count="333">333</span> reviews</span></div>
</section>
{marquee(['Toyota','Honda','Lexus','Honest work','Fair prices','Chino, CA','Mon–Fri 8 to 6'],'///')}
<section id="makes"><div class="wrap">
<div class="head"><div><p class="mono" style="color:var(--accent);margin-bottom:14px">01 — What we fix</p><h2 style="font-style:italic">Three makes.<br>Nothing else.</h2></div><p>We don't work on everything. We work on these three, every day. That focus is the whole idea behind the name.</p></div>
<div class="makes">
<div class="make reveal" style="--c:#d7261e"><span class="mono">01</span><h3>Toyota</h3><p>Camry, Corolla, Tacoma, RAV4, Prius and the rest of the family.</p></div>
<div class="make reveal" style="--c:#f26b1d;--d:1"><span class="mono">02</span><h3>Honda</h3><p>Civic, Accord, CR-V, Odyssey, Pilot. Daily drivers kept on the road.</p></div>
<div class="make reveal" style="--c:#f7b51c;--d:2"><span class="mono">03</span><h3>Lexus</h3><p>Dealer-level know-how for your ES, RX or IS, without the dealer invoice.</p></div>
</div></div></section>
<section class="why" id="why"><div class="wrap">
<div class="head"><div><p class="mono" style="color:var(--a3);margin-bottom:14px">02 — Why Tri Auto</p><h2 style="font-style:italic">What people<br>come in for.</h2></div><p>Taken from what customers say in their reviews, not from a sales brochure.</p></div>
<div class="cards">
<div class="card reveal" style="--c:#d7261e"><div class="phw"><img class="ph" loading="lazy" alt="Fresh oil being poured into an engine" src="{U(P['oil'],700,420)}"></div><span class="mono">A</span><h3>Maintenance &amp; oil changes</h3><p>Routine service done right and done the same day. One reviewer had several services finished in a few hours.</p></div>
<div class="card reveal" style="--c:#f26b1d;--d:1"><div class="phw"><img class="ph" loading="lazy" alt="Open engine bay" src="{U(P['bay'],700,420)}"></div><span class="mono">B</span><h3>Diagnosis &amp; repair</h3><p>A straight answer about what's wrong, what it costs, and what can wait.</p></div>
<div class="card reveal" style="--c:#f7b51c;--d:2"><div class="phw"><img class="ph" loading="lazy" alt="Car raised on a shop lift" src="{U(P['lift'],700,420)}"></div><span class="mono">C</span><h3>A second opinion</h3><p>Got a dealer quote that stings? Bring it in. One customer says Danny saved her almost $600.</p></div>
</div></div></section>
<section id="reviews"><div class="wrap">
<p class="mono" style="color:var(--accent);margin-bottom:20px">03 — Reviews</p>
<blockquote class="bigquote reveal">“Honest, timely, friendly, <span style="color:var(--accent)">and affordable!</span>”<cite>Heidi Todd Broberg · Facebook review</cite></blockquote>
<div class="quotes">{quotes([('Bye, bye dealerships!','Kristy Hudson · Facebook review'),('Very good service for reasonable price.','Disha Desai · Facebook recommendation'),('Trust worthy, honest and very reasonable.','CeeCee Gaatogo · Facebook review')])}</div>
</div></section>
<section class="visit" id="visit"><div class="wrap visit-grid">
<div class="reveal"><p class="mono" style="color:var(--accent)">04 — Visit</p><h2 style="font-style:italic;margin-top:14px">Schaefer Ave,<br>Chino.</h2>
<address>6108 Schaefer Ave<br>Chino, CA 91710</address><p style="color:var(--muted)">Stucco building with the Tri-Auto sign and the flag out front. Plenty of parking on the lot.</p>
<a class="bigphone" href="tel:+19094656422" style="font-style:italic">(909) 465-6422</a>
<div class="actions"><a class="btn" href="https://www.google.com/maps/search/?api=1&query=Tri+Auto+6108+Schaefer+Ave+Chino+CA+91710" rel="noopener">Get directions <i>→</i></a></div></div>
<div class="reveal" style="--d:1">{week({1:(8,18,'8:00 AM – 6:00 PM'),2:(8,18,'8:00 AM – 6:00 PM'),3:(8,18,'8:00 AM – 6:00 PM'),4:(8,18,'8:00 AM – 6:00 PM'),5:(8,18,'8:00 AM – 6:00 PM'),6:(None,None,''),0:(None,None,'')})}<p class="note">Hours from public listings. Call ahead to confirm.</p></div>
</div></section>
</main>
<footer><div class="wrap"><strong>Tri Auto · Chino, CA</strong><span>{DISCLAIMER}</span></div></footer>
'''

# ───────────────────────── A C TIRES ─────────────────────────
def _rot(el, step, start=0):
    return ''.join(el.replace('ROT', f'rotate({a} 200 200)') for a in range(start, 360+start, step))
TIRE = '''<svg viewBox="0 0 400 430" aria-hidden="true"><defs>
<radialGradient id="rub" cx="50%" cy="50%" r="50%"><stop offset=".56" stop-color="#050505"/><stop offset=".66" stop-color="#1d1d1f"/><stop offset=".8" stop-color="#2b2b2e"/><stop offset=".9" stop-color="#151516"/><stop offset="1" stop-color="#040404"/></radialGradient>
<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".34"/><stop offset=".32" stop-color="#fff" stop-opacity="0"/><stop offset=".72" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></linearGradient>
<linearGradient id="alloy" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fdfdfd"/><stop offset=".35" stop-color="#b9bec6"/><stop offset=".55" stop-color="#eef0f3"/><stop offset=".8" stop-color="#8b9099"/><stop offset="1" stop-color="#d7dadf"/></linearGradient>
<linearGradient id="spoke" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7d828b"/><stop offset=".3" stop-color="#f7f8fa"/><stop offset=".62" stop-color="#c3c7ce"/><stop offset="1" stop-color="#666a72"/></linearGradient>
<radialGradient id="disc" cx="50%" cy="50%" r="50%"><stop offset=".3" stop-color="#55585e"/><stop offset=".5" stop-color="#a9adb3"/><stop offset=".78" stop-color="#7c8086"/><stop offset="1" stop-color="#3a3c40"/></radialGradient>
<radialGradient id="well" cx="50%" cy="50%" r="50%"><stop offset=".7" stop-color="#101113"/><stop offset="1" stop-color="#3b3d42"/></radialGradient>
<radialGradient id="gs" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#000" stop-opacity=".6"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" result="t"/><feColorMatrix in="t" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .09 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>
<path id="arc" d="M200 200 m-150 0 a150 150 0 1 1 300 0 a150 150 0 1 1 -300 0"/></defs>
<ellipse cx="200" cy="405" rx="170" ry="18" fill="url(#gs)"/>
<g class="spin"><circle cx="200" cy="200" r="196" fill="url(#rub)"/>
<circle cx="200" cy="200" r="188" fill="none" stroke="#0a0a0a" stroke-width="16" stroke-dasharray="10.5 4.2"/>
<circle cx="200" cy="200" r="178" fill="none" stroke="#000" stroke-width="2" opacity=".8"/>
<circle cx="200" cy="200" r="163" fill="none" stroke="#3a3a3d" stroke-width="1"/><circle cx="200" cy="200" r="136" fill="none" stroke="#3a3a3d" stroke-width="1"/>
<text font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="15" letter-spacing="5" fill="#3d3d41"><textPath href="#arc" startOffset="2%">A C TIRES &amp; WHEELS</textPath><textPath href="#arc" startOffset="52%">ONTARIO · CALIFORNIA</textPath></text>
<circle cx="200" cy="200" r="196" fill="#fff" filter="url(#grain)"/>
<circle cx="200" cy="200" r="126" fill="url(#alloy)"/><circle cx="200" cy="200" r="117" fill="url(#well)"/>
<circle cx="200" cy="200" r="98" fill="url(#disc)"/>''' + _rot('<circle cx="200" cy="128" r="2.6" fill="#2c2d30" transform="ROT"/>', 20) + '''<path d="M286 150 a100 100 0 0 1 12 62 l-24 -4 a76 76 0 0 0 -9 -46z" fill="#c4161c"/><path d="M288 156 a96 96 0 0 1 8 48" fill="none" stroke="#ff6a5f" stroke-width="2" opacity=".7"/>''' + _rot('<g transform="ROT"><path d="M186 190 L176 86 Q200 78 224 86 L214 190 Z" fill="url(#spoke)"/><path d="M196 186 L192 96 Q200 93 208 96 L204 186 Z" fill="#2a2c30" opacity=".5" filter="url(#soft)"/></g>', 72) + '''<circle cx="200" cy="200" r="126" fill="none" stroke="url(#alloy)" stroke-width="9"/><circle cx="200" cy="200" r="121" fill="none" stroke="#000" stroke-width="1" opacity=".35"/>
<circle cx="200" cy="200" r="40" fill="url(#alloy)"/>''' + _rot('<g transform="ROT"><circle cx="200" cy="174" r="6.5" fill="#2b2d31"/><circle cx="199" cy="173" r="4" fill="#9a9fa8"/></g>', 72, 36) + '''<circle cx="200" cy="200" r="15" fill="#15161a"/><circle cx="200" cy="200" r="15" fill="none" stroke="#d7dadf" stroke-width="1.5"/></g>
<circle cx="200" cy="200" r="196" fill="url(#sheen)" style="mix-blend-mode:soft-light"/><circle cx="200" cy="200" r="196" fill="url(#sheen)" opacity=".45"/>
</svg>'''

ac_css = """
:root{--bg:#1f3fae;--ink:#fff;--accent:#d62b1f;--muted:#c5d0f5;--line:#4a66c9;--display:Poster,Impact,'Arial Black',sans-serif;--star:#ffd23c;--focus:#ffd23c;--btn-fill:#fff;--btn-hover:#1f3fae}
body{background:var(--bg)}.hero{background:radial-gradient(120% 90% at 78% 40%,#3558d6 0,#1f3fae 45%,#152c7c 100%)}
.sign{display:inline-block;background:#fdfbf4;color:var(--accent);font-family:var(--display);font-size:30px;letter-spacing:1px;padding:4px 16px 2px;line-height:1.2;text-transform:uppercase;box-shadow:0 3px 0 #0003}
.sign small{color:#1f3fae;font-size:.7em}
.hero{padding:70px 0 0;position:relative;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:30px;align-items:center}
h1{font-family:var(--display);font-weight:400;font-size:clamp(46px,6.2vw,88px);line-height:.95;text-transform:uppercase;margin-top:24px;letter-spacing:.005em}
h1 em{font-style:normal;background:#fdfbf4;color:var(--accent);padding:.04em .14em 0;display:inline-block;transform:rotate(-2deg);margin-top:.12em}
.lede{font-size:19px;max-width:500px;margin-top:28px;color:#e6ebff}
.tire{position:relative;transform:translateX(18%)}
.tire .spin{transform-origin:200px 200px;transform:rotate(calc(var(--scroll,0)*.22deg));}
.tire img{display:block;width:100%;aspect-ratio:1;object-fit:cover;border-radius:50%;border:12px solid #fdfbf4;background:#0e1c55;box-shadow:0 34px 50px -10px #000a,0 0 0 2px #0003;animation:roll 1.4s cubic-bezier(.2,.8,.2,1) both}
@keyframes roll{from{transform:translateX(120%) rotate(200deg)}to{transform:none}}
.late{position:absolute;left:-8%;bottom:12%;box-shadow:0 10px 24px #0006;background:#ffd23c;color:#111;width:128px;height:128px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:900;font-size:12px;line-height:1.2;text-align:center;transform:rotate(-12deg);animation:pop .6s 1.2s cubic-bezier(.3,1.6,.5,1) both}
.late strong{font-family:var(--display);font-size:34px;font-weight:400;line-height:1}
@keyframes pop{from{transform:scale(0) rotate(40deg)}to{transform:scale(1) rotate(-12deg)}}
.marquee{background:#fdfbf4;color:var(--accent);font-family:var(--display);font-size:26px;text-transform:uppercase;margin-top:70px;transform:rotate(-1.2deg) scale(1.03);box-shadow:0 6px 0 #0003}
.marquee span:nth-child(even){color:#1f3fae}
.services{background:#fdfbf4;color:#141a33;margin-top:-10px;padding-top:120px}
.services h2{color:var(--accent)}.services .head p:last-child{color:#4b5270}
.board{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.item{min-width:0;background:linear-gradient(170deg,#1f3faeb8 0,#12297ef2 62%),var(--img) center/cover #18318c;box-shadow:0 14px 26px -14px #0b1a55;color:#fff;padding:22px 20px 26px;min-height:230px;display:flex;flex-direction:column;justify-content:space-between;transition:transform .35s cubic-bezier(.2,.8,.2,1),background .3s}
.item:hover{transform:translateY(-10px) rotate(-1.5deg);background:linear-gradient(170deg,#d62b1f99 0,#8f120cf0 62%),var(--img) center/cover #a81710}.item{min-height:300px!important}.strip{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:6px;background:#fdfbf4;padding:0 0 6px}.strip .ph{height:clamp(160px,24vw,340px)}.proof{color:#e6ebff}
.item h3{font-family:var(--display);font-weight:400;font-size:30px;line-height:1;text-transform:uppercase}
.item p{font-size:13.5px;color:#dfe5ff}
.item svg{width:44px;height:44px;transition:transform .8s}.item:hover svg{transform:rotate(180deg)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);border-top:3px solid #fff;border-bottom:3px solid #fff;margin-bottom:60px}
.stat{padding:30px 24px;border-right:3px solid #fff}.stat:last-child{border:0}
.stat strong{font-family:var(--display);font-weight:400;font-size:clamp(54px,8vw,104px);line-height:1;display:block}
.quote{background:#fdfbf4;color:#141a33;border:0;--qm:#4b5270}.quote cite{color:#4b5270}.quote .stars{color:var(--accent)}
.quote:hover{box-shadow:8px 8px 0 #ffd23c}
.visit{background:#16307f}.visit .btn{--btn-hover:#16307f}
tr.today{background:#fdfbf4;color:var(--accent)}
@media(max-width:900px){.board{grid-template-columns:repeat(2,minmax(0,1fr))!important}.item h3{font-size:24px}.hero-grid{grid-template-columns:1fr}.tire{width:min(300px,82%);margin:26px auto 0;transform:none}.late{left:auto;right:-2%;bottom:2%}.board{grid-template-columns:1fr 1fr}.item{min-height:180px}.stats{grid-template-columns:1fr}.stat{border-right:0;border-bottom:3px solid #fff}.sign{font-size:22px}}
"""

ICON = '<svg viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="19" fill="none" stroke="currentColor" stroke-width="5"/><circle cx="22" cy="22" r="6" fill="currentColor"/><path d="M22 3v10M22 31v10M3 22h10M31 22h10" stroke="currentColor" stroke-width="3"/></svg>'
ac_items = [('tread','New tires','Fresh rubber in the sizes people around here actually drive.'),('used','Used tires','Good used tires for when the budget says “not today” to a full new set.'),('flat','Flat repair','Nail in the tread? In and out fast, weekends included.'),('mount','Mount &amp; balance','Bought tires elsewhere? We’ll mount and balance them.'),('alloy','Wheels','It’s on the sign: A C Tires &amp; Wheels.')]
ac_body = f'''
<header><div class="wrap"><a href="#" class="sign" aria-label="A C Tires and Wheels">AC-Tires <small>&amp;</small> Wheels</a>
<nav aria-label="Main"><a href="#services">Services</a><a href="#reviews">Reviews</a><a href="#visit">Hours &amp; location</a></nav>
<a class="phone" href="tel:+19093914636">(909) 391-4636</a></div></header>
<main id="main">
<section class="hero"><div class="wrap hero-grid">
<div><p class="mono status"><b></b><em style="font-style:normal">Ontario, California</em></p>
<h1>Flat at 7&nbsp;PM?<br><em>We're still open.</em></h1>
<p class="lede">New and used tires, flat repair and mount-and-balance at the blue shop on California Street. Open until 8 on weeknights and <strong>open every Sunday</strong>.</p>
<div class="actions"><a class="btn" href="tel:+19093914636" style="background:#fdfbf4;color:var(--accent);border-color:#fdfbf4;--btn-fill:#ffd23c;--btn-hover:#111">Call (909) 391-4636 <i>→</i></a><a class="btn" href="#visit">Find the blue building <i>↓</i></a></div><span class="mono proof">★ 4.4 on Google · 322 reviews</span></div>
<div class="tire"><img alt="Gloved hands fitting a tire onto a car" src="{U(P['mount'],900,900)}"><div class="late"><span>OPEN TIL</span><strong>8 PM</strong><span>MON–FRI</span></div></div>
</div>
{marquee(['New tires','Used tires','Flat repair','Mount &amp; balance','Open 7 days','Open late'],'●')}
</section>
<section class="services" id="services"><div class="wrap">
<div class="head"><div><p class="mono" style="margin-bottom:14px">What we do</p><h2>Tires. That's it.<br>That's the shop.</h2></div><p>No waiting-room upsell. Pull in, tell us what you need, and get back on the road.</p></div>
<div class="board">{''.join(f'<div class="item reveal" style="--d:{i};--img:url({U(P[k],520,640,60)})">{ICON}<div><h3>{t}</h3><p style="margin-top:10px">{d}</p></div></div>' for i,(k,t,d) in enumerate(ac_items))}</div>
</div></section>
<div class="strip" aria-hidden="true"><div class="phw"><img class="ph" loading="lazy" alt="" src="{U(P['wall'],1100,600)}"></div><div class="phw"><img class="ph" loading="lazy" alt="" src="{U(P['piles'],800,600)}"></div><div class="phw"><img class="ph" loading="lazy" alt="" src="{U(P['store'],800,600)}"></div></div>
<section id="reviews"><div class="wrap">
<div class="stats reveal">
<div class="stat"><strong><span data-count="4.4">4.4</span>★</strong><span class="mono">Google rating</span></div>
<div class="stat"><strong data-count="322">322</strong><span class="mono">Google reviews</span></div>
<div class="stat"><strong data-count="7">7</strong><span class="mono">Days a week</span></div></div>
<div class="head"><div><p class="mono" style="margin-bottom:14px;color:#ffd23c">From Yelp</p><h2>Quick, easy,<br>straight forward.</h2></div><p>What drivers wrote after pulling in with a flat.</p></div>
<div class="quotes" style="--qcols:2">{quotes([('…the dudes here are super nice and straight forward','Sam R. · Yelp · Aug 2025 · flat fixed on a Sunday'),('Super quick and easy.','Kristina G. · Yelp · Aug 2024 · flat repair')])}</div>
</div></section>
<section class="visit" id="visit"><div class="wrap visit-grid">
<div class="reveal"><p class="mono" style="color:#ffd23c">Find us</p><h2 style="margin-top:14px">Look for the<br>blue building.</h2>
<address>301 W California St<br>Ontario, CA 91762</address><p style="color:var(--muted)">Royal blue walls, red-and-white hand-painted sign, tires stacked out front. You can't miss it.</p>
<a class="bigphone" href="tel:+19093914636">(909) 391-4636</a>
<div class="actions"><a class="btn" href="https://www.google.com/maps/search/?api=1&query=A+C+Tires+301+W+California+St+Ontario+CA+91762" rel="noopener">Get directions <i>→</i></a></div></div>
<div class="reveal" style="--d:1">{week({1:(8,20,'8:00 AM – 8:00 PM'),2:(8,20,'8:00 AM – 8:00 PM'),3:(8,20,'8:00 AM – 8:00 PM'),4:(8,20,'8:00 AM – 8:00 PM'),5:(8,20,'8:00 AM – 8:00 PM'),6:(8,19,'8:00 AM – 7:00 PM'),0:(8,18,'8:00 AM – 6:00 PM')})}<p class="note">Hours from public listings. Call ahead to confirm.</p></div>
</div></section>
</main>
<footer><div class="wrap"><strong>A C Tires · Ontario, CA</strong><span>{DISCLAIMER}</span></div></footer>
'''

# ───────────────────────── MORENO'S ─────────────────────────
mo_css = """
:root{--bg:#f4f1ea;--ink:#16171b;--accent:#c81f25;--yellow:#ffd21f;--blue:#1d4fb8;--muted:#5c5e66;--line:#d3cec2;--display:Poster,Impact,'Arial Black',sans-serif;--focus:#1d4fb8}
body:before{content:"";display:block;height:14px;background:var(--accent)}
.logo{font-family:var(--display);font-size:30px;line-height:1;text-transform:uppercase;letter-spacing:.5px}
.logo span{color:var(--accent)}.logo small{display:block;font:700 10px ui-monospace,Menlo,monospace;letter-spacing:3px;margin-top:4px;color:var(--muted)}
.hero{padding:64px 0 0}
h1{font-family:var(--display);font-weight:400;font-size:clamp(56px,9.6vw,148px);line-height:.92;text-transform:uppercase;margin-top:22px}
h1 em{font-style:normal;color:var(--accent)}
.hero-row{display:flex;justify-content:space-between;align-items:flex-end;gap:40px;margin-top:30px;flex-wrap:wrap}
.lede{font-size:19px;max-width:520px}
.shop{overflow:hidden;margin-top:60px;position:relative;border-top:16px solid var(--accent);background:linear-gradient(180deg,#000a 0,#0003 38%,#0000 60%,#0006 100%),var(--img) center 60%/cover #1b1c20;padding-bottom:clamp(170px,27vw,400px)}
.bays{display:grid;grid-template-columns:repeat(3,1fr);gap:3%;padding:0 3%}
.bay{position:relative;padding-top:26px;display:flex;flex-direction:column}
.banner{display:block;position:relative;font-family:var(--display);text-transform:uppercase;font-size:clamp(15px,2.4vw,34px);line-height:1.05;padding:12px 14px;text-align:center;transform-origin:top;animation:unfurl .8s cubic-bezier(.3,1.4,.5,1) both;animation-delay:calc(var(--n)*160ms + 500ms);box-shadow:0 10px 14px -6px #0007,inset 0 0 0 1px #0002;background-image:linear-gradient(90deg,#0000 0,#fff3 12%,#0001 30%,#fff2 52%,#0002 74%,#fff2 90%,#0001 100%)}
.banner:before,.banner:after{content:'';position:absolute;top:5px;width:7px;height:7px;border-radius:50%;background:radial-gradient(#111 0 35%,#d9d9d9 40% 100%);box-shadow:0 1px 1px #0006}
.banner:before{left:6px}.banner:after{right:6px}
@keyframes unfurl{from{transform:scaleY(0) rotate(-3deg)}to{transform:none}}
.b-y{background-color:var(--yellow);color:#111}.b-r{background-color:var(--accent);color:#fff}.b-b{background-color:#fafafa;color:var(--blue)}
.marquee{background:var(--ink);color:#fff;font-family:var(--display);font-size:22px;text-transform:uppercase}
.marquee span:nth-child(4n+1){color:var(--yellow)}
.svc{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.s{padding:0;border:2px solid var(--ink);background:#fff;box-shadow:0 16px 26px -18px #000;transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s}
.s:hover{transform:translate(-5px,-5px);box-shadow:10px 10px 0 var(--ink)}
.s h3{background-image:linear-gradient(90deg,#0000 0,#fff3 14%,#0001 34%,#fff2 56%,#0002 78%,#fff2 100%);font-family:var(--display);font-weight:400;text-transform:uppercase;font-size:28px;line-height:1.05;padding:14px 18px;border-bottom:2px solid var(--ink)}
.s .ph{height:170px;border-bottom:2px solid var(--ink)}.s p{padding:18px;font-size:14.5px;color:#3e4047}.s .mono{display:block;padding:0 18px 18px;color:var(--muted);font-size:10px}
.family{background:radial-gradient(90% 120% at 20% 40%,#e02b31 0,#c81f25 45%,#8e1318 100%);color:#fff}.year{text-shadow:0 2px 0 #b98f00,0 18px 30px #5a0a0d}
.fam-grid{display:grid;grid-template-columns:auto 1fr;gap:60px;align-items:center}
.year{font-family:var(--display);font-size:clamp(120px,24vw,340px);line-height:.8;color:var(--yellow);transform:translateX(calc(var(--mx,0)*-20px))}
.family p{font-size:22px;line-height:1.45;max-width:520px}
.nums{display:flex;gap:44px;margin-top:34px;flex-wrap:wrap}.nums strong{font-family:var(--display);font-weight:400;font-size:54px;line-height:1;display:block}
.quote{background:#fff;border:2px solid var(--ink)}.quote:hover{box-shadow:8px 8px 0 var(--yellow)}
.visit{background:var(--ink);color:#fff;--line:#3b3d45;--muted:#a9abb3}.visit .btn{--btn-fill:#fff;--btn-hover:#16171b}
tr.today{background:var(--yellow);color:#111}
@media(max-width:900px){.svc{grid-template-columns:1fr}.fam-grid{grid-template-columns:1fr;gap:20px}.bays{gap:2%;padding:0 2%}}
"""
mo_svc = [('cam','b-y','Engine repair','From check-engine lights to major engine work. The shop is known for tracking down the hard-to-diagnose problems.','On the banner'),
('alloy','b-r','Computer alignment','Computerized wheel alignment, including taller vehicles other shops turn away.','On the banner'),
('vent','b-b','A/C complete service','Air conditioning diagnosis, repair and recharge. This is the Inland Empire. You need it.','On the banner'),
('gears','b-y','Transmission rebuild','Transmission service and full rebuilds done in-house.','On the banner'),
('inspect','b-r','Vehicle inspections','Vehicle inspections, a favorite of local rideshare drivers according to reviews.','From reviews'),
('diag','b-b','Diagnostics','A scan, a straight explanation and a fair price before any work starts.','From reviews')]
mo_body = f'''
<header><div class="wrap"><a href="#" class="logo" aria-label="Moreno's Auto Repair">Moreno<span>'</span>s<small>AUTO REPAIR · ONTARIO</small></a>
<nav aria-label="Main"><a href="#services">Services</a><a href="#family">Our shop</a><a href="#reviews">Reviews</a><a href="#visit">Visit</a></nav>
<a class="phone" href="tel:+19094186955">(909) 418-6955</a></div></header>
<main id="main">
<section class="hero">
<div class="wrap"><p class="mono status"><b></b><em style="font-style:normal">Holt Blvd · Ontario, CA</em></p>
<h1>If it's on the banner,<br><em>we fix it.</em></h1>
<div class="hero-row"><p class="lede">Engines, transmissions, alignments and A/C under one roof. Moreno's is a <strong>family-owned shop on Holt Boulevard</strong>, fixing Ontario's cars since 2009.</p>
<div class="actions" style="margin:0"><a class="btn" href="tel:+19094186955" style="background:var(--accent);color:#fff;border-color:var(--accent)">Call the shop <i>→</i></a><a class="btn" href="#services">See services <i>↓</i></a><span class="mono" style="flex-basis:100%;text-align:right">★ 4.7 on Google · 284 reviews</span></div></div></div>
<div class="shop" role="img" aria-label="Auto repair shop floor with red vehicle lifts" style="--img:url({U(P['shop'],1800,900)})"><div class="bays">
<div class="bay"><span class="banner b-y" style="--n:0">Engine Repair</span><span class="banner b-r" style="--n:1;margin-top:4px">Computer Alignment</span></div>
<div class="bay"><span class="banner b-b" style="--n:2">Air Condition<br>Complete Service</span></div>
<div class="bay"><span class="banner b-y" style="--n:3">Transmission Rebuild</span><span class="banner b-b" style="--n:4;margin-top:4px">Moreno's Auto Repair</span></div>
</div></div>
{marquee(['Engine repair','Computer alignment','A/C service','Transmission rebuild','Family owned','Since 2009'],'★')}
</section>
<section id="services"><div class="wrap">
<div class="head"><div><p class="mono" style="color:var(--accent);margin-bottom:14px">Services</p><h2>Read the wall.<br>That's the menu.</h2></div><p>The banners over our bay doors say what we do. Here's the same list, a little bigger.</p></div>
<div class="svc">{''.join(f'<div class="s reveal" style="--d:{i%3}"><h3 class="{c}">{t}</h3><div class="phw"><img class="ph" loading="lazy" alt="" src="{U(P[k],700,360,60)}"></div><p>{d}</p><span class="mono">{src}</span></div>' for i,(k,c,t,d,src) in enumerate(mo_svc))}</div>
</div></section>
<section class="family" id="family"><div class="wrap fam-grid">
<div class="year reveal" aria-hidden="true">'09</div>
<div class="reveal" style="--d:1"><p class="mono" style="color:var(--yellow);margin-bottom:16px">Family owned &amp; operated</p>
<p>Moreno's opened in 2009 and it's still run by the family. Same bays, same street, same name on the wall. Customers say the owner tells it straight and charges a fair price.</p>
<div class="nums"><div><strong><span data-count="4.7">4.7</span>★</strong><span class="mono">Google · 284 reviews</span></div><div><strong><span data-count="4.9">4.9</span>★</strong><span class="mono">SureCritic · 661 verified</span></div></div></div>
</div></section>
<section id="reviews"><div class="wrap">
<div class="head"><div><p class="mono" style="color:var(--accent);margin-bottom:14px">Reviews</p><h2>Above<br>and beyond.</h2></div><p>Real words from customers on Yelp and SureCritic.</p></div>
<div class="quotes">{quotes([('Good affordable service!!','James S. · Yelp · Jan 2025'),('…above and beyond…','G O. · Yelp · Nov 2025 · vehicle inspection'),('Outstanding Customer Service','Lisa A. · SureCritic verified · Nov 2026')])}</div>
</div></section>
<section class="visit" id="visit"><div class="wrap visit-grid">
<div class="reveal"><p class="mono" style="color:var(--yellow)">Visit</p><h2 style="margin-top:14px">527 East<br>Holt.</h2>
<address>527 E Holt Blvd<br>Ontario, CA 91761</address><p style="color:var(--muted)">White building, red trim, three open bays and a wall of banners.</p>
<a class="bigphone" href="tel:+19094186955">(909) 418-6955</a>
<div class="actions"><a class="btn" href="https://www.google.com/maps/search/?api=1&query=Moreno%27s+Auto+Repair+527+E+Holt+Blvd+Ontario+CA+91761" rel="noopener">Get directions <i>→</i></a></div></div>
<div class="reveal" style="--d:1">{week({1:(8,18,'8:00 AM – 6:00 PM'),2:(8,18,'8:00 AM – 6:00 PM'),3:(8,18,'8:00 AM – 6:00 PM'),4:(8,18,'8:00 AM – 6:00 PM'),5:(8,18,'8:00 AM – 6:00 PM'),6:(None,None,''),0:(None,None,'')})}<p class="note">Hours from public listings. Call ahead to confirm.</p></div>
</div></section>
</main>
<footer><div class="wrap"><strong>Moreno's Auto Repair LLC · Ontario, CA</strong><span>{DISCLAIMER}</span></div></footer>
'''

SITES = {
 'tri-auto': ("Tri Auto | Toyota, Honda & Lexus Repair in Chino, CA", "Tri Auto — independent Toyota, Honda and Lexus repair at 6108 Schaefer Ave, Chino. Honest work at fair prices. (909) 465-6422.", '#efe6d3', tri_css, tri_body),
 'ac-tires': ("A C Tires & Wheels | New & Used Tires in Ontario, CA", "A C Tires — new and used tires, flat repair, mount and balance at 301 W California St, Ontario. Open late and open Sundays. (909) 391-4636.", '#1f3fae', ac_css, ac_body),
 'morenos-auto-repair': ("Moreno's Auto Repair | Family-Owned Shop in Ontario, CA", "Moreno's Auto Repair — engine repair, computer alignment, A/C and transmission rebuilds at 527 E Holt Blvd, Ontario. Family owned since 2009. (909) 418-6955.", '#f4f1ea', mo_css, mo_body),
}
out = sys.argv[1]
for slug, args in SITES.items():
    os.makedirs(os.path.join(out, slug), exist_ok=True)
    p = os.path.join(out, slug, 'index.html')
    open(p, 'w').write(page(*args))
    print(p, os.path.getsize(p))
