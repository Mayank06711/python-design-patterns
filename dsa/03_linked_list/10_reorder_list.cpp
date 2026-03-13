/*
 * Problem: Reorder List (LeetCode #143) - Medium
 *
 * Given a singly linked list:
 *   L0 -> L1 -> ... -> Ln-1 -> Ln
 * Reorder it to:
 *   L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
 *
 * Approach:
 *   1. Find the middle of the list (slow/fast pointers).
 *   2. Reverse the second half.
 *   3. Interleave (merge) the two halves together.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 *
 * Example: [1,2,3,4] -> [1,4,2,3]
 *          [1,2,3,4,5] -> [1,5,2,4,3]
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
    void reorderList(ListNode* head) {
        // TODO: Implement find mid + reverse + interleave
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

    ListNode* l1 = buildList({1, 2, 3, 4});
    cout << "Original: ";
    printList(l1);
    sol.reorderList(l1);
    cout << "Reordered: ";
    printList(l1);
    // Expected: [1,4,2,3]

    cout << endl;
    ListNode* l2 = buildList({1, 2, 3, 4, 5});
    cout << "Original: ";
    printList(l2);
    sol.reorderList(l2);
    cout << "Reordered: ";
    printList(l2);
    // Expected: [1,5,2,4,3]

    return 0;
}
