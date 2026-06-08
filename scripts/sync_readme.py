#!/usr/bin/env python3
"""Synchronize generated README sections from repository metrics."""

from __future__ import annotations

import json
import subprocess
from collections import Counter
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
METRICS = ROOT / "assets" / "repository_metrics.json"


def ensure_metrics() -> dict:
    if not METRICS.exists():
        subprocess.run(["python", "scripts/update_stats.py"], cwd=ROOT, check=True)
    return json.loads(METRICS.read_text(encoding="utf-8"))


def replace_block(text: str, name: str, body: str) -> str:
    start = f"<!-- {name}:START -->"
    end = f"<!-- {name}:END -->"
    before, marker, rest = text.partition(start)
    if not marker:
        raise ValueError(f"Missing marker {start}")
    _, marker_end, after = rest.partition(end)
    if not marker_end:
        raise ValueError(f"Missing marker {end}")
    return f"{before}{start}\n{body}\n{end}{after}"


def weekly_activity() -> str:
    since = (date.today() - timedelta(days=13)).isoformat()
    try:
        result = subprocess.run(
            ["git", "log", f"--since={since}", "--date=short", "--pretty=%ad"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        counts = Counter(
            date.fromisoformat(line.strip()).strftime("%a")
            for line in result.stdout.splitlines()
            if line.strip()
        )
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        counts = Counter()

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    lines = ["```text"]
    for day in days:
        count = min(10, counts[day])
        lines.append(f"{day}  {'#' * count}{'-' * (10 - count)}")
    lines.append("```")
    return "\n".join(lines)


def main() -> None:
    metrics = ensure_metrics()
    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "STATS", metrics["stats_markdown"])
    text = replace_block(text, "ROADMAP", metrics["roadmap_markdown"])
    text = replace_block(text, "ACTIVITY", weekly_activity())
    README.write_text(text, encoding="utf-8")
    print("README synchronized.")


if __name__ == "__main__":
    main()
