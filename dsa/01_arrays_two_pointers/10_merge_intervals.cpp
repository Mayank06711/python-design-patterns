/*
 * Problem: Merge Intervals
 * LeetCode: #56 | Difficulty: Medium
 * Given an array of intervals where intervals[i] = [start_i, end_i],
 * merge all overlapping intervals and return an array of the non-overlapping
 * intervals that cover all the intervals in the input.
 * Example: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
 * Pattern: Sort intervals by start time, then do a single linear pass.
 *          For each interval, either merge it with the last result interval
 *          (if overlapping) or push it as a new interval.
 * Company: Google, Facebook, Amazon, Microsoft, Bloomberg, Uber
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Your solution here
    }
};

void printIntervals(const vector<vector<int>>& intervals) {
    cout << "[";
    for (int i = 0; i < (int)intervals.size(); i++) {
        cout << "[" << intervals[i][0] << "," << intervals[i][1] << "]";
        if (i < (int)intervals.size() - 1) cout << ",";
    }
    cout << "]";
}

int main() {
    Solution sol;

    // Test 1: Standard overlapping intervals
    vector<vector<int>> intervals1 = {{1,3},{2,6},{8,10},{15,18}};
    auto res1 = sol.merge(intervals1);
    cout << "Test 1: ";
    printIntervals(res1);
    cout << " (expected [[1,6],[8,10],[15,18]])" << endl;

    // Test 2: All intervals merge into one
    vector<vector<int>> intervals2 = {{1,4},{4,5}};
    auto res2 = sol.merge(intervals2);
    cout << "Test 2: ";
    printIntervals(res2);
    cout << " (expected [[1,5]])" << endl;

    // Test 3: No overlapping intervals
    vector<vector<int>> intervals3 = {{1,2},{3,4},{5,6}};
    auto res3 = sol.merge(intervals3);
    cout << "Test 3: ";
    printIntervals(res3);
    cout << " (expected [[1,2],[3,4],[5,6]])" << endl;

    // Test 4: Single interval
    vector<vector<int>> intervals4 = {{1,10}};
    auto res4 = sol.merge(intervals4);
    cout << "Test 4: ";
    printIntervals(res4);
    cout << " (expected [[1,10]])" << endl;

    // Test 5: Unsorted input with full overlap
    vector<vector<int>> intervals5 = {{1,4},{0,4}};
    auto res5 = sol.merge(intervals5);
    cout << "Test 5: ";
    printIntervals(res5);
    cout << " (expected [[0,4]])" << endl;

    return 0;
}
