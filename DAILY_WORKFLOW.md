# 📅 Daily Workflow Guide - Problem Solving & Committing

## 🎯 Quick Start (Daily Routine)

### Step 1️⃣: Solve a Problem
Create/write your C++ solution file

### Step 2️⃣: Add to Repo
Place the solution in the appropriate category folder

### Step 3️⃣: Update Status
Mark as solved in `problems_list.md`

### Step 4️⃣: Commit to Git
Commit with meaningful message showing your progress

### Step 5️⃣: Push to GitHub
Upload changes so they're saved online

---

## 📝 Detailed Steps

### **Step 1: Solve the Problem**

Write your C++ solution. Example:
```cpp
// Arrays/two_sum.cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if(map.find(complement) != map.end()) {
                return {map[complement], i};
            }
            map[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = sol.twoSum(nums, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
```

### **Step 2: File Naming Convention**

Place solution in the correct category folder:

```
📁 Arrays/
  ├── problems_list.md
  ├── two_sum.cpp              ← Problem #1
  ├── merge_sorted_array.cpp   ← Problem #88
  └── remove_duplicates.cpp    ← Problem #26

📁 Trees/
  ├── problems_list.md
  ├── symmetric_tree.cpp       ← Problem #101
  └── max_depth_binary_tree.cpp ← Problem #104

📁 DynamicProgramming/
  ├── problems_list.md
  ├── climbing_stairs.cpp      ← Problem #70
  └── house_robber.cpp         ← Problem #198
```

**Naming Rules:**
- Use problem number + problem name (lowercase with underscores)
- Example: `1_two_sum.cpp` or just `two_sum.cpp`

### **Step 3: Update Progress in problems_list.md**

**Before:**
```markdown
| 1 | Two Sum | Easy | |
```

**After:**
```markdown
| 1 | Two Sum | Easy | ✅ Solved |
```

Or use more detailed status:
```markdown
| 1 | Two Sum | Easy | ✅ 2026-06-08 |
| 26 | Remove Duplicates | Easy | 🔄 In Progress |
```

**How to edit:**
1. Open `Arrays/problems_list.md`
2. Find the problem row
3. Update the last column (Status)
4. Save the file

### **Step 4: Commit to Git**

#### **Option A: Single Problem Solved**

```bash
cd "c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo\DSA_in_C++\CPP"

git add Arrays/two_sum.cpp
git add Arrays/problems_list.md
git commit -m "✅ Solve LeetCode #1: Two Sum (Arrays)

- Time Complexity: O(n)
- Space Complexity: O(n)
- Approach: Hash Map
- Difficulty: Easy"
```

#### **Option B: Multiple Problems Solved (Daily)**

```bash
# After solving 3-5 problems in a day:

git add Arrays/two_sum.cpp
git add Arrays/remove_duplicates.cpp
git add Trees/symmetric_tree.cpp
git add Arrays/problems_list.md
git add Trees/problems_list.md

git commit -m "✅ Solve 3 problems - 2026-06-08

Arrays:
- #1: Two Sum (Easy, O(n))
- #26: Remove Duplicates (Easy, O(n))

Trees:
- #101: Symmetric Tree (Easy, O(n))"
```

### **Step 5: Push to GitHub**

```bash
# After committing, push to remote
git push origin main
```

---

## 📋 Commit Message Format

### **Best Practice Pattern:**

```
✅ Solve #{PROBLEM_NUMBER}: {PROBLEM_NAME} ({CATEGORY})

- Time Complexity: O(...)
- Space Complexity: O(...)
- Approach: ...
- Difficulty: Easy/Medium/Hard
- Status: ✅ Solved
```

### **Real Examples:**

**Example 1: Easy Problem**
```
✅ Solve #1: Two Sum (Arrays)

- Time Complexity: O(n)
- Space Complexity: O(n)
- Approach: Hash Map
- Difficulty: Easy
```

**Example 2: Medium Problem**
```
✅ Solve #101: Symmetric Tree (Trees)

- Time Complexity: O(n)
- Space Complexity: O(h) where h is height
- Approach: Recursive DFS
- Difficulty: Easy
```

**Example 3: Daily Batch**
```
✅ Solve 5 Array problems - 2026-06-08

- #1: Two Sum (Easy)
- #26: Remove Duplicates (Easy)
- #48: Rotate Image (Medium)
- #53: Maximum Subarray (Medium)
- #75: Sort Colors (Medium)

Status: 5/27 Array problems solved
```

---

## 🔄 Complete Daily Workflow Example

### **Scenario: You solve "Two Sum" problem**

```bash
# 1. Navigate to repo
cd "c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo\DSA_in_C++\CPP"

# 2. Create/edit your solution
# Write code in: Arrays/two_sum.cpp

# 3. Check git status
git status
# Output:
# Untracked files:
#   Arrays/two_sum.cpp

# 4. Add files to staging
git add Arrays/two_sum.cpp
git add Arrays/problems_list.md  # (if you updated status)

# 5. Commit with message
git commit -m "✅ Solve #1: Two Sum (Arrays)

- Time: O(n)
- Space: O(n)
- Approach: Hash Map
- Difficulty: Easy"

# 6. Push to GitHub
git push origin main

# 7. Verify
git log --oneline -1
# Shows: ✅ Solve #1: Two Sum (Arrays)
```

---

## 📊 Daily Progress Tracking

### **Option 1: Update PROGRESS_TRACKER.md Weekly**

```markdown
## Week of June 8-14, 2026

| Day | Problems Solved | Total | Time Spent |
|-----|-----------------|-------|-----------|
| June 8 | 3 | 3 | 1.5 hrs |
| June 9 | 2 | 5 | 1.2 hrs |
| June 10 | 4 | 9 | 2 hrs |
```

### **Option 2: Use Git Commits as History**

Each commit shows:
- What problem was solved
- When it was solved
- Complexity analysis
- Approach used

```bash
# View commit history
git log --oneline

# Output:
92fcb87 ✅ Solve #1: Two Sum (Arrays)
92fcb88 ✅ Solve #26: Remove Duplicates (Arrays)
92fcb89 ✅ Solve #48: Rotate Image (Arrays)
...
```

---

## ⚙️ Quick Commands Reference

### **Check Status**
```bash
git status
```
Shows modified/untracked files

### **Stage Files**
```bash
# Stage specific file
git add Arrays/two_sum.cpp

# Stage entire category
git add Arrays/

# Stage all changes
git add .
```

### **Commit**
```bash
# Commit with message
git commit -m "Your message here"

# Or interactive (opens editor)
git commit
```

### **Push**
```bash
git push origin main
```

### **View History**
```bash
# Last 10 commits
git log --oneline -10

# With stats
git log --stat -5

# Pretty format
git log --pretty=format:"%h %s" -10
```

### **View Differences**
```bash
# What changed in uncommitted files
git diff

# What changed in staged files
git diff --staged
```

---

## 📱 Minimal Daily Commands

### **Fastest Workflow (if solving 1 problem):**

```bash
cd CPP
git add {category}/problem.cpp
git add {category}/problems_list.md
git commit -m "✅ Solve #{NUM}: {NAME}"
git push origin main
```

### **Batch Workflow (solving multiple problems):**

```bash
cd CPP
git add .
git commit -m "✅ Solve 5 problems - $(date +%Y-%m-%d)

Arrays: #1, #26, #48
Trees: #101"
git push origin main
```

---

## 💡 Tips for Daily Success

### **1. Commit Frequency**
- ✅ **Best:** Commit after every 1-2 problems
- ⚠️ **Okay:** Commit once daily with all solutions
- ❌ **Avoid:** Going weeks without commits

### **2. Meaningful Messages**
- ✅ `✅ Solve #1: Two Sum - O(n) with Hash Map`
- ❌ `Fix bug` or `Update`

### **3. Status Updates**
- Update `problems_list.md` whenever you solve a problem
- Change status from blank `|  |` to `✅ 2026-06-08`

### **4. Push Regularly**
- Push to GitHub daily
- This backs up your work
- Shows your progress publicly

### **5. Track Progress**
- Check `PROGRESS_TRACKER.md`
- Update category counts periodically
- Monitor your solving rate

---

## 📈 Sample Monthly Progress

```bash
# June 1-7: 7 problems solved
# Commits: 7 (1 per problem)

# June 8-14: 12 problems solved
# Commits: 12 (1 per problem)

# June 15-30: 25 problems solved
# Commits: 25 (mix of 1-5 per commit)

# Total by June 30: ~44 problems solved
# Commit history shows your daily progress
```

---

## 🎯 Final Summary

**Daily Routine (15 minutes):**

1. **Solve** problem → write `solution.cpp`
2. **Place** in category folder
3. **Update** `problems_list.md` status
4. **Stage** files: `git add {files}`
5. **Commit**: `git commit -m "✅ Solve #X: Name"`
6. **Push**: `git push origin main`

**That's it!** Your progress is now:
- ✅ Tracked locally
- ✅ Backed up on GitHub
- ✅ Visible in commit history
- ✅ Documented for portfolio

---

**Happy Coding! 🚀**
