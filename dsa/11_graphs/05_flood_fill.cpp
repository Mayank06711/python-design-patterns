/*
 * Flood Fill
 * LeetCode: #733 | Difficulty: Easy
 * Paint bucket fill. Basic DFS on grid
 * Pattern: Recursive DFS on grid
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) { return image; }
};

int main() {
    Solution sol;
    vector<vector<int>> img={{1,1,1},{1,1,0},{1,0,1}};
    auto r=sol.floodFill(img,1,1,2);
    cout<<"Test: center="<<r[1][1]<<" (expected 2)"<<endl;
    return 0;
}
