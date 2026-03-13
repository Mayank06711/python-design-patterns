/*
 * Number of Provinces
 * LeetCode: #547 | Difficulty: Medium
 * Count connected components. Adjacency matrix
 * Pattern: Classic Union-Find
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> c={{1,1,0},{1,1,0},{0,0,1}};
    cout<<"Test1: "<<sol.findCircleNum(c)<<" (expected 2)"<<endl;
    return 0;
}
