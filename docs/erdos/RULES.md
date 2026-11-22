# Rules that bind any contribution to an Erdős problem

Compiled 2026-11-22. Each rule is labeled with where it was read. **The site's own rules were NOT
read** (erdosproblems.com disallows Claude agents in its robots.txt, see `README.md`). Before
anything is posted or submitted, the owner must read the site's FAQ and rules pages and add them
here.

## From the community database (read: `teorth/erdosproblems`, `CONTRIBUTING.md` and `README.md`, commit 8e3d61b)

- **Where to discuss mathematics.** "In general, discussion of Erdős problems should occur on the
  web site for that problem. The issue system here is mostly intended for matters relating to the
  database entries". Detailed mathematical commentary belongs on the problem's page, "which is the
  authoritative venue for it".
- **AI-generated issues** "will, at a bare minimum, need to disclose their use of AI, and will likely
  be closed if they are not contributing a significant amount of value."
- **AI-generated code and sequences.** If AI-generated code gives a sequence that matches no
  existing OEIS entry, "it will be important to independently verify the output of that code".
  Recommended: have the tool do a simplified version first, understand and check it, run sanity
  checks (for example monotonicity). "Asking a large language model to directly generate a
  sequence ... is discouraged".
- **OEIS.** "AI-generated submissions to the OEIS are forbidden"
  (https://oeis.org/wiki/Use_of_AI_for_OEIS_Submissions_is_Forbidden, not read by us). "any
  AI-generated components need to be replaced by human-generated substitutes before submission."
  **So no OEIS submission from this project unless a human redoes the work.**
- **False OEIS matches.** "Term-by-term agreement is not enough". Compare definitions, extend past
  the first agreement, and state offset, empty-object and b=c conventions (issue #356, not read).
- **Status field** is "an *unofficial* crowdsourced classification". When it disagrees with the
  site, the site "should be taken to be the more reliable source".
- **Status definitions** (verbatim, `CONTRIBUTING.md`):
  - "falsifiable": "the problem is open, but if false, can be disproven with a finitary counterexample."
  - "verifiable": "the problem is open, but if true, can be proven with a finitary example."
  - "decidable": "the problem is both falsifiable and verifiable, but not yet solved."
  - "open": "the problem is open and is not known to be either falsifiable or verifiable."
- **Formalized vs solved.** `formalized` = the *statement* is in google-deepmind/formal-conjectures.
  `formal_status` = a *solution* is formalized. They are different things.
- **Help wanted on sequences:** one may open an issue "HELP WANTED: Computing sequence for Erdős
  problem #X".
- **Citation of the database:** "[Erdős problems database](https://github.com/teorth/erdosproblems),
  2025. Maintained by Thomas Bloom and Terence Tao." (see its `CITATIONS.cff`).

## From the saved page (read: the owner's saved copy, content as of about 2026-10-16)

- Each entry says: "When referring to this problem, please use the original sources of Erdős. If
  you wish to acknowledge this website, the recommended citation format is: T. F. Bloom, Erdős
  Problem #N, https://www.erdosproblems.com/N, accessed <date>".
- Proof expositions: "please message a moderator or email" the site (address on the page).
- Proof claims have their own thread per problem (`/forum/thread/N/proof-claims`, not read).

## From robots.txt (read 2026-11-22)

- `Content-Signal: search=yes,ai-train=no,use=reference` for all agents, and `Disallow: /` for
  named AI agents, including Claude-User and ClaudeBot. **Consequence for this project: no Claude
  agent fetches the site. Only the owner saves pages from a browser.**

## Rules this project adds (from the hub's protocol)

1. Never announce a solution. Results carry labels (`../VERIFICATION_PROTOCOL.md`).
2. Do not contact anyone (site, authors, forums). Only the owner decides that.
3. Any computation comes with a certificate that plain code can check, and with a mutation-tested
   verifier. "No counterexample up to N" is reported as exactly that.
4. Disclose AI use in anything that leaves this repository.

## Not read, owner please save from a browser

- https://www.erdosproblems.com/faq
- the forum thread `blog:9` (the 2026-10-06 policy change)
- for each shortlisted problem: its page, `/latex/N`, `/forum/discuss/N`, `/forum/thread/N/proof-claims`
