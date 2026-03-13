/*
 * Trapping Rain Water (Stack)
 * LeetCode: #42 | Difficulty: Hard
 * Monotonic decreasing stack approach. [0,1,0,2,1,0,1,3,2,1,2,1]->6
 * Pattern: Monotonic decreasing stack
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) { return 0; }
};

int main() {
    Solution sol;
    vector<int> h={0,1,0,2,1,0,1,3,2,1,2,1}; cout<<"Test: "<<sol.trap(h)<<" (expected 6)"<<endl;
    return 0;
}
