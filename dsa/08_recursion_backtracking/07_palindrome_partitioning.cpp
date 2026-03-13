/*
 * Palindrome Partitioning
 * LeetCode: #131 | Difficulty: Medium
 * Partition so every part is palindrome. s=aab
 * Pattern: Partition + palindrome check
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) { return {}; }
};

int main() {
    Solution sol;
    cout<<"Test1: aab -> "<<sol.partition("aab").size()<<" (expected 2)"<<endl;
    cout<<"Test2: a -> "<<sol.partition("a").size()<<" (expected 1)"<<endl;
    return 0;
}
