/*
 * Problem: Reverse Linked List (LeetCode #206) - Easy
 *
 * Given the head of a singly linked list, reverse the list
 * and return the reversed list.
 *
 * Approach: 3-pointer swap using prev, curr, and next.
 * At each step, reverse the current node pointer to point
 * to prev, then advance all three pointers forward.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 *
 * Example: [1,2,3,4,5] -> [5,4,3,2,1]
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
    ListNode* reverseList(ListNode* head) {
        // TODO: Implement 3-pointer swap (prev/curr/next)
        return nullptr;
    }
};

// Helper: build list from vector
ListNode* buildList(const vector<int>& vals) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int v : vals) {
        tail->next = new ListNode(v);
        tail = tail->next;
    }
    return dummy.next;
}

// Helper: print list
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

    ListNode* list1 = buildList({1, 2, 3, 4, 5});
    cout << "Original: ";
    printList(list1);

    ListNode* reversed = sol.reverseList(list1);
    cout << "Reversed: ";
    printList(reversed);
    // Expected: [5,4,3,2,1]

    ListNode* list2 = buildList({1, 2});
    cout << "\nOriginal: ";
    printList(list2);

    ListNode* reversed2 = sol.reverseList(list2);
    cout << "Reversed: ";
    printList(reversed2);
    // Expected: [2,1]

    return 0;
}
