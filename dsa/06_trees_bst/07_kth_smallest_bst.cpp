/*
 * Problem: Kth Smallest Element in a BST (LeetCode #230) - Medium
 *
 * Given the root of a BST and an integer k, return the kth smallest value
 * (1-indexed) of all values in the BST.
 *
 * Approach: In-order traversal of a BST visits nodes in ascending order.
 *           Traverse in-order, decrement k, stop early when k reaches 0.
 *
 * Time Complexity:  O(H + k)
 * Space Complexity: O(H)
 *
 * Example:
 *   Input:  root = [3,1,4,null,2], k = 1
 *   Output: 1
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
    int kthSmallest(TreeNode* root, int k) {
        // TODO: implement in-order traversal + early stop
        return 0;
    }
};

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4);
    root->left->right = new TreeNode(2);

    Solution sol;
    cout << "1st smallest: " << sol.kthSmallest(root, 1) << endl; // Expected: 1
    cout << "2nd smallest: " << sol.kthSmallest(root, 2) << endl; // Expected: 2
    cout << "3rd smallest: " << sol.kthSmallest(root, 3) << endl; // Expected: 3

    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;
    return 0;
}
