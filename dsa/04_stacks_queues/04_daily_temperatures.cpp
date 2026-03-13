/*
 * Problem: Daily Temperatures (LeetCode #739) - Medium
 * Return how many days until a warmer temperature for each day.
 * Approach: Monotonic stack storing indices
 * Time: O(n) | Space: O(n)
 * Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
 */
#include <iostream>
#include <vector>
#include <stack>
#include <cassert>
using namespace std;
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // TODO: Implement
        return {};
    }
};
int main() {
    Solution sol;
    {
        vector<int> t={73,74,75,71,69,72,76,73}, exp={1,1,4,2,1,1,0,0};
        assert(sol.dailyTemperatures(t)==exp);
        cout << "Test 1 passed: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]" << endl;
    }
    {
        vector<int> t={30,40,50,60}, exp={1,1,1,0};
        assert(sol.dailyTemperatures(t)==exp);
        cout << "Test 2 passed: increasing -> [1,1,1,0]" << endl;
    }
    {
        vector<int> t={30,60,90}, exp={1,1,0};
        assert(sol.dailyTemperatures(t)==exp);
        cout << "Test 3 passed: [30,60,90] -> [1,1,0]" << endl;
    }
    {
        vector<int> t={50,50,50,50}, exp={0,0,0,0};
        assert(sol.dailyTemperatures(t)==exp);
        cout << "Test 4 passed: all same -> [0,0,0,0]" << endl;
    }
    {
        vector<int> t={90,80,70,60}, exp={0,0,0,0};
        assert(sol.dailyTemperatures(t)==exp);
        cout << "Test 5 passed: decreasing -> [0,0,0,0]" << endl;
    }
    cout << "\nAll tests passed!" << endl;
    return 0;
}
