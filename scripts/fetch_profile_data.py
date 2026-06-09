#!/usr/bin/env python3
"""Fetch solved problems from LeetCode and GeeksForGeeks profiles."""

import json
import sys
from pathlib import Path
import subprocess

try:
    import requests
except ImportError:
    print("❌ Error: 'requests' module not found")
    print("Install it with: pip install requests")
    sys.exit(1)

# Configuration
LEETCODE_USERNAME = "Gagan747"
GFG_USERNAME = "amandiwakar747"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets"


def fetch_leetcode_data():
    """Fetch LeetCode solved problems using GraphQL API."""
    print(f"🔄 Fetching LeetCode data for user: {LEETCODE_USERNAME}")
    
    url = "https://leetcode.com/graphql"
    query = """
    query getUserProfile($username: String!) {
        allQuestionsCount {
            difficulty
            count
        }
        matchedUser(username: $username) {
            username
            profile {
                realName
                userAvatar
            }
            submissionCalendar
            submitStats {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
    }
    """
    
    variables = {"username": LEETCODE_USERNAME}
    
    try:
        response = requests.post(
            url,
            json={"query": query, "variables": variables},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        if "errors" in data:
            print(f"❌ LeetCode API Error: {data['errors']}")
            return None
        
        print("✅ LeetCode data fetched successfully")
        return data.get("data", {})
    except Exception as e:
        print(f"❌ Error fetching LeetCode data: {e}")
        return None


def fetch_gfg_data():
    """Fetch GeeksForGeeks profile data (basic info via web scraping)."""
    print(f"🔄 Fetching GeeksForGeeks data for user: {GFG_USERNAME}")
    
    try:
        url = f"https://www.geeksforgeeks.org/profile/{GFG_USERNAME}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Note: GFG doesn't provide direct JSON export
        # This is a placeholder - actual data extraction would need parsing
        print("✅ GeeksForGeeks profile accessible")
        return {
            "username": GFG_USERNAME,
            "profile_url": url,
            "note": "GFG doesn't provide direct API access. Use browser dev tools to export problems."
        }
    except Exception as e:
        print(f"❌ Error fetching GeeksForGeeks data: {e}")
        return None


def save_data(leetcode_data, gfg_data):
    """Save fetched data to JSON files."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    if leetcode_data:
        lc_file = OUTPUT_DIR / "leetcode_profile.json"
        lc_file.write_text(json.dumps(leetcode_data, indent=2))
        print(f"✅ Saved LeetCode data to: {lc_file}")
    
    if gfg_data:
        gfg_file = OUTPUT_DIR / "gfg_profile.json"
        gfg_file.write_text(json.dumps(gfg_data, indent=2))
        print(f"✅ Saved GFG data to: {gfg_file}")


def main():
    print("=" * 60)
    print("🚀 Fetching Profile Data from LeetCode & GeeksForGeeks")
    print("=" * 60)
    
    lc_data = fetch_leetcode_data()
    gfg_data = fetch_gfg_data()
    
    if lc_data or gfg_data:
        save_data(lc_data, gfg_data)
        print("\n✅ Data fetch complete!")
    else:
        print("\n❌ Failed to fetch data from both platforms")
        sys.exit(1)


if __name__ == "__main__":
    main()
