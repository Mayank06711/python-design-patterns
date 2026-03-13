/*
 * Rotting Oranges
 * LeetCode: #994 | Difficulty: Medium
 * Multi-source BFS. All rotten spread simultaneously
 * Pattern: Multi-source BFS
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> g={{2,1,1},{1,1,0},{0,1,1}};
    cout<<"Test1: "<<sol.orangesRotting(g)<<" (expected 4)"<<endl;
    vector<vector<int>> g2={{2,1,1},{0,1,1},{1,0,1}};
    cout<<"Test2: "<<sol.orangesRotting(g2)<<" (expected -1)"<<endl;
    return 0;
}
