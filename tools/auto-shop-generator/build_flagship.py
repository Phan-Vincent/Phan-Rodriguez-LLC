#!/usr/bin/env python3
"""Flagship pages for the leads still in play (status in the lead sheet, 2026-11-10).

Each site gets its own art direction (hero composition, display type, palette),
built from shared high-craft sections. Facts come from build_leads.py / build_v2.py.

Run:  python3 tools/auto-shop-generator/build_flagship.py mockups
Fonts (Archivo, Instrument Serif; SIL Open Font License) are copied into each site's fonts/ folder.
"""
import sys, pathlib, json, html, shutil

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import build_leads as L  # noqa: E402
import build_v2 as V  # noqa: E402

FONTS = HERE / "fonts"
DAYS = L.DAYS
esc = lambda t: html.escape(t, quote=False)

CSS = """
@font-face{font-family:Archivo;src:url(fonts/archivo-latin-wdth-normal.woff2) format('woff2');font-weight:100 900;font-stretch:62% 125%;font-display:swap}
@font-face{font-family:'Instrument Serif';src:url(fonts/instrument-serif-latin-400-italic.woff2) format('woff2');font-style:italic;font-weight:400;font-display:swap}
@font-face{font-family:'Instrument Serif';src:url(fonts/instrument-serif-latin-400-normal.woff2) format('woff2');font-style:normal;font-weight:400;font-display:swap}
:root{--mut:color-mix(in srgb,var(--ink) 62%,var(--bone));--line:color-mix(in srgb,var(--ink) 16%,transparent);--ease:cubic-bezier(.24,1,.4,1)}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:70px}
body{margin:0;background:var(--bone);color:var(--ink);font:400 17px/1.5 Archivo,'Segoe UI',system-ui,Arial,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,p,blockquote,figure,ul{margin:0}ul{padding:0;list-style:none}a{color:inherit;text-decoration:none}img{display:block;max-width:100%}
a:focus-visible,button:focus-visible,[tabindex]:focus-visible{outline:2px solid var(--acc);outline-offset:4px;border-radius:4px}
.wrap{width:min(1360px,calc(100% - 64px));margin:auto}
.skip{position:absolute;left:16px;top:-80px;z-index:99;background:#fff;color:#000;padding:10px;border-radius:6px}.skip:focus{top:10px}
.it{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400;letter-spacing:-.01em;text-transform:none}
.tag{font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase}
.logo{display:inline-flex;align-items:center;gap:10px;font-weight:800;font-stretch:110%;font-size:19px;letter-spacing:-.03em;text-transform:uppercase}
.logo:before{content:"";width:12px;height:12px;border-radius:50%;background:var(--acc);box-shadow:7px 0 0 var(--star)}
.logo span{margin-left:6px}
.pill{display:inline-flex;align-items:center;gap:10px;min-height:46px;padding:10px 22px;border-radius:999px;border:1.5px solid currentColor;font-weight:600;font-size:15px;transition:background .25s var(--ease),color .25s var(--ease),border-color .25s}
.pill:after{content:"→";transition:transform .25s var(--ease)}.pill:hover:after{transform:translateX(5px)}
.pill.solid{background:var(--acc);border-color:var(--acc);color:var(--on-acc,#fff)}.pill.solid:hover{background:var(--ink);border-color:var(--ink);color:var(--bone)}
.pill:not(.solid):hover{background:var(--ink);color:var(--bone);border-color:var(--ink)}
.dark{background:var(--ink);color:var(--bone);--mut:color-mix(in srgb,var(--bone) 68%,var(--ink));--line:color-mix(in srgb,var(--bone) 22%,transparent)}
.dark .pill:not(.solid):hover,.hero.photo .pill:hover,.hero.block .pill:not(.solid):hover{background:var(--bone);color:var(--ink);border-color:var(--bone)}
.dark .pill.solid:hover{background:var(--bone);border-color:var(--bone);color:var(--ink)}
.top{position:relative;z-index:2;display:flex;align-items:center;justify-content:space-between;gap:24px;padding:22px 0}
.top nav,.bar nav{display:flex;gap:30px}.top nav a,.bar nav a{position:relative;padding:6px 0}
.top nav a:after,.bar nav a:after{content:"";position:absolute;left:0;right:0;bottom:0;height:1.5px;background:currentColor;transform:scaleX(0);transform-origin:left;transition:transform .3s var(--ease)}
.top nav a:hover:after,.bar nav a:hover:after{transform:scaleX(1)}
.bar{position:fixed;left:0;right:0;top:0;z-index:30;background:color-mix(in srgb,var(--bone) 94%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);transform:translateY(-101%);transition:transform .4s var(--ease)}
.bar.show{transform:none}.bar .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:58px}.bar .pill{min-height:38px;padding:6px 16px;font-size:14px}
h1{font-weight:800;font-stretch:var(--stretch,108%);text-transform:uppercase;line-height:.86;letter-spacing:-.05em}
h1 .it{font-size:1.04em;letter-spacing:-.03em;display:inline-block;padding-right:.06em}
.serif h1{font-family:'Instrument Serif',Georgia,serif;font-weight:400;text-transform:none;letter-spacing:-.03em;line-height:.92}
.serif h1 .it{font-size:1em}
.ln{display:block;overflow:hidden;padding:.06em 0 .18em;margin:-.06em 0 -.18em}
.ln>span{display:block;transform:translateY(110%);transition:transform 1.1s var(--ease);transition-delay:calc(var(--i,0)*110ms + 150ms)}
.ready .ln>span{transform:none}
.meta{display:grid;gap:12px}.meta p{max-width:270px;font-size:15px;line-height:1.4;opacity:.86}
.meta strong{font-size:44px;font-weight:800;line-height:1;letter-spacing:-.03em}.meta strong span{color:var(--star)}

/* hero: full photo */
.hero.photo{position:relative;height:100svh;min-height:600px;max-height:1000px;color:var(--bone);overflow:hidden;background:var(--ink);display:flex;flex-direction:column;justify-content:space-between}
.hero-img{position:absolute;inset:-4%;background:var(--img) center 40%/cover;transform:scale(calc(1.1 - var(--hp,0)*.1))}
.hero.photo:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,color-mix(in srgb,var(--ink) 70%,transparent) 0,color-mix(in srgb,var(--ink) 22%,transparent) 30%,color-mix(in srgb,var(--ink) 20%,transparent) 48%,color-mix(in srgb,var(--ink) 90%,transparent) 100%)}
.hero.photo>.wrap{margin:0 auto}
.hero.photo .hb{position:relative;z-index:2;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:30px;align-items:end;padding-bottom:34px}
.hero.photo h1{font-size:clamp(52px,var(--h1,11.6vw),200px)}.hero.photo .meta{justify-items:end;text-align:right;padding-bottom:8px}
/* hero: poster */
.hero.poster{padding-bottom:clamp(30px,4vw,56px)}
.hero.poster .kick{text-align:center;color:var(--mut);margin-top:clamp(10px,2vw,30px)}
.hero.poster h1{text-align:center;font-size:clamp(46px,var(--h1,11vw),190px);margin-top:14px}
.hero.poster h1 .it{color:var(--acc)}
.card-img{position:relative;border-radius:18px;overflow:hidden;margin-top:clamp(22px,3vw,44px);height:clamp(240px,42vw,620px);background:var(--ink)}
.card-img .hero-img{inset:-6%}
.card-img .chip{position:absolute;z-index:2;bottom:18px;background:color-mix(in srgb,var(--bone) 92%,transparent);backdrop-filter:blur(10px);color:var(--ink);border-radius:999px;padding:10px 18px;font-weight:700;font-size:14px}
.card-img .chip.l{left:18px}.card-img .chip.r{right:18px}.card-img .chip b{color:var(--acc)}
/* hero: split */
.hero.split{display:grid;grid-template-columns:minmax(0,1.08fr) minmax(0,.92fr);min-height:min(88svh,800px)}
.hero.split .l{display:flex;flex-direction:column;justify-content:space-between;padding:0 clamp(18px,3.2vw,48px) 34px}
.hero.split .l .top{padding-top:22px}
.hero.split h1{font-size:clamp(50px,var(--h1,8vw),150px);margin:clamp(30px,5vw,70px) 0 26px}
.hero.split .r{position:relative;overflow:hidden;background:var(--ink);min-height:320px}
.hero.split .meta{grid-template-columns:auto 1fr;align-items:center;gap:18px}
/* hero: block */
.hero.block{background:var(--acc);color:var(--on-acc,#fff);position:relative;padding-bottom:clamp(120px,16vw,230px)}
.hero.block .logo:before{background:var(--on-acc,#fff);box-shadow:7px 0 0 var(--star)}
.hero.block h1{font-size:clamp(52px,var(--h1,12.4vw),214px);margin-top:clamp(20px,4vw,60px)}
.hero.block h1 .it{color:var(--star)}
.hero.block .under{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:30px;margin-top:22px}
.hero.block .meta{grid-template-columns:auto 1fr;align-items:center;gap:18px}
.hero.block .pill.solid{background:var(--ink);border-color:var(--ink);color:var(--bone)}
.tilt{position:relative;z-index:3;width:min(1360px,calc(100% - 64px));margin:calc(clamp(120px,16vw,230px)*-1 + 30px) auto 0;height:clamp(230px,36vw,520px);border-radius:18px;overflow:hidden;background:var(--ink);transform:rotate(-1.2deg);box-shadow:0 40px 80px -40px #000a}
.tilt .hero-img{inset:-6%}

section{padding:clamp(52px,6.6vw,104px) 0}
.lab{display:flex;align-items:center;gap:10px;color:var(--mut)}.lab:before{content:"";width:8px;height:8px;border-radius:50%;background:var(--acc)}
.rv{opacity:0;transform:translateY(28px);transition:opacity .9s var(--ease),transform .9s var(--ease);transition-delay:calc(var(--d,0)*90ms)}.rv.in{opacity:1;transform:none}
.clip{clip-path:inset(0 0 100% 0);transition:clip-path 1.2s var(--ease);border-radius:14px;overflow:hidden}.clip.in{clip-path:inset(0)}
.clip img{width:100%;object-fit:cover;transform:scale(1.15);transition:transform 1.6s var(--ease)}.clip.in img{transform:none}
.state{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,3fr);gap:40px;align-items:start}
.state h2{font-weight:500;font-size:clamp(26px,3.5vw,56px);line-height:1.05;letter-spacing:-.035em}
.sub2{font-size:clamp(18px,1.6vw,24px);color:var(--mut);margin-top:16px}
.facts{display:grid;grid-template-columns:repeat(3,1fr);margin-top:clamp(32px,4.6vw,64px);border-top:1px solid var(--line)}
.facts div{padding:20px 20px 0 0;border-right:1px solid var(--line);margin-right:20px}.facts div:last-child{border:0;margin:0}
.facts strong{display:block;font-size:clamp(20px,2vw,30px);font-weight:700;letter-spacing:-.03em;margin-top:8px}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:32px}
/* services: giant rows */
.rows{border-top:1.5px solid currentColor;margin-top:24px}
.row{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,320px);gap:30px;align-items:end;padding:12px 0 16px;border-bottom:1.5px solid currentColor;transition:color .3s}
.row h3{font-weight:800;font-stretch:var(--stretch,108%);text-transform:uppercase;font-size:clamp(40px,var(--rowsz,8.6vw),150px);line-height:.88;letter-spacing:-.05em;transition:transform .6s var(--ease)}
.serif .row h3{font-family:'Instrument Serif',Georgia,serif;font-weight:400;text-transform:none;letter-spacing:-.03em}
.row p{font-size:15px;color:var(--mut);padding-bottom:.8vw}
.row:hover{color:var(--acc)}.row:hover h3{transform:translateX(2vw)}
.float{position:fixed;left:0;top:0;width:300px;height:380px;border-radius:14px;overflow:hidden;pointer-events:none;z-index:25;opacity:0;transform:translate(var(--fx,0),var(--fy,0)) scale(.86) rotate(-3deg);transition:opacity .3s,transform .5s var(--ease);box-shadow:0 30px 60px -20px #0009}
.float.on{opacity:1;transform:translate(var(--fx,0),var(--fy,0)) rotate(-3deg)}
.float img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .35s}.float img.on{opacity:1}
/* services: index */
.idx{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:clamp(30px,6vw,110px);align-items:start}
.idx .left{position:sticky;top:96px}
.big2{font-weight:800;font-stretch:var(--stretch,108%);text-transform:uppercase;font-size:clamp(38px,5.6vw,96px);line-height:.9;letter-spacing:-.045em;margin-top:18px}
.serif .big2{font-family:'Instrument Serif',Georgia,serif;font-weight:400;text-transform:none;letter-spacing:-.03em;line-height:.95}
.idx .left p{color:var(--mut);margin-top:20px;max-width:380px}
.grp{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--acc);margin:28px 0 4px}.grp:first-child{margin-top:0}
.item{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:20px;align-items:baseline;padding:16px 0;border-bottom:1px solid var(--line);transition:padding .35s var(--ease)}
.item:hover{padding-left:14px}.item h3{font-size:clamp(20px,2vw,28px);font-weight:700;letter-spacing:-.03em;line-height:1.05}.item p{color:var(--mut);font-size:15px}
.item.solo{grid-template-columns:1fr}
/* about */
.pts{display:grid;gap:14px;margin-top:22px}.pts li{padding-top:14px;border-top:1px solid var(--line)}.pts strong{display:block;font-size:19px}
.abt{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:clamp(30px,6vw,110px);align-items:start}
.abt .left{position:sticky;top:96px}.abt .left>p{color:var(--mut);margin-top:20px;max-width:420px;font-size:18px}
.abt .clip img{aspect-ratio:4/5}.band .clip img{aspect-ratio:21/9}
/* reviews */
.nums{display:flex;flex-wrap:wrap;gap:clamp(24px,5vw,90px);margin-top:20px}
.num strong{display:block;font-weight:800;font-stretch:var(--stretch,108%);font-size:clamp(64px,11vw,190px);line-height:.86;letter-spacing:-.05em}.num strong i{font-style:normal;color:var(--acc);font-size:.5em;vertical-align:.5em;margin-left:.06em}
.num span{display:block;margin-top:10px;color:var(--mut)}.num a{display:inline-block;margin-top:6px;font-weight:600;font-size:14px;text-decoration:underline;text-underline-offset:5px}
.qs{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:clamp(30px,4vw,56px)}
.q{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:26px;transition:background .3s,color .3s}.q:hover{background:var(--ink);color:var(--bone)}
.q p{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:30px;line-height:1.08}.q cite{display:block;font-style:normal;font-size:13px;opacity:.7;margin-top:22px}
.revtxt{font-size:clamp(20px,2vw,28px);max-width:820px;margin-top:26px;letter-spacing:-.02em;line-height:1.25}
.quotes{display:flex;gap:16px;overflow-x:auto;scrollbar-width:none;padding:4px 2px 10px;margin-top:clamp(30px,4vw,56px);cursor:grab}.quotes::-webkit-scrollbar{display:none}
.quotes .quote{flex:0 0 min(400px,82%);background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:26px;transition:background .3s,color .3s}
.quotes .quote:hover{background:var(--ink);color:var(--bone)}
.review-body{display:flex;flex-direction:column;justify-content:space-between;gap:34px;height:100%}
.review-origin{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--acc)}
.quotes .quote p:not(.review-origin){font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:30px;line-height:1.08}
.quotes .quote cite{display:block;font-style:normal;font-size:13px;opacity:.7}
.review-source{display:inline-block;margin-top:10px;font-size:13px;font-weight:600;text-decoration:underline;text-underline-offset:4px}
/* visit */
.phone{display:block;font-weight:800;font-stretch:var(--stretch,108%);font-size:clamp(44px,10.6vw,184px);line-height:.9;letter-spacing:-.05em;margin-top:14px;transition:color .3s}.phone:hover{color:var(--star)}
.vgrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(30px,6vw,110px);margin-top:clamp(30px,4.6vw,64px);padding-top:30px;border-top:1px solid var(--line)}
address{font-style:normal;font-size:clamp(22px,2.2vw,32px);font-weight:600;letter-spacing:-.02em;line-height:1.2;margin-top:12px}
.find{color:var(--mut);margin-top:10px;max-width:420px}
table{border-collapse:collapse;width:100%;font-size:16px;margin-top:8px}
th{text-align:left;font-weight:400}td{text-align:right;white-space:nowrap}th,td{padding:12px 0;border-bottom:1px solid var(--line)}
tr.today th,tr.today td{color:var(--star);font-weight:700}
.today-tag{font-size:10px;letter-spacing:.1em;text-transform:uppercase;border:1px solid currentColor;border-radius:999px;padding:2px 8px;margin-left:10px}
.hol{margin-top:16px;font-size:14px;color:var(--mut)}.hol a{color:inherit;text-decoration:underline;text-underline-offset:3px}
footer{background:var(--ink);color:color-mix(in srgb,var(--bone) 62%,var(--ink));padding:0 0 28px;overflow:hidden}
.word{font-weight:800;font-stretch:112%;text-transform:uppercase;font-size:var(--wordsz,15vw);line-height:.8;letter-spacing:-.055em;color:transparent;-webkit-text-stroke:1.5px color-mix(in srgb,var(--bone) 36%,transparent);white-space:nowrap;text-align:center;user-select:none}
footer .wrap{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;font-size:12.5px;margin-top:22px}footer span{max-width:720px}
.dock{display:none}
@media(max-width:860px){.wrap{width:calc(100% - 36px)}.top nav,.bar nav{display:none}.logo{font-size:16px}.top .pill{min-height:40px;padding:8px 14px;font-size:14px;white-space:nowrap}
.hero.photo .hb{grid-template-columns:1fr;gap:18px}.hero.photo .meta{justify-items:start;text-align:left;grid-template-columns:auto 1fr;align-items:center}
.hero.split{grid-template-columns:1fr}.hero.split .r{order:-1;height:42svh;min-height:260px}.hero.split .l{padding:0 18px 26px}.hero.split .l .top{position:absolute;left:18px;right:18px;top:0;color:var(--bone)}.hero.split{position:relative}.hero.split h1{margin:26px 0 20px}
.hero.block .under{grid-template-columns:1fr}.tilt{width:calc(100% - 36px)}.card-img .chip{font-size:12.5px;padding:8px 13px;bottom:12px}.card-img .chip.l{left:12px;bottom:auto;top:12px}.card-img .chip.r{right:12px}
.state{grid-template-columns:1fr;gap:16px}.facts{grid-template-columns:1fr}.facts div{border-right:0;margin:0;border-bottom:1px solid var(--line);padding:16px 0}
.row{grid-template-columns:1fr;gap:4px}.row p{padding:0}.float{display:none}.idx,.abt{grid-template-columns:1fr}.idx .left,.abt .left{position:static}.item{grid-template-columns:1fr;gap:4px}.vgrid{grid-template-columns:1fr}
body{padding-bottom:58px}.dock{display:grid;grid-template-columns:1.3fr 1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:40;background:var(--bone);color:var(--ink);border-top:1px solid var(--line)}.dock a{display:flex;align-items:center;justify-content:center;min-height:56px;font-size:14.5px;font-weight:700;border-right:1px solid var(--line)}.dock a:first-child{background:var(--acc);color:var(--on-acc,#fff)}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*:before,*:after{animation:none!important;transition:none!important}.ln>span{transform:none}.rv{opacity:1;transform:none}.clip{clip-path:none}.clip img{transform:none}.hero-img{transform:none}}
"""

JS = """<script>
(()=>{
const root=document.documentElement,reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
requestAnimationFrame(()=>requestAnimationFrame(()=>root.classList.add('ready')));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1,rootMargin:'0px 0px -6% 0px'});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
// photos wipe in when their block arrives (watch the parent: a fully clipped element never counts as visible)
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.querySelectorAll('.clip').forEach(c=>c.classList.add('in'));cio.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.cliphost').forEach(el=>cio.observe(el));
// hero photo eases back on scroll; slim nav bar appears after the hero
const bar=document.getElementById('bar'),hero=document.querySelector('.hero');let tick=false;
const upd=()=>{const h=hero.offsetHeight||innerHeight;if(!reduce)root.style.setProperty('--hp',Math.min(scrollY/h,1).toFixed(3));bar.classList.toggle('show',scrollY>h*.8);tick=false};
addEventListener('scroll',()=>{if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});upd();
// photo follows the pointer over the big service rows (mouse only)
const fl=document.getElementById('float');
if(fl&&matchMedia('(hover:hover) and (pointer:fine)').matches&&!reduce){const imgs=[...fl.querySelectorAll('img')];
document.querySelectorAll('.row').forEach((m,n)=>{m.addEventListener('pointerenter',()=>{imgs.forEach((im,i)=>im.classList.toggle('on',i===n%imgs.length));fl.classList.add('on')});m.addEventListener('pointerleave',()=>fl.classList.remove('on'))});
addEventListener('pointermove',e=>{fl.style.setProperty('--fx',Math.min(e.clientX+28,innerWidth-330)+'px');fl.style.setProperty('--fy',(e.clientY-190)+'px')},{passive:true})}
// footer wordmark always spans the page exactly
const word=document.querySelector('.word');
const fit=()=>{if(!word)return;word.style.fontSize='100px';const w=word.firstElementChild.offsetWidth;if(w)word.style.fontSize=Math.min(100*(innerWidth*.955)/w,innerWidth*.3)+'px'};
fit();addEventListener('resize',fit);if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);
// today's hours in the shop's time zone
const wd=new Intl.DateTimeFormat('en-US',{weekday:'short',timeZone:'America/Los_Angeles'}).format(new Date());
const d=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(wd);
document.querySelectorAll('[data-today]').forEach(el=>{try{el.textContent=JSON.parse(el.dataset.today)[(d+6)%7]}catch(e){}});
const row=document.querySelector('tr[data-day="'+d+'"]');
if(row){row.classList.add('today');const t=document.createElement('span');t.className='today-tag';t.textContent='Today';row.querySelector('th').append(t)}
})();
</script>"""


def tel(p):
    return "+1" + "".join(c for c in p if c.isdigit())


def h1(s):
    a, b = s["h1"]
    if s["art"].get("serif"):
        return f'<h1><span class="ln"><span>{esc(a)}</span></span><span class="ln"><span style="--i:1"><span class="it" style="color:var(--acc)">{esc(b)}</span></span></span></h1>'
    return f'<h1><span class="ln"><span>{esc(a)}</span></span><span class="ln"><span style="--i:1"><span class="it">{esc(b)}</span></span></span></h1>'


def nav(s, cls="top"):
    t = tel(s["phone"])
    links = f'<a href="#services">{s.get("svc_nav", "Services")}</a><a href="#reviews">Reviews</a><a href="#visit">Visit</a>'
    return f'<a href="#top" class="logo" aria-label="{esc(s["short"])}"><span>{esc(s["art"].get("mark", s["short"]))}</span></a><nav class="tag" aria-label="Sections">{links}</nav><a class="pill{" solid" if cls == "bar" else ""}" href="tel:{t}">{s["phone"]}</a>'


def meta(s):
    num, label, _ = s["ratings"][0]
    return f'<div class="meta"><strong>{num}<span>★</span></strong><p><span class="tag">{label}</span><br>{esc(s["kicker"])}</p></div>'


def hero(s):
    art = s["art"]
    img = f'style="--img:url({s["photos"][0]})" role="img" aria-label="{esc(s["alt"][0])}"'
    t = tel(s["phone"])
    kind = art["hero"]
    if kind == "photo":
        return f'<header class="hero photo" id="top"><div class="hero-img" {img}></div><div class="wrap top">{nav(s)}</div><div class="wrap hb">{h1(s)}{meta(s)}</div></header>'
    if kind == "poster":
        num, label, _ = s["ratings"][0]
        return f'<header class="hero poster" id="top"><div class="wrap"><div class="top">{nav(s)}</div><p class="tag kick">{esc(s["kicker"])}</p>{h1(s)}<div class="card-img"><div class="hero-img" {img}></div><span class="chip l"><b>{num} ★</b> {label}</span><a class="chip r" href="tel:{t}">Call {s["phone"]} →</a></div></div></header>'
    if kind == "split":
        return f'<header class="hero split" id="top"><div class="l"><div class="top">{nav(s)}</div><div>{h1(s)}{meta(s)}</div></div><div class="r"><div class="hero-img" {img}></div></div></header>'
    return f'<header class="hero block" id="top"><div class="wrap"><div class="top">{nav(s)}</div>{h1(s)}<div class="under">{meta(s)}<div class="cta" style="margin:0;justify-content:flex-end;align-items:flex-end"><a class="pill solid" href="tel:{t}">Call {s["phone"]}</a><a class="pill" href="#visit">Hours &amp; directions</a></div></div></div></header><div class="tilt"><div class="hero-img" {img}></div></div>'


def statement(s):
    t = tel(s["phone"])
    today = f"<strong data-today='{json.dumps(s['hours'])}'>See hours below</strong>" if s.get("hours") else "<strong>Call for hours</strong>"
    sub = f'<p class="sub2 rv">{esc(s["sub"])}</p>' if s.get("sub") else ""
    return f"""<section><div class="wrap">
<div class="state"><p class="tag lab rv">{esc(s['art'].get('about_label', 'The shop'))}</p><div><h2 class="rv">{esc(s['lede'])}</h2>{sub}</div></div>
<div class="facts"><div class="rv"><span class="tag lab">Today</span>{today}</div><div class="rv" style="--d:1"><span class="tag lab">Where</span><strong>{s['addr'].replace('<br>', ', ')}</strong></div><div class="rv" style="--d:2"><span class="tag lab">Call</span><strong><a href="tel:{t}">{s['phone']}</a></strong></div></div>
<div class="cta rv"><a class="pill solid" href="tel:{t}">Call the shop</a><a class="pill" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a></div>
</div></section>"""


def services(s):
    label = s.get("svc_label", "What we do")
    items = [(g, n, d) for g, its in s["services"] for n, d in its]
    if s["art"].get("svc") == "rows":
        rows = "".join(f'<div class="row rv"><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for _, n, d in items)
        fl = '<div class="float" id="float" aria-hidden="true">' + "".join(f'<img alt="" src="{p}">' for p in s["photos"]) + "</div>"
        note = f'<p class="hol rv" style="margin-top:18px">{esc(s["svc_note"])}</p>' if s.get("svc_note") else ""
        return f'<section id="services" style="padding-top:0"><div class="wrap"><p class="tag lab rv">{label}</p><div class="rows">{rows}</div>{note}</div>{fl}</section>'
    out, last = "", None
    for g, n, d in items:
        if g and g != last:
            out += f'<p class="grp rv">{esc(g)}</p>'
            last = g
        out += f'<div class="item rv{"" if d else " solo"}"><h3>{esc(n)}</h3>{"<p>" + esc(d) + "</p>" if d else ""}</div>'
    note = f'<p>{esc(s["svc_note"])}</p>' if s.get("svc_note") else ""
    text = f'<p>{esc(s["svc_text"])}</p>' if s.get("svc_text") else ""
    return f'<section class="dark" id="services"><div class="wrap idx"><div class="left"><p class="tag lab rv">{label}</p><h2 class="big2 rv">{esc(s["svc_title"])}</h2>{text}{note}</div><div>{out}</div></div></section>'


def about(s):
    a = s.get("about")
    img = f'<div class="clip"><img loading="lazy" alt="{esc(s["alt"][1])}" src="{s["photos"][1]}"></div>'
    if not a:
        return f'<section class="band cliphost"><div class="wrap">{img}</div></section>'
    pts = "".join(f"<li class='rv'><strong>{esc(h)}</strong>{esc(t)}</li>" for h, t in a.get("points", []))
    dark = "" if s["art"].get("svc") != "rows" else " dark"
    return f'<section class="{dark.strip()}"><div class="wrap abt cliphost"><div class="left"><p class="tag lab rv">Good to know</p><h2 class="big2 rv">{esc(a["title"])}</h2><p class="rv">{esc(a["text"])}</p>{f"<ul class=pts>{pts}</ul>" if pts else ""}</div>{img}</div></section>'


def reviews(s):
    nums = ""
    for num, label, url in s["ratings"]:
        link = f'<a href="{url}" target="_blank" rel="noopener noreferrer">Read the reviews ↗</a>' if url else ""
        nums += f'<div class="num rv"><strong>{num}<i>★</i></strong><span>{label}</span>{link}</div>'
    txt = f'<p class="revtxt rv">{esc(s["rev_text"])}</p>' if s.get("rev_text") else ""
    if s.get("track"):
        body = s["track"]
    elif s.get("quotes"):
        body = '<div class="qs">' + "".join(f'<blockquote class="q rv"><p>“{esc(q)}”</p><cite>From Google reviews</cite></blockquote>' for q in s["quotes"]) + "</div>"
    else:
        body = ""
    return f'<section id="reviews"><div class="wrap"><p class="tag lab rv">Reviews</p><div class="nums">{nums}</div>{txt}{body}</div></section>'


def visit(s):
    t = tel(s["phone"])
    if s.get("hours"):
        rows = "".join(f'<tr data-day="{(i + 1) % 7}"><th scope="row">{d}</th><td>{s["hours"][i]}</td></tr>' for i, d in enumerate(DAYS))
        hrs = f'<span class="tag lab">Hours</span><table>{rows}</table><p class="hol"><strong>Holiday hours.</strong> Hours can change on holidays, including Veterans Day, Thanksgiving, Christmas and New Year\'s Day. Call <a href="tel:{t}">{s["phone"]}</a> before you come in.</p>'
    else:
        hrs = f'<span class="tag lab">Hours</span><p class="revtxt" style="margin-top:12px">Call <a href="tel:{t}" style="text-decoration:underline;text-underline-offset:5px">{s["phone"]}</a> for current availability and hours.</p>'
    find = f'<p class="find">{esc(s["find"])}</p>' if s.get("find") else ""
    return f"""<section class="dark" id="visit"><div class="wrap"><p class="tag lab rv">Visit or call</p>
<a class="phone rv" href="tel:{t}">{s['phone']}</a>
<div class="vgrid"><div class="rv"><span class="tag lab">Address</span><address>{s['addr']}</address>{find}
<div class="cta"><a class="pill solid" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a><a class="pill" href="tel:{t}">Call the shop</a></div></div>
<div class="rv" style="--d:1">{hrs}</div></div></div></section>"""


def build(folder, s):
    art = s["art"]
    t = tel(s["phone"])
    v = f":root{{--ink:{art['ink']};--bone:{art['bone']};--paper:{art.get('paper', '#ffffff')};--acc:{art['acc']};--star:{art['star']};--on-acc:{art.get('on_acc', '#fff')};--stretch:{art.get('stretch', '108%')};--h1:{art.get('h1', '11vw')};--rowsz:{art.get('rowsz', '8.6vw')};--wordsz:{art.get('wordsz', '15vw')}}}"
    body = f"""<a class="skip" href="#main">Skip to content</a>
<div class="bar" id="bar"><div class="wrap">{nav(s, 'bar')}</div></div>
{hero(s)}
<main id="main">
{statement(s)}
{services(s)}
{about(s)}
{reviews(s)}
{visit(s)}
</main>
<footer><div class="word" aria-hidden="true"><span>{esc(art.get('word', s['short']))}</span></div><div class="wrap"><strong>{esc(s['footer'])}</strong><span>Concept website by Phan-Rodriguez LLC. Not the official site of this business. Photos are stock images.</span></div></footer>
<nav class="dock" aria-label="Quick actions"><a href="tel:{t}">Call</a><a href="{s['maps']}" target="_blank" rel="noopener noreferrer">Directions</a><a href="#visit">Hours</a></nav>"""
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="{art['ink']}">
<title>{esc(s['short'])} | {esc(s['kicker'].split(' · ')[-1])}</title>
<meta name="description" content="{esc(s['short'])}. {esc(s['lede']).replace('"', "'")} Concept site.">
<link rel="preload" href="fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>{v}{CSS}</style>
</head>
<body class="{'serif' if art.get('serif') else ''}">
{body}
{JS}
{s.get('extra_js', '')}
</body>
</html>
"""
    out = OUT / folder
    (out / "fonts").mkdir(parents=True, exist_ok=True)
    for f in FONTS.iterdir():
        shutil.copy(f, out / "fonts" / f.name)
    (out / "index.html").write_text(page)
    print("built", folder, art["hero"])


S = L.SITES
PX, U = L.PX, L.U
# Art direction per site. Everything else (facts, services, hours, ratings) is inherited.
ART = {
    "lockworx": dict(hero="split", ink="#1C1F20", bone="#F1EFE8", acc="#2C6E91", star="#E6C72F", h1="8.6vw", svc="index", mark="Lockworx", word="Lockworx", wordsz="19vw"),
    "el-rey": dict(hero="block", ink="#0B1C4A", bone="#FFF7E6", paper="#fff", acc="#C2261F", star="#F6C744", h1="12vw", stretch="78%", svc="rows", rowsz="8.4vw", mark="El Rey", word="El Rey", wordsz="26vw", about_label="The taqueria"),
    "don-cortez-tires": dict(hero="poster", ink="#0F2244", bone="#F2F4F8", acc="#1C4FB8", star="#F2C230", h1="10.4vw", svc="index", mark="Don Cortez", word="Don Cortez", wordsz="16vw"),
    "alejandros-tree-service": dict(hero="split", serif=True, ink="#14301F", bone="#F3F1E7", acc="#2F7A4F", star="#C9D66B", h1="9.4vw", svc="rows", rowsz="7.6vw", mark="Alejandros", word="Alejandros", wordsz="17vw", about_label="Tree care"),
    "sinaloa-tires": dict(hero="block", ink="#1D1F23", bone="#FAF6EE", acc="#D14A0E", star="#FFD23F", h1="10vw", svc="index", mark="Sinaloa Tires", word="Sinaloa", wordsz="22vw"),
    "king-tire-shop": dict(hero="photo", ink="#131A36", bone="#F4F1EA", acc="#C8242C", star="#F6C744", h1="11.8vw", stretch="74%", svc="index", mark="King Tire Shop", word="King Tire", wordsz="19vw"),
    "43s-mufflers-brakes": dict(hero="poster", ink="#131210", bone="#F3EEDF", acc="#8F3A29", star="#E8B90E", h1="9.6vw", svc="index", mark="43's Mufflers & Brakes", word="43's", wordsz="34vw"),
    "tepa-tire": dict(hero="split", ink="#0E1E4A", bone="#F4EFE3", acc="#C4551E", star="#E9A23B", h1="9.6vw", stretch="78%", svc="rows", rowsz="7.4vw", mark="Tepa", word="Tepa Tire", wordsz="19vw"),
}
SITES = {}
for k, art in ART.items():
    s = dict(S[k])
    s["art"] = art
    SITES[k] = s
SITES["el-rey"]["photos"] = (PX(35020122, 1800), PX(14006131), PX(28992999))
SITES["el-rey"]["services"] = [("", [(n, d) for n, d in S["el-rey"]["services"][0][1]])]
SITES["alejandros-tree-service"]["photos"] = (PX(12596112, 1600), PX(31127615))
SITES["tepa-tire"]["photos"] = (U("1578844251758-2f71da64c96f", 1400, 1600), PX(6870299), PX(8985660))
SITES["tepa-tire"]["lede"] = "New and used tires, flat repair, mounting and balancing, and brake work on South Mountain Avenue."

# A C Tires (facts verified 2026-11-10 against Google Maps; reviews link to Yelp and Birdeye)
SITES["ac-tires"] = dict(
    art=dict(hero="photo", ink="#101E47", bone="#F3F1EA", acc="#C2261F", star="#F0C24B", h1="10.8vw", svc="index", mark="A C Tires", word="A C Tires", wordsz="19vw"),
    short="A C Tires", kicker="New and used tires · Ontario, California", footer="A C Tires · Ontario, CA",
    h1=("Flat at 7 PM?", "We're still open."), lede="New and used tires, flat repair and mount-and-balance at the blue shop on California Street. Open until 8 on weeknights, and open Sundays.",
    phone="(909) 391-4636", addr="301 W California St<br>Ontario, CA 91762", maps="https://www.google.com/maps/search/?api=1&query=A+C+Tires+301+W+California+St+Ontario+CA+91762", find="Look for the blue building.",
    hours=["8:00 AM – 8:00 PM"] * 5 + ["8:00 AM – 7:00 PM", "8:00 AM – 6:00 PM"],
    ratings=[("4.4", "Google · 324 reviews", "https://www.google.com/maps/search/?api=1&query=A+C+Tires+301+W+California+St+Ontario+CA+91762")],
    services=[("", [("New tires", "Fresh rubber in the sizes people around here actually drive."), ("Used tires", "Good used tires for when the budget says “not today” to a full new set."), ("Flat repair", "Nail in the tread? In and out fast, weekends included."), ("Mount & balance", "Bought tires elsewhere? We'll mount and balance them."), ("Wheels", "Ask what's in stock for your car.")])],
    svc_title="Tires. That's the shop.", svc_text="No waiting-room upsell. Pull in, tell us what you need, and get back on the road.",
    photos=(U("1792792944402-5e94ce198dce", 2000, 1300), U("1578844251758-2f71da64c96f", 1600, 700)), alt=("Gloved hands mounting a tire in a workshop", "Stacks of tires in a tire shop"),
    track=V.track(V.AC_REVIEWS), extra_js=V.CAROUSEL_JS,
)

if __name__ == "__main__":
    OUT = pathlib.Path(sys.argv[1])
    only = sys.argv[2:]  # optional: site folder names
    for folder, s in SITES.items():
        if not only or folder in only:
            build(folder, s)
