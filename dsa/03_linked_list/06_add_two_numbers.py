"""
Add Two Numbers
LeetCode #2: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in REVERSE order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list.

Examples:
  l1: 2 -> 4 -> 3  (represents 342)
  l2: 5 -> 6 -> 4  (represents 465)
  out: 7 -> 0 -> 8  (represents 807, because 342 + 465 = 807)

  l1: 0
  l2: 0
  out: 0

  l1: 9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9  (9999999)
  l2: 9 -> 9 -> 9 -> 9                  (9999)
  out: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1  (10009998)

Constraints:
- Number of nodes in each list is [1, 100]
- 0 <= Node.val <= 9
- No leading zeros (except the number 0 itself)

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?) question wants me to cal sum of number linkedlist and return a new linkedliist which respresrt sum
# 2. HOW: (step-by-step algorithm) # there are two ways to solve this: 1: one iterte over linklist and create the actual number then sum and then same their didgits in new linkedlist by reverse it 2: we iterate over both given linkedlist till one of their node not raches tail and inside it we add nodes if there is a carry we take it for next iteration and while doing this we also keep adding sum in new linkedlist
# 3. EDGE CASES: (what could go wrong?) can`t find`
# 4. COMPLEXITY: (time and space) O(n+m)  where n+m is size of given linked list, s.c O(n) which is to store the answer
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    carry = 0
    result = ListNode(0)
    head = result
    temp1 = l1
    temp2 = l2
    while(temp1 and temp2):
        curr_sum = temp1.val + temp2.val + carry
        carry = curr_sum//10
        ones_digit = curr_sum%10
        curr_node = ListNode(ones_digit)
        result.next = curr_node
        result = result.next
        temp1 = temp1.next
        temp2 = temp2.next

    while(temp1):
        curr_sum = temp1.val + carry
        carry = curr_sum//10
        ones_digit = curr_sum%10
        curr_node = ListNode(ones_digit)
        result.next = curr_node
        result = result.next
        temp1 = temp1.next
    while(temp2):
        curr_sum = temp2.val + carry
        carry = curr_sum//10
        ones_digit = curr_sum%10
        curr_node = ListNode(ones_digit)
        result.next = curr_node
        result = result.next
        temp2 = temp2.next

    if carry > 0:
        curr_node = ListNode(carry)
        result.next = curr_node
        result = result.next
    return head.next
        
    




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
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1], [9, 9, 9], [0, 0, 0, 1]),
        ([5], [5], [0, 1]),
        ([1, 8], [0], [1, 8]),
        ([2, 4, 9], [5, 6, 4, 9], [7, 0, 4, 0, 1]),
        ([0, 0, 1], [0, 0, 2], [0, 0, 3]),
        ([9], [1], [0, 1]),
        ([1, 2, 3], [1, 2, 3], [2, 4, 6]),
    ]

    passed = 0
    total = len(tests)

    for i, (l1_arr, l2_arr, expected) in enumerate(tests, 1):
        try:
            l1 = build_list(l1_arr)
            l2 = build_list(l2_arr)
            result = list_to_arr(add_two_numbers(l1, l2))
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: add({l1_arr}, {l2_arr}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
