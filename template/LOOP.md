# Loop protocol

For autonomous, repeated sessions (for example Claude Code `/loop`). One iteration is one small,
verifiable step. Before doing anything read this file, `STATE.md`, `README.md` and the newest file
in `steps/`.

## One iteration

1. Read `STATE.md`. Take the first item of the queue. If the queue is empty, stop.
2. Do exactly that item. Keep it small enough to finish and verify in one go. For anything that
   runs more than a couple of minutes, save state every few tasks and make it resumable
   (see `docs/shared/LESSONS.md`).
3. Run the gates below.
4. Record it: add or update a file in `steps/` (format: `docs/shared/STEP_TEMPLATE.md`, including a
   non-empty "NOT verified" list). Add surprises and mistakes to `docs/LOG.md` or, if general, to
   `docs/shared/LESSONS.md`. Change status tables in `README.md` only to labels actually earned.
5. Update `STATE.md`: move the item to Done with the date, add follow-ups to the queue, write two
   lines under "Last iteration".
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

## Stop conditions

Stop and write the reason under "Blocked" in `STATE.md` when: the queue is empty; a check fails and
you cannot fix it in one iteration; three iterations in a row made no progress; or the next step
needs the owner (publishing elsewhere, license, naming, spending real money or compute).

## Suggested loop prompt

```
/loop Follow LOOP.md in this repository: do one iteration, then stop.
```
