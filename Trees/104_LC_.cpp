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
    int maxDepth(TreeNode* root) {
        if(root == NULL) return 0 ; 

        // if  Leaf Node : 
        if(root->left == NULL && root->right == NULL) {
            return 1 ; 
        }

        // Checking for the left subtree : 
        if(root->left == NULL ){
            return 1 + maxDepth(root->right) ; 

        }

        if(root->right == NULL){
            return 1+ maxDepth(root->left) ; 
        }


        return 1 + max(maxDepth(root->left) , maxDepth(root->right)) ; 
        
    }
};