/*
 * Problem: Binary Tree Right Side View (LeetCode #199) - Medium
 *
 * Imagine standing on the right side of a binary tree. Return the values
 * of the nodes you can see ordered from top to bottom.
 *
 * Approach: BFS level order traversal. For each level, take the last
 *           (rightmost) node.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 *
 * Example:
 *   Input:  [1,2,3,null,5,null,4]
 *   Output: [1,3,4]
 */

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        // TODO: implement BFS, last node per level
        vector<int> result;
        return result;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right = new TreeNode(5);
    root->right->right = new TreeNode(4);

    Solution sol;
    vector<int> result = sol.rightSideView(root);

    cout << "Right side view: [";
    for (int i = 0; i < (int)result.size(); i++) {
        cout << result[i];
        if (i < (int)result.size() - 1) cout << ",";
    }
    cout << "]" << endl;
    // Expected: [1,3,4]

    delete root->left->right;
    delete root->right->right;
    delete root->left;
    delete root->right;
    delete root;
    return 0;
}
