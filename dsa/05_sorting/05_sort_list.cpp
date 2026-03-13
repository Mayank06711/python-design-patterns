/*
 * Problem: Sort List (LeetCode #148) - Medium
 *
 * Given the head of a linked list, return the list after sorting it in
 * ascending order using O(n log n) time.
 *
 * Approach: Merge sort on linked list.
 *   - Use slow/fast pointer to find the middle.
 *   - Split the list into two halves.
 *   - Recursively sort each half.
 *   - Merge the two sorted halves.
 *
 * Time:  O(n log n)
 * Space: O(log n) recursion stack
 *
 * Example: [4,2,1,3] -> [1,2,3,4]
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* n) : val(x), next(n) {}
};

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        // TODO: implement merge sort on linked list
        return head;
    }
};

ListNode* buildList(const vector<int>& vals) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int v : vals) { tail->next = new ListNode(v); tail = tail->next; }
    return dummy.next;
}

vector<int> listToVec(ListNode* head) {
    vector<int> res;
    while (head) { res.push_back(head->val); head = head->next; }
    return res;
}

void freeList(ListNode* head) {
    while (head) { ListNode* t = head; head = head->next; delete t; }
}

string vecToString(const vector<int>& v) {
    string s = "[";
    for (int i = 0; i < (int)v.size(); i++) {
        if (i > 0) s += ",";
        s += to_string(v[i]);
    }
    return s + "]";
}

void runTest(int t, const vector<int>& input, const vector<int>& exp) {
    Solution sol;
    ListNode* head = buildList(input);
    head = sol.sortList(head);
    vector<int> res = listToVec(head);
    cout << "Test " << t << ": " << (res == exp ? "PASSED" : "FAILED")
         << " | Got: " << vecToString(res) << " Expected: " << vecToString(exp) << endl;
    freeList(head);
}

int main() {
    cout << "=== Sort List (LC #148) ===" << endl;
    runTest(1, {4,2,1,3}, {1,2,3,4});
    runTest(2, {-1,5,3,4,0}, {-1,0,3,4,5});
    runTest(3, {}, {});
    runTest(4, {1}, {1});
    runTest(5, {5,4,3,2,1}, {1,2,3,4,5});
    runTest(6, {3,1,2,3,1}, {1,1,2,3,3});
    return 0;
}
