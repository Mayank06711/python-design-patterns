/*
 * Problem: Lowest Common Ancestor of a Binary Tree (LeetCode #236) - Medium
 *
 * Given a binary tree, find the LCA of two given nodes p and q.
 * The LCA is the lowest node that has both p and q as descendants
 * (a node can be a descendant of itself).
 *
 * Approach: Recursive DFS. Simultaneously search left and right subtrees.
 *           If both sides return non-null, current node is the LCA.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(h)
 *
 * Example:
 *   Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
 *   Output: 3
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
        // TODO: implement recursive DFS simultaneous subtree search
        return nullptr;
    }
};

int main() {
    TreeNode* root = new TreeNode(3);
    TreeNode* node5 = new TreeNode(5);
    TreeNode* node1 = new TreeNode(1);
    TreeNode* node6 = new TreeNode(6);
    TreeNode* node2 = new TreeNode(2);
    TreeNode* node0 = new TreeNode(0);
    TreeNode* node8 = new TreeNode(8);
    TreeNode* node7 = new TreeNode(7);
    TreeNode* node4 = new TreeNode(4);

    root->left = node5;
    root->right = node1;
    node5->left = node6;
    node5->right = node2;
    node1->left = node0;
    node1->right = node8;
    node2->left = node7;
    node2->right = node4;

    Solution sol;

    TreeNode* lca1 = sol.lowestCommonAncestor(root, node5, node1);
    cout << "LCA of 5 and 1: " << (lca1 ? lca1->val : -1) << endl; // Expected: 3

    TreeNode* lca2 = sol.lowestCommonAncestor(root, node5, node4);
    cout << "LCA of 5 and 4: " << (lca2 ? lca2->val : -1) << endl; // Expected: 5

    delete node7; delete node4; delete node6;
    delete node2; delete node0; delete node8;
    delete node5; delete node1; delete root;
    return 0;
}
