/*
 * Problem: Median of Two Sorted Arrays
 * LeetCode: #4 | Difficulty: Hard
 *
 * Given two sorted arrays nums1 and nums2 of size m and n respectively,
 * return the median of the two sorted arrays.
 * The overall run time complexity should be O(log(min(m, n))).
 * Hint: Binary search on the partition of the smaller array. Find a cut
 * in both arrays such that left elements <= right elements, and both
 * halves have equal total size.
 *
 * Example: nums1 = [1,3], nums2 = [2] -> Output: 2.0
 * Example: nums1 = [1,2], nums2 = [3,4] -> Output: 2.5
 *
 * Pattern: Binary Search on Partition
 * Company: Amazon, Google, Microsoft, Apple, Goldman Sachs, Facebook
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // TODO: Binary search on partition of the smaller array
        return 0.0;
    }
};

int main() {
    Solution sol;

    auto approxEqual = [](double a, double b) {
        return abs(a - b) < 1e-5;
    };

    // Test 1: odd total length
    vector<int> a1 = {1, 3}, b1 = {2};
    double res1 = sol.findMedianSortedArrays(a1, b1);
    cout << "Test 1: [1,3],[2] -> " << res1;
    cout << (approxEqual(res1, 2.0) ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: even total length
    vector<int> a2 = {1, 2}, b2 = {3, 4};
    double res2 = sol.findMedianSortedArrays(a2, b2);
    cout << "Test 2: [1,2],[3,4] -> " << res2;
    cout << (approxEqual(res2, 2.5) ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: one empty array
    vector<int> a3 = {}, b3 = {1};
    double res3 = sol.findMedianSortedArrays(a3, b3);
    cout << "Test 3: [],[1] -> " << res3;
    cout << (approxEqual(res3, 1.0) ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: one empty, even length
    vector<int> a4 = {}, b4 = {2, 3};
    double res4 = sol.findMedianSortedArrays(a4, b4);
    cout << "Test 4: [],[2,3] -> " << res4;
    cout << (approxEqual(res4, 2.5) ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: non-overlapping arrays
    vector<int> a5 = {1, 2}, b5 = {3, 4, 5, 6};
    double res5 = sol.findMedianSortedArrays(a5, b5);
    cout << "Test 5: [1,2],[3,4,5,6] -> " << res5;
    cout << (approxEqual(res5, 3.5) ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: identical elements
    vector<int> a6 = {1, 1, 1}, b6 = {1, 1, 1};
    double res6 = sol.findMedianSortedArrays(a6, b6);
    cout << "Test 6: [1,1,1],[1,1,1] -> " << res6;
    cout << (approxEqual(res6, 1.0) ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
