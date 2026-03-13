/*
 * Count Good Nodes
 * LeetCode: #1448 | Difficulty: Medium
 * Node X good if no ancestor > X
 * Pattern: Pre-order DFS with running max
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val; TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
public:
    int goodNodes(TreeNode* root) { return 0; }
};

int main() {
    Solution sol;
    TreeNode* r=new TreeNode(3); r->left=new TreeNode(1); r->right=new TreeNode(4);
    r->left->left=new TreeNode(3); r->right->left=new TreeNode(1); r->right->right=new TreeNode(5);
    cout<<"Test: "<<sol.goodNodes(r)<<" (expected 4)"<<endl;
    return 0;
}
