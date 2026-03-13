/*
 * Subsets II
 * LeetCode: #90 | Difficulty: Medium
 * Array may have dupes. nums=[1,2,2]->6 subsets
 * Pattern: Sort + skip dupes at same level
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) { return {}; }
};

int main() {
    Solution sol;
    vector<int> n={1,2,2}; auto r=sol.subsetsWithDup(n);
    cout<<"Test: "<<r.size()<<" subsets (expected 6) "<<(r.size()==6?"PASS":"FAIL")<<endl;
    return 0;
}
