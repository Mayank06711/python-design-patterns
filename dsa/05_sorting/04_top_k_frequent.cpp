/*
 * Problem: Top K Frequent Elements (LeetCode #347) - Medium
 *
 * Given an integer array nums and an integer k, return the k most frequent
 * elements. Answer may be returned in any order.
 *
 * Approach 1: Bucket Sort - O(n)
 *   - Count frequencies with a hash map.
 *   - Create buckets where index = frequency, bucket[i] = elements with freq i.
 *   - Iterate buckets from high to low, collect until we have k elements.
 *
 * Approach 2: Min-heap of size k keyed by frequency - O(n log k)
 *
 * Time:  O(n) bucket sort / O(n log k) heap
 * Space: O(n)
 *
 * Example: [1,1,1,2,2,3] k=2 -> [1,2]
 */

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // TODO: implement bucket sort or heap approach
        return {};
    }
};

string vecToString(vector<int> v) {
    sort(v.begin(), v.end());
    string s = "[";
    for (int i = 0; i < (int)v.size(); i++) {
        if (i > 0) s += ",";
        s += to_string(v[i]);
    }
    return s + "]";
}

void runTest(int t, vector<int> nums, int k, vector<int> exp) {
    Solution sol;
    vector<int> res = sol.topKFrequent(nums, k);
    sort(res.begin(), res.end());
    sort(exp.begin(), exp.end());
    cout << "Test " << t << ": " << (res == exp ? "PASSED" : "FAILED")
         << " | Got: " << vecToString(res) << " Expected: " << vecToString(exp) << endl;
}

int main() {
    cout << "=== Top K Frequent Elements (LC #347) ===" << endl;
    runTest(1, {1,1,1,2,2,3}, 2, {1,2});
    runTest(2, {1}, 1, {1});
    runTest(3, {1,2,3}, 3, {1,2,3});
    runTest(4, {-1,-1,2,2,2,3}, 1, {2});
    runTest(5, {4,4,4,4,1,1,1,2,2,3}, 2, {1,4});
    return 0;
}
