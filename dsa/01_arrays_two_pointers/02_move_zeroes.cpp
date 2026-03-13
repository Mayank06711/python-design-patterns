/*
 * Problem: Move Zeroes
 * LeetCode: #283 | Difficulty: Easy
 *
 * Given an integer array nums, move all 0s to the end of it while
 * maintaining the relative order of the non-zero elements.
 * You must do this in-place without making a copy of the array.
 *
 * Example: [0,1,0,3,12] -> [1,3,12,0,0]
 *
 * Pattern: Read/Write Two Pointers (slow writer, fast reader)
 * Company: Meta, Amazon, Apple, Microsoft, Bloomberg
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test case 1: [0,1,0,3,12] -> [1,3,12,0,0]
    vector<int> nums1 = {0, 1, 0, 3, 12};
    sol.moveZeroes(nums1);
    cout << "Test 1: [";
    for (int i = 0; i < (int)nums1.size(); i++) {
        cout << nums1[i];
        if (i < (int)nums1.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Test case 2: [0] -> [0]
    vector<int> nums2 = {0};
    sol.moveZeroes(nums2);
    cout << "Test 2: [";
    for (int i = 0; i < (int)nums2.size(); i++) {
        cout << nums2[i];
        if (i < (int)nums2.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Test case 3: [1,0,0,2,3,0,4] -> [1,2,3,4,0,0,0]
    vector<int> nums3 = {1, 0, 0, 2, 3, 0, 4};
    sol.moveZeroes(nums3);
    cout << "Test 3: [";
    for (int i = 0; i < (int)nums3.size(); i++) {
        cout << nums3[i];
        if (i < (int)nums3.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}
