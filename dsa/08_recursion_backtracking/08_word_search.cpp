/*
 * Word Search
 * LeetCode: #79 | Difficulty: Medium
 * Find if word exists in grid via adjacent cells
 * Pattern: Grid DFS + visited + backtrack
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) { return false; }
};

int main() {
    Solution sol;
    vector<vector<char>> b={{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    cout<<"Test1: ABCCED -> "<<sol.exist(b,"ABCCED")<<" (expected 1)"<<endl;
    cout<<"Test2: SEE -> "<<sol.exist(b,"SEE")<<" (expected 1)"<<endl;
    cout<<"Test3: ABCB -> "<<sol.exist(b,"ABCB")<<" (expected 0)"<<endl;
    return 0;
}
