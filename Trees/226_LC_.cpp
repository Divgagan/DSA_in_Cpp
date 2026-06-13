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
    void Swap(TreeNode* root) {

        if(root == NULL) return;

        stack<TreeNode*> s;
        s.push(root);

        while(!s.empty()) {

            TreeNode* node = s.top();
            s.pop();

            // Actual inversion
            swap(node->left, node->right);

            if(node->left != NULL) {
                s.push(node->left);
            }

            if(node->right != NULL) {
                s.push(node->right);
            }
        }
    }

public:
    TreeNode* invertTree(TreeNode* root) {

        if(root == NULL) return NULL;

        Swap(root);

        return root;
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
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL) return NULL;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};

