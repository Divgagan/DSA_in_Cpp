# 🎓 Complete Real Example: Solving One Problem Step-by-Step

**Date:** 2026-06-08  
**Problem:** LeetCode #1 - Two Sum  
**Category:** Arrays  
**Difficulty:** Easy  

---

## 📌 Overview

This guide shows you **exactly** what to do when you solve **one real problem**, from start to finish, with actual code and commands.

---

## 🎯 Your Goal Today
Solve LeetCode #1 "Two Sum" and commit it to GitHub with proper tracking.

---

# 🔥 Let's Begin! (Step-by-Step)

## **STEP 1: Open Your Terminal**

```bash
# Navigate to your DSA repo
cd "c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo\DSA_in_C++\CPP"

# Check current status
git status
```

**Expected Output:**
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

## **STEP 2: Solve the Problem**

### 2a. Understand the Problem

**Problem:** Two Sum  
**Link:** https://leetcode.com/problems/two-sum/

**Problem Statement:**
```
Given an array of integers nums and an integer target, 
return the indices of the two numbers that add up to target.

You may assume each input has exactly one solution, 
and you cannot use the same element twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, so we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### 2b. Write Your Solution

Create a new file: `Arrays/1_two_sum.cpp`

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // HashMap to store value -> index mapping
        unordered_map<int, int> numMap;
        
        // Iterate through array
        for(int i = 0; i < nums.size(); i++) {
            // Calculate complement needed
            int complement = target - nums[i];
            
            // Check if complement exists in map
            if(numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            
            // Store current number and index
            numMap[nums[i]] = i;
        }
        
        // No solution found (shouldn't happen per problem statement)
        return {};
    }
};

int main() {
    Solution sol;
    
    // Test Case 1
    vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> result1 = sol.twoSum(nums1, target1);
    cout << "Test 1: [" << result1[0] << ", " << result1[1] << "]" << endl;
    // Output: Test 1: [0, 1]
    
    // Test Case 2
    vector<int> nums2 = {3, 2, 4};
    int target2 = 6;
    vector<int> result2 = sol.twoSum(nums2, target2);
    cout << "Test 2: [" << result2[0] << ", " << result2[1] << "]" << endl;
    // Output: Test 2: [1, 2]
    
    return 0;
}
```

**File Location:**
```
DSA_in_C++/CPP/
├── Arrays/
│   ├── problems_list.md
│   └── 1_two_sum.cpp          ← NEW FILE YOU CREATED
├── Trees/
├── DynamicProgramming/
...
```

---

## **STEP 3: Update Progress in problems_list.md**

### 3a. Before (Current State)

**File:** `Arrays/problems_list.md`

```markdown
# Array Problems

| # | Problem Name | Difficulty | Status |
|---|---|---|---|
| 1 | Two Sum | Easy | |
| 26 | Remove Duplicates from Sorted Array | Easy | |
| 48 | Rotate Image | Medium | |
...
```

### 3b. After (Updated State)

Update just the ONE row for problem #1:

```markdown
# Array Problems

| # | Problem Name | Difficulty | Status |
|---|---|---|---|
| 1 | Two Sum | Easy | ✅ Solved |
| 26 | Remove Duplicates from Sorted Array | Easy | |
| 48 | Rotate Image | Medium | |
...
```

**How to Edit:**
1. Open `Arrays/problems_list.md` in any text editor
2. Find the line: `| 1 | Two Sum | Easy | |`
3. Change it to: `| 1 | Two Sum | Easy | ✅ Solved |`
4. Save the file

---

## **STEP 4: Check What Changed**

Open terminal and check git status:

```bash
git status
```

**Expected Output:**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update the what will be committed)
        modified:   Arrays/problems_list.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Arrays/1_two_sum.cpp
```

**What this means:**
- ✅ `1_two_sum.cpp` - Your new solution file
- ✅ `problems_list.md` - Your status update

---

## **STEP 5: Stage Files for Commit**

```bash
# Add the solution file
git add Arrays/1_two_sum.cpp

# Add the updated progress file
git add Arrays/problems_list.md

# Verify staging
git status
```

**Expected Output:**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git add <file>..." to update the what will be committed)
        new file:   Arrays/1_two_sum.cpp
        modified:   Arrays/problems_list.md

nothing to commit, working tree clean
```

**What this means:**
- Both files are now "staged" and ready to commit
- When you commit, these changes will be saved

---

## **STEP 6: Commit with Meaningful Message**

```bash
git commit -m "✅ Solve #1: Two Sum (Arrays)

- Time Complexity: O(n)
- Space Complexity: O(n)
- Approach: Hash Map (Unordered Map)
- Algorithm: Single pass with complement lookup
- Difficulty: Easy
- Status: ✅ Solved & Tested"
```

**Expected Output:**
```
[main 92fcb87] ✅ Solve #1: Two Sum (Arrays)
 2 files changed, 45 insertions(+)
 create mode 100644 Arrays/1_two_sum.cpp
 rewrite mode 100644 Arrays/problems_list.md
```

**What this means:**
- ✅ Commit created successfully
- ✅ Changes saved to local git history
- ✅ Commit ID: `92fcb87` (unique identifier)

---

## **STEP 7: Push to GitHub**

```bash
# Upload your commit to GitHub
git push origin main
```

**Expected Output:**
```
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 3.50 KiB | 3.50 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Divgagan/DSA_in_Cpp.git
   92fcb87..93fcb88  main -> main
```

**What this means:**
- ✅ Your code is now on GitHub
- ✅ Backed up in the cloud
- ✅ Visible in your contribution graph
- ✅ Part of your portfolio

---

## **STEP 8: Verify Everything**

### Check commit history:
```bash
git log --oneline -3
```

**Expected Output:**
```
93fcb88 (HEAD -> main, origin/main) ✅ Solve #1: Two Sum (Arrays)
29891f9 📚 Add daily workflow guide for problem solving & committing
92fcb87 📊 Add 93 DSA problems from LeetCode & GFG with progress tracking
```

### Check GitHub:
Go to: https://github.com/Divgagan/DSA_in_Cpp

You'll see your commit on the main branch! ✅

---

# 🎨 Visual Flow

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: Terminal Ready                                      │
│ $ cd C++/CPP                                                │
│ $ git status → clean                                        │
└─────────────────────────────────────────────────────────────┘
                          ⬇️
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Write Solution                                      │
│ Create: Arrays/1_two_sum.cpp                                │
│ Write: Your C++ solution code                               │
└─────────────────────────────────────────────────────────────┘
                          ⬇️
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: Update Status                                       │
│ Edit: Arrays/problems_list.md                               │
│ Change: | 1 | Two Sum | Easy | | → | 1 | Two Sum | Easy | ✅ |
└─────────────────────────────────────────────────────────────┘
                          ⬇️
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: Check Changes                                       │
│ $ git status                                                │
│ ✅ Arrays/1_two_sum.cpp (new)                               │
│ ✅ Arrays/problems_list.md (modified)                       │
└─────────────────────────────────────────────────────────────┘
                          ⬇️
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: Stage Files                                         │
│ $ git add Arrays/1_two_sum.cpp                              │
│ $ git add Arrays/problems_list.md                           │
│ $ git status → Changes to be committed                      │
└─────────────────────────────────────────────────────────────┘
                          ⬇️
┌─────────────────────────────────────────────────────────────┐
│ STEP 6: Commit                                              │
│ $ git commit -m "✅ Solve #1: Two Sum (Arrays)              │
│   - Time: O(n)                                              │
│   - Space: O(n)                                             │
│   - Approach: Hash Map"                                     │
│ ✅ [main 93fcb88] Created                                   │
└─────────────────────────────────────────────────────────────┘
                          ⬇️
┌─────────────────────────────────────────────────────────────┐
│ STEP 7: Push to GitHub                                      │
│ $ git push origin main                                      │
│ ✅ 93fcb88..95fcb89 main → main (pushed!)                   │
└─────────────────────────────────────────────────────────────┘
                          ⬇️
┌─────────────────────────────────────────────────────────────┐
│ STEP 8: Done! 🎉                                            │
│ • Commit saved locally ✅                                   │
│ • Pushed to GitHub ✅                                       │
│ • Visible in contribution graph ✅                          │
│ • Problem marked as solved ✅                               │
└─────────────────────────────────────────────────────────────┘
```

---

# 📋 Tomorrow: Quick Checklist

When you solve the next problem tomorrow, just follow this:

```
☐ Solve problem & write solution.cpp
☐ Save file in correct category folder
☐ Update problems_list.md status (| ✅ Solved |)
☐ Terminal: git add {files}
☐ Terminal: git commit -m "✅ Solve #X: Name"
☐ Terminal: git push origin main
☐ Done! ✅
```

---

# 🔗 Quick Copy-Paste Commands

### For Next Time (Example: Problem #26)

```bash
# Navigate
cd "c:\Users\Gagan Diwakar\OneDrive\画像\Desktop\Git_repo\DSA_in_C++\CPP"

# Stage files
git add Arrays/26_remove_duplicates.cpp
git add Arrays/problems_list.md

# Commit
git commit -m "✅ Solve #26: Remove Duplicates from Sorted Array (Arrays)

- Time Complexity: O(n)
- Space Complexity: O(1)
- Approach: Two Pointers
- Difficulty: Easy"

# Push
git push origin main

# Verify
git log --oneline -1
```

---

# 💡 Real Example Files Created

### File 1: `Arrays/1_two_sum.cpp`
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if(numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> result1 = sol.twoSum(nums1, target1);
    cout << "Test 1: [" << result1[0] << ", " << result1[1] << "]" << endl;
    return 0;
}
```

### File 2: `Arrays/problems_list.md` (Updated)
```markdown
# Array Problems

| # | Problem Name | Difficulty | Status |
|---|---|---|---|
| 1 | Two Sum | Easy | ✅ Solved |
| 26 | Remove Duplicates from Sorted Array | Easy | |
| 48 | Rotate Image | Medium | |
| 53 | Maximum Subarray | Medium | |
| 75 | Sort Colors | Medium | |
... (rest of problems)
```

---

# 🎯 The Complete Cycle (All 8 Steps in 2 Minutes)

1. **Code** (1 min): Write your solution
2. **Update** (30 sec): Mark status as ✅
3. **Stage** (15 sec): `git add` files
4. **Commit** (30 sec): `git commit` with message
5. **Push** (30 sec): `git push origin main`
6. **Done** (5 sec): Verify with `git log`

**Total Time: 3-5 minutes per problem**

---

# 🚀 Tomorrow's Plan

Just:
1. Open this file (COMPLETE_EXAMPLE.md) as reference
2. Solve a problem (any from problems_list.md)
3. Follow the 8 steps shown here
4. Change only:
   - Problem number & name
   - File paths
   - Commit message
5. Everything else stays the same!

---

**You've got this! 💪**

When confused tomorrow → Read this file → Follow exact steps → Commit!

Good luck! 🚀
