/*
 * Problem: Validate Binary Search Tree (LeetCode #98) - Medium
 *
 * Given the root of a binary tree, determine if it is a valid BST.
 * A valid BST has all left subtree values < node and all right subtree values > node.
 *
 * Approach: Recursive range propagation. Pass allowable (min, max) bounds
 *           down the tree. Check that val is within bounds at each node.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(h)
 *
 * Example:
 *   Input:  [2,1,3] -> true
 *   Input:  [5,1,4,null,null,3,6] -> false
 */

#include <iostream>
#include <climits>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        // TODO: implement in-order with bounds / range propagation
        return false;
    }
};

int main() {
    TreeNode* root1 = new TreeNode(2);
    root1->left = new TreeNode(1);
    root1->right = new TreeNode(3);

    Solution sol;
    cout << "[2,1,3] valid BST: " << (sol.isValidBST(root1) ? "true" : "false") << endl;
    // Expected: true

    TreeNode* root2 = new TreeNode(5);
    root2->left = new TreeNode(1);
    root2->right = new TreeNode(4);
    root2->right->left = new TreeNode(3);
    root2->right->right = new TreeNode(6);

    cout << "[5,1,4,null,null,3,6] valid BST: " << (sol.isValidBST(root2) ? "true" : "false") << endl;
    // Expected: false

    delete root1->left; delete root1->right; delete root1;
    delete root2->right->left; delete root2->right->right;
    delete root2->left; delete root2->right; delete root2;
    return 0;
}
