/*
 * House Robber
 * LeetCode: #198 | Difficulty: Medium
 * Max money, no adjacent. [1,2,3,1]->4
 * Pattern: Take or skip
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) { return 0; }
};

int main() {
    Solution sol;
    vector<int> a={1,2,3,1}; cout<<"Test1: "<<sol.rob(a)<<" (expected 4)"<<endl;
    vector<int> b={2,7,9,3,1}; cout<<"Test2: "<<sol.rob(b)<<" (expected 12)"<<endl;
    return 0;
}
