/*
 * Merge K Sorted Lists
 * LeetCode: #23 | Difficulty: Hard
 * Merge k sorted linked lists into one sorted list
 * Pattern: Min-heap with K pointers
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val; ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) { return nullptr; }
};

ListNode* makeList(vector<int> v) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int x : v) { cur->next = new ListNode(x); cur = cur->next; }
    return dummy.next;
}

int main() {
    Solution sol;
    vector<ListNode*> lists = {makeList({1,4,5}), makeList({1,3,4}), makeList({2,6})};
    ListNode* r = sol.mergeKLists(lists);
    cout << "Test: ";
    while (r) { cout << r->val << " "; r = r->next; }
    cout << "(expected 1 1 2 3 4 4 5 6)" << endl;
    return 0;
}
