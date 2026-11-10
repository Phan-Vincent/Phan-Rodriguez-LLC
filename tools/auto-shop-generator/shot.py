import sys,asyncio
from playwright.async_api import async_playwright
PH='<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#6b5a4a"/><stop offset="1" stop-color="#1c1a19"/></linearGradient></defs><rect width="800" height="600" fill="url(#g)"/><circle cx="400" cy="300" r="120" fill="#8a7a6a"/></svg>'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for slug in ['tri-auto','ac-tires','morenos-auto-repair']:
            for w,h,tag in [(1440,900,'d'),(390,844,'m')]:
                pg=await b.new_page(viewport={'width':w,'height':h})
                errs=[]
                pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e:errs.append(str(e)))
                await pg.route('**/images.unsplash.com/**',lambda r:r.fulfill(status=200,content_type='image/svg+xml',body=PH))
                await pg.goto(f'file:///home/claude/phan-vincent/phan-rodriguez-llc/mockups/{slug}/index.html')
                await pg.wait_for_timeout(2500)
                await pg.screenshot(path=f'{slug}-{tag}-top.png')
                await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
                await pg.wait_for_timeout(1200)
                await pg.screenshot(path=f'{slug}-{tag}-full.png',full_page=True)
                ov=await pg.evaluate("document.documentElement.scrollWidth-innerWidth")
                print(slug,tag,'overflow',ov,'errors',errs)
        await b.close()
asyncio.run(main())
