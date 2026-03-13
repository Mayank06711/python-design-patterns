# DSA Interview Questions - Google, Amazon, Meta (2024-2025)

> Curated from LeetCode company tags, interview reports, and frequency data.
> Focus: Medium-Hard patterns for someone comfortable with basics.

---

## CATEGORY 1: Trees & BST (15 Questions)

| # | Problem | LC # | Difficulty | Pattern It Teaches | Company (Most Frequent) |
|---|---------|------|------------|-------------------|------------------------|
| 1 | Diameter of Binary Tree | 543 | Easy | Post-order DFS, computing height while tracking global max | Amazon, Meta, Google |
| 2 | Lowest Common Ancestor of a Binary Tree | 236 | Medium | Recursive DFS, simultaneous subtree search | Meta, Amazon, Google |
| 3 | Lowest Common Ancestor of a BST | 235 | Medium | BST property exploitation, split-point logic | Meta, Amazon |
| 4 | Validate Binary Search Tree | 98 | Medium | In-order traversal with bounds, range propagation | Amazon, Meta, Google |
| 5 | Binary Tree Maximum Path Sum | 124 | Hard | Post-order DFS, global max tracking, handling negative paths | Google, Amazon, Meta |
| 6 | Serialize and Deserialize Binary Tree | 297 | Hard | Pre-order/level-order encoding, queue-based reconstruction | Meta, Amazon, Google |
| 7 | Binary Tree Right Side View | 199 | Medium | BFS level-order traversal, taking last node per level | Meta, Amazon |
| 8 | Binary Tree Vertical Order Traversal | 314 | Medium | BFS + column indexing with HashMap, coordinate tracking | Meta, Amazon |
| 9 | Vertical Order Traversal of a Binary Tree | 987 | Hard | DFS/BFS + sorting by (col, row, val), coordinate system | Google, Amazon, Meta |
| 10 | Construct Binary Tree from Preorder and Inorder Traversal | 105 | Medium | Divide-and-conquer, index mapping, recursive subtree construction | Amazon, Google, Meta |
| 11 | Binary Tree Cameras | 968 | Hard | Greedy post-order DFS, 3-state system (covered/has-camera/not-covered) | Amazon, Google |
| 12 | Kth Smallest Element in a BST | 230 | Medium | In-order traversal gives sorted order, early termination | Amazon, Meta, Google |
| 13 | Binary Tree Level Order Traversal | 102 | Medium | BFS with queue, level-by-level processing | Amazon, Meta, Google |
| 14 | Flatten Binary Tree to Linked List | 114 | Medium | Reverse post-order or Morris-traversal-style pointer rewiring | Amazon, Meta |
| 15 | Count Good Nodes in Binary Tree | 1448 | Medium | Pre-order DFS with running max passed as parameter | Amazon, Google |

### Key Patterns Summary (Trees & BST):
- **Post-order DFS** (bottom-up): Diameter, Max Path Sum, Binary Tree Cameras
- **Pre-order DFS** (top-down): Serialize, Good Nodes, Validate BST (with bounds)
- **BFS / Level-order**: Right Side View, Vertical Order, Level Order
- **Divide & Conquer**: Construct from traversals
- **BST Property**: Validate BST, Kth Smallest, LCA of BST

---

## CATEGORY 2: Heaps / Priority Queue (8 Questions)

| # | Problem | LC # | Difficulty | Pattern It Teaches | Company (Most Frequent) |
|---|---------|------|------------|-------------------|------------------------|
| 1 | Top K Frequent Elements | 347 | Medium | Min-heap of size K, bucket sort alternative, frequency counting | Amazon, Meta, Google |
| 2 | Kth Largest Element in an Array | 215 | Medium | Min-heap of size K, quickselect alternative, partial sorting | Amazon, Meta, Google |
| 3 | Merge K Sorted Lists | 23 | Hard | Min-heap with K pointers, divide-and-conquer merge | Amazon, Google, Meta |
| 4 | Find Median from Data Stream | 295 | Hard | Two-heap technique (max-heap + min-heap), balanced partition | Amazon, Google, Meta |
| 5 | K Closest Points to Origin | 973 | Medium | Max-heap of size K, distance comparison without sqrt | Amazon, Meta, Google |
| 6 | Reorganize String | 767 | Medium | Max-heap + greedy placement, frequency-based character scheduling | Amazon, Google |
| 7 | Task Scheduler | 621 | Medium | Max-heap + cooldown queue, greedy idle-slot counting | Amazon, Meta, Google |
| 8 | Kth Largest Element in a Stream | 703 | Easy | Min-heap of fixed size K, stream processing pattern | Amazon, Google |

### Key Patterns Summary (Heaps):
- **Top-K pattern** (min-heap of size K): Top K Frequent, Kth Largest, K Closest Points
- **Two-heap (median finding)**: Find Median from Data Stream
- **Merge pattern** (min-heap with K pointers): Merge K Sorted Lists
- **Greedy + Heap scheduling**: Task Scheduler, Reorganize String

---

## CATEGORY 3: Recursion & Backtracking (12 Questions)

> **Progression order matters here.** Organized from intuition-building to advanced.
> If you get stuck, trace the decision tree on paper before coding.

### Phase 1: Build the Backtracking Muscle (Subsets/Permutations/Combinations)

| # | Problem | LC # | Difficulty | Pattern It Teaches | Company (Most Frequent) |
|---|---------|------|------------|-------------------|------------------------|
| 1 | Subsets | 78 | Medium | Include/exclude decision at each index, base case = end of array | Amazon, Meta, Google |
| 2 | Subsets II (with duplicates) | 90 | Medium | Sort + skip duplicates at same level of recursion tree | Amazon, Google |
| 3 | Permutations | 46 | Medium | Swap-based or used-array approach, order matters | Amazon, Meta, Google |
| 4 | Combination Sum | 39 | Medium | Unbounded choice (can reuse), start-index to avoid duplicates | Amazon, Meta, Google |

### Phase 2: Apply the Template to String/Grid Problems

| # | Problem | LC # | Difficulty | Pattern It Teaches | Company (Most Frequent) |
|---|---------|------|------------|-------------------|------------------------|
| 5 | Generate Parentheses | 22 | Medium | Constraint-based branching (open < n, close < open) | Amazon, Meta, Google |
| 6 | Letter Combinations of a Phone Number | 17 | Medium | Multi-way branching per digit, building string incrementally | Amazon, Meta, Google |
| 7 | Palindrome Partitioning | 131 | Medium | Partition point backtracking + palindrome check at each cut | Amazon, Google, Meta |
| 8 | Word Search | 79 | Medium | Grid DFS + visited marking + backtracking (unmark on return) | Amazon, Meta, Google |

### Phase 3: Hard Constraint Satisfaction (the "boss levels")

| # | Problem | LC # | Difficulty | Pattern It Teaches | Company (Most Frequent) |
|---|---------|------|------------|-------------------|------------------------|
| 9 | N-Queens | 51 | Hard | Column + diagonal constraint tracking, row-by-row placement | Amazon, Google, Meta |
| 10 | N-Queens II | 52 | Hard | Same as N-Queens but count-only, bit manipulation optimization | Google, Amazon |
| 11 | Sudoku Solver | 37 | Hard | Cell-by-cell filling, 3-constraint validation (row/col/box) | Amazon, Google |
| 12 | Word Search II | 212 | Hard | Trie + grid backtracking, pruning visited trie branches | Amazon, Google, Meta |

### How to Build Backtracking Intuition (if you get stuck):

```
TEMPLATE:
def backtrack(path, choices):
    if goal_reached(path):
        result.append(path[:])     # 1. Base case: found a valid answer
        return

    for choice in choices:
        if is_valid(choice):       # 2. Pruning: skip invalid choices
            path.append(choice)    # 3. Make the choice
            backtrack(path, next_choices)  # 4. Recurse
            path.pop()             # 5. Undo the choice (BACKTRACK)
```

**Mental model:** Every backtracking problem is a TREE of decisions.
- Each LEVEL = one decision point (which element? which cell? which digit?)
- Each BRANCH = one choice at that decision point
- PRUNING = skipping entire subtrees that cannot lead to valid answers

---

## CATEGORY 4: Greedy (8 Questions)

| # | Problem | LC # | Difficulty | Pattern It Teaches | Company (Most Frequent) |
|---|---------|------|------------|-------------------|------------------------|
| 1 | Jump Game | 55 | Medium | Track farthest reachable index, greedy forward scan | Amazon, Google, Meta |
| 2 | Jump Game II | 45 | Medium | BFS-style greedy (current range / next range), minimum jumps | Amazon, Google |
| 3 | Gas Station | 134 | Medium | Circular array greedy, reset start when tank goes negative | Amazon, Google |
| 4 | Non-overlapping Intervals | 435 | Medium | Sort by end time, count overlaps to remove (interval scheduling) | Amazon, Google, Meta |
| 5 | Meeting Rooms II | 253 | Medium | Min-heap or sweep line, track concurrent meetings | Amazon, Meta, Google |
| 6 | Merge Intervals | 56 | Medium | Sort by start, extend or create new interval | Amazon, Meta, Google |
| 7 | Minimum Number of Platforms (Geeks) / Meeting Rooms variant | -- | Medium | Arrival/departure sorting + sweep line, peak overlap count | Amazon, Google |
| 8 | Activity Selection / Interval Scheduling Maximization | -- | Medium | Sort by end time, greedily pick non-overlapping (classic proof) | Google, Amazon |

> **Note:** Problems 7 and 8 are classic algorithmic problems frequently asked verbally or as variants. Meeting Rooms II (LC 253) and Non-overlapping Intervals (LC 435) cover the same core patterns on LeetCode.

### Key Patterns Summary (Greedy):
- **Interval scheduling**: Sort by end time, greedily select non-overlapping (Problems 4, 6, 7, 8)
- **Reachability / Jump**: Track farthest reachable position (Problems 1, 2)
- **Circular greedy**: Reset and restart strategy (Problem 3)
- **Sweep line / Event processing**: Sort events, track concurrent usage (Problems 5, 7)

### Greedy Proof Checklist (interviewers ask "WHY is greedy correct?"):
1. **Greedy choice property**: Making the locally optimal choice does not prevent finding the globally optimal solution.
2. **Optimal substructure**: After making a greedy choice, the remaining problem has the same structure.
3. **Exchange argument**: Any solution that differs from the greedy solution can be transformed into the greedy solution without worsening it.

---

## CATEGORY 5: Bit Manipulation + Tries (5 Questions)

| # | Problem | LC # | Difficulty | Pattern It Teaches | Company (Most Frequent) |
|---|---------|------|------------|-------------------|------------------------|
| 1 | Single Number | 136 | Easy | XOR cancellation (a ^ a = 0), finding the unique element | Amazon, Google, Meta |
| 2 | Counting Bits | 338 | Easy | DP with bit relation: dp[i] = dp[i >> 1] + (i & 1) | Amazon, Google |
| 3 | Maximum XOR of Two Numbers in an Array | 421 | Medium | Bitwise trie (insert all nums, greedily pick opposite bits) | Google, Amazon |
| 4 | Implement Trie (Prefix Tree) | 208 | Medium | Trie node structure, insert/search/startsWith operations | Amazon, Google, Meta |
| 5 | Word Search II | 212 | Hard | Trie built from word list + grid DFS backtracking, trie pruning | Amazon, Google, Meta |

### Key Patterns Summary (Bit Manipulation + Tries):
- **XOR properties**: a ^ a = 0, a ^ 0 = a, XOR is commutative and associative (Problem 1)
- **Bit DP**: Relating dp[i] to dp[i/2] via last bit (Problem 2)
- **Bitwise Trie**: Store numbers bit-by-bit from MSB, greedily maximize XOR (Problem 3)
- **Standard Trie**: Character-by-character prefix tree for string operations (Problems 4, 5)
- **Trie + Backtracking fusion**: Build trie from dictionary, DFS grid against trie (Problem 5)

> **Note:** Word Search II (LC 212) appears in both Backtracking and Tries because it is the canonical problem that fuses both patterns. Practice it from both angles.

---

## Quick Reference: Total Problem Count

| Category | Count | Easy | Medium | Hard |
|----------|-------|------|--------|------|
| Trees & BST | 15 | 1 | 10 | 4 |
| Heaps / Priority Queue | 8 | 1 | 5 | 2 |
| Recursion & Backtracking | 12 | 0 | 8 | 4 |
| Greedy | 8 | 0 | 8 | 0 |
| Bit Manipulation + Tries | 5 | 2 | 2 | 1 |
| **TOTAL** | **48** | **4** | **33** | **11** |

---

## Suggested Practice Order

1. **Week 1 - Trees & Heaps**: Problems that build DFS/BFS intuition
   - Trees: 1 -> 13 -> 7 -> 2 -> 3 -> 4 -> 12 -> 10 -> 5 -> 6 -> 8 -> 9 -> 14 -> 15 -> 11
   - Heaps: 8 -> 2 -> 1 -> 5 -> 3 -> 6 -> 7 -> 4

2. **Week 2 - Backtracking (progressive)**: Follow the Phase 1 -> 2 -> 3 order above exactly

3. **Week 3 - Greedy + Bits/Tries**: Pattern recognition
   - Greedy: 6 -> 4 -> 5 -> 1 -> 2 -> 3 -> 7 -> 8
   - Bits/Tries: 1 -> 2 -> 4 -> 3 -> 5

---

## Sources

- [Amazon SDE Interview Questions 2024/2025 - LeetCode Wizard](https://leetcodewizard.io/blog/amazon-sde-interview-questions)
- [Google Software Engineer Interview Questions 2024/2025 - LeetCode Wizard](https://leetcodewizard.io/blog/google-software-engineer-interview-questions)
- [Meta's Most Asked 73 LeetCode Problems - Medium](https://medium.com/@johnadjanohoun/metas-most-asked-coding-interview-questions-the-complete-list-of-73-leetcode-problems-47e96767adc7)
- [2024 Google Interview Questions Compilation - LeetCode Discuss](https://leetcode.com/discuss/post/6185127/2024-google-interview-questions-compilat-mjrf/)
- [Top 300 Most-Asked DSA Questions for Amazon SDE-1 (2022-2025) - LeetCode Discuss](https://leetcode.com/discuss/post/7479312/top-300-most-asked-dsa-questions-for-ama-c656/)
- [Most Asked Interview Questions 2025 - LeetCode Discuss](https://leetcode.com/discuss/post/7417074/)
- [Top 100 LeetCode Questions 2025 Edition - Shadecoder](https://www.shadecoder.com/blogs/top-100-leetcode-coding-interview-questions-(2025-edition))
- [50 Greedy Algorithm Interview Questions - IGotAnOffer](https://igotanoffer.com/blogs/tech/greedy-algorithm-interview-questions)
- [47 Backtracking Interview Questions - IGotAnOffer](https://igotanoffer.com/blogs/tech/backtracking-interview-questions)
- [LeetCode Patterns - Sean Prashad](https://seanprashad.com/leetcode-patterns/)
- [Meta LeetCode Interview Questions - InterviewSolver](https://interviewsolver.com/interview-questions/meta)
- [Amazon LeetCode Interview Questions - InterviewSolver](https://www.interviewsolver.com/interview-questions/amazon)
- [15 Core Greedy Patterns - LeetCode Discuss](https://leetcode.com/discuss/post/7344979/15-core-greedy-patterns-for-coding-inter-a1wp/)
- [Google DS & Algo Interview Roadmap 2025 - Medium](https://medium.com/@prashant558908/google-ds-algo-interview-preparation-roadmap-2025-974d15cb10cd)
- [Amazon DS & Algo Interview Roadmap 2025 - Medium](https://medium.com/@prashant558908/amazon-ds-algo-interview-preparation-roadmap-2025-2989470d0c4c)
