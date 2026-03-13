/*
 * Min Cost to Connect All Points
 * LeetCode: #1584 | Difficulty: Medium
 * MST with Manhattan distance
 * Pattern: Minimum Spanning Tree (Prim/Kruskal)
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> p={{0,0},{2,2},{3,10},{5,2},{7,0}};
    cout<<"Test: "<<sol.minCostConnectPoints(p)<<" (expected 20)"<<endl;
    return 0;
}
