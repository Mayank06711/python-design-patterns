/*
 * Problem: Search a 2D Matrix
 * LeetCode: #74 | Difficulty: Medium
 *
 * You are given an m x n integer matrix with the following properties:
 * - Each row is sorted in non-decreasing order.
 * - The first integer of each row is greater than the last integer of
 *   the previous row.
 * Given an integer target, return true if target is in the matrix.
 * Hint: Treat the 2D matrix as a single sorted 1D array and binary search.
 *
 * Example: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> true
 * Example: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13 -> false
 *
 * Pattern: Binary Search on Virtual 1D Array (2D mapped to 1D)
 * Company: Amazon, Microsoft, Apple, Facebook, Bloomberg
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // TODO: Map 2D indices to 1D and binary search
        return false;
    }
};

int main() {
    Solution sol;

    // Test 1: target exists
    vector<vector<int>> mat1 = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    bool res1 = sol.searchMatrix(mat1, 3);
    cout << "Test 1: target=3 -> " << (res1 ? "true" : "false");
    cout << (res1 == true ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: target does not exist
    bool res2 = sol.searchMatrix(mat1, 13);
    cout << "Test 2: target=13 -> " << (res2 ? "true" : "false");
    cout << (res2 == false ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: target is first element
    bool res3 = sol.searchMatrix(mat1, 1);
    cout << "Test 3: target=1 -> " << (res3 ? "true" : "false");
    cout << (res3 == true ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: target is last element
    bool res4 = sol.searchMatrix(mat1, 60);
    cout << "Test 4: target=60 -> " << (res4 ? "true" : "false");
    cout << (res4 == true ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: single row matrix
    vector<vector<int>> mat5 = {{1, 3, 5, 7}};
    bool res5 = sol.searchMatrix(mat5, 5);
    cout << "Test 5: single row, target=5 -> " << (res5 ? "true" : "false");
    cout << (res5 == true ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: single element matrix, not found
    vector<vector<int>> mat6 = {{1}};
    bool res6 = sol.searchMatrix(mat6, 2);
    cout << "Test 6: single element, target=2 -> " << (res6 ? "true" : "false");
    cout << (res6 == false ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
