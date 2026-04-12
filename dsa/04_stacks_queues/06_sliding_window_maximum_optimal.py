"""
Exercise: Sliding Window Maximum — OPTIMAL (Monotonic Deque)
=============================================================

LeetCode #239 — REVISION (original at 01_arrays_two_pointers/06_sliding_window_maximum.py)

STARTED:   2026-04-11 17:16:03
COMPLETED: 2026-04-11 17:40:36
ATTEMPT:   2 runs (1 meta-test bug on my side + 1 clean pass)
SCORE:     7/10 (Correctness 4 + Time 1 + Hints 1 + Quality 1)
TIME:      ~24 min / 12 min (Hard) — over budget, but new pattern

WHY THIS EXERCISE EXISTS:
-------------------------
You solved this BRUTE FORCE (O(n·k)) on Mar 26 and it's been stuck on the
revision queue ever since. Today you built your own MyDeque from scratch.
Now you'll USE that deque to crack this at O(n) — the optimal solution that
interviewers expect for a "Hard" tag.

This is the canonical monotonic-deque problem. If you internalize this one,
every other "sliding window + extremum" problem falls over.

---

PROBLEM:
--------
Given an integer array `nums` and a window size `k`, a window of size k slides
from the left end of the array to the right, one step at a time. At each
position, report the MAXIMUM value inside the window.

Example:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

    Window                 Max
    [1  3 -1] -3  5  3  6  7     3
     1 [3 -1 -3] 5  3  6  7      3
     1  3 [-1 -3  5] 3  6  7     5
     1  3 -1 [-3  5  3] 6  7     5
     1  3 -1 -3 [5  3  6] 7      6
     1  3 -1 -3  5 [3  6  7]     7

    Output: [3, 3, 5, 5, 6, 7]

CONSTRAINTS:
  - 1 <= len(nums) <= 10^5
  - -10^4 <= nums[i] <= 10^4
  - 1 <= k <= len(nums)

REQUIREMENT:
  - MUST be O(n) time (not O(n·k))
  - MUST use YOUR OWN `MyDeque` from 05_build_deque.py — no collections.deque
  - Stress test with n = 100_000 will catch any O(n·k) attempt

---

RECOGNITION (memorize this):
  "sliding window + extremum" (min/max) → **monotonic deque**
  Key insight: when a bigger number arrives, every smaller number behind it
  that's still in the window is DEAD — it can never be the max while the
  bigger number is alive. So evict them. The deque stays monotonically
  decreasing; the front is always the answer.

PATTERN TEMPLATE (memorize this, don't memorize the code):
  For each new index i:
    1. EVICT FROM BACK: while deque not empty and nums[back] <= nums[i], popleft from the back
       (they're dead — the new guy dominates them while he's alive)
    2. APPEND i to the back
    3. EVICT FROM FRONT: while the front index is outside the window (front <= i - k), pop the front
       (he fell out of the window)
    4. RECORD ANSWER: once i >= k - 1, the window is full — front of deque is the max

CRITICAL DESIGN DECISION:
  Store INDICES in the deque, not values. Why? Because step 3 needs to know
  WHEN the front element falls out of the window — that's a position check.
  If you stored values, you'd have no way to know when to evict the front.

---
"""

# ============================================================================
# IMPORT HELPER — loads YOUR MyDeque from the neighbor file.
# (Python can't `import 05_build_deque` because module names can't start with
# a digit, so we load it via importlib. This is a pragmatic hack for the
# exercise — in real code you'd rename the file.)
# ============================================================================
import os
import importlib.util

_HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "build_deque", os.path.join(_HERE, "05_build_deque.py")
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
MyDeque = _module.MyDeque


# ============================================================================
# YOUR SOLUTION — write it here.
# ============================================================================
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Return a list where the i-th element is the maximum of the window
    nums[i : i + k] for i in range(len(nums) - k + 1).

    MUST be O(n) time.
    MUST use MyDeque (not stdlib deque, not list).
    """
    # YOUR CODE HERE
    dq = MyDeque()
    ans = []
    for i in range(len(nums)):
        while(dq and nums[dq.peek_right()] <= nums[i]):
            dq.pop()
        dq.append(i)
        if dq.peek_left() <= i-k:
            dq.popleft()
        if i >= k-1:
            ans.append(nums[dq.peek_left()]) # take the maximum of this window

    return ans
            



# ============================================================================
# TESTS — do not modify below this line
# ============================================================================

def test_classic_example():
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    print("PASS: classic [1,3,-1,-3,5,3,6,7] k=3")


def test_single_element_window():
    assert max_sliding_window([1, -1, 5, 2, 3], 1) == [1, -1, 5, 2, 3]
    print("PASS: k=1 returns the array unchanged")


def test_window_equals_array():
    assert max_sliding_window([4, 1, 7, 2, 3], 5) == [7]
    print("PASS: k == len(nums) returns single max")


def test_strictly_decreasing():
    # deque keeps growing (never evicts from back), good stress for that branch
    assert max_sliding_window([9, 8, 7, 6, 5, 4, 3, 2, 1], 3) == [9, 8, 7, 6, 5, 4, 3]
    print("PASS: strictly decreasing array")


def test_strictly_increasing():
    # deque constantly evicts (back-eviction hot path)
    assert max_sliding_window([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [3, 4, 5, 6, 7, 8, 9]
    print("PASS: strictly increasing array")


def test_all_equal():
    assert max_sliding_window([5, 5, 5, 5, 5], 3) == [5, 5, 5]
    print("PASS: all equal elements")


def test_negative_numbers():
    assert max_sliding_window([-7, -8, 7, 5, 7, 1, 6, 0], 4) == [7, 7, 7, 7, 7]
    print("PASS: mixed negative and positive")


def test_two_elements():
    assert max_sliding_window([9, 11], 2) == [11]
    print("PASS: two elements k=2")


def test_duplicates_with_repeats():
    assert max_sliding_window([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]
    print("PASS: duplicates and mixed")


def test_front_eviction_path():
    # Max keeps falling out of the window, forcing front-eviction
    assert max_sliding_window([10, 1, 2, 3, 4, 5], 2) == [10, 2, 3, 4, 5]
    print("PASS: front-eviction when max leaves window")


def test_large_stress_on_performance():
    """Catches O(n*k) attempts. n=100_000, k=500 → brute would be ~50M ops.
    O(n) solution finishes in well under a second."""
    import time
    n = 100_000
    k = 500
    nums = [(i * 2654435761) & 0xFFFF for i in range(n)]  # cheap pseudo-random
    start = time.perf_counter()
    result = max_sliding_window(nums, k)
    elapsed = time.perf_counter() - start
    assert len(result) == n - k + 1, f"wrong length: {len(result)} vs {n - k + 1}"
    # sanity: each window's reported max must equal the true max of that window
    # (check 5 random windows — full check would itself be O(n*k))
    import random
    random.seed(42)
    for _ in range(5):
        i = random.randint(0, n - k)
        true_max = max(nums[i:i + k])
        assert result[i] == true_max, f"window {i}: got {result[i]}, true {true_max}"
    assert elapsed < 2.0, f"TOO SLOW: {elapsed:.2f}s — you're probably O(n*k)"
    print(f"PASS: 100k stress test in {elapsed:.3f}s (O(n) confirmed)")


def test_uses_mydeque_not_list():
    """Meta-check: reading the source of max_sliding_window, you should see
    MyDeque. This test doesn't enforce it but the docstring does."""
    import inspect
    src = inspect.getsource(max_sliding_window)
    assert "MyDeque" in src, \
        "You must USE your MyDeque — the whole point of this exercise"
    assert "collections" not in src, \
        "Don't import collections.deque — use MyDeque"
    print("PASS: solution uses MyDeque (no collections.deque)")


if __name__ == "__main__":
    test_classic_example()
    test_single_element_window()
    test_window_equals_array()
    test_strictly_decreasing()
    test_strictly_increasing()
    test_all_equal()
    test_negative_numbers()
    test_two_elements()
    test_duplicates_with_repeats()
    test_front_eviction_path()
    test_front_eviction_path()
    test_large_stress_on_performance()
    test_uses_mydeque_not_list()
    print("\nAll tests passed ✅  You've solved SWM optimally with your own deque.")
