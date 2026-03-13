/*
 * Problem: Search Insert Position
 * LeetCode: #35 | Difficulty: Easy
 *
 * Given a sorted array of distinct integers and a target value, return
 * the index if the target is found. If not, return the index where it
 * would be inserted in order.
 * This is equivalent to finding the lower_bound (bisect_left).
 * You must write an algorithm with O(log n) runtime.
 *
 * Example: nums = [1,3,5,6], target = 5 -> Output: 2
 * Example: nums = [1,3,5,6], target = 2 -> Output: 1
 * Example: nums = [1,3,5,6], target = 7 -> Output: 4
 *
 * Pattern: Lower Bound / Bisect Left Binary Search
 * Company: Amazon, Google, Apple, Bloomberg, Adobe
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // TODO: Implement lower bound binary search
        return 0;
    }
};

int main() {
    Solution sol;

    // Test 1: target exists in array
    vector<int> nums1 = {1, 3, 5, 6};
    int result1 = sol.searchInsert(nums1, 5);
    cout << "Test 1: nums=[1,3,5,6], target=5 -> " << result1;
    cout << (result1 == 2 ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: target needs to be inserted in middle
    int result2 = sol.searchInsert(nums1, 2);
    cout << "Test 2: nums=[1,3,5,6], target=2 -> " << result2;
    cout << (result2 == 1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: target larger than all elements
    int result3 = sol.searchInsert(nums1, 7);
    cout << "Test 3: nums=[1,3,5,6], target=7 -> " << result3;
    cout << (result3 == 4 ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: target smaller than all elements
    int result4 = sol.searchInsert(nums1, 0);
    cout << "Test 4: nums=[1,3,5,6], target=0 -> " << result4;
    cout << (result4 == 0 ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: single element, target equals
    vector<int> nums5 = {1};
    int result5 = sol.searchInsert(nums5, 1);
    cout << "Test 5: nums=[1], target=1 -> " << result5;
    cout << (result5 == 0 ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: insert between elements
    int result6 = sol.searchInsert(nums1, 4);
    cout << "Test 6: nums=[1,3,5,6], target=4 -> " << result6;
    cout << (result6 == 2 ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
