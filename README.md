# math-curiosity

Open, reproducible experiments on equational laws and, later, other open problems. **One repository
per problem**, each with granular step records, certificates that anyone can re-check, a status label
on every claim, and CI that re-verifies on every push.

**Early and experimental. No result has passed the full verification protocol, and nothing is checked in
Lean.** Lean acceptance alone is not treated as proof, see [`docs/LEAN_CAVEATS.md`](docs/LEAN_CAVEATS.md).

## Problems

| Repository | Question | State |
|------------|----------|-------|
| [eq-unary-magma-laws](https://github.com/MauroBCardoso/eq-unary-magma-laws) | Which short laws over one binary and one unary operation imply which? | 712 laws up to size 3. 335,885 non-implications certified, 163,054 implications rest on z3 alone, 7,293 pairs open |
| [eq-laws-without-small-models](https://github.com/MauroBCardoso/eq-laws-without-small-models) | Nine of those laws have no model with 2 or 3 elements. Do they collapse every structure to one element? | 1 collapse (z3-only), 2 with verified size-4 models, 2 finite-versus-general leads, 4 open |

Planned, nothing started: problems from erdosproblems.com that carry no prize ([`docs/ERDOS_PLAN.md`](docs/ERDOS_PLAN.md)).

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
OWNER=<github-login> tools/new_problem.sh erdos-123
```

creates `../erdos-123` from [`template/`](template) with the shared docs copied in.

## Run autonomous sessions

[`docs/LOOPS.md`](docs/LOOPS.md).

## For LLMs

[`llms.txt`](llms.txt).

## License

Apache-2.0, see [`LICENSE`](LICENSE).

## Contributing

If you know of existing results that cover any of this, please open an issue with a reference. We have
not shown that any of these families is unstudied.
