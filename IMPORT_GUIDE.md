# How to Import Your LeetCode & GFG Problems

## Current Status
- LeetCode: 103 problems solved (43 Easy, 52 Medium, 8 Hard)
- GeeksForGeeks: 31 problems solved

## Next Steps

### Step 1: Export Your Problems
1. Go to your LeetCode profile: https://leetcode.com/u/Gagan747/
2. Scroll to "Solved Problems" section
3. Select all problems (Ctrl+A)
4. Copy the list
5. Paste into a text file

### Step 2: Edit the import script
Edit scripts/import_problems.py and add your problems in this format:
```
Two Sum | Easy | Array | https://leetcode.com/problems/two-sum/
Add Two Numbers | Medium | Linked List | https://leetcode.com/problems/add-two-numbers/
```

### Step 3: Run the import
```bash
python scripts/import_problems.py
```

This will automatically:
- Create folders for each category
- Add problem templates with links
- Organize by difficulty
- Update README files

## File Structure Created
Each problem will have:
- Problem description
- Your solution code
- Approach/explanation
- Complexity analysis
- Links to LeetCode/GFG
