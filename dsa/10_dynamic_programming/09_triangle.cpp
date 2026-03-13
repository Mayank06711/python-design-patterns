/*
 * Triangle
 * LeetCode: #120 | Difficulty: Medium
 * Min path sum top to bottom. [[2],[3,4],[6,5,7],[4,1,8,3]]->11
 * Pattern: Bottom-up DP
 * Company: Amazon, Apple
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> t={{2},{3,4},{6,5,7},{4,1,8,3}};
    cout<<"Test: "<<sol.minimumTotal(t)<<" (expected 11)"<<endl;
    return 0;
}
