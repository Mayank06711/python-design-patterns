/*
 * Problem: Largest Rectangle in Histogram (LeetCode #84) - Hard
 *
 * Given an array of integers heights representing the histogram bar heights
 * where the width of each bar is 1, return the area of the largest rectangle
 * in the histogram.
 *
 * Approach: Use a monotonic increasing stack of indices. For each bar, pop
 *           all taller bars from the stack. When popping, calculate the area
 *           using the popped bar height and the width determined by the
 *           current index and the new stack top. After processing all bars,
 *           pop remaining bars using n as the right boundary.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 *
 * Example: [2,1,5,6,2,3] -> 10
 *          (The largest rectangle has area 10, spanning bars with heights 5 and 6)
 */

#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> st; // monotonic increasing stack of indices
        int maxArea = 0;

        for (int i = 0; i <= n; i++) {
            // Use height 0 as a sentinel to flush the stack at the end
            int currentHeight = (i == n) ? 0 : heights[i];

            while (!st.empty() && heights[st.top()] > currentHeight) {
                int height = heights[st.top()];
                st.pop();

                // Width: from (stack top + 1) to (i - 1)
                int width = st.empty() ? i : (i - st.top() - 1);
                maxArea = max(maxArea, height * width);
            }

            st.push(i);
        }

        return maxArea;
    }
};

int main() {
    Solution sol;

    // Test 1: LeetCode example 1
    {
        vector<int> heights = {2, 1, 5, 6, 2, 3};
        int result = sol.largestRectangleArea(heights);
        assert(result == 10);
        cout << "Test 1 passed: [2,1,5,6,2,3] -> " << result << endl;
    }

    // Test 2: LeetCode example 2
    {
        vector<int> heights = {2, 4};
        int result = sol.largestRectangleArea(heights);
        assert(result == 4);
        cout << "Test 2 passed: [2,4] -> " << result << endl;
    }

    // Test 3: Single bar
    {
        vector<int> heights = {5};
        int result = sol.largestRectangleArea(heights);
        assert(result == 5);
        cout << "Test 3 passed: [5] -> " << result << endl;
    }

    // Test 4: All same height
    {
        vector<int> heights = {3, 3, 3, 3};
        int result = sol.largestRectangleArea(heights);
        assert(result == 12);
        cout << "Test 4 passed: [3,3,3,3] -> " << result << endl;
    }

    // Test 5: Increasing heights
    {
        vector<int> heights = {1, 2, 3, 4, 5};
        int result = sol.largestRectangleArea(heights);
        assert(result == 9);
        cout << "Test 5 passed: [1,2,3,4,5] -> " << result << endl;
    }

    // Test 6: Decreasing heights
    {
        vector<int> heights = {5, 4, 3, 2, 1};
        int result = sol.largestRectangleArea(heights);
        assert(result == 9);
        cout << "Test 6 passed: [5,4,3,2,1] -> " << result << endl;
    }

    // Test 7: Valley shape
    {
        vector<int> heights = {6, 2, 5, 4, 5, 1, 6};
        int result = sol.largestRectangleArea(heights);
        assert(result == 12);
        cout << "Test 7 passed: [6,2,5,4,5,1,6] -> " << result << endl;
    }

    cout << "\nAll tests passed!" << endl;
    return 0;
}
