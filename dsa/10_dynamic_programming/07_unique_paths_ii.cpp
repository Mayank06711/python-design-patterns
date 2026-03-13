/*
 * Unique Paths II
 * LeetCode: #63 | Difficulty: Medium
 * Grid with obstacles
 * Pattern: Grid + constraints
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& grid) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> g={{0,0,0},{0,1,0},{0,0,0}};
    cout<<"Test: "<<sol.uniquePathsWithObstacles(g)<<" (expected 2)"<<endl;
    return 0;
}
