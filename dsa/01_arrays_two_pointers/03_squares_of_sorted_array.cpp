/*
 * Problem: Squares of a Sorted Array
 * LeetCode: #977 | Difficulty: Easy
 *
 * Given an integer array nums sorted in non-decreasing order, return
 * an array of the squares of each number sorted in non-decreasing order.
 * Use two pointers from both ends since the largest squares come from
 * the extremes (most negative or most positive).
 *
 * Example: [-4,-1,0,3,10] -> [0,1,9,16,100]
 *
 * Pattern: Two Pointers from Both Ends (converging, fill result right to left)
 * Company: Meta, Amazon, Google, Microsoft, Apple
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test case 1: [-4,-1,0,3,10] -> [0,1,9,16,100]
    vector<int> nums1 = {-4, -1, 0, 3, 10};
    vector<int> res1 = sol.sortedSquares(nums1);
    cout << "Test 1: [";
    for (int i = 0; i < (int)res1.size(); i++) {
        cout << res1[i];
        if (i < (int)res1.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Test case 2: [-7,-3,2,3,11] -> [4,9,9,49,121]
    vector<int> nums2 = {-7, -3, 2, 3, 11};
    vector<int> res2 = sol.sortedSquares(nums2);
    cout << "Test 2: [";
    for (int i = 0; i < (int)res2.size(); i++) {
        cout << res2[i];
        if (i < (int)res2.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    // Test case 3: [-1] -> [1]
    vector<int> nums3 = {-1};
    vector<int> res3 = sol.sortedSquares(nums3);
    cout << "Test 3: [";
    for (int i = 0; i < (int)res3.size(); i++) {
        cout << res3[i];
        if (i < (int)res3.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}
