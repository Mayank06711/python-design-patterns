/*
 * Is Graph Bipartite?
 * LeetCode: #785 | Difficulty: Medium
 * 2-color the graph. Odd cycle = not bipartite
 * Pattern: Graph coloring BFS/DFS
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) { return false; }
};

int main() {
    Solution sol;
    vector<vector<int>> g1={{1,2,3},{0,2},{0,1,3},{0,2}}; cout<<"Test1: "<<sol.isBipartite(g1)<<" (expected 0)"<<endl;
    vector<vector<int>> g2={{1,3},{0,2},{1,3},{0,2}}; cout<<"Test2: "<<sol.isBipartite(g2)<<" (expected 1)"<<endl;
    return 0;
}
