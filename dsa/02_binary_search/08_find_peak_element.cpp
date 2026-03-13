/*
 * Problem: Find Peak Element
 * LeetCode: #162 | Difficulty: Medium
 *
 * A peak element is an element that is strictly greater than its neighbors.
 * Given a 0-indexed integer array nums, find a peak element and return its
 * index. If the array contains multiple peaks, return the index to any of
 * the peaks. You may imagine that nums[-1] = nums[n] = -infinity.
 * You must write an algorithm that runs in O(log n) time.
 * Hint: Binary search using gradient -- move toward the higher neighbor.
 *
 * Example: nums = [1,2,3,1] -> Output: 2
 * Example: nums = [1,2,1,3,5,6,4] -> Output: 5 (or 1, any peak is valid)
 *
 * Pattern: Binary Search with Gradient / Hill Climbing
 * Company: Facebook, Google, Amazon, Microsoft, Apple
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        // TODO: Binary search -- move toward the side with the larger neighbor
        return 0;
    }
};

int main() {
    Solution sol;

    auto isPeak = [](vector<int>& nums, int idx) {
        if (idx < 0 || idx >= (int)nums.size()) return false;
        bool leftOk = (idx == 0) || (nums[idx] > nums[idx - 1]);
        bool rightOk = (idx == (int)nums.size() - 1) || (nums[idx] > nums[idx + 1]);
        return leftOk && rightOk;
    };

    // Test 1: single peak
    vector<int> nums1 = {1, 2, 3, 1};
    int res1 = sol.findPeakElement(nums1);
    cout << "Test 1: nums=[1,2,3,1] -> " << res1;
    cout << (isPeak(nums1, res1) ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: multiple peaks, any valid
    vector<int> nums2 = {1, 2, 1, 3, 5, 6, 4};
    int res2 = sol.findPeakElement(nums2);
    cout << "Test 2: nums=[1,2,1,3,5,6,4] -> " << res2;
    cout << (isPeak(nums2, res2) ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: single element
    vector<int> nums3 = {1};
    int res3 = sol.findPeakElement(nums3);
    cout << "Test 3: nums=[1] -> " << res3;
    cout << (isPeak(nums3, res3) ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: two elements, first is peak
    vector<int> nums4 = {3, 1};
    int res4 = sol.findPeakElement(nums4);
    cout << "Test 4: nums=[3,1] -> " << res4;
    cout << (isPeak(nums4, res4) ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: strictly increasing (peak at end)
    vector<int> nums5 = {1, 2, 3, 4, 5};
    int res5 = sol.findPeakElement(nums5);
    cout << "Test 5: nums=[1,2,3,4,5] -> " << res5;
    cout << (isPeak(nums5, res5) ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: strictly decreasing (peak at start)
    vector<int> nums6 = {5, 4, 3, 2, 1};
    int res6 = sol.findPeakElement(nums6);
    cout << "Test 6: nums=[5,4,3,2,1] -> " << res6;
    cout << (isPeak(nums6, res6) ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
