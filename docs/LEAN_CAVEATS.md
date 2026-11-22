# Lean caveats: what a Lean-accepted proof does NOT guarantee

Compiled 2026-11-22. Sources were read on their own pages, not taken from search summaries.
Where a source could not be read or two sources disagree, that is stated. Re-check before
relying on any item, Lean moves fast.

Labels:
- **PAGE-STATED**: we read it on the cited page.
- **SINGLE-SOURCE**: appears on one page only, the other pages are silent.
- **UNCONFIRMED**: seen in a search summary or second-hand text. We could not verify it.
  Do not rely on it and do not repeat it as fact.

Rule of thumb for this repo: **Lean accepting a proof is necessary, never sufficient.**

---

## C1. Lean checks the statement as written, not as intended (PAGE-STATED)

Lean reference, "Validating Proofs":
https://lean-lang.org/doc/reference/4.36.0/ValidatingProofs/

- It says it is "important to distinguish the question 'does the theorem have a valid proof'
  from 'what does the theorem statement mean'."
- Even the strongest setup (comparator with external kernels) lists as remaining assumptions
  that there is "No human error or misleading presentation of the theorem statement in the
  trusted challenge file", and that no bug is shared by all checkers.
- If in doubt, "its statement and all referenced definitions must be investigated carefully,
  in particular with regard to custom notation and type classes."

**For us:** the most likely way to fool ourselves is a Lean statement that is not the law
implication we mean. See `VERIFICATION_PROTOCOL.md`, statement fidelity step.

## C2. Documented misformalizations (partly confirmed)

- **Erdős Problem 124** (PAGE-STATED, arXiv 2605.13171v1, Related Work, read verbatim):
  "Boris Alexeev used a repository formalization to prove Erdős Problem 124 ... with
  Aristotle ... Although the statement was initially misformalized and included an unintended
  extra hypothesis, Aristotle's proof succeeded without relying on it."
  https://arxiv.org/html/2605.13171v1
- Same paper, verbatim: "since a proof may settle a misformalized statement rather than the
  intended problem, any result for an open conjecture triggers manual inspection for
  fidelity." It also reports 291 misformalizations fixed, with misrepresentation (48%) and
  semantic (35%) the most common categories. (Read in the verbatim part of the page. Counts
  not independently checked.)
- **Erdős 707** (PARTLY CONFIRMED): the Lean Zulip thread relays the paper's claim. Boris
  Alexeev there: "Claim 10 from our paper ... corresponds to the minor mis-formalization
  issue in the `formal-conjectures` project, namely the 'infinite' case v=0." The thread does
  not show the repository statement being changed.
  https://leanprover-community.github.io/archive/stream/113488-general/topic/Erdos.20707.html
- **Aletheia and Erdős problems** (PAGE-STATED but limited): paper quote relayed on Zulip:
  "An expert is still required to interpret the argument in natural language to determine if
  a formally verified proof addresses the intended mathematical meaning." A Zulip comment
  gives "137 Fundamentally Flawed solutions from the 63 Technically Correct". We could not
  check those numbers in the paper itself (the PDF text was not readable).
  https://leanprover-community.github.io/archive/stream/219941-Machine-Learning-for-Theorem-Proving/topic/DeepMind's.20Aletheia.20Erdos.20problem.html
- **UNCONFIRMED:** a search summary said only "13" of the AI system's correct solutions
  addressed the intended problem. We did NOT find that number. Do not cite it.
- **UNCONFIRMED:** Erdős 918 as a case where a bound was lost in formalization.

## C3. Junk values and silent conventions (PAGE-STATED, Lean Zulip thread, May 2025)

https://leanprover-community.github.io/archive/stream/113488-general/topic/Documenting.20lean.20pitfalls.3A.20feedback.20requested.html
Living document by the thread author: https://github.com/nielsvoss/lean-pitfalls (not read by us).

Confirmed in the part of the thread we read verbatim:
- Subtraction on natural numbers truncates at 0.
- Division by zero returns 0 (junk value). Natural number division rounds down.
- `Real.sqrt` on negatives, `Real.log 0`, subtraction on `NNReal`/`ENNReal` return junk values.
- `⨅ i ∈ s, f i` ranges over proofs of `i ∈ s`, so a default value can give a wrong result.
  Example from the thread: `⨆ (x : ℝ) (_ : x < - 3), x = 0`.
- Two non-definitionally-equal instances for "the same" structure is a common pitfall.
- Arithmetic on `Fin n` silently wraps around.
- `(x : S)` for a set `S` (a subtype) differs from `(x : X) (hx : x ∈ S)`.
- Finite sets can be modeled by several non-equivalent encodings.

**UNCONFIRMED (summary only, not read verbatim):** advice to avoid `n-1`, `sSup ∅ = 0`,
"motive is not type correct", `let` versus `have` issues.
**UNCONFIRMED:** arXiv 2606.29493 ("Faults in Our Formal Benchmarking") defect categories and
percentages. The PDF text could not be read, so nothing from it is used here.

## C4. `sorry`, axioms, and the green check (PAGE-STATED, Lean reference)

- The editor's "blue double check marks" appear "even when there are explicit uses of sorry
  or incomplete proofs in the dependencies". They do not prove the dependencies are complete.
- `#print axioms` should list only `propext`, `Classical.choice`, `Quot.sound`.
  `sorryAx` means the theorem or a dependency is incomplete. An axiom with `_native` in the
  name means native evaluation was used. Any other axiom means the theorem is only valid
  relative to that axiom. `#print axioms` does not catch malicious code.

## C5. `native_decide` and trusting the compiler (PAGE-STATED)

Lean reference (Validating Proofs) and Lean Zulip threads:
https://leanprover-community.github.io/archive/stream/458659-Equational/topic/ofReduceBool.20and.20all.20that.html
https://leanprover-community.github.io/archive/stream/270676-lean4/topic/soundness.20bug.3A.20native_decide.20leakage.html

- `decide +native` admits its result through an axiom and depends "on the correctness of the
  Lean compiler and all definitions with an `@[implemented_by]` attribute."
- "External checkers (lean4checker, comparator) cannot check such proofs, as they do not have
  access to the Lean compiler."
- Since Lean 4.29.0 each such computation introduces its own dedicated axiom. The
  `Lean.trustCompiler` machinery was removed in 4.35.0 (per the docs).
- Mario Carneiro (Zulip, 2025): `native_decide` is a wrapper around `ofReduceBool`, "really
  trusting an unbounded set of extensions to the compiler"; `@[csimp]`, `@[implemented_by]`,
  `@[extern]` all go through it. He showed a constructed proof of `False` this way.
- A 2023 constructed exploit used `IO.getRandomBytes`; lean4#2656 reportedly addressed it.
- **We found no confirmed real-world wrong result from `native_decide`**, only constructed
  examples on those pages.

## C6. A kernel soundness bug that gave an axiom-free proof of `False` (mixed confidence)

GitHub issue leanprover/lean4#14576, "Kernel accepts wrong-structure projections, allowing an
axiom-free proof of False": https://github.com/leanprover/lean4/issues/14576

PAGE-STATED (GitHub issue):
- The repro "proves `False` with no axioms. It does not use `sorry`, `unsafeCast`,
  `debug.skipKernelTC`, `addDeclWithoutChecking`, FFI, or a modified `.olean` file." Output
  says `'boom' does not depend on any axioms`. Run with `lean --trust=0`.
- The repro uses `import Lean`, `meta def`, and `elab ... : command`, so it runs a metaprogram.
- Reported by @kiranandcode on 2026-07-28 while reviewing a Collatz-related repository
  (https://github.com/xrchz/CollatzLean). Fix PR #14577, issue closed 2026-07-28.

SINGLE-SOURCE (oss-security advisory by Jonathan Brossard, 2026-08-02; the GitHub issue is
silent on these): https://openwall.com/lists/oss-security/2026/08/02/1
- Affected: Lean 4 up to and including v4.31.0 and nightlies through 2026-07-27. Fixed in
  nightly-2026-07-29. "No stable release containing the fix has been issued" at that date.
- The advisory describes nested inductives and an expression-hash collision as the mechanism.
- It says the proof was accepted by the Lean kernel and by the Nanoda independent checker.
- It advises re-checking proof artifacts with `--trust=0` on the patched kernel.

**Disagreements between those two sources, not resolved:** the GitHub repro ran on a
4.34.0 nightly while the advisory's affected range ends at v4.31.0; GitHub says "proof of
the Collatz Conjecture", the advisory says "disproving"; only the advisory mentions nested
inductives, the hash collision and Nanoda.

**UNCONFIRMED, do not repeat:** a CVE id (the advisory states none is assigned and that one
is being requested; a search summary gave a specific number, we could not verify it); that
the `comparator` tool is unaffected (not mentioned on any page we read); which stable
release contains the fix.

**Lesson:** an independent second kernel and `#print axioms` showing nothing unusual did not
protect against this, if the advisory is accurate. Statement review, literature check, and a
second, non-Lean line of evidence (here: explicit finite counterexamples checked by plain
code) are not optional.

## C7. Limits of the checkers themselves (PAGE-STATED)

- `lean4checker` replays `.olean` declarations through the kernel and "trusts that the .olean
  files are structurally correct." It is archived, now distributed with Lean as `leanchecker`
  (from v4.28.0 per its README).
- `comparator` (merged into core as `lake comparator` as of v4.35.0, per its README) checks
  that the solution proves the same statement as the challenge, with only permitted axioms,
  accepted by the kernel, optionally also by external kernels. Its README says definition
  holes "must always be checked with an additional (potentially human) verifier."

---

## Rules this repo takes from the above

1. Never call anything verified because Lean accepted it. See `VERIFICATION_PROTOCOL.md`.
2. Verification Lean files: no `native_decide`, no `decide +native`, no `Lean.ofReduceBool`,
   no `@[csimp]`, `@[implemented_by]`, `@[extern]`, no `sorry`, no `axiom`.
3. No `meta`, `elab`, `macro`, `syntax` or `import Lean` metaprogramming in verification
   files (the known kernel bug needed a metaprogram). Review by `grep` before accepting.
4. `#print axioms` must show only the three standard axioms. Record the output.
5. Record the exact Lean and Mathlib versions used. Use a version newer than the fix.
6. Prefer claims that also have a non-Lean certificate that plain code can check
   (explicit finite countermodel tables).
7. Write the statement in plain English next to every formal statement, and test it with
   sanity cases, including cases that must be false.
8. Treat web summaries and agent reports as leads. Read the primary page. Label what we
   could not read.
