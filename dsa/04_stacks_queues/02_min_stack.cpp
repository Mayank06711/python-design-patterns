/*
 * Problem: Min Stack (LeetCode #155) - Medium
 * Design a stack with push, pop, top, and O(1) getMin.
 * Approach: Auxiliary stack tracking current minimum
 * Time: O(1) all ops | Space: O(n)
 */
#include <iostream>
#include <stack>
#include <cassert>
#include <algorithm>
using namespace std;
class MinStack {
private:
    // TODO: Declare main stack and min stack
public:
    MinStack() {}
    void push(int val) {
        // TODO
    }
    void pop() {
        // TODO
    }
    int top() {
        // TODO
        return 0;
    }
    int getMin() {
        // TODO
        return 0;
    }
};
int main() {
    {
        MinStack ms;
        ms.push(-2); ms.push(0); ms.push(-3);
        assert(ms.getMin() == -3);
        cout << "Test 1a passed: getMin() -> -3" << endl;
        ms.pop();
        assert(ms.top() == 0);
        cout << "Test 1b passed: top() -> 0" << endl;
        assert(ms.getMin() == -2);
        cout << "Test 1c passed: getMin() -> -2" << endl;
    }
    {
        MinStack ms;
        ms.push(5); ms.push(5); ms.push(5);
        assert(ms.getMin() == 5);
        ms.pop();
        assert(ms.getMin() == 5);
        cout << "Test 2 passed: all same, getMin() -> 5" << endl;
    }
    {
        MinStack ms;
        ms.push(3); ms.push(2); ms.push(1);
        assert(ms.getMin() == 1);
        ms.pop(); assert(ms.getMin() == 2);
        ms.pop(); assert(ms.getMin() == 3);
        cout << "Test 3 passed: decreasing, min updates on pop" << endl;
    }
    cout << "\nAll tests passed!" << endl;
    return 0;
}
