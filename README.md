# math-curiosity

Open, reproducible experiments in the style of the Equational Theories Project (ETP): which short
laws imply which, for structures the ETP did not cover. **One repository per problem**, each with granular step records, certificates that anyone can re-check, a status label
on every claim, and CI that re-verifies on every push.

**Early and experimental. No result has passed the full verification protocol, and nothing is checked in
Lean.** Lean acceptance alone is not treated as proof, see [`docs/LEAN_CAVEATS.md`](docs/LEAN_CAVEATS.md).

## Problems

| Repository | Question | State |
|------------|----------|-------|
| [eq-unary-magma-laws](https://github.com/Math-Problem-Solving-Using-AI/eq-unary-magma-laws) | Which short laws over one binary and one unary operation imply which? | 712 laws up to size 3. 335,885 non-implications certified, 163,054 implications rest on z3 alone, 7,293 pairs open in the stored table (1,256 of them settled by the Equational Theories Project data and 608 more by new certificates, 2026-11-22). The part without `f` agrees with the ETP: 0 disagreements |
| [eq-laws-without-small-models](https://github.com/Math-Problem-Solving-Using-AI/eq-laws-without-small-models) | Nine of those laws have no model with 2 or 3 elements. Do they collapse every structure to one element? | **Finished 2026-11-23.** Every law answered with a machine check: 3 collapse, 2 have a 4-element model (known laws: central groupoid, Stein's third law), 4 have an infinite model (`z3-only`; that they have no finite one is a hand argument). Nothing Lean-checked |

## Queue

The next repositories come from [`docs/ideas/etp-variants.md`](docs/ideas/etp-variants.md): 21 ETP-style
ideas, each checked on 2026-11-22 against the ETP paper, its Zulip channel, arXiv and GitHub. Most are
done by others or crowded. The four we found no work on each have a repository prepared on 2026-11-23,
not published yet:

1. Laws with a unit element (a constant): `eq-unit-magma-laws`
2. Two binary operations, short laws first: `eq-two-operation-laws`
3. Implications inside commutative-only or idempotent-only magmas: `eq-commutative-idempotent-magmas`
4. Conditional rules, starting with cancellativity: `eq-cancellative-magma-laws`

Each one starts with its exact statement and a literature check before any computing.

## When a repository is finished

Every repository has a finish line (see [`docs/LOOPS.md`](docs/LOOPS.md)): every case its README asks
about has an answer, each answer has a machine check, and the answer is explained in plain words.
Then work stops there. Raising labels (Lean, second provers) and more literature are kept as
"Optional later" in its `STATE.md`.

## How this is organised

- This **hub** holds the shared rules, the problem template and the tools. The canonical shared docs live
  in [`docs/`](docs) and are copied into each problem repository under `docs/shared/` by
  [`tools/sync_shared_docs.sh`](tools/sync_shared_docs.sh).
- Each **problem repository** has: `README.md` (question and status table), `steps/` (one record per step
  with commands, checks, and a list of what was NOT verified), `results/` (certificates), `STATE.md` and
  `LOOP.md` for autonomous sessions, `llms.txt` for LLMs, and `.github/workflows/verify.yml`.

## Principles in one paragraph

Every claim has a label (`z3-only` < `model-verified` < `lean-checked` < `lean-checked + fidelity-reviewed +
literature-checked`) and only the last may be called a result. Counterexamples are stored as finite
structures that plain code can check. A checker that cannot fail proves nothing, so verifiers are
mutation-tested. If something is unknown it is written down as unknown. Full text:
[`docs/VERIFICATION_PROTOCOL.md`](docs/VERIFICATION_PROTOCOL.md).

## Add a problem

```
tools/new_problem.sh eq-unit-magma-laws
```

creates `../eq-unit-magma-laws` from [`template/`](template) with the shared docs copied in.

## Run autonomous sessions

[`docs/LOOPS.md`](docs/LOOPS.md).

## For LLMs

[`llms.txt`](llms.txt).

## License

Apache-2.0, see [`LICENSE`](LICENSE).

## Contributing

If you know of existing results that cover any of this, please open an issue with a reference. We have
not shown that any of these families is unstudied.
