/*
 * Binary Tree Cameras
 * LeetCode: #968 | Difficulty: Hard
 * Min cameras. Camera covers parent+self+children
 * Pattern: Greedy post-order DFS, 3-state
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
    int minCameraCover(TreeNode* root) { return 0; }
};

int main() {
    Solution sol;
    TreeNode* r=new TreeNode(0); r->left=new TreeNode(0);
    r->left->left=new TreeNode(0); r->left->right=new TreeNode(0);
    cout<<"Test: "<<sol.minCameraCover(r)<<" (expected 1)"<<endl;
    return 0;
}
