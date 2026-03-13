/*
 * Problem: Top K Frequent Elements (LC #347) - Medium
 *
 * Given an integer array nums and an integer k, return the k
 * most frequent elements in any order.
 * [1,1,1,2,2,3] k=2 -> [1,2]
 *
 * Approach: Count frequencies with hash map, then use a min-heap
 * of size K storing (frequency, element) pairs.
 *
 * Time:  O(N log K)
 * Space: O(N)
 */

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // TODO: Frequency map + min-heap of size K
        return {};
    }
};

void printVector(const vector<int>& v) {
    cout << "[";
    for (int i = 0; i < (int)v.size(); i++) {
        cout << v[i];
        if (i < (int)v.size() - 1) cout << ",";
    }
    cout << "]";
}

bool sameElements(vector<int> a, vector<int> b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    return a == b;
}

int main() {
    cout << "=== Top K Frequent Elements (LC #347) ===" << endl;
    Solution sol;

    vector<int> nums1 = {1, 1, 1, 2, 2, 3};
    vector<int> r1 = sol.topKFrequent(nums1, 2);
    cout << "Test 1: [1,1,1,2,2,3] k=2 -> ";
    printVector(r1);
    cout << " (expected [1,2])" << endl;
    assert(sameElements(r1, {1, 2}));

    vector<int> nums2 = {1};
    vector<int> r2 = sol.topKFrequent(nums2, 1);
    cout << "Test 2: [1] k=1 -> ";
    printVector(r2);
    cout << " (expected [1])" << endl;
    assert(sameElements(r2, {1}));

    vector<int> nums3 = {-1, -1, 2, 2, 2, 3};
    vector<int> r3 = sol.topKFrequent(nums3, 1);
    cout << "Test 3: [-1,-1,2,2,2,3] k=1 -> ";
    printVector(r3);
    cout << " (expected [2])" << endl;
    assert(sameElements(r3, {2}));

    cout << "\nAll tests passed!" << endl;
    return 0;
}
