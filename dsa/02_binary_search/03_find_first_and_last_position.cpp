/*
 * Problem: Find First and Last Position of Element in Sorted Array
 * LeetCode: #34 | Difficulty: Medium
 *
 * Given an array of integers sorted in non-decreasing order, find the
 * starting and ending position of a given target value.
 * If target is not found, return [-1, -1].
 * You must write an algorithm with O(log n) runtime.
 * Hint: Use two binary searches -- one for left bound, one for right bound.
 *
 * Example: nums = [5,7,7,8,8,10], target = 8 -> Output: [3,4]
 * Example: nums = [5,7,7,8,8,10], target = 6 -> Output: [-1,-1]
 *
 * Pattern: Two Binary Searches (Left Bound + Right Bound)
 * Company: Facebook, Amazon, Google, LinkedIn, Microsoft, Bloomberg
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        // TODO: Implement left bound + right bound binary searches
        return {-1, -1};
    }
};

int main() {
    Solution sol;

    auto printResult = [](vector<int>& res) {
        cout << "[" << res[0] << "," << res[1] << "]";
    };

    // Test 1: target found with multiple occurrences
    vector<int> nums1 = {5, 7, 7, 8, 8, 10};
    vector<int> res1 = sol.searchRange(nums1, 8);
    cout << "Test 1: nums=[5,7,7,8,8,10], target=8 -> ";
    printResult(res1);
    cout << (res1[0] == 3 && res1[1] == 4 ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: target not found
    vector<int> res2 = sol.searchRange(nums1, 6);
    cout << "Test 2: nums=[5,7,7,8,8,10], target=6 -> ";
    printResult(res2);
    cout << (res2[0] == -1 && res2[1] == -1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: empty array
    vector<int> nums3 = {};
    vector<int> res3 = sol.searchRange(nums3, 0);
    cout << "Test 3: nums=[], target=0 -> ";
    printResult(res3);
    cout << (res3[0] == -1 && res3[1] == -1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: single occurrence
    vector<int> res4 = sol.searchRange(nums1, 10);
    cout << "Test 4: nums=[5,7,7,8,8,10], target=10 -> ";
    printResult(res4);
    cout << (res4[0] == 5 && res4[1] == 5 ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: all elements are target
    vector<int> nums5 = {2, 2, 2, 2};
    vector<int> res5 = sol.searchRange(nums5, 2);
    cout << "Test 5: nums=[2,2,2,2], target=2 -> ";
    printResult(res5);
    cout << (res5[0] == 0 && res5[1] == 3 ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: target at beginning only
    vector<int> res6 = sol.searchRange(nums1, 5);
    cout << "Test 6: nums=[5,7,7,8,8,10], target=5 -> ";
    printResult(res6);
    cout << (res6[0] == 0 && res6[1] == 0 ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
