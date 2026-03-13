/*
 * Problem: Trapping Rain Water
 * LeetCode: #42 | Difficulty: Hard
 * Given n non-negative integers representing an elevation map where the
 * width of each bar is 1, compute how much water it can trap after raining.
 * Example: height = [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
 * Pattern: Two pointers with left_max and right_max. Water at any position
 *          is min(left_max, right_max) - height[i]. Move the pointer with
 *          the smaller max inward, because the bottleneck is always the
 *          shorter side.
 * Company: Google, Amazon, Facebook, Microsoft, Goldman Sachs, Apple
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        // Your solution here
    }
};

int main() {
    Solution sol;

    // Test 1: Classic example
    vector<int> h1 = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    cout << "Test 1: [0,1,0,2,1,0,1,3,2,1,2,1] -> " << sol.trap(h1)
         << " (expected 6)" << endl;

    // Test 2: Simple V shape
    vector<int> h2 = {4, 2, 0, 3, 2, 5};
    cout << "Test 2: [4,2,0,3,2,5] -> " << sol.trap(h2)
         << " (expected 9)" << endl;

    // Test 3: No water (ascending)
    vector<int> h3 = {1, 2, 3, 4, 5};
    cout << "Test 3: [1,2,3,4,5] -> " << sol.trap(h3)
         << " (expected 0)" << endl;

    // Test 4: No water (descending)
    vector<int> h4 = {5, 4, 3, 2, 1};
    cout << "Test 4: [5,4,3,2,1] -> " << sol.trap(h4)
         << " (expected 0)" << endl;

    // Test 5: Empty or too small
    vector<int> h5 = {2, 1};
    cout << "Test 5: [2,1] -> " << sol.trap(h5)
         << " (expected 0)" << endl;

    // Test 6: Flat with dip
    vector<int> h6 = {3, 0, 3};
    cout << "Test 6: [3,0,3] -> " << sol.trap(h6)
         << " (expected 3)" << endl;

    return 0;
}
