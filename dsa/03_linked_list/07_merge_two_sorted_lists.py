"""
PROBLEM: Merge Two Sorted Lists
LeetCode #21: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

CONSTRAINTS:
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

DIFFICULTY: Easy
TIME LIMIT: 5 minutes
STARTED:
COMPLETED:
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: question want me sort the given linked list without using extra space i mean by using these two list
# 2. HOW: 1: i will take a dummy node so it can be used for returnng and merging the list, i will iterate on first pass til both list1 and 2 exist once any of these done we will go in other 2 loops (bcz their length can be diff) and merge but sicne we use same list for sorting its not needed. we compare the val of list nodes and merge in orde
# 3. EDGE CASES:  one them is empty or head is noen return the 2nd list both are such that we just have to point tail of one to head of other When you start a loop inside that loop we will check if L1 dot value is less than equals to L2 dot value then we will create a dummy note which will save L1 next like saving where L1 next exist then we will point L1 next to L2 right then we will move L1 to dummy node otherwise we will do the same for L and once the loop is done we will check if L1 is there that means L2 is finished and L2's tail needs to point at L1 so we will point L2 next L1 and if L1 is not exist like LL1 is finished L2 there L2 L1's next will point to L2 
# 4. COMPLEXITY: Time O(?), Space O(?): max(O(n,m)), O(1)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    temp1 = list1
    temp2 = list2
    dummy = ListNode(0)
    head = dummy
    while(temp1 and temp2):
        if temp1.val <= temp2.val:
            dummy.next = temp1
            temp1 = temp1.next
            dummy = dummy.next
        else:
            dummy.next = temp2
            temp2 = temp2.next
            dummy = dummy.next
    if(temp1):
        dummy.next = temp1
        dummy = dummy.next
    if(temp2):
        dummy.next = temp2
        dummy = dummy.next
    return head.next



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================
def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def run_tests():
    passed = 0
    total = 8

    # Test 1: basic merge
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    result = list_to_array(merge_two_lists(l1, l2))
    if result == [1, 1, 2, 3, 4, 4]:
        print("  [PASS] Test 1: [1,2,4] + [1,3,4] → [1,1,2,3,4,4]")
        passed += 1
    else:
        print(f"  [FAIL] Test 1: got {result}, expected [1,1,2,3,4,4]")

    # Test 2: both empty
    result = list_to_array(merge_two_lists(None, None))
    if result == []:
        print("  [PASS] Test 2: both empty → []")
        passed += 1
    else:
        print(f"  [FAIL] Test 2: got {result}, expected []")

    # Test 3: one empty
    l1 = build_list([1, 2, 3])
    result = list_to_array(merge_two_lists(l1, None))
    if result == [1, 2, 3]:
        print("  [PASS] Test 3: one empty → other list")
        passed += 1
    else:
        print(f"  [FAIL] Test 3: got {result}, expected [1,2,3]")

    # Test 4: other empty
    l2 = build_list([4, 5, 6])
    result = list_to_array(merge_two_lists(None, l2))
    if result == [4, 5, 6]:
        print("  [PASS] Test 4: first empty → second list")
        passed += 1
    else:
        print(f"  [FAIL] Test 4: got {result}, expected [4,5,6]")

    # Test 5: different lengths
    l1 = build_list([1, 5])
    l2 = build_list([2, 3, 4, 6, 7])
    result = list_to_array(merge_two_lists(l1, l2))
    if result == [1, 2, 3, 4, 5, 6, 7]:
        print("  [PASS] Test 5: different lengths merged correctly")
        passed += 1
    else:
        print(f"  [FAIL] Test 5: got {result}, expected [1,2,3,4,5,6,7]")

    # Test 6: single element each
    l1 = build_list([2])
    l2 = build_list([1])
    result = list_to_array(merge_two_lists(l1, l2))
    if result == [1, 2]:
        print("  [PASS] Test 6: [2] + [1] → [1,2]")
        passed += 1
    else:
        print(f"  [FAIL] Test 6: got {result}, expected [1,2]")

    # Test 7: duplicates across lists
    l1 = build_list([1, 1, 1])
    l2 = build_list([1, 1, 1])
    result = list_to_array(merge_two_lists(l1, l2))
    if result == [1, 1, 1, 1, 1, 1]:
        print("  [PASS] Test 7: all duplicates merged")
        passed += 1
    else:
        print(f"  [FAIL] Test 7: got {result}, expected [1,1,1,1,1,1]")

    # Test 8: negative values
    l1 = build_list([-3, -1, 2])
    l2 = build_list([-2, 0, 4])
    result = list_to_array(merge_two_lists(l1, l2))
    if result == [-3, -2, -1, 0, 2, 4]:
        print("  [PASS] Test 8: negative values merged")
        passed += 1
    else:
        print(f"  [FAIL] Test 8: got {result}, expected [-3,-2,-1,0,2,4]")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
