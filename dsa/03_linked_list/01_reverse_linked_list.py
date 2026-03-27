"""
PROBLEM: Reverse Linked List
LeetCode #206: https://leetcode.com/problems/reverse-linked-list/
TRACK: B (Refresh — Linked List)

Given the head of a singly linked list, reverse the list, and return
the reversed list.

Example:
    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

    Input: 1 -> 2
    Output: 2 -> 1

    Input: (empty)
    Output: (empty)

CONSTRAINTS:
- The number of nodes in the list is in the range [0, 5000]
- -5000 <= Node.val <= 5000

NOTE: In Python there are no raw pointers like C++. You work with
node objects that have .val and .next attributes. Same logic, cleaner syntax.

DIFFICULTY: Easy
TIME LIMIT: 5 minutes
STARTED: 2:00 AM, Mar 28, 2026
COMPLETED: 4:14 AM, Mar 28, 2026
ATTEMPT: 1 (2nd run after loop condition + null check fix)
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: question says simply reverse the given linked list like 1-2-3 => 3-2-1
# 2. HOW: we loop over linkedlist starting with head and rever the next so tail become head and hea d become tail
# 3. EDGE CASES: it can a circular or only head is given or null
# 4. COMPLEXITY: O(n) n -> size of linkedlist, S>c O(1)


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
def reverse_list(head: ListNode):
    if head is None or head.next == None:
        return head
    temp = head
    prev = None 
    while(temp!= None):
        temp_next = temp.next
        temp.next = prev
        prev = temp
        temp = temp_next
    return prev
        


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def list_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

def run_tests():
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 1, 1], [1, 1, 1]),
        ([1, 2, 3], [3, 2, 1]),
        ([-1, 0, 1], [1, 0, -1]),
    ]

    passed = 0
    total = len(tests)

    for i, (input_arr, expected) in enumerate(tests, 1):
        try:
            head = build_list(input_arr)
            result_head = reverse_list(head)
            result = list_to_arr(result_head)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: reverse({input_arr}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
