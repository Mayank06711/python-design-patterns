/*
 * House Robber II
 * LeetCode: #213 | Difficulty: Medium
 * Circular houses. [2,3,2]->3
 * Pattern: Circular to two linear
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) { return 0; }
};

int main() {
    Solution sol;
    vector<int> a={2,3,2}; cout<<"Test1: "<<sol.rob(a)<<" (expected 3)"<<endl;
    vector<int> b={1,2,3,1}; cout<<"Test2: "<<sol.rob(b)<<" (expected 4)"<<endl;
    return 0;
}
