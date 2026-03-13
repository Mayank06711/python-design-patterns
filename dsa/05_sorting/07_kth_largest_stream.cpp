/*
 * Kth Largest Element in a Stream
 * LeetCode: #703 | Difficulty: Easy
 * Min-heap of size k for streaming kth largest
 * Pattern: Min-heap of size K (online)
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) { /* TODO */ }
    int add(int val) { return 0; }
};

int main() {
    vector<int> nums = {4, 5, 8, 2};
    KthLargest kl(3, nums);
    cout << "add(3): " << kl.add(3) << " (expected 4)" << endl;
    cout << "add(5): " << kl.add(5) << " (expected 5)" << endl;
    cout << "add(10): " << kl.add(10) << " (expected 5)" << endl;
    cout << "add(9): " << kl.add(9) << " (expected 8)" << endl;
    return 0;
}
