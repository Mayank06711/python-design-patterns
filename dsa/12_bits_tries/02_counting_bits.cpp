/*
 * Counting Bits
 * LeetCode: #338 | Difficulty: Easy
 * dp[i]=dp[i>>1]+(i&1). n=5->[0,1,1,2,1,2]
 * Pattern: Bit DP
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countBits(int n) { return {}; }
};

int main() {
    Solution sol;
    auto r=sol.countBits(5);
    cout<<"Test: size="<<r.size()<<" (expected 6)"<<endl;
    return 0;
}
