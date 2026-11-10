import { chromium } from '/Users/vincentphan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('../',import.meta.url));
const browser=await chromium.launch({channel:'chrome',headless:true});
const results=[];
for(const slug of (process.argv.slice(2).length?process.argv.slice(2):['tepa-tire','muffler-doctor','alejandros-tree-service'])){
  const dir=root+`mockups/${slug}/screenshots`;
  await fs.mkdir(dir,{recursive:true});
  for(const width of [1440,390]){
    const page=await browser.newPage({viewport:{width,height:width===1440?1000:844},deviceScaleFactor:1});
    const errors=[];
    page.on('pageerror',e=>errors.push(String(e)));
    await page.goto(`http://127.0.0.1:8765/mockups/${slug}/`,{waitUntil:'networkidle'});
    await page.evaluate(async()=>{await document.fonts.ready;});
    for(let y=0;y<await page.evaluate(()=>document.body.scrollHeight);y+=600){await page.evaluate(y=>window.scrollTo(0,y),y);await page.waitForTimeout(60);}
    await page.evaluate(()=>window.scrollTo(0,0));
    await page.waitForTimeout(450);
    const metrics=await page.evaluate(()=>({
      overflow:document.documentElement.scrollWidth-innerWidth,
      title:document.title,
      h1:document.querySelectorAll('h1').length,
      missingImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),
      anchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>a.hash.length>1&&!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash),
      calls:[...document.querySelectorAll('a[href^="tel:"]')].map(a=>a.getAttribute('href')),
      emptyLinks:[...document.querySelectorAll('a')].filter(a=>!a.textContent.trim()&&!a.getAttribute('aria-label')).length,
      robots:document.querySelector('meta[name="robots"]')?.content
    }));
    await page.screenshot({path:dir+`/${width}.png`,fullPage:true});
    await page.screenshot({path:dir+`/${width}-fold.png`});
    await page.emulateMedia({reducedMotion:'reduce'});
    const animated=await page.evaluate(()=>document.getAnimations().filter(a=>a.playState==='running').length);
    results.push({slug,width,...metrics,runningAnimationsReducedMotion:animated,errors});
    await page.close();
  }
}
await browser.close();
await fs.writeFile(root+'docs/lead-batch-2026-11-09/browser-results.json',JSON.stringify(results,null,2));
console.log(JSON.stringify(results,null,2));
if(results.some(r=>r.overflow>0||r.errors.length||r.anchors.length||r.h1!==1||r.missingImages.length))process.exitCode=1;
