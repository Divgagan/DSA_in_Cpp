#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void dfs(vector<int>& nums, int index, vector<int>& path, vector<vector<int>>& ans) {
        if (index == static_cast<int>(nums.size())) {
            ans.push_back(path);
            return;
        }
        dfs(nums, index + 1, path, ans);
        path.push_back(nums[index]);
        dfs(nums, index + 1, path, ans);
        path.pop_back();
    }
};
