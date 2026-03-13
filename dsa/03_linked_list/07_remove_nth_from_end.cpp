/*
 * Problem: Remove Nth Node From End of List (LeetCode #19) - Medium
 *
 * Given the head of a linked list, remove the nth node from
 * the end of the list and return its head.
 *
 * Approach: Two pointers with N-gap.
 *   1. Advance the first pointer n steps ahead.
 *   2. Move both pointers together until first reaches the end.
 *   3. The second pointer is now just before the node to remove.
 *   4. Skip over the target node.
 *
 * Time Complexity:  O(n) - single pass
 * Space Complexity: O(1)
 *
 * Example: [1,2,3,4,5] n=2 -> [1,2,3,5]
 */

#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // TODO: Implement two pointers with N-gap
        return nullptr;
    }
};

ListNode* buildList(const vector<int>& vals) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int v : vals) {
        tail->next = new ListNode(v);
        tail = tail->next;
    }
    return dummy.next;
}

void printList(ListNode* head) {
    cout << "[";
    while (head) {
        cout << head->val;
        if (head->next) cout << ",";
        head = head->next;
    }
    cout << "]" << endl;
}

int main() {
    Solution sol;

    ListNode* l1 = buildList({1, 2, 3, 4, 5});
    cout << "Original: ";
    printList(l1);
    ListNode* r1 = sol.removeNthFromEnd(l1, 2);
    cout << "Remove 2nd from end: ";
    printList(r1);
    // Expected: [1,2,3,5]

    ListNode* l2 = buildList({1});
    ListNode* r2 = sol.removeNthFromEnd(l2, 1);
    cout << "\nRemove only node: ";
    printList(r2);
    // Expected: []

    ListNode* l3 = buildList({1, 2});
    ListNode* r3 = sol.removeNthFromEnd(l3, 1);
    cout << "\nRemove 1st from end of [1,2]: ";
    printList(r3);
    // Expected: [1]

    return 0;
}
