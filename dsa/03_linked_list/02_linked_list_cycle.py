"""
PROBLEM: Linked List Cycle
LeetCode #141: https://leetcode.com/problems/linked-list-cycle/
TRACK: B (Refresh — Linked List)

Given head, the head of a linked list, determine if the linked list
has a cycle in it.

There is a cycle if some node in the list can be reached again by
continuously following the next pointer.

Return True if there is a cycle, False otherwise.

Example:
    Input: 3 -> 2 -> 0 -> -4 -> (back to node with val 2)
    Output: True

    Input: 1 -> 2 -> (back to node with val 1)
    Output: True

    Input: 1 -> None
    Output: False

CONSTRAINTS:
- Number of nodes in the list is in [0, 10^4]
- -10^5 <= Node.val <= 10^5
- Solve in O(1) extra space (no hash set)

DIFFICULTY: Easy
TIME LIMIT: 5 minutes
STARTED:
COMPLETED:
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT:
# 2. HOW:
# 3. EDGE CASES:
# 4. COMPLEXITY:


# ============================================================
# NODE DEFINITION (DO NOT MODIFY)
# ============================================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def build_cycle_list(arr, pos):
    """Build list where tail connects to node at index pos (-1 = no cycle)."""
    if not arr:
        return None
    nodes = [ListNode(v) for v in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]

def run_tests():
    tests = [
        # (arr, cycle_pos, expected)
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1, 2, 3, 4, 5], -1, False),
        ([1, 2, 3, 4, 5], 2, True),
        ([1], 0, True),
        ([1, 2, 3], -1, False),
    ]

    passed = 0
    total = len(tests)

    for i, (arr, pos, expected) in enumerate(tests, 1):
        try:
            head = build_cycle_list(arr, pos)
            result = has_cycle(head)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                cycle_desc = f"cycle at pos {pos}" if pos >= 0 else "no cycle"
                print(f"  [FAIL] Test {i}: has_cycle({arr}, {cycle_desc}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
