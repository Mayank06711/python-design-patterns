/*
 * Coin Change II
 * LeetCode: #518 | Difficulty: Medium
 * Number of combos. coins=[1,2,5] amount=5->4
 * Pattern: Unbounded knapsack (count)
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int change(int amount, vector<int>& coins) { return 0; }
};

int main() {
    Solution sol;
    vector<int> c={1,2,5}; cout<<"Test: "<<sol.change(5,c)<<" (expected 4)"<<endl;
    return 0;
}
