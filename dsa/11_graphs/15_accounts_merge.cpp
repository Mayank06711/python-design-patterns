/*
 * Accounts Merge
 * LeetCode: #721 | Difficulty: Medium
 * Merge accounts sharing emails
 * Pattern: Union-Find grouping
 * Company: Meta, Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) { return {}; }
};

int main() {
    Solution sol;
    vector<vector<string>> a={{"John","j1@e","j2@e"},{"John","j1@e","j3@e"},{"Mary","m@e"}};
    auto r=sol.accountsMerge(a);
    cout<<"Test: "<<r.size()<<" accounts (expected 2)"<<endl;
    return 0;
}
