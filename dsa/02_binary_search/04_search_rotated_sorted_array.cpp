/*
 * Problem: Search in Rotated Sorted Array
 * LeetCode: #33 | Difficulty: Medium
 *
 * Given an integer array nums sorted in ascending order with distinct values
 * that has been rotated at an unknown pivot, and a target value, return the
 * index of target if found, or -1 if not found.
 * You must write an algorithm with O(log n) runtime.
 * Hint: Identify which half is sorted, then decide which half to search.
 *
 * Example: nums = [4,5,6,7,0,1,2], target = 0 -> Output: 4
 * Example: nums = [4,5,6,7,0,1,2], target = 3 -> Output: -1
 *
 * Pattern: Modified Binary Search - Identify Sorted Half
 * Company: Facebook, Amazon, Microsoft, Google, Bloomberg, Uber, Apple
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // TODO: Identify sorted half, then decide direction
        return -1;
    }
};

int main() {
    Solution sol;

    // Test 1: target in right portion
    vector<int> nums1 = {4, 5, 6, 7, 0, 1, 2};
    int result1 = sol.search(nums1, 0);
    cout << "Test 1: nums=[4,5,6,7,0,1,2], target=0 -> " << result1;
    cout << (result1 == 4 ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: target not found
    int result2 = sol.search(nums1, 3);
    cout << "Test 2: nums=[4,5,6,7,0,1,2], target=3 -> " << result2;
    cout << (result2 == -1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: single element found
    vector<int> nums3 = {1};
    int result3 = sol.search(nums3, 1);
    cout << "Test 3: nums=[1], target=1 -> " << result3;
    cout << (result3 == 0 ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: single element not found
    int result4 = sol.search(nums3, 0);
    cout << "Test 4: nums=[1], target=0 -> " << result4;
    cout << (result4 == -1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: target in left portion
    int result5 = sol.search(nums1, 5);
    cout << "Test 5: nums=[4,5,6,7,0,1,2], target=5 -> " << result5;
    cout << (result5 == 1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: no rotation (already sorted)
    vector<int> nums6 = {1, 2, 3, 4, 5};
    int result6 = sol.search(nums6, 3);
    cout << "Test 6: nums=[1,2,3,4,5], target=3 -> " << result6;
    cout << (result6 == 2 ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
