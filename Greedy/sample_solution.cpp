#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sample(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums.empty() ? 0 : nums.back();
    }
};
