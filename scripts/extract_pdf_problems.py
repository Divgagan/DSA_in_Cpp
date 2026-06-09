#!/usr/bin/env python3
"""
Extract LeetCode problems from PDF progress reports
"""
import sys
from pathlib import Path

# Try to use pdfplumber or PyPDF2
try:
    import pdfplumber
    PDF_LIB = "pdfplumber"
except ImportError:
    try:
        from PyPDF2 import PdfReader
        PDF_LIB = "PyPDF2"
    except ImportError:
        PDF_LIB = None

PDF_DIR = Path("c:\\Users\\Gagan Diwakar\\OneDrive\\画像\\Desktop\\Git_repo")
PDF_FILES = list(PDF_DIR.glob("Progress - LeetCode*.pdf"))

def extract_with_pdfplumber(pdf_path):
    """Extract text using pdfplumber"""
    problems = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                print(f"✓ Extracted from page: {len(text)} chars")
                problems.append(text)
    except Exception as e:
        print(f"Error with pdfplumber: {e}")
    return problems

def extract_with_pypdf(pdf_path):
    """Extract text using PyPDF2"""
    problems = []
    try:
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                print(f"✓ Extracted page {page_num + 1}: {len(text)} chars")
                problems.append(text)
    except Exception as e:
        print(f"Error with PyPDF2: {e}")
    return problems

def main():
    print("=" * 70)
    print("Extracting Problems from LeetCode PDFs")
    print("=" * 70)
    
    if not PDF_FILES:
        print("No LeetCode PDF files found")
        return
    
    print(f"\nFound {len(PDF_FILES)} PDF files:\n")
    for pdf in PDF_FILES:
        print(f"  - {pdf.name}")
    
    if PDF_LIB == "pdfplumber":
        print("\nUsing pdfplumber to extract...")
        for pdf_path in PDF_FILES:
            print(f"\nProcessing: {pdf_path.name}")
            extract_with_pdfplumber(pdf_path)
    elif PDF_LIB == "PyPDF2":
        print("\nUsing PyPDF2 to extract...")
        for pdf_path in PDF_FILES:
            print(f"\nProcessing: {pdf_path.name}")
            extract_with_pypdf(pdf_path)
    else:
        print("\nERROR: Install a PDF library:")
        print("  pip install pdfplumber")
        print("  OR")
        print("  pip install PyPDF2")
        return
    
    print("\n" + "=" * 70)
    print("Note: Save the extracted text to process further")
    print("=" * 70)

if __name__ == "__main__":
    main()
