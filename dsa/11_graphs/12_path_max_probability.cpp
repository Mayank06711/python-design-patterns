/*
 * Path with Maximum Probability
 * LeetCode: #1514 | Difficulty: Medium
 * Modified Dijkstra (max-heap, multiply probs)
 * Pattern: Modified Dijkstra (max)
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& prob, int s, int e) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> ed={{0,1},{1,2},{0,2}}; vector<double> pr={0.5,0.5,0.2};
    cout<<"Test: "<<sol.maxProbability(3,ed,pr,0,2)<<" (expected 0.25)"<<endl;
    return 0;
}
