/*
 * Problem: Lowest Common Ancestor of a BST (LeetCode #235) - Medium
 *
 * Given a BST, find the LCA of two given nodes p and q.
 * In a BST, left descendants < node < right descendants.
 *
 * Approach: BST split-point logic. If both p and q are smaller, go left.
 *           If both larger, go right. Otherwise current node is the LCA.
 *
 * Time Complexity:  O(h)
 * Space Complexity: O(1) iterative
 *
 * Example:
 *   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
 *   Output: 6
 */

#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // TODO: implement BST split-point logic
        return nullptr;
    }
};

int main() {
    TreeNode* root = new TreeNode(6);
    TreeNode* node2 = new TreeNode(2);
    TreeNode* node8 = new TreeNode(8);
    TreeNode* node0 = new TreeNode(0);
    TreeNode* node4 = new TreeNode(4);
    TreeNode* node7 = new TreeNode(7);
    TreeNode* node9 = new TreeNode(9);
    TreeNode* node3 = new TreeNode(3);
    TreeNode* node5 = new TreeNode(5);

    root->left = node2;
    root->right = node8;
    node2->left = node0;
    node2->right = node4;
    node8->left = node7;
    node8->right = node9;
    node4->left = node3;
    node4->right = node5;

    Solution sol;

    TreeNode* lca1 = sol.lowestCommonAncestor(root, node2, node8);
    cout << "LCA of 2 and 8: " << (lca1 ? lca1->val : -1) << endl; // Expected: 6

    TreeNode* lca2 = sol.lowestCommonAncestor(root, node2, node4);
    cout << "LCA of 2 and 4: " << (lca2 ? lca2->val : -1) << endl; // Expected: 2

    delete node3; delete node5; delete node0;
    delete node4; delete node7; delete node9;
    delete node2; delete node8; delete root;
    return 0;
}
