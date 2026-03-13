/*
 * Problem: Next Greater Element II (LeetCode #503) - Medium
 *
 * Given a circular integer array nums, return the next greater number
 * for every element in nums. The next greater number of a number x is
 * the first greater number traversing circularly to the right. If it
 * does not exist, return -1.
 *
 * Approach: Use a monotonic decreasing stack of indices. Iterate through
 *           the array twice (2*n) using modulo to simulate the circular
 *           behavior. On the second pass, we only pop from the stack
 *           (we do not push, since those indices are already handled).
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 *
 * Example: [1,2,1] -> [2,-1,2]
 */

#include <iostream>
#include <vector>
#include <stack>
#include <cassert>

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, -1);
        stack<int> st; // stores indices

        // Iterate twice to handle circular nature
        for (int i = 0; i < 2 * n; i++) {
            int idx = i % n;

            while (!st.empty() && nums[st.top()] < nums[idx]) {
                result[st.top()] = nums[idx];
                st.pop();
            }

            // Only push indices during the first pass
            if (i < n) {
                st.push(idx);
            }
        }

        return result;
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

int main() {
    Solution sol;

    // Test 1: LeetCode example 1
    {
        vector<int> nums = {1, 2, 1};
        vector<int> expected = {2, -1, 2};
        vector<int> result = sol.nextGreaterElements(nums);
        assert(result == expected);
        cout << "Test 1 passed: [1,2,1] -> ";
        printVector(result);
        cout << endl;
    }

    // Test 2: LeetCode example 2
    {
        vector<int> nums = {1, 2, 3, 4, 3};
        vector<int> expected = {2, 3, 4, -1, 4};
        vector<int> result = sol.nextGreaterElements(nums);
        assert(result == expected);
        cout << "Test 2 passed: [1,2,3,4,3] -> ";
        printVector(result);
        cout << endl;
    }

    // Test 3: All same elements
    {
        vector<int> nums = {5, 5, 5, 5};
        vector<int> expected = {-1, -1, -1, -1};
        vector<int> result = sol.nextGreaterElements(nums);
        assert(result == expected);
        cout << "Test 3 passed: all same -> [-1,-1,-1,-1]" << endl;
    }

    // Test 4: Single element
    {
        vector<int> nums = {1};
        vector<int> expected = {-1};
        vector<int> result = sol.nextGreaterElements(nums);
        assert(result == expected);
        cout << "Test 4 passed: single element -> [-1]" << endl;
    }

    // Test 5: Two elements
    {
        vector<int> nums = {1, 2};
        vector<int> expected = {2, -1};
        vector<int> result = sol.nextGreaterElements(nums);
        assert(result == expected);
        cout << "Test 5 passed: [1,2] -> [2,-1]" << endl;
    }

    // Test 6: Circular wrap-around needed
    {
        vector<int> nums = {3, 1, 2};
        vector<int> expected = {-1, 2, 3};
        vector<int> result = sol.nextGreaterElements(nums);
        assert(result == expected);
        cout << "Test 6 passed: [3,1,2] -> [-1,2,3]" << endl;
    }

    cout << "\nAll tests passed!" << endl;
    return 0;
}
