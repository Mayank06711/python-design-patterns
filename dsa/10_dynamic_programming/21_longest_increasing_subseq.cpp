/*
 * Longest Increasing Subsequence
 * LeetCode: #300 | Difficulty: Medium
 * [10,9,2,5,3,7,101,18]->4
 * Pattern: LIS pattern, O(n2) or O(nlogn)
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) { return 0; }
};

int main() {
    Solution sol;
    vector<int> a={10,9,2,5,3,7,101,18}; cout<<"Test1: "<<sol.lengthOfLIS(a)<<" (expected 4)"<<endl;
    vector<int> b={0,1,0,3,2,3}; cout<<"Test2: "<<sol.lengthOfLIS(b)<<" (expected 4)"<<endl;
    return 0;
}
