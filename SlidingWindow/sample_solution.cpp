#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sample(vector<int>& nums, int k) {
        int sum = 0;
        for (int i = 0; i < min(k, static_cast<int>(nums.size())); ++i) sum += nums[i];
        return sum;
    }
};
