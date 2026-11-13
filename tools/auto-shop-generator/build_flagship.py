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
body{margin:0;background:var(--bone);color:var(--ink);font:400 17px/1.5 Archivo,'Segoe UI',system-ui,Arial,sans-serif;-webkit-font-smoothing:antialiased}
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
.ln>span{display:block;transform:none;transition:transform 1.1s var(--ease);transition-delay:calc(var(--i,0)*110ms + 150ms)}
.motion-ready:not(.ready) .ln>span{transform:translateY(110%)}
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
.hero.split{display:grid;grid-template-columns:minmax(0,1.08fr) minmax(0,.92fr);min-height:0}
.hero.split .l{display:flex;flex-direction:column;justify-content:space-between;padding:0 clamp(18px,3.2vw,48px) 34px}
.hero.split .l .top{padding-top:22px}
.hero.split h1{font-size:clamp(50px,var(--h1,8vw),150px);margin:clamp(36px,6vw,96px) 0 26px}
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

section{padding:clamp(44px,5.4vw,84px) 0}
.lab{display:flex;align-items:center;gap:10px;color:var(--mut)}.lab:before{content:"";width:8px;height:8px;border-radius:50%;background:var(--acc)}
.rv{opacity:1;transform:none;transition:opacity .9s var(--ease),transform .9s var(--ease);transition-delay:calc(var(--d,0)*90ms)}.motion-ready .rv:not(.in){opacity:0;transform:translateY(28px)}
.clip{clip-path:inset(0);transition:clip-path 1.2s var(--ease);border-radius:14px;overflow:hidden}.motion-ready .clip:not(.in){clip-path:inset(0 0 100% 0)}
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
.abt{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(30px,5vw,80px);align-items:center}
.abt .left{position:static}.abt .left>p{color:var(--mut);margin-top:20px;max-width:420px;font-size:18px}
.abt .clip img{aspect-ratio:4/3}.band .clip img{aspect-ratio:21/9}
/* reviews */
.revhead{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:24px clamp(30px,6vw,110px);margin-top:20px}.revhead .revtxt{flex:1 1 380px;margin:0 0 10px;max-width:640px}
.nums{display:flex;flex-wrap:wrap;gap:clamp(24px,5vw,90px)}
.num strong{display:block;font-weight:800;font-stretch:var(--stretch,108%);font-size:clamp(64px,11vw,190px);line-height:.86;letter-spacing:-.05em}.num strong i{font-style:normal;color:var(--acc);font-size:.5em;vertical-align:.5em;margin-left:.06em}
.num span{display:block;margin-top:10px;color:var(--mut)}.num a{display:inline-block;margin-top:6px;font-weight:600;font-size:14px;text-decoration:underline;text-underline-offset:5px}
.qs{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:clamp(30px,4vw,56px)}
.q{display:block;background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:26px;transition:background .3s,color .3s}.q:hover{background:var(--ink);color:var(--bone)}
.q p{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:30px;line-height:1.08}.q cite{display:block;font-style:normal;font-size:13px;opacity:.7;margin-top:22px}
.revtxt{font-size:clamp(20px,2vw,28px);max-width:820px;margin-top:26px;letter-spacing:-.02em;line-height:1.25}
.quotes{display:flex;gap:16px;overflow-x:auto;scrollbar-width:none;padding:4px 2px 10px;margin-top:clamp(30px,4vw,56px);cursor:grab}.quotes::-webkit-scrollbar{display:none}
.quotes .quote{flex:1 0 min(380px,82%);background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:26px;transition:background .3s,color .3s}
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
.map{display:block;width:100%;height:clamp(200px,22vw,300px);border:0;border-radius:14px;margin-top:26px;filter:grayscale(.2)}
.hol{margin-top:16px;font-size:14px;color:var(--mut)}.hol a{color:inherit;text-decoration:underline;text-underline-offset:3px}
footer{background:var(--ink);color:color-mix(in srgb,var(--bone) 62%,var(--ink));padding:0 0 28px;overflow:hidden}
.word{font-weight:800;font-stretch:112%;text-transform:uppercase;font-size:var(--wordsz,15vw);line-height:.8;letter-spacing:-.055em;color:transparent;-webkit-text-stroke:1.5px color-mix(in srgb,var(--bone) 36%,transparent);white-space:nowrap;text-align:center;user-select:none}
footer .wrap{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;font-size:12.5px;margin-top:22px}footer span{max-width:720px}
.dock{display:none}
/* per-site variants (see vary()) */
.accent{background:var(--acc);color:var(--on-acc);--mut:color-mix(in srgb,var(--on-acc) 82%,var(--acc));--line:color-mix(in srgb,var(--on-acc) 32%,transparent)}
.accent .pill.solid{background:var(--ink);border-color:var(--ink);color:var(--bone)}.accent .pill:hover,.accent .pill.solid:hover{background:var(--on-acc);border-color:var(--on-acc);color:var(--acc)}
.accent tr.today th,.accent tr.today td{color:inherit;font-weight:800}.accent .lab:before{background:currentColor}.accent .phone:hover{color:var(--ink)}
.lightv{border-top:1.5px solid var(--ink)}.lightv tr.today th,.lightv tr.today td{color:var(--acc)}.lightv .phone:hover{color:var(--acc)}
.sh-sq .pill,.sh-sq .card-img,.sh-sq .tilt,.sh-sq .clip,.sh-sq .q,.sh-sq .quotes .quote,.sh-sq .map,.sh-sq .chip,.sh-sq .cardx,.sh-sq .facts,.sh-sq .float,.sh-sq .today-tag{border-radius:0}
.sh-soft .pill,.sh-soft .chip,.sh-soft .today-tag{border-radius:8px}.sh-soft .card-img,.sh-soft .tilt,.sh-soft .clip,.sh-soft .q,.sh-soft .quotes .quote,.sh-soft .map,.sh-soft .cardx{border-radius:8px}
.lb-line .lab:before{width:22px;height:2px;border-radius:0}.lb-sq .lab:before{border-radius:0;width:7px;height:7px}
.lg-bar .logo:before{width:5px;height:18px;border-radius:0;box-shadow:none}.lg-bar .logo span{margin-left:0}.lg-none .logo:before{display:none}.lg-none .logo span{margin-left:0}
.ft-solid .word{color:var(--acc);-webkit-text-stroke:0}.ft-bone .word{color:color-mix(in srgb,var(--bone) 13%,var(--ink));-webkit-text-stroke:0}.ft-none .word{display:none}.ft-none footer{padding-top:14px}
.fx-bar .facts{background:var(--ink);color:var(--bone);border:0;border-radius:16px;padding:4px 26px 24px}.fx-bar .facts div{border-color:color-mix(in srgb,var(--bone) 22%,transparent)}.fx-bar .facts .lab{color:color-mix(in srgb,var(--bone) 70%,var(--ink))}
.st-center .state{grid-template-columns:1fr;justify-items:center;text-align:center;gap:14px}.st-center .state h2{max-width:1040px}.st-center .state+.facts+.cta,.st-center .cta.rv{justify-content:center}
.rv-row .num strong{font-size:clamp(46px,5.4vw,84px)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:clamp(24px,3vw,40px)}
.cardx{border:1.5px solid var(--line);border-radius:14px;padding:22px;min-height:160px;display:flex;flex-direction:column;justify-content:space-between;gap:24px;transition:background .3s,color .3s,border-color .3s}
.cardx:hover{background:var(--ink);color:var(--bone);border-color:var(--ink)}.cardx h3{font-size:clamp(22px,2.1vw,30px);font-weight:700;letter-spacing:-.03em;line-height:1.05}.cardx p{font-size:15px;opacity:.72}.cardx .grp{margin:0}
.cardhead{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:16px 60px}.cardhead p{max-width:420px;color:var(--mut)}
@media(max-width:860px){.wrap{width:calc(100% - 36px)}.top nav,.bar nav{display:none}.logo{font-size:16px}.top .pill{min-height:40px;padding:8px 14px;font-size:14px;white-space:nowrap}
.hero.photo .hb{grid-template-columns:1fr;gap:18px;padding-bottom:78px}.hero.photo .meta{justify-items:start;text-align:left;grid-template-columns:auto 1fr;align-items:center}
.hero.split{grid-template-columns:1fr}.hero.split .r{order:-1;height:42svh;min-height:260px}.hero.split .l{padding:0 18px 26px}.hero.split .l .top{position:absolute;left:18px;right:18px;top:0;color:var(--bone)}.hero.split{position:relative}.hero.split h1{margin:26px 0 20px}
.hero.block .under{grid-template-columns:1fr}.tilt{width:calc(100% - 36px)}.card-img .chip{font-size:12.5px;padding:8px 13px;bottom:12px}.card-img .chip.l{left:12px;bottom:auto;top:12px}.card-img .chip.r{right:12px}
.state{grid-template-columns:1fr;gap:16px}.facts{grid-template-columns:1fr}.facts div{border-right:0;margin:0;border-bottom:1px solid var(--line);padding:16px 0}
.row{grid-template-columns:1fr;gap:4px}.row p{padding:0}.float{display:none}.idx,.abt{grid-template-columns:1fr}.idx .left,.abt .left{position:static}.item{grid-template-columns:1fr;gap:4px}.vgrid{grid-template-columns:1fr}
body{padding-bottom:58px}.dock{display:grid;grid-template-columns:1.3fr 1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:40;background:var(--bone);color:var(--ink);border-top:1px solid var(--line)}.dock a{display:flex;align-items:center;justify-content:center;min-height:56px;font-size:14.5px;font-weight:700;border-right:1px solid var(--line)}.dock a:first-child{background:var(--acc);color:var(--on-acc,#fff)}}
/* Keep real content within its container, including classic-scrollbar viewports. */
.top,.bar .wrap{flex-wrap:wrap}
.logo{min-width:0;max-width:100%;overflow-wrap:anywhere}
.logo:before{flex-shrink:0}.logo span{min-width:0}
.top .pill,.bar .pill{flex-shrink:0;max-width:100%}
h1,h2,h3,.phone,address{overflow-wrap:anywhere}
.cards{grid-template-columns:repeat(auto-fit,minmax(min(250px,100%),1fr))}
@media(max-width:860px){
html{scroll-padding-top:140px}
.top,.bar .wrap{gap:10px 16px}.bar .wrap{padding:8px 0}
.top .logo,.bar .logo{flex:1 1 160px}
.top .pill,.bar .pill{white-space:nowrap}
.row h3{font-size:clamp(32px,7vw,60px)}
.phone{font-size:clamp(26px,7.8vw,64px);letter-spacing:-.035em}
table{table-layout:fixed;font-size:14px}th{width:40%}td{white-space:normal;overflow-wrap:anywhere}
.today-tag{display:table;margin:4px 0 0}
.hero.photo{height:auto;min-height:100svh}.hero.photo .hb{padding-top:40px}
}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*:before,*:after{animation:none!important;transition:none!important}.ln>span,.motion-ready:not(.ready) .ln>span{transform:none}.rv,.motion-ready .rv:not(.in){opacity:1;transform:none}.clip,.motion-ready .clip:not(.in){clip-path:none}.clip img{transform:none}.hero-img{transform:none}}
"""

JS = """<script>
(()=>{
const root=document.documentElement,reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
requestAnimationFrame(()=>requestAnimationFrame(()=>root.classList.add('ready')));
try{
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.1,rootMargin:'0px 0px -6% 0px'});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
// photos wipe in when their block arrives (watch the parent: a fully clipped element never counts as visible)
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.querySelectorAll('.clip').forEach(c=>c.classList.add('in'));cio.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.cliphost').forEach(el=>cio.observe(el));
root.classList.add('motion-ready');
}catch(e){root.classList.remove('motion-ready')}
// hero photo eases back on scroll; slim nav bar appears after the hero
const bar=document.getElementById('bar'),hero=document.querySelector('.hero');let tick=false;
const upd=()=>{const h=hero.offsetHeight||innerHeight;if(!reduce)root.style.setProperty('--hp',Math.min(scrollY/h,1).toFixed(3));const show=scrollY>h*.8;
if(!show&&bar.contains(document.activeElement))document.querySelector('.hero .logo').focus();
bar.inert=!show;bar.setAttribute('aria-hidden',String(!show));bar.classList.toggle('show',show);tick=false};
addEventListener('scroll',()=>{if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});upd();
// photo follows the pointer over the big service rows (mouse only)
const fl=document.getElementById('float');
if(fl&&matchMedia('(hover:hover) and (pointer:fine)').matches&&!reduce){const imgs=[...fl.querySelectorAll('img')];
document.querySelectorAll('.row').forEach((m,n)=>{m.addEventListener('pointerenter',()=>{imgs.forEach((im,i)=>im.classList.toggle('on',i===n%imgs.length));fl.classList.add('on')});m.addEventListener('pointerleave',()=>fl.classList.remove('on'))});
addEventListener('pointermove',e=>{fl.style.setProperty('--fx',Math.min(e.clientX+28,innerWidth-330)+'px');fl.style.setProperty('--fy',(e.clientY-190)+'px')},{passive:true})}
// footer wordmark always spans the page exactly
const word=document.querySelector('.word');
const fit=()=>{if(!word)return;word.style.fontSize='100px';const w=word.firstElementChild.offsetWidth;if(w)word.style.fontSize=Math.min(100*(root.clientWidth*.955)/w,root.clientWidth*.3)+'px'};
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
<div class="facts"><div class="rv"><span class="tag lab">{'Today · call to confirm' if s.get('hours_note') else 'Today'}</span>{today}</div><div class="rv" style="--d:1"><span class="tag lab">Where</span><strong>{s['addr'].replace('<br>', ', ')}</strong></div><div class="rv" style="--d:2"><span class="tag lab">Call</span><strong><a href="tel:{t}">{s['phone']}</a></strong></div></div>
<div class="cta rv"><a class="pill solid" href="tel:{t}">Call the shop</a><a class="pill" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a></div>
</div></section>"""


def services(s, first=True):
    label = s.get("svc_label", "What we do")
    items = [(g, n, d) for g, its in s["services"] for n, d in its]
    if s["art"].get("svc") == "cards":
        cards = "".join(f'<div class="cardx rv"><div>{"<p class=grp>" + esc(g) + "</p>" if g else ""}<h3>{esc(n)}</h3></div>{"<p>" + esc(d) + "</p>" if d else ""}</div>' for g, n, d in items)
        extra = " ".join(esc(s[k]) for k in ("svc_text", "svc_note") if s.get(k))
        return f'<section id="services"{" style=padding-top:0" if first else ""}><div class="wrap"><p class="tag lab rv">{label}</p><div class="cardhead"><h2 class="big2 rv">{esc(s.get("svc_title", "What we do."))}</h2>{"<p class=rv>" + extra + "</p>" if extra else ""}</div><div class="cards">{cards}</div></div></section>'
    if s["art"].get("svc") == "rows":
        rows = "".join(f'<div class="row rv"><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for _, n, d in items)
        fl = '<div class="float" id="float" aria-hidden="true">' + "".join(f'<img alt="" src="{p}">' for p in s["photos"]) + "</div>"
        note = f'<p class="hol rv" style="margin-top:18px">{esc(s["svc_note"])}</p>' if s.get("svc_note") else ""
        return f'<section id="services"{" style=padding-top:0" if first else ""}><div class="wrap"><p class="tag lab rv">{label}</p><div class="rows">{rows}</div>{note}</div>{fl}</section>'
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
    dark = " dark" if s["art"].get("svc") in ("rows", "cards") else ""
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
        url = s["ratings"][0][2]
        body = '<div class="qs">' + "".join(f'<a class="q rv" href="{url}" target="_blank" rel="noopener noreferrer"><p>“{esc(q)}”</p><cite>From Google reviews · open the listing ↗</cite></a>' for q in s["quotes"]) + "</div>"
    else:
        body = ""
    return f'<section id="reviews"><div class="wrap"><p class="tag lab rv">Reviews</p><div class="revhead"><div class="nums">{nums}</div>{txt}</div>{body}</div></section>'


def frag(base, text):
    from urllib.parse import quote
    return base + "#:~:text=" + quote(text, safe="")


def visit(s):
    t = tel(s["phone"])
    if s.get("hours"):
        rows = "".join(f'<tr data-day="{(i + 1) % 7}"><th scope="row">{d}</th><td>{s["hours"][i]}</td></tr>' for i, d in enumerate(DAYS))
        hrs = f'<span class="tag lab">{"Listed hours · call to confirm" if s.get("hours_note") else "Hours"}</span><table>{rows}</table><p class="hol"><strong>Holiday hours.</strong> Hours can change on holidays, including Veterans Day, Thanksgiving, Christmas and New Year\'s Day. Call <a href="tel:{t}">{s["phone"]}</a> before you come in.</p>'
    else:
        hrs = f'<span class="tag lab">Hours</span><p class="revtxt" style="margin-top:12px">Call <a href="tel:{t}" style="text-decoration:underline;text-underline-offset:5px">{s["phone"]}</a> for current availability and hours.</p>'
    if s.get("hours_note"):
        hrs += f'<p class="hol"><strong>Confirm regular hours.</strong> {esc(s["hours_note"])} Call <a href="tel:{t}">{s["phone"]}</a> before travelling.</p>'
    find = f'<p class="find">{esc(s["find"])}</p>' if s.get("find") else ""
    from urllib.parse import quote_plus
    mp = f'<iframe class="map" loading="lazy" title="Map of {esc(s["short"])}" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={quote_plus(s["short"] + ", " + s["addr"].replace("<br>", ", "))}&z=15&output=embed"></iframe>' if s.get("hours") else ""
    return f"""<section class="{s['art'].get('visit', 'dark')}" id="visit"><div class="wrap"><p class="tag lab rv">Visit or call</p>
<a class="phone rv" href="tel:{t}">{s['phone']}</a>
<div class="vgrid"><div class="rv"><span class="tag lab">Address</span><address>{s['addr']}</address>{find}
<div class="cta"><a class="pill solid" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a><a class="pill" href="tel:{t}">Call the shop</a></div>{mp}</div>
<div class="rv" style="--d:1">{hrs}</div></div></div></section>"""


def build(folder, s):
    art = s["art"]
    t = tel(s["phone"])
    v = f":root{{--ink:{art['ink']};--bone:{art['bone']};--paper:{art.get('paper', '#ffffff')};--acc:{art['acc']};--star:{art['star']};--on-acc:{art.get('on_acc', '#fff')};--stretch:{art.get('stretch', '108%')};--h1:{art.get('h1', '11vw')};--rowsz:{art.get('rowsz', '8.6vw')};--wordsz:{art.get('wordsz', '15vw')}}}"
    order = art.get("order", 0)
    parts = [[statement(s), services(s), about(s), reviews(s)], [statement(s), about(s), services(s, False), reviews(s)], [statement(s), reviews(s), services(s, False), about(s)]][order]
    sections = "\n".join(parts)
    body = f"""<a class="skip" href="#main">Skip to content</a>
<div class="bar" id="bar" inert aria-hidden="true"><div class="wrap">{nav(s, 'bar')}</div></div>
{hero(s)}
<main id="main">
{sections}
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
<body class="{'serif ' if art.get('serif') else ''}{art.get('cls', '')}">
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
    # Batch added 2026-11-10 (evening): the rest of the built leads, same craft, different direction per site
    "mailos-auto-repair": dict(hero="photo", ink="#12191C", bone="#F2F0E9", acc="#1F5F74", star="#E0B34A", h1="9.4vw", svc="index", mark="Mailo's", word="Mailo's", wordsz="20vw"),
    "bee-z-auto-care": dict(hero="block", ink="#17150E", bone="#FBF6E4", acc="#F0C02E", on_acc="#17150E", star="#17150E", h1="10.4vw", stretch="80%", svc="index", mark="Bee Z Auto Care", word="Bee Z", wordsz="26vw"),
    "quality-auto-complete-auto-repair": dict(hero="poster", ink="#1A1216", bone="#F5F0EC", acc="#7B1F3A", star="#C98A1B", h1="9.6vw", svc="index", mark="Quality Auto", word="Quality Auto", wordsz="15vw"),
    "county-brake-alignment": dict(hero="split", ink="#1B1A18", bone="#F4EEE3", acc="#9A4A12", star="#D99A1E", h1="7.8vw", stretch="78%", svc="index", mark="County Brake", word="County Brake", wordsz="15vw"),
    "jc-bumper-repair": dict(hero="photo", ink="#11151C", bone="#EEF0F3", acc="#1E4A9C", star="#D9C27A", h1="10.4vw", stretch="76%", svc="rows", rowsz="7vw", mark="JC Bumper Repair", word="JC Bumper", wordsz="17vw"),
    "with-pride-auto-air": dict(hero="block", ink="#0A2A40", bone="#EFF6FA", acc="#0B5E8E", star="#F2B632", h1="9vw", svc="index", mark="With Pride Auto Air", word="With Pride", wordsz="16vw"),
    "performance-lube-oil": dict(hero="poster", ink="#0D2730", bone="#F1F6F6", acc="#0E6F8F", star="#E8A200", h1="11.4vw", stretch="80%", svc="rows", rowsz="6.6vw", mark="Performance Lube", word="Performance", wordsz="15vw"),
    "j-s-auto-center-smog": dict(hero="split", serif=True, ink="#1A1D14", bone="#F3F2E6", acc="#5C6B1E", star="#C99A1E", h1="8vw", svc="index", mark="J & S Auto", word="J & S", wordsz="26vw"),
    "jc-auto-electric": dict(hero="block", ink="#16181B", bone="#F5F2EC", acc="#8E1B16", star="#F2B632", h1="10vw", svc="index", mark="J C Auto Electric", word="J C Electric", wordsz="15vw"),
    "diesel-injection-service": dict(hero="photo", ink="#101410", bone="#EFF1EA", acc="#1B6B38", star="#D2A546", h1="6.6vw", stretch="80%", svc="rows", rowsz="6.4vw", mark="Diesel Injection Service", word="Diesel", wordsz="24vw"),
    "toy-shop-transmissions": dict(hero="poster", serif=True, ink="#1D1A17", bone="#F4F0E8", acc="#1A6B6A", star="#C9952B", h1="11vw", svc="index", mark="Toy Shop Transmissions", word="Toy Shop", wordsz="18vw"),
    "hocks-japanese-car-specialists": dict(hero="split", ink="#15171F", bone="#F1F1F4", acc="#34407A", star="#C8962A", h1="7.6vw", svc="index", mark="Hock's", word="Hock's", wordsz="22vw"),
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
    h1=("Weeknight flat at 7?", "We're open until 8."), lede="New and used tires, flat repair and mount-and-balance at the blue shop on California Street. Open until 8 on weeknights, and open Sundays.",
    phone="(909) 391-4636", addr="301 W California St<br>Ontario, CA 91762", maps="https://www.google.com/maps/search/?api=1&query=A+C+Tires+301+W+California+St+Ontario+CA+91762", find="Look for the blue building.",
    hours=["8:00 AM – 8:00 PM"] * 5 + ["8:00 AM – 7:00 PM", "8:00 AM – 6:00 PM"],
    ratings=[("4.4", "Google · 324 reviews", "https://www.google.com/maps/search/?api=1&query=A+C+Tires+301+W+California+St+Ontario+CA+91762")],
    services=[("", [("New tires", "Fresh rubber in the sizes people around here actually drive."), ("Used tires", "Good used tires for when the budget says “not today” to a full new set."), ("Flat repair", "Nail in the tread? In and out fast, weekends included."), ("Mount & balance", "Bought tires elsewhere? We'll mount and balance them."), ("Wheels", "Ask what's in stock for your car.")])],
    svc_title="Tires. That's the shop.", svc_text="No waiting-room upsell. Pull in, tell us what you need, and get back on the road.",
    photos=(U("1792792944402-5e94ce198dce", 2000, 1300), U("1578844251758-2f71da64c96f", 1600, 700)), alt=("Gloved hands mounting a tire in a workshop", "Stacks of tires in a tire shop"),
    track=V.track(V.AC_REVIEWS[:4]), extra_js=V.CAROUSEL_JS,
)

# Real reviews, each linked to the review itself (found and checked 2026-11-10).
# Yelp links use the review's own id (hrid), read from the shop's MapQuest listing, which shows its Yelp reviews.
# King Tire, Don Cortez and Alejandros have no individually linkable reviews we could confirm; they link to the listing.
def be(slug, words):
    return frag("https://reviews.birdeye.com/" + slug, words)


Y, G, yelp = "Yelp review", "Google review", V.yelp
REAL = {
    "lockworx": [("Daniel H.", Y, "They were quick, kind, and the prices are very good!", yelp("lockworx-fontana-4", "iEA7oRzGEo_1-Sn6flNhPw"), "Yelp"),
                 ("Julie Y.", Y, "…Lockworx came to the rescue immediately.", yelp("lockworx-fontana-4", "1kRNcSs6UMOjYFl_renmsw"), "Yelp"),
                 ("Arthur P.", Y, "Shane has great customer service", yelp("lockworx-fontana-4", "9gBlS8JOM_5wuMf-ZFFV3Q"), "Yelp"),
                 ("Arie G.", Y, "…honest very transparent…", yelp("lockworx-fontana-4", "pYm_8XWg9qa7cW_TN1GloA"), "Yelp"),
                 ("Char", Y, "Very professional very helpful…", yelp("lockworx-fontana-4", "ytZ8FPdbIiZpYFawKrRJHw"), "Yelp")],
    "el-rey": [("James J.", Y, "…finally stopped in--wow, I've been missing out!", yelp("el-rey-chino", "w7GAgAniG0mgx7GjYvk5hQ"), "Yelp"),
               ("James M.", Y, "…great quality food, drinks and self serve salsa.", yelp("el-rey-chino", "RxdtEwT1aOGotPQ5PJFcUQ"), "Yelp"),
               ("Suzanne C.", Y, "Wow, the size of the portion is huge…", yelp("el-rey-chino", "GlO7-fQI9i_0pM5ao6IQrg"), "Yelp")],
    "sinaloa-tires": [("Alex C.", Y, "Danny is awesome and knowledgeable.", yelp("sinaloa-tires-pomona-2", "VZaex1arX1qtCqZuDv81qw"), "Yelp"),
                      ("Kim N.", Y, "these are the kindest, most genuine and honest people…", yelp("sinaloa-tires-pomona-2", "romopcdBiezp4d46-hAK8A"), "Yelp"),
                      ("Emma G.", Y, "…el buen servicio que me dieron…", yelp("sinaloa-tires-pomona-2", "MItIqFT4R749PlZELMRzXg"), "Yelp")],
    "43s-mufflers-brakes": [("Mark M.", Y, "…extremely helpful, honest, and fair with pricing.", yelp("43s-muffler-and-brakes-pomona", "HdfToYnn_LewqjPDiHOClg"), "Yelp"),
                            ("Hector G.", Y, "Fast and communicative!", yelp("43s-muffler-and-brakes-pomona", "MQTU6LEpUlKLvJ3NFf7z_w"), "Yelp"),
                            ("Melanie G.", Y, "In and out, great job. Highly recommend…", yelp("43s-muffler-and-brakes-pomona", "1Vnyynu9CuCggp5NzchNmQ"), "Yelp"),
                            ("The M.", Y, "La dueña del local Jenni, siempre ayudandome…", yelp("43s-muffler-and-brakes-pomona", "ZL5XxdbtOOUqJycyWqPmoQ"), "Yelp"),
                            ("Mike", Y, "Brakes done within reasonable time. Great prices…", yelp("43s-muffler-and-brakes-pomona", "SNWK7vdjd5Al1nAbY0O1Gw"), "Yelp")],
    "tepa-tire": [("Troy D.", Y, "Jaime was excellent!", yelp("tepa-tire-and-auto-care-montclair", "bKngFnYLn6k4xIkYCroJsg"), "Yelp"),
                  ("La Reina P.", Y, "They offer many services from tires used and new…", yelp("tepa-tire-and-auto-care-montclair", "D1tXekO3BUZucwrme3Nd5g"), "Yelp")],
}
for k, r in REAL.items():
    SITES[k]["track"] = V.track(r)
    SITES[k]["extra_js"] = V.CAROUSEL_JS
    SITES[k].pop("quotes", None)

# Researched 2026-11-10 on Google Maps (address, phone, hours, rating) and the shop's MapQuest/Yelp listing.
# Basic Auto Repair moved: older directories say 810 E Holt Blvd; Google and a customer review say 803.
GM = "https://www.google.com/maps/search/?api=1&query="
SITES["basic-auto-repair"] = dict(
    art=dict(hero="block", ink="#141B2B", bone="#F4F1EA", acc="#1F3F8F", star="#F2B632", h1="10.4vw", stretch="80%", svc="index", mark="Basic Auto Repair", word="Basic Auto", wordsz="17vw"),
    short="Basic Auto Repair", kicker="Auto repair · E Holt Blvd, Ontario", footer="Basic Auto Repair · Ontario, CA",
    h1=("Honest work.", "That's the basics."), lede="Full-service auto repair on East Holt Boulevard, serving Ontario since 1995. Smog inspection, brakes, tune-ups and routine maintenance.",
    phone="(909) 984-8011", addr="803 E Holt Blvd<br>Ontario, CA 91764", maps=GM + "Basic+Auto+Repair+803+E+Holt+Blvd+Ontario+CA", find="New location. Older listings still show 810 E Holt Blvd; the shop is at 803.",
    hours=["8:00 AM – 5:00 PM"] * 5 + ["8:00 AM – 1:00 PM", "Closed"],
    ratings=[("4.8", "Google · 115 reviews", GM + "Basic+Auto+Repair+803+E+Holt+Blvd+Ontario+CA")],
    services=[("", [("Smog inspection", "Emission testing and smog inspection."), ("Brake repair", ""), ("Tune-ups", ""), ("Routine maintenance", "Including belt replacement."), ("Repairs", "Reviewers mention radiator repair and starter replacement. Call about yours.")])],
    svc_title="Full service, plainly done.", svc_text="Tell us the car and what it's doing. We'll tell you what it needs.",
    rev_text="“Honest mechanic” is the phrase Google reviewers use most.",
    photos=(PX(8986100, 1800), PX(6870299)), alt=("Mechanic working under a car on a lift", "Close-up of a brake rotor being inspected"),
    track=V.track([("Angie G.", "Yelp review", "I highly recommend the shop if you value 100% honesty…", V.yelp("basic-auto-repair-ontario", "olw7l5e7vWCG7xPBZz5eeA"), "Yelp"),
                   ("Raena S.", "Yelp review", "…knowledgeable, honest and cordial.", V.yelp("basic-auto-repair-ontario", "kuxe2uu4hux-L5NwxBusJQ"), "Yelp"),
                   ("Stephanie W.", "Yelp review", "I am so glad I listened to the majority of the people who recommended this shop!", V.yelp("basic-auto-repair-ontario", "b49PtK1gbPYmwJgH9gf9zg"), "Yelp")]),
    extra_js=V.CAROUSEL_JS,
)
SITES["a-tech-automotive"] = dict(
    art=dict(hero="split", ink="#161616", bone="#F2F2EE", acc="#B3261E", star="#D99A1E", h1="8.4vw", svc="rows", rowsz="7vw", mark="A Tech", word="A Tech", wordsz="24vw"),
    short="A Tech Automotive", kicker="Auto repair · Central Ave, Chino", footer="A Tech Automotive · Chino, CA",
    h1=("Good work.", "Fair prices."), lede="Auto repair and maintenance on Central Avenue in Chino. Several Google reviewers say they have been coming back for ten years or more.",
    phone="(909) 590-0123", addr="12365 Central Ave, Unit A<br>Chino, CA 91710", maps=GM + "A+Tech+Automotive+12365+Central+Ave+Chino+CA",
    hours=["8:00 AM – 5:00 PM"] * 5 + ["8:00 AM – 3:00 PM", "Closed"],
    ratings=[("4.5", "Google · 104 reviews", GM + "A+Tech+Automotive+12365+Central+Ave+Chino+CA")],
    services=[("", [("Oil changes", "One of the most-mentioned jobs in the shop's Google reviews."), ("Maintenance", "Regular service to keep a high-mileage car on the road."), ("Repairs", "From small fixes to major repairs. Call and describe what the car is doing.")])],
    quotes=["They do good work and charge fair prices.", "Good fast service,easy to talk to as well.pleasent service."],
    rev_text="Reviewers most often mention the professional team, kind staff, repair time and oil changes.",
    photos=(PX(31097241, 1600), PX(8985660)), alt=("Mechanic working on a wheel in a workshop", "Mechanic rolling a tire beside a car on a lift"),
)

# Batch 7, researched 2026-11-10. Address, hours, description and Yelp reviews from each shop's MapQuest listing;
# Google rating and phone from the lead sheet. Ceres Collision: MapQuest lists (909) 349-2880, Google lists (909) 251-4447 (used here).
SITES["johns-auto-repair"] = dict(
    art=dict(hero="photo", ink="#10141C", bone="#F2F1EC", acc="#1D5FA8", star="#E8B32A", h1="10.6vw", stretch="80%", svc="index", mark="John's Auto Repair", word="John's", wordsz="24vw"),
    short="John's Auto Repair", kicker="BMW, Mercedes-Benz and Mini · Ceres Ave, Fontana", footer="John's Auto Repair · Fontana, CA",
    h1=("European cars.", "Straight answers."), lede="A family-owned shop on Ceres Avenue that focuses on BMW, Mercedes-Benz and Mini Cooper. Clear explanations and accurate quotes before the work starts.",
    phone="(909) 822-5606", addr="16566 Ceres Ave, Unit 1 and 2<br>Fontana, CA 92335", maps=GM + "John%27s+Auto+Repair+16566+Ceres+Ave+Fontana+CA",
    hours=["9:00 AM – 5:00 PM"] * 6 + ["Closed"],
    ratings=[("4.6", "Google · 93 reviews", GM + "John%27s+Auto+Repair+16566+Ceres+Ave+Fontana+CA")],
    services=[("What we work on", [("BMW", ""), ("Mercedes-Benz", ""), ("Mini Cooper", "")]),
              ("What we do", [("Check engine light repairs", "Diagnosis first, then a quote."), ("Oil changes", ""), ("Engine rebuilding", ""), ("Inspections", "A thorough look over the car, explained in plain words.")])],
    svc_title="One kind of car, done well.", svc_text="Tell us the model and what it's doing. We'll tell you what it needs.",
    photos=(PX(8986100, 1800), PX(6870299)), alt=("Mechanic working under a car on a lift", "Close-up of a brake rotor being inspected"),
    track=V.track([("Jay S.", "Yelp review", "Trustworthy mechanic with no BS.", V.yelp("johns-auto-repair-specialist-fontana-5", "Y1QvrdlHCuVQqBMlR1wejw"), "Yelp"),
                   ("Darren S.", "Yelp review", "John and team are a stellar crew.", V.yelp("johns-auto-repair-specialist-fontana-5", "YeJaM1s2XoEmI2hyaqHOxQ"), "Yelp"),
                   ("chuyito r.", "Yelp review", "Muy confiable y honesto!", V.yelp("johns-auto-repair-specialist-fontana-5", "8kFiOoIsIcyadyMAbnqMrQ"), "Yelp"),
                   ("Michael V.", "Yelp review", "Very please with the services. Upfront and honest.", V.yelp("johns-auto-repair-specialist-fontana-5", "aue4kPyLiTNvgkwEYZ1GEA"), "Yelp"),
                   ("Charley B.", "Yelp review", "This man does an excellent job at fixing your car…", V.yelp("johns-auto-repair-specialist-fontana-5", "Mz_GC882eff4T1zbfrhK_Q"), "Yelp")]),
    extra_js=V.CAROUSEL_JS,
)
SITES["ceres-collision"] = dict(
    art=dict(hero="split", ink="#1A1614", bone="#F3EFE8", acc="#B4321F", star="#E0A52E", h1="8.8vw", svc="rows", rowsz="7vw", mark="Ceres Collision", word="Ceres", wordsz="26vw", about_label="The body shop"),
    short="Ceres Collision", kicker="Auto body and collision repair · Fontana", footer="Ceres Collision · Fontana, CA",
    h1=("After the accident,", "we work with you."), lede="Auto body and collision repair on Ceres Avenue. The shop says it has served the community for 20 years and can answer questions about your insurance claim.",
    phone="(909) 251-4447", addr="16616 Ceres Ave, #1<br>Fontana, CA 92335", maps=GM + "Ceres+Collision+16616+Ceres+Ave+Fontana+CA",
    hours=["8:00 AM – 5:00 PM"] * 5 + ["Closed", "Closed"],
    ratings=[("4.8", "Google · 50 reviews", GM + "Ceres+Collision+16616+Ceres+Ave+Fontana+CA")],
    services=[("", [("Collision repair", "Bring the car in or call first. We'll look at the damage with you."), ("Insurance claims", "Questions about your insurance or your claim? Ask us. We work directly with you."), ("Auto body work", "Customer service and attention to detail are what the shop says it is proud of.")])],
    svc_label="What we do",
    about=dict(title="From your first call until you leave.", text="Going to a body shop can be stressful. Ceres Collision says its aim is a good experience from the first phone call to the day you pick the car up."),
    rev_text="Rated 4.8 on Google. Open the listing to read what customers wrote.",
    photos=(PX(8470881, 1600), PX(6870314)), alt=("Painter working on a car in a body shop", "Spray gun painting a car part"),
)

# Prime Truck and Trailer Repair (Google Maps listing read in a browser 2026-11-10; no matching Yelp page found)
SITES["prime-truck-trailer-repair"] = dict(
    art=dict(hero="photo", ink="#14171A", bone="#F2EFE9", acc="#A8321A", star="#E6B23C", h1="9vw", stretch="80%", svc="rows", rowsz="6.4vw", mark="Prime Truck and Trailer Repair", word="Prime", wordsz="26vw"),
    short="Prime Truck and Trailer Repair", kicker="Truck and trailer repair · Cherry Ave, Fontana", footer="Prime Truck and Trailer Repair · Fontana, CA",
    h1=("Truck down?", "Bring it to Cherry Ave."), lede="Truck and trailer repair in Fontana, from alignments and suspension to engine rebuilds. Owner-operators welcome.",
    phone="(909) 644-3029", addr="9978 Cherry Ave<br>Fontana, CA 92335", maps=GM + "Prime+Truck+and+Trailer+Repair+9978+Cherry+Ave+Fontana+CA",
    hours=["8:30 AM – 6:00 PM"] * 5 + ["8:30 AM – 3:30 PM", "Closed"],
    ratings=[("4.4", "Google · 102 reviews", GM + "Prime+Truck+and+Trailer+Repair+9978+Cherry+Ave+Fontana+CA")],
    services=[("", [("Engine work", "Diagnostics through full engine rebuilds."), ("Suspension", ""), ("Alignment", ""), ("Trailer repair", ""), ("Bring your own parts", "Some reviewers had customer-supplied parts fitted. Ask when you call.")])],
    svc_title="Truck and trailer repair.", svc_text="Call with the truck, the problem and where it is parked.",
    rev_text="Google reviewers mention quality of work, honest mechanics, alignments and trailer repair.",
    photos=(PX(6720519, 1800), PX(7019376)), alt=("Mechanic working on the front of a truck with the hood open", "Red semi truck parked in a repair shop"),
)
# Batch 8, researched 2026-11-10. Address, hours, description and Yelp reviews (linked by review id) come from each
# shop's MapQuest listing, read in a browser. Phone matches the lead sheet; Google rating and count are from the lead sheet.
def _y(biz, rows):
    return V.track([(n, "Yelp review", q, V.yelp(biz, h), "Yelp") for n, q, h in rows])


SITES["freddies-auto-repair"] = dict(
    art=dict(hero="poster", ink="#1B1F1A", bone="#F1F0E8", acc="#2D6A4F", star="#E3B23C", h1="9.4vw", svc="index", mark="Freddie's", word="Freddie's", wordsz="20vw"),
    short="Freddie's Auto Repair", kicker="Auto repair · E Mission Blvd, Pomona", footer="Freddie's Auto Repair · Pomona, CA",
    h1=("Honest mechanics", "still exist."), lede="Auto repair and oil changes on East Mission Boulevard. Customers on Yelp keep using the same two words: honest and knowledgeable.",
    phone="(909) 622-7216", addr="915 E Mission Blvd<br>Pomona, CA 91766", maps=GM + "Freddie%27s+Auto+Repair+915+E+Mission+Blvd+Pomona+CA",
    hours=["8:30 AM – 5:00 PM"] * 5 + ["Closed", "Closed"],
    ratings=[("4.6", "Google · 71 reviews", GM + "Freddie%27s+Auto+Repair+915+E+Mission+Blvd+Pomona+CA")],
    services=[("", [("Auto repair", "Tell Freddie what the car is doing and he'll tell you what it needs."), ("Oil changes", ""), ("Diagnosis", "Call first with the year, make and model.")])],
    svc_title="Bring it to Freddie.", svc_text="A small shop where you talk to the person working on your car.",
    photos=(PX(8985660, 1800), PX(6870299)), alt=("Mechanic rolling a tire beside a car on a lift", "Close-up of a brake rotor being inspected"),
    track=_y("freddies-auto-repair-pomona", [("Mary K.", "There really is still honest and reliable mechanics.", "6Leu7W5E5axejUxgiyWcYw"), ("Victor G.", "Honest and great mechanical knowledge…", "vN9mnCOWe3P8VmxHaXNLoQ"), ("Yolanda M.", "Freddy is so knowledgeable, friendly & does an amazing job!", "sOjG6YB0lsZvOr5TEwB_zA"), ("Party A.", "They're honest and hard working.", "BFLy1HSnixKdu3FILeRFlQ"), ("Erin B.", "I've been coming here for years…", "uygv3qF2WJskuclBIYdzCQ")]),
    extra_js=V.CAROUSEL_JS,
)
SITES["bates-auto-service"] = dict(
    art=dict(hero="split", serif=True, ink="#1E1A2B", bone="#F4F1EC", acc="#5B3F9B", star="#E0A62E", h1="9vw", svc="rows", rowsz="6.6vw", mark="Bates Auto", word="Bates", wordsz="26vw"),
    short="Bates Auto Service", kicker="Auto repair · W 9th St, Upland", footer="Bates Auto Service · Upland, CA",
    h1=("Worth the", "drive."), lede="Auto repair on West 9th Street in Upland. Yelp reviewers mention quick turnaround, competitive pricing and Henry, who they keep coming back to.",
    phone="(909) 949-7984", addr="958 W 9th St<br>Upland, CA 91786", maps=GM + "Bates+Auto+Service+958+W+9th+St+Upland+CA",
    hours=["8:00 AM – 5:00 PM"] * 5 + ["Closed", "Closed"],
    ratings=[("4.7", "Google · 69 reviews", GM + "Bates+Auto+Service+958+W+9th+St+Upland+CA")],
    services=[("", [("Diagnosis", "A strange noise, a warning light, overheating. Start by describing it."), ("Repairs", "Call with the year, make and model for a quote."), ("Maintenance", "Ask what your car is due for.")])],
    svc_label="What we do",
    photos=(PX(8986100, 1600), PX(6870311)), alt=("Mechanic working under a car on a lift", "Mechanic inspecting a tire in a workshop"),
    track=_y("bates-auto-service-upland-3", [("Theresa H.", "…it's totally worth the drive!", "vbOUwIvyOV4hUTKg6-ZOiQ"), ("Jeff B.", "Great customer service, competitive pricing, and a quick turnaround!", "SfDfG54_SNsFaPVveXYlbQ"), ("B N.", "Quick quality service…", "EC6sEcUxZq7-czo7lq2JVA"), ("Rita C.", "I'm a returning customer of Henry.", "jD2VfHy5NzTjMNmO8qMFEQ")]),
    extra_js=V.CAROUSEL_JS,
)
SITES["express-transmissions"] = dict(
    art=dict(hero="block", ink="#111417", bone="#F2F2F0", acc="#0F5C7A", star="#F2B84B", h1="10.6vw", stretch="76%", svc="index", mark="Express Transmissions", word="Express", wordsz="22vw"),
    short="Express Transmissions", kicker="Transmission shop · E Mission Blvd, Pomona", footer="Express Transmissions · Pomona, CA",
    h1=("Slipping gears?", "Start here."), lede="A family-owned transmission shop on East Mission Boulevard. Transmission repair, differentials, transfer cases and diagnostics, plus fleet service.",
    phone="(909) 469-2282", addr="309 E Mission Blvd<br>Pomona, CA 91766", maps=GM + "Express+Transmissions+309+E+Mission+Blvd+Pomona+CA",
    hours=["8:00 AM – 6:00 PM"] * 5 + ["8:00 AM – 2:00 PM", "Closed"],
    ratings=[("4.7", "Google · 48 reviews", GM + "Express+Transmissions+309+E+Mission+Blvd+Pomona+CA")],
    services=[("Drivetrain", [("Transmission repair", "Including rebuilds. Ask for a price before any work starts."), ("Differential service", ""), ("Transfer case repair", ""), ("Diagnostics", "A check-up to find out what the transmission actually needs.")]),
              ("Also", [("Fleet service", "Maintenance for commercial vehicles."), ("Makes", "The listing names Chevrolet, Dodge, Ford, Honda and Toyota.")])],
    svc_title="Transmission and drivetrain service.", svc_text="Tell us the vehicle and what it's doing when it shifts.",
    about=dict(title="Ask about the warranty.", text="The shop's listing mentions a three-year, 100,000-mile warranty on transmission work. Ask for the terms when you call."),
    photos=(PX(31097241, 1800), PX(8986100)), alt=("Mechanic working on a wheel in a workshop", "Mechanic working under a car on a lift"),
    track=_y("express-transmission-pomona", [("Aren Y.", "I was referred to Juan by my trusted mechanic and he was responsive…", "-jhN4lnS7AJ9HSVmXJT7WA"), ("Geno F.", "Jaun is a great guy to work with…", "_xJkz94E4x_7Dj_oVHzH4w"), ("Daniel S.", "…they did a great job…", "xi4JSvWLrbribTa5AIwF5A")]),
    extra_js=V.CAROUSEL_JS,
)
SITES["menas-brake-suspension"] = dict(
    art=dict(hero="photo", ink="#1A1210", bone="#F5F0E6", acc="#B5361C", star="#F0B429", h1="10.4vw", svc="index", mark="Menas", word="Menas", wordsz="26vw"),
    short="Menas Brake & Suspension", kicker="Brakes, suspension and repair · E Holt Blvd, Ontario", footer="Menas Brake & Suspension · Ontario, CA",
    h1=("Brakes first.", "Then everything else."), lede="Brake service and suspension on East Holt Boulevard, plus diagnostics, tune-ups, oil changes and engine and transmission work.",
    phone="(909) 933-9131", addr="646 E Holt Blvd<br>Ontario, CA 91761", maps=GM + "Menas+Brake+%26+Suspension+646+E+Holt+Blvd+Ontario+CA",
    hours=["8:00 AM – 5:30 PM"] * 5 + ["8:00 AM – 1:30 PM", "Closed"],
    ratings=[("4.6", "Google · 47 reviews", GM + "Menas+Brake+%26+Suspension+646+E+Holt+Blvd+Ontario+CA")],
    services=[("Under the car", [("Brake service", ""), ("Suspension", ""), ("Axle replacement", "")]),
              ("Under the hood", [("Diagnostics", ""), ("Tune-ups", ""), ("Oil changes", ""), ("Engine and transmission overhaul", ""), ("Transmission service", ""), ("Electrical", ""), ("Fuel pump replacement", "")])],
    svc_title="What the shop lists.", svc_text="Call with the car and the symptom. Ask for a price before work starts.",
    rev_text="Rated 4.6 on Google. Open the listing to read what customers wrote.",
    photos=(PX(6870299, 1800), PX(8985660)), alt=("Close-up of a brake rotor being inspected", "Mechanic rolling a tire beside a car on a lift"),
)
SITES["the-auto-clinic"] = dict(
    art=dict(hero="split", ink="#0E2A2A", bone="#F0F3EF", acc="#0E7C6B", star="#E8A93A", h1="8.6vw", stretch="84%", svc="rows", rowsz="6.6vw", mark="The Auto Clinic", word="Auto Clinic", wordsz="17vw"),
    short="The Auto Clinic", kicker="Auto repair · Schaefer Ave, Chino", footer="The Auto Clinic · Chino, CA",
    h1=("A second opinion", "you can trust."), lede="Auto repair and oil changes on Schaefer Avenue in Chino. Yelp reviewers describe Marcos as knowledgeable, honest and willing to explain.",
    phone="(909) 628-6796", addr="5530 Schaefer Ave, Ste A<br>Chino, CA 91710", maps=GM + "The+Auto+Clinic+5530+Schaefer+Ave+Chino+CA",
    hours=["8:00 AM – 4:00 PM"] * 5 + ["Closed", "Closed"],
    ratings=[("4.9", "Google · 55 reviews", GM + "The+Auto+Clinic+5530+Schaefer+Ave+Chino+CA")],
    services=[("", [("Oil changes", "The job reviewers mention most."), ("Repairs", "Call with the year, make and model."), ("Check-ups", "Not a car person? Ask Marcos to walk you through it.")])],
    svc_label="What we do",
    photos=(PX(6870311, 1600), PX(8986100)), alt=("Mechanic inspecting a tire in a workshop", "Mechanic working under a car on a lift"),
    track=_y("the-auto-clinic-chino", [("Gracie D.", "Marcos is the best! He's incredibly knowledgeable and honest…", "usS-tUUGQ4hQtRdoappPhw"), ("Regina B.", "I trust him !!", "nQc5-yFg-Gw_y6kuPzV9Ig"), ("Kayli M.", "…amazed at how nice and informative Marcos was.", "h02mgS4Ur3-kysBN2qPDxQ"), ("Jair", "The guy is really honest…", "Rs5mzlIv4_IcYkAzeoZabQ"), ("Drew N.", "For service that goes above and beyond…", "EeoQwWCTuHkJ2iT8jCMU2g")]),
    extra_js=V.CAROUSEL_JS,
)


# Batch 9, researched 2026-11-10 the same way as batch 8 (MapQuest listing in a browser; phone matches the lead sheet;
# Google rating and count from the lead sheet). mk() keeps these entries short.
_ALT = {8986100: "Mechanic working under a car on a lift", 6870299: "Close-up of a brake rotor being inspected", 8985660: "Mechanic rolling a tire beside a car on a lift",
        31097241: "Mechanic working on a wheel in a workshop", 6870311: "Mechanic inspecting a tire in a workshop"}


def mk(folder, art, short, kicker, h1, lede, phone, addr, q, hours, rating, services, ph, yelp_biz=None, revs=(), **extra):
    link = GM + q
    s = dict(art=art, short=short, kicker=kicker, footer=f"{short} · {addr.split('<br>')[1].split(',')[0]}, CA", h1=h1, lede=lede, phone=phone, addr=addr, maps=link,
             hours=hours, ratings=[(rating[0], f"Google · {rating[1]} reviews", link)], services=services,
             photos=(PX(ph[0], 1800), PX(ph[1])), alt=(_ALT[ph[0]], _ALT[ph[1]]), **extra)
    if revs:
        s["track"], s["extra_js"] = _y(yelp_biz, revs), V.CAROUSEL_JS
    else:
        s.setdefault("rev_text", f"Rated {rating[0]} on Google. Open the listing to read what customers wrote.")
    SITES[folder] = s


def wkh(mf, sat="Closed", sun="Closed"):
    return [mf] * 5 + [sat, sun]


mk("auto-technik-carcare", dict(hero="photo", ink="#101820", bone="#F1F3F2", acc="#0B6E99", star="#F0B93A", h1="10vw", stretch="84%", svc="index", mark="Auto Technik", word="Technik", wordsz="22vw"),
   "Auto Technik Carcare", "Auto repair · Las Flores Dr, Chino", ("The small shop", "that explains it."), "An independent auto repair shop on Las Flores Drive. Yelp reviewers name the owners, Sham and Jay, and describe careful diagnosis and honest work.",
   "(909) 393-2679", "5260 Las Flores Dr, Ste A & B<br>Chino, CA 91710", "Auto+Technik+Carcare+5260+Las+Flores+Dr+Chino+CA", wkh("9:30 AM – 6:00 PM"), ("4.8", 83),
   [("", [("Diagnosis", "Rough idle, warning lights, a noise you can't place. Start by describing it."), ("Repairs", "Reviewers mention work a dealer had quoted first."), ("Maintenance", "Call with the year, make and model.")])],
   (8986100, 6870311), "auto-technik-carcare-chino-2", [("Kevin Q.", "WOW, I am truly impressed with the level of care and professionalism…", "dFdgJawgbFzGAWwt7Nz0dg"), ("Ernie B.", "Both owners Sham and Jay are honest hard working…", "p9WMFxunPoWRGrGzyHskbA"), ("Javier J.", "Jay diagnosed the issue…", "R09sCneqUdOiGm-yi05tmw")],
   svc_title="Tell us what it's doing.")
mk("diamond-auto-center", dict(hero="block", ink="#16131F", bone="#F4F2F7", acc="#4A2FA3", star="#F2C14E", h1="10.6vw", stretch="78%", svc="index", mark="Diamond Auto", word="Diamond", wordsz="21vw"),
   "Diamond Auto Center", "Auto repair · W California St, Ontario", ("Need a repair?", "Ask for Rick."), "Oil changes, brakes, transmission repair and engine diagnostics on West California Street. Call to confirm availability, especially on Sundays.",
   "(909) 218-7600", "105 W California St<br>Ontario, CA 91762", "Diamond+Auto+Center+105+W+California+St+Ontario+CA", wkh("8:00 AM – 5:00 PM", "8:00 AM – 4:00 PM", "9:00 AM – 2:00 PM"), ("4.8", 78),
   [("Everyday", [("Oil changes", ""), ("Brake repairs", ""), ("Tire and wheel maintenance", ""), ("Air conditioning service", "")]), ("Bigger jobs", [("Engine diagnostics", ""), ("Transmission repairs", ""), ("Suspension and steering", "")])],
   (31097241, 6870299), "diamond-auto-center-ontario-5", [("Jasmin C.", "I had such a wonderful experience here!", "dEJqAIVcVqnIaYH-R9HVOQ"), ("Judy V.", "Rick is THE GOAT. Honestly a life saver.", "Y-4Q8jhPQDMO5i68aZBO-Q"), ("Robert17515", "I took my Audi A5 and Rick took care of me.", "lzQo72dgWkOcNuqzoaRtoQ")],
   svc_title="Small jobs. Big jobs.")
mk("claremont-auto-care", dict(hero="poster", serif=True, ink="#22201C", bone="#F5F1E8", acc="#8A5A1F", star="#D9A441", h1="9vw", svc="rows", rowsz="6.4vw", mark="Claremont Auto Care", word="Claremont", wordsz="17vw"),
   "Claremont Auto Care", "Auto repair and smog · Lynoak Dr", ("Twenty years", "of the same customers."), "Oil changes, smog tests and general repairs on Lynoak Drive, with mechanics who explain the work before they do it.",
   "(909) 621-3872", "3624 Lynoak Dr<br>Pomona, CA 91767", "Claremont+Auto+Care+3624+Lynoak+Dr", wkh("8:00 AM – 5:00 PM", "8:00 AM – 5:00 PM"), ("4.5", 75),
   [("", [("Oil changes", ""), ("Smog tests", ""), ("General repairs", "Clear explanations of what the car needs and why.")])],
   (8985660, 8986100), "claremont-auto-care-pomona", [("Willie H.", "We have been going to Claremont Auto Care for over 20 years…", "FVsNdWBN7ftKt1S9RcUB3Q"), ("Jared A.", "Great service, fair pricing, and honesty…", "8XTQdIjaFU7ei31DLFf6nQ"), ("Nancy A.", "Prices were affordable and they got the work done fast.", "isTfBIf9AnkidZ4qd4k8UA")])
mk("l-r-auto-repair", dict(hero="split", ink="#1C1C1C", bone="#F3F1EC", acc="#C2410C", star="#EAB308", h1="8.8vw", stretch="80%", svc="index", mark="L & R Auto Repair", word="L & R", wordsz="30vw"),
   "L & R Auto Repair", "Auto repair · W Holt Blvd, Ontario", ("Engine light on?", "Bring it in."), "Brake repair, tune-ups, axles, shocks, struts and timing belts on West Holt Boulevard. Open Saturdays.",
   "(909) 972-8883", "504 W Holt Blvd<br>Ontario, CA 91762", "L+%26+R+Auto+Repair+504+W+Holt+Blvd+Ontario+CA", wkh("8:00 AM – 6:00 PM", "8:00 AM – 4:00 PM"), ("4.4", 72),
   [("", [("Brake repair", ""), ("Tune-ups", ""), ("Axles", ""), ("Shocks and struts", ""), ("Timing belts", ""), ("Check engine light", "Bring the vehicle in when the light comes on.")])],
   (6870299, 31097241), "l-and-r-auto-repair-ontario", [("David A.", "Honest and reasonable mechanics", "hiVakwzTqMQF4pmuNXuz_Q"), ("Fernando V.", "I had a fantastic experience.", "jl6y7Wh7DdrHdjDOlSu7YQ"), ("Julianna B.", "…honest prices & outstanding work.", "PP4xjXja5xYsxm8iZqUc6g")],
   svc_title="The usual suspects.")
mk("baja-auto-center", dict(hero="photo", ink="#0F1F17", bone="#F2F4EE", acc="#1F7A3F", star="#F4C430", h1="10.2vw", svc="rows", rowsz="6.4vw", mark="Baja Auto Center", word="Baja", wordsz="30vw"),
   "Baja Auto Center Smog & Lamp", "Smog check and repair · E Holt Blvd, Ontario", ("Smog check due?", "See Tony."), "California smog checks and vehicle safety inspections on East Holt Boulevard, plus oil changes and diagnostics.",
   "(909) 986-7172", "817 E Holt Blvd, Ste B<br>Ontario, CA 91761", "Baja+Auto+Center+Smog+817+E+Holt+Blvd+Ontario+CA", wkh("8:00 AM – 5:00 PM", "8:00 AM – 1:00 PM"), ("4.5", 70),
   [("", [("Smog checks", "California state smog checks."), ("Safety inspections", "Vehicle safety inspections."), ("Oil changes", ""), ("Diagnostics", "")])],
   (6870311, 8985660), "baja-auto-center-smog-and-lamp-ontario", [("Jason H.", "Honest mechanic who is knowledgeable, friendly, and fair.", "-uvWaOBH4lYUHhm2Bz1DPw"), ("Andrew P.", "Awesome service. Tony is incredibly chill and a friendly guy.", "GzMPEdR01WiDONxJBW3Jlw"), ("Jonathan R.", "Great shop. Tony helped me with a vehicle safety inspection.", "JDPEmTX6ot4OEUuqSUtVpA"), ("Jose G.", "Look no further for THE BEST mechanic in the Inland Empire!", "PkioI28UBx-3lmnNDUeOnQ")])
mk("ie-automotive", dict(hero="block", ink="#141414", bone="#F4F0E6", acc="#9A1B1B", star="#E9B43A", h1="11vw", svc="rows", rowsz="6.4vw", mark="I.E Automotive", word="I.E Auto", wordsz="21vw"),
   "I.E Automotive", "Auto repair · S Bon View Ave, Ontario", ("Twenty years", "with Ricky."), "Auto repair on South Bon View Avenue. One Yelp reviewer says they have been going to Ricky and his team for close to 20 years.",
   "(909) 538-4789", "628 S Bon View Ave, Unit B<br>Ontario, CA 91761", "I.E+Automotive+628+S+Bon+View+Ave+Ontario+CA", wkh("8:00 AM – 5:00 PM", "8:00 AM – 3:00 PM"), ("4.8", 65),
   [("", [("Mechanical repair", "Reviewers mention seals, water pumps and radiators."), ("Quotes", "Bring the car by. One reviewer came for a quote and left with it fixed."), ("Maintenance", "Call with the year, make and model.")])],
   (8986100, 6870299), "i-e-automotive-ontario", [("Pete F.", "Very trustworthy and honest.", "FnY0AGxK6Ia995rcAn25pg"), ("Elizabeth D.", "Ricardo and his team are the best mechanics.", "PxkbHtPRKxariw9Z3ZscIg"), ("James S.", "Reliable.. honest.. hardworking... trustworthy...", "PdEzAovZ8E28VapY_H5rhA")])
mk("v-tech-auto-care", dict(hero="split", ink="#0E1A2B", bone="#EFF3F6", acc="#1B5EA8", star="#F2A93B", h1="8.6vw", svc="index", mark="V Tech Auto Care", word="V Tech", wordsz="26vw"),
   "V Tech Auto Care", "Auto repair · Rio Rancho Rd, Pomona", ("The honest", "second quote."), "Auto repair and air conditioning work on Rio Rancho Road. Yelp reviewers say they came after a dealer quote and stayed.",
   "(909) 620-1660", "45 Rio Rancho Rd, Ste 2 C<br>Pomona, CA 91766", "V+Tech+Auto+Care+45+Rio+Rancho+Rd+Pomona+CA", ["8:00 AM – 4:00 PM", "8:00 AM – 3:00 PM", "8:00 AM – 4:00 PM", "8:00 AM – 3:00 PM", "8:00 AM – 4:00 PM", "8:00 AM – 2:00 PM", "Closed"], ("4.7", 50),
   [("", [("Air conditioning repair", ""), ("General repairs", "Reviewers say they bring every car they own."), ("Diagnostics", "Ask what the diagnostic costs when you call.")])],
   (31097241, 8986100), "v-tech-auto-care-pomona-2", [("Jasmine P.", "Hands down to the honesty of this auto repair shop.", "uvDVIF-BaDrwaM2r5FcNlA"), ("Allison S.", "I cannot say enough nice things about V Tech & their staff!", "jJZw5e6D2JXAYQ7GmMFsuw"), ("Mehmeh J.", "Trust them with my cars.", "V6LXDFpXMwW_bHK1vTzwIg"), ("Lee B.", "Air conditioning repair. Very reliable company…", "stc3z_8h9quG8JDEvgc-8g")],
   svc_title="Bring the dealer's quote.")


# Batch 10, researched 2026-11-10 the same way as batches 8 and 9.
_ALT.update({8470881: "Painter working on a car in a body shop", 6870314: "Spray gun painting a car part", 6720519: "Mechanic working on the front of a truck with the hood open"})
mk("japanese-auto-tech", dict(hero="poster", ink="#161616", bone="#F5F3EE", acc="#B91C1C", star="#E5A823", h1="9.6vw", stretch="86%", svc="rows", rowsz="6.4vw", mark="Japanese Auto Tech", word="JAT", wordsz="30vw"),
   "Japanese Auto Tech", "Auto repair · E Arrow Hwy, Upland", ("Diagnosed fast.", "Fixed right."), "An auto repair shop on East Arrow Highway. Yelp reviewers call it honest, reliable and quick to find the problem.",
   "(909) 949-3011", "259 E Arrow Hwy, Ste A<br>Upland, CA 91786", "Japanese+Auto+Tech+259+E+Arrow+Hwy+Upland+CA", wkh("8:00 AM – 4:00 PM", "8:00 AM – 12:00 PM"), ("4.6", 46),
   [("", [("Diagnosis", "One reviewer was diagnosed and back on the road the same morning."), ("Repairs", "Call with the year, make and model."), ("Oil changes", "Ask for a quote by phone.")])],
   (8986100, 6870299), "japanese-auto-tech-upland", [("Debbie T.", "very honest and reliable more than my expectations.", "vQmrVBXKdc-4tRXVh2a-PQ"), ("Felicia W.", "I love this shop Best place to go to", "ZWDdzGf_c7XfR0sfvYlLOw"), ("Tracey T.", "The BEST MECHANIC IN THE STATE!!", "a04kJynNHcusJl6UxPehqg"), ("Mario G.", "Tong diagnosed my problem super fast…", "SYcRGomf_2MpV_Bd2yMT9w")])
mk("german-and-japanese-auto-pro", dict(hero="split", ink="#111827", bone="#F3F4F1", acc="#0F766E", star="#EAB308", h1="8.4vw", svc="index", mark="German & Japanese Auto Pro", word="Auto Pro", wordsz="21vw"),
   "German and Japanese Auto Pro", "German and Japanese car repair · N Central Ave, Upland", ("He listens.", "Then he fixes it."), "Service and repair for German and Japanese cars on North Central Avenue. Yelp reviewers mention a Mercedes, a Honda and an Audi A3.",
   "(909) 587-9394", "825 N Central Ave, Ste E<br>Upland, CA 91786", "German+and+Japanese+Auto+825+N+Central+Ave+Upland+CA", wkh("8:00 AM – 5:00 PM"), ("4.9", 60),
   [("What we work on", [("German cars", "Reviewers mention Mercedes and Audi."), ("Japanese cars", "Reviewers mention Honda.")]), ("What we do", [("Service", "Regular servicing, done by the same mechanic each time."), ("Repairs", "No upselling. Tell us your concerns first.")])],
   (6870311, 8985660), "german-and-japanese-auto-pro-upland-12", [("Melanie B.", "Honest mechanic with reasonable prices.", "VWPuEom7e0_4xbiuEAhDxg"), ("Jackie C.", "An honest mechanic that listens to your concerns…", "bACBO0syhMD7pAVVpvWV6A"), ("Craig L.", "…the best mechanic in in town…", "bBFoBUcymzHZrwUXfw__nA")],
   svc_title="Two kinds of car.")
mk("mendiola-diesel-auto", dict(hero="photo", ink="#17140F", bone="#F4EFE4", acc="#A16207", star="#F5C542", h1="10.4vw", stretch="78%", svc="rows", rowsz="6.4vw", mark="Mendiola Diesel & Auto", word="Mendiola", wordsz="19vw"),
   "Mendiola Diesel & Auto", "Diesel and auto repair · S Garey Ave, Pomona", ("Diesel or gas.", "Call for availability."), "Diesel and auto repair on South Garey Avenue. Call to confirm regular hours. Yelp reviewers name Arturo and mention same-day diagnosis.",
   "(909) 630-1641", "1321 S Garey Ave, Unit C<br>Pomona, CA 91766", "Mendiola+Diesel+%26+Auto+1321+S+Garey+Ave+Pomona+CA", ["8:00 AM – 6:00 PM"] * 7, ("4.8", 58),
   [("", [("Diesel repair", ""), ("Auto repair", ""), ("Diagnosis", "One reviewer was seen the same day.")])],
   (6720519, 8986100), "mendiola-diesel-and-auto-pomona", [("Tanye C.", "PROFESSIONAL SERVICE all around! Arturo is the MAN.", "zlwLwH1AndNsY_HZXgrYvg"), ("Gustavo N.", "Arturo is an excellent mechanic…", "S8uu6nm-8HUwoG0WDyMKuA"), ("Don N.", "Fantastic job Quick response got me in same day…", "nRp1otJEnxAcDLKWS1x53g")])
mk("molinas-tire-towing", dict(hero="block", ink="#151515", bone="#F6F2E7", acc="#1D4ED8", star="#FACC15", h1="10.8vw", stretch="76%", svc="index", mark="Molina's Tire & Towing", word="Molina's", wordsz="20vw"),
   "Molina's Tire & Towing", "Tires and towing · W Mission Blvd, Pomona", ("Flat tire?", "Tow or roll in."), "New and used tires, flat repair and patching, and towing on West Mission Boulevard. Open Saturdays.",
   "(909) 620-5528", "1558 W Mission Blvd<br>Pomona, CA 91766", "Molinas+Tire+%26+Towing+1558+W+Mission+Blvd+Pomona+CA", wkh("8:00 AM – 6:00 PM", "8:00 AM – 4:00 PM"), ("4.5", 58),
   [("Tires", [("New tires", ""), ("Used tires", ""), ("Flat repair and patching", "One reviewer was in and out for a patch in no time.")]), ("On the road", [("Towing", "Call first with where the vehicle is."), ("Mechanical help", "")])],
   (8985660, 31097241), "molinas-tire-and-towing-pomona", [("Daniel P.", "Quick and efficient, came for a tire patch…", "CUf12hT4vBJpmlpmTgCwrw"), ("Abraham H.", "Fueron muy rápidos para hacer el trabajo y muy profesionales.", "Z7h5KyhxE7ypDGWwNdUoUw"), ("Gerardo C.", "Quality & optional brands…", "R2l3ZlZHY2sOP3XBhziA6A")],
   svc_title="Tires and a tow truck.")
mk("williams-independent-auto", dict(hero="split", serif=True, ink="#1F2421", bone="#F2F0EA", acc="#3F6212", star="#D4A72C", h1="8.6vw", svc="rows", rowsz="6.4vw", mark="Williams Independent", word="Williams", wordsz="20vw"),
   "Williams Independent Auto Repair & Smog", "Auto repair and smog · Sierra Ave, Fontana", ("Repair and smog,", "one stop."), "Independent auto repair and smog on Sierra Avenue in Fontana. Open weekdays and Saturday mornings.",
   "(909) 428-6805", "9435 Sierra Ave<br>Fontana, CA 92335", "Williams+Independent+Auto+9435+Sierra+Ave+Fontana+CA", wkh("8:00 AM – 5:00 PM", "8:00 AM – 2:00 PM"), ("4.5", 54),
   [("", [("Auto repair", "Call with the year, make and model."), ("Smog", "Ask what to bring when you call.")])],
   (6870299, 6870311))
mk("rudys-auto-works-paint", dict(hero="photo", ink="#1A1320", bone="#F5F1F4", acc="#9D174D", star="#F2B33D", h1="10vw", svc="index", mark="Rudy's Auto Works", word="Rudy's", wordsz="26vw"),
   "Rudy's Auto Works and Paint", "Body work and paint · Arrow Route, Fontana", ("Dents out.", "Paint on."), "Auto body repair, painting and fender work in Fontana. Yelp reviewers mention a full repaint of a 1970 Chevelle and classic restoration.",
   "(909) 437-0649", "14597 Arrow Route<br>Fontana, CA 92335", "Rudy%27s+Auto+Works+and+Paint+14597+Arrow+Route+Fontana+CA", wkh("8:00 AM – 5:00 PM", "9:00 AM – 2:00 PM"), ("4.8", 51),
   [("", [("Auto body repair", ""), ("Painting", "From a scratch to a full repaint."), ("Fender work", ""), ("Classic restoration", "Mentioned by reviewers. Ask Rudy about your project.")])],
   (8470881, 6870314), "rudys-auto-works-and-paint-fontana", [("Jon F.", "Great for general repair and classic restoration. Fair prices and great service!", "EfYfVMlZPec-0Hv6K9xFPw"), ("Nikki R.", "I have been doing business with Rudy for many years…", "tPpT8lG2HEtUqa2k9V8sNg"), ("Chi T.", "…friendly and helpful people working here.", "kkfdchDGo1yyYjKBBL8gmQ")],
   svc_title="Body, paint, fenders.", find="Reviewers say the shop can be hard to find. Call if you can't spot it.")
mk("auto-repair-foreign-domestic-vw", dict(hero="poster", ink="#0F172A", bone="#F1F5F3", acc="#B45309", star="#F59E0B", h1="9.2vw", stretch="80%", svc="index", mark="Foreign Domestic & VW", word="Chino VW", wordsz="20vw"),
   "Auto Repair Foreign Domestic & VW", "Auto repair · Central Ave, Chino", ("Foreign, domestic", "and Volkswagen."), "Auto repair for foreign and domestic vehicles on Central Avenue in Chino. Yelp reviewers name Maha and call him patient, quick and honest.",
   "(909) 627-5018", "12949 Central Ave<br>Chino, CA 91710", "Auto+Repair+Foreign+Domestic+12949+Central+Ave+Chino+CA", wkh("8:00 AM – 5:00 PM", "8:00 AM – 1:30 PM"), ("4.3", 94),
   [("What we work on", [("Foreign vehicles", ""), ("Domestic vehicles", ""), ("Volkswagen", "")]), ("What we do", [("Check-ups", "One reviewer was overdue and had everything looked over."), ("Repairs", "No talking you into work you don't need.")])],
   (31097241, 6870311), "auto-repair-foreign-domestic-and-vw-chino-3", [("Davia C.", "Maha and his team are quick, reliable, and extremely knowledgeable.", "c78DtOxqB9evkFsuXCNKkw"), ("Sylvia M.", "God bless Maha! You are so very patient and kind!", "Lx84XcA8wf3bfNmO8SR3ww"), ("Brandon C.", "Maha is an awesome mechanic…", "l3GByd-GMXFIcqrKHOaHvw")],
   svc_title="Whatever you drive.")


# Dated listing disagreements, not owner-confirmed schedules. Used beside the table.
HOURS_NOTES = {
    "ceres-collision": "Saved listings disagree on weekday closing: 4:30 or 5 PM.",
    "express-transmissions": "Saved listings disagree on weekday closing: 5 or 6 PM.",
    "l-r-auto-repair": "Saved weekday hours are 9 AM–5 PM or 8 AM–6 PM; Saturday is 10 AM–3 PM or 8 AM–4 PM.",
    "baja-auto-center": "Saved Saturday closing times differ: 1 or 5 PM.",
    "mendiola-diesel-auto": "Saved daily hours differ: 8 AM–6 PM or 9 AM–7 PM.",
    "rudys-auto-works-paint": "Saved Saturday closing times differ: noon or 2 PM.",
    "auto-technik-carcare": "Saved weekday opening times differ: 9 or 9:30 AM. Yelp's full week was not captured.",
    "diamond-auto-center": "Sunday availability is disputed: one saved listing says closed, another says 9 AM–2 PM.",
    "molinas-tire-towing": "Saved Monday opening times differ: 7 or 8 AM. Both listings show Saturday 8 AM–6 PM and Sunday opening at 8 AM, but Sunday closing differs: 5 or 6 PM. Weekend hours need confirmation.",
    "williams-independent-auto": "Saved weekday closing times differ: 5 or 5:30 PM; Saturday closing differs: 2 or 3 PM.",
    "a-tech-automotive": "Saved weekday closing times differ: 5 or 6 PM; Saturday closing differs: 3 or 4 PM.",
    "mailos-auto-repair": "The displayed schedule follows the saved Google listing. Yelp shows longer hours; call if coming early or late.",
}
for _folder, _note in HOURS_NOTES.items():
    SITES[_folder]["hours_note"] = _note
# Do not turn conflicting snapshots into an asserted operating schedule.
SITES["molinas-tire-towing"]["hours"][5:] = ["Call to confirm", "Call to confirm"]
SITES["molinas-tire-towing"]["lede"] = SITES["molinas-tire-towing"]["lede"].replace("Open Saturdays.", "Call to confirm weekend hours.")


# Purrfect Auto Service, Montclair (requested by Andrew 2026-11-12). MapQuest listing read in a browser the same day;
# phone matches the lead sheet. Part of a multi-location name: this page covers the Montclair shop only.
_ALT.update({8985614: "Mechanic repairing a vehicle", 4116207: "Car engine bay"})
mk("purrfect-auto-service", dict(hero="poster", ink="#15131A", bone="#F6F3EE", acc="#BE123C", star="#F2B33D", h1="9.8vw", stretch="88%", svc="index", mark="Purrfect Auto", word="Purrfect", wordsz="20vw"),
   "Purrfect Auto Service", "Auto repair · Arrow Hwy, Montclair", ("Running rough?", "Make it purr."), "Auto maintenance and repair on Arrow Highway in Montclair, from oil changes to engine repairs. Open Saturdays.",
   "(909) 982-1919", "5483 Arrow Hwy<br>Montclair, CA 91763", "Purrfect+Auto+Service+5483+Arrow+Hwy+Montclair+CA", wkh("8:00 AM – 5:30 PM", "8:00 AM – 4:30 PM"), ("4.7", 104),
   [("Maintenance", [("Oil changes", ""), ("A/C work", "Mentioned by a customer of eight years."), ("Transmission service", "")]), ("Repair", [("Engine repairs", "From small fixes to complex engine work."), ("Diagnosis", "Call with the year, make and model.")])],
   (8985614, 4116207), "purrfect-auto-service-montclair-7", [("Denise K.", "Always fair price and good service.", "2kAsBsuEP2dW5TN5PC2gGg"), ("Jennifer S.", "…Richard at this Montclair location has been absolutely awesome.", "33hyWnQDUj0JnkjMmFcZ1w")],
   svc_title="Oil change to engine work.")

# Photo pass, 2026-11-10: every site gets its own photos, chosen to match the trade and the slot (portrait photos only
# in the tall split hero). All are Pexels free-license photos; each id was loaded in a browser and the alt text follows
# the photographer's own title. A check at the bottom of this block fails the build if any photo is used on two sites.
PHOTOS = {
    "sinaloa-tires": [(31097241, "Mechanic working on a wheel in a workshop"), (6641641, "Used tires stacked beside a wall")],
    "king-tire-shop": [(8985660, "Mechanic rolling a tire beside a car on a lift"), (13746781, "Man rolling a tire")],
    "tepa-tire": [(6870316, "Mechanic in a blue uniform holding a car tire"), (6870307, "Mechanic working on a car's brake system"), (13350018, "Close-up of brake pads behind a wheel")],
    "basic-auto-repair": [(8986132, "Mechanic in blue coveralls standing beside a white car"), (4116193, "Hand holding a diagnostic tool")],
    "a-tech-automotive": [(6870326, "Mechanic in blue coveralls holding a diagnostic tool"), (4315570, "Mechanic checking the engine of a car")],
    "johns-auto-repair": [(36608166, "Close-up of a BMW engine in a garage"), (515674, "BMW engine bay")],
    "ceres-collision": [(30250199, "Painter spraying a car in a body shop"), (6870296, "Person buffing a car's paint")],
    "rudys-auto-works-paint": [(40649187, "Bodywork being spray painted in a workshop"), (14615263, "Close-up of a man painting car parts")],
    "mendiola-diesel-auto": [(7541356, "Mechanic repairing the engine of a truck"), (7018493, "Man working underneath a truck")],
    "freddies-auto-repair": [(8985456, "Mechanic fixing a car engine"), (13065696, "Hands pouring oil into an engine")],
    "bates-auto-service": [(6870328, "Mechanic working on the brakes of a car"), (8478234, "Mechanic leaning over a car's engine bay")],
    "express-transmissions": [(8986137, "Underside of a car on a lift"), (8985664, "Technician repairing a motor part")],
    "menas-brake-suspension": [(34277923, "Close-up of a car's disc brake"), (6870300, "Mechanic working at a car's wheel hub")],
    "the-auto-clinic": [(13065693, "Close-up of oil being poured into an engine"), (8985452, "Mechanic looking at the engine of a car")],
    "auto-technik-carcare": [(4116170, "White car in a repair shop"), (36281957, "Mechanic checking a car's oil level")],
    "diamond-auto-center": [(4756887, "Cars inside a repair shop"), (34277926, "Close-up of a brake caliper and disc")],
    "claremont-auto-care": [(29198156, "Car on a lift in an auto repair shop"), (5233282, "Car exhaust pipe")],
    "l-r-auto-repair": [(8986105, "Mechanic in blue coveralls working under a vehicle"), (4022545, "Disc brake in a service workshop")],
    "baja-auto-center": [(5233283, "Silver car with a black exhaust pipe"), (6870295, "Mechanic in blue coveralls checking a vehicle")],
    "ie-automotive": [(8985457, "Mechanic standing beside a white car's open hood"), (4116225, "Person repairing a car engine")],
    "v-tech-auto-care": [(32152039, "Car being serviced in a modern repair shop"), (4116198, "Close-up of a mechanic with a tablet")],
    "japanese-auto-tech": [(8478262, "Mechanic fixing a car under its hood"), (8478213, "Person looking at the engine of a car")],
    "german-and-japanese-auto-pro": [(33055323, "Car engine under an open hood"), (8986033, "White car raised on a lift")],
    "molinas-tire-towing": [(6870331, "Mechanic checking the tire of an orange car"), (10061763, "Tow truck carrying a car")],
    "williams-independent-auto": [(31042165, "Close-up of dual exhaust pipes"), (8986148, "Mechanic in blue checking a car")],
    "auto-repair-foreign-domestic-vw": [(8985517, "Mechanic in a garage"), (13065689, "Close-up of a mechanic working on a car")],
}
for _k, _ps in PHOTOS.items():
    SITES[_k]["photos"] = tuple(PX(i, 1800 if n == 0 else 1200) for n, (i, _) in enumerate(_ps))
    SITES[_k]["alt"] = tuple(a for _, a in _ps)
SITES["ac-tires"]["photos"] = (SITES["ac-tires"]["photos"][0], PX(7807035))
SITES["ac-tires"]["alt"] = (SITES["ac-tires"]["alt"][0], "Mechanic holding a tire wrench")
_seen = {}
for _k, _s in SITES.items():
    for _u in _s["photos"]:
        _id = _u.split("?")[0]
        if _id in _seen and not {_k, _seen[_id]} <= {"el-rey", "el-rey-retro-roadside"}:
            raise SystemExit(f"photo reused: {_id} on {_seen[_id]} and {_k}")
        _seen[_id] = _k


def _lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def vary():
    """Give every site its own mix of details so no two read as copies: button and card shape, label and logo marks,
    footer wordmark, facts strip, statement alignment, section order, visit colour, and service layout.
    The mix is fixed by the site's position in SITES, so rebuilds are stable. Anything set in a site's art wins."""
    for i, (k, s) in enumerate(SITES.items()):
        a = s["art"] = dict(s["art"])
        cls = [["", "sh-sq", "sh-soft"][i % 3], ["", "lb-line", "lb-sq"][(i // 3 + i) % 3], ["", "lg-bar", "lg-none", ""][(i + i // 4) % 4],
               ["", "ft-solid", "", "ft-bone", "ft-none"][i % 5], ["", "fx-bar"][(i // 2) % 2], "st-center" if i % 5 in (1, 3) else "", "rv-row" if i % 4 == 1 else ""]
        a.setdefault("cls", " ".join(c for c in cls if c))
        a.setdefault("order", (i * 2 + i // 3) % 3)
        on = a.get("on_acc", "#ffffff")
        ratio = (max(_lum(a["acc"]), _lum(on)) + .05) / (min(_lum(a["acc"]), _lum(on)) + .05)
        v = ["dark", "accent", "lightv"][(i + i // 3) % 3]
        a.setdefault("visit", "dark" if (v == "accent" and ratio < 4.5) else v)
        if i % 4 == 3 and len([1 for g, its in s["services"] for _ in its]) >= 4:
            a["svc"] = "cards"


vary()

if __name__ == "__main__":
    OUT = pathlib.Path(sys.argv[1])
    only = sys.argv[2:]  # optional: site folder names
    for folder, s in SITES.items():
        if not only or folder in only:
            build(folder, s)

    if not only or "el-rey-retro-roadside" in only:
        css, body = L.layout_d(L.SITES["el-rey-retro-roadside"])
        out = OUT / "el-rey-retro-roadside"
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(V.page(
            L.TITLES["el-rey-retro-roadside"],
            "El Rey de las Tortas. Big tortas. Al pastor tacos. A salsa bar worth making room for. Find El Rey on Riverside Drive. Concept site.",
            css, body))
        print("built el-rey-retro-roadside D")
