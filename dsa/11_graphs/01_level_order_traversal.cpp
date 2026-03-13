/*
 * Binary Tree Level Order Traversal
 * LeetCode: #102 | Difficulty: Medium
 * BFS level by level. Gentlest BFS intro
 * Pattern: Core BFS with queue
 * Company: Amazon, Meta, Google
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
    vector<vector<int>> levelOrder(TreeNode* root) { return {}; }
};

int main() {
    Solution sol;
    TreeNode* r=new TreeNode(3); r->left=new TreeNode(9); r->right=new TreeNode(20);
    r->right->left=new TreeNode(15); r->right->right=new TreeNode(7);
    auto res=sol.levelOrder(r);
    cout<<"Test: "<<res.size()<<" levels (expected 3)"<<endl;
    return 0;
}
