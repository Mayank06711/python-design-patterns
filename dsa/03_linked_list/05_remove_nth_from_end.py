"""
Remove Nth Node From End of List
LeetCode #19: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the END of the
list and return its head.

Examples:
  1 -> 2 -> 3 -> 4 -> 5, n=2  ->  1 -> 2 -> 3 -> 5
  1, n=1  ->  (empty list)
  1 -> 2, n=1  ->  1

Constraints:
- Number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Follow-up: Can you do this in one pass?

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?) question want me to remove nth node from ending of linkedlist
# 2. HOW: (step-by-step algorithm) # brute force is to fid length of linked list then substract n from len then go till on before an drmeove node.
# 3. EDGE CASES: (what could go wrong?) n == length we need to remove head
# 4. COMPLEXITY: (time and space) O(n), S>c O(1)
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    temp = head
    for i in range(n):
        temp = temp.next
    if temp is None:
        return head.next
    slow = head
    while(temp.next):
        slow = slow.next
        temp = temp.next
    slow.next = slow.next.next
    return head


    


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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
        ([1, 2, 3], 1, [1, 2]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([10, 20, 30, 40], 2, [10, 20, 40]),
        ([5, 10], 2, [10]),
    ]

    passed = 0
    total = len(tests)

    for i, (arr, n, expected) in enumerate(tests, 1):
        try:
            head = build_list(arr)
            result = list_to_arr(remove_nth_from_end(head, n))
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: remove_nth({arr}, {n}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
