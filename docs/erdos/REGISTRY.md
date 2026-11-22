# Registry of Erdős problems to attempt later

Problems are **registered** here so they can be worked on one at a time in later sessions. **None has
been attempted.** Each row says what is known, what the first concrete step is, and what blocks it.
Sources and method: [`triage-2026-11-22.md`](triage-2026-11-22.md). Rules: [`RULES.md`](RULES.md).

Status values: `registered` (in the triage list only) → `dossier` (dossier written) → `ready` (owner
review done, nothing blocks) → `in progress` (a repository `erdos-<n>` exists) → `done` (result
recorded with its label). `closed` = not worth attempting (already solved or too hard), kept for the record.

## Queue (take the first item that is not blocked)

| Order | # | Status | Verdict | Next action | Blocked by |
|-------|---|--------|---------|-------------|------------|
| 1 | [585](dossiers/585.md) | dossier | `PURSUE` | Owner glance at the site page (0 comments). Then start `erdos-585`: checker for "two edge-disjoint cycles on the same vertex set", sanity g(4) = 6, g(5) = 9, then small n | owner OK to create the repository |
| 2 | [642](dossiers/642.md) | dossier | `PURSUE` | Read the 4 site comments. Check `Walk.IsChord` in Mathlib. Start `erdos-642`: cycle/chord checker, sanity f(4) = 6, f(5) = 9, then small n | owner OK; 4 site comments unread |
| 3 | [151](dossiers/151.md) | dossier | `PURSUE-AFTER-REVIEW` | Owner reads the site's proof claim and comments. If still open: all graphs n <= 10 against n - H(n) | the unread proof claim |
| 4 | [614](dossiers/614.md) | dossier | `PURSUE-AFTER-REVIEW` | Re-derive the forbidden families F_3, F_4 by brute force and compare with the unreviewed note. Then SAT for f(n,3), n <= 20 | owner reads the site comment |
| 5 | [1094](dossiers/1094.md) | dossier | `PURSUE-AFTER-REVIEW` | Owner reads ELS93 (Math. Comp. 1993) for its search range. Then a certified search with one witness prime per (n,k) | ELS93 range unknown |
| 6 | candidates below | registered | - | Write dossiers (literature check first), in this order: 902, 883, 1189, 319, 404, 938, 885, 373, 624, 317 | none |

## Closed (kept so they are not redone)

| # | Verdict | Why | What could still be reported (owner decides, nothing is announced) |
|---|---------|-----|----------------------------------------------------------------------|
| [887](dossiers/887.md) | `ALREADY-SOLVED` + `UNCLEAR-STATEMENT` | "is 4 best possible": no (five divisors infinitely often, Lean proof linked from formal-conjectures) | The saved notes state a C = 1 result that cannot hold. Check the live page first |
| [866](dossiers/866.md) | `ALREADY-SOLVED` (k <= 4) | g_3 = 1, g_4 = 3 (van Doorn, arXiv 2605.00040) | Notes as saved give "g_4 <= 2032" and mix two definitions. Possible Lean statement for formal-conjectures issue #990 |
| [1055](dossiers/1055.md) | `ALREADY-SOLVED` (computational part) | OEIS A005113 lists p_1 to p_19 | nothing |
| [340](dossiers/340.md) | `TOO-HARD` | 33 checked against 10^5 terms, n^3 growth | nothing |
| [556](dossiers/556.md) | `TOO-HARD` | first open case R_3(C_9) <= 33 is a hard Ramsey computation | statement lacks "n >= 4" (already noted by formal-conjectures) |

## Next candidates for dossiers (registered, from the cheap pass)

One line each, written by the cheap-pass subagents and **not yet checked**. The full list of 93 is in
the triage file.

| # | Kind | What would be computed |
|---|------|------------------------|
| [902](https://www.erdosproblems.com/902) | i | Schütte tournaments: small tournaments where every 4-set is dominated, giving upper bounds on f(4) (OEIS A362137) |
| [883](https://www.erdosproblems.com/883) | i | Coprime graph on large A ⊆ [n]: does it contain all short odd cycles? Small-n counterexample search |
| [1189](https://www.erdosproblems.com/1189) | ii | Irreducible covering sets of size k: counts, extreme moduli, for k <= 7 |
| [319](https://www.erdosproblems.com/319) | ii | Largest A ⊆ [N] with a signed reciprocal sum 0 and no proper zero sub-sum, N <= 30 |
| [404](https://www.erdosproblems.com/404) | i | f(2,2): highest power of 2 dividing a sum of distinct factorials (known <= 254) |
| [938](https://www.erdosproblems.com/938) | i | Three consecutive powerful numbers in arithmetic progression, search to 10^18 |
| [885](https://www.erdosproblems.com/885) | i | Five integers whose factor-difference sets share five elements (k <= 4 known) |
| [373](https://www.erdosproblems.com/373) | i | n! as a product of smaller factorials, k >= 3 factors, beyond the known solutions |
| [624](https://www.erdosproblems.com/624) | ii | H(n) for n <= 9 by SAT (subset-to-element maps) |
| [317](https://www.erdosproblems.com/317) | ii | Smallest nonzero signed harmonic sum, exact values to n ≈ 35 |

## How to start an attempt (procedure for a later session)

1. **Owner:** read the problem's live page, its comments and proof claims, and save them from a
   browser into `source/` (local only). Agents must not fetch erdosproblems.com (`README.md`).
2. **Owner:** approve the repository name `erdos-<n>` (and create it on GitHub when ready).
3. `tools/new_problem.sh erdos-<n>` from the hub.
4. `steps/01-statement-and-fidelity.md`: copy the dossier's statement, reading, ambiguities and Lean
   comparison. Add the LaTeX from the saved `/latex/<n>` page.
5. `steps/02-literature.md`: copy the dossier's literature section, then redo the search (it ages fast).
6. `steps/03-...`: write the checker first, with the dossier's sanity cases as tests. A mutation test
   must show the checker can fail.
7. Computation steps: save state and resume (`../LESSONS.md`), store certificates, and verify them with an
   independent verifier. "Nothing found up to N" is recorded as exactly that.
8. Update this registry (status), the hub README and `../ERDOS_PLAN.md`. Never announce. Anything
   leaving the repository is the owner's decision and discloses AI use (`RULES.md`).
