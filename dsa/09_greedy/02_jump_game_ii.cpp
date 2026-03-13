/*
 * Jump Game II
 * LeetCode: #45 | Difficulty: Medium
 * Min jumps to last index. [2,3,1,1,4]->2
 * Pattern: BFS-style greedy (current/next range)
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) { return 0; }
};

int main() {
    Solution sol;
    vector<int> a={2,3,1,1,4}; cout<<"Test1: "<<sol.jump(a)<<" (expected 2)"<<endl;
    vector<int> b={2,3,0,1,4}; cout<<"Test2: "<<sol.jump(b)<<" (expected 2)"<<endl;
    return 0;
}
