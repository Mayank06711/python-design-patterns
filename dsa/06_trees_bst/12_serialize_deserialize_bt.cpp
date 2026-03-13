/*
 * Serialize and Deserialize Binary Tree
 * LeetCode: #297 | Difficulty: Hard
 * Encode tree to string, decode string to tree
 * Pattern: Pre-order encoding + queue reconstruction
 * Company: Meta, Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val; TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Codec {
public:
    string serialize(TreeNode* root) { return ""; }
    TreeNode* deserialize(string data) { return nullptr; }
};

int main() {
    TreeNode* r = new TreeNode(1);
    r->left = new TreeNode(2); r->right = new TreeNode(3);
    r->right->left = new TreeNode(4); r->right->right = new TreeNode(5);
    Codec codec;
    string s = codec.serialize(r);
    cout << "Serialized: " << s << endl;
    TreeNode* r2 = codec.deserialize(s);
    cout << "Deserialized root: " << (r2 ? to_string(r2->val) : "null") << " (expected 1)" << endl;
    return 0;
}
