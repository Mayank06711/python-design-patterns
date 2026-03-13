/*
 * Binary Tree Max Path Sum
 * LeetCode: #124 | Difficulty: Hard
 * Max path sum any two nodes. Local vs global optimum
 * Pattern: Tree DP, post-order DFS
 * Company: Google, Amazon, Meta
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
    int maxPathSum(TreeNode* root) { return 0; }
};

int main() {
    Solution sol;
    TreeNode* r = new TreeNode(1); r->left = new TreeNode(2); r->right = new TreeNode(3);
    cout<<"Test1: "<<sol.maxPathSum(r)<<" (expected 6)"<<endl;
    TreeNode* r2 = new TreeNode(-10); r2->left = new TreeNode(9); r2->right = new TreeNode(20);
    r2->right->left = new TreeNode(15); r2->right->right = new TreeNode(7);
    cout<<"Test2: "<<sol.maxPathSum(r2)<<" (expected 42)"<<endl;
    return 0;
}
