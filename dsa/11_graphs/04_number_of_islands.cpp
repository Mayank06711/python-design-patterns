/*
 * Number of Islands
 * LeetCode: #200 | Difficulty: Medium
 * Count connected components in grid. THE classic graph problem
 * Pattern: DFS/BFS connected components
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<char>> g={{'1','1','0','0','0'},{'1','1','0','0','0'},{'0','0','1','0','0'},{'0','0','0','1','1'}};
    cout<<"Test: "<<sol.numIslands(g)<<" (expected 3)"<<endl;
    return 0;
}
