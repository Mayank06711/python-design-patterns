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
STARTED: 1:30 PM, Mar 29, 2026
COMPLETED: 2:00 PM, Mar 29, 2026
ATTEMPT: 1 (hash map first, then Floyd's after or→and fix)
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: question want me to find out wether likedlistis cyclic or not
# 2. HOW: run a loop while loop till head->next != null and inside we will use a hashmap which will store the nodes and in each iteration we check wether the current node already exist in node or not if yes it a cyclic linkedlist.
# 3. EDGE CASES: empty or only head node is given
# 4. COMPLEXITY:t.c-> O(n) and s.c->O(n)
# algo 2 
# we take twwo pointer slow and fast slow run one step at a time and fast runs two at a time so if its circular so till slow complet one revoltution fast will do twice
# this way if they ever meet it means it was circular
#t.c O(N) s.c O(1)

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
def has_cycle_brute(head: ListNode)->bool:
    if head is None or head.next == None:
        return False
    temp = head
    hash_map = {}
    hash_map[temp] = 1
    temp = temp.next
    while(temp.next):
        if hash_map.get(temp):
            return True
        else:
            hash_map[temp] = 1
            temp = temp.next
    
    return False
def has_cycle(head:ListNode)->bool:
    if head is None or head.next is None:
        return False
    slow = head
    fast = head
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    return False


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
