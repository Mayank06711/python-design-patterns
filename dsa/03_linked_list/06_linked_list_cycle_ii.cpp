/*
 * Problem: Linked List Cycle II (LeetCode #142) - Medium
 *
 * Given the head of a linked list, return the node where the
 * cycle begins. If there is no cycle, return nullptr.
 *
 * Approach: Floyd cycle detection extended.
 *   1. Use slow (1 step) and fast (2 steps) to detect cycle.
 *   2. Once they meet, reset one pointer to head.
 *   3. Move both pointers 1 step at a time - they meet at cycle start.
 *
 * Mathematical proof: If distance from head to cycle start is "a",
 * and distance from cycle start to meeting point is "b", then
 * slow traveled a+b, fast traveled a+b+c+b (one full cycle extra).
 * Since fast = 2*slow => a+b+c+b = 2(a+b) => c = a.
 * So moving from head and meeting point at same speed meets at start.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
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
    ListNode* detectCycle(ListNode* head) {
        // TODO: Implement Floyd extended - find cycle start node
        return nullptr;
    }
};

int main() {
    Solution sol;

    // Test 1: [3,2,0,-4] with cycle at index 1 (node val=2)
    ListNode* n1 = new ListNode(3);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(0);
    ListNode* n4 = new ListNode(-4);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n2; // cycle to node val=2

    ListNode* result1 = sol.detectCycle(n1);
    if (result1) {
        cout << "Test 1 - Cycle starts at node with val: " << result1->val << endl;
    } else {
        cout << "Test 1 - No cycle" << endl;
    }
    // Expected: Cycle starts at node with val: 2

    // Test 2: [1,2] with cycle at index 0 (node val=1)
    ListNode* m1 = new ListNode(1);
    ListNode* m2 = new ListNode(2);
    m1->next = m2;
    m2->next = m1; // cycle to head

    ListNode* result2 = sol.detectCycle(m1);
    if (result2) {
        cout << "Test 2 - Cycle starts at node with val: " << result2->val << endl;
    } else {
        cout << "Test 2 - No cycle" << endl;
    }
    // Expected: Cycle starts at node with val: 1

    // Test 3: [1] no cycle
    ListNode* s1 = new ListNode(1);
    ListNode* result3 = sol.detectCycle(s1);
    cout << "Test 3 - " << (result3 ? "Has cycle" : "No cycle") << endl;
    // Expected: No cycle

    return 0;
}
