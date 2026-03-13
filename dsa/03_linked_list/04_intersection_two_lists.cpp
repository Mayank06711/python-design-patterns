/*
 * Problem: Intersection of Two Linked Lists (LeetCode #160) - Easy
 *
 * Given the heads of two singly linked lists, return the node
 * at which the two lists intersect. If they do not intersect,
 * return nullptr.
 *
 * Approach: Two-pointer technique. When a pointer reaches the end
 * of its list, redirect it to the head of the other list. Both
 * pointers will meet at the intersection node (or both become
 * nullptr if no intersection) after at most 2 passes.
 *
 * Why it works: Both pointers travel the same total distance
 * (lenA + lenB), so they align at the intersection point.
 *
 * Time Complexity:  O(n + m)
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
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        // TODO: Implement switch-to-other-head at null trick
        return nullptr;
    }
};

int main() {
    Solution sol;

    // Build intersecting lists:
    //   A: 4 -> 1 --\
    //                 8 -> 4 -> 5
    //   B: 5 -> 6 -> 1 --/
    ListNode* common = new ListNode(8);
    common->next = new ListNode(4);
    common->next->next = new ListNode(5);

    ListNode* headA = new ListNode(4);
    headA->next = new ListNode(1);
    headA->next->next = common;

    ListNode* headB = new ListNode(5);
    headB->next = new ListNode(6);
    headB->next->next = new ListNode(1);
    headB->next->next->next = common;

    ListNode* result = sol.getIntersectionNode(headA, headB);
    if (result) {
        cout << "Test 1 - Intersection at node with val: " << result->val << endl;
    } else {
        cout << "Test 1 - No intersection" << endl;
    }
    // Expected: Intersection at node with val: 8

    // Test 2: No intersection
    ListNode* h1 = new ListNode(1);
    h1->next = new ListNode(2);
    ListNode* h2 = new ListNode(3);
    h2->next = new ListNode(4);

    ListNode* result2 = sol.getIntersectionNode(h1, h2);
    cout << "Test 2 - " << (result2 ? "Has intersection" : "No intersection") << endl;
    // Expected: No intersection

    return 0;
}
