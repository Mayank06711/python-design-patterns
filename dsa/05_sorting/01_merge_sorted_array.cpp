/*
 * Problem: Merge Sorted Array (LeetCode #88) - Easy
 *
 * Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
 * and two integers m and n representing the number of elements in nums1 and
 * nums2 respectively. Merge nums2 into nums1 as one sorted array.
 *
 * nums1 has length m + n where the last n elements are 0 and should be ignored.
 *
 * Approach: Three-pointer merge from end.
 *   - Pointer i at m-1 (end of valid nums1), j at n-1 (end of nums2),
 *     k at m+n-1 (end of nums1 total).
 *   - Compare from back, place larger element at k, decrement accordingly.
 *   - Copy remaining nums2 elements if j >= 0 after loop.
 *
 * Time:  O(m + n)
 * Space: O(1)
 *
 * Example: nums1=[1,2,3,0,0,0] m=3, nums2=[2,5,6] n=3 -> [1,2,2,3,5,6]
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // TODO: implement three-pointer merge from end
    }
};

string vecToString(const vector<int>& v) {
    string s = "[";
    for (int i = 0; i < (int)v.size(); i++) {
        if (i > 0) s += ",";
        s += to_string(v[i]);
    }
    return s + "]";
}

void runTest(int t, vector<int> n1, int m, vector<int> n2, int n, const vector<int>& exp) {
    Solution sol;
    sol.merge(n1, m, n2, n);
    cout << "Test " << t << ": " << (n1 == exp ? "PASSED" : "FAILED")
         << " | Got: " << vecToString(n1) << " Expected: " << vecToString(exp) << endl;
}

int main() {
    cout << "=== Merge Sorted Array (LC #88) ===" << endl;
    runTest(1, {1,2,3,0,0,0}, 3, {2,5,6}, 3, {1,2,2,3,5,6});
    runTest(2, {1}, 1, {}, 0, {1});
    runTest(3, {0}, 0, {1}, 1, {1});
    runTest(4, {4,5,6,0,0,0}, 3, {1,2,3}, 3, {1,2,3,4,5,6});
    runTest(5, {2,0}, 1, {1}, 1, {1,2});
    return 0;
}
