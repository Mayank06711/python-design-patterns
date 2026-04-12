"""
Exercise: Build MyDeque from Scratch
=====================================

STARTED:   2026-04-09 13:57:16
COMPLETED: 2026-04-09 15:04:30
ATTEMPT:   4 runs (check + 3 failed + 1 pass)
SCORE:     7/10 (Correctness 4 + Attempts 1 + Hints 1 + Quality 1)
TIME:      ~67 min (target 18 — over by a lot because of pointer-chasing bugs)

KEY LEARNINGS:
  1. Standard DLL insert-between-A-and-B pattern beats any clever "shift the
     dummy" trick. You initially tried the shift trick, it worked for the
     structure but made pop/peek inconsistent (pop read from dummy, peek read
     from dummy.prev). You refactored to the standard pattern and the bugs
     evaporated. Lesson: when a pattern forces special-casing downstream, it's
     probably wrong — the standard pattern is standard BECAUSE it composes.

  2. Dummies NEVER hold values. Every read must walk PAST the dummy
     (self.head.next.val, self.tail.prev.val). Every check for "empty" is
     "head.next IS tail" (identity), never "head.next is None".

  3. __iter__ off-by-one: if your loop condition checks X but you read from
     X.next, the loop runs one step too many. Fix by either checking X.next
     in the condition, OR by starting X at the first real node and reading
     from X itself.

  4. __bool__ is the OPPOSITE of "is it empty?" — an empty collection should
     be falsy.

  5. list in a loop: list.pop(0) is O(n), so n pops = O(n²). Deque pops are
     O(1) on both ends.

WHY THIS EXERCISE EXISTS:
-------------------------
You asked to build a deque from scratch because "internally it uses a doubly
linked list." This is the right instinct. Building the data structure forces
you to derive WHY append/appendleft/pop/popleft are all O(1) — because a
doubly linked list gives you direct pointers to BOTH ends.

After you finish this, you'll use YOUR OWN MyDeque to solve Sliding Window
Maximum optimal (revision). Building then using = the deepest way to learn.

---

PROBLEM:
--------
Implement a `MyDeque` class that supports all core deque operations in O(1)
on both ends. You must use a doubly linked list internally — NOT a Python list.
The whole point is to earn the O(1) guarantee on BOTH ends.

INTERFACE (the tests will exercise all of these):
  - append(val)      : add val to the RIGHT end                O(1)
  - appendleft(val)  : add val to the LEFT end                 O(1)
  - pop()            : remove and return RIGHT end             O(1)
                       raise IndexError if empty
  - popleft()        : remove and return LEFT end              O(1)
                       raise IndexError if empty
  - peek_right()     : return RIGHT end without removing       O(1)
                       raise IndexError if empty
  - peek_left()      : return LEFT end without removing        O(1)
                       raise IndexError if empty
  - __len__()        : number of elements                      O(1)
  - __iter__()       : iterate left-to-right                   O(n) total
  - __bool__()       : True if non-empty (optional, free from __len__)

CONSTRAINTS:
  - NO using `collections.deque` (the whole point is you're building it)
  - NO using Python list / array for storage
  - All advertised O(1) operations must actually be O(1) (no loops)
  - All pointer wiring must be correct — a popped node should not leave
    dangling references into the deque

DESIGN HINT (free — this is the only "hint"):
  Think about the dummy head / dummy tail pattern you used in Merge Two Lists.
  It massively simplifies edge cases (empty deque, single-element deque,
  removing the first/last real node) because real nodes ALWAYS have neighbors
  on both sides. Without dummies you'll write a lot of `if self.head is None`
  checks and get pointer bugs.

---
"""
class ListNode:
    def __init__(self, val, Prev = None,Next = None):
        self.val = val
        self.next = Next
        self.prev = Prev

class MyDeque:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.total_nodes = 0
    
    def __len__(self):
        return self.total_nodes
    
    def append(self, val):
        temp = ListNode(val)
        temp.next = self.tail
        temp.prev = self.tail.prev
        self.tail.prev.next = temp
        self.tail.prev = temp
        self.total_nodes += 1
    
    def appendleft(self, val):
        temp = ListNode(val)
        temp.next = self.head.next
        temp.prev = self.head
        self.head.next.prev = temp
        self.head.next = temp
        self.total_nodes += 1

    def pop(self):
        if self.total_nodes >= 1:
            temp = self.tail
            val =  self.tail.prev.val
            self.tail.prev.next = None
            self.tail.prev.val = None
            self.tail = self.tail.prev
            temp.prev = None
            self.total_nodes -= 1
            return val
        else:
            raise IndexError("Index not in scope")
    

    def popleft(self):
        if self.total_nodes >= 1:
            temp = self.head
            val =  self.head.next.val
            self.head.next.prev = None
            self.head.next.val = None
            self.head = self.head.next
            temp.prev = None
            self.total_nodes -= 1
            return val
        else:
            raise IndexError("Index not in scope")

    def peek_right(self):
        if self.total_nodes >=1:
            return self.tail.prev.val
        else:
            raise IndexError("Index out of bound")

    def peek_left(self):
        if self.total_nodes >= 1:
            return self.head.next.val
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        temp_head = self.head
        if self.total_nodes == 0:
            return []
        while(temp_head.next != self.tail):
            yield temp_head.next.val
            temp_head = temp_head.next

    def __bool__(self):
        if self.total_nodes == 0:
            return False
        else:
            return True  



    


    

        


# ============================================================================
# TESTS — do not modify below this line
# ============================================================================

def test_empty_deque():
    dq = MyDeque()
    assert len(dq) == 0, f"empty len should be 0, got {len(dq)}"
    assert not dq, "empty deque should be falsy"
    try:
        dq.pop()
        assert False, "pop on empty should raise IndexError"
    except IndexError:
        pass
    try:
        dq.popleft()
        assert False, "popleft on empty should raise IndexError"
    except IndexError:
        pass
    try:
        dq.peek_left()
        assert False, "peek_left on empty should raise IndexError"
    except IndexError:
        pass
    try:
        dq.peek_right()
        assert False, "peek_right on empty should raise IndexError"
    except IndexError:
        pass
    print("PASS: empty deque behaves correctly")


def test_append_and_pop_right_only():
    dq = MyDeque()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    assert len(dq) == 3
    assert dq.peek_right() == 3
    assert dq.peek_left() == 1
    assert dq.pop() == 3
    assert dq.pop() == 2
    assert dq.pop() == 1
    assert len(dq) == 0
    print("PASS: append + pop (right side acts as stack)")


def test_appendleft_and_popleft_only():
    dq = MyDeque()
    dq.appendleft(1)
    dq.appendleft(2)
    dq.appendleft(3)
    # order from left to right is now: 3, 2, 1
    assert dq.peek_left() == 3
    assert dq.peek_right() == 1
    assert dq.popleft() == 3
    assert dq.popleft() == 2
    assert dq.popleft() == 1
    assert len(dq) == 0
    print("PASS: appendleft + popleft (left side)")


def test_fifo_queue_behavior():
    """Classic queue: append right, popleft."""
    dq = MyDeque()
    for x in [10, 20, 30, 40]:
        dq.append(x)
    assert dq.popleft() == 10
    assert dq.popleft() == 20
    assert dq.popleft() == 30
    assert dq.popleft() == 40
    assert len(dq) == 0
    print("PASS: FIFO queue behavior (append right, popleft)")


def test_mixed_operations():
    dq = MyDeque()
    dq.append(1)            # [1]
    dq.appendleft(0)        # [0, 1]
    dq.append(2)            # [0, 1, 2]
    dq.appendleft(-1)       # [-1, 0, 1, 2]
    assert len(dq) == 4
    assert dq.peek_left() == -1
    assert dq.peek_right() == 2
    assert dq.popleft() == -1   # [0, 1, 2]
    assert dq.pop() == 2         # [0, 1]
    assert dq.peek_left() == 0
    assert dq.peek_right() == 1
    assert len(dq) == 2
    print("PASS: mixed append/appendleft/pop/popleft")


def test_iteration_left_to_right():
    dq = MyDeque()
    for x in [5, 10, 15, 20]:
        dq.append(x)
    collected = [v for v in dq]
    assert collected == [5, 10, 15, 20], f"iteration order wrong: {collected}"
    # iterate again — should still work (iteration shouldn't consume)
    collected2 = list(dq)
    assert collected2 == [5, 10, 15, 20], "second iteration broke"
    print("PASS: iteration is left-to-right and non-consuming")


def test_refill_after_empty():
    """Edge case: empty, then fill, then empty, then fill again.
    Catches bugs where dummy-node pointers aren't reset correctly."""
    dq = MyDeque()
    dq.append(1)
    dq.append(2)
    dq.popleft()
    dq.popleft()
    assert len(dq) == 0
    # refill
    dq.appendleft(100)
    dq.append(200)
    assert len(dq) == 2
    assert dq.peek_left() == 100
    assert dq.peek_right() == 200
    assert list(dq) == [100, 200]
    print("PASS: deque can be refilled after being fully emptied")


def test_single_element_both_ends():
    """Single element: peek_left == peek_right, and either pop drains it."""
    dq = MyDeque()
    dq.append(42)
    assert dq.peek_left() == 42
    assert dq.peek_right() == 42
    assert len(dq) == 1
    assert dq.pop() == 42
    assert len(dq) == 0

    dq.appendleft(99)
    assert dq.popleft() == 99
    assert len(dq) == 0
    print("PASS: single-element edge cases work for both ends")


def test_large_mixed_workload():
    """Stress test — catches O(n) bugs masquerading as O(1)."""
    dq = MyDeque()
    expected = []
    for i in range(1000):
        if i % 2 == 0:
            dq.append(i)
            expected.append(i)
        else:
            dq.appendleft(i)
            expected.insert(0, i)
    assert len(dq) == 1000
    assert list(dq) == expected, "order diverged during 1000-op workload"

    # now drain alternately
    for i in range(500):
        dq.popleft()
        dq.pop()
    assert len(dq) == 0
    print("PASS: 1000-op mixed workload correct")


def test_peek_does_not_remove():
    dq = MyDeque()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    assert dq.peek_right() == 3
    assert dq.peek_right() == 3   # peek twice → same value
    assert dq.peek_left() == 1
    assert dq.peek_left() == 1
    assert len(dq) == 3           # peeks did not mutate
    print("PASS: peek_left and peek_right do not mutate")


if __name__ == "__main__":
    test_empty_deque()
    test_append_and_pop_right_only()
    test_appendleft_and_popleft_only()
    test_fifo_queue_behavior()
    test_mixed_operations()
    test_iteration_left_to_right()
    test_refill_after_empty()
    test_single_element_both_ends()
    test_large_mixed_workload()
    test_peek_does_not_remove()
    print("\nAll 10 tests passed ✅  MyDeque is ready to use in Sliding Window Max.")
