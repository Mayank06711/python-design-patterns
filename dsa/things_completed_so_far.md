# DSA Progress Tracker

> Updated after every question completed. Never delete entries -- this is your progress log.

---

## Summary

| Category | Total | Done | Remaining |
|----------|-------|------|-----------|
| Arrays/Two Pointers | 15 | 9 | 6 |
| Binary Search | 10 | 2 | 8 |
| Linked List | 12 | 7 | 5 |
| Stacks/Queues | 10 | 5 | 5 |
| Sorting | 8 | 0 | 8 |
| Trees & BST | 15 | 0 | 15 |
| Heaps | 8 | 0 | 8 |
| Recursion/Backtracking | 12 | 0 | 12 |
| Greedy | 8 | 0 | 8 |
| Dynamic Programming | 30 | 0 | 30 |
| Graphs | 20 | 0 | 20 |
| Bits/Tries | 5 | 0 | 5 |
| **TOTAL** | **153** | **23** | **130** |

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

### Day 9 — Mar 25, 2026

**Revisions:**
- [x] Product of Array Except Self REVISION (LC #238) | Prefix/Suffix | Medium | **10/10** (was 5/10) | ✅ CLEARED | 1st run, 0 hints. Wrote optimal O(n)/O(1) solution from memory. Pattern retained: left product in ans, running r_prod from right. | **Def:** For each index, answer = product of everything left × product of everything right. Build left products forward, multiply right products backward in one pass. O(n) time, O(1) extra space.

### Session 17 — Apr 9 & Apr 11-12, 2026 (split across 3 days due to meetings)

**Stacks/Queues (B2):**
- [x] MyDeque from Scratch | Doubly Linked List | Advanced | **7/10** | 10/10 tests, 4 runs (1 check + 3 failed + 1 pass), ~67 min. Dummy head/tail DLL pattern. Bugs: shift-dummy trick didn't compose with peek/pop; __iter__ off-by-one; __bool__ inversion. Refactored to standard insert-between-A-and-B. | **Def:** Doubly linked list with dummy head + dummy tail sentinels. All advertised O(1) ops guaranteed via direct pointers to both ends.
- [x] Sliding Window Maximum OPTIMAL REVISION (LC #239) | Monotonic Deque | Hard | **7/10** (was 7/10 brute) | ✅ CLEARED | 12/12 tests. 4-step loop: evict dominated (back) → append → evict window (front) → record. Used own MyDeque. Multiple approach bugs flagged pre-coding (wrong order, wrong side, peek vs pop, index vs value). | **Def:** Monotonic deque holds indices of candidates for window max. Back side = dominance eviction. Front side = window eviction + answer. O(n) amortized, O(k) space.
- [x] Next Greater Element I (LC #496) | Monotonic Stack | Easy | **7/10** | 10/10 tests. Stack stores values, dict bridges nums2→next_greater, then lookup from nums1 via dict.get(v, -1). Pre-filled ans=[-1]*n eliminates cleanup. Hints needed for value-stack + dict bridge concept. | **Def:** Monotonic decreasing stack on nums2; when nums2[i] > stack top, pop and record. Build value→next_greater dict. Query nums1 via dict lookup. O(n+m) time/space.
- [x] Next Greater Element II REVISION (LC #503) | Monotonic Stack + Circular | Medium | **9/10** | 10/10 tests, 1st run. Circular twist via 2n loop + i%n. Only push during first pass (i<n). Free hint on circular/rotation concept (user had never been taught). BEST SCORE THIS SESSION. | **Def:** Extend mono stack to circular array by iterating 2*n times with real index = i%n. Push only during first pass; pop during both. O(n) time, O(n) space.

**DSA — Binary Search (Session 17, Track A):**
- [x] Search in Rotated Sorted Array REVISION (LC #33) | Binary Search | Medium | **8/10** (was 4/10) | ✅ CLEARED (from 4/10). 12/12 first run, ~7 min (under 8-min budget). Fresh file (no peeking at original). Session 15 bugs all fixed except 1 latent: right-branch has strict `<` instead of `<=` on boundary check. Correct template: while left<=right, if left-sorted check target in [nums[left], nums[mid]), else check target in (nums[mid], nums[right]]. | **Def:** Rotated array has exactly 1 pivot; one half is always sorted. Check if left-half sorted via nums[left]<=nums[mid]; if target in that half's range, search it, else search other half. O(log n).

**Graph Micro-concept #12:**
- [x] Weighted Graphs | Graph Theory | PASSED | Weighted edges = edges that carry a number (cost/distance/time/price). Store as adjacency list of tuples [(neighbor, weight)]. BFS no longer works for shortest path — need Dijkstra (positive weights) or Bellman-Ford (with negatives). Own example: Music graph — nodes=notes (G,D,A,E), edges=transitions between notes on a string, weight=frequency change in Hz (G=196Hz, D=293Hz, so G↔D edge weight = 97 Hz). Valid weighted graph with unit and meaning. Can be directed (pitch up ≠ pitch down). | **Def:** Weighted graph = edges carry numeric weight representing cost/distance/effort. Store as adjacency list of (neighbor, weight) tuples. Dijkstra for positive-weight shortest path; BFS is insufficient.

