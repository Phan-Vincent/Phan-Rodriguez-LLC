#!/usr/bin/env python3
"""Build the call list and per-lead outreach kits from leads/leads.json.

    python3 tools/leads/outreach.py            (sync.py also runs this at the end)

Reads   leads/leads.json
Writes  leads/outreach/index.html   one phone-friendly page: follow-ups due, new calls ranked best first,
                                    and for each lead an opener, talking points, the mockup link and QR code,
                                    and ready-to-send follow-up text and email. Call outcomes are logged in the
                                    page (saved in that browser) and copied out as lines for the Google Sheet.
Standard library only. Call statuses come from columns J and K of the workbook, so copy them in from the
Google Sheet before regenerating if you want today's follow-ups to be right.
"""
import datetime
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE = "https://phan-vincent.github.io/Phan-Rodriguez-LLC/mockups/{}/"
CALLER = "Vincent"
STUDIO = "Phan Rodriguez"
PRIORITY = {"High": 0, "Medium": 1, "Low": 2}
VERDICT = {"Build first": 0, "Build": 1, "Build, Google only": 2}  # anything else (or no research) ranks after these
DATE = re.compile(r"\b(\d{1,2})/(\d{1,2})\b")


def parse_status(status, today, notes=None):
    """Return (kind, due date or None). kind is 'new', 'followup', 'waiting' or 'declined'.
    The sheet's two columns are used loosely (a status sometimes lands in Notes), so dates are read from both."""
    st = (status or "").strip().lower()
    if not st:
        return "new", None
    s = (st + " " + (notes or "").strip().lower()).strip()
    if "not interested" in s or "do not call" in s:
        return "declined", None
    dates = []
    for m, d in DATE.findall(s):
        try:
            dates.append(datetime.date(today.year, int(m), int(d)))
        except ValueError:
            pass
    # a date "in the future" by more than ~2 months is really last year (list started Nov 2026)
    dates = [d.replace(year=d.year - 1) if (d - today).days > 60 else d for d in dates]
    later = re.search(r"in (\d+) (day|week)s?", s)
    if later and dates:
        n = int(later.group(1)) * (7 if later.group(2) == "week" else 1)
        return "followup", max(dates) + datetime.timedelta(days=n)
    if "call us back" in s or "will call" in s:
        return "waiting", (max(dates) + datetime.timedelta(days=7)) if dates else None
    if dates:
        due = max(dates)
        if re.fullmatch(r"(called|msg left|left (a )?msg|no answer)\s+\d{1,2}/\d{1,2}", st):
            due += datetime.timedelta(days=2)  # nothing scheduled: try again two days later
        return "followup", due
    return "followup", today


def lead_card(l, today):
    res = l.get("research") or {}
    g, y = res.get("google") or {}, res.get("yelp") or {}
    rating = g.get("rating") or l.get("sheet_rating")
    reviews = g.get("reviews") or l.get("sheet_reviews")
    kind, due = parse_status((l.get("call") or {}).get("status"), today, (l.get("call") or {}).get("notes"))
    topics = sorted((g.get("topics") or {}).items(), key=lambda kv: -kv[1])[:4]
    name = res.get("name") or l["name"]
    return {
        "row": l["row"], "name": name, "category": l.get("category"), "city": res.get("city") or l.get("area"),
        "address": (g.get("address") or l.get("address")), "phone": l.get("phone"), "maps": l.get("maps"),
        "priority": l.get("priority"), "verdict": res.get("verdict"), "rating": rating, "reviews": reviews,
        "yelp": {"rating": y.get("rating"), "reviews": y.get("reviews"), "claimed": y.get("claimed")} if y else None,
        "angle": res.get("angle"), "topics": [t for t, _ in topics], "flags": res.get("flags") or [],
        "services": (y.get("services") or [])[:5],
        "hours": g.get("hours") or y.get("hours") or None,
        "url": SITE.format(l["mockup"]["folder"]),
        "status": (l.get("call") or {}).get("status"), "notes": (l.get("call") or {}).get("notes"),
        "kind": kind, "due": due.isoformat() if due else None,
        "rank": [PRIORITY.get(l.get("priority"), 3), VERDICT.get(res.get("verdict"), 3 if res else 4),
                 -(reviews or 0), -(rating or 0), l["row"]],
    }


def main():
    data = json.loads((ROOT / "leads" / "leads.json").read_text())
    today = datetime.date.today()
    leads = data["leads"]
    with_site = [l for l in leads if (l.get("mockup") or {}).get("exists")]
    cards = [lead_card(l, today) for l in with_site]
    declined = [c for c in cards if c["kind"] == "declined"]
    cards = [c for c in cards if c["kind"] != "declined"]
    cards.sort(key=lambda c: c["rank"])
    # newest date written in any call status: how fresh the copy of the Google Sheet's Status column is
    logged = [datetime.date(today.year, int(m), int(d)) for c in cards + declined
              for m, d in DATE.findall(f"{c['status'] or ''} {c['notes'] or ''}") if 1 <= int(m) <= 12 and 1 <= int(d) <= 31]
    logged = [d for d in logged if d <= today]
    last_call = max(logged).isoformat() if logged else None
    meta = {"generated": today.isoformat(), "last_call": last_call,
            "caller": CALLER, "studio": STUDIO, "no_site": len(leads) - len(with_site), "declined": len(declined)}
    page = TEMPLATE.replace("__DATA__", json.dumps({"meta": meta, "leads": cards}, ensure_ascii=False).replace("</", "<\\/"))
    page = page.replace("__GENERATED__", html.escape(today.isoformat()))
    out = ROOT / "leads" / "outreach"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(page)
    due = sum(1 for c in cards if c["kind"] != "new" and (not c["due"] or c["due"] <= today.isoformat()))
    print(f"outreach: {sum(c['kind'] == 'new' for c in cards)} new calls, {due} follow-ups due, "
          f"{len(declined)} declined skipped -> leads/outreach/index.html")
    return 0


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Call List</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>
<style>
:root{--bg:#f6f5f2;--card:#fff;--ink:#1b1b1a;--muted:#6b6a66;--line:#e4e2dc;--accent:#1f5f4a;--accent-ink:#fff;
--due:#a3471b;--due-bg:#fbeee6;--open:#1f6e3a;--open-bg:#e5f3e8;--shut:#7a7a76;--chip:#efede8}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141413;--card:#1e1e1c;--ink:#ecebe7;--muted:#a09f99;
--line:#33322f;--accent:#5fb894;--accent-ink:#0d1f18;--due:#f0a57c;--due-bg:#3a2418;--open:#7fd39a;--open-bg:#1b3323;--shut:#8a8984;--chip:#2a2927}}
:root[data-theme="dark"]{--bg:#141413;--card:#1e1e1c;--ink:#ecebe7;--muted:#a09f99;--line:#33322f;--accent:#5fb894;--accent-ink:#0d1f18;
--due:#f0a57c;--due-bg:#3a2418;--open:#7fd39a;--open-bg:#1b3323;--shut:#8a8984;--chip:#2a2927}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:12px 16px}
.wrap{max-width:820px;margin:0 auto}
h1{font-size:19px;margin:0 0 2px}
.sub{color:var(--muted);font-size:13px}
.bar{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;align-items:center}
.tab,.btn{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:6px 12px;font:inherit;font-size:14px;cursor:pointer}
.tab[aria-pressed="true"]{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.btn.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
label.tog{font-size:14px;display:flex;gap:6px;align-items:center;color:var(--muted)}
input[type=search]{flex:1;min-width:140px;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:6px 12px;font:inherit}
main{padding:12px 16px 80px}
.warn{background:var(--due-bg);color:var(--due);border-radius:10px;padding:10px 12px;font-size:13px;margin-bottom:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;margin-bottom:10px;overflow:hidden}
.card.logged:not(.open){opacity:.6}
a.btn{text-decoration:none;display:inline-block}
.head{display:flex;gap:10px;align-items:flex-start;padding:12px;cursor:pointer}
.head .main{flex:1;min-width:0}
.name{font-weight:650;font-size:16px}
.meta{color:var(--muted);font-size:13px}
.pill{display:inline-block;font-size:12px;border-radius:999px;padding:1px 8px;margin:4px 4px 0 0;background:var(--chip);color:var(--muted)}
.pill.open{background:var(--open-bg);color:var(--open)}
.pill.due{background:var(--due-bg);color:var(--due)}
.pill.shut{color:var(--shut)}
.call{flex:none;text-decoration:none;background:var(--accent);color:var(--accent-ink);border-radius:999px;padding:8px 14px;font-weight:600;font-size:14px;white-space:nowrap}
.body{display:none;border-top:1px solid var(--line);padding:12px}
.card.open .body{display:block}
.body h3{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:14px 0 6px}
.body h3:first-child{margin-top:0}
.script{background:var(--chip);border-radius:10px;padding:10px 12px;white-space:pre-wrap}
ul{margin:0;padding-left:18px}
.row2{display:flex;gap:14px;flex-wrap:wrap;align-items:flex-start}
.qr{background:#fff;padding:6px;border-radius:8px;line-height:0}
.qr svg{width:116px;height:116px}
.links a{color:var(--accent);word-break:break-all}
.copy{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}
.log{display:flex;gap:6px;flex-wrap:wrap}
.log .btn{font-size:13px;padding:5px 10px}
.log .btn.on{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.note{width:100%;margin-top:8px;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:8px;padding:8px;font:inherit}
.empty{color:var(--muted);text-align:center;padding:30px 0}
footer.dock{position:fixed;bottom:0;left:0;right:0;background:var(--card);border-top:1px solid var(--line);padding:10px 16px}
footer.dock .wrap{display:flex;gap:10px;align-items:center;justify-content:space-between}
.toast{position:fixed;left:50%;bottom:70px;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:8px 14px;border-radius:999px;font-size:14px;opacity:0;transition:opacity .2s;pointer-events:none}
.toast.show{opacity:1}
</style>
</head>
<body>
<header><div class="wrap">
  <h1>Call list</h1>
  <div class="sub" id="sub"></div>
  <div class="bar">
    <button class="tab" data-tab="due" aria-pressed="true">Follow-ups</button>
    <button class="tab" data-tab="new" aria-pressed="false">New calls</button>
    <button class="tab" data-tab="all" aria-pressed="false">All</button>
    <label class="tog"><input type="checkbox" id="openOnly"> Open now</label>
  </div>
  <div class="bar"><input type="search" id="q" placeholder="Search name, city, category"></div>
</div></header>
<main><div class="wrap">
  <div class="warn" id="warn" hidden></div>
  <div id="list"></div>
</div></main>
<footer class="dock"><div class="wrap">
  <span class="sub" id="logCount">No calls logged yet</span>
  <span><button class="btn" id="clearLog">Clear</button> <button class="btn primary" id="copyLog">Copy log for sheet</button></span>
</div></footer>
<div class="toast" id="toast"></div>
<script>
const DATA = __DATA__;
const M = DATA.meta;
const TZ = "America/Los_Angeles";
const KEY = "pr-outreach-log-v1";
let LOG = {};
try { LOG = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { LOG = {}; }
function saveLog(){ try { localStorage.setItem(KEY, JSON.stringify(LOG)); } catch (e) {} renderDock(); }

function laNow(){
  const p = Object.fromEntries(new Intl.DateTimeFormat("en-US",{timeZone:TZ,weekday:"short",hour:"numeric",minute:"numeric",hourCycle:"h23",year:"numeric",month:"2-digit",day:"2-digit"}).formatToParts(new Date()).map(x=>[x.type,x.value]));
  const dow = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"].indexOf(p.weekday);
  return {dow, mins:(+p.hour)*60+(+p.minute), iso:`${p.year}-${p.month}-${p.day}`, md:`${+p.month}/${+p.day}`};
}
const NOW = laNow();
function toMin(t){ const m=t.trim().match(/(\d{1,2}):(\d\d)\s*([AP]M)/i); if(!m) return null; let h=+m[1]%12; if(m[3].toUpperCase()==="PM") h+=12; return h*60+(+m[2]); }
function ranges(day){
  if(!day) return null; if(/closed/i.test(day)) return []; if(/24 hours/i.test(day)) return [[0,1440]];
  const out=[]; for(const part of day.split(",")){ const [a,b]=part.split(/[–-]/); const s=toMin(a||""), e=toMin(b||""); if(s==null||e==null) return null; out.push([s, e<=s? e+1440 : e]); }
  return out;
}
function openState(hours){
  if(!hours || hours.length!==7) return "unknown";
  const today=ranges(hours[NOW.dow]), yest=ranges(hours[(NOW.dow+6)%7]);
  if(today===null) return "unknown";
  if(today.some(([s,e])=>NOW.mins>=s&&NOW.mins<e)) return "open";
  if((yest||[]).some(([s,e])=>e>1440&&NOW.mins<e-1440)) return "open";
  return "closed";
}
function todayHours(hours){ return hours && hours.length===7 ? hours[NOW.dow] : null; }

function stars(l){ return l.rating ? `${l.rating}★ · ${l.reviews} Google reviews` : "No rating on the sheet"; }
function opener(l){
  const proof = l.rating && l.reviews ? `${l.rating} stars from ${l.reviews} reviews on Google` : "great reviews on Google";
  return `Hi, is this the owner or manager of ${l.name}?\n\nMy name's ${M.caller}, I'm with ${M.studio}, a small web design studio here in the Inland Empire. I saw ${l.name} has ${proof} but no website, so we put together a sample site for you. It costs nothing to look at.\n\nCan I text you the link?`;
}
function textMsg(l){ return `Hi, it's ${M.caller} from ${M.studio}. Here's the sample website we made for ${l.name}: ${l.url}\nTake a look and let me know what you think, or anything you'd change.`; }
function emailMsg(l){ return {subject:`A sample website for ${l.name}`, body:`Hi,\n\nThanks for talking with me today. Here's the sample website we put together for ${l.name}:\n\n${l.url}\n\nIt uses your real hours, services and reviews. Have a look, and tell me anything you'd like changed. Happy to walk you through it on a quick call.\n\n${M.caller}\n${M.studio}`}; }

const OUTCOMES = [
  ["noanswer","No answer"],["msg","Left msg"],["callback","Call back"],["sent","Sent link"],["interested","Interested"],["no","Not interested"]
];
function addDays(n){ const [y,m,d]=NOW.iso.split("-").map(Number); const t=new Date(Date.UTC(y,m-1,d+n)); return `${t.getUTCMonth()+1}/${t.getUTCDate()}`; }
function statusText(o){
  return {noanswer:`no answer ${NOW.md}, call again ${addDays(1)}`, msg:`msg left ${NOW.md}, call again ${addDays(2)}`,
    callback:`call back (see note) ${NOW.md}`, sent:`sent link ${NOW.md}, call ${addDays(2)}`, interested:`interested ${NOW.md}`, no:"not interested"}[o] || `note ${NOW.md}`;
}

function esc(s){ return String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }
function tel(p){ return "tel:"+String(p||"").replace(/[^0-9+]/g,""); }
function qrSvg(url){ try{ const q=qrcode(0,"M"); q.addData(url); q.make(); return q.createSvgTag({cellSize:4,margin:2,scalable:true}); }catch(e){ return ""; } }

let TAB="due";
function bucket(l){
  if(l.kind==="new") return "new";
  return "due";
}
function isDue(l){ return l.kind!=="new" && (!l.due || l.due<=NOW.iso); }

function render(){
  const q=document.getElementById("q").value.trim().toLowerCase();
  const openOnly=document.getElementById("openOnly").checked;
  let rows=DATA.leads.map(l=>({...l, st:openState(l.hours)}));
  if(TAB!=="all") rows=rows.filter(l=>bucket(l)===TAB);
  if(q) rows=rows.filter(l=>[l.name,l.city,l.category].join(" ").toLowerCase().includes(q));
  if(openOnly) rows=rows.filter(l=>l.st!=="closed");
  const stRank={open:0,unknown:1,closed:2};
  rows.sort((a,b)=> (TAB==="due" ? (isDue(b)-isDue(a)) || String(a.due||"9").localeCompare(String(b.due||"9")) : 0)
    || stRank[a.st]-stRank[b.st] || a.rank.reduce((acc,v,i)=>acc||(v<b.rank[i]?-1:v>b.rank[i]?1:0),0));
  const list=document.getElementById("list");
  if(!rows.length){ list.innerHTML=`<div class="empty">Nothing here${openOnly?" that's open right now":""}.</div>`; return; }
  list.innerHTML=rows.map(card).join("");
}
function card(l){
  const lg=LOG[l.row];
  const th=todayHours(l.hours);
  const stPill = l.st==="open" ? `<span class="pill open">Open now${th?" · "+esc(th):""}</span>` : l.st==="closed" ? `<span class="pill shut">Closed now${th?" · today "+esc(th):""}</span>` : `<span class="pill">Hours unknown</span>`;
  const duePill = l.kind!=="new" ? `<span class="pill ${isDue(l)?"due":""}">${esc(l.status)}${l.due?` · due ${l.due.slice(5).replace("-","/")}`:""}</span>` : "";
  const em=emailMsg(l);
  return `<div class="card${lg?" logged":""}" id="r${l.row}">
  <div class="head" data-row="${l.row}">
    <div class="main"><div class="name">${esc(l.name)}</div>
      <div class="meta">${esc(l.category||"")} · ${esc(l.city||"")} · ${esc(stars(l))}</div>
      <div>${duePill}${stPill}<span class="pill">${esc(l.priority||"")}${l.verdict?" · "+esc(l.verdict):""}</span>${lg?`<span class="pill open">Logged: ${esc(OUTCOMES.find(o=>o[0]===lg.o)?.[1]||"note")}</span>`:""}</div>
    </div>
    <a class="call" href="${tel(l.phone)}" onclick="event.stopPropagation()">Call</a>
  </div>
  <div class="body">
    <h3>Opener</h3><div class="script">${esc(opener(l))}</div>
    <h3>Talking points</h3><ul>
      ${l.angle?`<li>${esc(l.angle)}</li>`:""}
      <li>${esc(stars(l))}${l.yelp&&l.yelp.rating?` · Yelp ${esc(l.yelp.rating)}★ from ${esc(l.yelp.reviews)}${l.yelp.claimed?" (they claimed their Yelp page)":""}`:""}</li>
      ${l.topics.length?`<li>Reviewers keep mentioning: ${esc(l.topics.join(", "))}</li>`:""}
      ${l.services.length?`<li>Services on Yelp: ${esc(l.services.join(", "))}</li>`:""}
      <li>Their site would show up when people search for them, with hours, directions and a call button.</li>
    </ul>
    ${l.flags.length?`<h3>From the research (ask or avoid)</h3><ul>${l.flags.map(f=>`<li>${esc(f)}</li>`).join("")}</ul>`:""}
    ${l.notes?`<h3>Sheet note</h3><div>${esc(l.notes)}</div>`:""}
    <h3>Their sample site</h3>
    <div class="row2"><div class="qr">${qrSvg(l.url)}</div>
      <div class="links"><a href="${esc(l.url)}" target="_blank" rel="noopener">${esc(l.url)}</a><br>
      <span class="sub">${esc(l.address||"")} · <a href="${esc(l.maps)}" target="_blank" rel="noopener">Maps</a> · ${esc(l.phone||"")}</span>
      <div class="copy">
        <a class="btn" href="sms:${tel(l.phone).slice(4)}?&body=${encodeURIComponent(textMsg(l))}">Text the link</a>
        <button class="btn" data-copy="text" data-row="${l.row}">Copy text</button>
        <a class="btn" href="mailto:?subject=${encodeURIComponent(em.subject)}&body=${encodeURIComponent(em.body)}">Email the link</a>
      </div></div></div>
    <h3>Log this call</h3>
    <div class="log">${OUTCOMES.map(([k,t])=>`<button class="btn${lg&&lg.o===k?" on":""}" data-out="${k}" data-row="${l.row}">${t}</button>`).join("")}</div>
    <input class="note" data-note="${l.row}" placeholder="Note (best time, owner's name, what they asked)" value="${esc(lg?.n||"")}">
  </div></div>`;
}

function renderDock(){
  const n=Object.keys(LOG).length;
  document.getElementById("logCount").textContent = n ? `${n} call${n>1?"s":""} logged` : "No calls logged yet";
}
function toast(t){ const el=document.getElementById("toast"); el.textContent=t; el.classList.add("show"); setTimeout(()=>el.classList.remove("show"),1600); }
async function copy(t){ try{ await navigator.clipboard.writeText(t); toast("Copied"); }catch(e){ prompt("Copy this:", t); } }

document.addEventListener("click",e=>{
  const tab=e.target.closest(".tab");
  if(tab){ TAB=tab.dataset.tab; document.querySelectorAll(".tab").forEach(b=>b.setAttribute("aria-pressed",b===tab)); try{localStorage.setItem(KEY+"-tab",TAB);}catch(_){} render(); return; }
  const out=e.target.closest("[data-out]");
  if(out){ const row=out.dataset.row, prev=LOG[row]||{}; if(prev.o===out.dataset.out){ delete LOG[row]; } else { LOG[row]={o:out.dataset.out,n:prev.n||"",t:NOW.iso}; }
    saveLog(); const open=new Set([...document.querySelectorAll(".card.open")].map(c=>c.id)); render(); open.forEach(id=>document.getElementById(id)?.classList.add("open")); return; }
  const cp=e.target.closest("[data-copy]");
  if(cp){ const l=DATA.leads.find(x=>String(x.row)===cp.dataset.row); copy(textMsg(l)); return; }
  const head=e.target.closest(".head");
  if(head){ head.parentElement.classList.toggle("open"); }
});
document.addEventListener("input",e=>{
  if(e.target.dataset.note){ const row=e.target.dataset.note; LOG[row]=Object.assign(LOG[row]||{o:"",t:NOW.iso},{n:e.target.value}); saveLog(); }
  if(e.target.id==="q") render();
});
document.getElementById("openOnly").addEventListener("change",render);
document.getElementById("copyLog").addEventListener("click",()=>{
  const rows=Object.entries(LOG).map(([row,v])=>{ const l=DATA.leads.find(x=>String(x.row)===row)||{name:"?"}; return [row,l.name,statusText(v.o),v.n||""].join("\t"); });
  if(!rows.length){ toast("Nothing logged yet"); return; }
  copy("Row\tBusiness\tStatus\tNotes\n"+rows.join("\n"));
});
document.getElementById("clearLog").addEventListener("click",()=>{ if(confirm("Clear the call log on this device?")){ LOG={}; saveLog(); render(); } });

(function init(){
  try{ const t=localStorage.getItem(KEY+"-tab"); if(t){ TAB=t; document.querySelectorAll(".tab").forEach(b=>b.setAttribute("aria-pressed",b.dataset.tab===t)); } }catch(_){}
  const due=DATA.leads.filter(l=>isDue(l)).length, nw=DATA.leads.filter(l=>l.kind==="new").length;
  document.getElementById("sub").textContent=`${due} follow-ups due · ${nw} not called yet · ${M.declined} declined and ${M.no_site} without a site left out`;
  const age=M.last_call ? Math.round((new Date(NOW.iso)-new Date(M.last_call))/864e5) : null;
  if(age!==null && age>=3){ const w=document.getElementById("warn"); w.hidden=false; w.textContent=`The newest call status here is from ${M.last_call.slice(5).replace("-","/")} (${age} days ago). If you've called since, copy the Status and Notes columns in from the Google Sheet and rerun tools/leads/sync.py.`; }
  renderDock(); render();
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    sys.exit(main())
