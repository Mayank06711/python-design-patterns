/*
 * Palindrome Partitioning II
 * LeetCode: #132 | Difficulty: Hard
 * Min cuts. aab->1
 * Pattern: Two DP tables (palindrome + cuts)
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCut(string s) { return 0; }
};

int main() {
    Solution sol;
    cout<<"Test1: "<<sol.minCut("aab")<<" (expected 1)"<<endl;
    cout<<"Test2: "<<sol.minCut("a")<<" (expected 0)"<<endl;
    return 0;
}
