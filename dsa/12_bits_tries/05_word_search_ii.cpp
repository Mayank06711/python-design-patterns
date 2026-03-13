/*
 * Word Search II
 * LeetCode: #212 | Difficulty: Hard
 * Find all words from list in grid
 * Pattern: Trie + grid DFS backtracking
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) { return {}; }
};

int main() {
    Solution sol;
    vector<vector<char>> b={{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
    vector<string> w={"oath","pea","eat","rain"};
    auto r=sol.findWords(b,w);
    cout<<"Found "<<r.size()<<" words (expected 2) "<<(r.size()==2?"PASS":"FAIL")<<endl;
    return 0;
}
