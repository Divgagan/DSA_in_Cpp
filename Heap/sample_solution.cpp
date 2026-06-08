#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sample(vector<int>& nums) {
        priority_queue<int> pq(nums.begin(), nums.end());
        return pq.empty() ? 0 : pq.top();
    }
};
