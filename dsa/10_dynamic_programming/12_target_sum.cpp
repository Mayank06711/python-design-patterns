/*
 * Target Sum
 * LeetCode: #494 | Difficulty: Medium
 * Assign +/- to reach target. [1,1,1,1,1] t=3->5
 * Pattern: Transform to subset sum
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) { return 0; }
};

int main() {
    Solution sol;
    vector<int> a={1,1,1,1,1}; cout<<"Test: "<<sol.findTargetSumWays(a,3)<<" (expected 5)"<<endl;
    return 0;
}
