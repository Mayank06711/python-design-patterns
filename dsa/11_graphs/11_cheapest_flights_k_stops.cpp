/*
 * Cheapest Flights Within K Stops
 * LeetCode: #787 | Difficulty: Medium
 * Modified Bellman-Ford with max K stops
 * Pattern: Bellman-Ford with edge constraint
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> f={{0,1,100},{1,2,100},{2,0,100},{1,3,600},{2,3,200}};
    cout<<"Test: "<<sol.findCheapestPrice(4,f,0,3,1)<<" (expected 700)"<<endl;
    return 0;
}
