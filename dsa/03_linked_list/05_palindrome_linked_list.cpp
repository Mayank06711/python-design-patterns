/*
 * Problem: Palindrome Linked List (LeetCode #234) - Easy
 *
 * Given the head of a singly linked list, return true if it
 * is a palindrome, false otherwise.
 *
 * Approach:
 *   1. Find the middle of the list using slow/fast pointers.
 *   2. Reverse the second half of the list.
 *   3. Compare the first half and reversed second half node by node.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 *
 * Example: [1,2,2,1] -> true
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
    bool isPalindrome(ListNode* head) {
        // TODO: Implement find mid + reverse half + compare
        return false;
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

int main() {
    Solution sol;

    ListNode* l1 = buildList({1, 2, 2, 1});
    cout << "Test [1,2,2,1]:   " << (sol.isPalindrome(l1) ? "true" : "false") << endl;
    // Expected: true

    ListNode* l2 = buildList({1, 2});
    cout << "Test [1,2]:       " << (sol.isPalindrome(l2) ? "true" : "false") << endl;
    // Expected: false

    ListNode* l3 = buildList({1, 2, 3, 2, 1});
    cout << "Test [1,2,3,2,1]: " << (sol.isPalindrome(l3) ? "true" : "false") << endl;
    // Expected: true

    ListNode* l4 = buildList({1});
    cout << "Test [1]:         " << (sol.isPalindrome(l4) ? "true" : "false") << endl;
    // Expected: true

    return 0;
}
