#!/usr/bin/env python3
"""
Debug PDF content extraction
"""

import pdfplumber
from pathlib import Path

PDF_DIR = Path(r"c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo")
pdf_file = list(PDF_DIR.glob("Progress - LeetCode.pdf"))[0]

print(f"Reading: {pdf_file.name}\n")

with pdfplumber.open(pdf_file) as pdf:
    print(f"Total pages: {len(pdf.pages)}\n")
    
    # Show first page content
    page = pdf.pages[0]
    text = page.extract_text()
    
    print("=" * 70)
    print("FIRST PAGE CONTENT (first 2000 chars):")
    print("=" * 70)
    print(text[:2000])
    print("\n" + "=" * 70)
    print("SHOWING TABLE DATA IF AVAILABLE:")
    print("=" * 70)
    
    # Try to extract tables
    tables = page.extract_tables()
    if tables:
        print(f"Found {len(tables)} tables on page 1")
        for i, table in enumerate(tables):
            print(f"\nTable {i+1}:")
            for j, row in enumerate(table[:10]):  # First 10 rows
                print(f"  {row}")
