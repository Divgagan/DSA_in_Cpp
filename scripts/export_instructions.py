#!/usr/bin/env python3
"""
Export LeetCode solved problems to JSON.
Manual alternative: Go to https://leetcode.com/u/Gagan747/
Click "Problems Solved" -> Select "Sort by Date" -> Export/Copy
"""

import json
from pathlib import Path

LEETCODE_USERNAME = "Gagan747"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets"


def generate_export_instructions():
    """Generate instructions for manual export."""
    instructions = {
        "method": "MANUAL EXPORT - Automatic API export has restrictions",
        "steps": [
            "1. Visit: https://leetcode.com/u/Gagan747/",
            "2. Scroll to 'Solved Problems' section",
            "3. Click the problems list",
            "4. Open Browser DevTools (F12)",
            "5. Go to Network tab",
            "6. Refresh the page",
            "7. Look for requests to 'graphql'",
            "8. Find the response with problem data",
            "9. Copy and save as JSON",
            "",
            "EASIER ALTERNATIVE:",
            "- Use LeetCode Export Chrome Extension",
            "- Or manually copy-paste from the Problems page"
        ],
        "sample_problem_structure": {
            "id": "1",
            "title": "Two Sum",
            "titleSlug": "two-sum",
            "difficulty": "Easy",
            "category": "Array",
            "solved_date": "2024-01-15"
        }
    }
    
    output_file = OUTPUT_DIR / "EXPORT_INSTRUCTIONS.json"
    output_file.write_text(json.dumps(instructions, indent=2))
    print("\n📋 Export Instructions:")
    print("\n".join(instructions["steps"]))
    return instructions


def main():
    print("=" * 70)
    print("🔗 LeetCode & GeeksForGeeks Data Export")
    print("=" * 70)
    print("\n⚠️  Note: LeetCode API has rate limits and authentication requirements")
    print("\nOptions:")
    print("1️⃣  AUTOMATIC (if you have Python requests + auth)")
    print("2️⃣  MANUAL EXPORT (fastest method)")
    print("3️⃣  Use LeetCode Export Extension\n")
    
    generate_export_instructions()
    
    print("\n✅ Once you export your problem list, save it as 'solved_problems.json'")
    print("📁 Location: DSA_in_C++/CPP/assets/solved_problems.json")


if __name__ == "__main__":
    main()
