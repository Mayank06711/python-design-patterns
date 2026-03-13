/*
 * Problem: Sliding Window Maximum
 * LeetCode: #239 | Difficulty: Hard
 * Given an array nums and a sliding window of size k moving from left to
 * right, return the max value in each window position.
 * Example: nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
 * Pattern: Monotonic decreasing deque. The deque stores indices and
 *          maintains elements in decreasing order. The front of the deque
 *          is always the maximum for the current window. Pop from the
 *          back when a new element is larger (they can never be the max),
 *          and pop from the front when an index falls out of the window.
 * Company: Google, Amazon, Facebook, Microsoft, Uber, Citadel
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // Your solution here
    }
};

void printArray(const vector<int>& arr) {
    cout << "[";
    for (int i = 0; i < (int)arr.size(); i++) {
        cout << arr[i];
        if (i < (int)arr.size() - 1) cout << ",";
    }
    cout << "]";
}

int main() {
    Solution sol;

    // Test 1: Standard case
    vector<int> nums1 = {1, 3, -1, -3, 5, 3, 6, 7};
    auto res1 = sol.maxSlidingWindow(nums1, 3);
    cout << "Test 1: ";
    printArray(res1);
    cout << " (expected [3,3,5,5,6,7])" << endl;

    // Test 2: Window size equals array size
    vector<int> nums2 = {1, 3, -1};
    auto res2 = sol.maxSlidingWindow(nums2, 3);
    cout << "Test 2: ";
    printArray(res2);
    cout << " (expected [3])" << endl;

    // Test 3: Window size of 1
    vector<int> nums3 = {1, -1, 5, 3};
    auto res3 = sol.maxSlidingWindow(nums3, 1);
    cout << "Test 3: ";
    printArray(res3);
    cout << " (expected [1,-1,5,3])" << endl;

    // Test 4: All same elements
    vector<int> nums4 = {7, 7, 7, 7};
    auto res4 = sol.maxSlidingWindow(nums4, 2);
    cout << "Test 4: ";
    printArray(res4);
    cout << " (expected [7,7,7])" << endl;

    // Test 5: Decreasing sequence
    vector<int> nums5 = {9, 8, 7, 6, 5};
    auto res5 = sol.maxSlidingWindow(nums5, 3);
    cout << "Test 5: ";
    printArray(res5);
    cout << " (expected [9,8,7])" << endl;

    // Test 6: Increasing sequence
    vector<int> nums6 = {1, 2, 3, 4, 5};
    auto res6 = sol.maxSlidingWindow(nums6, 3);
    cout << "Test 6: ";
    printArray(res6);
    cout << " (expected [3,4,5])" << endl;

    return 0;
}
