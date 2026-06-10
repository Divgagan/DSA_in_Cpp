#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 **/

// LeetCode 236 - Lowest Common Ancestor of a Binary Tree
// Difficulty: Medium
//
// Approach: DFS / Recursion
// - If root is NULL, return NULL.
// - If root matches p or q, return root (found one of the nodes).
// - Recurse on left and right subtrees.
// - If both left and right return non-NULL, root is the LCA.
// - Otherwise, return whichever side is non-NULL (propagate upward).
//
// Time Complexity  : O(N) — visits every node once
// Space Complexity : O(H) — recursion stack, H = height of tree

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {

        if (root == NULL)
            return NULL;

        if (root == p || root == q)
            return root;

        TreeNode* left  = lowestCommonAncestor(root->left,  p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        // p and q found in different subtrees → current root is LCA
        if (left != NULL && right != NULL)
            return root;

        // Only one side found → propagate it upward
        if (left != NULL)
            return left;

        return right;
    }
};
