"""Build app/index.html from app/template.html, embedding the job history CSV and the sample brief.

Run from the repo root:  python3 app/build.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
html = (root / "app/template.html").read_text()
csv = (root / "data/past-jobs.csv").read_text().strip()
brief = (root / "briefs/sample-harper-ridge.json").read_text().strip()
for name, text in (("CSV", csv), ("brief", brief)):
    if "</" in text:
        raise SystemExit(f"The {name} contains '</', which would break the page's script tag.")
html = html.replace("__SAMPLE_CSV__", csv).replace("__SAMPLE_BRIEF__", brief)
(root / "app/index.html").write_text(html)
print("Wrote app/index.html")
