#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sample(vector<int>& nums) {
        unordered_set<int> seen(nums.begin(), nums.end());
        return static_cast<int>(seen.size());
    }
};
