#!/usr/bin/env python3
"""Generate repository metrics for the DSA in C++ portfolio repository."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

TOPICS = {
    "Arrays": 50,
    "Strings": 40,
    "LinkedList": 30,
    "Stack": 25,
    "Queue": 20,
    "Trees": 45,
    "BST": 25,
    "Heap": 25,
    "Hashing": 35,
    "Recursion": 30,
    "Backtracking": 30,
    "Greedy": 35,
    "BinarySearch": 35,
    "SlidingWindow": 25,
    "TwoPointers": 25,
    "BitManipulation": 25,
    "Graphs": 60,
    "DynamicProgramming": 75,
    "Tries": 20,
    "SegmentTree": 25,
    "DisjointSet": 20,
    "Math": 35,
    "PatternWise": 50,
    "ContestProblems": 50,
    "General": 30,
}


def is_solution(path: Path) -> bool:
    return path.suffix == ".cpp" and path.name != "sample_solution.cpp"


def count_topic_solutions(topic: str) -> int:
    topic_dir = ROOT / topic
    if not topic_dir.exists():
        return 0
    return sum(1 for path in topic_dir.rglob("*.cpp") if is_solution(path))


def progress_bar(value: int, target: int, width: int = 10) -> str:
    percent = 0 if target == 0 else min(100, round((value / target) * 100))
    filled = min(width, round((percent / 100) * width))
    return f"`{'█' * filled}{'░' * (width - filled)}` {percent}%"


def collect_metrics() -> dict:
    topic_rows = []
    total_solved = 0
    total_target = 0

    for topic, target in TOPICS.items():
        solved = count_topic_solutions(topic)
        total_solved += solved
        total_target += target
        topic_rows.append(
            {
                "topic": topic,
                "status": "Done" if solved >= target else "In Progress",
                "solved": solved,
                "target": target,
                "progress": progress_bar(solved, target),
            }
        )

    cpp_files = list(ROOT.rglob("*.cpp"))
    markdown_files = list(ROOT.rglob("*.md"))
    completion = 0 if total_target == 0 else round((total_solved / total_target) * 100)

    return {
        "generated_on": date.today().isoformat(),
        "topics": len(TOPICS),
        "cpp_files": len(cpp_files),
        "markdown_files": len(markdown_files),
        "total_solved": total_solved,
        "total_target": total_target,
        "completion": completion,
        "topic_rows": topic_rows,
    }


def render_stats(metrics: dict) -> str:
    return "\n".join(
        [
            "| Metric | Value |",
            "|---|---:|",
            f"| Total topic folders | {metrics['topics']} |",
            f"| C++ solution files | {metrics['cpp_files']} |",
            f"| Markdown guides | {metrics['markdown_files']} |",
            f"| Completion | {metrics['completion']}% |",
            f"| Last generated | {metrics['generated_on']} |",
        ]
    )


def render_roadmap(metrics: dict) -> str:
    lines = ["| Topic | Status | Solved | Target | Progress |", "|---|---|---:|---:|---|"]
    for row in metrics["topic_rows"]:
        lines.append(
            f"| {row['topic']} | {row['status']} | {row['solved']} | "
            f"{row['target']} | {row['progress']} |"
        )
    return "\n".join(lines)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    metrics = collect_metrics()
    metrics["stats_markdown"] = render_stats(metrics)
    metrics["roadmap_markdown"] = render_roadmap(metrics)
    (ASSETS / "repository_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(f"Generated metrics for {metrics['topics']} topics and {metrics['cpp_files']} C++ files.")


if __name__ == "__main__":
    main()
