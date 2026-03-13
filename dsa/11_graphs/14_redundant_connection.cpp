/*
 * Redundant Connection
 * LeetCode: #684 | Difficulty: Medium
 * Find extra edge creating cycle
 * Pattern: Union-Find cycle detection
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) { return {}; }
};

int main() {
    Solution sol;
    vector<vector<int>> e={{1,2},{1,3},{2,3}}; auto r=sol.findRedundantConnection(e);
    cout<<"Test: ["<<r[0]<<","<<r[1]<<"] (expected [2,3])"<<endl;
    return 0;
}
