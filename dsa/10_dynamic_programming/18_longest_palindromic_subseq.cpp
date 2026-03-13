/*
 * Longest Palindromic Subsequence
 * LeetCode: #516 | Difficulty: Medium
 * LPS. bbbab->4. Trick: LCS(s,reverse(s))
 * Pattern: LCS reduction
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestPalindromeSubseq(string s) { return 0; }
};

int main() {
    Solution sol;
    cout<<"Test1: "<<sol.longestPalindromeSubseq("bbbab")<<" (expected 4)"<<endl;
    cout<<"Test2: "<<sol.longestPalindromeSubseq("cbbd")<<" (expected 2)"<<endl;
    return 0;
}
