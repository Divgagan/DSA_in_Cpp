#!/usr/bin/env python3
"""
Add GFG problems from folder to repo organized by category
"""

import json
import re
from pathlib import Path
from collections import defaultdict

GFG_DIR = Path(r"c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo\GFG")
CPP_DIR = Path(r"c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo\DSA_in_C++\CPP")

# Map filename patterns to categories
GFG_CATEGORY_MAP = {
    # Arrays
    "count_inversion": "Arrays",
    "count_K_subset": "Arrays",
    "find_missing_number": "Arrays",
    "k_sized_subarray_max": "Arrays",
    "k_th_smallest_element": "Arrays",
    "max_1s_in_2D_arr": "Arrays",
    "max_prod_sub_arr": "Arrays",
    "missing_and_repeating_ele": "Arrays",
    "Peak_element": "Arrays",
    "ROTATE_ARR": "Arrays",
    "Second_largest_element": "Arrays",
    "union_arr_sorted": "Arrays",
    "Longest_sub_array_of_Sum_K": "Arrays",
    "CHECK_EQUAL_ARR": "Arrays",
    "get_min_diff": "Arrays",
    "Equilibrium_point": "Arrays",
    
    # Linked List
    "remoing_loop_LL": "LinkedList",
    
    # Stack
    "Balanced_Parenthese": "Stack",
    
    # Binary Search
    "Binary_search_Modified": "BinarySearch",
    "floor_num": "BinarySearch",
    
    # Dynamic Programming
    "distinct_subset_sum": "DynamicProgramming",
    
    # Miscellaneous
    "minimum_platoforms": "General",
}

def convert_filename_to_name(filename):
    """Convert GFG filename to readable problem name"""
    # Remove .cpp extension
    name = filename.replace(".cpp", "").replace("_", " ")
    # Fix spacing
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def categorize_gfg_problem(filename):
    """Categorize GFG problem based on filename"""
    for pattern, category in GFG_CATEGORY_MAP.items():
        if pattern.lower() in filename.lower():
            return category
    return "General"

def get_existing_problems(category_file):
    """Extract existing problems from problems_list.md"""
    existing = {}
    if not category_file.exists():
        return existing
    
    content = category_file.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    for line in lines:
        if '|' in line and line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) > 2 and parts[1].isdigit():
                num = int(parts[1])
                if len(parts) > 2:
                    name = parts[2]
                    existing[num] = name
    
    return existing

def add_gfg_problems():
    """Add GFG problems to repo"""
    
    print("=" * 70)
    print("Adding GeeksforGeeks Problems to Repository")
    print("=" * 70 + "\n")
    
    # Find all GFG problems
    gfg_files = sorted(GFG_DIR.glob("*.cpp"))
    gfg_problems = []
    
    print(f"Found {len(gfg_files)} GFG problem files:\n")
    
    for idx, filepath in enumerate(gfg_files, 1):
        filename = filepath.name
        prob_name = convert_filename_to_name(filename)
        category = categorize_gfg_problem(filename)
        
        gfg_problems.append({
            'number': f"GFG-{idx:03d}",
            'name': prob_name,
            'category': category,
            'source': 'GFG'
        })
        
        print(f"  {idx:2}. {prob_name:40} → {category}")
    
    # Organize by category
    by_category = defaultdict(list)
    for prob in gfg_problems:
        by_category[prob['category']].append(prob)
    
    print(f"\n{'='*70}")
    print(f"Updating {len(by_category)} categories with GFG problems")
    print(f"{'='*70}\n")
    
    # Update each category's problems_list.md
    updated_categories = []
    
    for category, repo_folder in [
        ("Arrays", "Arrays"),
        ("LinkedList", "LinkedList"),
        ("Stack", "Stack"),
        ("BinarySearch", "BinarySearch"),
        ("DynamicProgramming", "DynamicProgramming"),
        ("General", "General"),
    ]:
        if category not in by_category:
            continue
        
        category_dir = CPP_DIR / repo_folder
        category_dir.mkdir(parents=True, exist_ok=True)
        problems_file = category_dir / "problems_list.md"
        
        # Get existing problems
        existing = {}
        lc_probs = []
        
        if problems_file.exists():
            content = problems_file.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            # Extract LeetCode problems (numeric IDs)
            for line in lines:
                if '|' in line and line.strip().startswith('|'):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) > 2:
                        try:
                            num = int(parts[1])
                            name = parts[2] if len(parts) > 2 else ""
                            diff = parts[3] if len(parts) > 3 else "Unknown"
                            lc_probs.append((num, name, diff))
                        except ValueError:
                            pass
        
        # Build new content
        cat_display = category.replace("_", " ")
        content = f"# {cat_display} Problems\n\n"
        content += "| # | Problem Name | Difficulty | Status |\n"
        content += "|---|---|---|---|\n"
        
        # Add LeetCode problems first (sorted by number)
        for num, name, diff in sorted(lc_probs):
            content += f"| {num} | {name} | {diff} | |\n"
        
        # Add GFG problems
        for prob in sorted(by_category[category], key=lambda p: p['number']):
            content += f"| {prob['number']} | {prob['name']} | GFG | |\n"
        
        # Write file
        problems_file.write_text(content, encoding='utf-8')
        updated_categories.append((repo_folder, len(by_category[category])))
        
        print(f"{category} → {repo_folder}/ (+{len(by_category[category])} GFG problems)")
    
    # Update summary JSON
    summary_file = CPP_DIR / "assets" / "problems_summary.json"
    if summary_file.exists():
        summary_data = json.loads(summary_file.read_text(encoding='utf-8'))
    else:
        summary_data = {
            "total_solved": 0,
            "by_difficulty": {},
            "by_category": {},
            "problems": []
        }
    
    # Add GFG problems to summary
    for prob in gfg_problems:
        summary_data["problems"].append({
            "number": prob['number'],
            "name": prob['name'],
            "difficulty": "GFG",
            "category": prob['category']
        })
    
    summary_data["total_gfg"] = len(gfg_problems)
    summary_file.write_text(json.dumps(summary_data, indent=2), encoding='utf-8')
    
    print(f"\n{'='*70}")
    print(f"✅ COMPLETE! Added {len(gfg_problems)} GFG problems to {len(updated_categories)} categories")
    print(f"{'='*70}")

if __name__ == "__main__":
    add_gfg_problems()
