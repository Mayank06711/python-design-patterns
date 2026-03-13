/*
 * Merge Intervals
 * LeetCode: #56 | Difficulty: Medium
 * Merge overlapping intervals
 * Pattern: Sort + sweep
 * Company: Google, Meta, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) { return {}; }
};

int main() {
    Solution sol;
    vector<vector<int>> a={{1,3},{2,6},{8,10},{15,18}}; auto r=sol.merge(a);
    cout<<"Test: "<<r.size()<<" intervals (expected 3) "<<(r.size()==3?"PASS":"FAIL")<<endl;
    return 0;
}
