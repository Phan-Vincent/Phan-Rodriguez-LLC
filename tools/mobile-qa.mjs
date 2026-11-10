import {homedir} from 'node:os';
import {fileURLToPath} from 'node:url';
const {chromium}=await import(process.env.PLAYWRIGHT_MODULE || homedir()+'/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs');
import fs from 'node:fs/promises';
const root=fileURLToPath(new URL('../',import.meta.url)).replace(/\/$/,'');
const b=await chromium.launch({channel:'chrome',headless:true});const results=[];
for(const slug of ['tepa-tire','muffler-doctor','alejandros-tree-service'])for(const [width,height] of [[320,740],[360,800],[390,844],[430,932],[768,1024],[844,390]]){
 const p=await b.newPage({viewport:{width,height},isMobile:true,hasTouch:true,reducedMotion:'reduce'});
 const errors=[];p.on('pageerror',e=>errors.push(String(e)));
 await p.goto(`http://127.0.0.1:8765/mockups/${slug}/`,{waitUntil:'domcontentloaded'});
 await p.evaluate(()=>document.fonts.ready);
 for(let y=0;y<await p.evaluate(()=>document.body.scrollHeight);y+=700){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(20);}
 await p.evaluate(()=>scrollTo(0,0));await p.waitForTimeout(150);
 await p.evaluate(()=>Promise.all([...document.images].map(i=>i.complete?Promise.resolve():Promise.race([new Promise(r=>{i.onload=r;i.onerror=r}),new Promise(r=>setTimeout(r,8000))]))));
 const metrics=await p.evaluate(()=>({innerWidth,clientWidth:document.documentElement.clientWidth,overflow:document.documentElement.scrollWidth-innerWidth,clipped:[...document.querySelectorAll('h1,h2,h3,p,summary,.btn,.button,.actions,table')].filter(e=>{const r=e.getBoundingClientRect();return r.width&&getComputedStyle(e).visibility!=='hidden'&&(e.scrollWidth>e.clientWidth+3||r.right>innerWidth+2||r.left < -2)}).map(e=>({tag:e.tagName,class:e.className,text:e.textContent.trim().slice(0,80),scroll:e.scrollWidth,width:e.clientWidth})),images:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src)}));
 if([320,390,430].includes(width)){await p.screenshot({path:`${root}/mockups/${slug}/screenshots/mobile-${width}.png`,fullPage:true});await p.screenshot({path:`${root}/mockups/${slug}/screenshots/mobile-${width}-fold.png`});}
 if(slug==='muffler-doctor'&&width===390)await p.locator('#proof').screenshot({path:root+'/mockups/'+slug+'/screenshots/mobile-review-section.png'});
 let menu=null;const summary=p.locator('details summary');if(await summary.isVisible()){
 await summary.tap();const link=p.locator('details a[href^="#"]').first();const hash=await link.getAttribute('href');await link.tap();await p.waitForTimeout(200);
 menu=await p.evaluate(hash=>{const t=document.querySelector(hash),head=document.querySelector('.site-head');return{closed:!document.querySelector('details').open,anchorTop:t?.getBoundingClientRect().top,stickyBottom:head?.getBoundingClientRect().bottom??0}},hash);
 }
 await p.evaluate(()=>scrollTo(0,document.body.scrollHeight));
 const footer=await p.evaluate(()=>{const fixed=document.querySelector('.mobile-call,.callbar');const f=document.querySelector('footer');return{footerBottom:f.getBoundingClientRect().bottom,viewport:innerHeight,fixed:fixed?{display:getComputedStyle(fixed).display,top:fixed.getBoundingClientRect().top,bottom:fixed.getBoundingClientRect().bottom}:null}});
 results.push({slug,width,height,...metrics,menu,footer,errors});await p.close();
}
await b.close();await fs.writeFile(root+'/docs/lead-batch-2026-11-09/mobile-audit.json',JSON.stringify(results,null,2));console.log(JSON.stringify({checks:results.length,problems:results.filter(r=>r.innerWidth>r.width||r.clipped.length||r.images.length||r.errors.length||(r.menu&&(!r.menu.closed||r.menu.anchorTop<r.menu.stickyBottom-1)))},null,2));
if(results.some(r=>r.innerWidth>r.width||r.clipped.length||r.images.length||r.errors.length||(r.menu&&(!r.menu.closed||r.menu.anchorTop<r.menu.stickyBottom-1))))process.exitCode=1;
