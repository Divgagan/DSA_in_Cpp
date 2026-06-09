#!/usr/bin/env python3
"""
Extract LeetCode problems from PDFs with proper format:
Problem#. Problem Name | Difficulty
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
    "Dynamic Programming": "DynamicProgramming",
    "Greedy": "Greedy",
    "Backtracking": "Backtracking",
    "Bit Manipulation": "BitManipulation",
    "Math": "Math",
    "Graph": "Graphs",
}

def extract_problems_from_pdfs():
    """Extract problem list from all PDFs"""
    problems_dict = {}  # Use dict to avoid duplicates
    
    pdf_files = sorted(PDF_DIR.glob("Progress - LeetCode*.pdf"))
    
    print(f"Found {len(pdf_files)} PDF files\n")
    
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        
        try:
            with pdfplumber.open(pdf_file) as pdf:
                full_text = ""
                for page in pdf.pages:
                    full_text += page.extract_text() + "\n"
                
                # Extract problems using pattern: "Number. Problem Name"
                # followed by date and difficulty
                pattern = r'(\d+)\.\s+([A-Za-z\s\-\+\(\)\'",#]+?)\s*\n.*?(Easy|Med\.|Hard)'
                matches = re.finditer(pattern, full_text)
                
                for match in matches:
                    prob_num = int(match.group(1))
                    prob_name = match.group(2).strip()
                    difficulty = match.group(3)
                    
                    # Normalize difficulty
                    if difficulty == "Med.":
                        difficulty = "Medium"
                    
                    # Avoid duplicates
                    if prob_num not in problems_dict:
                        problems_dict[prob_num] = {
                            'name': prob_name,
                            'difficulty': difficulty
                        }
                        print(f"  {prob_num}. {prob_name} | {difficulty}")
        
        except Exception as e:
            print(f"  Error: {e}")
    
    return sorted(problems_dict.items())

def categorize_problem(name):
    """Guess category based on problem name"""
    name_lower = name.lower()
    
    keywords = {
        "Array": ["array", "container", "median", "two sum", "sort", "rotate"],
        "String": ["string", "substring", "palindrome", "word"],
        "Hash Table": ["hash", "group", "valid", "word pattern"],
        "Linked List": ["linked", "list", "node", "merge"],
        "Stack": ["stack", "calculate", "min stack"],
        "Queue": ["queue"],
        "Tree": ["tree", "binary", "path", "leaf", "lowest", "traverse"],
        "Dynamic Programming": ["dp", "climb", "unique", "distinct", "ways", "house", "rob", "break", "word break"],
        "Greedy": ["greedy", "jump", "candy", "interval"],
        "Backtracking": ["backtrack", "permutation", "combination", "n-queens", "sudoku"],
        "Bit Manipulation": ["bit", "power", "number of"],
        "Math": ["pow", "sqrt", "factorial", "excel", "fraction"],
        "Graph": ["graph", "clone", "course", "network", "island"],
    }
    
    for category, words in keywords.items():
        if any(word in name_lower for word in words):
            return category
    
    return "General"

def organize_problems_in_repo(problems):
    """Create problem list files in each category folder"""
    
    print(f"\n{'='*70}")
    print(f"Found {len(problems)} total problems")
    print(f"{'='*70}\n")
    
    by_category = defaultdict(list)
    
    # Organize by category
    for prob_num, prob_data in problems:
        category = categorize_problem(prob_data['name'])
        by_category[category].append((prob_num, prob_data['name'], prob_data['difficulty']))
    
    # Create problems list for each category
    for category, probs in sorted(by_category.items()):
        repo_folder = CATEGORY_MAP.get(category, "General")
        category_dir = CPP_DIR / repo_folder
        
        if not category_dir.exists():
            print(f"⚠️  Folder not found: {category_dir}")
            continue
        
        print(f"\n{category} → {repo_folder}/ ({len(probs)} problems)")
        
        # Create markdown table of problems
        content = f"# {category} Problems\n\n"
        content += "| # | Problem Name | Difficulty | Status |\n"
        content += "|---|---|---|---|\n"
        
        for prob_num, prob_name, difficulty in sorted(probs):
            content += f"| {prob_num} | {prob_name} | {difficulty} | |\n"
            print(f"  {prob_num}. {prob_name} ({difficulty})")
        
        # Write problems list
        problems_file = category_dir / "problems_list.md"
        problems_file.write_text(content, encoding='utf-8')
    
    # Create master summary
    summary_data = {
        "total_solved": len(problems),
        "by_difficulty": {
            "Easy": len([p for p in problems if p[1]['difficulty'] == 'Easy']),
            "Medium": len([p for p in problems if p[1]['difficulty'] == 'Medium']),
            "Hard": len([p for p in problems if p[1]['difficulty'] == 'Hard']),
        },
        "problems": [
            {
                "number": num,
                "name": data['name'],
                "difficulty": data['difficulty'],
                "category": categorize_problem(data['name'])
            }
            for num, data in problems
        ]
    }
    
    summary_file = CPP_DIR / "assets" / "problems_summary.json"
    summary_file.write_text(json.dumps(summary_data, indent=2), encoding='utf-8')
    
    print(f"\n✅ Summary saved to: {summary_file}")

def main():
    print("="*70)
    print("Extracting LeetCode Problems from PDF Progress Reports")
    print("="*70 + "\n")
    
    problems = extract_problems_from_pdfs()
    
    if problems:
        print(f"\n✅ Successfully extracted {len(problems)} problems!")
        organize_problems_in_repo(problems)
        print("\n" + "="*70)
        print("✅ All problems organized in repo!")
        print("   - Created problems_list.md in each category")
        print("   - Created problems_summary.json in assets/")
        print("="*70)
    else:
        print("\n❌ No problems found")

if __name__ == "__main__":
    main()
