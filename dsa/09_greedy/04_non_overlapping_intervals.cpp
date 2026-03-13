/*
 * Non-overlapping Intervals
 * LeetCode: #435 | Difficulty: Medium
 * Min removals. [[1,2],[2,3],[3,4],[1,3]]->1
 * Pattern: Sort by end, count overlaps
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> a={{1,2},{2,3},{3,4},{1,3}}; cout<<"Test1: "<<sol.eraseOverlapIntervals(a)<<" (expected 1)"<<endl;
    vector<vector<int>> b={{1,2},{1,2},{1,2}}; cout<<"Test2: "<<sol.eraseOverlapIntervals(b)<<" (expected 2)"<<endl;
    return 0;
}
