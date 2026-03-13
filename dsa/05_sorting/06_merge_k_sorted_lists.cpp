/*
 * Problem: Merge k Sorted Lists (LeetCode #23) - Hard
 *
 * Given an array of k linked-lists, each sorted in ascending order,
 * merge all into one sorted linked-list.
 *
 * Approach 1: Min-Heap (Priority Queue)
 *   - Push head of each list into a min-heap.
 *   - Pop smallest, append to result, push its next node if exists.
 *   - Repeat until heap is empty.
 *
 * Approach 2: Divide and Conquer
 *   - Merge lists in pairs repeatedly until one remains.
 *
 * Time:  O(N log k) where N = total nodes, k = number of lists
 * Space: O(k) for the heap
 *
 * Example: lists=[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
 */

#include <iostream>
#include <vector>
#include <queue>
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // TODO: implement min-heap or divide-and-conquer merge
        return nullptr;
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

void runTest(int t, vector<vector<int>> inputs, const vector<int>& exp) {
    Solution sol;
    vector<ListNode*> lists;
    for (auto& v : inputs) lists.push_back(buildList(v));
    ListNode* res = sol.mergeKLists(lists);
    vector<int> got = listToVec(res);
    cout << "Test " << t << ": " << (got == exp ? "PASSED" : "FAILED")
         << " | Got: " << vecToString(got) << " Expected: " << vecToString(exp) << endl;
    freeList(res);
}

int main() {
    cout << "=== Merge k Sorted Lists (LC #23) ===" << endl;
    runTest(1, {{1,4,5},{1,3,4},{2,6}}, {1,1,2,3,4,4,5,6});
    runTest(2, {}, {});
    runTest(3, {{}}, {});
    runTest(4, {{1,2,3}}, {1,2,3});
    runTest(5, {{1,3,5},{2,4,6}}, {1,2,3,4,5,6});
    runTest(6, {{1},{0}}, {0,1});
    return 0;
}
