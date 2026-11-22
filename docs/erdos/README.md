# Erdős problems with no prize: sources, data, triage

Work started 2026-11-22. Plan: [`../ERDOS_PLAN.md`](../ERDOS_PLAN.md). Rules for any contribution:
[`RULES.md`](RULES.md). Triage: [`triage-2026-11-22.md`](triage-2026-11-22.md). One dossier per
shortlisted problem: [`dossiers/`](dossiers). Attempts, each laid out like a future problem
repository: [`attempts/`](attempts).

## What "prize 0" means (verified, not assumed)

The owner's starting point was the page https://www.erdosproblems.com/prizes/0. It lists **1,107
problems**. The community database [teorth/erdosproblems](https://github.com/teorth/erdosproblems)
(file `data/problems.yaml`, Apache-2.0, commit `8e3d61bff616e6c6498d046eb6f0dd42cf4d9afe` of
2026-11-22) has a field `prize`. Its `CONTRIBUTING.md` says: "use "no" if no prize given, or the
currency amount otherwise". In that file 1,107 of the 1,221 problems have `prize: "no"`, and **these
1,107 numbers are exactly the 1,107 numbers on the saved page** (checked by set comparison, 0
differences in either direction). So "prize 0" = the problems with no prize. The list contains both
open and solved problems.

## Sources and how they were obtained

| Source | How | Date | Checksum / version |
|--------|-----|------|--------------------|
| Saved page `source/prizes-0-2026-11-22.html` (local only, not committed: it is a copy of someone else's site) | saved by the owner in a browser, because our tool got HTTP 403 | saved 2026-11-22, **content dates from about 2026-10-16** (see below) | 151,690,579 bytes |
| `teorth/erdosproblems` `data/problems.yaml` | `gh repo clone` | 2026-11-22 | commit `8e3d61b` |
| `google-deepmind/formal-conjectures` (Lean statements) | `gh repo clone` | 2026-11-22 | see the dossiers |

**erdosproblems.com itself is not fetched by us.** Its `robots.txt` (read on 2026-11-22) contains
`User-agent: Claude-User` / `Disallow: /`, and the same for `ClaudeBot`, `Claude-Web`, `anthropic-ai`
and `Claude-SearchBot`. The assistant doing this work is a Claude agent, so the site is off limits to it.
One page (`/5`) had been requested once with `curl`, before the robots file was read. The response
was discarded unread (recorded in `../LESSONS.md`). The site's problem pages, LaTeX sources,
comment threads, FAQ and rules are therefore **not read**. Where they matter, a dossier says so and
the owner is asked to save the page.

## The saved page is about five weeks older than its save date

Each entry's citation line says "accessed 2026-10-16", but the file was saved on 2026-11-22.
Test: the page shows two fields that come from the community database, "Formalised statement?"
and OEIS. Comparing them with the database of 2026-11-22:
- 148 entries say "No" on the page but "yes" in the database. For **every one** of them, the
  database's `formalized.last_update` is between 2026-10-17 and 2026-11-19. None is on or before
  2026-10-16.
- No entry has "yes" on both sides with a database update after 2026-10-16.
- 54 entries have OEIS links in the database that are missing on the page.

Conclusion: the page shows the database as it was around 2026-10-16. It is most likely a cached
rendering. Anything taken from the page may be up to five weeks stale. **Status, formalization
and OEIS fields are therefore taken from the database (2026-11-22), not from the page.**

## Statuses (from the database, not from the site)

The site stopped showing statuses on 2026-10-06. The database README says this follows "policy changes
announced at erdosproblems.com" on that date (forum thread `blog:9`, not read by us). The
database still records an unofficial, crowdsourced status. Its `CONTRIBUTING.md` says the site
"will report whether these problems are officially classified as "solved"" and is "the more
reliable source" when the two disagree.

The 1,107 problems with no prize, by database status: open 522, proved 309, disproved 126, solved
97, falsifiable 25, not disprovable 8, verifiable 7, decidable 7, independent 3, not provable 3.
Definitions are quoted in `RULES.md`. The triage works on the 561 that are open, falsifiable,
verifiable or decidable.

## The extraction, and how it was checked

`extract_prizes0.py` (regular expressions) produced `data/prizes0-2026-11-22.json` (local only).
`spotcheck_extraction.py` re-reads entries with a different method (Python's event-based
`html.parser` on each entry's block) and compares tags, formalised yes/no and link, OEIS numbers,
comment, proof-claim and exposition counts, reaction lists, and the plain words of the statement.

- 25 entries chosen at random (seed 20261122): **0 mismatches**.
- Mutation test: in a copy of the JSON, one entry each got a changed tag list, comment count,
  formalised flag, OEIS list, or statement. Every corruption that touches compared text was
  reported. A word replaced inside a formula was not: formulas are compared only as placeholders,
  by design.
- Counts recomputed from the JSON match the ones given in the prompt: 773 formalised and 334 not, 294
  with OEIS links, 847 with comments, 191 with at least one proof claim, 71 marked "looks tractable",
  126 "looks difficult", 165 "currently working on".

Limits: statements on the page are screen-reader text, not LaTeX. They are fine for a first read,
but no formula is relied on until it is checked against a LaTeX or Lean source. Reactions are
user opinions. User names are kept only in the local JSON and are never copied into committed files.
