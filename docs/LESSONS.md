# Lessons: do not repeat these

Add an entry whenever something fails or surprises us. Format: what happened, why, rule.

## Environment

- **numpy missing in venv** (2026-11-22). `models.py` crashed with ModuleNotFoundError.
  Venv only had z3. Rule: install from `requirements.txt` first, and refreeze after adding packages.
- **`rmdir` failed with "Device or resource busy"** (2026-11-22). Shell working directory was
  inside the folder being removed, and a `&&` chain then skipped later steps silently.
  Rule: never remove the current directory, and check output of chained commands.
- Windows: call the venv Python directly (`.venv/Scripts/python.exe`), not `python`.

## Method

- A web search result summary is not a literature review. Mark claims of novelty only after
  a deeper search. See `PRIOR_WORK.md`.
- Counterexample-by-small-model leaves candidates that may still be false, because some
  non-implications need models larger than 3 elements (ETP found the same).
- "No model of size 2 or 3" does NOT mean "forces a one-element structure". Two laws,
  `(x*y)*(y*x) = y` and `(x*y)*(y*z) = y`, have models of size 4. Headline candidate counts
  also mislead: 153,576 of 171,055 candidates came from such zero-model source laws.

## Long runs

- **A 40-minute run kept results only in memory and saved at the end** (2026-11-22). I stopped it
  when it looked stuck on the last 14 of 464 tasks and lost everything. Rule: any run longer than
  a couple of minutes saves state every few tasks, resumes from saved state, and prints progress.
- **Skip work whose answer is already decided.** The slow tail was nine laws with 711 targets each,
  where z3 could not succeed in a useful way. Rule: before launching a big run, check which
  tasks are hopeless and give them their own problem.
- Never split a path on a substring like `"src"`. Use `pathlib` (`Path(__file__).resolve()`).

## Facts from the web and from subagents

- **Search summaries disagreed with the primary pages.** Examples found on 2026-11-22: a summary
  gave a specific CVE number for the Lean kernel bug, the advisory says none was assigned; a
  summary said only "13" of an AI system's Erdős solutions addressed the intended problem, no
  page we read says that; a summary said a checker was unaffected, no page mentions it.
  Rule: summaries are leads. Read the primary page, quote it, label SINGLE-SOURCE or UNCONFIRMED.
- A PDF fetched as raw bytes may be unreadable, and a "summary" of it may invent content. If the
  body text was not read, say "not read" (see `LEAN_CAVEATS.md`, arXiv 2606.29493).

## Hand math

- **My first hand proof skipped a step.** For `f(x)*(y*z) = y` I sketched "f constant, so
  collapse". z3 returned `unknown` on the last step. The missing step was applying the law at the
  product `y*z`. Rule: a hand proof is not a proof until each step is machine-checked or checked
  by an independent method, and a timeout is information that a step may be missing.

## z3

- `CheckSatResult` is unhashable. Use `str(result)` as the dict key.
- `EnumSort` names must be unique per call, or z3 raises "enumeration sort name is already declared".
- **z3 outcomes are not stable between runs.** Proving collapse for 216 laws gave 207 proofs
  at a 5s timeout and 205 at a 60s timeout (8 parallel workers). `unsat` (a proof) can be
  trusted, `unknown` carries no information. Rule: accumulate proofs across runs, never
  overwrite, never read a missing proof as evidence of non-implication.

## Access and sources

- **Read `robots.txt` before the first request to a site** (2026-11-22). One request to
  erdosproblems.com (`curl` of `/5`, output discarded) was sent before reading its `robots.txt`,
  which disallows Claude agents (`Claude-User`, `ClaudeBot`, ...). A plain `curl` is not
  blocked by the server, but sending it anyway would be working around the site's wishes.
  Rule: read `robots.txt` first, and if it disallows the agent, use the owner's saved copy, a
  database with an open license, or ask the owner. Do not change the user agent to get through.
- **A saved page can be older than its save date.** The prizes page saved on 2026-11-22 showed
  data from about 2026-10-16 (dated by comparing fields with a database that records update
  dates). Rule: date the content, not the file.

## Laws and solvers

- **A law with a variable that appears only on one side, as that whole side, collapses
  trivially** (`((x*y)*z)*x = w`: put `x = y = z = a` and get `a = b`). z3 returned `unknown`
  on it at 5 s and it sat on the "open" list until the ETP cross-check showed it. Rule: before
  calling a law open, check the cheap syntactic cases by hand, and cross-check against any
  external data that covers part of the family.
- **Split a stuck bucket by its simplest feature before declaring it hard.** The nine laws with
  no small model were one bucket. Three of them do not mention `f`, and for those the ETP data
  plus "try every `f` on a known model" settled 1,417 + 1,256 pairs in seconds.
