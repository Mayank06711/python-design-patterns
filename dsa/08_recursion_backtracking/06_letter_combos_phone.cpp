/*
 * Letter Combinations of a Phone Number
 * LeetCode: #17 | Difficulty: Medium
 * Digit string -> all letter combos. digits=23
 * Pattern: Multi-way branching per digit
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) { return {}; }
};

int main() {
    Solution sol;
    cout<<"Test1: 23 -> "<<sol.letterCombinations("23").size()<<" (expected 9)"<<endl;
    cout<<"Test2: empty -> "<<sol.letterCombinations("").size()<<" (expected 0)"<<endl;
    return 0;
}
