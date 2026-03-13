/*
 * Surrounded Regions
 * LeetCode: #130 | Difficulty: Medium
 * Flip surrounded Os. DFS from boundary inward
 * Pattern: Boundary DFS (invert problem)
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) { /* TODO */ }
};

int main() {
    Solution sol;
    vector<vector<char>> b={{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};
    sol.solve(b);
    cout<<"Test: [1][1]="<<b[1][1]<<" (expected X), [3][1]="<<b[3][1]<<" (expected O)"<<endl;
    return 0;
}
