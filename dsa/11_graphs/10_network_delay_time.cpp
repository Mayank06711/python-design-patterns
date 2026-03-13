/*
 * Network Delay Time
 * LeetCode: #743 | Difficulty: Medium
 * Classic Dijkstra. Signal reach all nodes
 * Pattern: Dijkstra shortest path
 * Company: Google, Amazon, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> t={{2,1,1},{2,3,1},{3,4,1}};
    cout<<"Test: "<<sol.networkDelayTime(t,4,2)<<" (expected 2)"<<endl;
    return 0;
}
