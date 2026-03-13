/*
 * Problem: Two Sum
 * LeetCode: #1 | Difficulty: Easy
 *
 * Given an array of integers nums and an integer target, return indices
 * of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution,
 * and you may not use the same element twice.
 *
 * Example: nums = [2,7,11,15], target = 9 -> [0,1]
 *
 * Pattern: Hash Map Complement Lookup
 * Company: Amazon, Google, Meta, Apple, Microsoft, Bloomberg
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test case 1: nums = [2,7,11,15], target = 9 -> [0,1]
    vector<int> nums1 = {2, 7, 11, 15};
    vector<int> res1 = sol.twoSum(nums1, 9);
    cout << "Test 1: [" << res1[0] << ", " << res1[1] << "]" << endl;

    // Test case 2: nums = [3,2,4], target = 6 -> [1,2]
    vector<int> nums2 = {3, 2, 4};
    vector<int> res2 = sol.twoSum(nums2, 6);
    cout << "Test 2: [" << res2[0] << ", " << res2[1] << "]" << endl;

    // Test case 3: nums = [3,3], target = 6 -> [0,1]
    vector<int> nums3 = {3, 3};
    vector<int> res3 = sol.twoSum(nums3, 6);
    cout << "Test 3: [" << res3[0] << ", " << res3[1] << "]" << endl;

    return 0;
}
