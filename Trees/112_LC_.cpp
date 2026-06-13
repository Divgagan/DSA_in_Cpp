/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    bool check_sum(TreeNode* root, int targetSum, int sum) {

        if(root == NULL) {
            return false;
        }

        sum += root->val;

        // Leaf node check
        if(root->left == NULL && root->right == NULL) {
            return (sum == targetSum);
        }

        bool left_sum = check_sum(root->left, targetSum, sum);
        bool right_sum = check_sum(root->right, targetSum, sum);

        return left_sum || right_sum;
    }

public:                                                
    bool hasPathSum(TreeNode* root, int targetSum) {

        if(root == NULL) {
            return false;
        }

        return check_sum(root, targetSum, 0);   
    }
}; 

// Recursive Solution is given below :

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public: 
    bool hasPathSum(TreeNode* root, int targetSum) {

        if(root == NULL) {
            return false;
        }

        // Leaf node check
        if(root->left == NULL && root->right == NULL) {
            return (root->val == targetSum);
        }

        bool left_sum = hasPathSum(root->left, targetSum - root->val);
        bool right_sum = hasPathSum(root->right, targetSum - root->val);

        return left_sum || right_sum;
    }
};