/*
 * Single Number
 * LeetCode: #136 | Difficulty: Easy
 * XOR all. a^a=0, a^0=a. [2,2,1]->1
 * Pattern: XOR cancellation
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) { return 0; }
};

int main() {
    Solution sol;
    vector<int> a={2,2,1}; cout<<"Test1: "<<sol.singleNumber(a)<<" (expected 1)"<<endl;
    vector<int> b={4,1,2,1,2}; cout<<"Test2: "<<sol.singleNumber(b)<<" (expected 4)"<<endl;
    return 0;
}
