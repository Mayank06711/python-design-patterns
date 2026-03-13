/*
 * Problem: Next Greater Element I (LeetCode #496) - Easy
 * Given nums1 (subset of nums2), find next greater element in nums2 for each.
 * Approach: Monotonic decreasing stack + hashmap on nums2
 * Time: O(n+m) | Space: O(n)
 * Example: nums1=[4,1,2] nums2=[1,3,4,2] -> [-1,3,-1]
 */
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
#include <cassert>
using namespace std;
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // TODO: Implement
        return {};
    }
};
int main() {
    Solution sol;
    {
        vector<int> n1={4,1,2}, n2={1,3,4,2}, exp={-1,3,-1};
        assert(sol.nextGreaterElement(n1,n2)==exp);
        cout << "Test 1 passed: [4,1,2],[1,3,4,2] -> [-1,3,-1]" << endl;
    }
    {
        vector<int> n1={2,4}, n2={1,2,3,4}, exp={3,-1};
        assert(sol.nextGreaterElement(n1,n2)==exp);
        cout << "Test 2 passed: [2,4],[1,2,3,4] -> [3,-1]" << endl;
    }
    {
        vector<int> n1={1}, n2={1}, exp={-1};
        assert(sol.nextGreaterElement(n1,n2)==exp);
        cout << "Test 3 passed: single element -> [-1]" << endl;
    }
    {
        vector<int> n1={4,3,2,1}, n2={4,3,2,1}, exp={-1,-1,-1,-1};
        assert(sol.nextGreaterElement(n1,n2)==exp);
        cout << "Test 4 passed: all decreasing -> [-1,-1,-1,-1]" << endl;
    }
    cout << "\nAll tests passed!" << endl;
    return 0;
}
