/*
 * Problem: Binary Search
 * LeetCode: #704 | Difficulty: Easy
 *
 * Given a sorted array of integers nums and a target value, return the
 * index if the target is found. If not, return -1.
 * You must write an algorithm with O(log n) runtime complexity.
 *
 * Example: nums = [-1,0,3,5,9,12], target = 9 -> Output: 4
 * Example: nums = [-1,0,3,5,9,12], target = 2 -> Output: -1
 *
 * Pattern: Vanilla Binary Search
 * Company: Amazon, Microsoft, Google, Facebook, Apple
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // TODO: Implement binary search
        return -1;
    }
};

int main() {
    Solution sol;

    // Test 1: target exists in array
    vector<int> nums1 = {-1, 0, 3, 5, 9, 12};
    int result1 = sol.search(nums1, 9);
    cout << "Test 1: nums=[-1,0,3,5,9,12], target=9 -> " << result1;
    cout << (result1 == 4 ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: target does not exist
    int result2 = sol.search(nums1, 2);
    cout << "Test 2: nums=[-1,0,3,5,9,12], target=2 -> " << result2;
    cout << (result2 == -1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: single element found
    vector<int> nums3 = {5};
    int result3 = sol.search(nums3, 5);
    cout << "Test 3: nums=[5], target=5 -> " << result3;
    cout << (result3 == 0 ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: single element not found
    int result4 = sol.search(nums3, -1);
    cout << "Test 4: nums=[5], target=-1 -> " << result4;
    cout << (result4 == -1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: target is the first element
    int result5 = sol.search(nums1, -1);
    cout << "Test 5: nums=[-1,0,3,5,9,12], target=-1 -> " << result5;
    cout << (result5 == 0 ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: target is the last element
    int result6 = sol.search(nums1, 12);
    cout << "Test 6: nums=[-1,0,3,5,9,12], target=12 -> " << result6;
    cout << (result6 == 5 ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
