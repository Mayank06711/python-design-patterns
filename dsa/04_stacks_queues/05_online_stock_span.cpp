/*
 * Problem: Online Stock Span (LeetCode #901) - Medium
 *
 * Design an algorithm that collects daily price quotes for some stock and
 * returns the span of that stock price for the current day.
 *
 * The span of the stock price today is the maximum number of consecutive
 * days (starting from today going backward) for which the stock price was
 * less than or equal to today price.
 *
 * Approach: Use a monotonic decreasing stack that stores pairs of (price, span).
 *           When a new price comes in, pop all entries with price <= current price
 *           and accumulate their spans into the current span. Push the new entry.
 *
 * Time Complexity:  O(1) amortized per call to next()
 * Space Complexity: O(n) total
 *
 * Example: Prices [100, 80, 60, 70, 60, 75, 85]
 *          Spans  [1,   1,  1,  2,  1,  4,  6]
 */

#include <iostream>
#include <stack>
#include <vector>
#include <cassert>
#include <utility>

using namespace std;

class StockSpanner {
private:
    stack<pair<int, int>> st; // (price, cumulative span)

public:
    StockSpanner() {}

    int next(int price) {
        int span = 1;

        while (!st.empty() && st.top().first <= price) {
            span += st.top().second;
            st.pop();
        }

        st.push({price, span});
        return span;
    }
};

int main() {
    // Test 1: LeetCode example
    {
        StockSpanner spanner;
        assert(spanner.next(100) == 1);
        cout << "Test 1a passed: next(100) -> 1" << endl;

        assert(spanner.next(80) == 1);
        cout << "Test 1b passed: next(80) -> 1" << endl;

        assert(spanner.next(60) == 1);
        cout << "Test 1c passed: next(60) -> 1" << endl;

        assert(spanner.next(70) == 2);
        cout << "Test 1d passed: next(70) -> 2" << endl;

        assert(spanner.next(60) == 1);
        cout << "Test 1e passed: next(60) -> 1" << endl;

        assert(spanner.next(75) == 4);
        cout << "Test 1f passed: next(75) -> 4" << endl;

        assert(spanner.next(85) == 6);
        cout << "Test 1g passed: next(85) -> 6" << endl;
    }

    // Test 2: All increasing prices
    {
        StockSpanner spanner;
        assert(spanner.next(10) == 1);
        assert(spanner.next(20) == 2);
        assert(spanner.next(30) == 3);
        assert(spanner.next(40) == 4);
        cout << "Test 2 passed: increasing prices -> spans [1,2,3,4]" << endl;
    }

    // Test 3: All decreasing prices
    {
        StockSpanner spanner;
        assert(spanner.next(40) == 1);
        assert(spanner.next(30) == 1);
        assert(spanner.next(20) == 1);
        assert(spanner.next(10) == 1);
        cout << "Test 3 passed: decreasing prices -> spans [1,1,1,1]" << endl;
    }

    // Test 4: All same prices
    {
        StockSpanner spanner;
        assert(spanner.next(50) == 1);
        assert(spanner.next(50) == 2);
        assert(spanner.next(50) == 3);
        cout << "Test 4 passed: same prices -> spans [1,2,3]" << endl;
    }

    // Test 5: Single price
    {
        StockSpanner spanner;
        assert(spanner.next(99) == 1);
        cout << "Test 5 passed: single price -> span 1" << endl;
    }

    cout << "\nAll tests passed!" << endl;
    return 0;
}
