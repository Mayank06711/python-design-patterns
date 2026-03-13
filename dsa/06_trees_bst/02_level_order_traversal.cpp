/*
 * Problem: Binary Tree Level Order Traversal (LeetCode #102) - Medium
 *
 * Given the root of a binary tree, return the level order traversal
 * of its node values (left to right, level by level).
 *
 * Approach: BFS using a queue. Process all nodes at current level
 *           before moving to the next. Collect values per level.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 *
 * Example:
 *   Input:  [3,9,20,null,null,15,7]
 *   Output: [[3],[9,20],[15,7]]
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        // TODO: implement BFS with queue
        vector<vector<int>> result;
        return result;
    }
};

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Solution sol;
    vector<vector<int>> result = sol.levelOrder(root);

    cout << "Level order: [";
    for (int i = 0; i < (int)result.size(); i++) {
        cout << "[";
        for (int j = 0; j < (int)result[i].size(); j++) {
            cout << result[i][j];
            if (j < (int)result[i].size() - 1) cout << ",";
        }
        cout << "]";
        if (i < (int)result.size() - 1) cout << ",";
    }
    cout << "]" << endl;
    // Expected: [[3],[9,20],[15,7]]

    delete root->right->right;
    delete root->right->left;
    delete root->left;
    delete root->right;
    delete root;
    return 0;
}
