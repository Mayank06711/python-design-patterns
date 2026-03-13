/*
 * Problem: Valid Parentheses (LeetCode #20) - Easy
 * Given a string s containing just '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 * Approach: Stack matching pairs
 * Time: O(n) | Space: O(n)
 * Example: s = "()[]{}" -> true, s = "(]" -> false
 */
#include <iostream>
#include <string>
#include <stack>
#include <cassert>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        // TODO: Implement
    }
};
int main() {
    Solution sol;
    assert(sol.isValid("()[]{}") == true);
    cout << "Test 1 passed: ()[] {} -> true" << endl;
    assert(sol.isValid("()") == true);
    cout << "Test 2 passed: () -> true" << endl;
    assert(sol.isValid("(]") == false);
    cout << "Test 3 passed: (] -> false" << endl;
    assert(sol.isValid("([{}])") == true);
    cout << "Test 4 passed: ([{}]) -> true" << endl;
    assert(sol.isValid("((") == false);
    cout << "Test 5 passed: (( -> false" << endl;
    assert(sol.isValid("") == true);
    cout << "Test 6 passed: empty -> true" << endl;
    assert(sol.isValid(")") == false);
    cout << "Test 7 passed: ) -> false" << endl;
    cout << "\nAll tests passed!" << endl;
    return 0;
}
