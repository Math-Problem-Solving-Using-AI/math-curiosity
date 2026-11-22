> Script names below (`check_laws_text.py`, `check_laws_count.py`, `selftest_verifiers.py`) come from the `eq-unary-magma-laws` repository. Other problems provide their own equivalents.

# Verification protocol

A claim is a result only after every applicable stage below, in order. If a stage cannot be
completed, the claim stays at the last completed stage and the gap is written down. Never
skip a stage and never fill a gap from memory. Unknown stays "unknown".

Background: `LEAN_CAVEATS.md`.

## S0. State the claim exactly
- One sentence in plain English.
- Formal statement over the term encoding (laws are `lhs = rhs` over variables, `*` and `f`).
- Say what counts as evidence for and against.
- Say whether structures may be empty or have one element, and whether "implies" means over
  all structures or only finite ones. (Finite and general implication can differ.)

## S1. Statement fidelity
- Round-trip test: law text parses back to the stored term (`src/check_laws_text.py`).
- Independent re-count of the law enumeration by a different algorithm
  (`src/check_laws_count.py`).
- Sanity cases that must come out true AND cases that must come out false.
- For any Lean statement: write the English reading next to it, check types of every
  variable, look for junk values, vacuous or contradictory hypotheses, extra hypotheses.
  Prove a non-vacuity lemma (the hypotheses are satisfiable).

## S2. Evidence by kind
- **Non-implication (A does not imply B):** a finite structure, as tables. Checked by plain
  evaluation of every assignment (`check_model`), independent of z3 and numpy. Strongest
  kind of evidence, needs no trust in a prover.
- **Implication (A implies B):** a derivation: a chain of rewriting steps, each an instance
  of A, that a tiny separate checker can verify. A solver saying "unsat" is only a lead.
- **Collapse (A forces x = y):** same as implication.

## S2b. Test the verifier itself
- A checker that cannot fail proves nothing. Feed it corrupted input (flip a table entry, swap
  A and B, shift the law list) and confirm it reports failures. `src/selftest_verifiers.py`
  does this for our verifiers.
- If a run looks suspiciously fast or clean, measure it before believing it.

## S3. Second opinion from a different tool
- A second prover or independent implementation reaches the same conclusion.

## S4. Lean
- Only for claims that passed S2 and S3.
- All rules in `LEAN_CAVEATS.md` section "Rules this repo takes". Record `lean --version`,
  Mathlib commit, `#print axioms` output, and which external checker was run.

## S5. Literature check
- Search deeply (not one query). Look for the exact family and for equivalent formulations
  (universal algebra, algebras of type (2,1), identities, varieties).
- If found: label `known`, cite, do not present as new.
- If not found: write "not found in searches <list queries and dates>". That is not proof of
  novelty.

## S6. Write-up
- What is claimed, what is NOT claimed, every unresolved item, every tool and version.
- Result file has one of the status labels from the problem's `results/README.md`.

## Status ladder (a claim carries the highest one it earned)

`unverified` < `z3-only` < `model-verified` (non-implications only) < `independent-prover`
< `lean-checked` < `lean-checked + fidelity-reviewed + literature-checked`

Only the last one may be called a result.
