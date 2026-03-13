/*
 * Problem: Find Minimum in Rotated Sorted Array
 * LeetCode: #153 | Difficulty: Medium
 *
 * Given a sorted rotated array of unique elements, return the minimum
 * element. You must write an algorithm that runs in O(log n) time.
 * The array was originally sorted in ascending order and then rotated
 * between 1 and n times.
 *
 * Example: nums = [3,4,5,1,2] -> Output: 1
 * Example: nums = [4,5,6,7,0,1,2] -> Output: 0
 * Example: nums = [11,13,15,17] -> Output: 11
 *
 * Pattern: Binary Search on Rotated Array
 * Company: Amazon, Microsoft, Facebook, Google, Bloomberg
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        // TODO: Binary search comparing mid with right boundary
        return -1;
    }
};

int main() {
    Solution sol;

    // Test 1: rotated array
    vector<int> nums1 = {3, 4, 5, 1, 2};
    int result1 = sol.findMin(nums1);
    cout << "Test 1: nums=[3,4,5,1,2] -> " << result1;
    cout << (result1 == 1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: rotated array with more elements
    vector<int> nums2 = {4, 5, 6, 7, 0, 1, 2};
    int result2 = sol.findMin(nums2);
    cout << "Test 2: nums=[4,5,6,7,0,1,2] -> " << result2;
    cout << (result2 == 0 ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: not rotated (sorted)
    vector<int> nums3 = {11, 13, 15, 17};
    int result3 = sol.findMin(nums3);
    cout << "Test 3: nums=[11,13,15,17] -> " << result3;
    cout << (result3 == 11 ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: two elements
    vector<int> nums4 = {2, 1};
    int result4 = sol.findMin(nums4);
    cout << "Test 4: nums=[2,1] -> " << result4;
    cout << (result4 == 1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: single element
    vector<int> nums5 = {1};
    int result5 = sol.findMin(nums5);
    cout << "Test 5: nums=[1] -> " << result5;
    cout << (result5 == 1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: rotated by one position
    vector<int> nums6 = {2, 3, 4, 5, 1};
    int result6 = sol.findMin(nums6);
    cout << "Test 6: nums=[2,3,4,5,1] -> " << result6;
    cout << (result6 == 1 ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
