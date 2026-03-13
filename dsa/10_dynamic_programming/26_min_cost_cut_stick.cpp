/*
 * Min Cost to Cut a Stick
 * LeetCode: #1547 | Difficulty: Hard
 * n=7 cuts=[1,3,4,5]->16
 * Pattern: Interval DP
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(int n, vector<int>& cuts) { return 0; }
};

int main() {
    Solution sol;
    vector<int> c={1,3,4,5}; cout<<"Test: "<<sol.minCost(7,c)<<" (expected 16)"<<endl;
    return 0;
}
