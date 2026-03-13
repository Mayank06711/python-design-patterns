/*
 * Word Break
 * LeetCode: #139 | Difficulty: Medium
 * Can segment into dict words? leetcode,[leet,code]->true
 * Pattern: String partition DP
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) { return false; }
};

int main() {
    Solution sol;
    vector<string> d={"leet","code"}; cout<<"Test1: "<<sol.wordBreak("leetcode",d)<<" (expected 1)"<<endl;
    vector<string> e={"cats","dog","sand","and","cat"}; cout<<"Test2: "<<sol.wordBreak("catsandog",e)<<" (expected 0)"<<endl;
    return 0;
}
