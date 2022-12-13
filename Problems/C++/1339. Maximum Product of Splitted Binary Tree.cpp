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
    long maxProd = 0, treeSum = 0;

    int totalSum(TreeNode* root) {
        if (root == NULL)
            return 0;

        long subTreeSum = root->val + totalSum(root->left) + totalSum(root->right);
        maxProd = max(maxProd, subTreeSum * (treeSum - subTreeSum));

        return subTreeSum;
    }

    int maxProduct(TreeNode* root) {
        if (root == NULL)
            return 0;

        treeSum = totalSum(root);
        totalSum(root);
        
        return maxProd % (int)(1e9 + 7);
    }
};