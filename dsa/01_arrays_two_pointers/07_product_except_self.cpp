/*
 * Problem: Product of Array Except Self
 * LeetCode: #238 | Difficulty: Medium
 *
 * Given an integer array nums, return an array answer such that
 * answer[i] is equal to the product of all the elements of nums
 * except nums[i]. The product of any prefix or suffix of nums is
 * guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without
 * using the division operation.
 * Use prefix product from left, then suffix product from right.
 *
 * Example: [1,2,3,4] -> [24,12,8,6]
 *
 * Pattern: Prefix/Suffix Product (no division allowed)
 * Company: Amazon, Meta, Google, Apple, Microsoft, Bloomberg
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test case 1: [1,2,3,4] -> [24,12,8,6]
    vector<int> nums1 = {1, 2, 3, 4};
    vector<int> res1 = sol.productExceptSelf(nums1);
    cout << "Test 1: [";
    for (int i = 0; i < (int)res1.size(); i++) {
        cout << res1[i];
        if (i < (int)res1.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Test case 2: [-1,1,0,-3,3] -> [0,0,9,0,0]
    vector<int> nums2 = {-1, 1, 0, -3, 3};
    vector<int> res2 = sol.productExceptSelf(nums2);
    cout << "Test 2: [";
    for (int i = 0; i < (int)res2.size(); i++) {
        cout << res2[i];
        if (i < (int)res2.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Test case 3: [2,3,4,5] -> [60,40,30,24]
    vector<int> nums3 = {2, 3, 4, 5};
    vector<int> res3 = sol.productExceptSelf(nums3);
    cout << "Test 3: [";
    for (int i = 0; i < (int)res3.size(); i++) {
        cout << res3[i];
        if (i < (int)res3.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}
