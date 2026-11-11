import fs from 'node:fs/promises';
import path from 'node:path';
import {homedir} from 'node:os';
import {fileURLToPath} from 'node:url';

export function layoutFailure(m, tolerance = 3) {
  return m.right > m.viewport + tolerance || m.left < -tolerance ||
    (m.client > 0 && m.scroll > m.client + tolerance) ||
    (m.parentLeft != null && (m.left < m.parentLeft - tolerance || m.right > m.parentRight + tolerance));
}
export function motionFailure(samples, tolerance = 1) {
  return samples.some(s => s.animations > 0) || samples.some(s =>
    s.positions.some((x, i) => Math.abs(x - samples[0].positions[i]) > tolerance));
}
export function footerFailure(footer, dock, viewport, tolerance = 3) {
  return footer.bottom > viewport + tolerance || (dock &&
    footer.bottom > dock.top + tolerance && footer.top < dock.bottom - tolerance);
}
export function catalogTargets(html) {
  const targets = [...html.matchAll(/href=["'](?:\.\/)?(mockups\/[^"'#?]+)["']/g)]
    .map(m => m[1].endsWith('/') ? m[1] + 'index.html' : m[1]);
  if (!targets.length) throw new Error('Catalog contains no mockup targets');
  if (targets.some(p => !/^mockups\/[a-z0-9-]+\/index\.html$/.test(p))) throw new Error('Unexpected catalog target');
  return [...new Set(targets)].sort();
}

export async function runQA(widths, label) {
  const root = fileURLToPath(new URL('../', import.meta.url));
  const options = {};
  for (let i = 2; i < process.argv.length; i += 2) {
    const key = process.argv[i];
    if (!['--base', '--out'].includes(key) || !process.argv[i + 1]) throw new Error('Use --base URL --out DIRECTORY');
    options[key] = process.argv[i + 1];
  }
  const base = new URL(options['--base'] || process.env.QA_BASE_URL || 'http://127.0.0.1:8765/');
  if (!['http:', 'https:'].includes(base.protocol) || !['localhost', '127.0.0.1', '[::1]'].includes(base.hostname) || base.username || base.password || base.search || base.hash) {
    throw new Error('QA base must be a loopback HTTP(S) URL without credentials, query or fragment');
  }
  if (!base.pathname.endsWith('/')) base.pathname += '/';
  const parent = path.resolve(options['--out'] || process.env.QA_OUTPUT_DIR || path.join(root, 'qa-runs'));
  await fs.mkdir(parent, {recursive: true});
  // Always create a fresh run directory, even when --out is supplied.
  const output = await fs.mkdtemp(path.join(parent, `${label}-`));
  const targets = catalogTargets(await fs.readFile(path.join(root, 'index.html'), 'utf8'));
  const {chromium} = await import(process.env.PLAYWRIGHT_MODULE || homedir() + '/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs');
  const browser = await chromium.launch({headless: true, ...(process.env.QA_BROWSER_CHANNEL ? {channel: process.env.QA_BROWSER_CHANNEL} : {})});
  const results = [];
  try {
    for (const target of targets) for (const width of widths) {
      const context = await browser.newContext({viewport: {width, height: width >= 1000 ? 1000 : 844}, reducedMotion: 'reduce'});
      const page = await context.newPage();
      const failures = [];
      const record = {target, width, failures};
      page.on('pageerror', e => failures.push(`pageerror: ${e.message}`));
      page.on('console', m => {if (m.type() === 'error') failures.push(`console: ${m.text()}`);});
      page.on('requestfailed', r => failures.push(`request: ${r.url()} ${r.failure()?.errorText}`));
      page.on('response', r => {if (r.status() >= 400) failures.push(`HTTP ${r.status()}: ${r.url()}`);});
      try {
        const localHTML = await fs.readFile(path.join(root, target), 'utf8');
        const expectedTitle = localHTML.match(/<title>([\s\S]*?)<\/title>/i)?.[1];
        const response = await page.goto(new URL(target, base).href, {waitUntil: 'load', timeout: 30000});
        if (!response?.ok() || !/text\/html/i.test(response.headers()['content-type'] || '')) throw new Error('Missing HTML response');
        await page.evaluate(() => document.fonts.ready);
        // Force a scrollbar where supported; 305px is also tested explicitly for overlay-scrollbar hosts.
        await page.addStyleTag({content: 'html{overflow-y:scroll!important}'});
        const structure = await page.evaluate(() => ({
          h1: document.querySelectorAll('h1').length,
          title: document.title,
          concept: document.body.textContent.includes('Not the official site of this business.'),
          anchors: [...document.querySelectorAll('a[href^="#"]')].filter(a => {
            if (a.hash.length < 2) return false;
            try {return !document.getElementById(decodeURIComponent(a.hash.slice(1)));} catch {return true;}
          }).map(a => a.getAttribute('href')),
          robots: document.querySelector('meta[name="robots"]')?.content || ''
        }));
        const servedTitle = await page.locator('title').innerHTML();
        if (servedTitle !== expectedTitle || !structure.concept || structure.h1 !== 1 || structure.anchors.length || !structure.robots.includes('noindex')) failures.push({structure});
        const geometry = [];
        const inspect = async () => {
          const metrics = await page.evaluate(() => {
            const viewport = document.documentElement.clientWidth;
            const elements = [...document.querySelectorAll('h1,h2,h3,p,a,button,summary,table,address,.top,.bar .wrap,.facts,.vgrid,.v3,.dock,#review-track')];
            return {viewport, documentWidth: document.documentElement.scrollWidth, elements: elements.flatMap(e => {
              // Review cards intentionally scroll. Still check the track itself.
              if (e.closest('[inert],[aria-hidden="true"],#review-help,.skip') ||
                  (e.closest('#review-track') && e.id !== 'review-track')) return [];
              const style = getComputedStyle(e), r = e.getBoundingClientRect();
              if (!r.width || !r.height || style.visibility === 'hidden' || style.display === 'none') return [];
              const p = e.parentElement.getBoundingClientRect();
              const metric = {text: e.textContent.trim().slice(0, 90), left: r.left, right: r.right,
                client: e.clientWidth, scroll: e.id === 'review-track' ? e.clientWidth : e.scrollWidth, viewport,
                parentLeft: p.left, parentRight: p.right};
              // Test actual glyph bounds too: overflow:hidden must not conceal a failing label.
              const range = document.createRange();
              if (/^(H[1-3]|P|A|BUTTON|SUMMARY|ADDRESS)$/.test(e.tagName)) range.selectNodeContents(e);
              const text = [...range.getClientRects()].map(t => ({text: metric.text, left: t.left, right: t.right,
                client: 0, scroll: 0, viewport, parentLeft: r.left, parentRight: r.right}));
              return [metric, ...text];
            })};
          });
          if (metrics.documentWidth > metrics.viewport + 3) geometry.push({documentWidth: metrics.documentWidth, viewport: metrics.viewport});
          geometry.push(...metrics.elements.filter(m => layoutFailure(m)));
        };
        // Reveal and load content throughout the page, not just the first viewport.
        for (let y = 0; y <= await page.evaluate(() => document.documentElement.scrollHeight); y += 600) {
          await page.evaluate(y => scrollTo(0, y), y);
          await page.waitForTimeout(80);
          await inspect();
        }
        if (geometry.length) failures.push({layout: geometry});
        const missingAssets = await page.evaluate(async () => {
          const urls = new Set([...document.images].map(i => i.currentSrc || i.src));
          for (const e of document.querySelectorAll('*')) for (const pseudo of [null, '::before', '::after']) {
            const bg = getComputedStyle(e, pseudo).backgroundImage;
            for (const m of bg.matchAll(/url\(["']?(.*?)["']?\)/g)) urls.add(new URL(m[1], document.baseURI).href);
          }
          return (await Promise.all([...urls].map(url => new Promise(resolve => {
            const image = new Image();
            const timer = setTimeout(() => resolve(url), 10000);
            image.onload = () => {clearTimeout(timer);resolve(image.naturalWidth ? null : url);};
            image.onerror = () => {clearTimeout(timer);resolve(url);};
            image.src = url;
          })))).filter(Boolean);
        });
        if (missingAssets.length) failures.push({missingAssets});
        await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
        const footer = await page.evaluate(() => {
          const f = document.querySelector('footer');
          const d = [...document.querySelectorAll('.dock,.mobile-call,.callbar')].find(e => getComputedStyle(e).display !== 'none');
          const rect = e => {const r = e.getBoundingClientRect();return {top: r.top, bottom: r.bottom};};
          return {footer: f && rect(f), dock: d && rect(d), viewport: innerHeight};
        });
        if (!footer.footer || footerFailure(footer.footer, footer.dock, footer.viewport)) failures.push({footer});
        // Exercise focus transfer on hide, then confirm the concealed bar cannot take focus.
        if (await page.locator('#bar').count()) {
          await page.locator('#bar a').first().focus();
          await page.evaluate(() => scrollTo(0, 0));
          await page.waitForTimeout(100);
          const sticky = await page.evaluate(() => {
            const b = document.getElementById('bar');
            b.querySelector('a').focus();
            return {inert: b.inert, hidden: b.getAttribute('aria-hidden'), focused: b.contains(document.activeElement)};
          });
          if (!sticky.inert || sticky.hidden !== 'true' || sticky.focused) failures.push({sticky});
        }
        // Test both an initial reduced preference and a change while the carousel is active.
        const tracks = page.locator('#review-track');
        const checkMotion = async () => {
          const samples = [];
          for (let i = 0; i < 4; i++) {
            samples.push(await page.evaluate(() => ({animations: document.getAnimations().filter(a => a.playState === 'running').length,
              positions: [...document.querySelectorAll('#review-track')].map(e => e.scrollLeft)})));
            await page.waitForTimeout(200);
          }
          if (motionFailure(samples)) failures.push({reducedMotion: samples});
        };
        if (await tracks.count()) await tracks.first().scrollIntoViewIfNeeded();
        await page.mouse.move(0, 0);
        await page.evaluate(() => document.activeElement?.blur());
        await page.waitForTimeout(100);
        await checkMotion();
        await page.emulateMedia({reducedMotion: 'no-preference'});
        await page.waitForTimeout(1400);
        await page.emulateMedia({reducedMotion: 'reduce'});
        await page.waitForTimeout(100);
        await checkMotion();
      } catch (e) {failures.push(`check: ${e.message}`);}
      finally {
        results.push(record);
        await context.close();
        await fs.writeFile(path.join(output, 'results.json'), JSON.stringify(results, null, 2));
      }
      console.log(`${failures.length ? 'FAIL' : 'PASS'} ${target} @ ${width}`);
    }
  } finally {await browser.close();}
  console.log(JSON.stringify({output, checks: results.length, failed: results.filter(r => r.failures.length).length}));
  if (results.some(r => r.failures.length)) process.exitCode = 1;
}
