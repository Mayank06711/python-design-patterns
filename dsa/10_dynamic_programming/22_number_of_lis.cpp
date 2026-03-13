/*
 * Number of LIS
 * LeetCode: #673 | Difficulty: Medium
 * Count all LIS. [1,3,5,4,7]->2
 * Pattern: Track count[] alongside length[]
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) { return 0; }
};

int main() {
    Solution sol;
    vector<int> a={1,3,5,4,7}; cout<<"Test1: "<<sol.findNumberOfLIS(a)<<" (expected 2)"<<endl;
    vector<int> b={2,2,2,2,2}; cout<<"Test2: "<<sol.findNumberOfLIS(b)<<" (expected 5)"<<endl;
    return 0;
}
