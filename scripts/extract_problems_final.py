#!/usr/bin/env python3
"""
Extract ALL LeetCode problems from PDFs
Format: 
  Number. Problem Name
  YYYY.MM.DD Status
  Difficulty
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
    """Extract all problems from PDFs"""
    problems_dict = {}
    
    pdf_files = sorted(PDF_DIR.glob("Progress - LeetCode*.pdf"))
    print(f"Found {len(pdf_files)} PDF files\n")
    
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        
        try:
            with pdfplumber.open(pdf_file) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    lines = text.split('\n')
                    
                    # Parse multi-line format
                    i = 0
                    while i < len(lines):
                        line = lines[i].strip()
                        
                        # Look for pattern: "Number. Problem Name"
                        if re.match(r'^\d+\.\s+', line):
                            match = re.match(r'^(\d+)\.\s+(.+)$', line)
                            if match:
                                prob_num = int(match.group(1))
                                prob_name = match.group(2).strip()
                                
                                # Get difficulty from next lines
                                difficulty = "Unknown"
                                for j in range(i+1, min(i+5, len(lines))):
                                    next_line = lines[j].strip()
                                    if next_line in ["Easy", "Med.", "Hard"]:
                                        difficulty = next_line
                                        if difficulty == "Med.":
                                            difficulty = "Medium"
                                        break
                                
                                # Store if not duplicate
                                if prob_num not in problems_dict:
                                    problems_dict[prob_num] = {
                                        'name': prob_name,
                                        'difficulty': difficulty
                                    }
                                    print(f"  {prob_num:3}. {prob_name:40} | {difficulty}")
                        
                        i += 1
        
        except Exception as e:
            print(f"  Error: {e}")
    
    return sorted(problems_dict.items())

def categorize_problem(name):
    """Categorize based on problem name"""
    name_lower = name.lower()
    
    keywords = {
        "Array": ["array", "container", "median", "two sum", "sort", "rotate", "max area", "trapping", "best time"],
        "String": ["string", "substring", "palindrome", "word", "letter", "integer (atoi)", "atoi"],
        "Hash Table": ["hash", "group", "valid", "word pattern", "isomorphic"],
        "Linked List": ["linked", "list", "node", "merge", "reverse"],
        "Stack": ["stack", "calculate", "min stack", "simplify"],
        "Queue": ["queue", "sliding window", "moving"],
        "Tree": ["tree", "binary", "path", "leaf", "lowest", "traverse", "symmetric", "level order"],
        "Dynamic Programming": ["dp", "climb", "unique", "distinct", "ways", "house", "rob", "break", "word break", "partition", "falling", "triangle", "minimum path", "fibonacci", "jump", "word ladder"],
        "Greedy": ["greedy", "jump", "candy", "interval", "gas", "assign"],
        "Backtracking": ["backtrack", "permutation", "combination", "n-queens", "sudoku", "subsets", "generate"],
        "Bit Manipulation": ["bit", "power", "number of", "single", "missing", "hamming"],
        "Math": ["pow", "sqrt", "factorial", "excel", "fraction", "happy", "ugly"],
        "Graph": ["graph", "clone", "course", "network", "island", "region"],
        "Recursion": ["recursion", "reverse", "fib"]
    }
    
    for category, words in keywords.items():
        if any(word in name_lower for word in words):
            return category
    
    return "General"

def create_repo_files(problems):
    """Create problem list files in repo"""
    
    print(f"\n{'='*70}")
    print(f"Organizing {len(problems)} problems by category")
    print(f"{'='*70}\n")
    
    by_category = defaultdict(list)
    
    for prob_num, prob_data in problems:
        category = categorize_problem(prob_data['name'])
        by_category[category].append((prob_num, prob_data['name'], prob_data['difficulty']))
    
    # Create files for each category
    all_files_created = []
    
    for category in sorted(by_category.keys()):
        probs = by_category[category]
        repo_folder = CATEGORY_MAP.get(category, "General")
        category_dir = CPP_DIR / repo_folder
        
        if not category_dir.exists():
            print(f"⚠️  Creating folder: {repo_folder}/")
            category_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n{category} → {repo_folder}/ ({len(probs)} problems)")
        
        # Create problems_list.md
        content = f"# {category} Problems\n\n"
        content += "| # | Problem Name | Difficulty | Status |\n"
        content += "|---|---|---|---|\n"
        
        for prob_num, prob_name, difficulty in sorted(probs):
            content += f"| {prob_num} | {prob_name} | {difficulty} | |\n"
            print(f"  {prob_num:3}. {prob_name}")
        
        problems_file = category_dir / "problems_list.md"
        problems_file.write_text(content, encoding='utf-8')
        all_files_created.append(problems_file)
    
    # Create summary JSON
    summary_data = {
        "total_solved": len(problems),
        "by_difficulty": {
            "Easy": len([p for p in problems if p[1]['difficulty'] == 'Easy']),
            "Medium": len([p for p in problems if p[1]['difficulty'] == 'Medium']),
            "Hard": len([p for p in problems if p[1]['difficulty'] == 'Hard']),
        },
        "by_category": {cat: len(probs) for cat, probs in by_category.items()},
        "problems": [
            {
                "number": num,
                "name": data['name'],
                "difficulty": data['difficulty']
            }
            for num, data in problems
        ]
    }
    
    summary_file = CPP_DIR / "assets" / "problems_summary.json"
    summary_file.write_text(json.dumps(summary_data, indent=2), encoding='utf-8')
    all_files_created.append(summary_file)
    
    return all_files_created

def main():
    print("=" * 70)
    print("Extracting LeetCode Problems from PDFs")
    print("=" * 70 + "\n")
    
    problems = extract_problems_from_pdfs()
    
    if problems:
        print(f"\n✅ Successfully extracted {len(problems)} problems!")
        files = create_repo_files(problems)
        
        print("\n" + "=" * 70)
        print(f"✅ COMPLETE! Created {len(files)} files:")
        for f in files[:5]:
            print(f"   - {f.relative_to(CPP_DIR)}")
        if len(files) > 5:
            print(f"   ... and {len(files) - 5} more")
        print("=" * 70)
    else:
        print("\n❌ No problems found in PDFs")

if __name__ == "__main__":
    main()
