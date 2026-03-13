/*
 * Dungeon Game
 * LeetCode: #174 | Difficulty: Hard
 * Min initial HP to reach end. Reverse DP
 * Pattern: Reverse direction DP
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> d={{-2,-3,3},{-5,-10,1},{10,30,-5}};
    cout<<"Test: "<<sol.calculateMinimumHP(d)<<" (expected 7)"<<endl;
    return 0;
}
