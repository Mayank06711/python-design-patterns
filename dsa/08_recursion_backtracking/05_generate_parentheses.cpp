/*
 * Generate Parentheses
 * LeetCode: #22 | Difficulty: Medium
 * Generate all valid combos of n pairs of parens
 * Pattern: Constraint branching (open<n, close<open)
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) { return {}; }
};

int main() {
    Solution sol;
    cout<<"Test1: n=3 -> "<<sol.generateParenthesis(3).size()<<" (expected 5)"<<endl;
    cout<<"Test2: n=1 -> "<<sol.generateParenthesis(1).size()<<" (expected 1)"<<endl;
    cout<<"Test3: n=4 -> "<<sol.generateParenthesis(4).size()<<" (expected 14)"<<endl;
    return 0;
}
