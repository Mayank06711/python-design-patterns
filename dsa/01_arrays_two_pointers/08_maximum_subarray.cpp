/*
 * Problem: Maximum Subarray
 * LeetCode: #53 | Difficulty: Medium
 *
 * Given an integer array nums, find the subarray with the largest sum,
 * and return its sum.
 * Use Kadane algorithm: at each position, decide whether to extend
 * the current subarray or start a new one.
 * local_max = max(nums[i], local_max + nums[i])
 * global_max = max(global_max, local_max)
 *
 * Example: [-2,1,-3,4,-1,2,1,-5,4] -> 6 (subarray [4,-1,2,1])
 *
 * Pattern: Kadane Algorithm (dynamic programming / greedy)
 * Company: Amazon, Google, Meta, Microsoft, Apple, LinkedIn
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test case 1: [-2,1,-3,4,-1,2,1,-5,4] -> 6
    vector<int> nums1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Test 1: " << sol.maxSubArray(nums1) << endl;

    // Test case 2: [1] -> 1
    vector<int> nums2 = {1};
    cout << "Test 2: " << sol.maxSubArray(nums2) << endl;

    // Test case 3: [5,4,-1,7,8] -> 23
    vector<int> nums3 = {5, 4, -1, 7, 8};
    cout << "Test 3: " << sol.maxSubArray(nums3) << endl;

    // Test case 4: [-1] -> -1
    vector<int> nums4 = {-1};
    cout << "Test 4: " << sol.maxSubArray(nums4) << endl;

    return 0;
}
