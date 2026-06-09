#!/usr/bin/env python3
"""
Simple script to help you manually process LeetCode PDFs
"""

from pathlib import Path

PDF_DIR = Path("c:\\Users\\Gagan Diwakar\\OneDrive\\画像\\Desktop\\Git_repo")
PDF_FILES = list(PDF_DIR.glob("Progress - LeetCode*.pdf"))

def main():
    print("=" * 70)
    print("LeetCode PDF Problem Extraction Guide")
    print("=" * 70)
    
    print(f"\nFound {len(PDF_FILES)} PDF files:")
    for i, pdf in enumerate(PDF_FILES, 1):
        size_mb = pdf.stat().st_size / (1024*1024)
        print(f"{i}. {pdf.name} ({size_mb:.2f} MB)")
    
    print("\n" + "=" * 70)
    print("RECOMMENDED NEXT STEPS:")
    print("=" * 70)
    
    print("""
1. EASY METHOD - Copy Problems Manually:
   - Open each PDF file
   - Take screenshots of the problem lists
   - Copy-paste problem names into import_problems.py

2. AUTOMATIC METHOD - Install PDF library:
   Run in PowerShell as Administrator:
   python -m pip install --user pdfplumber
   
   Then run:
   python scripts/extract_pdf_problems.py

3. QUICK ALTERNATIVE:
   - Export from LeetCode profile directly
   - Go to: https://leetcode.com/u/Gagan747/
   - Copy "Solved Problems" section
   - Paste into scripts/import_problems.py

PROBLEM FORMAT:
Problem Name | Difficulty | Category | Link
Example:
Two Sum | Easy | Array | https://leetcode.com/problems/two-sum/

Ready to continue? Let me know!
""")

if __name__ == "__main__":
    main()
