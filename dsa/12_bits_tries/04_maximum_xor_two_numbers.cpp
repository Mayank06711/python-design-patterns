/*
 * Maximum XOR of Two Numbers
 * LeetCode: #421 | Difficulty: Medium
 * Bitwise trie, greedily pick opposite bits. [3,10,5,25,2,8]->28
 * Pattern: Bitwise trie
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) { return 0; }
};

int main() {
    Solution sol;
    vector<int> n={3,10,5,25,2,8}; cout<<"Test: "<<sol.findMaximumXOR(n)<<" (expected 28)"<<endl;
    return 0;
}
