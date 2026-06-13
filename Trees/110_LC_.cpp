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
private : 

public:
int dfsHeight(TreeNode* root) {
    if(root == NULL) return  0 ; 
    
    int Lh =dfsHeight(root->left) ; 
    if(Lh == -1 ) return -1 ; 

    int Rh = dfsHeight(root->right) ; 
    if(Rh == -1 ) return -1 ; 

    if(abs(Lh-Rh) > 1 ) return -1 ; 

    return 1 + max(Lh , Rh ) ; 

}

    bool isBalanced(TreeNode* root) {

        return dfsHeight(root) != -1 ; 






        
    }
};