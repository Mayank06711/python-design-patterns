/*
 * Problem: Add Two Numbers (LeetCode #2) - Medium
 *
 * You are given two non-empty linked lists representing two
 * non-negative integers. The digits are stored in reverse order,
 * and each node contains a single digit. Add the two numbers
 * and return the sum as a linked list.
 *
 * Approach: Traverse both lists simultaneously, digit by digit.
 * Maintain a carry variable. Create new nodes for the result.
 * Continue until both lists are exhausted and carry is 0.
 *
 * Time Complexity:  O(max(n, m))
 * Space Complexity: O(max(n, m)) for the result list
 *
 * Example: [2,4,3] + [5,6,4] -> [7,0,8]
 *          (342 + 465 = 807)
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // TODO: Implement digit-by-digit addition with carry
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

    ListNode* l1 = buildList({2, 4, 3});
    ListNode* l2 = buildList({5, 6, 4});
    cout << "List 1: ";
    printList(l1);
    cout << "List 2: ";
    printList(l2);

    ListNode* sum1 = sol.addTwoNumbers(l1, l2);
    cout << "Sum:    ";
    printList(sum1);
    // Expected: [7,0,8] (342 + 465 = 807)

    cout << endl;
    ListNode* l3 = buildList({9, 9, 9, 9, 9, 9, 9});
    ListNode* l4 = buildList({9, 9, 9, 9});
    cout << "List 3: ";
    printList(l3);
    cout << "List 4: ";
    printList(l4);

    ListNode* sum2 = sol.addTwoNumbers(l3, l4);
    cout << "Sum:    ";
    printList(sum2);
    // Expected: [8,9,9,9,0,0,0,1] (9999999 + 9999 = 10009998)

    return 0;
}
