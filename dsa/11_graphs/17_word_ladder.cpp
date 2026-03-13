/*
 * Word Ladder
 * LeetCode: #127 | Difficulty: Hard
 * BFS on implicit graph. Words differ by 1 letter = edge
 * Pattern: BFS on implicit graph
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) { return 0; }
};

int main() {
    Solution sol;
    vector<string> wl={"hot","dot","dog","lot","log","cog"};
    cout<<"Test: "<<sol.ladderLength("hit","cog",wl)<<" (expected 5)"<<endl;
    return 0;
}
