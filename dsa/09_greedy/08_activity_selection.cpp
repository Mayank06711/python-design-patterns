/*
 * Activity Selection
 * LeetCode: Classic | Difficulty: Medium
 * Max non-overlapping activities
 * Pattern: Sort by end time, greedy pick
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxActivities(vector<vector<int>>& acts) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> a={{1,2},{3,4},{0,6},{5,7},{8,9},{5,9}};
    cout<<"Test: "<<sol.maxActivities(a)<<" activities (expected 4)"<<endl;
    return 0;
}
