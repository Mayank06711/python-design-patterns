/*
 * Problem: Construct Binary Tree from Preorder and Inorder Traversal (LeetCode #105) - Medium
 *
 * Given two integer arrays preorder and inorder where preorder is the preorder
 * traversal of a binary tree and inorder is the inorder traversal of the same
 * tree, construct and return the binary tree.
 *
 * Approach: Divide and conquer. The first element of preorder is always the root.
 *           Find that element in inorder to split into left and right subtrees.
 *           Use a hashmap for O(1) index lookup in inorder array.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 *
 * Example:
 *   Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
 *   Output: [3,9,20,null,null,15,7]
 */

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // Build index map for inorder array
        unordered_map<int, int> inorderMap;
        for (int i = 0; i < (int)inorder.size(); i++) {
            inorderMap[inorder[i]] = i;
        }

        int preIdx = 0;
        return build(preorder, preIdx, inorderMap, 0, (int)inorder.size() - 1);
    }

private:
    TreeNode* build(vector<int>& preorder, int &preIdx,
                    unordered_map<int, int>& inorderMap,
                    int inLeft, int inRight) {
        if (inLeft > inRight) return nullptr;

        int rootVal = preorder[preIdx++];
        TreeNode* root = new TreeNode(rootVal);

        int inIdx = inorderMap[rootVal];

        // Build left subtree first (matches preorder sequence)
        root->left = build(preorder, preIdx, inorderMap, inLeft, inIdx - 1);
        root->right = build(preorder, preIdx, inorderMap, inIdx + 1, inRight);

        return root;
    }
};

// Helper to print tree in level order for verification
void printInorder(TreeNode* node) {
    if (!node) return;
    printInorder(node->left);
    cout << node->val << " ";
    printInorder(node->right);
}

void deleteTree(TreeNode* node) {
    if (!node) return;
    deleteTree(node->left);
    deleteTree(node->right);
    delete node;
}

int main() {
    vector<int> preorder = {3, 9, 20, 15, 7};
    vector<int> inorder = {9, 3, 15, 20, 7};

    Solution sol;
    TreeNode* root = sol.buildTree(preorder, inorder);

    // Verify by printing inorder (should match original inorder)
    cout << "Inorder traversal of constructed tree: ";
    printInorder(root);
    cout << endl;
    // Expected: 9 3 15 20 7

    cout << "Root value: " << root->val << endl; // Expected: 3
    cout << "Root->left value: " << root->left->val << endl; // Expected: 9
    cout << "Root->right value: " << root->right->val << endl; // Expected: 20

    deleteTree(root);

    return 0;
}
