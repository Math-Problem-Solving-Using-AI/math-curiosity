# Plan: problems from erdosproblems.com with no prize

Status (2026-11-22): **triage done, 10 dossiers written, no problem attempted.** Start with
[`erdos/REGISTRY.md`](erdos/REGISTRY.md) (queue and procedure), [`erdos/triage-2026-11-22.md`](erdos/triage-2026-11-22.md)
(how the candidates were chosen), [`erdos/RULES.md`](erdos/RULES.md) and [`erdos/README.md`](erdos/README.md)
(sources; the site disallows Claude agents, so only the owner saves its pages).

The owner wants to take part in problems from
[erdosproblems.com](https://www.erdosproblems.com) that carry no prize, one repository each, named
`erdos-<number>`.

## Before a repository is created

1. Read the current entry on the site: statement, status, references, comments. Status changes, so
   record the date.
2. Search the literature and the site's references for a solution or partial results. A problem
   listed as open may already be solved elsewhere. Do not start until this is written down.
3. Check the formal statement (if one exists, for example in a Lean formalization repository) against
   the original wording. Documented misformalizations of Erdős problems exist, see
   `docs/LEAN_CAVEATS.md` section C2. A proof of a misformalized statement answers a different question.
4. Write down ambiguities in the original wording and which reading we take.

## Repository for one problem

Create with `tools/new_problem.sh erdos-<number>`, then:

- `steps/01-statement-and-fidelity.md`: original wording (quoted, with the date and link), our reading,
  ambiguities, formal statement if any, sanity cases that must come out true and false.
- `steps/02-literature.md`: queries, dates, what was found and not found.
- Then computation or proof steps, each with certificates and the verification protocol.
- `STATE.md` queue and `LOOP.md` so autonomous sessions can work on it.

## Principles

- Computer search for counterexamples or small cases is the safest first line of work: a certificate
  can be checked by plain code, with no trust in a prover.
- Never announce a solution. A result carries a label (`docs/VERIFICATION_PROTOCOL.md`), and anything
  above `z3-only` or `model-verified` needs independent review before it leaves the repository.
- Contacting the site's maintainer or an expert is the owner's decision, not an agent's.
