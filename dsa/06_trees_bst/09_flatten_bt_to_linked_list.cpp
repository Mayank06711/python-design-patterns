/*
 * Problem: Flatten Binary Tree to Linked List (LeetCode #114) - Medium
 *
 * Given the root of a binary tree, flatten the tree into a "linked list":
 * - The linked list should use the same TreeNode class where the right child
 *   pointer points to the next node and the left child pointer is always null.
 * - The linked list should be in the same order as a pre-order traversal.
 *
 * Approach: Reverse post-order traversal (right -> left -> root). Maintain a
 *           "prev" pointer. Each node points its right to prev and sets left to null.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(h) for recursion stack
 *
 * Example:
 *   Input:  [1,2,5,3,4,null,6]
 *   Output: [1,null,2,null,3,null,4,null,5,null,6]
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
    void flatten(TreeNode* root) {
        TreeNode* prev = nullptr;
        flattenHelper(root, prev);
    }

private:
    void flattenHelper(TreeNode* node, TreeNode*& prev) {
        if (!node) return;

        // Process right subtree first, then left, then current
        flattenHelper(node->right, prev);
        flattenHelper(node->left, prev);

        // Point current node to previously processed node
        node->right = prev;
        node->left = nullptr;
        prev = node;
    }
};

int main() {
    // Build tree:
    //        1
    //       / \
    //      2   5
    //     / \   \
    //    3   4   6
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->right = new TreeNode(6);

    Solution sol;
    sol.flatten(root);

    // Print the flattened list
    cout << "Flattened tree (linked list): ";
    TreeNode* current = root;
    while (current) {
        cout << current->val;
        if (current->right) cout << " -> ";
        current = current->right;
    }
    cout << endl;
    // Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6

    // Cleanup (all nodes are now in a right-linked list)
    current = root;
    while (current) {
        TreeNode* next = current->right;
        delete current;
        current = next;
    }

    return 0;
}
