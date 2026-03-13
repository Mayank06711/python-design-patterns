/*
 * Climbing Stairs
 * LeetCode: #70 | Difficulty: Easy
 * n steps, 1 or 2 at a time. n=3->3
 * Pattern: Fibonacci DP
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int climbStairs(int n) { return 0; }
};

int main() {
    Solution sol;
    cout<<"Test1: "<<sol.climbStairs(2)<<" (expected 2)"<<endl;
    cout<<"Test2: "<<sol.climbStairs(3)<<" (expected 3)"<<endl;
    cout<<"Test3: "<<sol.climbStairs(5)<<" (expected 8)"<<endl;
    return 0;
}
