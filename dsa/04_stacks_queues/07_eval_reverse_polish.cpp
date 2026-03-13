/*
 * Problem: Evaluate Reverse Polish Notation (LeetCode #150) - Medium
 *
 * You are given an array of strings tokens that represents an arithmetic
 * expression in Reverse Polish Notation (postfix notation).
 *
 * Evaluate the expression and return an integer representing the value.
 *
 * Valid operators are +, -, *, and /. Each operand may be an integer
 * or another expression. Division between two integers truncates toward zero.
 *
 * Approach: Use a stack. Push operands onto the stack. When an operator is
 *           encountered, pop two operands, apply the operator, and push
 *           the result back onto the stack. The final result is the last
 *           element on the stack.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 *
 * Example: ["2","1","+","3","*"] -> 9
 *          Explanation: ((2 + 1) * 3) = 9
 */

#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <cassert>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long long> st;

        for (const string& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                long long b = st.top(); st.pop();
                long long a = st.top(); st.pop();

                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else if (token == "/") st.push(a / b); // truncates toward zero
            } else {
                st.push(stoll(token));
            }
        }

        return (int)st.top();
    }
};

int main() {
    Solution sol;

    // Test 1: LeetCode example 1
    {
        vector<string> tokens = {"2", "1", "+", "3", "*"};
        int result = sol.evalRPN(tokens);
        assert(result == 9);
        cout << "Test 1 passed: [\"2\",\"1\",\"+\",\"3\",\"*\"] -> " << result << endl;
    }

    // Test 2: LeetCode example 2
    {
        vector<string> tokens = {"4", "13", "5", "/", "+"};
        int result = sol.evalRPN(tokens);
        assert(result == 6);
        cout << "Test 2 passed: [\"4\",\"13\",\"5\",\"/\",\"+\"] -> " << result << endl;
    }

    // Test 3: LeetCode example 3
    {
        vector<string> tokens = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
        int result = sol.evalRPN(tokens);
        assert(result == 22);
        cout << "Test 3 passed: complex expression -> " << result << endl;
    }

    // Test 4: Single number
    {
        vector<string> tokens = {"42"};
        int result = sol.evalRPN(tokens);
        assert(result == 42);
        cout << "Test 4 passed: single number -> " << result << endl;
    }

    // Test 5: Negative result
    {
        vector<string> tokens = {"3", "5", "-"};
        int result = sol.evalRPN(tokens);
        assert(result == -2);
        cout << "Test 5 passed: 3 - 5 -> " << result << endl;
    }

    // Test 6: Division truncates toward zero
    {
        vector<string> tokens = {"7", "2", "/"};
        int result = sol.evalRPN(tokens);
        assert(result == 3);
        cout << "Test 6 passed: 7 / 2 -> " << result << " (truncated)" << endl;
    }

    cout << "\nAll tests passed!" << endl;
    return 0;
}
