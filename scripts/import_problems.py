#!/usr/bin/env python3
# Import LeetCode/GFG problems into DSA_in_C++ repo
# Edit the PROBLEMS list below and run: python import_problems.py

from pathlib import Path

# ===== PASTE YOUR PROBLEMS HERE =====
# Format: Problem Name | Difficulty | Category | Link
PROBLEMS = """
# Two Sum | Easy | Array | https://leetcode.com/problems/two-sum/
# Add Two Numbers | Medium | Linked List | https://leetcode.com/problems/add-two-numbers/
"""

CATEGORY_MAP = {
    "Array": "Arrays",
    "String": "Strings",
    "Hash Table": "Hashing",
    "Linked List": "LinkedList",
    "Stack": "Stack",
    "Tree": "Trees",
    "Graph": "Graphs",
    "Dynamic Programming": "DynamicProgramming",
    "Greedy": "Greedy",
    "Backtracking": "Backtracking",
    "Two Pointers": "TwoPointers",
    "Sliding Window": "SlidingWindow",
}

def main():
    print("Importing problems...")
    problems = [p.strip() for p in PROBLEMS.strip().split('\n') if p.strip() and not p.startswith('#')]
    
    if not problems:
        print("No problems found! Edit PROBLEMS variable above.")
        return
    
    print(f"Found {len(problems)} problems")
    print("\nProblems to import:")
    for p in problems[:5]:
        print(f"  - {p}")
    
    print("\nNext: Create problem files in respective category folders")

if __name__ == "__main__":
    main()
