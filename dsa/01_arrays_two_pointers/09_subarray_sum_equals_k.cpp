/*
 * Problem: Subarray Sum Equals K
 * LeetCode: #560 | Difficulty: Medium
 * Given an array of integers nums and an integer k, return the total number
 * of subarrays whose sum equals to k.
 * Example: nums = [1,1,1], k = 2 -> 2
 * Pattern: Prefix sum + hash map. If prefix[j] - prefix[i] == k, then
 *          the subarray [i+1..j] sums to k. Store prefix sum frequencies
 *          in a hash map and look up (currentSum - k) at each step.
 * Company: Facebook, Google, Amazon, Microsoft, Bloomberg
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test 1: Basic case
    vector<int> nums1 = {1, 1, 1};
    cout << "Test 1: [1,1,1], k=2 -> " << sol.subarraySum(nums1, 2)
         << " (expected 2)" << endl;

    // Test 2: Single element equal to k
    vector<int> nums2 = {1, 2, 3};
    cout << "Test 2: [1,2,3], k=3 -> " << sol.subarraySum(nums2, 3)
         << " (expected 2)" << endl;

    // Test 3: Negative numbers
    vector<int> nums3 = {1, -1, 0};
    cout << "Test 3: [1,-1,0], k=0 -> " << sol.subarraySum(nums3, 0)
         << " (expected 3)" << endl;

    // Test 4: All zeros
    vector<int> nums4 = {0, 0, 0, 0};
    cout << "Test 4: [0,0,0,0], k=0 -> " << sol.subarraySum(nums4, 0)
         << " (expected 10)" << endl;

    // Test 5: No valid subarray
    vector<int> nums5 = {1, 2, 3};
    cout << "Test 5: [1,2,3], k=7 -> " << sol.subarraySum(nums5, 7)
         << " (expected 0)" << endl;

    return 0;
}
