/*
 * Problem: Maximum Product Subarray
 * LeetCode: #152 | Difficulty: Medium
 * Given an integer array nums, find a subarray that has the largest product,
 * and return the product.
 * Example: nums = [2,3,-2,4] -> 6 (subarray [2,3])
 * Pattern: Track both min AND max products ending at each position because
 *          a negative number can flip the min to become the max. At each
 *          step, the new max/min is one of: num, maxSoFar*num, minSoFar*num.
 * Company: Amazon, Google, Microsoft, LinkedIn, Apple
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test 1: Standard case with negative in middle
    vector<int> nums1 = {2, 3, -2, 4};
    cout << "Test 1: [2,3,-2,4] -> " << sol.maxProduct(nums1)
         << " (expected 6)" << endl;

    // Test 2: Two negatives make a positive
    vector<int> nums2 = {-2, 0, -1};
    cout << "Test 2: [-2,0,-1] -> " << sol.maxProduct(nums2)
         << " (expected 0)" << endl;

    // Test 3: All negative, even count
    vector<int> nums3 = {-2, -3, -4};
    cout << "Test 3: [-2,-3,-4] -> " << sol.maxProduct(nums3)
         << " (expected 24)" << endl;

    // Test 4: Single element
    vector<int> nums4 = {-2};
    cout << "Test 4: [-2] -> " << sol.maxProduct(nums4)
         << " (expected -2)" << endl;

    // Test 5: Contains zero in between
    vector<int> nums5 = {2, -5, -2, -4, 3};
    cout << "Test 5: [2,-5,-2,-4,3] -> " << sol.maxProduct(nums5)
         << " (expected 24)" << endl;

    return 0;
}
