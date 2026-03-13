/*
 * Longest Common Subsequence
 * LeetCode: #1143 | Difficulty: Medium
 * LCS. abcde, ace -> 3
 * Pattern: Two-string comparison DP
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string t1, string t2) { return 0; }
};

int main() {
    Solution sol;
    cout<<"Test1: "<<sol.longestCommonSubsequence("abcde","ace")<<" (expected 3)"<<endl;
    cout<<"Test2: "<<sol.longestCommonSubsequence("abc","def")<<" (expected 0)"<<endl;
    return 0;
}
