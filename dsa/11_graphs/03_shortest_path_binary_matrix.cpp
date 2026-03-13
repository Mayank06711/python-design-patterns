/*
 * Shortest Path in Binary Matrix
 * LeetCode: #1091 | Difficulty: Medium
 * BFS shortest path, 8-directional
 * Pattern: BFS shortest path (unweighted)
 * Company: Meta, Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> g={{0,1},{1,0}};
    cout<<"Test1: "<<sol.shortestPathBinaryMatrix(g)<<" (expected 2)"<<endl;
    return 0;
}
