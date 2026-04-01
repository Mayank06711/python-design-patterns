"""
PROBLEM: Linked List Cycle II
LeetCode #142: https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

There is a cycle in a linked list if there is some node that can be reached
again by continuously following the next pointer.

Do NOT modify the linked list.

Follow-up: Can you solve it using O(1) memory?

Constraints:
- The number of nodes is in range [0, 10^4]
- -10^5 <= Node.val <= 10^5

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 1:35 PM, Apr 1, 2026
COMPLETED: 2:37 PM, Apr 1, 2026
ATTEMPT: 1
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?) Question want me to find that node from where cycle in linked list started , i mean the first node from where cycle started
# 2. HOW: (step-by-step algorithm)  # 1 algo-> ii will keep iterating over linked lsit and saving each node in a hashmap by checking if it already exist or not if any ndoe already exist that is the stat of cycle , #2 algo: two pointer one slow and fast fadt move by 2 step and slow by 1, then detect when they meet once they meet put the slow or fast pointer at head again and keep iterating nwo when theyy meet its starting of cycle.
# 3. EDGE CASES: (what could go wrong?)  # there is no cycle , only headh or null or linkedlist just crossed once
# 4. COMPLEXITY: (time and space)  # 1: t.c (n) and s.c O(n), 2nd: t.c O(N), s.c O(1)
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def detect_cycle(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    while(fast and fast.next):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            fast = head
            break
    if fast is None or fast.next is None:
        return None
    while(slow != fast):
        slow = slow.next
        fast = fast.next
    return slow


# ============================================================
# HELPER FUNCTIONS — DO NOT MODIFY
# ============================================================

def build_cycle_list(values, pos):
    """Build a linked list with a cycle at position pos (-1 = no cycle)"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)

    if pos >= 0:
        current.next = nodes[pos]

    return head

# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (values, cycle_pos, expected_val_at_cycle_start or None)
        ([3, 2, 0, -4], 1, 2),
        ([1, 2], 0, 1),
        ([1], -1, None),
        ([1, 2, 3, 4, 5], 2, 3),
        ([1, 2, 3, 4, 5], -1, None),
        ([5, 3, 2, 1], 0, 5),
        ([1, 2], 1, 2),
        ([], -1, None),
    ]

    passed = 0
    total = len(tests)

    for i, (values, pos, expected_val) in enumerate(tests, 1):
        try:
            head = build_cycle_list(values, pos)
            result = detect_cycle(head)

            if expected_val is None:
                if result is None:
                    print(f"  [PASS] Test {i}")
                    passed += 1
                else:
                    print(f"  [FAIL] Test {i}: Expected no cycle, but got node with val {result.val}")
            else:
                if result and result.val == expected_val:
                    print(f"  [PASS] Test {i}")
                    passed += 1
                else:
                    actual_val = result.val if result else None
                    print(f"  [FAIL] Test {i}: Expected cycle at node val {expected_val}, got {actual_val}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()