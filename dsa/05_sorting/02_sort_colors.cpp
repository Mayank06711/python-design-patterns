/*
 * Problem: Sort Colors (LeetCode #75) - Medium
 *
 * Given an array nums with n objects colored red (0), white (1), or blue (2),
 * sort them in-place so objects of the same color are adjacent: 0s, 1s, 2s.
 *
 * Approach: Dutch National Flag 3-way partition.
 *   - Three pointers: low (boundary for 0s), mid (current), high (boundary for 2s).
 *   - nums[mid]==0: swap(nums[low], nums[mid]), low++, mid++
 *   - nums[mid]==1: mid++
 *   - nums[mid]==2: swap(nums[mid], nums[high]), high-- (do NOT advance mid)
 *
 * Time:  O(n) single pass
 * Space: O(1)
 *
 * Example: [2,0,2,1,1,0] -> [0,0,1,1,2,2]
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        // TODO: implement Dutch National Flag 3-way partition
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

void runTest(int t, vector<int> nums, const vector<int>& exp) {
    Solution sol;
    sol.sortColors(nums);
    cout << "Test " << t << ": " << (nums == exp ? "PASSED" : "FAILED")
         << " | Got: " << vecToString(nums) << " Expected: " << vecToString(exp) << endl;
}

int main() {
    cout << "=== Sort Colors (LC #75) ===" << endl;
    runTest(1, {2,0,2,1,1,0}, {0,0,1,1,2,2});
    runTest(2, {0,0,1,1,2,2}, {0,0,1,1,2,2});
    runTest(3, {2,2,1,1,0,0}, {0,0,1,1,2,2});
    runTest(4, {1}, {1});
    runTest(5, {2,0}, {0,2});
    runTest(6, {2,0,2,0,2,0}, {0,0,0,2,2,2});
    return 0;
}
