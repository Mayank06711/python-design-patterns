/*
 * Coin Change
 * LeetCode: #322 | Difficulty: Medium
 * Min coins. coins=[1,2,5] amount=11->3
 * Pattern: Unbounded knapsack (min)
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) { return 0; }
};

int main() {
    Solution sol;
    vector<int> c={1,2,5}; cout<<"Test1: "<<sol.coinChange(c,11)<<" (expected 3)"<<endl;
    vector<int> d={2}; cout<<"Test2: "<<sol.coinChange(d,3)<<" (expected -1)"<<endl;
    return 0;
}
