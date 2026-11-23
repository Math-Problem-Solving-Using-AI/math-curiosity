# Running autonomous loop sessions

Each problem repository has `LOOP.md` (the protocol), `STATE.md` (queue, state, push policy) and
`llms.txt`. A loop session works on one repository at a time.

## Start a session

1. Open a terminal in the problem repository (clone it first).
2. Start Claude Code and run:

```
/loop Follow LOOP.md in this repository: do one iteration, then stop.
```

Omitting an interval lets the model pace itself. One iteration is one small, verifiable step.

## Rules that make loops safe

- The queue in `STATE.md` is the only source of tasks. Add tasks there, not in chat.
- Gates in `LOOP.md` run every iteration: independent verifiers, mutation tests, no stronger label than
  earned, no novelty claim without a literature check, "unknown" instead of guessing.
- `push: ask` in `STATE.md` means loop sessions only commit locally. Review, then push yourself. Switch
  to `push: allowed` only for repositories you trust the loop in.
- Every repository has a **finish line** (`LOOP.md`): every case the README asks about has an answer,
  every answer has a machine check, and the answer is explained in plain words. Then `STATE.md` gets
  `finished: yes` and loops stop. Raising labels (Lean, second provers), more literature and side
  questions go to "Optional later" in `STATE.md`, which loops never take. This rule exists because a
  loop on `eq-laws-without-small-models` had an answer for every case after run 3 and then ran 18 more
  times (runs 4 to 21, 2026-11-22 to 2026-11-23), raising labels and chasing literature leads.
- Loops also stop on an empty queue, a failing check they cannot fix, three iterations without
  progress, or a decision that belongs to the owner.
- Watch cost: z3 runs and large searches belong in background tasks that save state and resume.

## After a session

Read the new files in `steps/`, the diff of the README status tables, and `docs/LOG.md`. Do the
labels match the evidence? If a step claims more than its checks support, fix the label.
