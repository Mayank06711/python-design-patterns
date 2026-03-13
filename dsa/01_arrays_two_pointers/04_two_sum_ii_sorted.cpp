/*
 * Problem: Two Sum II - Input Array Is Sorted
 * LeetCode: #167 | Difficulty: Medium
 *
 * Given a 1-indexed array of integers numbers that is already sorted
 * in non-decreasing order, find two numbers such that they add up to
 * a specific target number. Return the indices of the two numbers
 * (1-indexed) as an integer array of length 2.
 * You must use only constant extra space.
 *
 * Example: numbers = [2,7,11,15], target = 9 -> [1,2]
 *
 * Pattern: Converging Two Pointers (left and right moving inward)
 * Company: Amazon, Google, Meta, Apple, Bloomberg
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test case 1: [2,7,11,15], target = 9 -> [1,2]
    vector<int> nums1 = {2, 7, 11, 15};
    vector<int> res1 = sol.twoSum(nums1, 9);
    cout << "Test 1: [" << res1[0] << ", " << res1[1] << "]" << endl;

    // Test case 2: [2,3,4], target = 6 -> [1,3]
    vector<int> nums2 = {2, 3, 4};
    vector<int> res2 = sol.twoSum(nums2, 6);
    cout << "Test 2: [" << res2[0] << ", " << res2[1] << "]" << endl;

    // Test case 3: [-1,0], target = -1 -> [1,2]
    vector<int> nums3 = {-1, 0};
    vector<int> res3 = sol.twoSum(nums3, -1);
    cout << "Test 3: [" << res3[0] << ", " << res3[1] << "]" << endl;

    return 0;
}
