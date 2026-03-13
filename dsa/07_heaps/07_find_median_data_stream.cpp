/*
 * Problem: Find Median from Data Stream (LC #295) - Hard
 *
 * Implement MedianFinder class:
 * - addNum(int num): adds integer to data structure
 * - findMedian(): returns the median of all elements so far
 *
 * Approach: Two heaps:
 * - maxHeap (left half): stores smaller half, largest on top
 * - minHeap (right half): stores larger half, smallest on top
 * Balance so maxHeap.size() >= minHeap.size(), differ by at most 1.
 *
 * Time:  O(log N) per addNum, O(1) per findMedian
 * Space: O(N)
 */

#include <iostream>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

class MedianFinder {
private:
    priority_queue<int> maxHeap;                             // left half
    priority_queue<int, vector<int>, greater<int>> minHeap;  // right half

public:
    MedianFinder() {}

    void addNum(int num) {
        // TODO: Add to appropriate heap, rebalance
    }

    double findMedian() {
        // TODO: Return top of maxHeap if odd, avg of tops if even
        return 0.0;
    }
};

int main() {
    cout << "=== Find Median from Data Stream (LC #295) ===" << endl;

    MedianFinder mf;

    mf.addNum(1);
    double m1 = mf.findMedian();
    cout << "After add(1): median = " << m1 << " (expected 1.0)" << endl;
    assert(fabs(m1 - 1.0) < 1e-5);

    mf.addNum(2);
    double m2 = mf.findMedian();
    cout << "After add(2): median = " << m2 << " (expected 1.5)" << endl;
    assert(fabs(m2 - 1.5) < 1e-5);

    mf.addNum(3);
    double m3 = mf.findMedian();
    cout << "After add(3): median = " << m3 << " (expected 2.0)" << endl;
    assert(fabs(m3 - 2.0) < 1e-5);

    // Test even count
    MedianFinder mf2;
    mf2.addNum(1);
    mf2.addNum(2);
    mf2.addNum(3);
    mf2.addNum(4);
    double m4 = mf2.findMedian();
    cout << "After [1,2,3,4]: median = " << m4 << " (expected 2.5)" << endl;
    assert(fabs(m4 - 2.5) < 1e-5);

    // Test negative numbers
    MedianFinder mf3;
    mf3.addNum(-1);
    mf3.addNum(-2);
    mf3.addNum(-3);
    double m5 = mf3.findMedian();
    cout << "After [-1,-2,-3]: median = " << m5 << " (expected -2.0)" << endl;
    assert(fabs(m5 - (-2.0)) < 1e-5);

    cout << "\nAll tests passed!" << endl;
    return 0;
}
