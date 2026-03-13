/*
 * Problem: 3Sum
 * LeetCode: #15 | Difficulty: Medium
 *
 * Given an integer array nums, return all the triplets
 * [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
 * and nums[i] + nums[j] + nums[k] == 0.
 * The solution set must not contain duplicate triplets.
 * Sort the array, fix one element, then use two pointers on the rest.
 * Skip duplicate values to avoid duplicate triplets.
 *
 * Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
 *
 * Pattern: Sort + Fix One + Two Pointer + Skip Duplicates
 * Company: Amazon, Meta, Google, Microsoft, Apple, Bloomberg
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test case 1: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    vector<int> nums1 = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> res1 = sol.threeSum(nums1);
    cout << "Test 1: [";
    for (int i = 0; i < (int)res1.size(); i++) {
        cout << "[" << res1[i][0] << ", " << res1[i][1] << ", " << res1[i][2] << "]";
        if (i < (int)res1.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Test case 2: [0,1,1] -> []
    vector<int> nums2 = {0, 1, 1};
    vector<vector<int>> res2 = sol.threeSum(nums2);
    cout << "Test 2: [";
    for (int i = 0; i < (int)res2.size(); i++) {
        cout << "[" << res2[i][0] << ", " << res2[i][1] << ", " << res2[i][2] << "]";
        if (i < (int)res2.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Test case 3: [0,0,0] -> [[0,0,0]]
    vector<int> nums3 = {0, 0, 0};
    vector<vector<int>> res3 = sol.threeSum(nums3);
    cout << "Test 3: [";
    for (int i = 0; i < (int)res3.size(); i++) {
        cout << "[" << res3[i][0] << ", " << res3[i][1] << ", " << res3[i][2] << "]";
        if (i < (int)res3.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}
