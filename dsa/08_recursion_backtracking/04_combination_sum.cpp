/*
 * Combination Sum
 * LeetCode: #39 | Difficulty: Medium
 * Combos summing to target, reuse allowed. [2,3,6,7] t=7
 * Pattern: Unbounded choice, start-index
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& c, int target) { return {}; }
};

int main() {
    Solution sol;
    vector<int> c={2,3,6,7}; auto r=sol.combinationSum(c,7);
    cout<<"Test: "<<r.size()<<" combos (expected 2) "<<(r.size()==2?"PASS":"FAIL")<<endl;
    return 0;
}
