# DSA Pattern Reference — Master Index

> **Philosophy:** The PATTERN is the skill. Data structures are just where you apply it.
> Learn the parent problem → every variant is just a tweak.
>
> **How to use this file:**
> 1. New problem? → Scan "Recognition Triggers" to identify pattern
> 2. Studying a pattern? → Solve the **Parent** first, then variants across different DS
> 3. Review? → Use the cross-pattern guide at the bottom
>
> **Sources:** [Striver A2Z](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z) | [Aditya Verma](https://github.com/skjha1/Aditya-verma-youtube-playlist-code) | [NeetCode 150](https://neetcode.io/roadmap) | [16 Patterns](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews) | [Sean Prashad](https://seanprashad.com/leetcode-patterns/) | [14 Patterns Blog](https://leetcode.com/discuss/post/4039411/14-Patterns-to-Ace-Any-Coding-Interview-Question/)
>
> **Learning approach (research-backed):**
> - Pattern-based learning is more efficient than random grinding ([source](https://medium.com/@thita.ai/beyond-leetcode-why-pattern-based-learning-is-the-future-of-dsa-mastery-8837c85b1c06))
> - Interleaving (mixing patterns) beats blocked practice for long-term retention ([MIT research](https://openlearning.mit.edu/mit-faculty/research-based-learning-findings/spaced-and-interleaved-practice))
> - Spaced repetition (revisit after 3-5 days) doubles retention vs cramming ([source](https://www.redgreencode.com/leetcode-tip-10-planning-a-spaced-repetition-schedule/))
> - Best combo: Learn pattern → 5-7 problems in pattern → mix with other patterns → revise

---

## MASTER TREE (32 patterns, ~200 problems)

```
DSA Patterns
│
├── TWO POINTERS (12 problems)
├── SLIDING WINDOW (8 problems)
├── BINARY SEARCH (11 problems)
├── PREFIX SUM / PRODUCT (5 problems)
├── MONOTONIC STACK / QUEUE (8 problems)
├── MERGE INTERVALS (6 problems)
├── CYCLIC SORT (5 problems)
├── IN-PLACE LINKED LIST REVERSAL (6 problems)
├── BFS (9 problems)
├── DFS (9 problems)
├── BACKTRACKING — SUBSETS/PERMS/COMBOS (12 problems)
├── TOPOLOGICAL SORT (5 problems)
├── UNION FIND (6 problems)
├── TWO HEAPS (3 problems)
├── TOP-K ELEMENTS / HEAP (8 problems)
├── K-WAY MERGE (4 problems)
├── KADANE'S / SUBARRAY (4 problems)
├── GREEDY (7 problems)
├── MATRIX TRAVERSAL (5 problems)
├── DIVIDE AND CONQUER (4 problems)
├── BIT MANIPULATION (8 problems)
├── TRIE (5 problems)
├── GRAPH: SHORTEST PATH (4 problems)
├── DP: 0/1 KNAPSACK (8 problems)
├── DP: UNBOUNDED KNAPSACK (6 problems)
├── DP: LCS FAMILY (10 problems)
├── DP: LIS (6 problems)
├── DP: MCM / PARTITION DP (8 problems)
├── DP: GRID / PATH (6 problems)
├── DP: FIBONACCI / LINEAR (7 problems)
├── DP: TREES (5 problems)
└── DP: BITMASK (5 problems)
```

---

## 0. RECOGNITION CHEAT SHEET (read-the-problem → pick-the-DS)

> **Purpose:** When you read a problem, the phrasing should *trigger* the right pattern in under 10 seconds.
> This table maps problem phrases to the pattern + data structure + a one-line WHY.
> Grow this table every session — any time you misrecognize a problem, add the misread → correct mapping here.
>
> For the full pattern body (variants, parent problems, etc.), jump to the section link.

| When the problem says… | Pattern | DS | Why (one line) | Section |
|---|---|---|---|---|
| "sliding window + min/max" / "max in every window of size k" | Monotonic Deque | deque | Dominated elements are dead; keep a decreasing queue so front = max in O(1) | [§5](#5-monotonic-stack--queue-8-problems) |
| "next greater/smaller element" / "days until warmer" | Monotonic Stack | stack | Pop while current beats stack top — each element pushed/popped once → O(n) | [§5](#5-monotonic-stack--queue-8-problems) |
| "top k" / "k-th largest/smallest" / "closest k points" | Top-K Heap | min-heap of size k | Heap top gives the threshold in O(1); kick out loser on overflow → O(n log k) | [§15](#15-top-k-elements--heap-8-problems) |
| "median of a stream" / "running median" | Two Heaps | max-heap + min-heap | Two heap tops ARE the two middle elements; balance sizes → O(log n) insert, O(1) query | [§14](#14-two-heaps-3-problems) |
| "level order" / "BFS on tree or grid" / "shortest path in unweighted graph" | BFS | deque (plain) | Layer-by-layer expansion; FIFO guarantees shortest-first | [§9](#9-bfs-9-problems) |
| "LIFO" / "undo" / "balanced parens" / "nested expression" | Stack | stack | Most-recent-first access = stack's definition | [§5](#5-monotonic-stack--queue-8-problems) |
| "FIFO queue" / "producer-consumer" / "buffering" | Plain Queue | deque | O(1) append + popleft | [§5](#5-monotonic-stack--queue-8-problems) |
| "scheduling by priority" / "job with smallest deadline" / "Dijkstra" | Priority Queue | heap | Always need the min/max of a *changing* set → heap's one job | [§15](#15-top-k-elements--heap-8-problems) |
| "merge k sorted lists/streams" | K-Way Merge | min-heap of k heads | Heap picks the smallest head across all k lists in O(log k) | [§16](#16-k-way-merge-4-problems) |
| "subarray/substring of fixed/variable size" + "sum/count/distinct" | Sliding Window | two pointers | Window slides, state updates incrementally — avoids recomputation | [§2](#2-sliding-window-8-problems) |
| "find a pair in sorted array" / "3Sum" / "container with most water" | Two Pointers | two pointers | Sorted order lets you decide which pointer to move → O(n) | [§1](#1-two-pointers-12-problems) |
| "cycle in linked list" / "middle of LL" / "palindrome LL" | Fast/Slow Pointers | two pointers | Speed differential collapses O(n²) traversal to O(n) | [§1](#1-two-pointers-12-problems) |
| "reverse linked list" / "reverse in groups of k" | In-Place LL Reversal | pointers | Flip `next` with 3 local variables; no extra memory | [§8](#8-in-place-linked-list-reversal-6-problems) |
| "search in sorted / rotated / monotonic" | Binary Search | — | Halve the search space each step → O(log n) | [§3](#3-binary-search-11-problems) |
| "minimize max / maximize min such that condition holds" | Binary Search on Answer | — | Monotonic predicate on answer space → binary search the answer itself | [§3](#3-binary-search-11-problems) |
| "range sum" / "range XOR" / "count subarrays with sum K" | Prefix Sum + Hashmap | array + dict | Precompute cumulative → range query in O(1); hashmap counts complements | [§4](#4-prefix-sum--product-5-problems) |
| "intervals overlap / merge / insert" | Merge Intervals | sort + sweep | Sort by start; sweep with running end → greedy merge | [§6](#6-merge-intervals-6-problems) |
| "missing / duplicate in 1..n" | Cyclic Sort | array swap | Index is the key — put `nums[i]` at position `nums[i]-1` in O(n) | [§7](#7-cyclic-sort-5-problems) |
| "all paths" / "connected components" / "tree traversal with state" | DFS | recursion/stack | Go deep, backtrack on dead ends — natural for trees and exhaustive exploration | [§10](#10-dfs-9-problems) |
| "generate all subsets/permutations/combinations" | Backtracking | recursion | Choose → recurse → un-choose; explores the decision tree | [§11](#11-backtracking--subsetspermscombos-12-problems) |
| "task/course ordering with dependencies" / "schedule with prerequisites" | Topological Sort | graph + queue | DAG + in-degree queue processes nodes only after all prereqs done | [§12](#12-topological-sort-5-problems) |
| "friend circles" / "accounts merge" / "group dynamically" | Union Find | DSU | Near-O(1) union + find with path compression + rank | [§13](#13-union-find-6-problems) |
| "max subarray sum" / "best time to buy/sell (one txn)" | Kadane's | running sum | Reset when running sum goes negative — greedy O(n) | [§17](#17-kadanes--subarray-4-problems) |
| "choose items with limit (weight/cost) to max value" | 0/1 Knapsack DP | 2D dp | Each item: take or skip — classic decision DP | [§24](#24-dp-01-knapsack-8-problems) |
| "unlimited copies of each item (coin change)" | Unbounded Knapsack DP | 1D dp | Same decision but item stays available → 1D roll | [§25](#25-dp-unbounded-knapsack-6-problems) |
| "longest common / edit distance / regex match" | LCS Family DP | 2D dp | Compare `s1[i]` vs `s2[j]` — match or not → 2D grid | [§26](#26-dp-lcs-family-10-problems) |
| "longest increasing subseq" / "Russian doll envelopes" | LIS DP | 1D dp / patience | O(n²) DP or O(n log n) patience sorting | [§27](#27-dp-lis-6-problems) |
| "shortest path weighted" / "single source shortest" | Dijkstra | min-heap + graph | Greedy relax — works on non-negative weights | [§23](#23-graph-shortest-path-4-problems) |

**Recognition drill (self-test):** Cover the "Pattern" column, read the trigger, say the pattern out loud. If you miss one, add a note in the Why column until it sticks.

---

## 1. TWO POINTERS (12 problems)

> **Recognition:** Sorted array/list + find pair/triplet. OR linked list + cycle/middle/kth.
> **Core Idea:** Two references traverse structure, reducing O(n²) → O(n).
> **Edge Cases:** Empty input, all same elements, even vs odd length, duplicate skipping.

**Parent:** [Two Sum II #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — simplest opposite-direction two-pointer.

### On Arrays
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Two Sum II (sorted)** | [LC #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Easy | **PARENT** — sum too small → left++, too big → right-- |
| 3Sum | [LC #15](https://leetcode.com/problems/3sum/) | Medium | Fix one, two-pointer on rest. Skip duplicates |
| Container With Most Water | [LC #11](https://leetcode.com/problems/container-with-most-water/) | Medium | Move shorter wall inward |
| Trapping Rain Water | [LC #42](https://leetcode.com/problems/trapping-rain-water/) | Hard | Process shorter side; taller guarantees bottleneck |
| Sort Colors (Dutch Flag) | [LC #75](https://leetcode.com/problems/sort-colors/) | Medium | 3 pointers: low/mid/high partition |
| Remove Duplicates from Sorted | [LC #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | Slow=write, fast=read |
| Merge Sorted Array | [LC #88](https://leetcode.com/problems/merge-sorted-array/) | Easy | Fill from end to avoid overwriting |

### On Linked Lists
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Linked List Cycle | [LC #141](https://leetcode.com/problems/linked-list-cycle/) | Easy | Floyd's: fast=2x, slow=1x |
| Linked List Cycle II | [LC #142](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | After meeting, reset to head, both speed 1 |
| Middle of Linked List | [LC #876](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | Fast at end → slow at middle |
| Remove Nth From End | [LC #19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Create gap of N, walk together |
| Palindrome Linked List | [LC #234](https://leetcode.com/problems/palindrome-linked-list/) | Easy | Find middle → reverse half → compare |

---

## 2. SLIDING WINDOW (8 problems)

> **Recognition:** "subarray/substring of size K" OR "longest/shortest subarray with condition"
> **Core Idea:** Maintain window over contiguous elements, slide to avoid recomputation.
> **Edge Cases:** Window > array, all same elements, empty string.
> **TRAP:** [Subarray Sum = K (#560)](https://leetcode.com/problems/subarray-sum-equals-k/) looks like sliding window but ISN'T — negatives break monotonicity. Use prefix sum + hashmap.

**Parent:** Max Sum Subarray of Size K — simplest fixed window.

### On Arrays (Fixed Window)
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Max Sum Subarray Size K** | [GFG](https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/) | Easy | **PARENT** — add incoming, subtract outgoing |
| Sliding Window Maximum | [LC #239](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Monotonic deque maintains decreasing candidates |
| Permutation in String | [LC #567](https://leetcode.com/problems/permutation-in-string/) | Medium | Fixed window len(s1), check char frequency |

### On Strings (Variable Window)
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Longest Substring Without Repeating | [LC #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Expand right, shrink on duplicate (set/map) |
| Minimum Window Substring | [LC #76](https://leetcode.com/problems/minimum-window-substring/) | Hard | Expand to include all chars, shrink to minimize |
| Longest Repeating Char Replacement | [LC #424](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Valid if `window - max_freq <= k` |

### On Arrays (Variable Window)
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Fruit Into Baskets | [LC #904](https://leetcode.com/problems/fruit-into-baskets/) | Medium | Longest subarray with ≤2 distinct |
| Max Consecutive Ones III | [LC #1004](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | Longest subarray with ≤k zeros |

---

## 3. BINARY SEARCH (11 problems)

> **Recognition:** Sorted data + find element. OR "minimize max" / "maximize min" / "find minimum K such that..."
> **Core Idea:** Halve search space. Works on ANY monotonic function.
> **Edge Cases:** Overflow (`left + (right-left)//2`), `<=` vs `<` in while, off-by-one in answer space, duplicates in rotated.

**Parent:** [Binary Search #704](https://leetcode.com/problems/binary-search/) — everything else modifies the condition.

### On Sorted Array
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Binary Search** | [LC #704](https://leetcode.com/problems/binary-search/) | Easy | **PARENT** — `mid = left + (right-left)//2` |
| Search Insert Position | [LC #35](https://leetcode.com/problems/search-insert-position/) | Easy | Not found → `left` is insert position |
| Find First and Last Position | [LC #34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | Two BS: leftmost + rightmost |

### On Rotated / Modified Array
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Search Rotated Sorted Array | [LC #33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Identify sorted half, check if target in it |
| Find Min in Rotated Sorted | [LC #153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Compare mid with right |
| Find Peak Element | [LC #162](https://leetcode.com/problems/find-peak-element/) | Medium | mid < mid+1 → peak is right |

### On Answer Space (BS on the answer, not an array)
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Koko Eating Bananas | [LC #875](https://leetcode.com/problems/koko-eating-bananas/) | Medium | BS on speed [1, max(piles)] |
| Capacity to Ship Packages | [LC #1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | BS on capacity [max(w), sum(w)] |
| Split Array Largest Sum | [LC #410](https://leetcode.com/problems/split-array-largest-sum/) | Hard | BS on max sum [max(arr), sum(arr)] |

### On Matrix
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Search 2D Matrix | [LC #74](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | 2D as 1D: `row=mid//cols, col=mid%cols` |

### Advanced
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Median of Two Sorted Arrays | [LC #4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | BS on partition in smaller array |

---

## 4. PREFIX SUM / PRODUCT (5 problems)

> **Recognition:** "sum of subarray i to j" or "number of subarrays with sum = K"
> **Core Idea:** Precompute cumulative sum → range queries in O(1).
> **Edge Cases:** Negatives (don't confuse with sliding window), zeros in product, overflow.

**Parent:** [Range Sum Query #303](https://leetcode.com/problems/range-sum-query-immutable/) — `sum(i,j) = prefix[j+1] - prefix[i]`

### On Arrays
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Range Sum Query** | [LC #303](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | **PARENT** |
| Subarray Sum Equals K | [LC #560](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | prefix_sum + hashmap: `count[prefix - k]` |
| Product Except Self | [LC #238](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Left prefix × right prefix |
| Contiguous Array (0s/1s) | [LC #525](https://leetcode.com/problems/contiguous-array/) | Medium | Treat 0 as -1, prefix sum |
| Running Sum of 1D Array | [LC #1480](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | Direct prefix sum |

---

## 5. MONOTONIC STACK / QUEUE (8 problems)

> **Recognition:** "next greater/smaller element" / "histogram" / "stock span" / "days until warmer"
> **Core Idea:** Stack maintains increasing/decreasing order. Popped elements get their answer.
> **Rules:** Decreasing stack → Next Greater. Increasing stack → Next Smaller.
> **Edge Cases:** Empty stack, circular arrays (double or modulo), equal elements.

**Parent:** [Next Greater Element I #496](https://leetcode.com/problems/next-greater-element-i/) — basic decreasing stack.

### On Arrays
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Next Greater Element I** | [LC #496](https://leetcode.com/problems/next-greater-element-i/) | Easy | **PARENT** — pop when current > top |
| Next Greater Element II (circular) | [LC #503](https://leetcode.com/problems/next-greater-element-ii/) | Medium | Loop twice (i % n) |
| Daily Temperatures | [LC #739](https://leetcode.com/problems/daily-temperatures/) | Medium | Store indices; ans[top] = i - top |
| Online Stock Span | [LC #901](https://leetcode.com/problems/online-stock-span/) | Medium | Count consecutive ≤ today |

### On Arrays (Histogram/Area)
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Largest Rectangle in Histogram | [LC #84](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Increasing stack; find left/right boundaries |
| Maximal Rectangle | [LC #85](https://leetcode.com/problems/maximal-rectangle/) | Hard | Row-by-row histogram + LC #84 |
| Trapping Rain Water (stack) | [LC #42](https://leetcode.com/problems/trapping-rain-water/) | Hard | Alternative to two-pointer |

### On Arrays (Monotonic Deque)
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Sliding Window Maximum | [LC #239](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Deque: front = max of window |

---

## 6. MERGE INTERVALS (6 problems)

> **Recognition:** "overlapping intervals" / "merge" / "meeting rooms"
> **Core Idea:** Sort by start, merge if overlap.
> **Edge Cases:** Adjacent [1,2]+[2,3], single interval, all overlapping.

**Parent:** [Merge Intervals #56](https://leetcode.com/problems/merge-intervals/)

### On Intervals
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Merge Intervals** | [LC #56](https://leetcode.com/problems/merge-intervals/) | Medium | **PARENT** — sort by start, merge if start ≤ prev.end |
| Insert Interval | [LC #57](https://leetcode.com/problems/insert-interval/) | Medium | Find overlap, merge, keep rest |
| Non-Overlapping Intervals | [LC #435](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Greedy: count removals |
| Meeting Rooms | [LC #252](https://leetcode.com/problems/meeting-rooms/) | Easy | Sort, check overlap |
| Meeting Rooms II | [LC #253](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Min heap of end times |
| Interval List Intersections | [LC #986](https://leetcode.com/problems/interval-list-intersections/) | Medium | Two pointers on two sorted lists |

---

## 7. CYCLIC SORT (5 problems)

> **Recognition:** "find missing/duplicate in range 1 to n"
> **Core Idea:** Place each number at index = value.
> **Edge Cases:** Numbers outside [1,n], multiple duplicates.

**Parent:** [Missing Number #268](https://leetcode.com/problems/missing-number/)

### On Arrays (range 1 to n)
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Missing Number** | [LC #268](https://leetcode.com/problems/missing-number/) | Easy | **PARENT** |
| Find All Duplicates | [LC #442](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Medium | Negate to mark visited |
| Find All Missing Numbers | [LC #448](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Easy | Place, scan mismatches |
| First Missing Positive | [LC #41](https://leetcode.com/problems/first-missing-positive/) | Hard | Cyclic sort [1,n], ignore out-of-range |
| Set Mismatch | [LC #645](https://leetcode.com/problems/set-mismatch/) | Easy | Find duplicate + missing |

---

## 8. IN-PLACE LINKED LIST REVERSAL (6 problems)

> **Recognition:** "reverse linked list" / "reverse between m and n" / "reverse in K-groups"
> **Core Idea:** prev/curr/next pointer swapping without extra memory.
> **Edge Cases:** Single node, K > length, even vs odd for palindrome.

**Parent:** [Reverse Linked List #206](https://leetcode.com/problems/reverse-linked-list/)

### On Linked Lists
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Reverse Linked List** | [LC #206](https://leetcode.com/problems/reverse-linked-list/) | Easy | **PARENT** — prev=None, swap next |
| Reverse LL II (m to n) | [LC #92](https://leetcode.com/problems/reverse-linked-list-ii/) | Medium | Navigate to m, reverse n-m+1, reconnect |
| Reverse Nodes in K-Group | [LC #25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | Reverse K at a time |
| Swap Nodes in Pairs | [LC #24](https://leetcode.com/problems/swap-nodes-in-pairs/) | Medium | K=2 special case |
| Palindrome Linked List | [LC #234](https://leetcode.com/problems/palindrome-linked-list/) | Easy | Middle → reverse half → compare |
| Reorder List | [LC #143](https://leetcode.com/problems/reorder-list/) | Medium | Middle → reverse half → interleave |

---

## 9. BFS (9 problems)

> **Recognition:** "shortest path" / "minimum steps" / "level order" / "nearest" / "spreading"
> **Core Idea:** Queue-based, level by level. Guarantees shortest in unweighted graphs.
> **Edge Cases:** Disconnected components, cycles (MUST track visited), empty graph.

**Parent:** [Binary Tree Level Order #102](https://leetcode.com/problems/binary-tree-level-order-traversal/)

### On Trees
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **BT Level Order Traversal** | [LC #102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | **PARENT** — queue + level size |
| BT Zigzag Level Order | [LC #103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | Medium | Alternate direction per level |
| Min Depth of Binary Tree | [LC #111](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Easy | BFS finds min depth faster than DFS |

### On Matrix
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Rotting Oranges | [LC #994](https://leetcode.com/problems/rotting-oranges/) | Medium | Multi-source BFS from ALL rotten |
| 01 Matrix | [LC #542](https://leetcode.com/problems/01-matrix/) | Medium | Multi-source BFS from all 0s |
| Number of Islands | [LC #200](https://leetcode.com/problems/number-of-islands/) | Medium | BFS from each '1', mark visited |
| Shortest Path Binary Matrix | [LC #1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | BFS, 8 directions |

### On Graphs
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Word Ladder | [LC #127](https://leetcode.com/problems/word-ladder/) | Hard | Each word = node, 1-char diff = edge |
| Open the Lock | [LC #752](https://leetcode.com/problems/open-the-lock/) | Medium | Each combo = node, 8 neighbors |

---

## 10. DFS (9 problems)

> **Recognition:** "all paths" / "detect cycle" / "connected components" / "tree traversal"
> **Core Idea:** Go deep, backtrack. Stack or recursion.
> **Edge Cases:** Stack overflow (deep recursion), cycles (3-state visited for directed), null tree.

**Parent:** [Max Depth of Binary Tree #104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### On Trees
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Max Depth of Binary Tree** | [LC #104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | **PARENT** — `1 + max(left, right)` |
| Binary Tree Inorder | [LC #94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | Left → Root → Right |
| Path Sum | [LC #112](https://leetcode.com/problems/path-sum/) | Easy | Subtract, check leaf = 0 |
| Path Sum II | [LC #113](https://leetcode.com/problems/path-sum-ii/) | Medium | Track path, backtrack |

### On Matrix
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Number of Islands | [LC #200](https://leetcode.com/problems/number-of-islands/) | Medium | DFS from each '1' |
| Surrounded Regions | [LC #130](https://leetcode.com/problems/surrounded-regions/) | Medium | DFS from borders first |

### On Graphs
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Clone Graph | [LC #133](https://leetcode.com/problems/clone-graph/) | Medium | DFS + hashmap (old→new) |
| Course Schedule (cycle) | [LC #207](https://leetcode.com/problems/course-schedule/) | Medium | 3-state: unvisited/in-progress/done |
| All Paths Source to Target | [LC #797](https://leetcode.com/problems/all-paths-from-source-to-target/) | Medium | DFS + backtrack (DAG, no visited) |

---

## 11. BACKTRACKING (12 problems)

> **Recognition:** "all possible" / "generate all" / "subsets" / "permutations" / "combinations"
> **3 Core Templates:** Subsets (2^n), Permutations (n!), Combinations (n choose k).
> **Edge Cases:** Duplicates → sort + skip at same level. Empty input → [[]].

**Parent:** [Subsets #78](https://leetcode.com/problems/subsets/) — include/exclude each element.

### Subsets Family
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Subsets** | [LC #78](https://leetcode.com/problems/subsets/) | Medium | **PARENT** — include/exclude |
| Subsets II (with dups) | [LC #90](https://leetcode.com/problems/subsets-ii/) | Medium | Sort + skip duplicates |

### Permutations Family
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Permutations | [LC #46](https://leetcode.com/problems/permutations/) | Medium | Track used elements |
| Permutations II (with dups) | [LC #47](https://leetcode.com/problems/permutations-ii/) | Medium | Sort + skip same at same position |

### Combinations Family
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Combinations | [LC #77](https://leetcode.com/problems/combinations/) | Medium | Start index prevents revisit |
| Combination Sum (reuse) | [LC #39](https://leetcode.com/problems/combination-sum/) | Medium | Can reuse → don't increment start |
| Combination Sum II (no reuse) | [LC #40](https://leetcode.com/problems/combination-sum-ii/) | Medium | Sort + skip dups |
| Letter Combos of Phone | [LC #17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | Map digits → letters |

### Constraint Satisfaction
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Palindrome Partitioning | [LC #131](https://leetcode.com/problems/palindrome-partitioning/) | Medium | Check palindrome at each cut |
| N-Queens | [LC #51](https://leetcode.com/problems/n-queens/) | Hard | Track cols, diagonals |
| Word Search | [LC #79](https://leetcode.com/problems/word-search/) | Medium | Matrix DFS + backtrack |
| Generate Parentheses | [LC #22](https://leetcode.com/problems/generate-parentheses/) | Medium | open < n, close < open |

---

## 12. TOPOLOGICAL SORT (5 problems)

> **Recognition:** "ordering with prerequisites" / "dependency" / "task scheduling"
> **Core Idea:** Linear ordering where u→v means u before v. DAGs only.
> **Edge Cases:** Cycle → impossible. Disconnected. Multiple valid orderings.

**Parent:** [Course Schedule #207](https://leetcode.com/problems/course-schedule/)

### On Graphs
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Course Schedule** | [LC #207](https://leetcode.com/problems/course-schedule/) | Medium | **PARENT** — cycle detection |
| Course Schedule II | [LC #210](https://leetcode.com/problems/course-schedule-ii/) | Medium | Return actual order |
| Alien Dictionary | [LC #269](https://leetcode.com/problems/alien-dictionary/) | Hard | Build graph from word order |
| Minimum Height Trees | [LC #310](https://leetcode.com/problems/minimum-height-trees/) | Medium | Remove leaves layer by layer |
| Parallel Courses | [LC #1136](https://leetcode.com/problems/parallel-courses/) | Medium | BFS levels = min semesters |

---

## 13. UNION FIND (6 problems)

> **Recognition:** "connected components" / "redundant connection" / "are nodes connected?"
> **Core Idea:** find(x) + union(x,y). Path compression + rank = near O(1).
> **Edge Cases:** Self-loops, already connected, multiple components.

**Parent:** [Number of Connected Components #323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

### On Graphs
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Connected Components** | [LC #323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Medium | **PARENT** |
| Redundant Connection | [LC #684](https://leetcode.com/problems/redundant-connection/) | Medium | If already connected = redundant |
| Graph Valid Tree | [LC #261](https://leetcode.com/problems/graph-valid-tree/) | Medium | n-1 edges + all connected |
| Accounts Merge | [LC #721](https://leetcode.com/problems/accounts-merge/) | Medium | Union emails of same person |
| Number of Islands (alt) | [LC #200](https://leetcode.com/problems/number-of-islands/) | Medium | Union adjacent land |
| Longest Consecutive Sequence | [LC #128](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Union consecutive nums |

---

## 14. TWO HEAPS (3 problems)

> **Recognition:** "find median" / "split into two parts needing min of one, max of other"
> **Core Idea:** Max-heap (lower half) + min-heap (upper half).

**Parent:** [Find Median from Data Stream #295](https://leetcode.com/problems/find-median-from-data-stream/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Find Median from Data Stream** | [LC #295](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | **PARENT** |
| Sliding Window Median | [LC #480](https://leetcode.com/problems/sliding-window-median/) | Hard | Two heaps + lazy deletion |
| IPO | [LC #502](https://leetcode.com/problems/ipo/) | Hard | Max-heap profits, min-heap capitals |

---

## 15. TOP-K / HEAP (8 problems)

> **Recognition:** "top K" / "K largest" / "K most frequent" / "K closest"
> **Core Idea:** Heap of size K for efficient extraction.
> **Edge Cases:** K=0, K > length, all same. Python heapq is min-heap → negate for max.

**Parent:** [Kth Largest Element #215](https://leetcode.com/problems/kth-largest-element-in-an-array/)

### On Arrays
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Kth Largest Element** | [LC #215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | **PARENT** — min-heap of K |
| Top K Frequent Elements | [LC #347](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Heap by frequency |
| K Closest Points to Origin | [LC #973](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Max-heap of K smallest |
| Reorganize String | [LC #767](https://leetcode.com/problems/reorganize-string/) | Medium | Always place most frequent first |

### On Sorted Structures
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Merge K Sorted Lists | [LC #23](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Min-heap of heads |
| Kth Smallest in Sorted Matrix | [LC #378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Medium | Min-heap, expand right |
| Find K Pairs Smallest Sum | [LC #373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Medium | Min-heap expansion |
| Sort Characters by Frequency | [LC #451](https://leetcode.com/problems/sort-characters-by-frequency/) | Medium | Max-heap all (freq, char) |

---

## 16. K-WAY MERGE (4 problems)

> **Recognition:** "merge K sorted" / "smallest range from K lists"

**Parent:** [Merge K Sorted Lists #23](https://leetcode.com/problems/merge-k-sorted-lists/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Merge K Sorted Lists** | [LC #23](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | **PARENT** |
| Kth Smallest in Sorted Matrix | [LC #378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Medium | Rows as sorted lists |
| Smallest Range Covering K Lists | [LC #632](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Hard | Track max while heap gives min |
| Merge Sorted Array | [LC #88](https://leetcode.com/problems/merge-sorted-array/) | Easy | K=2, fill from end |

---

## 17. KADANE'S / SUBARRAY (4 problems)

> **Recognition:** "maximum/minimum subarray sum/product" / "contiguous subarray"
> **Core Idea:** At each position: extend previous or start fresh.
> **Edge Cases:** All negatives, zeros in product, circular.

**Parent:** [Maximum Subarray #53](https://leetcode.com/problems/maximum-subarray/)

### On Arrays
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Maximum Subarray** | [LC #53](https://leetcode.com/problems/maximum-subarray/) | Medium | **PARENT** — `max(nums[i], curr+nums[i])` |
| Maximum Product Subarray | [LC #152](https://leetcode.com/problems/maximum-product-subarray/) | Medium | Track BOTH max AND min |
| Max Sum Circular Subarray | [LC #918](https://leetcode.com/problems/maximum-sum-circular-subarray/) | Medium | `max(kadane, total - min_subarray)` |
| Longest Turbulent Subarray | [LC #978](https://leetcode.com/problems/longest-turbulent-subarray/) | Medium | Two counters: inc/dec |

---

## 18. GREEDY (7 problems)

> **Recognition:** "minimum number of" / scheduling / "can you reach?"
> **Core Idea:** Local optimal → global optimal. Must prove correctness.
> **Edge Cases:** Greedy doesn't always work — must prove exchange argument.

**Parent:** [Jump Game #55](https://leetcode.com/problems/jump-game/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Jump Game** | [LC #55](https://leetcode.com/problems/jump-game/) | Medium | **PARENT** — track farthest reachable |
| Jump Game II | [LC #45](https://leetcode.com/problems/jump-game-ii/) | Medium | BFS-like range tracking |
| Gas Station | [LC #134](https://leetcode.com/problems/gas-station/) | Medium | If total ≥ 0, start where cumulative resets |
| Task Scheduler | [LC #621](https://leetcode.com/problems/task-scheduler/) | Medium | Most frequent determines gaps |
| Non-Overlapping Intervals | [LC #435](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Sort by end, keep earliest |
| Partition Labels | [LC #763](https://leetcode.com/problems/partition-labels/) | Medium | Track last occurrence |
| Assign Cookies | [LC #455](https://leetcode.com/problems/assign-cookies/) | Easy | Sort both, match smallest |

---

## 19. MATRIX TRAVERSAL (5 problems)

> **Recognition:** "spiral order" / "rotate matrix" / "set zeroes" / "diagonal"
> **Edge Cases:** Non-square (m≠n), 1x1, rotate only for square.

**Parent:** [Spiral Matrix #54](https://leetcode.com/problems/spiral-matrix/)

### On 2D Arrays
| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Spiral Matrix** | [LC #54](https://leetcode.com/problems/spiral-matrix/) | Medium | **PARENT** — 4 boundaries shrink |
| Rotate Image | [LC #48](https://leetcode.com/problems/rotate-image/) | Medium | Transpose + reverse rows |
| Set Matrix Zeroes | [LC #73](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | First row/col as markers |
| Diagonal Traverse | [LC #498](https://leetcode.com/problems/diagonal-traverse/) | Medium | Alternate up-right / down-left |
| Reshape Matrix | [LC #566](https://leetcode.com/problems/reshape-the-matrix/) | Easy | Index math: `old[i//c][i%c]` |

---

## 20. BIT MANIPULATION (8 problems)

> **Recognition:** "single number" / "power of 2" / "counting bits" / "without +/-"
> **Key tricks:** `n & (n-1)` removes lowest set bit. XOR: pairs cancel.

**Parent:** [Single Number #136](https://leetcode.com/problems/single-number/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Single Number** | [LC #136](https://leetcode.com/problems/single-number/) | Easy | **PARENT** — XOR all |
| Single Number II | [LC #137](https://leetcode.com/problems/single-number-ii/) | Medium | Count bits mod 3 |
| Number of 1 Bits | [LC #191](https://leetcode.com/problems/number-of-1-bits/) | Easy | `n & (n-1)` loop |
| Counting Bits | [LC #338](https://leetcode.com/problems/counting-bits/) | Easy | `dp[i] = dp[i>>1] + (i&1)` |
| Missing Number | [LC #268](https://leetcode.com/problems/missing-number/) | Easy | XOR indices + values |
| Reverse Bits | [LC #190](https://leetcode.com/problems/reverse-bits/) | Easy | Shift and build |
| Power of Two | [LC #231](https://leetcode.com/problems/power-of-two/) | Easy | `n > 0 and n & (n-1) == 0` |
| Sum Without +/- | [LC #371](https://leetcode.com/problems/sum-of-two-integers/) | Medium | XOR + AND shift |

---

## 21. TRIE (5 problems)

> **Recognition:** "prefix search" / "autocomplete" / "word dictionary with wildcards"
> **Core Idea:** Tree where each path = string prefix. O(L) insert/search.

**Parent:** [Implement Trie #208](https://leetcode.com/problems/implement-trie-prefix-tree/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Implement Trie** | [LC #208](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | **PARENT** |
| Word Search II | [LC #212](https://leetcode.com/problems/word-search-ii/) | Hard | Trie + board backtracking |
| Add and Search Words | [LC #211](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Trie + DFS for '.' wildcards |
| Replace Words | [LC #648](https://leetcode.com/problems/replace-words/) | Medium | Trie of roots |
| Longest Word in Dictionary | [LC #720](https://leetcode.com/problems/longest-word-in-dictionary/) | Medium | BFS through trie |

---

## 22. GRAPH: SHORTEST PATH (4 problems)

> **Recognition:** "shortest/cheapest path" in WEIGHTED graph
> **Choose:** BFS (unweighted) → Dijkstra (non-negative) → Bellman-Ford (negative) → Floyd-Warshall (all-pairs)

**Parent:** [Network Delay Time #743](https://leetcode.com/problems/network-delay-time/) — classic Dijkstra

| Problem | Link | Difficulty | Algorithm |
|---------|------|-----------|-----------|
| **Network Delay Time** | [LC #743](https://leetcode.com/problems/network-delay-time/) | Medium | **PARENT** — Dijkstra |
| Cheapest Flights K Stops | [LC #787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Bellman-Ford (K iterations) |
| Path With Min Effort | [LC #1631](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | Dijkstra (weight = max diff) |
| Swim in Rising Water | [LC #778](https://leetcode.com/problems/swim-in-rising-water/) | Hard | Dijkstra or BS + BFS |

---

## DP PATTERNS (Aditya Verma Framework)

> **Aditya Verma's key insight:** Every DP pattern has ONE parent problem.
> All variants just change what "weight", "value", or "capacity" means.

---

## 23. DP: 0/1 KNAPSACK FAMILY (8 problems)

> **Recognition:** "choose/don't choose" each item + capacity constraint. No repetition.
> **Template:** `dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w-wt[i]])`
> **Edge Cases:** Total sum odd → partition impossible. All zeros. Space opt: 1D, iterate W backwards.

**Parent:** 0/1 Knapsack — [GFG](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)

| Problem | Link | Difficulty | How it maps to Knapsack |
|---------|------|-----------|------------------------|
| **0/1 Knapsack** | [GFG](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/) | Medium | **PARENT** |
| Subset Sum | [GFG](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/) | Medium | val=wt, target=W |
| Equal Sum Partition | [LC #416](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | target = totalSum/2 |
| Count Subsets with Given Sum | [GFG](https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/) | Medium | Count instead of max |
| Min Subset Sum Difference | [GFG](https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/) | Hard | Minimize \|S1-S2\| |
| Target Sum | [LC #494](https://leetcode.com/problems/target-sum/) | Medium | count(sum = (target+total)/2) |
| Last Stone Weight II | [LC #1049](https://leetcode.com/problems/last-stone-weight-ii/) | Medium | Same as min subset diff |
| Ones and Zeroes | [LC #474](https://leetcode.com/problems/ones-and-zeroes/) | Medium | 2D knapsack (0s, 1s) |

---

## 24. DP: UNBOUNDED KNAPSACK (6 problems)

> **Recognition:** "unlimited supply" / "can reuse" / "coin change" / "rod cutting"
> **Key diff from 0/1:** Include → stay at same item: `dp[i][w-wt[i]]` not `dp[i-1][...]`
> **Edge Cases:** Amount=0 → 1 way or 0 coins. No combo → -1.

**Parent:** Unbounded Knapsack — [GFG](https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Unbounded Knapsack** | [GFG](https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/) | Medium | **PARENT** |
| Rod Cutting | [GFG](https://www.geeksforgeeks.org/cutting-a-rod-dp-13/) | Medium | lengths=weights, prices=values |
| Coin Change (min coins) | [LC #322](https://leetcode.com/problems/coin-change/) | Medium | Minimize count |
| Coin Change II (num ways) | [LC #518](https://leetcode.com/problems/coin-change-ii/) | Medium | Count combinations |
| Perfect Squares | [LC #279](https://leetcode.com/problems/perfect-squares/) | Medium | Squares are "coins" |
| Integer Break | [LC #343](https://leetcode.com/problems/integer-break/) | Medium | Maximize product of parts |

---

## 25. DP: LCS FAMILY (10 problems)

> **Recognition:** Two strings/sequences + "common" / "convert" / "palindrome subsequence"
> **Template:** match → `1 + dp[i-1][j-1]`, no match → `max(dp[i-1][j], dp[i][j-1])`
> **Edge Cases:** Empty strings, identical strings, case sensitivity.

**Parent:** [Longest Common Subsequence #1143](https://leetcode.com/problems/longest-common-subsequence/)

| Problem | Link | Difficulty | How it reduces to LCS |
|---------|------|-----------|----------------------|
| **Longest Common Subsequence** | [LC #1143](https://leetcode.com/problems/longest-common-subsequence/) | Medium | **PARENT** |
| Longest Common Substring | [GFG](https://www.geeksforgeeks.org/longest-common-substring-dp-29/) | Medium | Only extend on match |
| Shortest Common Supersequence | [LC #1092](https://leetcode.com/problems/shortest-common-supersequence/) | Hard | len = m + n - LCS |
| Min Delete to Make Strings Equal | [LC #583](https://leetcode.com/problems/delete-operation-for-two-strings/) | Medium | del = m + n - 2*LCS |
| Longest Palindromic Subsequence | [LC #516](https://leetcode.com/problems/longest-palindromic-subsequence/) | Medium | LCS(s, reverse(s)) |
| Min Insertions for Palindrome | [LC #1312](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | Hard | len - LPS |
| Edit Distance | [LC #72](https://leetcode.com/problems/edit-distance/) | Medium | Extended LCS with costs |
| Distinct Subsequences | [LC #115](https://leetcode.com/problems/distinct-subsequences/) | Hard | Count s1 as subseq of s2 |
| Longest Repeating Subsequence | [GFG](https://www.geeksforgeeks.org/longest-repeating-subsequence/) | Medium | LCS(s, s) with i≠j |
| Is Subsequence | [LC #392](https://leetcode.com/problems/is-subsequence/) | Easy | LCS == len(s)? |

---

## 26. DP: LIS (6 problems)

> **Recognition:** "longest increasing/decreasing" / "box stacking" / "envelope nesting"
> **Edge Cases:** All same → 1. Already sorted → n. Strictly vs non-strictly.

**Parent:** [Longest Increasing Subsequence #300](https://leetcode.com/problems/longest-increasing-subsequence/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **LIS** | [LC #300](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | **PARENT** — O(n²) DP or O(n log n) |
| Number of LIS | [LC #673](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | Medium | Track count + length |
| Russian Doll Envelopes | [LC #354](https://leetcode.com/problems/russian-doll-envelopes/) | Hard | Sort by width, LIS on height |
| Max Length Pair Chain | [LC #646](https://leetcode.com/problems/maximum-length-of-pair-chain/) | Medium | Greedy or LIS |
| Increasing Triplet Subsequence | [LC #334](https://leetcode.com/problems/increasing-triplet-subsequence/) | Medium | Track first and second smallest |
| Longest String Chain | [LC #1048](https://leetcode.com/problems/longest-string-chain/) | Medium | Sort by length, LIS with predecessor |

---

## 27. DP: MCM / PARTITION DP (8 problems)

> **Recognition:** "minimum cost to merge/split" / "burst balloons" / "partition" / "parenthesize"
> **Template:** Try every partition k: `dp[i][j] = min/max over k of (dp[i][k] + dp[k+1][j] + cost)`
> **Edge Cases:** Single element, two elements, must memoize.

**Parent:** Matrix Chain Multiplication — [GFG](https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **MCM** | [GFG](https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/) | Hard | **PARENT** |
| Burst Balloons | [LC #312](https://leetcode.com/problems/burst-balloons/) | Hard | Which to burst LAST |
| Palindrome Partitioning II | [LC #132](https://leetcode.com/problems/palindrome-partitioning-ii/) | Hard | Min cuts for all palindromes |
| Boolean Parenthesization | [GFG](https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/) | Hard | Count True evaluations |
| Scramble String | [LC #87](https://leetcode.com/problems/scramble-string/) | Hard | Can s2 be scrambled s1? |
| Min Cost Tree From Leaf | [LC #1130](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) | Medium | MCM on merging leaves |
| Super Egg Drop | [LC #887](https://leetcode.com/problems/super-egg-drop/) | Hard | Partition floors |
| Stone Game variations | [LC #1000](https://leetcode.com/problems/minimum-cost-to-merge-stones/) | Hard | Merge adjacent |

---

## 28. DP: GRID / PATH (6 problems)

> **Recognition:** "unique paths" / "minimum path sum" / "grid with obstacles"
> **Template:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]` (paths) or `min(...)` (cost)
> **Edge Cases:** Start is obstacle, single row/col, negatives.

**Parent:** [Unique Paths #62](https://leetcode.com/problems/unique-paths/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Unique Paths** | [LC #62](https://leetcode.com/problems/unique-paths/) | Medium | **PARENT** |
| Unique Paths II (obstacles) | [LC #63](https://leetcode.com/problems/unique-paths-ii/) | Medium | Obstacle = 0 paths |
| Minimum Path Sum | [LC #64](https://leetcode.com/problems/minimum-path-sum/) | Medium | Add min(top, left) |
| Triangle | [LC #120](https://leetcode.com/problems/triangle/) | Medium | Bottom-up: min of two below |
| Maximal Square | [LC #221](https://leetcode.com/problems/maximal-square/) | Medium | `min(left, top, diag) + 1` |
| Dungeon Game | [LC #174](https://leetcode.com/problems/dungeon-game/) | Hard | Work backwards |

---

## 29. DP: FIBONACCI / LINEAR (7 problems)

> **Recognition:** "ways to reach step n" / "rob houses" / "decode" / "tiling"
> **Core Idea:** Current depends on fixed number of previous states.
> **Edge Cases:** n=0/1, leading zeros (decode), circular (robber II).

**Parent:** [Climbing Stairs #70](https://leetcode.com/problems/climbing-stairs/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Climbing Stairs** | [LC #70](https://leetcode.com/problems/climbing-stairs/) | Easy | **PARENT** — `dp[n] = dp[n-1] + dp[n-2]` |
| House Robber | [LC #198](https://leetcode.com/problems/house-robber/) | Medium | `max(dp[i-1], dp[i-2] + nums[i])` |
| House Robber II (circular) | [LC #213](https://leetcode.com/problems/house-robber-ii/) | Medium | Two passes: skip first OR last |
| Decode Ways | [LC #91](https://leetcode.com/problems/decode-ways/) | Medium | 1-digit + 2-digit choices |
| Min Cost Climbing Stairs | [LC #746](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | Add cost to min(prev two) |
| Tribonacci | [LC #1137](https://leetcode.com/problems/n-th-tribonacci-number/) | Easy | 3 previous states |
| Delete and Earn | [LC #740](https://leetcode.com/problems/delete-and-earn/) | Medium | Transform to House Robber |

---

## 30. DP: TREES (5 problems)

> **Recognition:** "diameter" / "max path sum" / "tree with weights"
> **Template:** Each node returns value to parent + updates global answer.
> **Edge Cases:** Single node, negatives (sometimes skip subtree).

**Parent:** [Diameter of Binary Tree #543](https://leetcode.com/problems/diameter-of-binary-tree/)

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| **Diameter of Binary Tree** | [LC #543](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | **PARENT** — left+right height, return max+1 |
| Binary Tree Max Path Sum | [LC #124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | node+left+right for answer |
| Longest Same Value Path | [LC #687](https://leetcode.com/problems/longest-univalue-path/) | Medium | Extend only if same value |
| House Robber III | [LC #337](https://leetcode.com/problems/house-robber-iii/) | Medium | Rob this (skip kids) vs skip (rob kids) |
| Sum of Distances in Tree | [LC #834](https://leetcode.com/problems/sum-of-distances-in-tree/) | Hard | Re-rooting technique |

---

## 31. DP: BITMASK (5 problems)

> **Recognition:** "assign items to slots" / "TSP" / n ≤ 20 (2^n feasible)
> **Template:** `dp[mask][i]` = answer for subset `mask` ending at `i`.
> **Edge Cases:** n > 20 → infeasible.

**Parent:** Travelling Salesman Problem

| Problem | Link | Difficulty | Variant |
|---------|------|-----------|---------|
| Partition to K Equal Subsets | [LC #698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | Medium | Bitmask tracks used |
| Shortest Path Visiting All Nodes | [LC #847](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | Hard | BFS + bitmask |
| Can I Win | [LC #464](https://leetcode.com/problems/can-i-win/) | Medium | Bitmask for chosen numbers |
| Matchsticks to Square | [LC #473](https://leetcode.com/problems/matchsticks-to-square/) | Medium | Bitmask or backtracking |
| Minimum XOR Sum of Two Arrays | [LC #1879](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/) | Hard | Assign elements optimally |

---

## CROSS-PATTERN RECOGNITION GUIDE

> When you see a new problem, use this table to identify the pattern:

| If you see... | First try... | If that fails... |
|--------------|-------------|-----------------|
| Sorted array + find element | Binary Search | Two Pointers |
| Subarray sum = K (all positive) | Sliding Window | — |
| Subarray sum = K (has negatives) | Prefix Sum + HashMap | NOT sliding window |
| "Next greater/smaller element" | Monotonic Stack | Brute O(n²) |
| "Find median" | Two Heaps | Sort (if static) |
| "Connected components" | Union Find | BFS/DFS |
| "Shortest path unweighted" | BFS | — |
| "Shortest path weighted" | Dijkstra | Bellman-Ford (negative weights) |
| "All subsets/permutations" | Backtracking | Bitmask DP (if n ≤ 20) |
| "Choose/don't choose + capacity" | 0/1 Knapsack | Greedy (if provable) |
| "Unlimited supply + target" | Unbounded Knapsack | — |
| "Two strings + common" | LCS Family | Edit Distance variant |
| "Ordering with dependencies" | Topological Sort | — |
| "Minimize max" / "maximize min" | Binary Search on Answer | — |
| "Level order" / "spreading" | BFS | — |
| "Cycle detection" (directed) | DFS (3-state) | Topological Sort |
| "Cycle detection" (undirected) | Union Find | DFS |
| "K sorted arrays" | K-Way Merge (Heap) | — |
| "Top K / Kth largest" | Heap of size K | Quickselect O(n) avg |
| "Overlapping intervals" | Merge Intervals | Sweep Line |
| "Missing/duplicate in [1,n]" | Cyclic Sort | XOR / Math |
| "Reverse linked list segment" | In-Place LL Reversal | — |
| "Spiral / rotate matrix" | Matrix Traversal (boundaries) | — |

---

## PATTERN COVERAGE TRACKER

> **Target:** 5-7 problems per pattern before it's considered solidified.
> **Update this after every session.** Teacher checks this when selecting problems.

| # | Pattern | Problems Solved | Target | Status | Problems Done |
|---|---------|----------------|--------|--------|---------------|
| 1 | Two Pointers | 5 | 5-7 | On track | 3Sum, Sort Colors, Trapping Rain Water, Container (concept), Remove Dupes (concept) |
| 2 | Sliding Window | 1 | 5-7 | Needs more | Sliding Window Max (brute only) |
| 3 | Binary Search | 1 | 5-7 | Just started | Binary Search #704 |
| 4 | Prefix Sum/Product | 3 | 5-7 | Needs more | Subarray Sum K, Product Except Self, Kadane's (related) |
| 5 | Monotonic Stack | 0 | 5-7 | Not started | — |
| 6 | Merge Intervals | 1 | 5-7 | Needs more | Merge Intervals |
| 7 | Cyclic Sort | 0 | 5-7 | Not started | — |
| 8 | LL Reversal | 1 | 5-7 | Needs more | Reverse Linked List |
| 9 | BFS | 0 | 5-7 | Not started (theory done) | — |
| 10 | DFS | 0 | 5-7 | Not started (theory done) | — |
| 11 | Backtracking | 1 | 5-7 | Needs more | Generate Permutations |
| 12 | Topological Sort | 0 | 5-7 | Not started | — |
| 13 | Union Find | 0 | 5-7 | Not started | — |
| 14 | Two Heaps | 0 | 3 | Not started | — |
| 15 | Top-K / Heap | 0 | 5-7 | Not started | — |
| 16 | K-Way Merge | 0 | 4 | Not started | — |
| 17 | Kadane's / Subarray | 2 | 4 | Needs more | Max Subarray, Max Product Subarray |
| 18 | Greedy | 1 | 5-7 | Needs more | Buy/Sell Stock |
| 19 | Matrix Traversal | 0 | 5 | Not started (files created) | — |
| 20 | Bit Manipulation | 0 | 5-7 | Not started | — |
| 21 | Trie | 0 | 5 | Not started | — |
| 22 | Shortest Path | 0 | 4 | Not started | — |
| 23 | DP: 0/1 Knapsack | 0 | 5-7 | Not started | — |
| 24 | DP: Unbounded Knapsack | 0 | 5-7 | Not started | — |
| 25 | DP: LCS | 0 | 5-7 | Not started | — |
| 26 | DP: LIS | 0 | 5-7 | Not started | — |
| 27 | DP: MCM | 0 | 5-7 | Not started | — |
| 28 | DP: Grid/Path | 0 | 5-7 | Not started | — |
| 29 | DP: Fibonacci/Linear | 0 | 5-7 | Not started | — |
| 30 | DP: Trees | 0 | 5 | Not started | — |
| 31 | DP: Bitmask | 0 | 5 | Not started | — |
| 32 | Divide and Conquer | 0 | 4 | Not started | — |

**Also tracked but not a "pattern":**
- Fast/Slow Pointers (Floyd's): 3 problems (Cycle I, Cycle II, Middle of LL) — under Two Pointers
- Dummy Head technique: 1 problem (Add Two Numbers) — under LL construction
- Next Permutation (lexicographic): 1 problem — standalone

**Patterns at 5+ = SOLIDIFIED.** Patterns at 0-2 = PRIORITY for upcoming sessions.
