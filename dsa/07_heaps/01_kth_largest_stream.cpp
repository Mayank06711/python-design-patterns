/*
 * Problem: Kth Largest Element in a Stream (LC #703) - Easy
 *
 * Design a class to find the kth largest element in a stream.
 * KthLargest(3, [4,5,8,2])
 * add(3) -> 4, add(5) -> 5, add(10) -> 5
 *
 * Approach: Maintain a min-heap of size K. The top of the heap
 * is always the Kth largest element.
 *
 * Time:  O(N log K) constructor, O(log K) per add
 * Space: O(K)
 */

#include <iostream>
#include <vector>
#include <queue>
#include <cassert>

using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    KthLargest(int k, vector<int>& nums) : k(k) {
        // TODO: Push nums into minHeap, keep size <= k
    }

    int add(int val) {
        // TODO: Push val, pop if size > k, return top
        return -1;
    }
};

int main() {
    cout << "=== Kth Largest Element in a Stream (LC #703) ===" << endl;

    vector<int> nums = {4, 5, 8, 2};
    KthLargest kthLargest(3, nums);

    int r1 = kthLargest.add(3);
    cout << "add(3) -> " << r1 << " (expected 4)" << endl;
    assert(r1 == 4);

    int r2 = kthLargest.add(5);
    cout << "add(5) -> " << r2 << " (expected 5)" << endl;
    assert(r2 == 5);

    int r3 = kthLargest.add(10);
    cout << "add(10) -> " << r3 << " (expected 5)" << endl;
    assert(r3 == 5);

    cout << "\nAll tests passed!" << endl;
    return 0;
}
