# DSA Progress Tracker

> Updated after every question completed. Never delete entries -- this is your progress log.

---

## Summary

| Category | Total | Done | Remaining |
|----------|-------|------|-----------|
| Arrays/Two Pointers | 15 | 9 | 6 |
| Binary Search | 10 | 0 | 10 |
| Linked List | 12 | 0 | 12 |
| Stacks/Queues | 10 | 0 | 10 |
| Sorting | 8 | 0 | 8 |
| Trees & BST | 15 | 0 | 15 |
| Heaps | 8 | 0 | 8 |
| Recursion/Backtracking | 12 | 0 | 12 |
| Greedy | 8 | 0 | 8 |
| Dynamic Programming | 30 | 0 | 30 |
| Graphs | 20 | 0 | 20 |
| Bits/Tries | 5 | 0 | 5 |
| **TOTAL** | **153** | **9** | **144** |

---

## Day-wise Log

### Day 4 — Mar 17, 2026

**Arrays & Two Pointers:**
- [x] Two Sum II (LC #167) | Two Pointers | Easy | **9/10** | Solved in Python + C++ | Opposite-end two pointers on sorted array. O(n) time, O(1) space. Bug: initial syntax error (`else j -= 1` missing colon), then IndexError (`len` vs `len()-1`). Logic correct from 3rd run. | **Def:** Two pointers on sorted array — left/right converge based on sum comparison with target. Works because sorting guarantees monotonic sum behavior.
- [x] Container With Most Water (LC #11) | Two Pointers | Medium | **10/10** | Solved in Python + C++ | Opposite-end two pointers. Move shorter height pointer because keeping it can only decrease/maintain area. O(n) time, O(1) space. 1 hint (which pointer to move). First-run correct logic. | **Def:** Two pointers on unsorted array — move the shorter side because it's the bottleneck; keeping the taller side gives a chance at bigger area despite shrinking width.

### Day 5 — Mar 18, 2026

**Arrays & Two Pointers:**
- [x] 3Sum (LC #15) | Two Pointers | Medium | **5/10** | Solved in Python | Fix i, two-pointer j/k on sorted subarray, target = -nums[i]. O(n²) time, O(n) space (hashmap dedup). 4 attempts: Run 1 (2/10) k not reset + abs() logic, Run 2 (1/10) unhashable list in dict, Run 3 (5/10) abs() comparison + if/elif fall-through, Run 4 (10/10). Multiple hints on Python fundamentals (hashable types, dict KeyError) + abs() trap. Approach logic correct from start — all bugs were Python implementation. | **Def:** 3Sum reduces to 2Sum — fix one element, two-pointer the rest. Sort first for O(1) dedup via pointer skipping (optimal) or tuple-in-dict (user's approach). Key: compare total against 0 directly, don't use abs().

### Day 6 — Mar 19, 2026

**Arrays & Two Pointers:**
- [x] Sort Colors / Dutch National Flag (LC #75) | Three Pointers | Medium | **9/10** | Solved in Python | 1st run all 10 tests passed. 3 approaches: (1) bucket sort O(n)/O(n), (2) counting sort O(n)/O(1) two-pass, (3) Dutch National Flag one-pass O(n)/O(1). low/separator/high pointers — zones: before low=0s, after high=2s, between=1s. Key trap: don't advance separator after swapping with high. 1 hint. | **Def:** Dutch National Flag = 3-way partition using low/mid/high pointers. Swap 0s left, swap 2s right, 1s stay in middle. One pass, O(1) space.

### Day 7 — Mar 22, 2026

**Arrays & Two Pointers:**
- [x] Product of Array Except Self (LC #238) | Prefix/Suffix | Medium | **5/10** | Solved in Python | 4+ attempts. Prefix-suffix product + O(1) space optimization.
- [x] Maximum Subarray / Kadane's (LC #53) | Kadane's | Medium | **9/10** | Solved in Python | 1st run pass. Running sum + reset when negative. 1 hint.

### Day 8 — Mar 24, 2026

**Arrays & Two Pointers:**
- [x] Best Time to Buy and Sell Stock (LC #121) | Single Pass / Greedy | Easy | **10/10** | Solved in Python | 1st run pass. Track min_price, compute profit at each step. 0 hints. Same pattern as Kadane's.
- [x] Merge Intervals (LC #56) | Sort + Merge | Medium | **8/10** | Solved in Python | 1st run pass. Sort by start, scan once, compare against last in answer list. 2 hints (missing sort, end should use max). Rewrote from scratch for understanding. | **Def:** Sort intervals by start. Scan left-to-right: if current overlaps last merged (end >= start), extend end with max. Otherwise push new interval. O(n log n).

