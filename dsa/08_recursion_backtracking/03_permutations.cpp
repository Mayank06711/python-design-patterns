/*
 * Permutations
 * LeetCode: #46 | Difficulty: Medium
 * All permutations of distinct ints. nums=[1,2,3]
 * Pattern: Swap-based or used-array
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) { return {}; }
};

int main() {
    Solution sol;
    vector<int> n={1,2,3}; auto r=sol.permute(n);
    cout<<"Test: "<<r.size()<<" perms (expected 6) "<<(r.size()==6?"PASS":"FAIL")<<endl;
    return 0;
}
