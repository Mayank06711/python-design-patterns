/*
 * Problem: Kth Largest Element in an Array (LC #215) - Medium
 *
 * Given an integer array nums and an integer k, return the kth
 * largest element in the array.
 * [3,2,1,5,6,4] k=2 -> 5
 *
 * Approach 1: Min-heap of size K.
 * Approach 2: Quickselect (avg O(N)).
 *
 * Time:  O(N log K) heap, O(N) avg quickselect
 * Space: O(K)
 */

#include <iostream>
#include <vector>
#include <queue>
#include <cassert>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // TODO: Min-heap approach or Quickselect
        return -1;
    }
};

int main() {
    cout << "=== Kth Largest Element in an Array (LC #215) ===" << endl;
    Solution sol;

    vector<int> nums1 = {3, 2, 1, 5, 6, 4};
    int r1 = sol.findKthLargest(nums1, 2);
    cout << "Test 1: [3,2,1,5,6,4] k=2 -> " << r1 << " (expected 5)" << endl;
    assert(r1 == 5);

    vector<int> nums2 = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    int r2 = sol.findKthLargest(nums2, 4);
    cout << "Test 2: [3,2,3,1,2,4,5,5,6] k=4 -> " << r2 << " (expected 4)" << endl;
    assert(r2 == 4);

    vector<int> nums3 = {1};
    int r3 = sol.findKthLargest(nums3, 1);
    cout << "Test 3: [1] k=1 -> " << r3 << " (expected 1)" << endl;
    assert(r3 == 1);

    cout << "\nAll tests passed!" << endl;
    return 0;
}
