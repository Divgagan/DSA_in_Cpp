#!/usr/bin/env python3
"""
Simple script to add LeetCode/GFG problems to DSA repo
Just paste your problem names here and run!
"""

import json
from pathlib import Path

# ===== PASTE YOUR PROBLEMS HERE =====
# Format: "Problem Name | Difficulty | Link"

LEETCODE_PROBLEMS = """
Two Sum | Easy | https://leetcode.com/problems/two-sum/
Add Two Numbers | Medium | https://leetcode.com/problems/add-two-numbers/
Longest Substring Without Repeating Characters | Medium | https://leetcode.com/problems/longest-substring-without-repeating-characters/
Median of Two Sorted Arrays | Hard | https://leetcode.com/problems/median-of-two-sorted-arrays/
Palindrome Number | Easy | https://leetcode.com/problems/palindrome-number/
Container With Most Water | Medium | https://leetcode.com/problems/container-with-most-water/
"""

# Copy-paste your full list from your LeetCode profile
# Just follow the format above

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets"

def parse_problems(text):
    """Parse problem list"""
    problems = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 2:
            problems.append({
                'name': parts[0],
                'difficulty': parts[1] if len(parts) > 1 else 'Unknown',
                'link': parts[2] if len(parts) > 2 else ''
            })
    return problems

def main():
    problems = parse_problems(LEETCODE_PROBLEMS)
    
    output_file = OUTPUT_DIR / "manual_problems.json"
    output_file.write_text(json.dumps({
        'leetcode': problems,
        'total': len(problems),
        'instructions': 'Edit the script above to add more problems'
    }, indent=2))
    
    print(f"✅ Found {len(problems)} problems")
    print(f"✅ Saved to: {output_file}")
    
    # Show preview
    for p in problems[:3]:
        print(f"  - {p['name']} ({p['difficulty']})")

if __name__ == "__main__":
    main()
