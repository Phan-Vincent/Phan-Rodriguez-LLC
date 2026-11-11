#!/usr/bin/env python3
"""Builds the three auto shop concept sites (2026-11-10 layouts).

Each site has its own layout on purpose:
  tri-auto            split hero, three make tiles, zigzag rows, rotating reviews
  ac-tires            photo banner with info bar, service list, week strip
  morenos-auto-repair profile page: sticky shop card beside a content column

Run:  python3 build_v2.py <path-to-mockups-dir>
Tri Auto's review markup (Vincent's Birdeye links) lives in tri_reviews/.
"""
import sys, pathlib

HERE = pathlib.Path(__file__).parent


def U(pid, w, h, q=70):
    return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}&h={h}&q={q}"


BASE = """
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:84px}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 'Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,p,blockquote,figure,ul{margin:0}ul{padding:0;list-style:none}a{color:inherit;text-decoration:none}img{display:block;max-width:100%}
h1,h2,h3{letter-spacing:-.02em;line-height:1.1;font-weight:700}
a:focus-visible,button:focus-visible,[tabindex]:focus-visible{outline:2px solid var(--focus,var(--accent));outline-offset:3px;border-radius:4px}
.wrap{width:min(1160px,calc(100% - 48px));margin:auto}
.skip{position:absolute;left:16px;top:-80px;z-index:99;background:#fff;color:#000;padding:10px;border-radius:6px}.skip:focus{top:10px}
.label{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:10px 20px;border-radius:6px;font-weight:600;font-size:15px;background:var(--chip);color:var(--ink);transition:filter .175s}
.btn:hover{filter:brightness(.94)}.btn.primary{background:var(--accent);color:#fff}
.card{background:#fff;border-radius:8px;box-shadow:0 1px 2px #0003}
.muted{color:var(--muted)}
table{border-collapse:separate;border-spacing:0 4px;width:100%;font-size:15px}
th{text-align:left;font-weight:500}td{text-align:right;white-space:nowrap}
@media(max-width:480px){table{font-size:14px}th,td{padding:9px 8px}}th,td{padding:10px 12px;background:var(--row,#fff)}
tr th{border-radius:6px 0 0 6px}tr td{border-radius:0 6px 6px 0}
tr.today th,tr.today td{background:var(--today,var(--accent));color:var(--on-today,#fff);font-weight:700}
.tag{font-size:10px;text-transform:uppercase;letter-spacing:.06em;margin-left:8px;border:1px solid currentColor;border-radius:6px;padding:2px 6px}
.js .reveal{opacity:0;transform:translateY(32px);transition:opacity .6s cubic-bezier(.24,1,.4,1),transform .6s cubic-bezier(.24,1,.4,1);transition-delay:calc(var(--d,0)*90ms)}
.js .reveal.in{opacity:1;transform:none}
.holiday{margin-top:12px;padding:12px 14px;border-radius:8px;background:var(--chip);font-size:14px}.holiday strong{display:block;font-size:13px}.holiday p{color:var(--muted);margin-top:2px}.holiday a{color:var(--ink);font-weight:600;text-decoration:underline;text-underline-offset:3px}
footer{margin-top:72px;padding:26px 0 34px;border-top:1px solid var(--line);font-size:12.5px;color:var(--muted)}
footer .wrap{display:flex;gap:24px;justify-content:space-between;flex-wrap:wrap}footer span{max-width:760px}

/* ---- energy layer: rising headline, moving band, stripes, rating badge, hover fills (motion values from Astryx) ---- */
body{background:radial-gradient(1100px 520px at 88% -8%,color-mix(in srgb,var(--accent) 16%,transparent),transparent 62%),var(--bg);background-repeat:no-repeat}
h1,h2,.lead h2{font-weight:800;letter-spacing:-.035em}
.progress{position:fixed;left:0;top:0;height:4px;width:calc(var(--p,0)*100%);background:linear-gradient(90deg,var(--accent),var(--gold,var(--accent)));z-index:60}
.label{color:var(--accent)}.label:before{content:"";display:inline-block;width:22px;height:3px;background:currentColor;margin-right:9px;vertical-align:middle}
.js h1 .wd,.js .lead h2 .wd{display:inline-block;overflow:hidden;vertical-align:top;padding:.1em .05em .14em 0;margin:-.1em 0 -.14em}
.js h1 .wd>span,.js .lead h2 .wd>span{display:inline-block;transform:translateY(112%);transition:transform .9s cubic-bezier(.24,1,.4,1);transition-delay:calc(var(--i)*70ms)}
.js.ready h1 .wd>span,.js.ready .lead h2 .wd>span{transform:none}
.btn{position:relative;overflow:hidden;isolation:isolate;transition:color .175s,filter .175s}
.btn.primary:before{content:"";position:absolute;inset:0;background:var(--ink,#050505);transform:translateY(101%);transition:transform .41s cubic-bezier(.24,1,.4,1);z-index:-1}
.btn.primary:hover:before{transform:none}.btn.primary:hover{filter:none}
.btn.primary:after{content:"→";transition:transform .175s}.btn.primary:hover:after{transform:translateX(5px)}
.marquee{overflow:hidden;white-space:nowrap;background:var(--dark,#141414);color:#fff;font-weight:800;text-transform:uppercase;letter-spacing:.03em;font-size:16px}
.marquee div{display:inline-block;animation:slide 34s linear infinite;padding:13px 0}.marquee span{margin:0 22px}.marquee i{font-style:normal;color:var(--gold,#E9B949)}
@keyframes slide{to{transform:translateX(-50%)}}
.stripes{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:0}
.stripes i{position:absolute;top:-20%;height:140%;width:2.3vw;right:calc(var(--n)*3.3vw + 6vw);transform:skewX(-18deg) translateY(calc(var(--scroll,0)*-.1px));background:linear-gradient(90deg,#fff3,#fff0 20%,#0000 70%,#0003),var(--c);animation:drop 1.1s cubic-bezier(.24,1,.4,1) both;animation-delay:calc(var(--n)*120ms + 300ms);opacity:.93}
.stripes i:nth-child(1){--n:2;--c:var(--accent)}.stripes i:nth-child(2){--n:1;--c:var(--gold,#E9B949)}.stripes i:nth-child(3){--n:0;--c:#fff}
@keyframes drop{from{clip-path:inset(0 0 100% 0)}to{clip-path:inset(0)}}
.shot{position:relative;isolation:isolate}
.shot:before{content:"";position:absolute;right:-16px;bottom:-16px;width:72%;height:72%;background:var(--accent);border-radius:8px;z-index:-1}
.shot:after{content:"";position:absolute;left:-14px;top:-14px;width:30%;height:34%;background:var(--gold,#E9B949);border-radius:8px;z-index:-1}
.badge{position:absolute;left:-18px;bottom:26px;z-index:2;background:linear-gradient(160deg,#2a2a2a,#0c0c0c);color:#fff;padding:16px 22px;border-radius:8px;box-shadow:0 22px 40px -14px #000a;transform:rotate(-4deg) translate(calc(var(--mx,0)*-14px),calc(var(--my,0)*-14px));transition:transform .2s}
.badge b{display:block;font-size:46px;line-height:1;font-weight:800;letter-spacing:-.03em}.badge b i{font-style:normal;color:var(--gold,#E9B949)}.badge small{display:block;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#ffffffcc}
.cover{position:relative;overflow:hidden}.cover .badge{left:auto;right:28px;bottom:76px}
.tile,.make,.it,.rate,.q,.s,.day{transition:transform .175s cubic-bezier(.24,1,.4,1),box-shadow .175s,color .175s,background .175s}
.tile,.make{position:relative;overflow:hidden;isolation:isolate}
.tile:before,.make:before{content:"";position:absolute;inset:0;background:var(--accent);transform:translateY(101%);transition:transform .41s cubic-bezier(.24,1,.4,1);z-index:-1}
.tile:hover:before,.make:hover:before{transform:none}.tile:hover,.make:hover{color:#fff;transform:translateY(-4px)}.tile:hover p,.make:hover p{color:#ffffffe0}
.rate:hover,.q:hover,.s:hover,a.quote:hover{transform:translateY(-4px) rotate(-.5deg);box-shadow:6px 6px 0 var(--accent)}
.svc li{transition:padding .175s,background .175s}.svc li:hover{padding-left:30px;background:color-mix(in srgb,var(--accent) 7%,#fff)}
.it:hover{transform:translateX(6px)}
.hero img,.row img,.side img,.photo img,.s img{transition:filter .41s,transform .41s cubic-bezier(.24,1,.4,1);filter:saturate(.9) contrast(1.03)}
.hero img:hover,.row img:hover,.side img:hover,.photo img:hover,.s:hover img{filter:none;transform:scale(1.02)}
span[data-count]{font:inherit!important;color:inherit!important;letter-spacing:inherit!important;text-transform:none!important}
h1 em,.lead h2 em{background:linear-gradient(transparent 68%,color-mix(in srgb,var(--gold,#E9B949) 60%,transparent) 0)}
@media(max-width:860px){.stripes i{width:12px;right:calc(var(--n)*18px + 12px);opacity:.3}.name{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}.badge{left:10px;bottom:-18px;padding:12px 16px}.badge b{font-size:34px}.shot{margin:14px 14px 22px 14px;order:-1}.cover .badge{right:14px;bottom:52px}.marquee{font-size:14px}}
@media(prefers-reduced-motion:reduce){.js h1 .wd>span,.js .lead h2 .wd>span{transform:none}html{scroll-behavior:auto}*,*:before,*:after{animation:none!important;transition:none!important}.js .reveal{opacity:1;transform:none}}
"""

JS = """<script>
(()=>{
// scroll reveal: blocks stay hidden until scrolled to, then fade and slide up; siblings arrive one after another
document.documentElement.classList.add('js');
const targets=[...document.querySelectorAll('.hero>*,.hero>div>*,.banner .wrap>*,.bar,.intro,.make,.row,.bigquote,#review-track,.visit,.side,.svc li,.stats,.quotes>.quote:not(#review-track .quote),.day,.find,.cover,.shop,.feed>.card,.s,.rev li,.tile,.rate,.q,.it,.aboutc,.marquee,.shot,main section>.wrap>.label,main section>.wrap>h2,main section>.wrap>div>.label,main section>.wrap>div>h2,.reveal')];
targets.forEach(el=>{el.classList.add('reveal');const sibs=[...el.parentElement.children].filter(c=>targets.includes(c));el.style.setProperty('--d',Math.min(sibs.indexOf(el),5))});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1,rootMargin:'0px 0px -6% 0px'});
targets.forEach(el=>io.observe(el));
// headline words rise in
const root=document.documentElement,reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
document.querySelectorAll('h1,.lead h2').forEach(h=>{let i=0;const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\\s+)/).forEach(t=>{if(!t.trim()){f.append(t);return}const w=document.createElement('span');w.className='wd';const sp=document.createElement('span');sp.style.setProperty('--i',i++);sp.textContent=t;w.append(sp);f.append(w)});c.replaceWith(f)}else if(c.tagName!=='BR')walk(c)})};walk(h)});
requestAnimationFrame(()=>requestAnimationFrame(()=>root.classList.add('ready')));
// numbers count up when they come into view
const count=el=>{const end=parseFloat(el.dataset.count),dec=(el.dataset.count.split('.')[1]||'').length;if(reduce)return;const t0=performance.now();const step=t=>{const p=Math.min((t-t0)/1300,1),e=1-Math.pow(1-p,3);el.textContent=(end*e).toFixed(dec);if(p<1)requestAnimationFrame(step)};requestAnimationFrame(step)};
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){count(e.target);cio.unobserve(e.target)}}),{threshold:.6});
document.querySelectorAll('[data-count]').forEach(el=>cio.observe(el));
// scroll progress bar, stripe drift and badge following the pointer
if(!reduce){let tick=false;const upd=()=>{root.style.setProperty('--scroll',scrollY);root.style.setProperty('--p',(scrollY/Math.max(1,root.scrollHeight-innerHeight)).toFixed(4));tick=false};addEventListener('scroll',()=>{if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});
addEventListener('pointermove',e=>{if(e.pointerType==='mouse'){root.style.setProperty('--mx',(e.clientX/innerWidth-.5).toFixed(3));root.style.setProperty('--my',(e.clientY/innerHeight-.5).toFixed(3))}},{passive:true})}
// highlight today's hours in the shop's time zone
const wd=new Intl.DateTimeFormat('en-US',{weekday:'short',timeZone:'America/Los_Angeles'}).format(new Date());
const d=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(wd);
document.querySelectorAll('[data-day="'+d+'"]').forEach(row=>{row.classList.add('today');const h=row.querySelector('th,.dname');if(h){const t=document.createElement('span');t.className='tag';t.textContent='Today';h.append(t)}});
})();
</script>"""

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def holiday(phone, tel):
    return f'<div class="holiday"><strong>Holiday hours</strong><p>Hours can change on holidays, including Veterans Day, Thanksgiving, Christmas and New Year\'s Day. Call <a href="tel:{tel}">{phone}</a> before you come in.</p></div>'


def hours_table(hours, phone, tel):
    rows = "".join(
        f'<tr data-day="{(i + 1) % 7}"><th scope="row">{d}</th><td>{hours[i]}</td></tr>'
        for i, d in enumerate(DAYS)
    )
    return f'<table><caption class="label" style="text-align:left;padding-bottom:8px">Hours</caption>{rows}</table>{holiday(phone, tel)}'


def marquee(items):
    run = "".join(f"<span>{i}</span><i>///</i>" for i in items)
    return f'<div class="marquee" aria-hidden="true"><div>{run}{run}</div></div>'


def badge(num, small):
    return f'<div class="badge"><small>Google rating</small><b><span data-count="{num}">{num}</span><i>★</i></b><small>{small}</small></div>'


STRIPES = '<div class="stripes" aria-hidden="true"><i></i><i></i><i></i></div>'


def page(title, desc, css, body, extra_js=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<style>{BASE}{css}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
{body}
{JS}
{extra_js}
</body>
</html>
"""


def footer(name):
    return f'<footer><div class="wrap"><strong>{name}</strong><span>Concept website by Phan-Rodriguez LLC. Not the official site of this business. Photos are stock images.</span></div></footer>'



CAR_CSS = """
.quotes{display:flex;gap:16px;overflow-x:auto;scrollbar-width:none;padding:4px 2px 18px;cursor:grab}.quotes::-webkit-scrollbar{display:none}
.quotes .quote{flex:0 0 min(380px,82%);background:var(--qbg,#fff);border-radius:8px;box-shadow:0 1px 2px #0003;padding:22px}
.review-body{display:flex;flex-direction:column;justify-content:space-between;gap:24px;height:100%}
.review-origin{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent)}
.quotes .quote p:not(.review-origin){font-size:19px;font-weight:600;line-height:1.35}
.quotes .quote cite{display:block;font-style:normal;font-size:12.5px;color:var(--muted)}
.review-source{display:inline-block;margin-top:10px;font-size:13px;font-weight:600;letter-spacing:0;text-decoration:underline;text-underline-offset:4px}
"""
CAROUSEL_JS = (HERE / "tri_reviews" / "carousel.html").read_text()


def track(reviews):
    """reviews: (name, source label, short excerpt, link to the review, site name for the link text)"""
    cards = "".join(
        f'<a class="quote" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="Read {name}’s review on {site} (opens in a new tab)"><blockquote class="review-body"><div><p class="review-origin">Customer review</p><p style="margin-top:14px">“{text}”</p></div><div><cite>{name} · {label}</cite><span class="review-source">Read review on {site} ↗</span></div></blockquote></a>'
        for name, label, text, url, site in reviews
    )
    return f'<p id="review-help" style="position:absolute;left:-9999px">Customer reviews scroll automatically and pause while you touch, hover or focus them.</p>\n<div class="quotes" id="review-track" role="region" aria-label="Customer reviews" aria-describedby="review-help" tabindex="0">{cards}</div>'


def yelp(biz, hrid):
    return f"https://www.yelp.com/biz/{biz}?hrid={hrid}"


AC_REVIEWS = [
    ("Sam R.", "Yelp review", "…the dudes here are super nice and straight forward…", yelp("ac-tires-ontario", "qpYzQvT4rPGetO2iujY9AA"), "Yelp"),
    ("Christopher H.", "Yelp review", "This shop saved me…", yelp("ac-tires-ontario", "KIjkkkd9y3sKk48GIKdnIg"), "Yelp"),
    ("Jason B.", "Yelp review", "Better prices and faster service…", yelp("ac-tires-ontario", "mEdlYEeRdGaw9HvtcZtlBg"), "Yelp"),
    ("Samantha D.", "Yelp review", "…Really Fast Reliable Employees", yelp("ac-tires-ontario", "9hu7OMh86t_kzCD_94nGGQ"), "Yelp"),
    ("Ru", "Google review", "Lifesavers on a Rainy Night…", "https://reviews.birdeye.com/a-c-tires-156071200776516#:~:text=Lifesavers%20on%20a%20Rainy%20Night", "Birdeye"),
]
SC = "https://www.surecritic.com/reviews/morenos-auto-repair#:~:text="
MO_REVIEWS = [
    ("Lisa A.", "SureCritic · Nov 2026", "Outstanding Customer Service", SC + "Outstanding%20Customer%20Service", "SureCritic"),
    ("Alex L.", "SureCritic · Oct 2026", "Great honest Mechanics", SC + "Great%20honest%20Mechanics", "SureCritic"),
    ("Tyrone J.", "Yelp review", "Very professional and expedient service.", yelp("morenos-auto-repair-ontario-2", "BQJK_qJYwKShB12glCtFBg"), "Yelp"),
    ("Azucena B.", "SureCritic · Oct 2026", "Professional and efficient, fair prices too", SC + "Professional%20and%20efficient%2C%20fair%20prices%20too", "SureCritic"),
    ("Lilly Z.", "Yelp review", "…they did an awesome job, communicated well…", yelp("morenos-auto-repair-ontario-2", "uTCS3aO0lrz0njDDfpxlyw"), "Yelp"),
    ("Nicol B.", "SureCritic · Sep 2026", "Very professional &amp; prepared, great customer service.", SC + "Very%20professional%20%26%20prepared%2C%20great%20customer%20service.", "SureCritic"),
    ("Vipneet S.", "SureCritic · Sep 2026", "Excellent staff", SC + "Excellent%20staff", "SureCritic"),
]

# ---------------------------------------------------------------- Tri Auto
tri_css = """
:root{--bg:#F0F2F5;--ink:#050505;--muted:#65676B;--line:#CED0D4;--chip:#E4E6EB;--accent:#B3261E;--a2:#C8642A;--a3:#D9A53A;--dark:#141414;--gold:#E9B949}
header{position:sticky;top:0;z-index:20;background:#fff;box-shadow:0 1px 2px #0000001f}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:60px}
nav{display:flex;gap:26px;font-size:14px;font-weight:600}nav a:hover{color:var(--accent)}
.hero{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:48px;align-items:center;padding:56px 0 64px}
h1{font-size:clamp(40px,5.8vw,78px);line-height:1}h1 em{font-style:normal;color:var(--accent)}
.lede{font-size:18px;color:var(--muted);margin-top:20px;max-width:520px}
.actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}
.rating{margin-top:22px;font-size:14px;font-weight:600}.rating b{color:var(--accent)}
.hero img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:8px}
section{padding:56px 0}h2{font-size:clamp(26px,3vw,38px);margin-top:8px}
.intro{max-width:620px;margin-bottom:28px}.intro p:last-child{margin-top:10px;color:var(--muted)}
.makes{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.make{padding:26px 24px 28px;border-top:4px solid var(--c)}
.make h3{font-size:34px}.make p{margin-top:10px;color:var(--muted);font-size:15px}
.row{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;margin-top:28px}
.row img{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:8px}
.row:nth-child(even) img{order:2}
.row h3{font-size:26px}.row p{margin-top:12px;color:var(--muted);max-width:440px}
.bigquote{font-size:clamp(26px,3.6vw,46px);font-weight:700;letter-spacing:-.02em;line-height:1.12;margin:10px 0 34px}
.bigquote cite{display:block;font-style:normal;font-size:13px;font-weight:600;letter-spacing:0;color:var(--muted);margin-top:16px}
.review-source{display:inline-block;margin-top:10px;font-size:13px;font-weight:600;letter-spacing:0;text-decoration:underline;text-underline-offset:4px}
.quotes{display:flex;gap:16px;overflow-x:auto;scrollbar-width:none;padding:4px 2px 18px;cursor:grab}.quotes::-webkit-scrollbar{display:none}
.quote{flex:0 0 min(380px,82%);background:#fff;border-radius:8px;box-shadow:0 1px 2px #0003;padding:22px}
.review-body{display:flex;flex-direction:column;justify-content:space-between;gap:24px;height:100%}
.review-origin{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent)}
.quote p:not(.review-origin){font-size:19px;font-weight:600;line-height:1.35}
.quote cite{display:block;font-style:normal;font-size:12.5px;color:var(--muted)}
.visit{display:grid;grid-template-columns:1fr 1fr;gap:40px;padding:34px;align-items:center}
address{font-style:normal;font-size:20px;font-weight:600;line-height:1.4;margin:14px 0 6px}
.bigphone{display:inline-block;font-size:clamp(28px,3.4vw,40px);font-weight:700;letter-spacing:-.02em;margin-top:16px}
.visit{--row:#F0F2F5}
@media(max-width:860px){nav{display:none}.hero{grid-template-columns:1fr;gap:28px;padding:28px 0 40px}.hero .shot{order:-1}.makes{grid-template-columns:1fr}.row{grid-template-columns:1fr;gap:18px}.row:nth-child(even) img{order:0}.visit{grid-template-columns:1fr;padding:22px}section{padding:40px 0}}
"""

tri_logo = '<svg viewBox="0 0 250 60" role="img" aria-label="Tri-Auto" style="width:150px;display:block"><text x="0" y="44" font-family="\'Segoe UI\',system-ui,Arial,sans-serif" font-weight="700" font-size="44" letter-spacing="-1.5" fill="currentColor">Tri-Auto</text><g transform="skewX(-18)"><rect x="205" y="10" width="9" height="38" fill="#B3261E"/><rect x="218" y="10" width="9" height="38" fill="#C8642A"/><rect x="231" y="10" width="9" height="38" fill="#D9A53A"/></g></svg>'

tri_body = f"""
<header><div class="wrap"><a href="#" aria-label="Tri Auto home">{tri_logo}</a>
<nav aria-label="Main"><a href="#makes">What we fix</a><a href="#why">Why Tri Auto</a><a href="#reviews">Reviews</a><a href="#visit">Visit</a></nav>
<a class="btn" href="tel:+19094656422">(909) 465-6422</a></div></header>
<main id="main">
<div class="wrap hero">
<div><h1>Bye-bye, <em>dealership.</em></h1>
<p class="lede">Tri Auto is Chino's independent shop for <strong style="color:var(--ink)">Toyota, Honda and Lexus</strong>. Three makes, known inside out, at prices well below the dealer's.</p>
<div class="actions"><a class="btn primary" href="tel:+19094656422">Call Danny's shop</a><a class="btn" href="#visit">Hours &amp; directions</a></div>
</div>
<div class="shot"><img alt="Close-up of a mechanic's gloved hand holding a wrench" src="{U('1729844164746-d074d1d4ac6c', 1100, 825)}">{badge('4.9', '333 reviews')}</div>
</div>
{marquee(['Toyota', 'Honda', 'Lexus', 'Honest work', 'Fair prices', 'Chino, CA'])}
<section id="makes"><div class="wrap">
<div class="intro"><span class="label">What we fix</span><h2>Three makes. Nothing else.</h2><p>We don't work on everything. We work on these three, every day. That focus is the whole idea behind the name.</p></div>
<div class="makes">
<div class="card make reveal" style="--c:#B3261E"><h3>Toyota</h3><p>Camry, Corolla, Tacoma, RAV4, Prius and the rest of the family.</p></div>
<div class="card make reveal" style="--c:#C8642A"><h3>Honda</h3><p>Civic, Accord, CR-V, Odyssey, Pilot. Daily drivers kept on the road.</p></div>
<div class="card make reveal" style="--c:#D9A53A"><h3>Lexus</h3><p>Dealer-level know-how for your ES, RX or IS, without the dealer invoice.</p></div>
</div></div></section>
<section id="why"><div class="wrap">
<div class="intro"><span class="label">Why Tri Auto</span><h2>What people come in for.</h2><p>The reasons customers keep coming back.</p></div>
<div class="row reveal"><img loading="lazy" alt="Fresh oil being poured into an engine" src="{U('1487754180451-c456f719a1fc', 900, 562)}"><div><h3>Maintenance &amp; oil changes</h3><p>Routine service done right, often the same day.</p></div></div>
<div class="row reveal"><img loading="lazy" alt="Open engine bay" src="{U('1686082307524-c89fb0bfadde', 900, 562)}"><div><h3>Diagnosis &amp; repair</h3><p>A straight answer about what's wrong, what it costs, and what can wait.</p></div></div>
<div class="row reveal"><img loading="lazy" alt="Car raised on a shop lift" src="{U('1791419542289-693087bd1044', 900, 562)}"><div><h3>A second opinion</h3><p>Got a dealer quote that stings? Bring it in. One customer saved almost $600.</p></div></div>
</div></section>
<section id="reviews"><div class="wrap">
<span class="label">Reviews</span>
{(HERE / 'tri_reviews' / 'bigquote.html').read_text().replace(' reveal', '')}
<p id="review-help" style="position:absolute;left:-9999px">Customer reviews scroll automatically and pause while you touch, hover or focus them.</p>
{(HERE / 'tri_reviews' / 'track.html').read_text()}
</div></section>
<section id="visit"><div class="wrap"><div class="card visit">
<div><span class="label">Visit</span><h2>Schaefer Ave, Chino.</h2>
<address>6108 Schaefer Ave<br>Chino, CA 91710</address><a class="bigphone" href="tel:+19094656422">(909) 465-6422</a>
<div class="actions"><a class="btn primary" href="https://www.google.com/maps/search/?api=1&query=Tri+Auto+6108+Schaefer+Ave+Chino+CA+91710" rel="noopener">Get directions</a></div></div>
<div>{hours_table(['8:00 AM – 5:00 PM'] * 5 + ['Closed', 'Closed'], '(909) 465-6422', '+19094656422')}</div>
</div></div></section>
</main>
{footer('Tri Auto · Chino, CA')}
"""

# ---------------------------------------------------------------- A C Tires
ac_css = """
:root{--dark:#16295E;--bg:#F5F6F8;--ink:#0B1220;--muted:#5A6272;--line:#D5D9E0;--chip:#E6E9EF;--accent:#B3261E;--navy:#16295E;--gold:#E9B949;--focus:#16295E}
header{background:var(--navy);color:#fff;--focus:#fff}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:64px}
.sign{font-weight:700;font-size:20px;letter-spacing:-.01em}.sign small{color:var(--gold);font-size:.8em;font-weight:600}
nav{display:flex;gap:26px;font-size:14px;font-weight:600}nav a:hover{text-decoration:underline;text-underline-offset:5px}
header .btn{background:#fff;color:var(--navy)}
.banner{position:relative;color:#fff;background:linear-gradient(90deg,#101E47f2 0,#16295Ed9 46%,#16295E59 100%),var(--img) center/cover #16295E;--focus:#fff}
.banner .wrap{padding:84px 0 132px}
.banner{overflow:hidden}.banner .wrap{position:relative;z-index:1}h1{font-size:clamp(40px,6.2vw,84px);line-height:1;max-width:760px}h1 .hl{color:var(--gold)}
.lede{font-size:18px;max-width:520px;margin-top:20px;color:#E3E8F5}
.bar{display:grid;grid-template-columns:repeat(3,1fr);margin-top:-64px;position:relative;z-index:2}
.bar>*{padding:22px 24px;border-right:1px solid var(--line)}.bar>*:last-child{border:0}
.bar strong{display:block;font-size:20px;letter-spacing:-.01em;margin-top:4px}.bar a strong{color:var(--accent)}
.bar small{display:block;color:var(--muted);font-size:13.5px;margin-top:2px}
section{padding:64px 0 0}h2{font-size:clamp(26px,3vw,38px);margin-top:8px}
.split{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:48px;align-items:stretch}
.split .side{display:flex;flex-direction:column}.side p{color:var(--muted);margin-top:12px;max-width:360px}
.side img{width:100%;flex:1;min-height:240px;aspect-ratio:4/3;object-fit:cover;border-radius:8px;margin-top:24px}
.svc{display:grid;grid-auto-rows:1fr}.svc li{display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:center;padding:20px 24px;border-bottom:1px solid var(--line)}.svc li:last-child{border:0}
.svc svg{width:36px;height:36px;color:var(--navy)}.svc h3{font-size:19px}.svc p{color:var(--muted);font-size:15px;margin-top:4px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);background:var(--navy);color:#fff;border-radius:8px}
.stats div{padding:26px 28px;border-right:1px solid #ffffff2e}.stats div:last-child{border:0}
.stats strong{display:block;font-size:clamp(34px,4.4vw,52px);line-height:1;letter-spacing:-.02em}.stats span{font-size:13px;font-weight:600;color:#C9D2EA;letter-spacing:.04em;text-transform:uppercase}
.week{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin-top:24px}
.day{padding:16px 10px;text-align:center}.dname{display:block;font-weight:700;font-size:14px}.day .tag{display:block;margin:6px auto 0;width:max-content}
.day span.h{display:block;font-size:13px;color:var(--muted);margin-top:6px;line-height:1.35}
.day.today{background:var(--navy);color:#fff}.day.today span.h{color:#C9D2EA}
.find{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;padding:26px 28px;margin-top:16px}.holiday{max-width:none}
address{font-style:normal;font-size:20px;font-weight:600;line-height:1.4}
.find .actions{display:flex;gap:10px;flex-wrap:wrap}
@media(max-width:860px){nav{display:none}.sign{font-size:17px;white-space:nowrap}header .btn{white-space:nowrap;padding:8px 12px;font-size:14px}.banner .wrap{padding:52px 0 96px}.bar{grid-template-columns:1fr}.bar>*{border-right:0;border-bottom:1px solid var(--line)}.split{grid-template-columns:1fr;gap:24px}.side img{flex:none}.stats{grid-template-columns:1fr}.stats div{border-right:0;border-bottom:1px solid #ffffff2e}.week{grid-template-columns:1fr 1fr}.find{grid-template-columns:1fr}section{padding:44px 0 0}}
"""

tire_icon = '<svg viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="19" fill="none" stroke="currentColor" stroke-width="4"/><circle cx="22" cy="22" r="6" fill="currentColor"/><path d="M22 3v10M22 31v10M3 22h10M31 22h10" stroke="currentColor" stroke-width="3"/></svg>'
ac_services = [
    ("New tires", "Fresh rubber in the sizes people around here actually drive."),
    ("Used tires", "Good used tires for when the budget says “not today” to a full new set."),
    ("Flat repair", "Nail in the tread? In and out fast, weekends included."),
    ("Mount &amp; balance", "Bought tires elsewhere? We’ll mount and balance them."),
    ("Wheels", "Ask what’s in stock for your car."),
]
ac_hours = ["8 AM – 8 PM"] * 5 + ["8 AM – 7 PM", "8 AM – 6 PM"]
ac_week = "".join(
    f'<div class="card day" data-day="{(i + 1) % 7}"><span class="dname">{d[:3]}</span><span class="h">{ac_hours[i]}</span></div>'
    for i, d in enumerate(DAYS)
)

ac_body = f"""
<header><div class="wrap"><a href="#" class="sign" aria-label="A C Tires and Wheels">AC-Tires <small>&amp;</small> Wheels</a>
<nav aria-label="Main"><a href="#services">Services</a><a href="#reviews">Reviews</a><a href="#visit">Hours &amp; location</a></nav>
<a class="btn" href="tel:+19093914636">(909) 391-4636</a></div></header>
<main id="main">
<div class="banner" role="img" aria-label="Gloved hands mounting a tire in a workshop" style="--img:url({U('1792792944402-5e94ce198dce', 1800, 900)})">{STRIPES}<div class="wrap">
<h1>Flat at 7 PM? <span class="hl">We're still open.</span></h1>
<p class="lede">New and used tires, flat repair and mount-and-balance at the blue shop on California Street in Ontario.</p>
</div></div>
<div class="wrap"><div class="card bar">
<div><span class="label">Open late</span><strong>Until 8 PM weeknights</strong><small>Saturday until 7 · Sunday until 6</small></div>
<a href="tel:+19093914636"><span class="label">Call the shop</span><strong>(909) 391-4636</strong><small>Tap to call</small></a>
<a href="#visit"><span class="label">Find us</span><strong style="color:var(--ink)">301 W California St</strong><small>Ontario, CA 91762 · look for the blue building</small></a>
</div></div>
<div style="margin-top:44px">{marquee(['New tires', 'Used tires', 'Flat repair', 'Mount &amp; balance', 'Open til 8 PM', 'Open Sundays'])}</div>
<section id="services"><div class="wrap split">
<div class="side"><span class="label">What we do</span><h2>Tires. That's it. That's the shop.</h2><p>No waiting-room upsell. Pull in, tell us what you need, and get back on the road.</p>
<img loading="lazy" alt="Stacks of tires in a tire shop" src="{U('1578844251758-2f71da64c96f', 900, 675)}"></div>
<ul class="card svc">{"".join(f'<li class="reveal" >{tire_icon}<div><h3>{n}</h3><p>{t}</p></div></li>' for i, (n, t) in enumerate(ac_services))}</ul>
</div></section>
<section id="reviews"><div class="wrap">
<div class="stats reveal"><div><strong><span data-count="4.4">4.4</span> ★</strong><span>Google rating</span></div><div><strong data-count="324">324</strong><span>Google reviews</span></div><div><strong data-count="7">7</strong><span>Days a week</span></div></div>
<div style="margin-top:48px"><span class="label">Reviews</span><h2>Quick, easy, straight forward.</h2></div>
<div style="margin-top:24px">{track(AC_REVIEWS)}</div>
</div></section>
<section id="visit"><div class="wrap">
<span class="label">Hours &amp; location</span><h2>Look for the blue building.</h2>
<div class="week">{ac_week}</div>
{holiday('(909) 391-4636', '+19093914636')}
<div class="card find"><div><address>301 W California St, Ontario, CA 91762</address></div>
<div class="actions"><a class="btn primary" href="https://www.google.com/maps/search/?api=1&query=A+C+Tires+301+W+California+St+Ontario+CA+91762" rel="noopener">Get directions</a><a class="btn" href="tel:+19093914636">Call (909) 391-4636</a></div></div>
</div></section>
</main>
{footer('A C Tires · Ontario, CA')}
"""

# ---------------------------------------------------------------- Moreno's
mo_css = """
:root{--dark:#111418;--bg:#F2F3F5;--ink:#111418;--muted:#5F6670;--line:#D3D6DB;--chip:#E5E7EB;--accent:#A32420;--gold:#E9B949;--blue:#1E4A9C;--focus:#1E4A9C}
.cover{height:clamp(220px,32vw,400px);background:linear-gradient(180deg,#0000 55%,#0008 100%),var(--img) center 45%/cover #23262b;border-radius:0 0 8px 8px}
.layout{display:grid;grid-template-columns:340px minmax(0,1fr);gap:24px;align-items:start;margin-top:-56px;position:relative}
.shop{position:sticky;top:16px;padding:24px;--row:#F2F3F5}
.shop h1{font-size:28px}.shop h1 i{font-style:normal;color:var(--accent)}
.shop .sub{font-size:13px;font-weight:600;color:var(--muted);margin-top:4px}
.rates{display:flex;gap:18px;margin:16px 0;padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.rates strong{display:block;font-size:22px}.rates span{font-size:12px;color:var(--muted)}
.shop .btn{width:100%;margin-top:8px}
address{font-style:normal;font-weight:600;margin:16px 0 4px}
.shop table{font-size:14px;margin-top:14px}.shop th,.shop td{padding:7px 10px}
.shop{--today:var(--gold);--on-today:#111}
.feed{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;min-width:0}
.feed>.card{padding:28px}
.lead h2{font-size:clamp(34px,4.8vw,60px);line-height:1.02}.lead h2 em{font-style:normal;color:var(--accent)}
.lead p{font-size:18px;color:var(--muted);margin-top:14px;max-width:600px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.chips span{font-size:13px;font-weight:700;padding:7px 12px;border-radius:6px}
.y{background:var(--gold);color:#111}.r{background:var(--accent);color:#fff}.w{background:#fff;color:var(--blue);box-shadow:inset 0 0 0 1px var(--line)}
h2.t{font-size:24px;margin-top:6px}
.svc{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:20px}
.s{display:grid;grid-template-columns:104px 1fr;gap:14px;align-items:center;min-width:0}
.s img{width:104px;height:104px;object-fit:cover;border-radius:8px}
.s h3{font-size:17px}.s p{font-size:14px;color:var(--muted);margin-top:4px}.s small{display:block;font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin-top:6px}
.since{background:#7E1B17!important;color:#fff;display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center}
.since .yr{font-size:clamp(64px,9vw,112px);font-weight:700;line-height:.9;letter-spacing:-.04em;color:var(--gold)}
.since .label{color:#F3D9D7}.since p{font-size:17px;margin-top:8px;max-width:520px}
#reviews{--qbg:#F2F3F5}#reviews .quote{box-shadow:none}
.rev li{padding:18px 0;border-bottom:1px solid var(--line)}.rev li:first-child{padding-top:6px}.rev li:last-child{border:0;padding-bottom:0}
.rev p{font-size:19px;font-weight:600}.rev cite{display:block;font-style:normal;font-size:13px;color:var(--muted);margin-top:6px}
@media(max-width:900px){.layout{grid-template-columns:1fr;margin-top:-40px}.shop{position:static}.svc{grid-template-columns:1fr}.since{grid-template-columns:1fr;gap:10px}.feed>.card{padding:22px}}
"""

mo_services = [
    ("Engine repair", "From check-engine lights to major engine work. We track down the hard-to-diagnose problems.", "On the banner", "1429772011165-0c2e054367b8"),
    ("Computer alignment", "Computerized wheel alignment, including taller vehicles other shops turn away.", "On the banner", "1444947295498-07f60c19a4ff"),
    ("A/C complete service", "Air conditioning diagnosis, repair and recharge. This is the Inland Empire. You need it.", "On the banner", "1542399204-b8dd4af5113d"),
    ("Transmission rebuild", "Transmission service and full rebuilds done in-house.", "On the banner", "1614447428943-52ec0bdbc7aa"),
    ("Vehicle inspections", "A favorite of local rideshare drivers.", "From reviews", "1557411255-28ebcc0fdd54"),
    ("Diagnostics", "A scan, a straight explanation and a fair price before any work starts.", "From reviews", "1625047509248-ec889cbff17f"),
]

mo_body = f"""
{marquee(['Engine repair', 'Computer alignment', 'A/C service', 'Transmission rebuild', 'Family owned', 'Since 2009'])}
<main id="main">
<div class="wrap"><div class="cover" role="img" aria-label="Mechanic working under the hood of a car in a clean workshop" style="--img:url({U('1771340012319-0b4fca008b54', 1800, 760)})">{STRIPES}{badge('4.7', '284 reviews')}</div>
<div class="layout">
<aside class="card shop" aria-label="Shop details">
<h1>Moreno<i>'</i>s Auto Repair</h1><p class="sub">Family owned · Holt Blvd, Ontario · since 2009</p>
<div class="rates"><div><strong>4.7 ★</strong><span>Google · 284 reviews</span></div><div><strong>4.9 ★</strong><span>SureCritic · 661 reviews</span></div></div>
<a class="btn primary" href="tel:+19094186955">Call (909) 418-6955</a>
<a class="btn" href="https://www.google.com/maps/search/?api=1&query=Moreno%27s+Auto+Repair+527+E+Holt+Blvd+Ontario+CA+91761" rel="noopener">Get directions</a>
<address>527 E Holt Blvd<br>Ontario, CA 91761</address>{hours_table(['8:00 AM – 6:00 PM'] * 5 + ['Closed', 'Closed'], '(909) 418-6955', '+19094186955')}
</aside>
<div class="feed">
<div class="card lead"><h2>If it's on the banner, <em>we fix it.</em></h2>
<p>Engines, transmissions, alignments and A/C under one roof. Moreno's is a family-owned shop on Holt Boulevard, fixing Ontario's cars since 2009.</p>
<div class="chips" aria-label="Services on the shop's banners"><span class="y">Engine repair</span><span class="r">Computer alignment</span><span class="w">Air condition complete service</span><span class="y">Transmission rebuild</span></div></div>
<div class="card" id="services"><span class="label">Services</span><h2 class="t">Read the wall. That's the menu.</h2>
<div class="svc">{"".join(f'<div class="s reveal" ><img loading="lazy" alt="" src="{U(p, 240, 240, 60)}"><div><h3>{n}</h3><p>{t}</p></div></div>' for i, (n, t, src, p) in enumerate(mo_services))}</div></div>
<div class="card since reveal" id="family"><div class="yr" aria-hidden="true">'09</div><div><span class="label">Family owned &amp; operated</span><p>Moreno's opened in 2009 and it's still run by the family. Same bays, same street, same name on the wall. Straight answers and fair prices.</p></div></div>
<div class="card" id="reviews"><span class="label">Reviews</span><h2 class="t">Above and beyond.</h2>
<div style="margin-top:16px">{track(MO_REVIEWS)}</div></div>
</div></div></div>
</main>
{footer("Moreno's Auto Repair LLC · Ontario, CA")}
"""

SITES = {
    "tri-auto": ("Tri Auto | Toyota, Honda & Lexus Repair in Chino, CA", "Independent Toyota, Honda and Lexus repair in Chino, CA. Concept site.", tri_css, tri_body, (HERE / "tri_reviews" / "carousel.html").read_text()),
    "ac-tires": ("A C Tires | New & Used Tires in Ontario, CA", "New and used tires, flat repair and mount-and-balance in Ontario, CA. Open late and on Sundays. Concept site.", ac_css + CAR_CSS, ac_body, CAROUSEL_JS),
    "morenos-auto-repair": ("Moreno's Auto Repair | Ontario, CA", "Family-owned auto repair on Holt Blvd in Ontario, CA since 2009. Concept site.", mo_css + CAR_CSS, mo_body, CAROUSEL_JS),
}

if __name__ == "__main__":
    OUT = pathlib.Path(sys.argv[1])
    for folder, args in SITES.items():
        (OUT / folder).mkdir(parents=True, exist_ok=True)
        (OUT / folder / "index.html").write_text(page(*args))
        print("built", folder)
