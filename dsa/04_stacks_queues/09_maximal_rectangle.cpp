/*
 * Maximal Rectangle
 * LeetCode: #85 | Difficulty: Hard
 * Largest rectangle of 1s in binary matrix. Histogram per row + LC84
 * Pattern: Histogram per row + monotonic stack
 * Company: Google, Amazon, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<char>> m={{'1','0','1','0','0'},{'1','0','1','1','1'},{'1','1','1','1','1'},{'1','0','0','1','0'}};
    cout<<"Test: "<<sol.maximalRectangle(m)<<" (expected 6)"<<endl;
    return 0;
}
