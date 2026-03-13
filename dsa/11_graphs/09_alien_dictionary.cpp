/*
 * Alien Dictionary
 * LeetCode: #269 | Difficulty: Hard
 * Build graph from word ordering, then topo sort
 * Pattern: Graph construction + topo sort
 * Company: Google, Meta, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) { return ""; }
};

int main() {
    Solution sol;
    vector<string> w={"wrt","wrf","er","ett","rftt"};
    cout<<"Test: "<<sol.alienOrder(w)<<" (expected wertf)"<<endl;
    return 0;
}
