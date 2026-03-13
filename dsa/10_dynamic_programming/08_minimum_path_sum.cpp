/*
 * Minimum Path Sum
 * LeetCode: #64 | Difficulty: Medium
 * Min sum path top-left to bottom-right. [[1,3,1],[1,5,1],[4,2,1]]->7
 * Pattern: Grid optimization (min)
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> g={{1,3,1},{1,5,1},{4,2,1}};
    cout<<"Test: "<<sol.minPathSum(g)<<" (expected 7)"<<endl;
    return 0;
}
