"""Show everything we hold locally about one Erdős problem, with the source of each part.

Sources (see README.md): the saved prizes page (via data/prizes0-*.json, local only), the community
database teorth/erdosproblems (data/problems.yaml) and google-deepmind/formal-conjectures (the Lean
file, whose docstrings usually carry the statement in LaTeX). Clone both repositories into
../../../_external/ (next to the problem repositories) or pass their paths.

Usage: python show_problem.py N [--db PATH_TO_problems.yaml] [--fc PATH_TO_formal-conjectures]
"""
import argparse
import json
import re
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
EXT = HERE.parent.parent.parent / "_external"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("--db", default=str(EXT / "erdosproblems" / "data" / "problems.yaml"))
    ap.add_argument("--fc", default=str(EXT / "formal-conjectures"))
    ap.add_argument("--page", default=str(sorted((HERE / "data").glob("prizes0-*.json"))[-1]))
    a = ap.parse_args()

    page = {p["number"]: p for p in json.load(open(a.page, encoding="utf-8"))["problems"]}
    db = {int(p["number"]): p for p in yaml.safe_load(open(a.db, encoding="utf-8"))}
    n = a.n
    print(f"# Erdős problem {n}\n")
    d = db.get(n)
    print("## Database (teorth/erdosproblems)")
    if d:
        print(json.dumps({k: v for k, v in d.items() if k != "number"}, ensure_ascii=False, indent=1))
    else:
        print("not in database")
    p = page.get(n)
    print(f"\n## Saved page ({Path(a.page).name}; content as of about 2026-10-16; math is screen-reader text)")
    if p:
        print("STATEMENT:", p["statement"])
        print("NOTES:", p["additional_text"])
        print("tags:", p["tags"], "| oeis:", p["oeis"], "| comments:", p["comments"],
              "| proof claims:", p["proof_claims"], "| formalised:", p["formalised_statement"])
        print("reaction counts:", {k: len(v) for k, v in p["reactions"].items()})
    else:
        print("not on the saved page (it has a prize, or the number is wrong)")
    lean = Path(a.fc) / "FormalConjectures" / "ErdosProblems" / f"{n}.lean"
    print(f"\n## formal-conjectures: {lean.name}")
    if lean.exists():
        src = lean.read_text(encoding="utf-8")
        src = re.sub(r"\A/-\nCopyright.*?-/\n", "", src, flags=re.S)  # drop the license header
        print(src)
    else:
        print("no Lean file")


if __name__ == "__main__":
    main()
