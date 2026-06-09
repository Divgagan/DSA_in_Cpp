#!/usr/bin/env python3
"""
Fetch LeetCode problems using REST API with JWT token
"""
import json
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Installing requests...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# Your JWT token
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMTIyNjM0OTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMTg1NzU4ZWYzZWY0OGM5ZGEzNjI2YTBhNzBhMzI5MDRhYTkwMWMyYzZmYWQ2ZWQ4N2FmMDNiODBlMGVhYjM2Iiwic2Vzc2lvbl91dWlkIjoiNjdkZTU2NjEiLCJpZCI6MTIyNjM0OTMsImVtYWlsIjoiYW1hbmRpd2FrYXI3NDdAZ21haWwuY29tIiwidXNlcm5hbWUiOiJHYWdhbjc0NyIsInVzZXJfc2x1ZyI6IkdhZ2FuNzQ3IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2F2YXRhcnMvYXZhdGFyXzE3MDY5NDgzNjcucG5nIiwicmVmcmVzaGVkX2F0IjoxNzgwODk1Mjc5LCJpcCI6IjI0MDk6NDA5MDpmMDhkOjI4MTI6NDcwOmQ0MGY6OTA3NzphMTgyIiwiaWRlbnRpdHkiOiI5MGRhYTU1MTYwNDI2OWRiY2RjZjIzN2I1Y2M3MDBmMyIsImRldmljZV93aXRoX2lwIjpbImNiNzdmYTAzMjk4N2YzY2U3YzBmNDI3MTQyMjdjYjgyIiwiMjQwOTo0MDkwOmYwOGQ6MjgxMjo0NzA6ZDQwZjo5MDc3OmExODIiXX0.PunYE8CMmpQ7gqYhNI02_P6M_D7L3x6B-a2JLbayab0"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets" / "leetcode_problems"


def fetch_problems():
    """Fetch recent LeetCode submissions using JWT"""
    print("🔄 Fetching LeetCode problems...")
    
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    headers = {
        "Authorization": f"Bearer {JWT_TOKEN}",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com/u/Gagan747/"
    }
    
    # Try to fetch submissions
    try:
        # Fetch from LeetCode REST API
        url = "https://leetcode.com/api/submissions/"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            submissions = response.json()
            print(f"✅ Found {len(submissions)} submissions")
            
            # Save to file
            problems_file = output_dir / "submissions.json"
            problems_file.write_text(json.dumps(submissions, indent=2))
            print(f"✅ Saved to: {problems_file}")
            return submissions
        else:
            print(f"⚠️  API returned: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Alternative: Try the main leetcode-export tool with full cookies")
        return None


def main():
    print("=" * 70)
    print("📥 Fetching LeetCode Problems using JWT Token")
    print("=" * 70)
    
    problems = fetch_problems()
    
    if problems:
        print("\n✅ Problems fetched successfully!")
    else:
        print("\n⚠️  Could not fetch via REST API")
        print("Please provide the full cookie header from Request Headers")


if __name__ == "__main__":
    main()
