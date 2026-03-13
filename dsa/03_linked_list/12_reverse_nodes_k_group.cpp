/*
 * Problem: Reverse Nodes in k-Group (LeetCode #25) - Hard
 *
 * Given the head of a linked list, reverse the nodes of the
 * list k at a time, and return the modified list.
 *
 * k is a positive integer and is less than or equal to the
 * length of the linked list. If the number of nodes is not
 * a multiple of k then left-out nodes at the end should
 * remain as they are.
 *
 * Approach:
 *   1. Count k nodes ahead. If fewer than k remain, stop.
 *   2. Reverse the current group of k nodes.
 *   3. Connect the reversed group to the previous part.
 *   4. Recurse or iterate for the next group.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1) iterative, O(n/k) recursive stack
 *
 * Example: [1,2,3,4,5] k=2 -> [2,1,4,3,5]
 *          [1,2,3,4,5] k=3 -> [3,2,1,4,5]
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        // TODO: Implement reverse sublists of size k
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
    ListNode* r1 = sol.reverseKGroup(l1, 2);
    cout << "k=2:      ";
    printList(r1);
    // Expected: [2,1,4,3,5]

    cout << endl;
    ListNode* l2 = buildList({1, 2, 3, 4, 5});
    cout << "Original: ";
    printList(l2);
    ListNode* r2 = sol.reverseKGroup(l2, 3);
    cout << "k=3:      ";
    printList(r2);
    // Expected: [3,2,1,4,5]

    cout << endl;
    ListNode* l3 = buildList({1, 2, 3, 4, 5});
    cout << "Original: ";
    printList(l3);
    ListNode* r3 = sol.reverseKGroup(l3, 1);
    cout << "k=1:      ";
    printList(r3);
    // Expected: [1,2,3,4,5] (no change)

    return 0;
}
