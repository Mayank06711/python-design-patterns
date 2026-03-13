/*
 * Problem: Kth Largest Element in an Array (LeetCode #215) - Medium
 *
 * Given an integer array nums and an integer k, return the kth largest
 * element in the array (kth in sorted order, not kth distinct).
 *
 * Approach 1: Quickselect - O(n) average, O(n^2) worst
 *   - Partition around a random pivot. If pivot index == n-k, found it.
 *   - Otherwise recurse into the correct half.
 *
 * Approach 2: Min-heap of size k - O(n log k)
 *   - Push elements into a min-heap; if size > k, pop smallest.
 *   - After all elements, heap top = kth largest.
 *
 * Time:  O(n) avg quickselect / O(n log k) heap
 * Space: O(1) quickselect / O(k) heap
 *
 * Example: [3,2,1,5,6,4] k=2 -> 5
 */

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // TODO: implement quickselect or min-heap approach
        return -1;
    }
};

void runTest(int t, vector<int> nums, int k, int exp) {
    Solution sol;
    int res = sol.findKthLargest(nums, k);
    cout << "Test " << t << ": " << (res == exp ? "PASSED" : "FAILED")
         << " | Got: " << res << " Expected: " << exp << endl;
}

int main() {
    cout << "=== Kth Largest Element (LC #215) ===" << endl;
    runTest(1, {3,2,1,5,6,4}, 2, 5);
    runTest(2, {3,2,3,1,2,4,5,5,6}, 4, 4);
    runTest(3, {1}, 1, 1);
    runTest(4, {7,6,5,4,3,2,1}, 7, 1);
    runTest(5, {3,3,3,3,3}, 3, 3);
    runTest(6, {2,1}, 1, 2);
    return 0;
}
