"""Spot-check docs/erdos/data/prizes0-*.json against the saved HTML, by a DIFFERENT method.

extract_prizes0.py uses regular expressions on the whole file. This script cuts out the block of
each sampled entry and walks it with Python's html.parser (an event-based HTML parser), collecting
the same fields independently, then compares field by field.

Fields compared: problem number, tags, "Formalised statement?" yes/no and link, OEIS numbers,
comment / proof-claim / proof-exposition counts, reaction user lists, and the statement's plain
words (math replaced by a placeholder in both, since the math is screen-reader text).

Usage: python spotcheck_extraction.py SAVED.html EXTRACTED.json N_SAMPLES SEED
LOCAL ONLY, like the rest of docs/erdos/.
"""
import json
import random
import re
import sys
from html.parser import HTMLParser


class Entry(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []            # open tags with (tag, attrs)
        self.in_math = 0
        self.section = None        # 'content' | 'tags' | 'label' | 'value' | 'reaction'
        self.number = None
        self.tags = []
        self.statement = []
        self.labels = []           # (label text, [hrefs], text) for problem-info-data-row
        self.counts = {}
        self.reactions = {}
        self._row = None
        self._react = None
        self._span_text = []
        self._first_content_done = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.stack.append((tag, a))
        if tag == "mjx-container":
            self.in_math += 1
            if self.section == "content":
                self.statement.append(" MATH ")
        if tag == "div" and a.get("id") == "content" and not self._first_content_done:
            self.section = "content"
        if tag == "div" and a.get("id") == "tags":
            self.section = "tags"
        if tag == "a" and self.section is None and a.get("href", "").startswith("https://www.erdosproblems.com/") \
                and self.number is None and re.fullmatch(r"https://www\.erdosproblems\.com/\d+", a.get("href", "")):
            self._num_href = a["href"]
        if tag == "div" and "problem-info-data-row" in (a.get("class") or ""):
            self._row = {"label": "", "hrefs": [], "text": ""}
            if a.get("data-reaction-type"):
                self._react = a["data-reaction-type"]
                self.reactions[self._react] = []
        if self._row is not None and tag == "a":
            self._row["hrefs"].append(a.get("href", ""))
            if self._react and "/user/" in a.get("href", ""):
                self.reactions[self._react].append(a["href"].split("/user/")[1])
        if tag == "span":
            self._span_text = []

    def handle_endtag(self, tag):
        while self.stack:
            t, a = self.stack.pop()
            if t == "mjx-container":
                self.in_math -= 1
            if t == "div" and a.get("id") == "content" and self.section == "content":
                self.section = None
                self._first_content_done = True
            if t == "div" and a.get("id") == "tags" and self.section == "tags":
                self.section = None
            if t == "div" and "problem-info-data-row" in (a.get("class") or "") and self._row is not None:
                self.labels.append(self._row)
                self._row = None
                self._react = None
            if t == tag:
                break

    def handle_data(self, data):
        if self.in_math:
            return
        if self.section == "content":
            self.statement.append(data)
        elif self.section == "tags" and self.stack and self.stack[-1][0] == "a":
            self.tags.append(data.strip())
        if self._row is not None:
            self._row["text"] += data
        m = re.fullmatch(r"\s*(Comments|Proof claims|Proof expositions) \((\d+)\)\s*", data)
        if m:
            self.counts[m.group(1)] = int(m.group(2))
        m = re.fullmatch(r"#(\d+)", data.strip())
        if m and self.number is None:
            self.number = int(m.group(1))


def words(s):
    s = re.sub(r"\[\[.*?\]\]", " MATH ", s or "", flags=re.S)
    return re.findall(r"[A-Za-z]+", s)


def main():
    html_path, json_path, n, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    t = open(html_path, encoding="utf-8", errors="replace").read()
    rows = {r["number"]: r for r in json.load(open(json_path, encoding="utf-8"))["problems"]}
    starts = [m.start() for m in re.finditer(r'<div class="problem-box">', t)] + [len(t)]
    print("problem boxes in HTML:", len(starts) - 1, "| entries in JSON:", len(rows))
    sample = random.Random(seed).sample(range(len(starts) - 1), n)
    bad = 0
    for k in sorted(sample):
        p = Entry()
        p.feed(t[starts[k]:starts[k + 1]])
        r = rows.get(p.number)
        problems = []
        if r is None:
            problems.append("number not in JSON")
        else:
            if p.tags != r["tags"]:
                problems.append(f"tags {p.tags} vs {r['tags']}")
            fm = next((x for x in p.labels if "Formalised statement?" in x["text"]), None)
            fm_yes = "yes" if fm and "Yes" in fm["text"] else "no" if fm else "unknown"
            if fm_yes != r["formalised_statement"]:
                problems.append(f"formalised {fm_yes} vs {r['formalised_statement']}")
            link = next((h for h in (fm["hrefs"] if fm else []) if "formal-conjectures" in h), None)
            if link != r["formalised_link"]:
                problems.append(f"formal link {link} vs {r['formalised_link']}")
            oe = next((x for x in p.labels if x["text"].strip().startswith("OEIS")), None)
            oeis = [h.split("oeis.org/")[1] for h in (oe["hrefs"] if oe else []) if "oeis.org/A" in h]
            if sorted(set(oeis)) != sorted(set(r["oeis"])):
                problems.append(f"oeis {oeis} vs {r['oeis']}")
            for key, field in (("Comments", "comments"), ("Proof claims", "proof_claims"),
                               ("Proof expositions", "proof_expositions")):
                if p.counts.get(key) != r[field]:
                    problems.append(f"{field} {p.counts.get(key)} vs {r[field]}")
            for rt, users in p.reactions.items():
                if users != r["reactions"].get(rt, []):
                    problems.append(f"reaction {rt} {users} vs {r['reactions'].get(rt)}")
            w1 = words(" ".join(p.statement).replace(" MATH ", " [[m]] "))
            w2 = words(r["statement"])
            if w1 != w2:
                problems.append(f"statement words differ: {' '.join(w1)[:120]!r} vs {' '.join(w2)[:120]!r}")
        bad += bool(problems)
        print(f"#{p.number}: {'OK' if not problems else 'MISMATCH'}"
              + ("" if not problems else " | " + " | ".join(problems)))
    print(f"{n} sampled, {bad} with mismatches")


if __name__ == "__main__":
    main()
