/*
 * Russian Doll Envelopes
 * LeetCode: #354 | Difficulty: Hard
 * Sort+LIS. [[5,4],[6,4],[6,7],[2,3]]->3
 * Pattern: Sort + LIS (dimensional reduction)
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& env) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> e={{5,4},{6,4},{6,7},{2,3}};
    cout<<"Test: "<<sol.maxEnvelopes(e)<<" (expected 3)"<<endl;
    return 0;
}
