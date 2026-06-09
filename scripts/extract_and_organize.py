#!/usr/bin/env python3
"""
Extract LeetCode problem numbers and names from PDFs
and organize them in the repo by category
"""

import json
import re
from pathlib import Path
from collections import defaultdict

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber not installed")
    exit(1)

PDF_DIR = Path(r"c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo")
CPP_DIR = PDF_DIR / "DSA_in_C++" / "CPP"

# Map problem categories to repo folders
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
    "Topological Sort": "Graphs",
    "Union Find": "DisjointSet",
    "Segment Tree": "SegmentTree",
    "Dynamic Programming": "DynamicProgramming",
    "Greedy": "Greedy",
    "Backtracking": "Backtracking",
    "Bit Manipulation": "BitManipulation",
    "Math": "Math",
    "Recursion": "Recursion",
    "Two Pointers": "TwoPointers",
    "Sliding Window": "SlidingWindow",
}

def extract_problems_from_pdfs():
    """Extract problem list from all PDFs"""
    problems = []
    
    pdf_files = sorted(PDF_DIR.glob("Progress - LeetCode*.pdf"))
    
    print(f"Found {len(pdf_files)} PDF files\n")
    
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        
        try:
            with pdfplumber.open(pdf_file) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    
                    # Extract problem numbers and names
                    # Pattern: number. Problem Name (Difficulty)
                    pattern = r'(\d+)\.\s+([A-Za-z\s\-\+\(\)]+?)\s*\|'
                    matches = re.findall(pattern, text)
                    
                    for num, name in matches:
                        prob_num = int(num)
                        prob_name = name.strip()
                        
                        # Avoid duplicates
                        if not any(p[0] == prob_num for p in problems):
                            problems.append((prob_num, prob_name))
                            print(f"  [{page_num}] {prob_num}. {prob_name}")
        
        except Exception as e:
            print(f"  Error: {e}")
    
    return sorted(problems, key=lambda x: x[0])

def create_problem_entry(prob_num, prob_name, category="General"):
    """Create a markdown entry for a problem (no code)"""
    return f"""# {prob_num}. {prob_name}

## Problem Details
- **Number**: {prob_num}
- **Name**: {prob_name}
- **Category**: {category}
- **Status**: Not solved yet

## Notes
[Add approach and solution later]
"""

def organize_problems(problems):
    """Organize problems by category in repo"""
    
    print(f"\n{'='*70}")
    print(f"Found {len(problems)} total problems")
    print(f"{'='*70}\n")
    
    # Group by difficulty (naive categorization)
    by_category = defaultdict(list)
    
    for prob_num, prob_name in problems:
        # Try to categorize based on problem name keywords
        category = "General"
        
        name_lower = prob_name.lower()
        
        if any(word in name_lower for word in ["array", "container", "median", "twosum"]):
            category = "Array"
        elif any(word in name_lower for word in ["string", "substring", "palindrome", "word"]):
            category = "String"
        elif any(word in name_lower for word in ["hash", "group", "valid"]):
            category = "Hash Table"
        elif any(word in name_lower for word in ["linked", "list", "node"]):
            category = "Linked List"
        elif any(word in name_lower for word in ["stack", "calculate"]):
            category = "Stack"
        elif any(word in name_lower for word in ["queue", "moving"]):
            category = "Queue"
        elif any(word in name_lower for word in ["tree", "binary", "path", "leaf", "lowest"]):
            category = "Tree"
        elif any(word in name_lower for word in ["search", "binary"]):
            category = "Array"  # Binary search problems go to Arrays
        elif any(word in name_lower for word in ["dynamic", "climb", "unique", "distinct"]):
            category = "Dynamic Programming"
        elif any(word in name_lower for word in ["greedy", "jump", "candy"]):
            category = "Greedy"
        elif any(word in name_lower for word in ["backtrack", "permutation", "combination"]):
            category = "Backtracking"
        elif any(word in name_lower for word in ["bit", "power"]):
            category = "Bit Manipulation"
        elif any(word in name_lower for word in ["graph", "clone", "course"]):
            category = "Graph"
        elif any(word in name_lower for word in ["trie", "word"]):
            category = "Trie"
        elif any(word in name_lower for word in ["divide", "conquer"]):
            category = "Recursion"
        elif any(word in name_lower for word in ["pointer", "meeting"]):
            category = "Two Pointers"
        elif any(word in name_lower for word in ["window"]):
            category = "Sliding Window"
        
        by_category[category].append((prob_num, prob_name))
    
    # Create problem files in respective directories
    for category, probs in sorted(by_category.items()):
        repo_category = CATEGORY_MAP.get(category, "General")
        category_dir = CPP_DIR / repo_category
        
        print(f"\n{category} -> {repo_category}/ ({len(probs)} problems)")
        
        # Create problems file for this category
        problems_file = category_dir / "problems_list.md"
        
        content = f"# {category} Problems\n\n"
        content += "| # | Problem Name | Status |\n"
        content += "|---|---|---|\n"
        
        for prob_num, prob_name in probs:
            content += f"| {prob_num} | {prob_name} | - |\n"
            print(f"  {prob_num}. {prob_name}")
        
        # Write to file
        problems_file.write_text(content, encoding='utf-8')
        print(f"  -> Saved to: {problems_file}")
    
    # Create summary file
    summary_file = CPP_DIR / "assets" / "problems_summary.json"
    summary = {
        "total_problems": len(problems),
        "by_category": {cat: len(probs) for cat, probs in by_category.items()},
        "problems": [{"number": num, "name": name} for num, name in problems]
    }
    summary_file.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(f"\n✅ Summary saved to: {summary_file}")

def main():
    print("="*70)
    print("Extracting LeetCode Problems from PDFs")
    print("="*70 + "\n")
    
    # Extract problems
    problems = extract_problems_from_pdfs()
    
    if problems:
        print(f"\n✅ Successfully extracted {len(problems)} problems!")
        organize_problems(problems)
        print("\n" + "="*70)
        print("✅ All problems organized in repo!")
        print("="*70)
    else:
        print("\n❌ No problems found in PDFs")

if __name__ == "__main__":
    main()
