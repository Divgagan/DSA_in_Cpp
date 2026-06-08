#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sample(vector<int>& nums, int target) {
        auto it = lower_bound(nums.begin(), nums.end(), target);
        return it == nums.end() ? -1 : static_cast<int>(it - nums.begin());
    }
};
