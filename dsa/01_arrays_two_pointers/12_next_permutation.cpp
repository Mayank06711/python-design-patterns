/*
 * Problem: Next Permutation
 * LeetCode: #31 | Difficulty: Medium
 * A permutation of an array of integers is an arrangement of its members
 * into a sequence. Find the next lexicographically greater permutation.
 * If no such permutation exists, rearrange to the lowest possible order.
 * Example: [1,2,3] -> [1,3,2]
 * Pattern: Three steps:
 *   1. Find the rightmost ascent: largest i such that nums[i] < nums[i+1].
 *   2. Find the smallest element to the right of i that is larger than
 *      nums[i], and swap them.
 *   3. Reverse the suffix after position i.
 *   If no ascent exists, the array is the last permutation -- just reverse it.
 * Company: Google, Facebook, Amazon, Microsoft, Apple
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
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
    vector<int> nums1 = {1, 2, 3};
    sol.nextPermutation(nums1);
    cout << "Test 1: ";
    printArray(nums1);
    cout << " (expected [1,3,2])" << endl;

    // Test 2: Last permutation wraps to first
    vector<int> nums2 = {3, 2, 1};
    sol.nextPermutation(nums2);
    cout << "Test 2: ";
    printArray(nums2);
    cout << " (expected [1,2,3])" << endl;

    // Test 3: Middle permutation
    vector<int> nums3 = {1, 1, 5};
    sol.nextPermutation(nums3);
    cout << "Test 3: ";
    printArray(nums3);
    cout << " (expected [1,5,1])" << endl;

    // Test 4: Longer array
    vector<int> nums4 = {1, 3, 5, 4, 2};
    sol.nextPermutation(nums4);
    cout << "Test 4: ";
    printArray(nums4);
    cout << " (expected [1,4,2,3,5])" << endl;

    // Test 5: Single element
    vector<int> nums5 = {1};
    sol.nextPermutation(nums5);
    cout << "Test 5: ";
    printArray(nums5);
    cout << " (expected [1])" << endl;

    return 0;
}
