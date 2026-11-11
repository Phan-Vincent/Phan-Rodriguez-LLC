#!/usr/bin/env python3
"""Builds the 22 lead-batch concept sites in the same house style as Tri Auto,
A C Tires and Moreno's (see build_v2.py), rotating three layouts:

  A  split hero, service tiles, photo row, visit card      (like Tri Auto)
  B  photo banner with info bar, service list, week strip  (like A C Tires)
  C  profile page: sticky shop card beside content cards   (like Moreno's)

Run:  python3 tools/auto-shop-generator/build_leads.py mockups

Business facts (names, addresses, phones, hours, ratings, services, quotes) were
carried over from Vincent's verified pages of Nov 9-10, 2026. Nothing new was
invented here. Photos are Pexels/Unsplash free-license stock, loaded by URL.
"""
import sys, pathlib, html

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_v2 import BASE, JS, DAYS, U, page, holiday, marquee, badge, dock  # noqa: E402
import json


def PX(pid, w=1200):
    return f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w={w}"


def esc(t):
    return html.escape(t, quote=False)


def footer(name):
    return f'<footer><div class="wrap"><strong>{name}</strong><span>Concept website by Phan-Rodriguez LLC. Not the official site of this business. Photos are stock images.</span></div></footer>'


def tel(phone):
    return "+1" + "".join(c for c in phone if c.isdigit())


def hours_rows(hours):
    return "".join(f'<tr data-day="{(i + 1) % 7}"><th scope="row">{d}</th><td>{hours[i]}</td></tr>' for i, d in enumerate(DAYS))


def hours_block(s):
    if not s.get("hours"):
        return f'<div class="holiday"><strong>Hours</strong><p>Call <a href="tel:{tel(s["phone"])}">{s["phone"]}</a> for current availability and hours.</p></div>'
    return f'<table><caption class="label" style="text-align:left;padding-bottom:8px">Hours</caption>{hours_rows(s["hours"])}</table>{holiday(s["phone"], tel(s["phone"]))}'


def ratings(s):
    out = []
    for num, label, url in s["ratings"]:
        inner = f'<strong><span data-count="{num}">{num}</span> ★</strong><span>{label}</span>'
        out.append(f'<a class="rate" href="{url}" target="_blank" rel="noopener noreferrer">{inner}<em>Read the reviews ↗</em></a>' if url else f'<div class="rate">{inner}</div>')
    return "".join(out)


def quotes(s):
    if not s.get("quotes"):
        return ""
    src = s["ratings"][0][2]
    return '<div class="qs">' + "".join(f'<blockquote class="card q"><p>“{esc(q)}”</p><cite>From Google reviews</cite></blockquote>' for q in s["quotes"]) + "</div>" + (f'<p style="margin-top:14px"><a class="more" href="{src}" target="_blank" rel="noopener noreferrer">Read the reviews on Google Maps ↗</a></p>' if src else "")


def groups(s, cls="tiles"):
    out = []
    for title, items in s["services"]:
        cards = "".join(f'<div class="card tile"><h3>{esc(n)}</h3>{"<p>" + esc(d) + "</p>" if d else ""}</div>' for n, d in items)
        out.append((f'<h3 class="gt">{esc(title)}</h3>' if title else "") + f'<div class="{cls}">{cards}</div>')
    return "".join(out)


def svc_list(s):
    out = []
    for title, items in s["services"]:
        rows = "".join(f'<li><span class="dot" aria-hidden="true"></span><div><h3>{esc(n)}</h3>{"<p>" + esc(d) + "</p>" if d else ""}</div></li>' for n, d in items)
        out.append((f'<h3 class="gt">{esc(title)}</h3>' if title else "") + f'<ul class="card svc">{rows}</ul>')
    return "".join(out)


def services(s):
    """Each site picks how its services are shown, so the pages do not all read the same."""
    mode = s.get("svc_mode", "tiles")
    if mode == "list":
        return svc_list(s)
    if mode == "two":
        return "".join((f'<h3 class="gt">{esc(t)}</h3>' if t else "") + '<div class="two">' + "".join(f'<div class="it"><h3>{esc(n)}</h3>{"<p>" + esc(d) + "</p>" if d else ""}</div>' for n, d in its) + "</div>" for t, its in s["services"])
    if mode == "chips":
        return "".join((f'<h3 class="gt">{esc(t)}</h3>' if t else "") + '<div class="cloud">' + "".join(f"<span>{esc(n)}</span>" for n, _ in its) + "</div>" for t, its in s["services"])
    if mode == "accordion":
        out = ""
        for t, its in s["services"]:
            out += (f'<h3 class="gt">{esc(t)}</h3>' if t else "") + "".join(f'<details class="acc"{" open" if i == 0 else ""}><summary>{esc(n)}</summary><p>{esc(d)}</p></details>' if d else f'<details class="acc"><summary>{esc(n)}</summary><p>Ask about it when you call.</p></details>' for i, (n, d) in enumerate(its))
        return out
    if mode == "tabs":
        grouped = len(s["services"]) > 1
        tabs = [(t, its) for t, its in s["services"]] if grouped else [(n, [(n, d)]) for n, d in s["services"][0][1]]
        btns = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}">{esc(t)}</button>' for i, (t, _) in enumerate(tabs))
        panels = ""
        for t, its in tabs:
            inner = "".join(f'<li><span class="dot" aria-hidden="true"></span><div><h3>{esc(n)}</h3>{"<p>" + esc(d) + "</p>" if d else ""}</div></li>' for n, d in its)
            panels += f'<div class="panel" role="tabpanel"><ul class="card svc">{inner}</ul></div>'
        return f'<div data-tabs><div class="tabs" role="tablist">{btns}</div>{panels}</div>'
    return groups(s)


def glance(s):
    """At-a-glance card: today's hours, phone, address and rating in one place."""
    t = tel(s["phone"])
    num, label, _ = s["ratings"][0]
    today = f"<strong data-today='{json.dumps(s['hours'])}'>See hours below</strong>" if s.get("hours") else "<strong>Call for hours</strong>"
    return f'''<div class="card glance"><div><span class="label">Today</span>{today}</div><a href="tel:{t}"><span class="label">Call</span><strong>{s['phone']}</strong></a><a href="{s['maps']}" target="_blank" rel="noopener noreferrer"><span class="label">Address</span><strong>{s['addr'].replace('<br>', ', ')}</strong></a><div><span class="label">Rating</span><strong><span data-count="{num}">{num}</span> ★ <small>{label}</small></strong></div></div>'''


def about(s):
    a = s.get("about")
    if not a:
        return ""
    pts = "".join(f"<li><strong>{esc(h)}</strong> {esc(t)}</li>" for h, t in a.get("points", []))
    return f'<h2>{esc(a["title"])}</h2><p>{esc(a["text"])}</p>' + (f'<ul class="pts">{pts}</ul>' if pts else "")


def band(s):
    if not s.get("band"):
        return ""
    items = [n for _, its in s["services"] for n, _ in its][:6]
    return marquee([esc(i) for i in items])


def gbadge(s):
    num, label, _ = s["ratings"][0]
    src, _, cnt = label.partition(" · ")
    return badge(num, cnt).replace("Google rating", f"{src} rating")


def head_vars(s):
    return f":root{{--bg:#F0F2F5;--ink:#050505;--muted:#65676B;--line:#CED0D4;--chip:#E4E6EB;--accent:{s['accent']};--dark:{s['dark']};--gold:{s['gold']};--focus:{s['accent']}}}"


SHARED = """
h2{font-size:clamp(26px,3vw,38px);margin-top:8px}
.lede{font-size:18px;margin-top:18px;max-width:560px}
.sub{font-size:15px;font-weight:600;margin-top:10px}
.actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.gt{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:26px 0 12px}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.tile{padding:22px;border-top:4px solid var(--accent)}.tile h3{font-size:19px}.tile p{color:var(--muted);font-size:15px;margin-top:6px}
.svc li{display:grid;grid-template-columns:14px 1fr;gap:14px;align-items:center;padding:16px 22px;border-bottom:1px solid var(--line)}.svc li:last-child{border:0}
.svc h3{font-size:18px}.svc p{color:var(--muted);font-size:15px;margin-top:3px}.dot{width:10px;height:10px;border-radius:50%;background:var(--accent)}
.rates{display:flex;flex-wrap:wrap;gap:14px}
.rate{display:block;background:#fff;border-radius:8px;box-shadow:0 1px 2px #0003;padding:18px 22px;min-width:200px}
.rate strong{display:block;font-size:30px;letter-spacing:-.02em;color:var(--accent)}.rate span{font-size:13.5px;color:var(--muted)}.rate em{display:block;font-style:normal;font-size:13px;font-weight:600;margin-top:8px;text-decoration:underline;text-underline-offset:4px}
.qs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:16px}
.q{padding:22px}.q p{font-size:19px;font-weight:600;line-height:1.35}.q cite{display:block;font-style:normal;font-size:12.5px;color:var(--muted);margin-top:14px}
.more{font-weight:600;text-decoration:underline;text-underline-offset:4px}
.pts{display:grid;gap:10px;margin-top:16px}.pts li{padding-left:16px;border-left:3px solid var(--gold)}.pts strong{display:block}
.note{margin-top:12px;font-size:14.5px;color:var(--muted)}
address{font-style:normal;font-size:20px;font-weight:600;line-height:1.4}
.bigphone{display:inline-block;font-size:clamp(26px,3.2vw,38px);font-weight:700;letter-spacing:-.02em;margin-top:14px}
.name{font-weight:700;font-size:20px;letter-spacing:-.01em}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px 28px;margin-top:6px}
.it{padding:12px 0 12px 14px;border-left:3px solid var(--accent)}.it h3{font-size:17px}.it p{font-size:14.5px;color:var(--muted);margin-top:3px}
.glance{display:grid}.glance>*{display:block;padding:14px 18px;border-bottom:1px solid var(--line)}.glance>*:last-child{border:0}.glance strong{display:block;font-size:17px;margin-top:2px}.glance small{font-weight:500;color:var(--muted);font-size:13px}.glance a strong{color:var(--accent)}
@media(max-width:860px){.two{grid-template-columns:1fr}}
@media(max-width:860px){.tiles{grid-template-columns:1fr}}
"""

# ------------------------------------------------------------------ layout A
A_CSS = """
header{position:sticky;top:0;z-index:20;background:#fff;box-shadow:0 1px 2px #0000001f}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:60px}
.name{border-left:5px solid var(--accent);padding-left:10px}
nav{display:flex;gap:26px;font-size:14px;font-weight:600}nav a:hover{color:var(--accent)}
.hero{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:48px;align-items:center;padding:40px 0 48px}
h1{font-size:clamp(36px,5vw,64px);line-height:1.02}h1 em{font-style:normal;color:var(--accent)}
.lede{color:var(--muted)}
.hero img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:8px}
section{padding:38px 0}
.intro{max-width:640px;margin-bottom:6px}.intro p{margin-top:10px;color:var(--muted)}
.row{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.row img{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:8px}
.row p{margin-top:12px;color:var(--muted)}
.visit{display:grid;grid-template-columns:1fr 1fr;gap:40px;padding:34px;align-items:center;--row:#F0F2F5}
@media(max-width:860px){nav{display:none}.hero{grid-template-columns:1fr;gap:26px;padding:26px 0 36px}.hero .shot{order:-1}.row{grid-template-columns:1fr;gap:18px}.visit{grid-template-columns:1fr;padding:22px}section{padding:38px 0}.name{font-size:17px}header .btn{white-space:nowrap;padding:8px 12px;font-size:14px}}
"""


def layout_a(s):
    t = tel(s["phone"])
    body = f"""
<header><div class="wrap"><a href="#" class="name">{esc(s['short'])}</a>
<nav aria-label="Main"><a href="#services">{s.get('svc_nav', 'Services')}</a><a href="#reviews">Reviews</a><a href="#visit">Visit</a></nav>
<a class="btn" href="tel:{t}">{s['phone']}</a></div></header>
<main id="main">
<div class="wrap hero"><div><span class="label">{esc(s['kicker'])}</span><h1 style="margin-top:10px">{esc(s['h1'][0])} <em>{esc(s['h1'][1])}</em></h1>
{f'<p class="sub">{esc(s["sub"])}</p>' if s.get('sub') else ''}<p class="lede">{esc(s['lede'])}</p>
<div class="actions"><a class="btn primary" href="tel:{t}">Call {s['phone']}</a><a class="btn" href="#visit">Hours &amp; directions</a></div></div>
<div class="shot"><img alt="{esc(s['alt'][0])}" src="{s['photos'][0]}">{gbadge(s)}</div></div>
{band(s)}
<section id="services"><div class="wrap"><div class="intro"><span class="label">{s.get('svc_label', 'What we do')}</span><h2>{esc(s['svc_title'])}</h2>{f'<p>{esc(s["svc_text"])}</p>' if s.get('svc_text') else ''}</div>
{services(s)}{f'<p class="note">{esc(s["svc_note"])}</p>' if s.get('svc_note') else ''}</div></section>
{f'<section><div class="wrap row"><img loading="lazy" alt="{esc(s["alt"][1])}" src="{s["photos"][1]}"><div>{about(s)}</div></div></section>' if s.get('about') else ''}
<section id="reviews"><div class="wrap"><span class="label">Reviews</span><h2>{esc(s['rev_title'])}</h2>{f'<p class="note" style="max-width:640px">{esc(s["rev_text"])}</p>' if s.get('rev_text') else ''}
<div class="rates" style="margin-top:18px">{ratings(s)}</div>{quotes(s)}</div></section>
<section id="visit"><div class="wrap"><div class="card visit">
<div><span class="label">Visit</span><h2>{esc(s.get('visit_title', 'Find us.'))}</h2><address style="margin-top:14px">{s['addr']}</address>{f'<p class="note">{esc(s["find"])}</p>' if s.get('find') else ''}
<a class="bigphone" href="tel:{t}">{s['phone']}</a>
<div class="actions"><a class="btn primary" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a></div></div>
<div>{hours_block(s)}</div></div></div></section>
</main>
{footer(s['footer'])}
{dock(s['phone'], t, s['maps'])}
"""
    return head_vars(s) + SHARED + A_CSS, body


# ------------------------------------------------------------------ layout B
B_CSS = """
header{background:var(--dark);color:#fff;--focus:#fff}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:64px}
nav{display:flex;gap:26px;font-size:14px;font-weight:600}nav a:hover{text-decoration:underline;text-underline-offset:5px}
header .btn{background:#fff;color:var(--dark)}
.banner{overflow:hidden;position:relative;color:#fff;background:linear-gradient(90deg,color-mix(in srgb,var(--dark) 96%,transparent) 0,color-mix(in srgb,var(--dark) 84%,transparent) 48%,color-mix(in srgb,var(--dark) 38%,transparent) 100%),var(--img) center/cover var(--dark);--focus:#fff}
.banner .wrap{position:relative;z-index:1;padding:64px 0 116px}.banner .label{color:#ffffffcc}
h1{font-size:clamp(36px,5.2vw,66px);line-height:1.03;max-width:720px;margin-top:10px}h1 .hl{color:var(--gold)}
.banner .lede{color:#ffffffe0}.banner .sub{color:var(--gold)}
.bar{display:grid;grid-template-columns:repeat(3,1fr);margin-top:-64px;position:relative;z-index:2}
.bar>*{padding:22px 24px;border-right:1px solid var(--line)}.bar>*:last-child{border:0}
.bar strong{display:block;font-size:19px;letter-spacing:-.01em;margin-top:4px}.bar a strong{color:var(--accent)}
.bar small{display:block;color:var(--muted);font-size:13.5px;margin-top:2px}
section{padding:44px 0 0}
.split{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:48px;align-items:start}
.side p{color:var(--muted);margin-top:12px;max-width:380px}
.side img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:8px;margin-top:22px}
.list .gt:first-child{margin-top:0}
.aboutc{padding:30px;background:var(--dark)!important;color:#fff}.aboutc p{color:#ffffffd9;margin-top:10px;max-width:720px}.aboutc .pts li{border-color:var(--gold)}
.week{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin-top:22px}
.day{padding:16px 8px;text-align:center}.dname{display:block;font-weight:700;font-size:14px}.day .tag{display:block;margin:6px auto 0;width:max-content}
.day span.h{display:block;font-size:13px;color:var(--muted);margin-top:6px;line-height:1.35}
.day.today{background:var(--dark);color:#fff}.day.today span.h{color:#ffffffcc}
.find{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;padding:26px 28px;margin-top:14px}
@media(max-width:860px){nav{display:none}.name{font-size:17px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}header .btn{white-space:nowrap;padding:8px 12px;font-size:14px}.banner .wrap{padding:48px 0 96px}.bar{grid-template-columns:1fr}.bar>*{border-right:0;border-bottom:1px solid var(--line)}.split{grid-template-columns:1fr;gap:24px}.week{grid-template-columns:1fr 1fr}.find{grid-template-columns:1fr}section{padding:42px 0 0}}
"""


def layout_b(s):
    t = tel(s["phone"])
    week = ""
    if s.get("hours"):
        short = [h.replace(":00", "") for h in s["hours"]]
        week = '<div class="week">' + "".join(f'<div class="card day" data-day="{(i + 1) % 7}"><span class="dname">{d[:3]}</span><span class="h">{short[i]}</span></div>' for i, d in enumerate(DAYS)) + "</div>"
    body = f"""
<header><div class="wrap"><a href="#" class="name">{esc(s['short'])}</a>
<nav aria-label="Main"><a href="#services">{s.get('svc_nav', 'Services')}</a><a href="#reviews">Reviews</a><a href="#visit">Hours &amp; location</a></nav>
<a class="btn" href="tel:{t}">{s['phone']}</a></div></header>
<main id="main">
<div class="banner" role="img" aria-label="{esc(s['alt'][0])}" style="--img:url({s['photos'][0]})"><div class="wrap">
<span class="label">{esc(s['kicker'])}</span><h1>{esc(s['h1'][0])} <span class="hl">{esc(s['h1'][1])}</span></h1>
{f'<p class="sub">{esc(s["sub"])}</p>' if s.get('sub') else ''}<p class="lede">{esc(s['lede'])}</p></div></div>
<div class="wrap"><div class="card bar">
<div><span class="label">{esc(s['bar'][0])}</span><strong>{esc(s['bar'][1])}</strong><small>{esc(s['bar'][2])}</small></div>
<a href="tel:{t}"><span class="label">Call</span><strong>{s['phone']}</strong><small>Tap to call</small></a>
<a href="#visit"><span class="label">Find us</span><strong style="color:var(--ink)">{esc(s['addr_short'][0])}</strong><small>{esc(s['addr_short'][1])}</small></a>
</div></div>
{f'<div style="margin-top:36px">{band(s)}</div>' if s.get('band') else ''}
<section id="services"><div class="wrap split">
<div class="side"><span class="label">{s.get('svc_label', 'What we do')}</span><h2>{esc(s['svc_title'])}</h2>{f'<p>{esc(s["svc_text"])}</p>' if s.get('svc_text') else ''}
<img loading="lazy" alt="{esc(s['alt'][1])}" src="{s['photos'][1]}"></div>
<div class="list">{services(s)}{f'<p class="note">{esc(s["svc_note"])}</p>' if s.get('svc_note') else ''}</div>
</div></section>
{f'<section><div class="wrap"><div class="card aboutc">{about(s)}</div></div></section>' if s.get('about') else ''}
<section id="reviews"><div class="wrap"><span class="label">Reviews</span><h2>{esc(s['rev_title'])}</h2>{f'<p class="note" style="max-width:640px">{esc(s["rev_text"])}</p>' if s.get('rev_text') else ''}
<div class="rates" style="margin-top:18px">{ratings(s)}</div>{quotes(s)}</div></section>
<section id="visit"><div class="wrap"><span class="label">Hours &amp; location</span><h2>{esc(s.get('visit_title', 'Find us.'))}</h2>
{week}{holiday(s['phone'], t) if s.get('hours') else hours_block(s)}
<div class="card find"><div><address>{s['addr'].replace('<br>', ', ')}</address>{f'<p class="note" style="margin-top:6px">{esc(s["find"])}</p>' if s.get('find') else ''}</div>
<div class="actions" style="margin:0"><a class="btn primary" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a><a class="btn" href="tel:{t}">Call {s['phone']}</a></div></div>
</div></section>
</main>
{footer(s['footer'])}
{dock(s['phone'], t, s['maps'])}
"""
    return head_vars(s) + SHARED + B_CSS, body


# ------------------------------------------------------------------ layout C
C_CSS = """
.cover{height:clamp(220px,32vw,400px);background:linear-gradient(180deg,#0000 55%,#0008 100%),var(--img) center 45%/cover var(--dark);border-radius:0 0 8px 8px}
.layout{display:grid;grid-template-columns:340px minmax(0,1fr);gap:24px;align-items:start;margin-top:-56px;position:relative}
.shop{position:sticky;top:16px;padding:24px;--row:#F0F2F5;--today:var(--dark)}
.shop h1{font-size:26px}.shop .sub{font-size:13px;font-weight:600;color:var(--muted);margin-top:4px}
.shop .rates{margin:16px 0;padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);gap:18px}
.shop .rate{box-shadow:none;padding:0;min-width:0}.shop .rate strong{font-size:22px;color:var(--ink)}.shop .rate span{font-size:12px}.shop .rate em{font-size:12px;margin-top:4px}
.shop .btn{width:100%;margin-top:8px}
.shop address{font-size:16px;margin:16px 0 4px}
.shop table{font-size:14px;margin-top:14px}.shop th,.shop td{padding:7px 10px}
.feed{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;min-width:0}
.feed>.card{padding:28px}
.lead h2{font-size:clamp(34px,4.8vw,58px);line-height:1.02;margin:0}.lead h2 em{font-style:normal;color:var(--accent)}
.lead p{color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}.chips span{font-size:13px;font-weight:700;padding:7px 12px;border-radius:6px;background:var(--chip)}
.chips span:nth-child(3n+1){background:var(--dark);color:#fff}.chips span:nth-child(3n+2){background:var(--gold);color:#111}
h2.t{font-size:24px;margin-top:6px}

.photo{padding:0!important;overflow:hidden}.photo img{width:100%;aspect-ratio:21/9;object-fit:cover}
.aboutc{background:var(--dark)!important;color:#fff}.aboutc h2{font-size:24px;margin:0}.aboutc p{color:#ffffffd9;margin-top:10px}.aboutc .pts li{border-color:var(--gold)}
.feed .rates{display:none}
@media(max-width:900px){.layout{grid-template-columns:1fr;margin-top:-40px}.shop{position:static}.feed>.card{padding:22px}}
"""


def layout_c(s):
    t = tel(s["phone"])
    items = services(s) if s.get('svc_mode') else ''.join((f'<h3 class="gt">{esc(t)}</h3>' if t else '') + '<div class="two">' + ''.join(f'<div class="it"><h3>{esc(n)}</h3>{"<p>" + esc(d) + "</p>" if d else ""}</div>' for n, d in its) + '</div>' for t, its in s['services'])
    chips = "".join(f"<span>{esc(c)}</span>" for c in s.get("chips", []))
    body = f"""
{band(s)}
<main id="main">
<div class="wrap"><div class="cover" role="img" aria-label="{esc(s['alt'][0])}" style="--img:url({s['photos'][0]})">{gbadge(s)}</div>
<div class="layout">
<aside class="card shop" id="visit" aria-label="Shop details">
<h1>{esc(s['short'])}</h1><p class="sub">{esc(s['kicker'])}</p>
<div class="rates">{ratings(s)}</div>
<a class="btn primary" href="tel:{t}">Call {s['phone']}</a>
<a class="btn" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a>
<address>{s['addr']}</address>{f'<p class="note" style="margin-top:4px">{esc(s["find"])}</p>' if s.get('find') else ''}
{hours_block(s)}
</aside>
<div class="feed">
<div class="card lead"><h2>{esc(s['h1'][0])} <em>{esc(s['h1'][1])}</em></h2>{f'<p class="sub" style="color:var(--ink)">{esc(s["sub"])}</p>' if s.get('sub') else ''}<p class="lede">{esc(s['lede'])}</p>
{f'<div class="chips">{chips}</div>' if chips else ''}</div>
<div class="card" id="services"><span class="label">{s.get('svc_label', 'Services')}</span><h2 class="t">{esc(s['svc_title'])}</h2>{f'<p class="note">{esc(s["svc_text"])}</p>' if s.get('svc_text') else ''}{items}{f'<p class="note">{esc(s["svc_note"])}</p>' if s.get('svc_note') else ''}</div>
<div class="card photo"><img loading="lazy" alt="{esc(s['alt'][1])}" src="{s['photos'][1]}"></div>
{f'<div class="card aboutc">{about(s)}</div>' if s.get('about') else ''}
<div class="card" id="reviews"><span class="label">Reviews</span><h2 class="t">{esc(s['rev_title'])}</h2>{f'<p class="note">{esc(s["rev_text"])}</p>' if s.get('rev_text') else ''}{quotes(s)}
<p style="margin-top:14px">{" · ".join(f'<a class="more" href="{u}" target="_blank" rel="noopener noreferrer">{n} ★ {l} ↗</a>' if u else f"{n} ★ {l}" for n, l, u in s['ratings'])}</p></div>
</div></div></div>
</main>
{footer(s['footer'])}
{dock(s['phone'], t, s['maps'])}
"""
    return head_vars(s) + SHARED + C_CSS, body



# ------------------------------------------------------------------ layout D: poster
D_CSS = """
header{background:var(--dark);color:#fff;--focus:#fff}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:60px}
nav{display:flex;gap:24px;font-size:14px;font-weight:600;align-items:center}nav a:hover{text-decoration:underline;text-underline-offset:5px}
.poster{background:var(--dark);color:#fff;--focus:#fff;padding:34px 0 0}
.poster .label{color:var(--gold)}
h1{font-size:clamp(40px,7.4vw,104px);line-height:.96;letter-spacing:-.045em;margin-top:12px}h1 .hl{color:var(--gold)}
.pgrid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,.9fr);gap:36px;align-items:end;margin-top:22px}
.poster .lede{color:#ffffffde;margin:0}
.facts{display:grid;gap:0;border-top:1px solid #ffffff3d}
.facts>*{display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-bottom:1px solid #ffffff3d;font-size:15px}.facts span{color:#ffffffb8}.facts strong{text-align:right}
.pshots{display:grid;grid-template-columns:1.4fr 1fr;gap:12px;margin-top:30px;transform:translateY(40px);margin-bottom:0}
.pshots img{width:100%;height:clamp(180px,24vw,320px);object-fit:cover;border-radius:8px;box-shadow:0 20px 40px -20px #000a}
main>section{padding:40px 0 0}main>section:first-of-type{padding-top:80px}
.cols{display:grid;grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr);gap:40px;align-items:start}
.cols>div:first-child p{color:var(--muted);margin-top:10px}
.aboutc{padding:28px;background:var(--dark)!important;color:#fff}.aboutc p{color:#ffffffd9;margin-top:10px;max-width:760px}
.v3{display:grid;grid-template-columns:1fr 1.2fr 1fr;gap:14px;margin-top:16px;align-items:stretch}.v3>.card{padding:22px;--row:#F0F2F5}
.v3 .btn{width:100%;margin-top:10px}
@media(max-width:860px){nav{display:none}.pgrid{grid-template-columns:1fr;gap:20px}.pshots{grid-template-columns:1fr}.pshots img:last-child{display:none}.cols{grid-template-columns:1fr;gap:16px}.v3{grid-template-columns:1fr}main>section:first-of-type{padding-top:64px}}
"""


def layout_d(s):
    t = tel(s["phone"])
    today = f"<strong data-today='{json.dumps(s['hours'])}'>See below</strong>" if s.get("hours") else "<strong>Call for hours</strong>"
    num, label, _ = s["ratings"][0]
    body = f"""
<header><div class="wrap"><a href="#" class="name">{esc(s['short'])}</a>
<nav aria-label="Main"><a href="#services">{s.get('svc_nav', 'Services')}</a><a href="#reviews">Reviews</a><a href="#visit">Visit</a><a class="btn" style="background:#fff;color:var(--dark)" href="tel:{t}">{s['phone']}</a></nav></div></header>
<main id="main">
<div class="poster"><div class="wrap"><span class="label">{esc(s['kicker'])}</span>
<h1>{esc(s['h1'][0])} <span class="hl">{esc(s['h1'][1])}</span></h1>
<div class="pgrid"><div>{f'<p class="sub" style="color:var(--gold)">{esc(s["sub"])}</p>' if s.get('sub') else ''}<p class="lede">{esc(s['lede'])}</p>
<div class="actions"><a class="btn primary" href="tel:{t}">Call {s['phone']}</a><a class="btn" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a></div></div>
<div class="facts"><div><span>Today</span>{today}</div><div><span>Where</span><strong>{s['addr'].replace('<br>', ', ')}</strong></div><div><span>Rating</span><strong><span data-count="{num}">{num}</span> ★ {label}</strong></div></div></div>
<div class="pshots"><img alt="{esc(s['alt'][0])}" src="{s['photos'][0]}"><img alt="{esc(s['alt'][1])}" src="{s['photos'][1]}"></div>
</div></div>
<section id="services"><div class="wrap cols"><div><span class="label">{s.get('svc_label', 'What we do')}</span><h2>{esc(s['svc_title'])}</h2>{f'<p>{esc(s["svc_text"])}</p>' if s.get('svc_text') else ''}{f'<p class="note">{esc(s["svc_note"])}</p>' if s.get('svc_note') else ''}</div>
<div>{services(s)}</div></div></section>
{f'<section><div class="wrap"><div class="card aboutc">{about(s)}</div></div></section>' if s.get('about') else ''}
<section id="reviews"><div class="wrap cols"><div><span class="label">Reviews</span><h2>{esc(s['rev_title'])}</h2>{f'<p>{esc(s["rev_text"])}</p>' if s.get('rev_text') else ''}</div>
<div><div class="rates">{ratings(s)}</div>{quotes(s)}</div></div></section>
<section id="visit"><div class="wrap"><span class="label">Visit</span><h2>{esc(s.get('visit_title', 'Find us.'))}</h2>
<div class="v3"><div class="card"><address>{s['addr']}</address>{f'<p class="note">{esc(s["find"])}</p>' if s.get('find') else ''}<a class="btn primary" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a><a class="btn" href="tel:{t}">Call {s['phone']}</a></div>
<div class="card">{hours_block(s)}</div>
<div class="card" style="padding:0;overflow:hidden"><img loading="lazy" alt="" style="width:100%;height:100%;min-height:220px;object-fit:cover" src="{s['photos'][1]}"></div></div>
</div></section>
</main>
{footer(s['footer'])}
{dock(s['phone'], t, s['maps'])}
"""
    return head_vars(s) + SHARED + D_CSS, body


# ------------------------------------------------------------------ layout E: framed photo
E_CSS = """
body{background:var(--bg)}
.frame{position:relative;margin:12px;border-radius:14px;overflow:hidden;color:#fff;min-height:min(78vh,620px);display:flex;flex-direction:column;justify-content:space-between;background:linear-gradient(180deg,#0009 0,#0000 30%,#0000 45%,#000c 100%),var(--img) center/cover var(--dark);--focus:#fff}
.ftop{display:flex;justify-content:space-between;align-items:center;gap:20px;padding:20px 26px}
.ftop nav{display:flex;gap:22px;font-size:14px;font-weight:600}.ftop nav a:hover{text-decoration:underline;text-underline-offset:5px}
.fbot{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,.6fr);gap:30px;align-items:end;padding:26px}
.frame .label{color:#ffffffd9}
h1{font-size:clamp(38px,6vw,84px);line-height:.98;font-weight:600!important;letter-spacing:-.04em;margin-top:10px}h1 .hl{color:var(--gold)}
.frame .lede{color:#ffffffe6;max-width:520px;margin-top:14px}
.glass{background:#ffffff1f;backdrop-filter:blur(14px);border:1px solid #ffffff3d;border-radius:10px;padding:18px}
.glass strong{display:block;font-size:18px}.glass span{font-size:13px;color:#ffffffcc}.glass .btn{width:100%;margin-top:12px}
main>section{padding:34px 0 0}
.ed{display:grid;grid-template-columns:300px minmax(0,1fr);gap:36px;align-items:start;border-top:1px solid var(--line);padding-top:26px}
.ed>div:first-child{position:sticky;top:16px}.ed h2{font-size:clamp(24px,2.6vw,34px);margin-top:8px}
.ed>div:first-child p{color:var(--muted);margin-top:8px;font-size:15px}
.wide{width:100%;aspect-ratio:21/8;object-fit:cover;border-radius:10px;margin-top:6px}
.vpanel{background:var(--dark);color:#fff;border-radius:14px;margin:34px 12px 0;padding:34px 0;--row:#ffffff14;--today:var(--gold);--on-today:#111;--muted:#ffffffbf;--chip:#ffffff1f;--ink:#fff;--focus:#fff}
.vpanel .wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}.vpanel .label{color:var(--gold)}.vpanel address{margin-top:12px}
.vpanel .btn{color:#111;background:#fff}.vpanel .btn.primary{background:var(--gold);color:#111}.vpanel .btn.primary:before{background:#fff}.vpanel .holiday a{color:#fff}
@media(max-width:860px){.ftop nav{display:none}.fbot{grid-template-columns:1fr;padding:18px}.ftop{padding:16px 18px}.ed{grid-template-columns:1fr;gap:12px}.ed>div:first-child{position:static}.vpanel .wrap{grid-template-columns:1fr;gap:22px}.frame{margin:8px;min-height:560px}.vpanel{margin:28px 8px 0}.wide{aspect-ratio:16/9}}
"""


def layout_e(s):
    t = tel(s["phone"])
    today = f"<strong data-today='{json.dumps(s['hours'])}'>See hours below</strong>" if s.get("hours") else "<strong>Call for hours</strong>"
    num, label, _ = s["ratings"][0]
    body = f"""
<main id="main">
<div class="frame" style="--img:url({s['photos'][0]})"><div class="ftop"><a href="#" class="name">{esc(s['short'])}</a>
<nav aria-label="Main"><a href="#services">{s.get('svc_nav', 'Services')}</a><a href="#reviews">Reviews</a><a href="#visit">Visit</a><a href="tel:{t}">{s['phone']}</a></nav></div>
<div class="fbot"><div><span class="label">{esc(s['kicker'])}</span><h1>{esc(s['h1'][0])} <span class="hl">{esc(s['h1'][1])}</span></h1><p class="lede">{esc(s['lede'])}</p></div>
<div class="glass"><span>Today</span>{today}<span style="display:block;margin-top:10px"><span data-count="{num}">{num}</span> ★ {label}</span><a class="btn primary" href="tel:{t}">Call {s['phone']}</a></div></div></div>
<section id="services"><div class="wrap ed"><div><span class="label">{s.get('svc_label', 'What we do')}</span><h2>{esc(s['svc_title'])}</h2>{f'<p>{esc(s["svc_text"])}</p>' if s.get('svc_text') else ''}</div>
<div>{services(s)}{f'<p class="note">{esc(s["svc_note"])}</p>' if s.get('svc_note') else ''}</div></div></section>
{f'<section><div class="wrap ed"><div><span class="label">Good to know</span></div><div>{about(s)}<img class="wide" loading="lazy" alt="{esc(s["alt"][1])}" src="{s["photos"][1]}"></div></div></section>' if s.get('about') else f'<section><div class="wrap"><img class="wide" loading="lazy" alt="{esc(s["alt"][1])}" src="{s["photos"][1]}"></div></section>'}
<section id="reviews"><div class="wrap ed"><div><span class="label">Reviews</span><h2>{esc(s['rev_title'])}</h2>{f'<p>{esc(s["rev_text"])}</p>' if s.get('rev_text') else ''}</div>
<div><div class="rates">{ratings(s)}</div>{quotes(s)}</div></div></section>
<div class="vpanel" id="visit"><div class="wrap"><div><span class="label">Visit</span><h2>{esc(s.get('visit_title', 'Find us.'))}</h2><address>{s['addr']}</address>{f'<p class="note">{esc(s["find"])}</p>' if s.get('find') else ''}
<div class="actions"><a class="btn primary" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a><a class="btn" href="tel:{t}">Call {s['phone']}</a></div></div>
<div>{hours_block(s)}</div></div></div>
</main>
{footer(s['footer'])}
{dock(s['phone'], t, s['maps'])}
"""
    return head_vars(s) + SHARED + E_CSS, body


# ------------------------------------------------------------------ layout F: service desk
F_CSS = """
header{position:sticky;top:0;z-index:20;background:#fff;box-shadow:0 1px 2px #0000001f}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:60px}
.name{display:flex;align-items:center;gap:10px}.name:before{content:"";width:14px;height:14px;border-radius:4px;background:var(--accent);box-shadow:8px 8px 0 -3px var(--gold)}
nav{display:flex;gap:26px;font-size:14px;font-weight:600}nav a:hover{color:var(--accent)}
.desk{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:28px;align-items:stretch;padding:34px 0 0}
.desk>div:first-child{display:flex;flex-direction:column;justify-content:center}
h1{font-size:clamp(36px,5vw,64px);line-height:1.02}h1 em{font-style:normal;color:var(--accent)}
.lede{color:var(--muted)}
.strip{width:100%;height:clamp(200px,26vw,340px);object-fit:cover;border-radius:8px;margin-top:22px;display:block}
main>section{padding:36px 0 0}
.cols{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;align-items:start}
.box{padding:26px}.box h2{font-size:clamp(22px,2.4vw,30px);margin-top:6px}.box>p{color:var(--muted);margin-top:8px}
.visit{display:grid;grid-template-columns:1fr 1fr;gap:34px;padding:28px;align-items:center;--row:#F0F2F5}
@media(max-width:860px){nav{display:none}.desk{grid-template-columns:1fr;padding-top:22px}.cols{grid-template-columns:1fr}.visit{grid-template-columns:1fr;padding:22px}header .btn{white-space:nowrap;padding:8px 12px;font-size:14px}.name{font-size:17px}}
"""


def layout_f(s):
    t = tel(s["phone"])
    body = f"""
<header><div class="wrap"><a href="#" class="name">{esc(s['short'])}</a>
<nav aria-label="Main"><a href="#services">{s.get('svc_nav', 'Services')}</a><a href="#reviews">Reviews</a><a href="#visit">Visit</a></nav>
<a class="btn" href="tel:{t}">{s['phone']}</a></div></header>
<main id="main">
<div class="wrap"><div class="desk"><div><span class="label">{esc(s['kicker'])}</span><h1 style="margin-top:10px">{esc(s['h1'][0])} <em>{esc(s['h1'][1])}</em></h1>
{f'<p class="sub">{esc(s["sub"])}</p>' if s.get('sub') else ''}<p class="lede">{esc(s['lede'])}</p>
<div class="actions"><a class="btn primary" href="tel:{t}">Call {s['phone']}</a><a class="btn" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a></div></div>
{glance(s)}</div>
<img class="strip" alt="{esc(s['alt'][0])}" src="{s['photos'][0]}"></div>
<section id="services"><div class="wrap cols"><div class="card box"><span class="label">{s.get('svc_label', 'What we do')}</span><h2>{esc(s['svc_title'])}</h2>{f'<p>{esc(s["svc_text"])}</p>' if s.get('svc_text') else ''}{f'<p class="note">{esc(s["svc_note"])}</p>' if s.get('svc_note') else ''}
<img loading="lazy" alt="{esc(s['alt'][1])}" src="{s['photos'][1]}" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:8px;margin-top:16px"></div>
<div>{services(s)}</div></div></section>
<section id="reviews"><div class="wrap cols"><div class="card box"><span class="label">Reviews</span><h2>{esc(s['rev_title'])}</h2>{f'<p>{esc(s["rev_text"])}</p>' if s.get('rev_text') else ''}<div class="rates" style="margin-top:14px">{ratings(s)}</div></div>
<div>{quotes(s) if s.get('quotes') else (f'<div class="card box">{about(s)}</div>' if s.get('about') else '')}</div></div></section>
{f'<section><div class="wrap"><div class="card box">{about(s)}</div></div></section>' if s.get('about') and s.get('quotes') else ''}
<section id="visit"><div class="wrap"><div class="card visit"><div><span class="label">Visit</span><h2>{esc(s.get('visit_title', 'Find us.'))}</h2><address style="margin-top:12px">{s['addr']}</address>{f'<p class="note">{esc(s["find"])}</p>' if s.get('find') else ''}
<div class="actions"><a class="btn primary" href="{s['maps']}" target="_blank" rel="noopener noreferrer">Get directions</a><a class="btn" href="tel:{t}">Call {s['phone']}</a></div></div>
<div>{hours_block(s)}</div></div></div></section>
</main>
{footer(s['footer'])}
{dock(s['phone'], t, s['maps'])}
"""
    return head_vars(s) + SHARED + F_CSS, body


LAYOUTS = {"A": layout_a, "B": layout_b, "C": layout_c, "D": layout_d, "E": layout_e, "F": layout_f}


def gmaps(q):
    return "https://www.google.com/maps/search/?api=1&query=" + q.replace(" ", "+").replace("&", "%26").replace("'", "%27")


def wk(mf, sat, sun):
    return [mf] * 5 + [sat, sun]


ELREY_MENU = [("", [
    ("Tortas", "Huge portions and the famous Torta Cubana. This is El Rey de las Tortas, after all."),
    ("Tacos", "Al pastor, asada, chicken and tripe. Asada tacos come with grilled onions and chips on the side."),
    ("Burritos", "Carne asada burritos and breakfast burritos, including chorizo."),
    ("Weekend specials", "Barbacoa de res, borrego en penca, barbacoa plate and consomé de borrego. Saturday and Sunday."),
    ("Drinks & raspados", "Licuados y biónicos, jugos naturales and aguas frescas artesanales, including agua de Jamaica."),
    ("Salsa bar", "Salsas estilo rancho, a salsa bar and free charro beans."),
])]
ELREY = dict(
    phone="(909) 590-0129", addr="4547 Riverside Dr<br>Chino, CA 91710", addr_short=("4547 Riverside Dr", "Chino, CA 91710 · inside the 7-Eleven"),
    maps="https://www.google.com/maps/place/?q=place_id:ChIJi0h5Bukyw4ARPfYBcCSu_ng", find="Inside the 7-Eleven. Look for El Rey.",
    hours=["7:00 AM – 10:00 PM"] * 4 + ["7:00 AM – 11:00 PM", "7:00 AM – 11:00 PM", "7:00 AM – 10:00 PM"],
    ratings=[("4.4", "Google · 2,328 reviews", "https://www.google.com/maps/place/?q=place_id:ChIJi0h5Bukyw4ARPfYBcCSu_ng")],
    quotes=["Hands down the best torta I've ever had!", "Very tasty Mexican food, free beans and a lot of hot sauces", "The tacos are delicious and big"],
    services=ELREY_MENU, svc_nav="Menu", svc_label="The menu", svc_title="The royal lineup.", svc_text="From a chorizo breakfast burrito to weekend barbacoa.",
    about=dict(title="El Reto: two Tortas Cubanas.", text="The challenge on El Rey's flyer: finish two Tortas Cubanas by yourself and you don't pay. “¡Si te comes 2 tortas cubanas tú solo, no pagas!”"),
    rev_title="Tortas con todo.", visit_title="Find the king.", footer="El Rey · Chino, CA",
    alt=("A Mexican torta served with a drink", "Tacos al pastor on a plate"),
)

SITES = {
    "43s-mufflers-brakes": dict(layout="C", svc_mode="two", short="43's Mufflers & Brakes", kicker="Exhaust and brakes · Holt Ave, Pomona", accent="#8F3A29", dark="#15130F", gold="#D9A81E",
        h1=("Loud, leaking or stolen.", "We fit it and weld it."), lede="Exhaust is what the sign says and what most people come in for. Tell us the car and what it's doing, and we'll tell you your options before we touch it.",
        chips=["Mufflers", "Catalytic converters", "Welding", "Brakes", "Tow hitches"],
        phone="(909) 868-1997", addr="1717 W Holt Ave, Ste 1709<br>Pomona, CA 91768", maps=gmaps("43's Mufflers & Brakes 1717 W Holt Ave Pomona CA"), find="In a busy auto plaza. Look for the black and yellow sign.",
        hours=wk("9:30 AM – 5:30 PM", "9:30 AM – 1:30 PM", "Closed"),
        ratings=[("4.5", "Google · 105 reviews", gmaps("43's Mufflers & Brakes 1717 W Holt Ave Pomona CA")), ("4.8", "Yelp · 98 reviews", "https://www.yelp.com/biz/43s-muffler-and-brakes-pomona")],
        services=[("Exhaust", [("Mufflers", "Swapped, replaced or changed for a different sound."), ("Catalytic converters", "Replaced, including after a theft."), ("Exhaust systems", "Pipe run and fitted to the car on the lift."), ("Welding", "Brackets, hangers, tips and broken joints."), ("Tow hitches", "")]),
                  ("Brakes and the rest", [("Brakes", "Drums and rotors."), ("General service", "Suspension, lights and engine work. Ask when you call."), ("Older cars welcome", "Sixties wagons and eighties pickups come through the bay.")])],
        svc_title="What we do.", rev_title="What people come back for.", rev_text="Straight answers, quotes that beat the last shop, fast turnaround on catalytic converters, and clean welds. Several customers brought their own parts and had them fitted.",
        footer="43's Mufflers & Brakes · Pomona, CA", photos=(PX(8986100, 1600), PX(6870299)), alt=("Mechanic inspecting an exhaust system under a lifted car", "Close-up of a brake rotor being inspected")),
    "alejandros-tree-service": dict(layout="E", svc_mode="tiles", short="Alejandros Tree Service", kicker="Tree care · Rialto, California", accent="#1F5A43", dark="#173E31", gold="#B9C96A",
        h1=("Room for a little", "more sky."), lede="For the palms above your roofline and the trees that make a house feel like home. Talk tree care with Alejandros.",
        phone="(909) 694-8945", addr="Based in Rialto, California", maps=gmaps("Alejandros Tree Service Rialto CA"), hours=None,
        ratings=[("4.8", "Google · 188 reviews", gmaps("Alejandros Tree Service Rialto CA"))],
        services=[("", [("Tree trimming", "Talk through overgrowth, branches around your home and the shape of your canopy."), ("Palm care", "Ask about trimming and tell the team about height, condition and access around the property."), ("Tree removal", "If a tree needs to come down, start with its location, nearby structures and access.")])],
        svc_title="A little attention. A different outlook.", svc_text="Three starting points for a conversation.",
        about=dict(title="Let's start with your tree.", text="A simple description is a good beginning.", points=[("Tell us what you see.", "What kind of tree is it, and what would you like to change?"), ("Talk about the space.", "Mention nearby buildings, fences and how the team could reach the tree."), ("Agree on the details.", "Confirm the scope, cleanup, price and timing before any work begins.")]),
        rev_title="The ground below, too.", rev_text="Customers on Google mention palm trimming, tree removal and the cleanup afterward.", visit_title="Tell us what's growing.",
        footer="Alejandros Tree Service · Rialto, CA", photos=(PX(12596112), PX(31127615)), alt=("Arborist climbing a palm tree at dusk", "Arborist cutting a tree trunk with a chainsaw")),
    "bee-z-auto-care": dict(layout="E", svc_mode="accordion", short="Bee Z Auto Care", kicker="Maintenance and repair · Arrow Hwy, Upland", accent="#8A6A00", dark="#17150E", gold="#F0C02E",
        h1=("Brakes feel off?", "Bee Z will check them."), lede="Maintenance and repair for domestic and foreign vehicles on Arrow Highway in Upland. Open from 7:30, six days a week.",
        phone="(909) 982-4321", addr="231 E Arrow Hwy<br>Upland, CA 91786", maps="https://www.google.com/maps/dir/?api=1&destination=231+E+Arrow+Hwy+Upland+CA+91786",
        hours=wk("7:30 AM – 5:00 PM", "7:30 AM – 12:00 PM", "Closed"),
        ratings=[("4.7", "Google · 145 reviews", gmaps("Bee Z Auto Care 231 E Arrow Hwy Upland CA")), ("4.3", "Yelp · 82 reviews", "https://www.yelp.com/biz/bee-z-auto-care-upland-3")],
        services=[("", [("Brakes", "The job reviewers mention most. For a squeal, a soft pedal or a shake when you stop."), ("Oil changes, fluids and filters", "Routine service on the schedule your car calls for."), ("Diagnostics and inspections", "Find out what is wrong first. Ask for a quote before any work starts."), ("Engine and transmission", "Repair work for both, on domestic and foreign vehicles."), ("Battery and electrical", "For a car that will not start or a warning light that will not clear.")])],
        svc_label="What we do", svc_title="Maintenance and repair.", svc_note="Credit cards accepted. Appointments can also be requested through the shop's Yelp page.",
        about=dict(title="Before you call.", text="Have the year, make and model ready, and say what the car is doing."),
        rev_title="Kind staff and no upsell.", visit_title="Arrow Highway, Upland.", footer="Bee Z Auto Care · Upland, CA",
        photos=(PX(6870313, 1800), PX(30470930)), alt=("Mechanic with a tablet checking a car's engine", "Gloved hand on a brake disc")),
    "county-brake-alignment": dict(layout="B", svc_mode="list", short="County Brake, Alignment & Mufflers Plus", kicker="Brakes and alignment · Ramona Ave, Montclair", accent="#9A4A12", dark="#1B1A18", gold="#E2B13C",
        h1=("Pulls to one side?", "We'll set it straight."), lede="Brakes, wheel alignment and mufflers on Ramona Avenue in Montclair. Tell us what the car is doing and we'll put it on the rack.",
        bar=("Shop hours", "8 AM to 5 PM", "Monday to Friday · Saturday till 4"),
        phone="(909) 482-0594", addr="10602 Ramona Ave<br>Montclair, CA 91763", addr_short=("10602 Ramona Ave", "Montclair, CA 91763"), maps="https://www.google.com/maps/dir/?api=1&destination=10602+Ramona+Ave+Montclair+CA+91763",
        hours=wk("8:00 AM – 5:00 PM", "8:00 AM – 4:00 PM", "Closed"),
        ratings=[("4.7", "Google · 101 reviews", gmaps("County Brake Alignment Mufflers Plus 10602 Ramona Ave Montclair CA")), ("4.1", "Yelp · 28 reviews", "https://www.yelp.com/biz/county-brake-and-alignment-plus-mufflers-montclair")],
        services=[("On the rack", [("Wheel alignment", "For a car that pulls, a steering wheel that sits off-centre or tires wearing on one edge."), ("Suspension and ball joints", "Worn parts get found and replaced before the alignment is set."), ("Tire rotation", "")]),
                  ("Brakes and exhaust", [("Brakes", "The job mentioned most in the shop's Google reviews."), ("Mufflers and exhaust", "Replacement mufflers and aftermarket exhaust fitted."), ("Pickup trucks welcome", "Trucks come through the bay as often as cars.")])],
        svc_title="Brakes, alignment and mufflers.", svc_text="It is all in the name. Call with the year, make and model for anything else.",
        rev_title="Rated on Google and Yelp.", rev_text="Reviewers mention brakes, quick alignments, polite staff and a family-run shop.",
        visit_title="Ramona Avenue, Montclair.", footer="County Brake, Alignment & Mufflers Plus · Montclair, CA",
        photos=(PX(6870319, 1800), PX(20408753)), alt=("Mechanic working at the wheel of a car on a lift", "Close-up of a car wheel and brake caliper")),
    "diesel-injection-service": dict(layout="D", svc_mode="tabs", short="Diesel Injection Service", kicker="Diesel fuel systems · Fontana", accent="#1B6B38", dark="#141614", gold="#D2A546",
        h1=("Diesel pumps, injectors and turbos,", "rebuilt and tested in Fontana."), lede="Half the work arrives as a part, the other half drives in. Either way, the fault gets found before anything gets replaced.",
        bar=("Shop hours", "Monday to Friday, 7 to 5", "Closed weekends"),
        phone="(909) 885-0590", addr="8482 Cherry Ave<br>Fontana, CA 92335", addr_short=("8482 Cherry Ave", "Fontana, CA 92335"), maps="https://www.google.com/maps/dir/?api=1&destination=8482+Cherry+Ave+Fontana+CA+92335",
        hours=wk("7:00 AM – 5:00 PM", "Closed", "Closed"),
        ratings=[("4.9", "Google · 83 reviews", gmaps("Diesel Injection Service 8482 Cherry Ave Fontana CA")), ("4.6", "Yelp · 39 reviews", "")],
        services=[("Bring the part", [("Injection pumps", "Diesel fuel injection pumps rebuilt and tested here, from a customer truck, a tractor or a generator set."), ("Injectors", "Rebuilt and tested the same way, in a full set or one at a time."), ("Turbochargers", "Call with the number off the tag if you are matching one up."), ("Parts counter", "A walk-in counter for mechanics, farms and generator owners.")]),
                  ("Bring the truck", [("Engine diagnostics", "Read the fault first, so a part only gets replaced when it is the part at fault."), ("Injector replacement", "Old injectors pulled and new ones fitted with the engine still in the truck."), ("Turbo repair", "For a turbo that is smoking, leaking or not making boost."), ("Basic maintenance", "Oil changes and the routine service a diesel needs between bigger jobs."), ("Fleet service", "Several trucks at once, scheduled around the days they are off the road.")])],
        svc_title="Bring the part or bring the truck.", svc_note="Call first with the part number if you have it. Credit cards accepted.",
        rev_title="Rated by the people who run diesels.", visit_title="Cherry Avenue, Fontana.", footer="Diesel Injection Service · Fontana, CA",
        photos=(PX(7564861, 1800), PX(6720532)), alt=("Mechanic repairing a truck engine", "Mechanic working on the front of a truck")),
    "don-cortez-tires": dict(layout="F", svc_mode="two", short="Don Cortez Tire Shop", kicker="Tire shop · Sierra Ave, Fontana", accent="#1E4A9C", dark="#132B50", gold="#E9B949",
        h1=("Your next stop.", "Your next set."), sub="Llantas nuevas y usadas", lede="New and used tires, custom wheels and everyday tire repairs. Find the blue awnings on Sierra Avenue.",
        chips=["New & used tires", "Wheels & bearings", "Car parts & accessories", "Open Sundays"],
        phone="(909) 251-4965", addr="9530 Sierra Ave, Ste 1<br>Fontana, CA 92335", maps="https://www.google.com/maps/place/?q=place_id:ChIJ00P9IL5Mw4ARfRyY1IHAtiQ", find="White storefront with royal blue awnings.",
        hours=wk("8:00 AM – 6:30 PM", "8:00 AM – 6:30 PM", "8:00 AM – 5:00 PM"),
        ratings=[("4.4", "Google · 362 reviews", "https://www.google.com/maps/place/?q=place_id:ChIJ00P9IL5Mw4ARfRyY1IHAtiQ")],
        quotes=["Great customer service and great prices", "Dude saved me money"],
        services=[("", [("New & used tires", "Tire replacement with new and used options. Ask about your tire size and availability."), ("Flat repair & patching", "Nail-in-tire repairs and tire patches."), ("Balancing & alignment", "Tire balancing and wheel alignment, with an alignment rack on site."), ("Wheels & bearings", "Custom wheels and rims on display, plus wheels and bearings."), ("Valve stems & parts", "Valve stem replacement, car parts and accessories."), ("Trailer tires", "Call the shop with the size you're looking for.")])],
        svc_title="A lot more than a new set.", svc_note="For current availability and pricing, call the shop.", rev_title="Great service. Great prices.",
        footer="Don Cortez Tire Shop · Fontana, CA", photos=(PX(6870311, 1600), U("1578844251758-2f71da64c96f", 1400, 600)), alt=("Mechanic inspecting a tire in a workshop", "Stacks of tires in a tire shop")),
    "el-rey": dict(ELREY, layout="B", svc_mode="tabs", band=True, short="El Rey de las Tortas", kicker="Taqueria · Chino, California", accent="#B3261E", dark="#0E2A6B", gold="#F0C24B",
        h1=("El Rey de las Tortas.", "¡El sabor que manda!"), lede="Big tortas. Al pastor tacos. A salsa bar worth making room for. Pull up to El Rey on Riverside Drive.",
        bar=("Open daily", "From 7 AM", "Until 10 PM · 11 PM Friday and Saturday"), photos=(PX(30179627, 1800), PX(14006131))),
    "el-rey-retro-roadside": dict(ELREY, layout="D", svc_mode="tiles", short="El Rey de las Tortas", kicker="Chino, CA · inside the 7-Eleven", accent="#A8301F", dark="#123D2B", gold="#E0B44C",
        h1=("Worth", "the stop."), lede="Big tortas. Al pastor tacos. A salsa bar worth making room for. Find El Rey on Riverside Drive.",
        svc_title="Pull up hungry.", photos=(PX(35020122), PX(28992999)), alt=("A Mexican torta on a plate", "Al pastor meat roasting on a spit")),
    "hocks-japanese-car-specialists": dict(layout="C", svc_mode="list", short="Hock's Japanese Car Specialists", kicker="Japanese car repair · Rio Rancho Rd, Pomona", accent="#34407A", dark="#15171F", gold="#D8B24A",
        h1=("Japanese cars,", "looked after in Pomona."), lede="A family owned and operated shop for Japanese makes, from oil changes to engine work. Open Tuesday to Saturday in the Rio Rancho Towne Center.",
        chips=["Brakes", "Engine repair", "Fluids and filters", "A/C and heating", "Battery and electrical"],
        phone="(909) 620-9761", addr="45 Rio Rancho Rd, Ste 2B<br>Pomona, CA 91766", maps="https://www.google.com/maps/dir/?api=1&destination=45+Rio+Rancho+Rd+Ste+2B+Pomona+CA+91766", find="Inside the Rio Rancho Towne Center. Closed Sunday and Monday.",
        hours=["Closed", "8:00 AM – 5:00 PM", "8:00 AM – 5:00 PM", "8:00 AM – 5:00 PM", "8:00 AM – 5:00 PM", "8:00 AM – 4:00 PM", "Closed"],
        ratings=[("4.7", "Google · 64 reviews", gmaps("Hock's Japanese Car Specialists 45 Rio Rancho Rd Pomona CA")), ("4.6", "Yelp · 106 reviews", "https://www.yelp.com/biz/hocks-japanese-car-specialists-pomona")],
        services=[("", [("Oil changes and fluids", "Oil, transmission fluid, filters and the scheduled maintenance in between."), ("Brakes", "For a soft pedal, a squeal or a shake when you stop."), ("Engine repair", "From a check-engine light to an engine replacement."), ("Air conditioning and heating", "For air that will not blow cold or a heater that will not warm up."), ("Battery and electrical", "For a car that will not start or a warning light that will not clear."), ("Hybrids", "Prius owners show up in the reviews. Ask when you call.")])],
        svc_title="What we work on.", svc_note="Credit cards accepted. Appointments can also be requested through the shop's Yelp page.",
        rev_title="Honest, and good at keeping you posted.", rev_text="Honesty is the word reviewers use most, along with clear communication. One says the family has brought cars here for more than twenty years.",
        footer="Hock's Japanese Car Specialists · Pomona, CA",
        photos=(PX(8478259, 1600), PX(8478228)), alt=("Mechanic leaning into the engine bay of a car", "Open engine bay with the battery in view")),
    "jc-auto-electric": dict(layout="F", svc_mode="accordion", short="J C Auto Electric", kicker="Auto electrical · Montclair", accent="#B3261E", dark="#16181B", gold="#D9A53A",
        h1=("What's it doing?", "We'll tell you what we check."), lede="Starting, charging, wiring, gauges and air conditioning. The fault gets tested before anything gets replaced.",
        phone="(909) 625-9181", addr="10640 Ramona Ave<br>Montclair, CA 91763", maps="https://www.google.com/maps/dir/?api=1&destination=J+C+Auto+Electric+10640+Ramona+Ave+Montclair+CA+91763",
        hours=wk("8:00 AM – 5:30 PM", "8:00 AM – 4:00 PM", "Closed"),
        ratings=[("4.7", "Google · 83 reviews", gmaps("J C Auto Electric 10640 Ramona Ave Montclair CA")), ("4.2", "Yelp · 12 reviews", "https://www.yelp.com/biz/jc-auto-electric-montclair")],
        services=[("", [("Won't start", "We test the battery, the starter, the ignition switch and the wiring between them."), ("Battery light on", "Usually the alternator or its wiring. We measure charging voltage with the engine running."), ("Dead battery every morning", "Something is drawing power with the key off. We measure the draw and pull circuits one at a time."), ("Gauge reads wrong", "We check the sender, the wiring and the cluster."), ("Windows or locks stuck", "Switches, motors and the wiring where the door meets the body."), ("Lights out or flickering", "We check bulbs, grounds, relays and switches."), ("A/C or blower dead", "Blower motor, resistor, relay and controls."), ("Check-engine light", "We read the code, then test the sensor and its circuit.")])],
        svc_label="Symptoms", svc_title="Pick the closest one.", svc_note="A real diagnosis needs the car in the shop. No wheel alignments.",
        about=dict(title="Not only electrical.", text="The shop handles general repair too. Ask when you call.", points=[("Starting and charging", ""), ("Wiring repair", ""), ("Fuel pumps and gauges", ""), ("Air conditioning", "")]),
        rev_title="Rated on Google and Yelp.", visit_title="Ramona Avenue, Montclair.", footer="J C Auto Electric · Montclair, CA",
        photos=(PX(8985448), PX(10490631)), alt=("Mechanic holding a diagnostic tablet", "Diagnostic equipment connected inside a car")),
    "jc-bumper-repair": dict(layout="E", svc_mode="two", short="JC Bumper Repair & Auto Body", kicker="Bumper and body work · Fontana", accent="#1E4A9C", dark="#14171C", gold="#D9C27A",
        h1=("Cracked bumper?", "Call for a look at yours."), lede="Bumper repair and body work in Fontana. Have your year, make and model handy, and tell us which bumper and what happened to it. A photo helps when you come by.",
        chips=["Bumper repair", "Collision repair", "Dent removal", "Chrome delete"],
        phone="(909) 349-0343", addr="16620 Ceres Ave, Suite 6<br>Fontana, CA 92335", maps="https://www.google.com/maps/dir/?api=1&destination=16620+Ceres+Ave+Ste+6+Fontana+CA+92335",
        hours=wk("9:00 AM – 5:00 PM", "10:30 AM – 2:00 PM", "Closed"),
        ratings=[("4.9", "Yelp · 32 reviews", ""), ("4.7", "Google · 98 reviews", gmaps("JC Bumper Repair 16620 Ceres Ave Fontana CA"))],
        services=[("", [("Bumper repair", "Cracks, splits, scrapes and torn mounting tabs, repaired and refinished."), ("Bumper replacement", "When a cover is bent or torn past repair, we fit a replacement."), ("Collision repair", "Body panels and structure damaged in a hit, straightened and repainted."), ("Dent removal", "Door, fender and quarter-panel dents worked back to shape."), ("Chrome delete", "Grille, trim and window surrounds refinished in the finish you pick."), ("Auto body restoration", "Older paint and bodywork brought back, panel by panel.")])],
        svc_label="What we fix", svc_title="Repaired, refinished, back on the car.", rev_title="Rated on Yelp and Google.",
        footer="JC Bumper Repair & Auto Body · Fontana, CA", photos=(PX(8470881, 1600), PX(6870314)), alt=("Painter working on a car in a body shop", "Spray gun painting a car part")),
    "j-s-auto-center-smog": dict(layout="F", svc_mode="tiles", short="J & S Auto Center & Smog", kicker="Smog check and repair · Sierra Ave, Fontana", accent="#5C6B1E", dark="#1A1D14", gold="#E0B84A",
        h1=("Smog check due?", "Get it done on Sierra Ave."), lede="Smog checks, oil changes and repairs on Sierra Avenue in Fontana. Open Monday to Saturday, 8 to 5.",
        chips=["Smog check", "Oil changes", "Check engine light", "Brakes", "Open Saturdays"],
        phone="(909) 822-3055", addr="8807 Sierra Ave<br>Fontana, CA 92335", maps="https://www.google.com/maps/dir/?api=1&destination=8807+Sierra+Ave+Fontana+CA+92335", find="Same lot as the J & S service station.",
        hours=wk("8:00 AM – 5:00 PM", "8:00 AM – 5:00 PM", "Closed"),
        ratings=[("4.9", "Google · 85 reviews", gmaps("J & S Auto Center & SMOG 8807 Sierra Ave Fontana CA")), ("4.4", "Yelp · 25 reviews", "https://www.yelp.com/biz/j-and-s-auto-center-fontana-2")],
        services=[("", [("Smog check", "Bring the DMV renewal notice if you have it."), ("Oil changes", "The fluids get checked on every visit."), ("Check engine light", "The code gets read before anything is replaced."), ("Brakes", ""), ("Steering and suspension", ""), ("Engine and electrical", "")])],
        svc_title="Smog, service and repairs.", svc_note="Credit cards accepted.",
        about=dict(title="Thirty years on the job.", text="The owner's Yelp profile says the shop has been in business for 30 years and checks the fluids every time a car comes in."),
        rev_title="4.9 on Google.", rev_text="Reviewers mention honest mechanics, smog checks, oil changes and fair prices.",
        visit_title="Sierra Avenue, Fontana.", footer="J & S Auto Center & Smog · Fontana, CA",
        photos=(PX(33814734, 1600), PX(37177070)), alt=("Cars on lifts in a repair shop", "Car battery under an open hood")),
    "king-tire-shop": dict(layout="B", svc_mode="chips", band=True, short="King Tire Shop", kicker="Tire shop · Rose Ave, Montclair", accent="#B3261E", dark="#1C2444", gold="#E9B949",
        h1=("Flat at 8 PM?", "We're open till nine."), lede="Tires, flats, brakes and oil changes on Rose Ave in Montclair. If it's getting close to nine, call first so we know you're coming.",
        bar=("Open late", "9 AM to 9 PM", "Monday to Saturday · closed Sunday"),
        phone="(909) 952-9219", addr="8939 Rose Ave<br>Montclair, CA 91763", addr_short=("8939 Rose Ave", "Montclair, CA 91763"), maps="https://www.google.com/maps/dir/?api=1&destination=King+Tire+Shop+8939+Rose+Ave+Montclair+CA+91763",
        hours=wk("9:00 AM – 9:00 PM", "9:00 AM – 9:00 PM", "Closed"),
        ratings=[("4.5", "Google · 135 reviews", gmaps("King Tire Shop 8939 Rose Ave Montclair CA")), ("4.3", "Yelp · 59 reviews", "https://www.yelp.com/biz/king-tire-shop-montclair")],
        services=[("Tires", [("Flat tire repair and patches", ""), ("New tires", ""), ("Used tires", ""), ("Mounting and balancing", ""), ("Tire rotation", ""), ("Tire pressure sensor (TPMS) repair", "")]), ("And more", [("Alignment", ""), ("Brakes", ""), ("Oil changes", "")])],
        svc_title="Twelve hours a day.", svc_text="Most tire shops close at 6 PM. King stays open until 9.", svc_note="Cards accepted.",
        rev_title="Rated on Google and Yelp.", visit_title="Rose Avenue, Montclair.", footer="King Tire Shop · Montclair, CA",
        photos=(PX(8985660, 1800), PX(31097241)), alt=("Mechanic rolling a tire beside a car on a lift", "Mechanic working on a wheel in a workshop")),
    "lockworx": dict(layout="D", svc_mode="tabs", short="Lockworx Locksmith Services", kicker="Locksmith · Fontana, CA · open 24/7", accent="#2C6E91", dark="#262A2B", gold="#E6D53A",
        h1=("Small key.", "Big difference."), lede="Home. Vehicle. Commercial. From a spare key to a remote that needs repair, let's get your keys working for you.",
        bar=("Always open", "24 hours, every day", "Women-owned · LGBTQ+ friendly"),
        phone="(909) 823-8510", addr="9035 Sierra Ave<br>Fontana, CA 92335", addr_short=("9035 Sierra Ave", "Fontana, CA 92335"), maps="https://www.google.com/maps/place/?q=place_id:ChIJDbCEWZJMw4ARnfN9USwFfDY", find="Charcoal brick, black awnings and the yellow key in the window.",
        hours=["Open 24 hours"] * 7,
        ratings=[("4.5", "Google · 496 reviews", "https://www.google.com/maps/place/?q=place_id:ChIJDbCEWZJMw4ARnfN9USwFfDY")],
        quotes=["Fair prices, friendly staff, and honest work.", "Kind professional mechanics solved my problem at a great price.", "very polite and professional"],
        services=[("Home", [("Key copying & duplication", "A spare for the house. A key for someone you trust."), ("Lock supplies", "")]), ("Vehicle", [("Key & remote programming", "Extra car keys, replacement keys and remotes that work together."), ("Key fob & car door lock repair", ""), ("Immobilizer / anti-theft key issues", "")]), ("Commercial", [("Key duplication", "Keys and lock supplies for your place of business."), ("Lock supplier", "")])],
        svc_title="Three ways we work.", svc_text="A neighborhood key shop with help for your home, your vehicle and your business.", svc_note="Key copies from $1.50, per the storefront sign. Call to ask about your specific key.",
        about=dict(title="Save your flip key.", text="Before buying a dealer key, ask about repair. Lockworx specializes in saving flip-type keys, with repair that can cost less than a dealer replacement. Online booking is offered through the Google listing."),
        rev_title="Good work. Good words.", visit_title="Look for the big letters.", footer="Lockworx Locksmith Services · Fontana, CA",
        photos=(PX(18101862, 1800), PX(6565048)), alt=("Rows of keys hanging on hooks", "Hand holding a car key fob")),
    "mailos-auto-repair": dict(layout="A", svc_mode="two", short="Mailo's Auto Repair", kicker="Auto repair · Ceres Ave, Fontana", accent="#1F4E5F", dark="#14191C", gold="#E0B34A",
        h1=("Check engine light on?", "Mailo's will take a look."), lede="Repairs and maintenance for cars and trucks on Ceres Avenue in Fontana. Open Monday to Saturday.",
        phone="(909) 427-9202", addr="16624 Ceres Ave<br>Fontana, CA 92335", maps="https://www.google.com/maps/dir/?api=1&destination=16624+Ceres+Ave+Fontana+CA+92335", find="Hours are from the Google listing. Yelp shows longer hours, so call if you are coming early or late.",
        hours=wk("8:00 AM – 6:00 PM", "8:00 AM – 6:00 PM", "Closed"),
        ratings=[("4.4", "Google · 153 reviews", gmaps("Mailo's Auto Repair 16624 Ceres Ave Fontana CA")), ("4.0", "Yelp · 34 reviews", "https://www.yelp.com/biz/mailos-auto-repair-fontana")],
        services=[("", [("Check engine light", "The code gets read and explained before any work starts."), ("Tune-ups and spark plugs", "Spark plug replacement comes up in the shop's reviews."), ("Oil changes and maintenance", "Routine service to keep the car out of the shop."), ("Cooling system", "Radiators, belts and hoses for a car that is running hot."), ("Trucks", "Pickup owners make up a good share of the reviews."), ("Stuck on the road?", "Call the shop and ask about a tow.")])],
        svc_title="What comes through the bay.", svc_note="Credit cards accepted.",
        rev_title="An honest mechanic, by most accounts.", rev_text="Honest, trustworthy and affordable are the words that come up most in the shop's Google reviews.",
        visit_title="Ceres Avenue, Fontana.", footer="Mailo's Auto Repair · Fontana, CA",
        photos=(PX(3807517, 1600), PX(4116221)), alt=("Mechanic inspecting the engine of a car", "Hands working on hoses in an engine bay")),
    "muffler-doctor": dict(layout="A", svc_mode="tiles", short="Muffler Doctor", kicker="Custom exhaust · Holt Blvd, Montclair", accent="#7A5C00", dark="#0B0D0E", gold="#E0B400",
        h1=("Exhaust work.", "Fitted to your car."), lede="Exhaust work in Montclair, inside the J & J Auto Services Center. Tell the shop what you drive, what you're hearing, and what you'd like to change.",
        phone="(909) 445-0024", addr="5436 Holt Blvd #A5<br>Montclair, CA 91763", maps="https://www.google.com/maps/place/?q=place_id:ChIJWaHSVsozw4ARm_j6ZTLx6Lc", find="A bay inside the J & J Auto Services Center, not a standalone storefront.",
        hours=wk("8:00 AM – 5:00 PM", "Closed", "Closed"),
        ratings=[("4.8", "Google · 165 reviews", "https://www.google.com/maps/place/?q=place_id:ChIJWaHSVsozw4ARm_j6ZTLx6Lc")],
        services=[("", [("Custom exhaust", "Built around the vehicle, the space under it and what you use the car for."), ("Muffler installation", "Pipe and muffler fitted to the car, not chosen from a one-size list."), ("Welds", "Joints welded and checked.")])],
        svc_label="The work", svc_title="Built around your vehicle.", svc_text="A note over the phone is not a quote. The car goes up, the route gets measured, and the options get explained.",
        about=dict(title="The whole route. Not just the box.", text="A muffler is one part of a system. Flanges, pipe diameter, bends, hangers and clearance all affect fit.", points=[("Look first.", "The vehicle goes up and the existing route, clearances, flanges and hangers are inspected."), ("Measure twice.", "Bends and hangers have to work in the space that is there."), ("Close the joint.", "Joints are welded and checked.")]),
        rev_title="Welds and custom work, reviewed.", visit_title="Find the bay.", footer="Muffler Doctor · Montclair, CA",
        photos=(PX(10827691), PX(32662276)), alt=("Twin exhaust tips on the rear of a car", "Close-up of a polished exhaust system")),
    "performance-lube-oil": dict(layout="C", svc_mode="chips", short="Performance Lube & Oil", kicker="Oil change and car wash · Riverside Dr, Chino", accent="#0E6F8F", dark="#0D2730", gold="#E8A200",
        h1=("Oil change.", "Free car wash."), lede="Open every day, 8 AM to 5 PM. A free complete car wash comes with every service. Ask about rainy days.",
        chips=["Oil changes", "Car wash", "Brakes", "Tune-ups", "Detailing"],
        phone="(909) 364-1197", addr="5288 Riverside Dr<br>Chino, CA 91710", maps="https://www.google.com/maps/dir/?api=1&destination=Performance+Lube+%26+Oil+5288+Riverside+Dr+Chino+CA+91710", find="Behind the Chevron.",
        hours=["8:00 AM – 5:00 PM"] * 7,
        ratings=[("4.3", "Google · 87 reviews", gmaps("Performance Lube & Oil 5288 Riverside Dr Chino CA")), ("4.2", "Yelp · 129 reviews", "https://www.yelp.com/biz/performance-lube-and-oil-chino-2")],
        services=[("Under the hood", [("Oil changes", ""), ("Transmission fluid", ""), ("Coolant flushes", ""), ("Tune-ups", ""), ("Brakes", ""), ("Belts", "")]), ("Outside", [("Car wash", ""), ("Hand wash", ""), ("Detailing", "")])],
        svc_title="One stop, two jobs.", svc_note="Not sure what it's due for? Bring the owner's manual or call with the mileage. Cards accepted.", rev_title="Rated on Google and Yelp.",
        footer="Performance Lube & Oil · Chino, CA", photos=(PX(13065690, 1600), PX(4876645)), alt=("Fresh engine oil being poured into an engine", "Person washing a car")),
    "quality-auto-complete-auto-repair": dict(layout="D", svc_mode="tabs", short="Quality Auto Complete Auto Repair", kicker="Complete auto repair · Rancho Cucamonga", accent="#7B1F3A", dark="#1A1216", gold="#E3B656",
        h1=("Failed smog?", "We find out why and fix it."), lede="Complete auto repair in Rancho Cucamonga, from smog problems and brakes to clutches and transmissions.",
        phone="(909) 466-1919", addr="8160 Masi Dr, Unit B<br>Rancho Cucamonga, CA 91730", maps="https://www.google.com/maps/dir/?api=1&destination=8160+Masi+Dr+B+Rancho+Cucamonga+CA+91730",
        hours=wk("8:00 AM – 5:00 PM", "8:00 AM – 2:00 PM", "Closed"),
        ratings=[("4.4", "Google · 142 reviews", gmaps("Quality Auto Complete Auto Repair 8160 Masi Dr Rancho Cucamonga CA")), ("4.1", "Yelp · 151 reviews", "https://www.yelp.com/biz/quality-auto-complete-auto-repair-rancho-cucamonga-2")],
        services=[("Engine and smog", [("Smog problems", "The topic that comes up most in the shop's Google reviews."), ("Engine repair", ""), ("Diesel service", ""), ("Exhaust systems", "")]),
                  ("Drivetrain", [("Clutch service", ""), ("Manual and automatic transmissions", ""), ("Driveshafts and axles", "")]),
                  ("Brakes and alignment", [("Brake repairs", ""), ("Alignments", "")])],
        svc_title="Complete means complete.", svc_note="Service list from the shop's own Yelp description. Credit cards accepted.",
        rev_title="Rated on Google and Yelp.", visit_title="Masi Drive, Rancho Cucamonga.", footer="Quality Auto Complete Auto Repair · Rancho Cucamonga, CA",
        photos=(PX(5276374, 1800), PX(8985712)), alt=("Mechanic working under a car on a lift", "Mechanic beside an engine on a stand")),
    "sinaloa-tires": dict(layout="F", svc_mode="chips", short="Sinaloa Tires", kicker="Used tires · Llantas usadas · Pomona", accent="#B8430B", dark="#22252A", gold="#E9B949",
        h1=("Used and new tires,", "seven days a week."), sub="Llantas usadas y nuevas, los siete días.", lede="Free air and a free check-engine scan. Aire gratis. Escaneo de check engine gratis.",
        phone="(909) 620-1199", addr="1542 S Garey Ave<br>Pomona, CA 91766", maps=gmaps("Sinaloa Tires 1542 S Garey Ave Pomona CA"), find="We're in the back. Estamos al fondo. Look for the orange flag at Garey Ave, then follow the driveway to the building.",
        hours=wk("8:00 AM – 7:00 PM", "8:00 AM – 6:00 PM", "8:00 AM – 3:00 PM"),
        ratings=[("4.3", "Google · 161 reviews", gmaps("Sinaloa Tires 1542 S Garey Ave Pomona CA"))],
        services=[("Tires", [("Used tires", ""), ("New tires", ""), ("Flat repair", ""), ("Mounting and balancing", ""), ("Rotation", ""), ("Tire sensor repair", "")]), ("And the rest", [("Brakes", ""), ("Oil changes", ""), ("Check-engine diagnosis", ""), ("General repair up to engine work", "")])],
        svc_title="Tires first. The rest, too.", svc_note="Bring cash or Zelle. Ask about cards when you call.",
        rev_title="Fair prices and fast service.", rev_text="Reviewers most often mention flat tire repair, used tires, brakes, fair prices and fast service.", visit_title="Garey Avenue, Pomona.", footer="Sinaloa Tires · Pomona, CA",
        photos=(PX(31097241), PX(6870311)), alt=("Mechanic working on a wheel in a workshop", "Mechanic inspecting a tire")),
    "tepa-tire": dict(layout="A", svc_mode="list", short="Tepa Tire & Auto Care", kicker="Tires and brakes · S Mountain Ave, Ontario", accent="#173A8F", dark="#0F275F", gold="#E08A4A",
        h1=("Tires and brakes,", "handled."), lede="New and used tires, flat repair, mounting and balancing, and brake work on South Mountain Avenue. Call to discuss your vehicle.",
        chips=["New & used tires", "Flat repair & patching", "Mount & balance", "Brakes", "Open 7 days"],
        phone="(909) 458-9200", addr="705 S Mountain Ave<br>Ontario, CA 91762", maps="https://www.google.com/maps/search/Tepa+tire+%26+auto+care+705+S+Mountain+Ave+Ontario+CA", find="Look for the blue-and-white sign, the stacked tires and the red and blue canopies.",
        hours=["8:00 AM – 6:00 PM"] * 7,
        ratings=[("4.6", "Google · 205 reviews", "https://www.google.com/maps/search/Tepa+tire+%26+auto+care+705+S+Mountain+Ave+Ontario+CA")],
        services=[("", [("New & used tires", "Call with your tire size for today's options."), ("Flat repair & patching", "Bring the wheel or the vehicle. The tire comes off and gets checked before anyone says whether it is repairable."), ("Mount & balance", "Tires fitted to wheels and balanced."), ("Brakes", "Grinding, squealing or a soft pedal? Describe it when you call.")])],
        svc_title="The kind of shop that writes it down.", svc_text="Tires are stacked where you can see them, and the work is explained before it starts.", rev_title="Your neighborhood tire counter.", rev_text="Review topics include new and used tires, patching and brakes.",
        footer="Tepa Tire & Auto Care · Ontario, CA", photos=(U("1578844251758-2f71da64c96f", 1600, 700), PX(6870299)), alt=("Stacks of tires in a tire shop", "Close-up of a brake rotor being inspected")),
    "toy-shop-transmissions": dict(layout="E", svc_mode="accordion", short="Toy Shop Transmissions", kicker="Transmissions and differentials · Pomona", accent="#1A6B6A", dark="#1D1A17", gold="#D9B45A",
        h1=("Back in drive.", "Rebuilt in Pomona."), lede="Transmissions and differentials for hot rods, customs and the car you drive to work.",
        bar=("Shop hours", "Monday to Friday, 9 to 6", "Closed weekends"),
        phone="(909) 620-5849", addr="1292 E 3rd St<br>Pomona, CA 91766", addr_short=("1292 E 3rd St", "Pomona, CA 91766"), maps="https://www.google.com/maps/dir/?api=1&destination=1292+E+3rd+St+Pomona+CA+91766",
        hours=wk("9:00 AM – 6:00 PM", "Closed", "Closed"),
        ratings=[("4.9", "Google · 67 reviews", gmaps("Toy Shop Transmissions 1292 E 3rd St Pomona CA")), ("4.9", "Yelp · 36 reviews", "")],
        services=[("", [("Automatic transmission rebuilds", "From a car that slips in second to one that will not move at all."), ("Transmission leak inspection", "We find where the red fluid is coming from and tell you what it takes to stop it."), ("Rear differential rebuilds", "A rear end that howls, whines or leaves a puddle on the floor gets rebuilt here."), ("Older vehicles and hard-to-find parts", "Old trucks and cars with parts nobody stocks are worth asking about."), ("Hot rods, customs and daily drivers", "The car you take to shows and the car you drive to work both come in.")])],
        svc_label="What comes in", svc_title="Slipping, leaking or stuck.", svc_note="Credit cards accepted.",
        about=dict(title="Before you call.", text="Have the year, make and model ready. Describe what it does and say whether it still drives. If it does not drive, call before you arrange the tow."),
        rev_title="4.9 on Google and Yelp.", visit_title="East 3rd Street, Pomona.", footer="Toy Shop Transmissions · Pomona, CA",
        photos=(PX(29181492, 1800), PX(15489247)), alt=("Mechanic repairing a transmission", "Car on a lift in a repair bay")),
    "with-pride-auto-air": dict(layout="A", svc_mode="two", short="With Pride Auto Air", kicker="Car air conditioning · Holt Blvd, Montclair", accent="#B3261E", dark="#0B4F7A", gold="#E0A21A",
        h1=("Your A/C should be cold.", "We find the fault first."), lede="Car air conditioning, diagnosed and repaired in Montclair by a family shop that has been at it for more than 40 years.",
        phone="(909) 391-4894", addr="5438 Holt Blvd, Unit F3<br>Montclair, CA 91763", maps=gmaps("With Pride Auto Air Conditioning 5438 Holt Blvd Montclair"), find="In the red building at 5438 Holt Blvd.",
        hours=wk("8:00 AM – 5:00 PM", "9:00 AM – 3:00 PM", "Closed"),
        ratings=[("4.7", "Google · 97 reviews", gmaps("With Pride Auto Air Conditioning 5438 Holt Blvd Montclair"))],
        services=[("Air conditioning", [("Diagnosis", "Warm air has a cause. We look for it before anything gets replaced."), ("Leak repair", "Find where the system is losing refrigerant and seal it."), ("Compressor repair", "The part that does the work, and the one customers bring to us most."), ("Recharge", "Done after the system holds, not instead of fixing it.")]),
                  ("Also on the lift", [("Radiators and cooling fans", "Engine cooling, not only cabin cooling."), ("Gauges", "Installed and wired, including on older cars."), ("Classic cars", "Classics come here for A/C."), ("Routine maintenance", "Ask when you call.")])],
        svc_label="What we fix", svc_title="Find the fault first. Then fix it.", svc_note="Every car is different, so we don't post prices. Call, tell us what it's doing, and we'll tell you what we'd check.",
        about=dict(title="Eddie and Elaine run it.", text="With Pride is a family business. Eddie is in the bays and Elaine keeps you posted from the office, so you talk to the people doing the work."),
        rev_title="Fair pricing. No upselling.", rev_text="Reviewers mostly talk about fair pricing, no upselling, leak repairs and compressors.", visit_title="Bring it in.", footer="With Pride Auto Air Conditioning · Montclair, CA",
        photos=(PX(6074540), PX(10490621)), alt=("Car climate control dials", "Gloved hand working in an engine bay")),
}

TITLES = {k: f"{v['short']} | {v['kicker'].split(' · ')[-1]}" for k, v in SITES.items()}

# Not built here: Muffler Doctor declined (site removed 2026-11-10); the rest are built by build_flagship.py
SKIP = None  # every lead page is now built by build_flagship.py; this file keeps the facts (SITES)

if __name__ == "__main__":
    OUT = pathlib.Path(sys.argv[1])
    for folder, s in SITES.items():
        if True:  # see SKIP note above
            continue
        css, body = LAYOUTS[s["layout"]](s)
        (OUT / folder).mkdir(parents=True, exist_ok=True)
        (OUT / folder / "index.html").write_text(page(TITLES[folder], f"{s['short']}. {s['lede']} Concept site.".replace('"', "'"), css, body))
        print("built", folder, s["layout"])
