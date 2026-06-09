#!/usr/bin/env python3
"""Fetch detailed solved problems from LeetCode with GraphQL."""

import json
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ Error: 'requests' module not found")
    print("Install it with: pip install requests")
    sys.exit(1)

LEETCODE_USERNAME = "Gagan747"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets"


def fetch_leetcode_problems():
    """Fetch LeetCode solved problems list using GraphQL."""
    print(f"🔄 Fetching LeetCode solved problems for: {LEETCODE_USERNAME}")
    
    url = "https://leetcode.com/graphql"
    
    # Query to get user's solved problems
    query = """
    query userProfileQuestions($username: String!) {
        allQuestionsCount {
            difficulty
            count
        }
        userPublicProfile(username: $username) {
            username
            name
            reputation
            solutionCount
            problemsSolvedBeatsStats {
                difficulty
                percentage
            }
        }
        recentAcSubmissionList(username: $username, limit: 100) {
            id
            title
            titleSlug
            timestamp
            statusDisplay
        }
    }
    """
    
    variables = {"username": LEETCODE_USERNAME}
    
    try:
        response = requests.post(
            url,
            json={"query": query, "variables": variables},
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()
        data = response.json()
        
        if "errors" in data:
            print(f"⚠️  LeetCode API Note: {data['errors'][0].get('message', 'Unknown error')}")
            return None
        
        result = data.get("data", {})
        print("✅ LeetCode problems fetched successfully")
        return result
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def fetch_gfg_data_details():
    """Fetch GeeksForGeeks profile with attempted problem list."""
    print("🔄 Fetching GeeksForGeeks profile details...")
    
    try:
        url = f"https://www.geeksforgeeks.org/api/profile/{GFG_USERNAME}"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✅ GFG data fetched")
            return response.json()
        else:
            # Fallback to basic info
            print(f"⚠️  GFG API returned {response.status_code}, using basic info")
            return None
    except Exception as e:
        print(f"⚠️  GFG fetch: {e}")
        return None


GFG_USERNAME = "amandiwakar747"


def save_problems(lc_data, gfg_data):
    """Save problems to JSON file."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    problems_file = OUTPUT_DIR / "solved_problems.json"
    
    combined_data = {
        "leetcode": lc_data or {},
        "geeksforgeeks": gfg_data or {},
        "timestamp": "June 8, 2026",
        "instructions": "Use this data to populate your DSA_in_C++ repository with solved problems"
    }
    
    problems_file.write_text(json.dumps(combined_data, indent=2))
    print(f"✅ Saved to: {problems_file}")


def main():
    print("=" * 70)
    print("📊 Fetching Detailed Problem Lists from LeetCode & GeeksForGeeks")
    print("=" * 70)
    
    lc_data = fetch_leetcode_problems()
    gfg_data = fetch_gfg_data_details()
    
    save_problems(lc_data, gfg_data)
    
    # Show summary
    if lc_data:
        print("\n📈 LeetCode Summary:")
        if "recentAcSubmissionList" in lc_data:
            problems = lc_data["recentAcSubmissionList"]
            print(f"   Recent solved problems: {len(problems)}")
            if problems:
                print("   Latest problems:")
                for p in problems[:5]:
                    print(f"   - {p.get('title', 'Unknown')}")
    
    print("\n✅ Data saved! Check 'assets/solved_problems.json' for details")
    print("Next: Use this data to populate your repo by topic")


if __name__ == "__main__":
    main()
