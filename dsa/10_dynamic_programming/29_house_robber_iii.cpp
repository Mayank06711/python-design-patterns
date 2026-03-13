/*
 * House Robber III
 * LeetCode: #337 | Difficulty: Medium
 * Rob houses on binary tree. Post-order (rob/not-rob pair)
 * Pattern: Tree DP
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
public:
    int rob(TreeNode* root) { return 0; }
};

int main() {
    Solution sol;
    TreeNode* r = new TreeNode(3);
    r->left = new TreeNode(2); r->right = new TreeNode(3);
    r->left->right = new TreeNode(3); r->right->right = new TreeNode(1);
    cout<<"Test: "<<sol.rob(r)<<" (expected 7)"<<endl;
    return 0;
}
