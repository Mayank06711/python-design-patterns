/*
 * Problem: Merge Two Sorted Lists (LeetCode #21) - Easy
 *
 * Merge two sorted linked lists and return it as a sorted list.
 * The list should be made by splicing together the nodes of
 * the first two lists.
 *
 * Approach: Use a dummy head node. Compare nodes from both lists,
 * attach the smaller one to the merged list, and advance that pointer.
 *
 * Time Complexity:  O(n + m)
 * Space Complexity: O(1)
 *
 * Example: [1,2,4] + [1,3,4] -> [1,1,2,3,4,4]
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // TODO: Implement dummy head + compare approach
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

    ListNode* l1 = buildList({1, 2, 4});
    ListNode* l2 = buildList({1, 3, 4});

    cout << "List 1: ";
    printList(l1);
    cout << "List 2: ";
    printList(l2);

    ListNode* merged = sol.mergeTwoLists(l1, l2);
    cout << "Merged: ";
    printList(merged);
    // Expected: [1,1,2,3,4,4]

    return 0;
}
