/*
 * Problem: Copy List with Random Pointer (LeetCode #138) - Medium
 *
 * A linked list of length n is given such that each node contains
 * an additional random pointer, which could point to any node
 * in the list, or null. Construct a deep copy of the list.
 *
 * Approach 1 (Hash Map): Use a hash map to map original nodes
 * to their copies. Two passes: first create all copies, then
 * set next and random pointers.
 *
 * Approach 2 (Interleaving): Insert copies right after originals,
 * then set random pointers, then separate the two lists.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n) for hash map, O(1) for interleaving
 */

#include <iostream>
#include <unordered_map>
using namespace std;

// Special Node for this problem (has random pointer)
struct Node {
    int val;
    Node* next;
    Node* random;
    Node(int x) : val(x), next(nullptr), random(nullptr) {}
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        // TODO: Implement hash map clone or interleaving trick
        return nullptr;
    }
};

void printList(Node* head) {
    cout << "[";
    while (head) {
        cout << "[" << head->val << ",";
        if (head->random) {
            cout << head->random->val;
        } else {
            cout << "null";
        }
        cout << "]";
        if (head->next) cout << ",";
        head = head->next;
    }
    cout << "]" << endl;
}

int main() {
    Solution sol;

    // Build: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Node* n1 = new Node(7);
    Node* n2 = new Node(13);
    Node* n3 = new Node(11);
    Node* n4 = new Node(10);
    Node* n5 = new Node(1);

    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n5;

    n1->random = nullptr;
    n2->random = n1;      // 13 -> 7
    n3->random = n5;      // 11 -> 1
    n4->random = n3;      // 10 -> 11
    n5->random = n1;      // 1 -> 7

    cout << "Original: ";
    printList(n1);

    Node* copied = sol.copyRandomList(n1);
    cout << "Copied:   ";
    printList(copied);
    // Expected: [[7,null],[13,7],[11,1],[10,11],[1,7]]

    // Verify deep copy (different pointers)
    if (copied && copied != n1) {
        cout << "Deep copy verified (different memory addresses)" << endl;
    }

    return 0;
}
