#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x = 0) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int sample(TreeNode* root) {
        return root ? root->val : 0;
    }
};
