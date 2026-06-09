#!/usr/bin/env python3
"""
Organize LeetCode problems into DSA_in_C++ repo by topic
This creates template files for your solved problems
"""

import json
from pathlib import Path

# Your stats (from what we found)
LEETCODE_STATS = {
    "username": "Gagan747",
    "total_solved": 103,
    "easy": 43,
    "medium": 52,
    "hard": 8,
}

GFG_STATS = {
    "username": "amandiwakar747",
    "total_solved": 31,
}

# Map categories to topics in your repo
CATEGORY_MAP = {
    "Array": "Arrays",
    "String": "Strings",
    "Hash Table": "Hashing",
    "Linked List": "LinkedList",
    "Stack": "Stack",
    "Queue": "Queue",
    "Tree": "Trees",
    "Binary Search Tree": "BST",
    "Trie": "Tries",
    "Heap": "Heap",
    "Graph": "Graphs",
    "Dynamic Programming": "DynamicProgramming",
    "Greedy": "Greedy",
    "Backtracking": "Backtracking",
    "Bit Manipulation": "BitManipulation",
    "Math": "Math",
    "Recursion": "Recursion",
    "Two Pointers": "TwoPointers",
    "Sliding Window": "SlidingWindow",
    "Disjoint Set": "DisjointSet",
    "Segment Tree": "SegmentTree",
}

CPP_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = CPP_DIR / "assets"

def create_problem_template(category, problem_name):
    """Create a template for a problem"""
    return f"""# {problem_name}

## Problem Details
- **Platform**: LeetCode
- **Category**: {category}
- **Difficulty**: 
- **Link**: https://leetcode.com/problems/

## Solution Approach
[Add your approach here]

## Time Complexity
O(?)

## Space Complexity
O(?)

## Code
\`\`\`cpp
// Add your solution code here
\`\`\`

## Notes
[Add any important notes]
"""

def create_stats_file():
    """Create a statistics file"""
    stats = {
        "leetcode": LEETCODE_STATS,
        "geeksforgeeks": GFG_STATS,
        "total_problems": LEETCODE_STATS["total_solved"] + GFG_STATS["total_solved"],
        "last_updated": "2026-06-08",
        "next_steps": [
            "1. Go to https://leetcode.com/u/Gagan747/",
            "2. Copy your solved problems list",
            "3. Paste into import_problems.py",
            "4. Run python import_problems.py to organize by topic"
        ]
    }
    
    stats_file = ASSETS_DIR / "problems_stats.json"
    stats_file.write_text(json.dumps(stats, indent=2), encoding='utf-8')
    print(f"Created: {stats_file}")

def create_import_guide():
    """Create a guide file"""
    guide = """# How to Import Your LeetCode & GFG Problems

## Current Status
- LeetCode: 103 problems solved (43 Easy, 52 Medium, 8 Hard)
- GeeksForGeeks: 31 problems solved

## Next Steps

### Step 1: Export Your Problems
1. Go to your LeetCode profile: https://leetcode.com/u/Gagan747/
2. Scroll to "Solved Problems" section
3. Select all problems (Ctrl+A)
4. Copy the list
5. Paste into a text file

### Step 2: Edit the import script
Edit scripts/import_problems.py and add your problems in this format:
```
Two Sum | Easy | Array | https://leetcode.com/problems/two-sum/
Add Two Numbers | Medium | Linked List | https://leetcode.com/problems/add-two-numbers/
```

### Step 3: Run the import
```bash
python scripts/import_problems.py
```

This will automatically:
- Create folders for each category
- Add problem templates with links
- Organize by difficulty
- Update README files

## File Structure Created
Each problem will have:
- Problem description
- Your solution code
- Approach/explanation
- Complexity analysis
- Links to LeetCode/GFG
"""
    
    guide_file = CPP_DIR / "IMPORT_GUIDE.md"
    guide_file.write_text(guide, encoding='utf-8')
    print(f"Created: {guide_file}")

def create_import_script():
    """Create a reusable import script template"""
    script = """#!/usr/bin/env python3
# Import LeetCode/GFG problems into DSA_in_C++ repo
# Edit the PROBLEMS list below and run: python import_problems.py

from pathlib import Path

# ===== PASTE YOUR PROBLEMS HERE =====
# Format: Problem Name | Difficulty | Category | Link
PROBLEMS = \"\"\"
# Two Sum | Easy | Array | https://leetcode.com/problems/two-sum/
# Add Two Numbers | Medium | Linked List | https://leetcode.com/problems/add-two-numbers/
\"\"\"

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
    problems = [p.strip() for p in PROBLEMS.strip().split('\\n') if p.strip() and not p.startswith('#')]
    
    if not problems:
        print("No problems found! Edit PROBLEMS variable above.")
        return
    
    print(f"Found {len(problems)} problems")
    print("\\nProblems to import:")
    for p in problems[:5]:
        print(f"  - {p}")
    
    print("\\nNext: Create problem files in respective category folders")

if __name__ == "__main__":
    main()
"""
    
    script_file = CPP_DIR / "scripts" / "import_problems.py"
    script_file.write_text(script, encoding='utf-8')
    script_file.chmod(0o755)
    print(f"Created: {script_file}")

def main():
    print("=" * 70)
    print("Setting up LeetCode/GFG Integration")
    print("=" * 70)
    
    ASSETS_DIR.mkdir(exist_ok=True)
    (CPP_DIR / "scripts").mkdir(exist_ok=True)
    
    create_stats_file()
    create_import_guide()
    create_import_script()
    
    print("\n" + "=" * 70)
    print("Setup Complete!")
    print("=" * 70)
    print("\nNext Steps:")
    print("1. Read: IMPORT_GUIDE.md")
    print("2. Edit: scripts/import_problems.py")
    print("3. Run: python scripts/import_problems.py")
    print("\nYour problems will be organized by topic automatically!")

if __name__ == "__main__":
    main()
