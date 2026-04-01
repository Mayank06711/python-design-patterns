"""
PROBLEM: Middle of the Linked List
LeetCode #876: https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node.

If there are two middle nodes, return the SECOND middle node.

Examples:
  [1,2,3,4,5] → return node 3
  [1,2,3,4,5,6] → return node 4 (the second middle)

Constraints:
- The number of nodes is in range [1, 100]
- 1 <= Node.val <= 100

DIFFICULTY: Easy
TIME LIMIT: 5 minutes
STARTED: 2:37 PM, Apr 1, 2026
COMPLETED: 3:04 PM, Apr 1, 2026
ATTEMPT: 2 (rewrote with fast/slow optimal)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?) question want me to find the middle of linkedlist , 
# 2. HOW: (step-by-step algorithm) # O(n) in 2 pass where in first pass we will find the length of linkedlist by traversing all the linked list, then in 2nd pass we go till middle and return
# 3. EDGE CASES: (what could go wrong?) # cycle in linkedlist, no node
# 4. COMPLEXITY: (time and space) # t.c O(N) and s.c O(1)
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def middle_node(head):
    if head is None:
        return 
    if head.next  is None:
        return head
    slow = head
    fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow




# ============================================================
# HELPER FUNCTIONS — DO NOT MODIFY
# ============================================================

def build_list(values):
    """Build a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (values, expected_middle_val)
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6], 4),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 3),
        ([5, 4, 3, 2, 1, 0], 2),
        ([10], 10),
    ]

    passed = 0
    total = len(tests)

    for i, (values, expected) in enumerate(tests, 1):
        try:
            head = build_list(values)
            result = middle_node(head)
            if result and result.val == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                actual = result.val if result else None
                print(f"  [FAIL] Test {i}: middle_node({values}) = {actual}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
