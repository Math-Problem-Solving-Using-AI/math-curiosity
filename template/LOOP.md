# Loop protocol

For autonomous, repeated sessions (for example Claude Code `/loop`). One iteration is one small,
verifiable step. Before doing anything read this file, `STATE.md`, `README.md` and the newest file
in `steps/`.

## One iteration

1. Read `STATE.md`. If it says `finished: yes`, stop: a finished repository gets no loop work.
   Otherwise take the first item of the queue. If the queue is empty, check the finish line
   below, then stop.
2. Do exactly that item. Keep it small enough to finish and verify in one go. For anything that
   runs more than a couple of minutes, save state every few tasks and make it resumable
   (see `docs/shared/LESSONS.md`).
3. Run the gates below.
4. Record it: add or update a file in `steps/` (format: `docs/shared/STEP_TEMPLATE.md`, including a
   non-empty "NOT verified" list). Add surprises and mistakes to `docs/LOG.md` or, if general, to
   `docs/shared/LESSONS.md`. Change status tables in `README.md` only to labels actually earned.
5. Update `STATE.md`: move the item to Done with the date, write two lines under "Last iteration".
   A follow-up goes into the queue only if it helps answer a case that is still open; every other
   follow-up goes to "Optional later". Then check the finish line below.
6. Commit in small commits, one logical change each. Do not push unless `STATE.md` says
   `push: allowed`.

## Gates (all must hold before anything is claimed)

- **Hallucination guard.** If you do not know something, write "unknown" and add a queue item to
  find out from a primary source. Never fill a gap from memory. Search results and other agents'
  reports are leads, not facts: read the primary page, quote it, label what you could not read.
- **Labels.** A claim carries only the label it earned (`docs/shared/VERIFICATION_PROTOCOL.md`).
  A z3 `unsat` is `z3-only`. Lean acceptance is not enough (`docs/shared/LEAN_CAVEATS.md`).
- **Independent checks pass.** Run from the repository root:
  - (list the repository's verifier commands here)
  A verifier you changed must still fail on corrupted input (mutation test).
- **Never** edit or delete certificates or results to make a check pass.
- **No novelty claim** without a recorded literature check.

## Finish line

The question in `README.md` names a finite list of cases (for example every pair of laws up to size 3,
or each of nine laws). The repository is **finished** when all three hold:

1. Every case has an answer (for example "implies" or "does not imply", "collapses" or "has a model").
2. Every answer has at least one machine check that the gates re-run: a certificate checked by plain
   code, a model checked by evaluation, or a solver result honestly labelled `z3-only`.
3. `README.md` states the answer in plain words, and every step file starts with "In plain words".

When it holds: write `finished: yes` and the date in `STATE.md`, move every remaining queue item to
"Optional later", say so under "Last iteration", and stop.

These are **not** reasons to keep going, and go to "Optional later" instead of the queue: raising the
label of an answer that already has a machine check (Lean, a second prover, a human review), reading
more literature, chasing leads, and side questions the README did not ask. Loop sessions never take
items from "Optional later"; only the owner moves an item back to the queue. Extending the question
(bigger laws, more cases) is a new question for the owner, not loop work. Labels stay honest either
way: finished means answered and machine-checked, not `lean-checked` and not novel.

## Stop conditions

Stop when the finish line is reached. Stop and write the reason under "Blocked" in `STATE.md`
when: the queue is empty but the finish line is not reached; a check fails and
you cannot fix it in one iteration; three iterations in a row made no progress; or the next step
needs the owner (publishing elsewhere, license, naming, spending real money or compute).

## Suggested loop prompt

```
/loop Follow LOOP.md in this repository: do one iteration, then stop.
```
