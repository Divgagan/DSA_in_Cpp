#!/usr/bin/env python3
"""Generate an SVG contribution heatmap from recent git commits."""

from __future__ import annotations

import subprocess
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "heatmap.svg"
COLORS = ["#1E293B", "#14532D", "#15803D", "#22C55E", "#86EFAC"]


def git_commit_dates(days: int = 98) -> Counter[str]:
    since = (date.today() - timedelta(days=days)).isoformat()
    try:
        result = subprocess.run(
            ["git", "log", f"--since={since}", "--date=short", "--pretty=%ad"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return Counter()
    return Counter(line.strip() for line in result.stdout.splitlines() if line.strip())


def color_for(count: int) -> str:
    if count <= 0:
        return COLORS[0]
    if count == 1:
        return COLORS[1]
    if count == 2:
        return COLORS[2]
    if count <= 4:
        return COLORS[3]
    return COLORS[4]


def build_svg(counts: Counter[str], days: int = 98) -> str:
    today = date.today()
    start = today - timedelta(days=days - 1)
    cells = []

    for index in range(days):
        current = start + timedelta(days=index)
        week = index // 7
        weekday = current.weekday()
        x = 24 + week * 18
        y = 64 + weekday * 18
        count = counts[current.isoformat()]
        cells.append(
            f'<rect x="{x}" y="{y}" width="12" height="12" rx="2" '
            f'fill="{color_for(count)}"><title>{current.isoformat()}: {count} commits</title></rect>'
        )

    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f'''<svg width="900" height="190" viewBox="0 0 900 190" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title">
  <title id="title">Local DSA contribution heatmap</title>
  <rect width="900" height="190" rx="8" fill="#0B1020"/>
  <text x="24" y="34" fill="#E5E7EB" font-family="Inter, Segoe UI, Arial" font-size="18" font-weight="700">Contribution Heatmap</text>
  <text x="24" y="52" fill="#94A3B8" font-family="Inter, Segoe UI, Arial" font-size="12">Generated {generated} from recent git commits.</text>
  {"".join(cells)}
  <text x="24" y="176" fill="#94A3B8" font-family="Inter, Segoe UI, Arial" font-size="12">Less</text>
  <rect x="60" y="166" width="12" height="12" rx="2" fill="{COLORS[0]}"/>
  <rect x="78" y="166" width="12" height="12" rx="2" fill="{COLORS[1]}"/>
  <rect x="96" y="166" width="12" height="12" rx="2" fill="{COLORS[2]}"/>
  <rect x="114" y="166" width="12" height="12" rx="2" fill="{COLORS[3]}"/>
  <rect x="132" y="166" width="12" height="12" rx="2" fill="{COLORS[4]}"/>
  <text x="154" y="176" fill="#94A3B8" font-family="Inter, Segoe UI, Arial" font-size="12">More</text>
</svg>
'''


def main() -> None:
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(build_svg(git_commit_dates()), encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
