#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int data;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
 * };
 **/

class Solution {
private:

    void check(TreeNode* root, vector<int>& path,
               vector<vector<int>>& ans) {

        if (!root)
            return;

        path.push_back(root->data);

        // Leaf node
        if (root->left == NULL && root->right == NULL) {
            ans.push_back(path);
            path.pop_back();
            return;
        }

        check(root->left, path, ans);
        check(root->right, path, ans);

        path.pop_back();   // Backtracking
    }

public:

    vector<vector<int>> allRootToLeaf(TreeNode* root) {

        vector<vector<int>> ans;

        if (root == NULL)
            return ans;

        vector<int> path;

        check(root, path, ans);

        return ans;
    }
};
