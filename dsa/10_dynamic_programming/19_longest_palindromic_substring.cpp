/*
 * Longest Palindromic Substring
 * LeetCode: #5 | Difficulty: Medium
 * Longest palindromic substring. babad->bab
 * Pattern: Expand around center / interval DP
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) { return ""; }
};

int main() {
    Solution sol;
    string r=sol.longestPalindrome("babad");
    cout<<"Test1: "<<r<<" (length "<<r.size()<<", expected 3)"<<endl;
    r=sol.longestPalindrome("cbbd");
    cout<<"Test2: "<<r<<" (length "<<r.size()<<", expected 2)"<<endl;
    return 0;
}
