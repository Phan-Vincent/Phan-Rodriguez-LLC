#!/usr/bin/env python3
"""Regenerate the lead files everyone reads.

    python3 tools/leads/sync.py

Reads   leads/West_IE_No_Website_Leads.xlsx   (sheet values, call status, mockup and research columns)
        leads/research/*.json                 (structured research entries, later files win)
        docs/handoffs/data/{site,google,yelp}-facts.json  (fact-check data for built sites, if present)
        docs/claims.md                        (who is working on which row)
        mockups/                              (which site folders exist)
Writes  leads/leads.json                      (one record per lead; do not edit by hand)
        leads/google-sheet-paste-L2.tsv       (columns L-Q, paste at L2 on the Leads tab)
        docs/BUILD-QUEUE.md                   (researched rows with no site, best first)
Prints  problems it finds. Standard library only.
"""
import datetime
import json
import pathlib
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[2]
XLSX = ROOT / "leads" / "West_IE_No_Website_Leads.xlsx"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "p": "http://schemas.openxmlformats.org/package/2006/relationships"}
COLS = ["priority", "name", "category", "area", "address", "phone", "rating", "reviews", "maps",
        "status", "notes", "mockup_exists", "mockup_path", "build_order", "build_effort", "research_note", "last_checked"]
SECOND_CONCEPTS = {"el-rey-retro-roadside"}  # a second concept for a row that already links one
VERDICTS = ["Build first", "Build", "Build, Google only", "Check website first", "Low priority", "Hold", "Skip"]


def col_index(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group():
        n = n * 26 + ord(ch) - 64
    return n - 1


def read_sheet():
    """Rows of the first worksheet as dicts keyed by COLS, plus the sheet row number and Maps link."""
    z = zipfile.ZipFile(XLSX)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    rels = {}
    rel_path = "xl/worksheets/_rels/sheet1.xml.rels"
    if rel_path in z.namelist():
        for rel in ET.fromstring(z.read(rel_path)).findall("p:Relationship", NS):
            rels[rel.get("Id")] = rel.get("Target")
    links = {}
    for h in sheet.iter("{%s}hyperlink" % NS["m"]):
        rid = h.get("{%s}id" % NS["r"])
        if rid in rels:
            links[h.get("ref")] = rels[rid]
    rows = []
    for row in sheet.iter("{%s}row" % NS["m"]):
        rnum = int(row.get("r"))
        if rnum == 1:
            continue
        rec = {k: None for k in COLS}
        for c in row.findall("m:c", NS):
            i = col_index(c.get("r"))
            if i >= len(COLS):
                continue
            v = c.find("m:v", NS)
            if v is None or v.text is None:
                continue
            t, text = c.get("t"), v.text
            if t == "s":
                val = shared[int(text)]
            elif t == "d":
                val = text[:10]
            elif t in ("str", "inlineStr", "b", "e"):
                val = text
            else:
                f = float(text)
                val = int(f) if f == int(f) else f
            rec[COLS[i]] = val
        if not rec["name"]:
            continue
        rec["row"] = rnum
        rec["maps"] = links.get("I%d" % rnum)
        rows.append(rec)
    return rows


def digits(s):
    return re.sub(r"\D", "", str(s or ""))


def read_research():
    out = {}
    for f in sorted((ROOT / "leads" / "research").glob("*.json")):
        data = json.loads(f.read_text())
        for e in data.get("entries", []):
            e = dict(e)
            e["date_read"] = data.get("_meta", {}).get("date_read")
            out[e["row"]] = e
    return out


def read_fact_check():
    d = ROOT / "docs" / "handoffs" / "data"
    try:
        site = json.loads((d / "site-facts.json").read_text())
        goog = json.loads((d / "google-facts.json").read_text())
        yelp = json.loads((d / "yelp-facts.json").read_text())
    except FileNotFoundError:
        return {}
    out = {}
    for folder, g in goog.items():
        if folder.startswith("_") or folder not in site or not site[folder].get("row"):
            continue
        out[site[folder]["row"]] = {"date_read": "2026-11-10", "folder": folder, "google": g, "yelp": yelp.get(folder)}
    return out


def read_claims(problems):
    out = {}
    f = ROOT / "docs" / "claims.md"
    if not f.exists():
        return out
    for line in f.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or not cells[0].isdigit():
            continue
        row, name, who, what, date, state = cells
        if state.lower() != "open":
            continue
        out[int(row)] = {"by": who, "for": what, "date": date}
        try:
            age = (datetime.date.today() - datetime.date.fromisoformat(date)).days
            if age > 1:
                problems.append(f"claim on row {row} ({name}) by {who} is {age} days old")
        except ValueError:
            problems.append(f"claim on row {row} has an unreadable date: {date}")
    return out


def main():
    problems = []
    rows = read_sheet()
    research = read_research()
    checks = read_fact_check()
    claims = read_claims(problems)
    folders = {p.name for p in (ROOT / "mockups").iterdir() if (p / "index.html").exists()}

    leads = []
    for r in rows:
        path = r["mockup_path"] or ""
        folder = path.split("/")[1] if path.startswith("mockups/") and path.count("/") >= 2 else None
        has_site = bool(folder and folder in folders)
        if r["mockup_exists"] == "Yes" and not has_site:
            problems.append(f"row {r['row']} ({r['name']}) is marked as having a mockup but {path or 'no path'} does not exist")
        res = research.get(r["row"])
        if res and digits(res.get("google", {}).get("phone")) and digits(res["google"]["phone"]) != digits(r["phone"]):
            problems.append(f"row {r['row']} ({r['name']}): research phone {res['google']['phone']} differs from sheet {r['phone']}")
        if res and res.get("verdict") not in VERDICTS:
            problems.append(f"row {r['row']}: unknown verdict {res.get('verdict')!r}")
        for src in (res or {}).get("google", {}), ((res or {}).get("yelp") or {}):
            h = src.get("hours")
            if h is not None and len(h) != 7:
                problems.append(f"row {r['row']}: an hours list does not have 7 entries")
        leads.append({
            "row": r["row"], "priority": r["priority"], "name": r["name"], "category": r["category"], "area": r["area"],
            "address": r["address"], "phone": r["phone"], "sheet_rating": r["rating"], "sheet_reviews": r["reviews"], "maps": r["maps"],
            "call": {"status": r["status"], "notes": r["notes"]},
            "mockup": {"exists": has_site, "folder": folder if has_site else None},
            "claim": claims.get(r["row"]),
            "research": res,
            "fact_check": checks.get(r["row"]),
            "research_note": r["research_note"], "last_checked": r["last_checked"],
        })
    marked = {l["mockup"]["folder"] for l in leads if l["mockup"]["exists"]}
    for f in sorted(folders - marked - SECOND_CONCEPTS):
        problems.append(f"site folder mockups/{f} is not linked from any sheet row")
    for row in sorted(set(claims) - {l["row"] for l in leads}):
        problems.append(f"claim on row {row} does not match a sheet row")

    meta = {"generated": datetime.date.today().isoformat(), "generator": "tools/leads/sync.py", "do_not_edit": True,
            "counts": {"leads": len(leads), "with_site": sum(l["mockup"]["exists"] for l in leads),
                       "researched": sum(bool(l["research"]) for l in leads), "open_claims": len(claims)}}
    (ROOT / "leads" / "leads.json").write_text(json.dumps({"_meta": meta, "leads": leads}, indent=1, ensure_ascii=False) + "\n")

    with open(ROOT / "leads" / "google-sheet-paste-L2.tsv", "w") as f:
        for r in rows:
            vals = [r["mockup_exists"], r["mockup_path"], r["build_order"], r["build_effort"], r["research_note"], r["last_checked"]]
            f.write("\t".join("" if v is None else str(v).replace("\t", " ").replace("\n", " ") for v in vals) + "\n")

    declined = lambda l: "not interested" in (l["call"]["status"] or "").lower()
    queue = [l for l in leads if l["research"] and not l["mockup"]["exists"] and not declined(l)]
    queue.sort(key=lambda l: (VERDICTS.index(l["research"]["verdict"]) if l["research"]["verdict"] in VERDICTS else 99, l["row"]))
    out = ["# Build queue", "",
           f"Generated by `tools/leads/sync.py` on {meta['generated']}. Do not edit; change the research, the workbook or `docs/claims.md` and rerun.", "",
           "Researched rows with no site, best first. Claim a row in `docs/claims.md` before building it. Rows below the line are not ready to build.", "",
           "| Row | Business | City | Verdict | Google | Yelp | Claimed | Brief |", "|---|---|---|---|---|---|---|---|"]
    ready = True
    for l in queue:
        res = l["research"]
        if ready and res["verdict"] in VERDICTS[3:]:
            ready = False
            out.append("| | **Not ready: clear the flag first** | | | | | | |")
        g, y = res.get("google") or {}, res.get("yelp") or {}
        gs = f"{g.get('rating')} / {g.get('reviews')}" if g.get("rating") else "–"
        ys = f"{y.get('rating')} / {y.get('reviews')}" if y.get("rating") else ("no page" if not y else "no rating")
        c = l["claim"]
        cs = f"{c['by']} ({c['for']})" if c else ""
        out.append(f"| {l['row']} | {res.get('name') or l['name']} | {res.get('city') or l['area']} | {res['verdict']} | {gs} | {ys} | {cs} | [{pathlib.Path(res['handoff']).name}](handoffs/{pathlib.Path(res['handoff']).name}) |")
    built_researched = [l for l in leads if l["research"] and l["mockup"]["exists"]]
    out += ["", f"{len(queue)} rows in the queue. {len(built_researched)} researched rows already have a site: "
            + ", ".join(f"{l['row']} {l['name']}" for l in built_researched) + "." if built_researched else f"{len(queue)} rows in the queue.", ""]
    (ROOT / "docs" / "BUILD-QUEUE.md").write_text("\n".join(out))

    print(f"{meta['counts']['leads']} leads, {meta['counts']['with_site']} with a site, {meta['counts']['researched']} researched, "
          f"{len(queue)} in the build queue, {len(claims)} open claims")
    if problems:
        print(f"{len(problems)} problems:")
        for p in problems:
            print(" -", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
