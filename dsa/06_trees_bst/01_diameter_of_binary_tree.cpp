/*
 * Problem: Diameter of Binary Tree (LeetCode #543) - Easy
 *
 * Given the root of a binary tree, return the length of the diameter.
 * The diameter is the longest path between any two nodes (measured in edges).
 * This path may or may not pass through the root.
 *
 * Approach: Post-order DFS. At each node compute left and right depths.
 *           Diameter through that node = leftDepth + rightDepth.
 *           Track a global max across all nodes.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(h)
 *
 * Example:
 *   Input:  [1,2,3,4,5]
 *   Output: 3  (path: 4->2->1->3 or 5->2->1->3)
 */

#include <iostream>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        // TODO: implement post-order DFS + global max
        return 0;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    Solution sol;
    cout << "Diameter: " << sol.diameterOfBinaryTree(root) << endl;
    // Expected: 3

    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;
    return 0;
}
