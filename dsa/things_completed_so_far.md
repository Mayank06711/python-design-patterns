# DSA Progress Tracker

> Updated after every question completed. Never delete entries -- this is your progress log.

---

## Summary

| Category | Total | Done | Remaining |
|----------|-------|------|-----------|
| Arrays/Two Pointers | 15 | 2 | 13 |
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
| **TOTAL** | **153** | **2** | **151** |

---

## Day-wise Log

### Day 4 — Mar 17, 2026

**Arrays & Two Pointers:**
- [x] Two Sum II (LC #167) | Two Pointers | Easy | **9/10** | Solved in Python + C++ | Opposite-end two pointers on sorted array. O(n) time, O(1) space. Bug: initial syntax error (`else j -= 1` missing colon), then IndexError (`len` vs `len()-1`). Logic correct from 3rd run. | **Def:** Two pointers on sorted array — left/right converge based on sum comparison with target. Works because sorting guarantees monotonic sum behavior.
- [x] Container With Most Water (LC #11) | Two Pointers | Medium | **10/10** | Solved in Python + C++ | Opposite-end two pointers. Move shorter height pointer because keeping it can only decrease/maintain area. O(n) time, O(1) space. 1 hint (which pointer to move). First-run correct logic. | **Def:** Two pointers on unsorted array — move the shorter side because it's the bottleneck; keeping the taller side gives a chance at bigger area despite shrinking width.

