"""Extract the entries of a saved erdosproblems.com/prizes/0 page into JSON.

LOCAL ONLY (this folder is excluded from git). Input is the HTML the owner saved from a browser.
Math in statements is NOT LaTeX: the saved page only keeps the site's spoken-text rendering of each
formula (aria-label of mjx-speech), shown between double brackets. Good enough for triage, NOT for
formalization. Get the LaTeX from the problem's page (/latex/<n>) or from a database.

Usage: python extract_prizes0.py "<saved.html>" out.json
"""
import html as H
import json
import re
import sys


def speech(m):
    s = re.search(r'<mjx-speech[^>]*aria-label="([^"]*)"', m.group(0))
    return " [[" + (H.unescape(s.group(1)).replace(", math", "") if s else "MATH") + "]] "


def text(x):
    x = re.sub(r"<mjx-container.*?</mjx-container>", speech, x, flags=re.S)
    x = re.sub(r"<style.*?</style>|<script.*?</script>", "", x, flags=re.S)
    x = re.sub(r"<br\s*/?>", "\n", x)
    x = re.sub(r"<li[^>]*>", "\n- ", x)
    x = re.sub(r"<[^>]+>", " ", x)
    x = H.unescape(x)
    x = re.sub(r"[ \t\r\f\v]+", " ", x)
    return re.sub(r"\n\s*\n+", "\n", x).strip()


def main():
    src, out = sys.argv[1], sys.argv[2]
    t = open(src, encoding="utf-8", errors="replace").read()
    saved_from = re.search(r"saved from url=\(\d+\)(\S+)", t)
    boxes = [m.start() for m in re.finditer(r'<div class="problem-box">', t)] + [len(t)]
    rows = []
    for a, b in zip(boxes, boxes[1:]):
        blk = t[a:b]
        n = re.search(r'<div id="problem_id">\s*<a href="https://www\.erdosproblems\.com/(\d+)">#\1</a>', blk)
        if not n:
            continue
        st = re.search(r'<div id="content">(.*?)</div>\s*<div id="problem_id">', blk, re.S)
        tags = re.search(r'<div id="tags">(.*?)</div>', blk, re.S)
        add = re.search(r'<div class="problem-additional-text">(.*?)<div id="bib-container', blk, re.S)
        fm = re.search(r"Formalised statement\?\s*</span>\s*<span>(.*?)</span>\s*</div>", blk, re.S)
        react = {}
        for r in re.finditer(r'data-reaction-type="(\w+)">(.*?)</div>\s*(?=<div class="problem-info-data-row|</div>)',
                             blk, re.S):
            react[r.group(1)] = re.findall(r'/user/([^"]+)"', r.group(2))
        num = lambda label: (lambda m: int(m.group(1)) if m else None)(re.search(label + r"\s*\((\d+)\)", blk))
        edited = re.search(r"This page was last edited ([^<]+?)\.", blk)
        rows.append({
            "number": int(n.group(1)),
            "statement": text(st.group(1)) if st else None,
            "tags": [x.strip() for x in re.findall(r">([^<]+)</a>", tags.group(1))] if tags else [],
            "additional_text": text(add.group(1)) if add else None,
            "formalised_statement": ("yes" if fm and "Yes" in fm.group(1) else "no" if fm else "unknown"),
            "formalised_link": (re.search(r'href="([^"]+)"', fm.group(1)).group(1) if fm and "href" in fm.group(1) else None),
            "oeis": re.findall(r"oeis\.org/(A\d+)", blk),
            "comments": num("Comments"),
            "proof_claims": num("Proof claims"),
            "proof_expositions": num("Proof expositions"),
            "last_edited": edited.group(1).strip() if edited else None,
            "reactions": react,
            "url": f"https://www.erdosproblems.com/{n.group(1)}",
        })
    json.dump({"saved_from": saved_from.group(1) if saved_from else None, "problems": rows},
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("problems extracted:", len(rows), "| saved from:", saved_from.group(1) if saved_from else None)


if __name__ == "__main__":
    main()
