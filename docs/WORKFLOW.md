# How we work the lead list

Agreed Nov 11, 2026 after a day in which two sessions built the same sites and research arrived after the builds. This is the short version; the look-and-feel rules stay in `docs/design-system/ui-changes-playbook.md`.

## Who does what

| Lane | Owner | Touches |
|---|---|---|
| Research and fact checks | Vincent's session | `docs/handoffs/`, `leads/` |
| Building sites | Andrew's session | `mockups/`, `tools/auto-shop-generator/` |
| Calls and call notes | Vincent | Status and Notes columns of the Google Sheet |

A session does not edit the other lane's files unless asked.

## The five rules

1. **Pull first, every time.** `git pull --rebase origin main` before picking rows and again before committing.
2. **Claim before you work.** Add a line to `docs/claims.md`, commit and push it, then start. One claim commit is cheap; a duplicated site is not. Remove or close the line when the work is pushed.
3. **Research before build.** A site is built only for a row that has a research entry (`leads/leads.json` has a `research` block for it, and it appears in `docs/BUILD-QUEUE.md`). If a row has no research, claim it for research first or ask.
4. **Build from the queue, top down.** `docs/BUILD-QUEUE.md` lists researched rows with no site, best first, with the verdict and the flags. Rows marked Hold, Skip or Check website first are not built until the flag is cleared.
5. **One generator, one style.** Sites are built by `tools/auto-shop-generator/build_flagship.py`. Style changes happen between batches, as one dated note in `DESIGN.md`, not mid-batch. Do not rebuild existing sites in a new style without both people agreeing first.

## Where facts live

- `leads/leads.json` is the one file to read for a lead: sheet values, call status, mockup path, claim, and research (Google Maps and Yelp facts, hours, verdict, flags). It is generated; do not edit it by hand.
- `leads/research/*.json` holds the research entries that feed it. New research is added there.
- `leads/West_IE_No_Website_Leads.xlsx` is the working copy of the sheet. Columns J and K (Status, Notes) belong to the Google Sheet and are copied in from it. Columns L to Q (mockup and research columns) belong to the repo.
- `leads/google-sheet-paste-L2.tsv` is columns L to Q for pasting into the Google Sheet at cell L2 on the Leads tab.
- `docs/handoffs/` holds the human-readable briefs and fact checks.

Regenerate the generated files after any change to the workbook, research or claims:

```bash
python3 tools/leads/sync.py
```

It needs only the Python standard library. It also prints problems it finds (a site folder with no sheet row marked, a claim older than a day, a research phone that does not match the sheet).

## Pushing research quickly

Research only helps if it lands before the build. Vincent has said he is happy for research handoffs, fact checks, `leads/` files and claim lines to be pushed as soon as they are checked. Each session still follows its own rules about confirming before it commits or pushes. Anything under `mockups/` or `tools/auto-shop-generator/` needs a yes from the person whose lane it is.

## Hours and other disagreements

When Google and Yelp disagree, the site shows the shorter hours and tells visitors to call. Nobody here can edit a shop's listing; "fix Google" means "tell the owner on the call".

## Open decision

Whether the flagship generator's current look is the one we keep for the next batches. Until Vincent and Andrew both say otherwise, it is.
