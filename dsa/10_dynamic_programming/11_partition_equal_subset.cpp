/*
 * Partition Equal Subset Sum
 * LeetCode: #416 | Difficulty: Medium
 * Can split into two equal-sum subsets? [1,5,11,5]->true
 * Pattern: 0/1 Knapsack
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) { return false; }
};

int main() {
    Solution sol;
    vector<int> a={1,5,11,5}; cout<<"Test1: "<<sol.canPartition(a)<<" (expected 1)"<<endl;
    vector<int> b={1,2,3,5}; cout<<"Test2: "<<sol.canPartition(b)<<" (expected 0)"<<endl;
    return 0;
}
