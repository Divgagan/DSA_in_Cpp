#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool sample(string s) {
        int left = 0, right = static_cast<int>(s.size()) - 1;
        while (left < right) {
            if (s[left++] != s[right--]) return false;
        }
        return true;
    }
};
