/*
 * Problem: LRU Cache (LeetCode #146) - Medium
 *
 * Design a data structure that follows the constraints of a
 * Least Recently Used (LRU) cache.
 *
 * Implement the LRUCache class:
 *   - LRUCache(int capacity): Initialize with positive capacity.
 *   - int get(int key): Return the value if key exists, otherwise -1.
 *   - void put(int key, int value): Update or insert. If capacity
 *     is exceeded, evict the least recently used key.
 *
 * Both get and put must run in O(1) average time.
 *
 * Approach: Doubly linked list + hash map.
 *   - Hash map: key -> pointer to node in the doubly linked list.
 *   - Doubly linked list: maintains usage order (most recent at head,
 *     least recent at tail).
 *   - On get/put: move the accessed node to the head.
 *   - On capacity overflow: remove from tail (least recently used).
 *
 * This is one of the most frequently asked design + data structure
 * interview problems.
 *
 * Time Complexity:  O(1) for both get and put
 * Space Complexity: O(capacity)
 */

#include <iostream>
#include <unordered_map>
using namespace std;

// Doubly linked list node
struct DLLNode {
    int key;
    int val;
    DLLNode* prev;
    DLLNode* next;
    DLLNode(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
public:
    LRUCache(int capacity) {
        // TODO: Initialize capacity, hash map, and dummy head/tail nodes
    }

    int get(int key) {
        // TODO: If key exists, move to front and return value; else return -1
        return -1;
    }

    void put(int key, int value) {
        // TODO: Insert or update. If over capacity, evict LRU (tail).
    }

private:
    // TODO: Declare capacity, hash map, dummy head/tail
    // Helper methods you may want to implement:
    // void addToFront(DLLNode* node) {}
    // void removeNode(DLLNode* node) {}
    // void moveToFront(DLLNode* node) {}
    // DLLNode* removeLRU() {}
};

int main() {
    // Test: ["LRUCache","put","put","get","put","get","put","get","get","get"]
    //       [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    LRUCache cache(2);

    cache.put(1, 1);
    cout << "put(1, 1)" << endl;

    cache.put(2, 2);
    cout << "put(2, 2)" << endl;

    cout << "get(1) = " << cache.get(1) << endl;
    // Expected: 1

    cache.put(3, 3); // evicts key 2
    cout << "put(3, 3) -- evicts key 2" << endl;

    cout << "get(2) = " << cache.get(2) << endl;
    // Expected: -1 (evicted)

    cache.put(4, 4); // evicts key 1
    cout << "put(4, 4) -- evicts key 1" << endl;

    cout << "get(1) = " << cache.get(1) << endl;
    // Expected: -1 (evicted)

    cout << "get(3) = " << cache.get(3) << endl;
    // Expected: 3

    cout << "get(4) = " << cache.get(4) << endl;
    // Expected: 4

    return 0;
}
