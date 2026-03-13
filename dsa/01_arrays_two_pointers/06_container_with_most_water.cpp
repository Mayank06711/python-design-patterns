/*
 * Problem: Container With Most Water
 * LeetCode: #11 | Difficulty: Medium
 *
 * You are given an integer array height of length n. There are n
 * vertical lines drawn such that the two endpoints of the ith line
 * are (i, 0) and (i, height[i]). Find two lines that together with
 * the x-axis form a container that holds the most water.
 * Return the maximum amount of water a container can store.
 * Always move the pointer pointing to the shorter line inward.
 *
 * Example: [1,8,6,2,5,4,8,3,7] -> 49
 *
 * Pattern: Converging Two Pointers - Shrink Shorter Side
 * Company: Amazon, Google, Meta, Microsoft, Goldman Sachs
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test case 1: [1,8,6,2,5,4,8,3,7] -> 49
    vector<int> h1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << "Test 1: " << sol.maxArea(h1) << endl;

    // Test case 2: [1,1] -> 1
    vector<int> h2 = {1, 1};
    cout << "Test 2: " << sol.maxArea(h2) << endl;

    // Test case 3: [4,3,2,1,4] -> 16
    vector<int> h3 = {4, 3, 2, 1, 4};
    cout << "Test 3: " << sol.maxArea(h3) << endl;

    return 0;
}
