/*
 * Problem: Linked List Cycle (LeetCode #141) - Easy
 *
 * Given head, determine if the linked list has a cycle in it.
 * A cycle exists if some node can be reached again by continuously
 * following the next pointer.
 *
 * Approach: Floyd cycle detection (tortoise and hare).
 * Use slow pointer (1 step) and fast pointer (2 steps).
 * If they meet, a cycle exists. If fast reaches null, no cycle.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 *
 * Example: Return true if cycle exists, false otherwise.
 */

#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode* head) {
        // TODO: Implement Floyd slow/fast pointer detection
        return false;
    }
};

int main() {
    Solution sol;

    // Test 1: List with cycle [3,2,0,-4] -> cycle at index 1
    ListNode* n1 = new ListNode(3);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(0);
    ListNode* n4 = new ListNode(-4);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n2; // cycle back to node with val=2

    cout << "Test 1 (has cycle): " << (sol.hasCycle(n1) ? "true" : "false") << endl;
    // Expected: true

    // Test 2: List without cycle [1,2,3]
    ListNode* m1 = new ListNode(1);
    ListNode* m2 = new ListNode(2);
    ListNode* m3 = new ListNode(3);
    m1->next = m2;
    m2->next = m3;

    cout << "Test 2 (no cycle):  " << (sol.hasCycle(m1) ? "true" : "false") << endl;
    // Expected: false

    // Test 3: Single node, no cycle
    ListNode* s1 = new ListNode(1);
    cout << "Test 3 (single):    " << (sol.hasCycle(s1) ? "true" : "false") << endl;
    // Expected: false

    return 0;
}
