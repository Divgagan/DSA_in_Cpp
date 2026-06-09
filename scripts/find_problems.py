#!/usr/bin/env python3
"""
Find where the actual problem list is in PDFs
"""

import pdfplumber
from pathlib import Path

PDF_DIR = Path(r"c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo")
pdf_file = list(PDF_DIR.glob("Progress - LeetCode.pdf"))[0]

print(f"Reading: {pdf_file.name}\n")

with pdfplumber.open(pdf_file) as pdf:
    print(f"Total pages: {len(pdf.pages)}\n")
    
    # Check all pages for problem lists
    for page_num, page in enumerate(pdf.pages, 1):
        text = page.extract_text()
        
        # Look for pattern with numbers and problem names
        if any(word in text.lower() for word in ["two sum", "add two", "longest", "median"]):
            print(f"\n✓ FOUND problem list on page {page_num}!")
            print("=" * 70)
            print(text[:1500])
            print("=" * 70)
            break
        elif any(char.isdigit() for char in text) and len(text) > 100:
            # Show pages that have content
            if "1." in text or "problem" in text.lower():
                print(f"\nPage {page_num}: Contains potential problem data")
                print(text[:500] + "...\n")
