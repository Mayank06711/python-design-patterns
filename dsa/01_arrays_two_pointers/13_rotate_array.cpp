/*
 * Problem: Rotate Array
 * LeetCode: #189 | Difficulty: Medium
 * Given an integer array nums, rotate the array to the right by k steps,
 * where k is non-negative. Do this in-place with O(1) extra space.
 * Example: nums = [1,2,3,4,5,6,7], k = 3 -> [5,6,7,1,2,3,4]
 * Pattern: Three-reverse trick (O(n) time, O(1) space):
 *   1. Reverse the entire array.
 *   2. Reverse the first k elements.
 *   3. Reverse the remaining n-k elements.
 *   This works because reversing twice restores order but shifts position.
 * Company: Amazon, Microsoft, Facebook, Google, Apple
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
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

    // Test 1: Standard rotation
    vector<int> nums1 = {1, 2, 3, 4, 5, 6, 7};
    sol.rotate(nums1, 3);
    cout << "Test 1: ";
    printArray(nums1);
    cout << " (expected [5,6,7,1,2,3,4])" << endl;

    // Test 2: k equals array length (no change)
    vector<int> nums2 = {1, 2, 3};
    sol.rotate(nums2, 3);
    cout << "Test 2: ";
    printArray(nums2);
    cout << " (expected [1,2,3])" << endl;

    // Test 3: k greater than array length
    vector<int> nums3 = {-1, -100, 3, 99};
    sol.rotate(nums3, 2);
    cout << "Test 3: ";
    printArray(nums3);
    cout << " (expected [3,99,-1,-100])" << endl;

    // Test 4: Single element
    vector<int> nums4 = {1};
    sol.rotate(nums4, 5);
    cout << "Test 4: ";
    printArray(nums4);
    cout << " (expected [1])" << endl;

    // Test 5: Rotate by 1
    vector<int> nums5 = {1, 2, 3, 4};
    sol.rotate(nums5, 1);
    cout << "Test 5: ";
    printArray(nums5);
    cout << " (expected [4,1,2,3])" << endl;

    return 0;
}
