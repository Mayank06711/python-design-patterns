/*
 * Jump Game
 * LeetCode: #55 | Difficulty: Medium
 * Can reach last index? [2,3,1,1,4]->true
 * Pattern: Track farthest reachable index
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) { return false; }
};

int main() {
    Solution sol;
    vector<int> a={2,3,1,1,4}; cout<<"Test1: "<<sol.canJump(a)<<" (expected 1)"<<endl;
    vector<int> b={3,2,1,0,4}; cout<<"Test2: "<<sol.canJump(b)<<" (expected 0)"<<endl;
    return 0;
}
