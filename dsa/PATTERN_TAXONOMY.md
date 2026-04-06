# DSA Pattern Taxonomy: Comprehensive Interview Reference

> **Philosophy:** The PATTERN is the top-level organizer. Problems from ANY data structure
> branch off from each pattern. This is how Aditya Verma teaches DP, how NeetCode organizes
> his roadmap, and how Striver structures his A2Z sheet.
>
> **Sources cross-referenced:**
> 1. Aditya Verma's DP playlist (YouTube) -- 0/1 Knapsack, Unbounded Knapsack, LCS, LIS, MCM, DP on Trees
> 2. Striver's A2Z DSA Sheet (takeuforward.org) -- Step-by-step topic organization
> 3. NeetCode.io Roadmap -- 18 pattern categories with 150 problems
> 4. LeetCode Study Plans -- Official curated problem lists
> 5. "14 Patterns to Ace Any Coding Interview" by Fahim ul Haq (Educative.io)
> 6. Sean Prashad's LeetCode Patterns -- Pattern-tagged problem list (~170 problems)

---

## HOW TO USE THIS DOCUMENT

For each pattern you will find:
- **Pattern Name** and sub-variants
- **Core Idea / Recognition Trigger** -- the "aha" moment that tells you this pattern applies
- **Edge Cases** specific to this pattern
- **Representative Problems** (5-10) with LeetCode numbers, spanning DIFFERENT data structures
- **Common Mistakes / Traps** that cost people interviews

---
---

## PATTERN 1: TWO POINTERS

### Sub-variants
- **Opposite direction** (converging from both ends)
- **Same direction** (one fast, one slow -- different from Floyd's cycle)
- **Three pointers** (Dutch National Flag)

### Core Idea / Recognition Trigger
You have a SORTED array (or can sort it) and need to find pairs/triplets satisfying a condition.
Or you need to process elements from both ends inward. The key trigger: "find two elements such
that..." on a sorted structure, or "partition in-place."

**Sources:** Fahim ul Haq's "14 Patterns" (Pattern #1), Sean Prashad (Two Pointers category),
NeetCode (Two Pointers section), Striver A2Z (Step 3.1).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Two Sum II (sorted input) | 167 | Opposite direction | Array | Classic converging pointers on sorted array |
| 2 | 3Sum | 15 | Opposite direction + iteration | Array | Fix one, two-pointer on remainder; skip duplicates |
| 3 | Container With Most Water | 11 | Opposite direction | Array | Shrink from shorter side; greedy + two pointers |
| 4 | Trapping Rain Water | 42 | Opposite direction | Array | Track leftMax/rightMax converging inward |
| 5 | Remove Duplicates from Sorted Array | 26 | Same direction | Array | Slow pointer = write position, fast = read position |
| 6 | Move Zeroes | 283 | Same direction | Array | Slow pointer for non-zero write position |
| 7 | Sort Colors (Dutch National Flag) | 75 | Three pointers | Array | low/mid/high partition into 0s, 1s, 2s |
| 8 | Valid Palindrome | 125 | Opposite direction | String | Converge from both ends comparing characters |
| 9 | Backspace String Compare | 844 | Reverse same direction | String | Process from end, skip characters after '#' |
| 10 | Squares of a Sorted Array | 977 | Opposite direction | Array | Largest squares at ends; merge inward |

### Edge Cases
- Empty array or single element
- All duplicates (e.g., [2,2,2] for 3Sum -- must skip duplicates correctly)
- Negative numbers in sorted array (affects square/product problems)
- When both pointers land on the same index (usually invalid for pair problems)

### Common Mistakes / Traps
1. **Forgetting to skip duplicates in 3Sum/4Sum** -- leads to duplicate triplets in output
2. **Moving the wrong pointer** in Container With Most Water (must move the shorter side)
3. **Off-by-one on boundaries** -- using `left < right` vs `left <= right` (for pairs: use `<`)
4. **Applying two pointers on UNSORTED input** -- must sort first, or the pattern breaks
5. **Not handling the case where both values equal target** in Two Sum II

---

## PATTERN 2: SLIDING WINDOW

### Sub-variants
- **Fixed-size window** (window size k is given)
- **Variable-size window** (find min/max window satisfying a condition)
- **Sliding window with HashMap/Counter** (character frequency tracking)

### Core Idea / Recognition Trigger
You need to find a CONTIGUOUS subarray/substring that satisfies some condition (max sum,
contains all characters, at most k distinct, etc.). The trigger: "contiguous subarray/substring"
+ "optimize size/sum/count."

**Sources:** Fahim ul Haq's "14 Patterns" (Pattern #2 and #3), Sean Prashad (Sliding Window),
NeetCode (Sliding Window), Striver A2Z (Step 10 -- Sliding Window & Two Pointer).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Maximum Sum Subarray of Size K | -- | Fixed window | Array | Slide window of size k, track running sum |
| 2 | Best Time to Buy and Sell Stock | 121 | Variable window (special) | Array | Track min price so far, max profit at each step |
| 3 | Longest Substring Without Repeating Characters | 3 | Variable window + HashSet | String | Expand right, shrink left when duplicate found |
| 4 | Minimum Window Substring | 76 | Variable window + HashMap | String | Expand until valid, shrink to minimize |
| 5 | Longest Repeating Character Replacement | 424 | Variable window + counter | String | Window valid if len - maxFreq <= k |
| 6 | Permutation in String | 567 | Fixed window + counter | String | Sliding window of size len(s1) over s2 |
| 7 | Sliding Window Maximum | 239 | Fixed window + Deque | Array | Monotonic deque maintains window max |
| 8 | Minimum Size Subarray Sum | 209 | Variable window | Array | Shrink from left when sum >= target |
| 9 | Subarrays with K Different Integers | 992 | Variable window (atMost trick) | Array | atMost(k) - atMost(k-1) = exactly(k) |
| 10 | Fruit Into Baskets | 904 | Variable window + HashMap | Array | Longest subarray with at most 2 distinct |

### Edge Cases
- Empty string/array
- Window size k larger than array length
- All identical elements
- Single character string for "without repeating" problems
- Target that cannot be achieved (return 0 or -1 depending on problem)

### Common Mistakes / Traps
1. **Shrinking the window incorrectly** -- for variable window, shrink from LEFT only (not both sides)
2. **Off-by-one when calculating window size** -- size = right - left + 1, not right - left
3. **Not updating the HashMap/counter when shrinking** -- must decrement count for left element
4. **Confusing "at most K" with "exactly K"** -- exactly(K) = atMost(K) - atMost(K-1)
5. **Using sliding window when prefix sum is needed** -- sliding window needs non-negative values for min-size problems (or the shrink logic breaks)

---

## PATTERN 3: BINARY SEARCH

### Sub-variants
- **Classic binary search** (find element in sorted array)
- **Binary search on answer / search space** (minimize/maximize a value)
- **Binary search with conditions** (first true, last true in boolean array)
- **Rotated array binary search**

### Core Idea / Recognition Trigger
The search space is MONOTONIC (sorted, or answer has a monotonic feasibility). The trigger:
"find minimum/maximum value such that some condition holds" or "sorted array" or "O(log n)
required." For binary search on answer: if you can answer "is X feasible?" in O(n), and
feasibility is monotonic, binary search on X.

**Sources:** NeetCode (Binary Search section), Striver A2Z (Step 4 -- Binary Search),
Sean Prashad (Binary Search), Aditya Verma (Binary Search on Answer playlist).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Binary Search | 704 | Classic | Sorted Array | Textbook binary search |
| 2 | Search in Rotated Sorted Array | 33 | Rotated array | Array | Identify sorted half, then decide direction |
| 3 | Find Minimum in Rotated Sorted Array | 153 | Rotated array | Array | Compare mid with right to find pivot |
| 4 | Koko Eating Bananas | 875 | Binary search on answer | Array | Min speed where she can finish in h hours |
| 5 | Capacity to Ship Packages | 1011 | Binary search on answer | Array | Min capacity to ship all in 'days' days |
| 6 | Split Array Largest Sum | 410 | Binary search on answer | Array | Minimize the max sum when splitting into m parts |
| 7 | Median of Two Sorted Arrays | 4 | Binary search on partition | Two Arrays | Partition both arrays to find combined median |
| 8 | Search a 2D Matrix | 74 | Classic (flattened) | 2D Matrix | Treat matrix as sorted 1D array |
| 9 | Find Peak Element | 162 | Condition-based | Array | Move toward the side with a larger neighbor |
| 10 | Time Based Key-Value Store | 981 | Upper bound variant | HashMap + Array | Binary search on timestamps for a key |

### Edge Cases
- Single element array
- Target smaller than all elements or larger than all elements
- Duplicates in array (changes from O(log n) to O(n) worst case -- see LC 81)
- Integer overflow in `mid = (left + right) / 2` -- use `mid = left + (right - left) // 2`
- Empty array

### Common Mistakes / Traps
1. **Infinite loop from wrong boundary update** -- if `left = mid` instead of `left = mid + 1`, you loop forever when left + 1 == right
2. **Wrong comparison in rotated array** -- compare with `nums[right]` not `nums[left]` for finding minimum
3. **Binary search on answer: wrong bounds** -- lower bound too high or upper bound too low misses the answer
4. **Not handling duplicates** -- Search in Rotated Sorted Array II (LC 81) needs worst-case O(n)
5. **Returning wrong index** -- after the loop, check whether `left` or `right` holds the answer depending on your template

---

## PATTERN 4: FAST / SLOW POINTERS (Floyd's Cycle Detection)

### Sub-variants
- **Cycle detection** (linked list, array-as-linked-list)
- **Finding cycle start** (Floyd's algorithm phase 2)
- **Finding middle of linked list**
- **Happy number / sequence cycle detection**

### Core Idea / Recognition Trigger
You need to detect a CYCLE in a linked structure, or find the MIDDLE of a sequence, or detect
repeating patterns. The trigger: "cycle," "repeated," "middle," or any problem where elements
form a functional graph (next = f(current)).

**Sources:** Fahim ul Haq's "14 Patterns" (Pattern #4 -- Fast & Slow Pointers),
NeetCode (Linked List section), Striver A2Z (Step 6 -- Linked List).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Linked List Cycle | 141 | Cycle detection | Linked List | Fast moves 2, slow moves 1; if they meet, cycle exists |
| 2 | Linked List Cycle II | 142 | Find cycle start | Linked List | After meeting, reset one to head; move both by 1 |
| 3 | Middle of the Linked List | 876 | Find middle | Linked List | When fast reaches end, slow is at middle |
| 4 | Happy Number | 202 | Cycle detection | Number sequence | Digits-squared sequence either reaches 1 or cycles |
| 5 | Find the Duplicate Number | 287 | Cycle detection in array | Array | Array values as "next pointers" form a cycle |
| 6 | Palindrome Linked List | 234 | Find middle + reverse | Linked List | Find middle, reverse second half, compare |
| 7 | Reorder List | 143 | Find middle + merge | Linked List | Find middle, reverse second half, interleave |

### Edge Cases
- Single node (no cycle possible, middle is itself)
- Cycle at the head (entire list is a cycle)
- Even vs odd length (middle definition changes -- usually second middle for even)
- Self-loop (node points to itself)

### Common Mistakes / Traps
1. **Forgetting null checks on fast.next** -- `while fast and fast.next` (both must be checked)
2. **Wrong phase 2 in Floyd's** -- after meeting point, reset ONE pointer to head, move BOTH by 1
3. **Middle of even-length list** -- fast/slow gives second middle; if you need first, use `fast.next and fast.next.next`
4. **Modifying the list in palindrome check** -- must reverse back if the problem requires no modification

---

## PATTERN 5: PREFIX SUM / PREFIX PRODUCT

### Sub-variants
- **Prefix sum** (range sum queries)
- **Prefix sum + HashMap** (subarray sum equals K)
- **Prefix product** (product of array except self)
- **Prefix XOR** (range XOR queries)
- **2D prefix sum** (submatrix sum)

### Core Idea / Recognition Trigger
You need RANGE QUERIES (sum/product/XOR of subarray) or need to find subarrays with a
specific sum. The trigger: "subarray sum equals K," "range sum query," "product of all
except self." The key insight: sum(i..j) = prefix[j+1] - prefix[i].

**Sources:** NeetCode (Arrays & Hashing), Striver A2Z (Step 3 -- Prefix Sum problems),
LeetCode Study Plan (Prefix Sum).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Range Sum Query - Immutable | 303 | Basic prefix sum | Array | Precompute prefix sums, O(1) range query |
| 2 | Subarray Sum Equals K | 560 | Prefix sum + HashMap | Array | Count prefix[j] - prefix[i] == k using HashMap |
| 3 | Product of Array Except Self | 238 | Prefix/Suffix product | Array | Left product array * right product array |
| 4 | Contiguous Array (0s and 1s) | 525 | Prefix sum + HashMap | Array | Replace 0 with -1, find longest subarray with sum 0 |
| 5 | Range Sum Query 2D - Immutable | 304 | 2D prefix sum | Matrix | Inclusion-exclusion on 2D prefix sums |
| 6 | Find Pivot Index | 724 | Prefix sum | Array | leftSum == totalSum - leftSum - nums[i] |
| 7 | Subarray Sums Divisible by K | 974 | Prefix sum + modular arithmetic | Array | Two prefix sums with same remainder mod K |
| 8 | Path Sum III | 437 | Prefix sum on tree | Binary Tree | DFS with running prefix sum + HashMap (like LC 560 on a tree) |

### Edge Cases
- Empty array
- Single element subarray
- Negative numbers (prefix sum is NOT monotonic -- cannot use binary search on it)
- Integer overflow in prefix products (use modular arithmetic or long/bigint)
- k = 0 in subarray sum (the HashMap must be initialized with {0: 1})

### Common Mistakes / Traps
1. **Forgetting to initialize HashMap with {0: 1}** in subarray sum problems -- misses subarrays starting at index 0
2. **Using prefix sum when values can be negative** and expecting monotonicity -- it won't be monotonic
3. **Integer overflow** in prefix product problems -- use division carefully (or avoid it for Product Except Self)
4. **Off-by-one in 2D prefix sum** -- the inclusion-exclusion formula must be exact
5. **Not handling the mod of negative numbers** in Python (Python's % handles it, but other languages don't)

---

## PATTERN 6: MONOTONIC STACK / MONOTONIC QUEUE

### Sub-variants
- **Monotonic decreasing stack** (next greater element)
- **Monotonic increasing stack** (next smaller element)
- **Monotonic deque** (sliding window min/max)

### Core Idea / Recognition Trigger
You need the NEXT GREATER / NEXT SMALLER element, or need to maintain a window's min/max
efficiently. The trigger: "next greater element," "largest rectangle," "sliding window
maximum," "stock span." The stack maintains a sorted order and pops elements that violate it.

**Sources:** Striver A2Z (Step 9 -- Stack and Queue, Monotonic Stack section),
NeetCode (Stack section), Sean Prashad (Stack pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Next Greater Element I | 496 | Monotonic decreasing stack | Array/Stack | Pop smaller elements when larger element arrives |
| 2 | Next Greater Element II (circular) | 503 | Monotonic stack + circular | Array/Stack | Process array twice (2*n) to handle circularity |
| 3 | Daily Temperatures | 739 | Monotonic decreasing stack | Array/Stack | Days until a warmer temperature |
| 4 | Largest Rectangle in Histogram | 84 | Monotonic increasing stack | Array/Stack | Find boundaries where bar is the minimum height |
| 5 | Maximal Rectangle | 85 | Monotonic stack + histogram | Matrix/Stack | Each row builds a histogram; apply LC 84 per row |
| 6 | Trapping Rain Water | 42 | Monotonic stack (or two pointers) | Array/Stack | Stack tracks boundaries; pop to compute trapped water |
| 7 | Sliding Window Maximum | 239 | Monotonic deque | Array/Deque | Deque front = max of window; remove expired indices |
| 8 | Online Stock Span | 901 | Monotonic decreasing stack | Stack | Count consecutive days with price <= today |
| 9 | Remove K Digits | 402 | Monotonic increasing stack | String/Stack | Remove peaks to make smallest number |
| 10 | Sum of Subarray Minimums | 907 | Monotonic stack (contribution) | Array/Stack | For each element, count subarrays where it's the minimum |

### Edge Cases
- All elements in increasing order (stack never pops -- all get "no next greater")
- All elements in decreasing order (everything pops immediately)
- Duplicate elements (use `<=` vs `<` carefully -- affects correctness of boundaries)
- Empty stack at the end (remaining elements have no next greater)

### Common Mistakes / Traps
1. **Storing values vs indices in the stack** -- almost always store INDICES (you need position information)
2. **Strict vs non-strict monotonicity** -- `<=` vs `<` changes behavior with duplicates; LC 84 and LC 907 require careful handling
3. **Not handling the remaining elements** in the stack after processing -- they have no next greater/smaller
4. **Circular array problems** -- must iterate 2*n and use `i % n` for index
5. **Largest Rectangle: not adding sentinel values** -- adding 0 at the beginning and end of heights simplifies boundary handling

---

## PATTERN 7: BFS / LEVEL-ORDER TRAVERSAL

### Sub-variants
- **Tree level-order traversal** (process level by level)
- **Graph BFS** (shortest path in unweighted graph)
- **Multi-source BFS** (start from multiple sources simultaneously)
- **BFS on matrix/grid** (flood fill, rotting oranges)
- **BFS with state** (visited includes extra dimensions)

### Core Idea / Recognition Trigger
You need the SHORTEST PATH in an unweighted graph, or need to process nodes LEVEL BY LEVEL,
or need to expand from MULTIPLE SOURCES simultaneously. The trigger: "minimum steps," "shortest
path" (unweighted), "level by level," "nearest," "rotting/spreading from multiple points."

**Sources:** Fahim ul Haq's "14 Patterns" (Pattern #8 -- Tree BFS), NeetCode (Trees, Graphs),
Striver A2Z (Step 11 -- Graphs BFS/DFS), Sean Prashad (BFS pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Binary Tree Level Order Traversal | 102 | Tree level-order | Binary Tree | Queue-based level-by-level processing |
| 2 | Binary Tree Right Side View | 199 | Tree level-order | Binary Tree | Last node at each level |
| 3 | Binary Tree Zigzag Level Order | 103 | Tree level-order | Binary Tree | Alternate direction per level |
| 4 | Rotting Oranges | 994 | Multi-source BFS | Grid/Matrix | All rotten oranges start in queue simultaneously |
| 5 | 01 Matrix | 542 | Multi-source BFS | Grid/Matrix | All 0-cells start in queue; expand to find nearest 0 for each 1 |
| 6 | Word Ladder | 127 | Graph BFS | String/Graph | Shortest transformation sequence = shortest path |
| 7 | Shortest Path in Binary Matrix | 1091 | Grid BFS | Grid/Matrix | 8-directional BFS on grid |
| 8 | Number of Islands | 200 | Grid BFS (or DFS) | Grid/Matrix | BFS from each unvisited '1', mark connected component |
| 9 | Open the Lock | 752 | BFS with state | Graph | Each state = 4-digit combo; BFS through state space |
| 10 | Minimum Knight Moves | 1197 | BFS with pruning | Grid/Graph | BFS on infinite grid with knight moves |

### Edge Cases
- Empty tree/grid
- Single node/cell
- Disconnected components (BFS from one source won't reach all nodes)
- Grid with all obstacles (no valid path)
- Start == End (distance is 0)

### Common Mistakes / Traps
1. **Not tracking the level boundary** -- must process `len(queue)` elements per level, not just one at a time
2. **Forgetting to mark visited BEFORE adding to queue** (not after popping) -- causes duplicates in queue and TLE
3. **Multi-source BFS: not adding ALL sources initially** -- must enqueue all sources at time 0
4. **BFS on grid: going out of bounds** -- always check 0 <= r < rows and 0 <= c < cols
5. **Using BFS for weighted graphs** -- BFS only gives shortest path for UNWEIGHTED graphs; use Dijkstra for weighted

---

## PATTERN 8: DFS / BACKTRACKING

### Sub-variants
- **Tree DFS** (preorder, inorder, postorder)
- **Graph DFS** (connected components, cycle detection)
- **Grid DFS** (island problems, flood fill)
- **Backtracking** (generate all valid combinations/permutations/partitions)
- **Constraint satisfaction** (N-Queens, Sudoku)

### Core Idea / Recognition Trigger
You need to EXPLORE ALL PATHS, generate ALL VALID COMBINATIONS, or traverse a tree/graph
depth-first. The trigger: "all possible," "generate all," "find all paths," or any problem
where you make a choice, explore, then UNDO the choice (backtrack).

**Sources:** Fahim ul Haq's "14 Patterns" (Pattern #7 -- Tree DFS, Pattern #10 -- Subsets),
NeetCode (Backtracking section), Striver A2Z (Step 7 -- Recursion & Backtracking),
Sean Prashad (DFS and Backtracking patterns).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Subsets | 78 | Backtracking (include/exclude) | Array | Generate all 2^n subsets |
| 2 | Subsets II | 90 | Backtracking + skip duplicates | Array | Sort first, skip same elements at same recursion level |
| 3 | Permutations | 46 | Backtracking (ordering) | Array | Generate all n! orderings |
| 4 | Combination Sum | 39 | Backtracking (reuse allowed) | Array | Unbounded selection with target sum |
| 5 | N-Queens | 51 | Constraint satisfaction | Grid/Board | Row-by-row placement with col/diagonal constraints |
| 6 | Word Search | 79 | Grid DFS + backtracking | Grid/String | Mark visited, explore 4 directions, unmark on return |
| 7 | Palindrome Partitioning | 131 | Partition backtracking | String | Try every cut point, check palindrome, recurse on rest |
| 8 | Generate Parentheses | 22 | Constraint-based branching | String | open < n can add '(', close < open can add ')' |
| 9 | Letter Combinations of a Phone Number | 17 | Multi-way branching | String | Each digit maps to 3-4 characters; explore all combos |
| 10 | Sudoku Solver | 37 | Constraint satisfaction | Grid/Board | Cell-by-cell, validate row/col/box constraints |

### Edge Cases
- Empty input (return empty result or [[]])
- Single element (base case)
- Duplicates in input (must sort and skip to avoid duplicate results)
- Very deep recursion (stack overflow risk -- Python default limit is ~1000)
- Large search space (need aggressive pruning)

### Common Mistakes / Traps
1. **Not making a COPY of the path** when adding to results -- `result.append(path[:])` not `result.append(path)`
2. **Forgetting to backtrack (undo the choice)** -- `path.pop()` or `visited[r][c] = False` after recursive call
3. **Not sorting before skipping duplicates** -- the skip logic `if i > start and nums[i] == nums[i-1]: continue` only works on sorted arrays
4. **Modifying the input array during iteration** -- use a separate visited set/array
5. **Not pruning aggressively enough** -- without pruning, backtracking degenerates to brute force

---

## PATTERN 9: TOPOLOGICAL SORT

### Sub-variants
- **Kahn's algorithm** (BFS-based, using in-degree)
- **DFS-based** (post-order DFS, reverse finish order)
- **Cycle detection in directed graph** (if topo sort fails, cycle exists)
- **Topological ordering with constraints** (lexicographically smallest, etc.)

### Core Idea / Recognition Trigger
You have DEPENDENCIES between tasks/nodes and need to find a valid ordering, or detect if
ordering is impossible (cycle). The trigger: "prerequisites," "course schedule," "build order,"
"dependency resolution," any DAG ordering problem.

**Sources:** NeetCode (Graphs -- Advanced section), Striver A2Z (Step 11 -- Topo Sort),
Sean Prashad (Topological Sort), Fahim ul Haq's "14 Patterns" (Pattern #12 -- Topological Sort).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Course Schedule | 207 | Cycle detection (BFS/DFS) | Directed Graph | Can all courses be finished? (is graph a DAG?) |
| 2 | Course Schedule II | 210 | Topological ordering | Directed Graph | Return a valid course order |
| 3 | Alien Dictionary | 269 | Build graph + topo sort | String/Graph | Derive character ordering from sorted alien words |
| 4 | Minimum Height Trees | 310 | BFS leaf removal (topo-like) | Undirected Graph | Peel leaves layer by layer until 1-2 nodes remain |
| 5 | Parallel Courses | 1136 | Topo sort + level counting | Directed Graph | Min semesters = longest path in DAG |
| 6 | Sequence Reconstruction | 444 | Unique topo sort check | Directed Graph | Is there exactly one valid topological order? |
| 7 | Sort Items by Groups Respecting Dependencies | 1203 | Two-level topo sort | Directed Graph | Topo sort within groups AND between groups |

### Edge Cases
- Self-loops (immediate cycle)
- Disconnected components (process all components)
- Multiple valid orderings (problem may ask for any one, or lexicographically smallest)
- Empty graph (trivially sorted)
- Single node with no edges

### Common Mistakes / Traps
1. **Forgetting to check for cycles** -- if the topo sort result has fewer nodes than the graph, there is a cycle
2. **Building the graph wrong for Alien Dictionary** -- only compare ADJACENT words, and only the FIRST differing character creates an edge
3. **Not handling disconnected components** -- must start BFS from ALL nodes with in-degree 0
4. **Kahn's: decrementing in-degree incorrectly** -- must decrement for ALL neighbors, not just one
5. **Confusing directed vs undirected** -- topological sort is ONLY for directed acyclic graphs

---

## PATTERN 10: UNION FIND / DISJOINT SET

### Sub-variants
- **Basic Union-Find** (connected components)
- **Union by Rank + Path Compression** (optimized)
- **Union-Find with size tracking** (component sizes)
- **Union-Find for dynamic connectivity** (edges added over time)

### Core Idea / Recognition Trigger
You need to dynamically GROUP elements and CHECK if two elements are in the same group.
The trigger: "connected components," "are X and Y connected?", "merge groups," "number of
islands" (especially with dynamic additions), "earliest time all connected."

**Sources:** NeetCode (Graphs -- Advanced section), Striver A2Z (Step 11 -- Disjoint Set),
Sean Prashad (Union Find pattern), LeetCode Study Plan (Graph Theory).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Number of Connected Components | 323 | Basic UF | Undirected Graph | Count distinct roots after all unions |
| 2 | Redundant Connection | 684 | Cycle detection via UF | Undirected Graph | Edge that connects already-connected nodes |
| 3 | Accounts Merge | 721 | UF on strings | Array of Lists | Union emails belonging to same person |
| 4 | Longest Consecutive Sequence | 128 | UF (or HashSet) | Array | Union consecutive numbers, find largest component |
| 5 | Number of Islands II | 305 | Dynamic UF | Grid/Matrix | Add land cells one by one, maintain component count |
| 6 | Graph Valid Tree | 261 | UF cycle detection | Undirected Graph | Tree = connected + no cycle (n-1 edges, all connected) |
| 7 | Earliest Moment When Everyone Becomes Friends | 1101 | UF with timestamps | Array/Graph | Process edges in time order, check when 1 component |
| 8 | Satisfiability of Equality Equations | 990 | UF on characters | String/Graph | Union '==' pairs, check '!=' pairs don't conflict |

### Edge Cases
- Single element (is its own component)
- All elements already in the same set
- Redundant union operations (must handle gracefully)
- Very large n (path compression + union by rank keeps it nearly O(1) amortized)

### Common Mistakes / Traps
1. **Not implementing path compression** -- without it, find() degrades to O(n)
2. **Not implementing union by rank/size** -- without it, tree becomes a linked list
3. **Finding root of wrong element** -- always call find() on both elements before comparing
4. **Off-by-one in component counting** -- start with n components, decrement on each successful union (where roots differ)
5. **Using Union-Find for directed graphs** -- UF is for UNDIRECTED connectivity only; for directed, use DFS/BFS or topo sort

---

## PATTERN 11: KADANE'S / SUBARRAY PATTERNS

### Sub-variants
- **Maximum subarray sum** (classic Kadane's)
- **Maximum product subarray** (track min and max simultaneously)
- **Circular subarray** (Kadane's + total minus minimum subarray)
- **Subarray count** (subarrays satisfying a condition)

### Core Idea / Recognition Trigger
You need the OPTIMAL CONTIGUOUS SUBARRAY (max sum, max product, etc.). The trigger: "maximum
subarray," "contiguous subarray" with optimization. The core insight: at each index, either
EXTEND the previous subarray or START a new one.

**Sources:** NeetCode (Arrays & Hashing, 1-D DP), Striver A2Z (Step 3 -- Arrays),
Sean Prashad (Arrays pattern), Aditya Verma (Kadane's).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Maximum Subarray | 53 | Classic Kadane's | Array | dp[i] = max(nums[i], dp[i-1] + nums[i]) |
| 2 | Maximum Product Subarray | 152 | Track min/max | Array | Negative * negative = positive; track both extremes |
| 3 | Maximum Sum Circular Subarray | 918 | Kadane's + complement | Array | max(maxSubarray, total - minSubarray) |
| 4 | Maximum Sum of Two Non-Overlapping Subarrays | 1031 | Double Kadane's | Array | Prefix max for first subarray, Kadane's for second |
| 5 | Longest Turbulent Subarray | 978 | Kadane's variant (alternating) | Array | Extend if direction alternates, reset otherwise |
| 6 | Maximum Absolute Sum of Any Subarray | 1749 | Max and Min Kadane's | Array | Answer = max(maxKadane, abs(minKadane)) |
| 7 | Subarray Sum Equals K | 560 | Prefix sum (NOT Kadane's) | Array | Included for contrast: this is prefix sum, NOT Kadane's |

### Edge Cases
- All negative numbers (Kadane's still works -- picks the least negative single element)
- All zeros (max subarray sum = 0; max product = 0)
- Single element array
- Circular case where ALL elements are negative (total - minSubarray = 0, but empty subarray not allowed -- must handle this)
- Zeros in product subarray (reset the running product)

### Common Mistakes / Traps
1. **Confusing Kadane's with prefix sum** -- Kadane's is O(1) space for max subarray; prefix sum is for finding subarrays with specific sum (LC 560)
2. **Max product: forgetting to track minimum** -- a very negative min * a negative number = a very positive max
3. **Circular max: not handling all-negative case** -- if all negative, total - minSubarray = 0, but empty subarray is invalid; return the standard Kadane's result
4. **Returning the subarray vs the sum** -- Kadane's as stated gives the sum; to return indices, track start/end when currentMax resets
5. **Initializing currentMax to 0 instead of nums[0]** -- must handle negative-only arrays

---

## PATTERN 12: MERGE INTERVALS

### Sub-variants
- **Merge overlapping intervals** (combine into non-overlapping set)
- **Insert interval** (add and merge)
- **Interval intersection** (find overlapping parts)
- **Sweep line / event processing** (meeting rooms, skyline)

### Core Idea / Recognition Trigger
You have a collection of INTERVALS and need to merge, intersect, or count overlaps.
The trigger: "intervals," "meetings," "overlapping," "start and end times."
Almost always sort by start time first.

**Sources:** Fahim ul Haq's "14 Patterns" (Pattern #5 -- Merge Intervals),
NeetCode (Intervals section), Striver A2Z (Step 12 -- Greedy, Interval scheduling),
Sean Prashad (Intervals pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Merge Intervals | 56 | Merge overlapping | Array of Intervals | Sort by start, extend or create new |
| 2 | Insert Interval | 57 | Insert and merge | Array of Intervals | Find overlap region, merge, keep non-overlapping |
| 3 | Non-overlapping Intervals | 435 | Remove minimum overlapping | Array of Intervals | Sort by end, greedily keep non-overlapping (=interval scheduling) |
| 4 | Meeting Rooms | 252 | Check any overlap | Array of Intervals | Sort by start, check if any start < prev end |
| 5 | Meeting Rooms II | 253 | Count max concurrent | Array of Intervals | Min-heap of end times, or sweep line |
| 6 | Interval List Intersections | 986 | Find intersections | Two Lists of Intervals | Two pointers, advance the one ending earlier |
| 7 | Employee Free Time | 759 | Merge + find gaps | List of Interval Lists | Flatten, sort, find gaps between merged intervals |
| 8 | Minimum Number of Arrows to Burst Balloons | 452 | Overlap counting | Array of Intervals | Sort by end, count distinct non-overlapping groups |

### Edge Cases
- Single interval (nothing to merge)
- All intervals identical (merge into one)
- No overlaps at all (return as-is)
- Intervals that touch at endpoints -- [1,2] and [2,3]: overlapping or not? (problem-specific)
- Intervals not sorted initially (must sort first)

### Common Mistakes / Traps
1. **Sorting by start vs end** -- merging: sort by START; interval scheduling (max non-overlapping): sort by END
2. **Not handling touching intervals** -- [1,3] and [3,5]: usually these DO overlap/merge (check problem definition)
3. **Meeting Rooms II: using sort instead of heap** -- the two-array sort approach works but heap approach is more intuitive and extensible
4. **Modifying intervals in-place while iterating** -- safer to build a new result list
5. **Forgetting to handle the last interval** -- after the loop, the current interval must be added to results

---

## PATTERN 13: LINKED LIST MANIPULATION

### Sub-variants
- **Reversal** (full list, partial, k-group)
- **Merge** (two sorted lists, k sorted lists)
- **Reorder / Rearrange** (interleave, partition)
- **Dummy head technique** (simplify edge cases)

### Core Idea / Recognition Trigger
You need to RESTRUCTURE a linked list -- reverse it, merge lists, split and recombine,
or remove nodes. The trigger: any linked list problem requiring pointer manipulation.
The dummy head trick eliminates most edge cases with head changes.

**Sources:** Fahim ul Haq's "14 Patterns" (Pattern #6 -- In-place Reversal of LinkedList),
NeetCode (Linked List section), Striver A2Z (Step 6 -- Linked List),
Sean Prashad (Linked List pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Reverse Linked List | 206 | Full reversal | Linked List | Iterative: prev/curr/next; Recursive: reverse rest then link |
| 2 | Reverse Linked List II | 92 | Partial reversal | Linked List | Reverse only positions m to n; track connection points |
| 3 | Reverse Nodes in k-Group | 25 | K-group reversal | Linked List | Count k nodes, reverse group, connect to next group |
| 4 | Merge Two Sorted Lists | 21 | Two-list merge | Linked List | Dummy head, compare and advance smaller |
| 5 | Merge K Sorted Lists | 23 | K-way merge | Linked List + Heap | Min-heap holds heads of all lists; pop smallest, push next |
| 6 | Remove Nth Node From End of List | 19 | Two pointers (gap) | Linked List | Advance fast n steps, then move both; slow.next = slow.next.next |
| 7 | Reorder List | 143 | Find mid + reverse + merge | Linked List | Three-step: find middle, reverse second half, interleave |
| 8 | Add Two Numbers | 2 | Digit-by-digit + carry | Linked List | Process both lists simultaneously, handle carry |
| 9 | Copy List with Random Pointer | 138 | Clone with HashMap | Linked List + HashMap | Map old nodes to new nodes, then wire random pointers |
| 10 | LRU Cache | 146 | Doubly LL + HashMap | DLL + HashMap | HashMap for O(1) lookup, DLL for O(1) eviction order |

### Edge Cases
- Empty list (return None)
- Single node
- Even vs odd length (affects middle finding and reversal)
- k larger than list length (don't reverse -- return as is)
- Cycle in list (must detect first before other operations)

### Common Mistakes / Traps
1. **Losing the next pointer during reversal** -- must save `curr.next` BEFORE rewiring
2. **Not using a dummy head** -- leads to special-casing when the head changes (e.g., remove head node)
3. **Off-by-one in "remove nth from end"** -- advance fast n+1 steps (not n) if using the "slow stops before target" approach
4. **Not handling carry in Add Two Numbers** -- after both lists are exhausted, carry might still be 1
5. **Modifying pointers in wrong order** -- draw the diagram on paper first; order of pointer updates matters

---

## PATTERN 14: TREE TRAVERSAL PATTERNS

### Sub-variants
- **Inorder** (left, root, right) -- gives sorted order for BST
- **Preorder** (root, left, right) -- used for serialization, copying structure
- **Postorder** (left, right, root) -- used for deletion, bottom-up computation
- **Morris traversal** (O(1) space inorder/preorder)
- **Iterative with stack** (explicit stack simulates recursion)

### Core Idea / Recognition Trigger
Different traversal orders serve different purposes. Inorder = sorted BST values. Preorder =
serialize/reconstruct structure. Postorder = compute values bottom-up (height, diameter).
The trigger: think about what INFORMATION FLOW you need -- top-down (preorder) or bottom-up
(postorder) or sorted order (inorder).

**Sources:** NeetCode (Trees section), Striver A2Z (Step 8 -- Binary Trees, BST),
Sean Prashad (Tree DFS pattern), Fahim ul Haq's "14 Patterns" (Pattern #7 -- Tree DFS).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Binary Tree Inorder Traversal | 94 | Inorder | Binary Tree | Stack-based iterative or recursive |
| 2 | Kth Smallest Element in a BST | 230 | Inorder (BST sorted) | BST | Inorder gives sorted; stop at kth element |
| 3 | Validate Binary Search Tree | 98 | Inorder with bounds | BST | Inorder must be strictly increasing; OR propagate bounds |
| 4 | Construct BT from Preorder and Inorder | 105 | Preorder + Inorder | Binary Tree | Preorder root splits inorder into left/right subtrees |
| 5 | Serialize and Deserialize Binary Tree | 297 | Preorder serialization | Binary Tree | Preorder with null markers enables unique reconstruction |
| 6 | Diameter of Binary Tree | 543 | Postorder (height) | Binary Tree | Compute height bottom-up; diameter = leftH + rightH at each node |
| 7 | Binary Tree Maximum Path Sum | 124 | Postorder (value) | Binary Tree | Compute max gain bottom-up; global max tracks best path |
| 8 | Lowest Common Ancestor | 236 | Postorder (search) | Binary Tree | Search both subtrees; if both non-null, current node is LCA |
| 9 | Flatten Binary Tree to Linked List | 114 | Reverse postorder / Morris | Binary Tree | Process right, then left, then root; link to previous |
| 10 | Binary Tree Cameras | 968 | Postorder (greedy + states) | Binary Tree | 3-state system: covered, has camera, not covered |

### Edge Cases
- Empty tree (return None / [] / 0)
- Single node (root is the answer for most problems)
- Skewed tree (essentially a linked list -- O(n) stack depth)
- BST with duplicates (usually not allowed, but check problem statement)

### Common Mistakes / Traps
1. **Using inorder for non-BST problems** -- inorder sorted order only applies to BSTs
2. **Confusing preorder and postorder for bottom-up problems** -- diameter, height, max path sum all need POSTORDER
3. **Stack overflow on skewed trees** -- iterative traversal avoids this; Morris traversal is O(1) space
4. **Construct from traversals: not using a hashmap for inorder index lookup** -- O(n) lookup per node makes it O(n^2)
5. **Global variable vs return value** -- diameter/max path sum need a global max updated during postorder, but RETURN only the single-branch gain to the parent

---

## PATTERN 15: DP -- 0/1 KNAPSACK FAMILY

### Sub-variants (Aditya Verma's classification)
- **Subset Sum** (can we reach target sum?)
- **Equal Sum Partition** (can we split into two equal halves?)
- **Count of Subset Sum** (how many subsets reach target?)
- **Minimum Subset Sum Difference** (minimize difference between two partitions)
- **Target Sum** (assign +/- to reach target)

### Core Idea / Recognition Trigger
You have a set of items, each usable AT MOST ONCE, and a capacity/target. At each item you
choose: INCLUDE or EXCLUDE. The trigger: "subset," "partition," "can you select items to reach
target," "each item used at most once."

**Aditya Verma's approach:** All 0/1 Knapsack problems share the same recursion:
`solve(items, n, W) = max/or(solve(items, n-1, W), solve(items, n-1, W-wt[n]) + val[n])`

**Sources:** Aditya Verma (0/1 Knapsack playlist -- 6 problems), NeetCode (1-D DP and 2-D DP),
Striver A2Z (Step 14 -- DP, Subsequence DP), Sean Prashad (DP pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | 0/1 Knapsack | -- | Classic template | Array | Include or exclude each item, maximize value under weight limit |
| 2 | Partition Equal Subset Sum | 416 | Equal partition (subset sum) | Array | Target = totalSum/2, then subset sum check |
| 3 | Target Sum | 494 | Count subsets | Array | Transform: find subset with sum = (total+target)/2 |
| 4 | Last Stone Weight II | 1049 | Min difference partition | Array | Minimize |S1 - S2| = minimize |total - 2*S1| |
| 5 | Ones and Zeroes | 474 | 2D knapsack | Array of Strings | Each string has cost (zeros, ones); maximize count within budget |
| 6 | Partition to K Equal Sum Subsets | 698 | K-way partition (backtracking+DP) | Array | Generalization of equal partition to K groups |
| 7 | Number of Subsets with Given Difference | -- | Count (Aditya Verma) | Array | S1-S2=diff, S1+S2=total -> S1=(total+diff)/2 |

### Edge Cases
- Total sum is odd (equal partition impossible -- return false immediately)
- Target is negative (transform: target = abs(target) or return 0)
- All zeros in array (every subset sums to 0)
- Empty array (only sum 0 is achievable)
- (total + target) is odd in Target Sum (no valid assignment -- return 0)

### Common Mistakes / Traps
1. **Not recognizing the problem as knapsack** -- "partition equal subset sum" doesn't mention knapsack, but it IS knapsack
2. **1D DP array: iterating capacity FORWARD instead of BACKWARD** -- forward iteration reuses current row's values (makes it unbounded knapsack)
3. **Forgetting the (total + target) % 2 != 0 check** in Target Sum -- impossible case
4. **Count of subsets: not handling zeros** -- zeros can be in either subset, multiplying the count by 2^(number of zeros)
5. **Space optimization: confusing row direction** -- in 1D DP, iterate W from HIGH to LOW for 0/1 knapsack

---

## PATTERN 16: DP -- UNBOUNDED KNAPSACK FAMILY

### Sub-variants (Aditya Verma's classification)
- **Unbounded Knapsack** (items reusable unlimited times)
- **Coin Change** (minimum coins to reach amount)
- **Coin Change II** (count ways to reach amount)
- **Rod Cutting** (maximize revenue from rod of length n)
- **Ribbon/Rod of maximum pieces**

### Core Idea / Recognition Trigger
Same as 0/1 Knapsack but items can be REUSED. The trigger: "unlimited supply," "can use each
item multiple times," "coin change," "rod cutting." The key difference from 0/1: when you
INCLUDE an item, you stay at the same item index (not i-1).

**Aditya Verma's approach:** Same recursion as 0/1 but the include branch stays at item i:
`solve(items, n, W) = max(solve(items, n-1, W), solve(items, n, W-wt[n]) + val[n])`

**Sources:** Aditya Verma (Unbounded Knapsack playlist), NeetCode (1-D DP),
Striver A2Z (Step 14 -- DP, Subsequence DP).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Coin Change | 322 | Minimize count | Array | Min coins to make amount; each coin reusable |
| 2 | Coin Change II | 518 | Count ways | Array | Number of combinations to make amount |
| 3 | Unbounded Knapsack | -- | Classic template | Array | Maximize value, items reusable |
| 4 | Rod Cutting | -- | Maximize revenue | Array | Cut rod into pieces to maximize total price |
| 5 | Perfect Squares | 279 | Minimize count | Number | Min perfect squares summing to n (coins = 1,4,9,16,...) |
| 6 | Minimum Cost for Tickets | 983 | Minimize cost | Array | Travel days with 1/7/30-day passes (like coins) |
| 7 | Integer Break | 343 | Maximize product | Number | Break n into sum of integers, maximize product |
| 8 | Word Break | 139 | Boolean reachability | String + Dictionary | Can string be segmented using dictionary words (unlimited reuse)? |

### Edge Cases
- Amount = 0 (1 way with 0 coins, or 0 coins needed)
- No coins available (impossible unless amount = 0)
- Very large amount with small coins (large DP table)
- Single coin that doesn't divide amount evenly (impossible)

### Common Mistakes / Traps
1. **1D DP array: iterating capacity BACKWARD** -- that is 0/1 knapsack! For unbounded, iterate FORWARD (low to high)
2. **Coin Change II: outer loop order matters** -- coins in outer loop = combinations; amount in outer loop = permutations (LC 377)
3. **Initializing dp[0]** -- for count problems: dp[0] = 1 (one way to make 0). For min problems: dp[0] = 0 (zero coins for amount 0)
4. **Forgetting to check dp[amount] == infinity** -- means amount is unreachable, return -1
5. **Confusing Coin Change (min coins) with Coin Change II (count ways)** -- different DP transitions despite same setup

---

## PATTERN 17: DP -- LCS (LONGEST COMMON SUBSEQUENCE) FAMILY

### Sub-variants (Aditya Verma's classification)
- **Longest Common Subsequence** (two strings)
- **Longest Common Substring** (contiguous version)
- **Shortest Common Supersequence** (merge two strings)
- **Edit Distance** (min operations to transform)
- **Longest Palindromic Subsequence** (LCS of s and reverse(s))
- **Minimum Insertions to Make Palindrome** (len - LPS)
- **Sequence Pattern Matching** (is s1 a subsequence of s2?)
- **Print LCS** (backtrack through DP table)

### Core Idea / Recognition Trigger
You are comparing TWO STRINGS (or a string against itself reversed) character by character.
The trigger: "two strings," "subsequence," "edit distance," "palindromic subsequence,"
"supersequence." The DP state: dp[i][j] = answer for first i chars of s1 and first j chars of s2.

**Aditya Verma's approach:** All LCS family problems share this base:
```
if s1[i-1] == s2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])  // or min for edit distance
```

**Sources:** Aditya Verma (LCS playlist -- 8 problems), NeetCode (2-D DP),
Striver A2Z (Step 14 -- DP on Strings).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Longest Common Subsequence | 1143 | Classic LCS | Two Strings | Base template for entire family |
| 2 | Edit Distance | 72 | Min operations | Two Strings | Insert/delete/replace; dp[i][j] = min of 3 choices |
| 3 | Longest Palindromic Subsequence | 516 | LCS(s, reverse(s)) | Single String | Reduce to LCS by reversing string |
| 4 | Shortest Common Supersequence | 1092 | Build from LCS | Two Strings | Length = m + n - LCS; reconstruct by backtracking DP table |
| 5 | Minimum Insertions to Make Palindrome | 1312 | len - LPS | Single String | Insertions needed = len(s) - LPS(s) |
| 6 | Distinct Subsequences | 115 | Count matching subsequences | Two Strings | How many times does t appear as subsequence of s? |
| 7 | Interleaving String | 97 | Two strings forming third | Three Strings | dp[i][j] = can s1[:i] and s2[:j] form s3[:i+j]? |
| 8 | Wildcard Matching | 44 | Pattern matching | Two Strings | '?' matches one, '*' matches any sequence |
| 9 | Regular Expression Matching | 10 | Pattern matching | Two Strings | '.' matches one, 'x*' matches zero or more of x |

### Edge Cases
- One or both strings empty (base cases: dp[0][j] and dp[i][0])
- Identical strings (LCS = the string itself; edit distance = 0)
- Completely different strings (LCS = 0; edit distance = max(m, n))
- Palindromic subsequence of a palindrome (= the string itself)
- Very long strings (space optimization: use 1D array rolling two rows)

### Common Mistakes / Traps
1. **1-indexed vs 0-indexed confusion** -- DP table is (m+1) x (n+1); s1[i-1] compares with s2[j-1]
2. **Longest Common Substring vs Subsequence** -- substring resets to 0 when characters don't match; subsequence takes max of skip options
3. **Edit Distance: wrong operation mapping** -- dp[i-1][j-1] = replace, dp[i-1][j] = delete from s1, dp[i][j-1] = insert into s1
4. **Printing the LCS: wrong backtracking direction** -- start from dp[m][n] and trace back; don't try to build forward
5. **Space optimization breaks backtracking** -- if you need to PRINT the answer, you need the full 2D table

---

## PATTERN 18: DP -- LIS (LONGEST INCREASING SUBSEQUENCE) FAMILY

### Sub-variants
- **Classic LIS** (O(n^2) DP or O(n log n) binary search)
- **Number of LIS** (count all longest subsequences)
- **Russian Doll Envelopes** (2D LIS)
- **Longest Chain / Box Stacking** (LIS on pairs/tuples)
- **Minimum deletions to make sorted** (n - LIS)

### Core Idea / Recognition Trigger
You need the longest subsequence where elements are STRICTLY INCREASING (or non-decreasing,
or satisfy some order). The trigger: "longest increasing," "minimum deletions to make sorted,"
"fitting envelopes/boxes," "longest chain of pairs."

**Sources:** Aditya Verma (LIS in DP playlist), NeetCode (1-D DP), Striver A2Z (Step 14 -- DP on LIS).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Longest Increasing Subsequence | 300 | Classic LIS | Array | O(n^2) DP: for each i, check all j < i. O(n log n): patience sorting |
| 2 | Number of Longest Increasing Subsequence | 673 | Count LIS | Array | Track both length[] and count[] arrays |
| 3 | Russian Doll Envelopes | 354 | 2D LIS | Array of Pairs | Sort by width ASC, height DESC for same width; LIS on heights |
| 4 | Longest String Chain | 1048 | LIS on strings | Array of Strings | Sort by length; dp[word] = max(dp[predecessor] + 1) |
| 5 | Maximum Length of Pair Chain | 646 | LIS on pairs (greedy works too) | Array of Pairs | Sort by end, greedily pick non-overlapping (or DP) |
| 6 | Longest Arithmetic Subsequence | 1027 | LIS variant | Array | dp[i][diff] = length of arithmetic subseq ending at i with common difference diff |
| 7 | Minimum Number of Removals to Make Mountain Array | 1671 | LIS + LDS | Array | LIS from left + LIS from right; mountain = LIS[i] + LDS[i] - 1 |
| 8 | Delete and Earn | 740 | LIS-like (House Robber variant) | Array | Group by value, then House Robber on value frequencies |

### Edge Cases
- All elements equal (LIS = 1)
- Already sorted (LIS = n)
- Strictly decreasing (LIS = 1)
- Duplicate values (strictly increasing means duplicates don't extend LIS)
- Empty array (LIS = 0)

### Common Mistakes / Traps
1. **O(n log n) LIS: the tails array is NOT the actual LIS** -- it gives the correct LENGTH but not the actual subsequence
2. **Russian Doll Envelopes: not sorting height DESCENDING for same width** -- without this, same-width envelopes can nest (wrong)
3. **Strict vs non-strict increasing** -- check problem statement; LC 300 is strictly increasing
4. **Number of LIS: forgetting to handle the count update** -- when dp[j]+1 == dp[i], ADD to count; when dp[j]+1 > dp[i], REPLACE count
5. **Using LIS when greedy works** -- Maximum Length of Pair Chain (LC 646) is better solved greedily (like interval scheduling)

---

## PATTERN 19: DP -- MATRIX CHAIN MULTIPLICATION (MCM) FAMILY

### Sub-variants (Aditya Verma's classification)
- **Matrix Chain Multiplication** (minimize multiplication cost)
- **Burst Balloons** (maximize coins from popping)
- **Palindrome Partitioning II** (minimize cuts)
- **Boolean Parenthesization** (count true evaluations)
- **Scramble String** (can one string transform to another via splits?)
- **Minimum Cost to Cut a Stick** (minimize cutting cost)

### Core Idea / Recognition Trigger
You have a SEQUENCE and need to find the optimal way to SPLIT/PARTITION it. For every subrange
[i, j], you try every possible split point k and combine results. The trigger: "partition a
sequence optimally," "burst/pop elements in some order," "split into groups with cost."

**Aditya Verma's approach:** All MCM problems share this template:
```
def solve(arr, i, j):
    if i >= j: return base_case
    result = initial_value  # infinity for min, 0 for max
    for k in range(i, j):  # try every split point
        left = solve(arr, i, k)
        right = solve(arr, k+1, j)
        result = optimize(result, left + right + cost(i, k, j))
    return result
```

**Sources:** Aditya Verma (MCM playlist -- 7 problems), NeetCode (2-D DP),
Striver A2Z (Step 14 -- DP on Partition / MCM).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Matrix Chain Multiplication | -- | Classic template | Array of dimensions | Minimize total scalar multiplications |
| 2 | Burst Balloons | 312 | Reverse thinking (last burst) | Array | Think about which balloon to burst LAST in [i,j] |
| 3 | Palindrome Partitioning II | 132 | Minimize cuts | String | Min cuts so every piece is a palindrome |
| 4 | Boolean Parenthesization | -- | Count true evaluations | String (T/F and ops) | Place parentheses to maximize True evaluations |
| 5 | Scramble String | 87 | String splitting check | Two Strings | Can s1 become s2 via recursive splitting and swapping? |
| 6 | Minimum Cost to Cut a Stick | 1547 | Minimize cut cost | Array of cut positions | Try each cut position as the split point |
| 7 | Strange Printer | 664 | Interval DP variant | String | If s[i]==s[j], merge subproblems; else try all splits |
| 8 | Super Egg Drop | 887 | Binary search + MCM | Number | Minimize worst-case drops to find critical floor |

### Edge Cases
- Single element range (i == j: base case, usually 0 cost or trivially solved)
- Two elements (only one split point)
- All identical elements (often simplifies significantly)
- Very large range (memoization essential -- O(n^3) time, O(n^2) space)

### Common Mistakes / Traps
1. **Burst Balloons: thinking about FIRST burst instead of LAST** -- the key insight is which balloon to burst LAST in the range [i,j]
2. **Wrong split point range** -- for arr[i..j], k ranges from i to j-1 (not i to j)
3. **Not memoizing** -- without memoization, the recursion is exponential
4. **Palindrome Partitioning II: not precomputing isPalindrome** -- checking palindrome in the DP loop makes it O(n^3); precompute for O(n^2) total
5. **Super Egg Drop: brute force is O(kn^2)** -- needs binary search optimization on the split point to get O(kn log n)

---

## PATTERN 20: DP -- GRID / PATH DP

### Sub-variants
- **Count paths** (how many ways from top-left to bottom-right)
- **Minimum/Maximum path sum**
- **Path with obstacles**
- **Triangle path**
- **Cherry Pickup / two-player grid**

### Core Idea / Recognition Trigger
You have a 2D GRID and move in restricted directions (usually right/down). You need to find
count of paths, min/max cost path, or handle obstacles. The trigger: "grid," "robot moving
right/down," "path sum," "unique paths."

**Sources:** NeetCode (2-D DP section), Striver A2Z (Step 14 -- DP on Grids),
Aditya Verma (grid DP within general DP).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Unique Paths | 62 | Count paths | Grid | dp[i][j] = dp[i-1][j] + dp[i][j-1] |
| 2 | Unique Paths II | 63 | Paths with obstacles | Grid | dp[i][j] = 0 if obstacle, else same formula |
| 3 | Minimum Path Sum | 64 | Min cost path | Grid | dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) |
| 4 | Triangle | 120 | Non-rectangular grid | Triangle Array | Bottom-up: dp[i][j] += min(dp[i+1][j], dp[i+1][j+1]) |
| 5 | Dungeon Game | 174 | Reverse direction DP | Grid | Must go bottom-right to top-left (future determines present) |
| 6 | Cherry Pickup | 741 | Two simultaneous paths | Grid | Two people traverse simultaneously; 4D->3D DP |
| 7 | Cherry Pickup II | 1463 | Two robots | Grid | Two robots from top row, move down; 3D DP (row, col1, col2) |
| 8 | Maximal Square | 221 | Largest square of 1s | Grid | dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 |
| 9 | Minimum Falling Path Sum | 931 | Column-flexible path | Grid | Can move to (i+1, j-1), (i+1, j), or (i+1, j+1) |

### Edge Cases
- 1x1 grid (answer is the cell itself)
- Grid with all obstacles except start and end (may be impossible)
- Very large grid (space optimization: use rolling 1D array)
- Negative values in grid (affects min/max calculations)
- Start or end cell is an obstacle (return 0 or -1)

### Common Mistakes / Traps
1. **Dungeon Game: solving forward instead of backward** -- minimum health depends on FUTURE cells, so must DP from bottom-right
2. **Not initializing first row and first column** -- they can only be reached from one direction
3. **Cherry Pickup: two separate greedy paths don't work** -- must model both paths simultaneously to avoid double-counting
4. **Maximal Square: confusing with maximal rectangle** -- square uses min of 3 neighbors + 1; rectangle uses histogram approach
5. **Space optimization: overwriting values you still need** -- use two rows or process in correct order

---

## PATTERN 21: DP -- PARTITION DP

### Sub-variants
- **Partition into K subsets** (equal sum, maximum sum minimized)
- **Palindrome Partitioning** (all parts palindromes)
- **Egg Drop** (partition floors into test ranges)
- **Painting/Coloring** (partition with adjacency constraints)

### Core Idea / Recognition Trigger
You need to DIVIDE an array/string into segments under constraints and optimize some cost.
The trigger: "split array into K parts," "partition string so each part satisfies X,"
"minimize the maximum/sum of partitions." Often overlaps with MCM pattern but the split
is constrained (e.g., exactly K groups, or each group satisfies a property).

**Sources:** Striver A2Z (Step 14 -- Partition DP), NeetCode (2-D DP),
Aditya Verma (overlaps with MCM family).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Palindrome Partitioning II | 132 | Min cuts for palindrome parts | String | dp[i] = min cuts for s[0..i]; check all j where s[j..i] is palindrome |
| 2 | Split Array Largest Sum | 410 | Min-max partition (binary search OR DP) | Array | Minimize the max sum when split into m groups |
| 3 | Partition to K Equal Sum Subsets | 698 | K-way equal partition | Array | Backtracking + bitmask DP |
| 4 | Painting the Fence | -- | Partition with color constraints | Array | dp[i] = (k-1) * (dp[i-1] + dp[i-2]) |
| 5 | Partition Array for Maximum Sum | 1043 | Max sum with at most K-length parts | Array | dp[i] = max over j of dp[i-j] + j * max(arr[i-j..i-1]) |
| 6 | Minimum Difficulty of a Job Schedule | 1335 | Partition days, min max-per-day | Array | dp[d][i] = min over j of dp[d-1][j] + max(jobs[j+1..i]) |
| 7 | Largest Sum of Averages | 813 | K partitions, max average sum | Array | dp[i][k] = max over j of dp[j][k-1] + avg(nums[j..i]) |

### Edge Cases
- K = 1 (entire array is one partition)
- K = n (each element is its own partition)
- All elements equal (any partition works)
- Impossible to partition (sum not divisible by K)

### Common Mistakes / Traps
1. **Split Array Largest Sum: not recognizing binary search on answer** -- binary search is cleaner than DP for this problem
2. **Partition to K Equal Sum: not pruning** -- without pruning, bitmask DP or backtracking is too slow
3. **Confusing Partition DP with MCM** -- MCM tries ALL split points within a range; Partition DP often has a fixed number of groups
4. **Not precomputing range queries** -- computing max/sum in inner loop makes it O(n^3); precompute prefix sums

---

## PATTERN 22: DP -- DP ON TREES

### Sub-variants
- **Rerooting technique** (compute answer rooted at every node)
- **Tree diameter / path problems** (postorder aggregation)
- **Independent set / vertex cover** (take or skip each node)
- **Subtree aggregation** (aggregate children's values)

### Core Idea / Recognition Trigger
The DP state is at each NODE of a tree. You run DFS (usually postorder) and at each node
combine results from children. The trigger: "tree," "maximum/minimum path in tree," "rob
houses on a tree," "count subtrees satisfying X."

**Sources:** Aditya Verma (DP on Trees playlist -- 4-5 problems), Striver A2Z (Step 14 -- DP on Trees),
NeetCode (Trees section, Advanced DP).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Binary Tree Maximum Path Sum | 124 | Path aggregation | Binary Tree | At each node: max gain = node + max(left, right); global max considers both sides |
| 2 | Diameter of Binary Tree | 543 | Path aggregation | Binary Tree | Diameter through a node = leftHeight + rightHeight |
| 3 | House Robber III | 337 | Take or skip (tree) | Binary Tree | Each node returns (rob_this, skip_this) |
| 4 | Unique Binary Search Trees | 96 | Catalan number DP | BST | G(n) = sum of G(i-1)*G(n-i) for i=1..n |
| 5 | Longest Path With Different Adjacent Colors | 2246 | Path aggregation | N-ary Tree | Track two longest differently-colored child paths |
| 6 | Sum of Distances in Tree | 834 | Rerooting technique | Undirected Tree | Compute for root, then re-root to every node in O(n) |
| 7 | Binary Tree Cameras | 968 | Greedy + DP states | Binary Tree | 3-state postorder: 0=not covered, 1=has camera, 2=covered |
| 8 | Maximum Product of Splitted Binary Tree | 1339 | Subtree sum aggregation | Binary Tree | Total sum - subtree sum gives other part; maximize product |

### Edge Cases
- Empty tree
- Single node (usually a base case -- return its value)
- Skewed tree (chain -- degenerates to linear DP)
- Negative node values (affects whether to include a subtree path or not)
- Root vs any node as starting point (path sum problems: path can start/end anywhere)

### Common Mistakes / Traps
1. **Confusing the value returned to parent vs the global answer** -- for max path sum: return single-branch gain to parent, but update global with both branches
2. **Not handling negative values** -- max(0, child_gain) clamps negative children to 0 (don't extend through them)
3. **Rerooting: wrong parent contribution calculation** -- when re-rooting, the parent's contribution is total - child's subtree contribution
4. **House Robber III: using HashMap for memoization instead of pair return** -- pair (rob, skip) is cleaner and faster than HashMap memoization
5. **Forgetting that the path doesn't have to pass through root** -- diameter and max path sum can be at any subtree

---

## PATTERN 23: DP -- FIBONACCI / CLIMBING STAIRS FAMILY

### Sub-variants
- **Fibonacci sequence** (dp[i] = dp[i-1] + dp[i-2])
- **Climbing Stairs** (same as Fibonacci)
- **House Robber** (dp[i] = max(dp[i-1], dp[i-2] + val))
- **Decode Ways** (conditional Fibonacci)
- **Tribonacci / N-step stairs**

### Core Idea / Recognition Trigger
dp[i] depends on a FIXED NUMBER of previous states (usually 1-3). The simplest family of DP.
The trigger: "number of ways to reach step n," "take or skip with adjacency constraint."
Can always be space-optimized to O(1) with just a few variables.

**Sources:** NeetCode (1-D DP, first problems), Striver A2Z (Step 14 -- Introduction to DP),
Aditya Verma (DP Introduction).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Climbing Stairs | 70 | Classic Fibonacci DP | Number | dp[i] = dp[i-1] + dp[i-2] |
| 2 | Fibonacci Number | 509 | Direct Fibonacci | Number | dp[i] = dp[i-1] + dp[i-2]; base: dp[0]=0, dp[1]=1 |
| 3 | House Robber | 198 | Take or skip | Array | dp[i] = max(dp[i-1], dp[i-2] + nums[i]) |
| 4 | House Robber II | 213 | Circular take or skip | Array | Two linear passes: [0..n-2] and [1..n-1] |
| 5 | Decode Ways | 91 | Conditional Fibonacci | String | dp[i] += dp[i-1] if valid 1-digit; dp[i] += dp[i-2] if valid 2-digit |
| 6 | Min Cost Climbing Stairs | 746 | Optimization Fibonacci | Array | dp[i] = cost[i] + min(dp[i-1], dp[i-2]) |
| 7 | N-th Tribonacci Number | 1137 | Three-state recurrence | Number | dp[i] = dp[i-1] + dp[i-2] + dp[i-3] |
| 8 | Delete and Earn | 740 | House Robber on values | Array | Group by value, apply House Robber pattern |

### Edge Cases
- n = 0 or n = 1 (base cases)
- All values equal
- Very large n (only need O(1) space with variable rotation)
- Decode Ways: leading zeros ("06" is invalid), consecutive zeros ("00" is invalid)

### Common Mistakes / Traps
1. **Decode Ways: not handling '0' correctly** -- "0" alone is invalid; "10" and "20" are valid but "30" is not
2. **House Robber II: not handling n=1 separately** -- with circular, the two-pass approach doesn't work for single-element
3. **Off-by-one in Climbing Stairs** -- dp[0] = 1 (one way to be at ground), dp[1] = 1 (one way to reach step 1)
4. **Not recognizing the pattern** -- Delete and Earn, Paint House, etc. are all House Robber in disguise
5. **Using O(n) space when O(1) suffices** -- only need prev1 and prev2 variables

---

## PATTERN 24: DP -- BITMASK DP

### Sub-variants
- **Traveling Salesman Problem (TSP)** (visit all nodes, minimize cost)
- **Assign tasks to workers** (each worker does one task)
- **Partition into subsets** (bitmask tracks which elements are used)
- **Counting subsets with constraints**

### Core Idea / Recognition Trigger
You have a SMALL set of items (n <= 20) and need to track WHICH ITEMS ARE USED. The state
includes a bitmask where each bit represents whether an item is selected. The trigger:
n <= 20, "assign each item to exactly one group," "visit all cities," "select a subset
with constraints."

**Sources:** Striver A2Z (Step 14 -- DP on Bits), NeetCode (Advanced DP),
LeetCode Study Plan (Bitmask DP problems).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Partition to K Equal Sum Subsets | 698 | Subset partition | Array | Bitmask tracks which elements are used |
| 2 | Minimum Cost to Connect Two Groups | 1595 | Assignment problem | 2D Cost Matrix | dp[mask] = min cost with group2 elements in mask connected |
| 3 | Shortest Path Visiting All Nodes | 847 | TSP variant (BFS + bitmask) | Graph | State = (current_node, visited_mask) |
| 4 | Maximum Students Taking Exam | 1349 | Bitmask on rows | Grid | dp[row][mask] = max students with seating arrangement mask |
| 5 | Number of Ways to Wear Different Hats | 1434 | Assign hats to people | Array | Bitmask on people (n<=10), iterate over hats |
| 6 | Find the Shortest Superstring | 943 | TSP-like (string overlap) | Array of Strings | dp[mask][i] = shortest superstring using strings in mask, ending with i |
| 7 | Parallel Courses II | 1494 | DAG scheduling with limit | Graph + Bitmask | dp[mask] = min semesters to complete courses in mask |

### Edge Cases
- n > 20 (bitmask DP is infeasible -- 2^20 = ~1M is about the limit)
- Empty mask (base case: no items selected)
- Full mask (all items selected -- usually the target state)
- Single item (trivial)

### Common Mistakes / Traps
1. **n too large for bitmask** -- 2^n states; n=20 is ~1M (OK), n=25 is ~33M (borderline), n=30 is ~1B (too much)
2. **Iterating bits wrong** -- to check if bit i is set: `mask & (1 << i)`. To set bit i: `mask | (1 << i)`
3. **Not using memoization/tabulation** -- naive recursion without memo is exponential
4. **Wrong base case** -- dp[0] (empty mask) usually has a defined base value (0 cost, 1 way, etc.)
5. **Confusing which dimension to bitmask** -- in "hats to people," bitmask the SMALLER dimension (people, not hats)

---

## PATTERN 25: GREEDY PATTERNS

### Sub-variants
- **Interval scheduling** (maximize non-overlapping intervals)
- **Activity selection** (sort by end time, greedily pick)
- **Jump game** (track farthest reachable position)
- **Huffman coding** (greedy + priority queue)
- **Fractional knapsack** (sort by value/weight ratio)
- **Task scheduling** (greedy + cooldown)

### Core Idea / Recognition Trigger
At each step, make the LOCALLY OPTIMAL choice, and it leads to a GLOBALLY OPTIMAL solution.
The trigger: the problem has "greedy choice property" (local optimal doesn't block global
optimal) and "optimal substructure." Common signals: "minimum number of," "maximum number of,"
interval/scheduling problems, "can you reach the end?"

**Sources:** NeetCode (Greedy section), Striver A2Z (Step 12 -- Greedy Algorithms),
Sean Prashad (Greedy pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Jump Game | 55 | Reachability | Array | Track farthest reachable index greedily |
| 2 | Jump Game II | 45 | Min jumps (BFS-like greedy) | Array | Track current range end and next range end |
| 3 | Gas Station | 134 | Circular greedy | Array | If total gas >= total cost, solution exists; reset start when deficit |
| 4 | Non-overlapping Intervals | 435 | Interval scheduling | Array of Intervals | Sort by end time, greedily pick non-overlapping |
| 5 | Task Scheduler | 621 | Cooldown scheduling | Array + Heap | Most frequent task determines idle slots |
| 6 | Candy | 135 | Two-pass greedy | Array | Left-to-right pass then right-to-left pass |
| 7 | Minimum Number of Platforms | -- | Sweep line | Array of Intervals | Sort arrivals and departures, count concurrent |
| 8 | Assign Cookies | 455 | Sort + two pointers | Array | Sort children by greed, cookies by size; match greedily |
| 9 | Minimum Number of Arrows to Burst Balloons | 452 | Interval overlap | Array of Intervals | Sort by end, one arrow per non-overlapping group |
| 10 | Partition Labels | 763 | Greedy intervals | String | Track last occurrence of each char; extend partition |

### Edge Cases
- Single element / empty input
- All identical elements
- Greedy fails -- recognize when DP is needed instead (e.g., 0/1 Knapsack is NOT greedy)
- Ties in sorting (break ties consistently -- problem-specific)

### Common Mistakes / Traps
1. **Applying greedy to problems that require DP** -- Coin Change with arbitrary denominations is NOT greedy (counterexample: coins [1,3,4], amount 6: greedy gives 4+1+1=3 coins, optimal is 3+3=2 coins)
2. **Wrong sorting criterion** -- interval scheduling: sort by END time (not start time)
3. **Not being able to PROVE greedy correctness** -- interviewers may ask for the exchange argument
4. **Jump Game II: not recognizing the BFS/level structure** -- each "level" is the range reachable in one jump
5. **Candy: only doing one pass** -- need TWO passes (left-to-right and right-to-left) to handle both neighbors

---

## PATTERN 26: DIVIDE AND CONQUER

### Sub-variants
- **Merge Sort applications** (count inversions, merge k lists)
- **Quick Select** (kth element in O(n) average)
- **Binary search** (inherently divide and conquer)
- **Tree construction** (build from traversals)
- **Closest pair of points** (geometric D&C)

### Core Idea / Recognition Trigger
SPLIT the problem into independent subproblems, SOLVE each recursively, COMBINE results.
The trigger: the problem can be split at a midpoint, solved independently on each half, and
merged. Often gives O(n log n) time.

**Sources:** NeetCode (various sections), Striver A2Z (Step 5 -- Sorting for merge sort applications),
LeetCode Study Plan (Divide and Conquer).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Merge Sort | -- | Classic D&C | Array | Split, sort halves, merge |
| 2 | Count of Inversions | -- | Merge sort application | Array | Count while merging: if left[i] > right[j], all remaining left elements are inversions |
| 3 | Merge K Sorted Lists | 23 | Pairwise merge | Linked Lists | Divide lists into pairs, merge each pair, repeat |
| 4 | Kth Largest Element in an Array | 215 | Quick Select | Array | Partition around pivot, recurse on one side only |
| 5 | Construct BT from Preorder and Inorder | 105 | Tree construction | Binary Tree | Root from preorder splits inorder into left/right subtrees |
| 6 | Sort an Array | 912 | Merge sort / Quick sort | Array | Classic D&C sorting algorithms |
| 7 | Maximum Subarray | 53 | D&C solution (not Kadane's) | Array | Max of: left half, right half, or crossing subarray |
| 8 | Search a 2D Matrix II | 240 | D&C / staircase search | Matrix | Start from top-right; eliminate row or column each step |
| 9 | Median of Two Sorted Arrays | 4 | Binary search D&C | Two Arrays | Partition arrays to find combined median |

### Edge Cases
- Single element (base case of recursion)
- Empty input
- Already sorted (merge sort still O(n log n); quicksort degrades to O(n^2) with bad pivot)
- All duplicates (quicksort partition can be tricky)

### Common Mistakes / Traps
1. **Quick Select worst case** -- O(n^2) with bad pivots; use random pivot or median of medians
2. **Merge sort: not stable if implemented incorrectly** -- use `<=` not `<` when merging to maintain stability
3. **Count inversions: modifying the merge step wrong** -- count += mid - i + 1 when left[i] > right[j] (all remaining left elements form inversions with right[j])
4. **Not recognizing D&C** -- many tree problems are D&C (split at root into left/right subtrees)
5. **Excessive space from creating new arrays** -- use index-based approach to avoid O(n log n) extra space

---

## PATTERN 27: BIT MANIPULATION PATTERNS

### Sub-variants
- **XOR tricks** (find missing/duplicate, single number)
- **Bit counting** (Brian Kernighan's algorithm, lookup table)
- **Bit masking** (check/set/clear specific bits)
- **Powers of 2** (n & (n-1) == 0)
- **Bitwise DP** (see Pattern 24)

### Core Idea / Recognition Trigger
The problem involves finding unique elements, checking properties related to binary representation,
or optimizing with bitwise operations. The trigger: "single number," "missing number," "power of 2,"
"hamming distance," "complement," or any problem where XOR/AND/OR can replace loops.

**Sources:** NeetCode (Bit Manipulation section), Striver A2Z (Step 8 -- Bit Manipulation),
Sean Prashad (Bit Manipulation pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Single Number | 136 | XOR cancellation | Array | a ^ a = 0; XOR all elements, unique remains |
| 2 | Single Number II | 137 | Bit counting mod 3 | Array | Count each bit position mod 3 |
| 3 | Single Number III | 260 | XOR + bit partitioning | Array | XOR all -> get diff bits -> partition by one diff bit |
| 4 | Number of 1 Bits | 191 | Brian Kernighan's | Number | n &= (n-1) clears lowest set bit; count iterations |
| 5 | Counting Bits | 338 | Bit DP | Array | dp[i] = dp[i >> 1] + (i & 1), or dp[i] = dp[i & (i-1)] + 1 |
| 6 | Missing Number | 268 | XOR with indices | Array | XOR all values with all indices 0..n; missing number remains |
| 7 | Reverse Bits | 190 | Bit-by-bit construction | Number | Extract LSB, shift result left, repeat 32 times |
| 8 | Power of Two | 231 | n & (n-1) == 0 | Number | Exactly one bit set means power of 2 |
| 9 | Sum of Two Integers | 371 | Bit-level addition | Number | a ^ b = sum without carry; (a & b) << 1 = carry; repeat |
| 10 | Maximum XOR of Two Numbers | 421 | Bitwise Trie | Array + Trie | Greedily pick opposite bits from MSB to LSB |

### Edge Cases
- Negative numbers (two's complement representation)
- Zero (special case for many bit problems)
- Integer overflow (be careful with left shifts on 32-bit numbers)
- Language-specific: Python has arbitrary precision integers (no overflow, but no fixed-width bits)

### Common Mistakes / Traps
1. **Signed vs unsigned interpretation** -- shifting negative numbers is implementation-defined in C/C++; Python handles it differently
2. **XOR does not help with three duplicates** -- Single Number II needs a different approach (bit counting mod 3)
3. **Forgetting n=0 for power of two** -- 0 & (0-1) = 0, but 0 is NOT a power of 2
4. **Sum of Two Integers: infinite loop with negative numbers in Python** -- Python integers have no fixed width; need masking to 32 bits
5. **Maximum XOR: not understanding the trie approach** -- build a trie of all numbers bit by bit, then for each number greedily choose the opposite bit path

---

## PATTERN 28: TRIE PATTERNS

### Sub-variants
- **Standard Trie** (insert, search, startsWith)
- **Bitwise Trie** (for XOR problems)
- **Trie + DFS/Backtracking** (word search on grid)
- **Trie for autocomplete** (prefix-based retrieval)

### Core Idea / Recognition Trigger
You need to efficiently search/match PREFIXES, or search for words with common prefixes,
or find XOR-optimal pairs. The trigger: "prefix search," "word dictionary with wildcard,"
"autocomplete," "maximum XOR of pairs."

**Sources:** NeetCode (Tries section), Striver A2Z (Step 8 -- Tries),
Sean Prashad (Trie pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Implement Trie (Prefix Tree) | 208 | Standard Trie | Trie | insert, search, startsWith in O(m) per operation |
| 2 | Design Add and Search Words DS | 211 | Trie + wildcard DFS | Trie | '.' matches any character; DFS through all children on '.' |
| 3 | Word Search II | 212 | Trie + grid backtracking | Trie + Grid | Build trie from word list; DFS grid against trie simultaneously |
| 4 | Maximum XOR of Two Numbers | 421 | Bitwise Trie | Trie + Array | Insert all numbers bit by bit; greedily maximize XOR |
| 5 | Replace Words | 648 | Prefix replacement | Trie + String | Insert roots into trie; for each word, find shortest prefix match |
| 6 | Map Sum Pairs | 677 | Trie with values | Trie | Store values at nodes; sum all values with given prefix |
| 7 | Palindrome Pairs | 336 | Trie for reverse lookup | Trie + String | Insert reversed words into trie; search for palindrome completions |

### Edge Cases
- Empty string (usually represents the root or a valid empty word)
- Single character words
- Words that are prefixes of other words (mark end-of-word explicitly)
- Very long words (trie depth = word length)
- Unicode/special characters (usually not tested, but be aware)

### Common Mistakes / Traps
1. **Not marking end-of-word** -- "apple" and "app": without end-of-word marker, search("app") incorrectly returns True
2. **Word Search II: not pruning the trie** -- after finding a word, remove it from trie to avoid duplicates and speed up search
3. **Memory overhead** -- each trie node has up to 26 children; for large dictionaries, this can be significant
4. **Wildcard search: exploring all 26 children on '.'** -- this is correct but can be slow; no way around it
5. **Bitwise trie: wrong bit order** -- must process from MSB to LSB (bit 31 down to bit 0) for greedy XOR to work

---

## PATTERN 29: HEAP / TOP-K PATTERNS

### Sub-variants
- **Top-K elements** (kth largest, k most frequent)
- **Two-heap** (median finding)
- **K-way merge** (merge k sorted streams)
- **Greedy + Heap scheduling** (task scheduler, reorganize string)
- **Lazy deletion heap** (mark deleted, skip when popping)

### Core Idea / Recognition Trigger
You need the K LARGEST/SMALLEST elements, or need to repeatedly extract the min/max, or need
to maintain a running median. The trigger: "top K," "kth largest," "merge K sorted," "median
of stream," "schedule tasks by frequency."

**Sources:** Fahim ul Haq's "14 Patterns" (Pattern #13 -- Top K Elements, Pattern #14 -- K-way Merge),
NeetCode (Heap / Priority Queue section), Striver A2Z (Step 7 -- Heaps),
Sean Prashad (Heap pattern).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Kth Largest Element in an Array | 215 | Top-K (min-heap of size K) | Array + Heap | Maintain min-heap of K largest; root = kth largest |
| 2 | Top K Frequent Elements | 347 | Frequency + Top-K | Array + Heap | Count frequencies, then top-K by frequency |
| 3 | Find Median from Data Stream | 295 | Two-heap technique | Two Heaps | Max-heap for lower half, min-heap for upper half |
| 4 | Merge K Sorted Lists | 23 | K-way merge | Linked Lists + Heap | Min-heap holds one node from each list |
| 5 | K Closest Points to Origin | 973 | Top-K by distance | Array + Heap | Max-heap of size K (or min-heap of all + pop K) |
| 6 | Task Scheduler | 621 | Greedy + max-heap | Array + Heap | Always schedule most frequent task; track cooldown |
| 7 | Reorganize String | 767 | Greedy + max-heap | String + Heap | Always place most frequent character; alternate |
| 8 | Kth Smallest Element in a Sorted Matrix | 378 | K-way merge on matrix | Matrix + Heap | Treat each row as a sorted list; merge with min-heap |
| 9 | Ugly Number II | 264 | Multi-pointer merge | Number + Heap | Merge 3 streams: n*2, n*3, n*5 |
| 10 | Smallest Range Covering Elements from K Lists | 632 | K-way merge + sliding window | K Lists + Heap | Min-heap of one element per list; track range |

### Edge Cases
- K = 0 (usually invalid or return empty)
- K = n (return all elements)
- K > n (invalid -- check constraints)
- All elements equal (any K elements are valid)
- Stream problems (handle before K elements have arrived)

### Common Mistakes / Traps
1. **Using max-heap when min-heap is needed (and vice versa)** -- Top-K LARGEST uses min-heap of size K (counterintuitive); Top-K SMALLEST uses max-heap of size K
2. **Two-heap median: not balancing correctly** -- max-heap size should equal or exceed min-heap size by at most 1
3. **Python heapq is a MIN-heap** -- for max-heap, negate values: `heappush(heap, -val)`
4. **K-way merge: pushing None/expired nodes** -- always check if the popped node has a next before pushing
5. **Not considering QuickSelect alternative** -- for kth element, QuickSelect is O(n) average vs O(n log k) for heap

---

## PATTERN 30: GRAPH -- SHORTEST PATH PATTERNS

### Sub-variants
- **Dijkstra's algorithm** (single-source, non-negative weights)
- **Bellman-Ford** (single-source, handles negative weights)
- **Floyd-Warshall** (all-pairs shortest paths)
- **0-1 BFS** (edge weights are 0 or 1, use deque)
- **A* search** (heuristic-guided Dijkstra)
- **SPFA** (Bellman-Ford with queue optimization)

### Core Idea / Recognition Trigger
You need the SHORTEST PATH in a WEIGHTED graph. The trigger: "minimum cost path," "cheapest
flight," "shortest path with weights," "network delay." Choose algorithm by: non-negative
weights -> Dijkstra; negative weights -> Bellman-Ford; all-pairs -> Floyd-Warshall;
0/1 weights -> 0-1 BFS.

**Sources:** NeetCode (Graphs -- Advanced section), Striver A2Z (Step 11 -- Shortest Path Algorithms),
LeetCode Study Plan (Graph Theory II).

### Representative Problems

| # | Problem | LC # | Sub-variant | Data Structure | Why This Pattern |
|---|---------|------|-------------|----------------|-----------------|
| 1 | Network Delay Time | 743 | Dijkstra (single-source) | Weighted Graph | Min time for signal to reach all nodes |
| 2 | Cheapest Flights Within K Stops | 787 | Bellman-Ford with K iterations | Weighted Graph | Relax edges at most K+1 times |
| 3 | Path with Maximum Probability | 1514 | Modified Dijkstra (maximize) | Weighted Graph | Dijkstra but maximize probability (use max-heap) |
| 4 | Path with Minimum Effort | 1631 | Dijkstra on grid | Grid/Graph | Minimize max absolute difference along path |
| 5 | Swim in Rising Water | 778 | Dijkstra / binary search + BFS | Grid/Graph | Minimize the max elevation along path (minimax) |
| 6 | Shortest Path in Weighted Graph | -- | Classic Dijkstra | Weighted Graph | Template: priority queue + relaxation |
| 7 | Find the City With the Smallest Number of Neighbors at a Threshold Distance | 1334 | Floyd-Warshall or Dijkstra x n | Weighted Graph | All-pairs shortest paths, then filter |
| 8 | Minimum Cost to Make at Least One Valid Path in a Grid | 1368 | 0-1 BFS | Grid/Graph | Moving in arrow direction = cost 0; other directions = cost 1 |
| 9 | Shortest Path with Alternating Colors | 1129 | BFS with state | Graph | State = (node, last_color); BFS through states |
| 10 | Number of Ways to Arrive at Destination | 1976 | Dijkstra + counting | Weighted Graph | Standard Dijkstra + count paths with equal distance |

### Edge Cases
- Disconnected graph (some nodes unreachable -- return -1 or infinity)
- Negative weight cycles (Bellman-Ford detects them; Dijkstra gives wrong answers)
- Self-loops with weight 0 (can cause infinite loops if not handled)
- Multiple edges between same pair of nodes (keep the minimum weight one)
- Single node graph (distance to itself is 0)

### Common Mistakes / Traps
1. **Using Dijkstra with negative weights** -- WRONG. Dijkstra assumes non-negative weights. Use Bellman-Ford instead
2. **Not using a visited set with Dijkstra** -- without it, same node can be processed multiple times (TLE for dense graphs)
3. **Bellman-Ford: wrong number of iterations** -- need V-1 iterations to find shortest paths; Kth iteration for K-stop constraint
4. **Cheapest Flights: using Dijkstra instead of Bellman-Ford** -- Dijkstra doesn't respect the K-stop constraint correctly
5. **Floyd-Warshall: wrong loop order** -- the intermediate node k MUST be the outermost loop: for k, for i, for j
6. **0-1 BFS: using regular BFS instead of deque** -- 0-cost edges go to FRONT of deque; 1-cost edges go to BACK

---
---

## CROSS-PATTERN REFERENCE: WHICH PATTERN FOR WHICH TRIGGER?

| If you see this in the problem... | Think about this pattern... |
|---|---|
| "Sorted array" + "find pair/target" | Two Pointers (opposite direction) |
| "Contiguous subarray/substring" + "optimize" | Sliding Window or Kadane's |
| "Sorted" + "find element" + "O(log n)" | Binary Search |
| "Minimum/maximum value such that condition holds" | Binary Search on Answer |
| "Cycle detection" or "middle of list" | Fast/Slow Pointers |
| "Range sum query" or "subarray sum = K" | Prefix Sum + HashMap |
| "Next greater/smaller element" | Monotonic Stack |
| "Sliding window max/min" | Monotonic Deque |
| "Shortest path (unweighted)" or "level by level" | BFS |
| "Generate all" or "find all valid" | DFS/Backtracking |
| "Prerequisites" or "dependency order" | Topological Sort |
| "Are X and Y connected?" or "dynamic grouping" | Union Find |
| "Maximum contiguous subarray sum/product" | Kadane's Algorithm |
| "Overlapping intervals" or "meetings" | Merge Intervals |
| "Reverse/reorder a linked list" | Linked List Manipulation |
| "BST sorted order" or "kth element in BST" | Inorder Traversal |
| "Bottom-up tree computation (height, diameter)" | Postorder DFS |
| "Select items, each used once, reach target" | 0/1 Knapsack DP |
| "Items reusable, reach target" | Unbounded Knapsack DP |
| "Compare two strings character by character" | LCS family DP |
| "Longest increasing subsequence" | LIS DP |
| "Split sequence optimally at every point" | MCM / Interval DP |
| "Grid, move right/down, count paths or min cost" | Grid DP |
| "Divide into K groups optimally" | Partition DP |
| "Tree + optimal value at each node" | DP on Trees |
| "dp[i] depends on dp[i-1], dp[i-2]" | Fibonacci family DP |
| "n <= 20, track which items used" | Bitmask DP |
| "Locally optimal = globally optimal" | Greedy |
| "Split into halves, solve, merge" | Divide and Conquer |
| "Find unique/missing using XOR" | Bit Manipulation |
| "Prefix search" or "word dictionary" | Trie |
| "Top K" or "kth largest/smallest" or "running median" | Heap |
| "Shortest path (weighted, non-negative)" | Dijkstra |
| "Shortest path (weighted, negative ok)" | Bellman-Ford |
| "All-pairs shortest path" | Floyd-Warshall |

---

## ADITYA VERMA DP PATTERN MAP (Complete)

Aditya Verma organizes ALL of DP into these parent patterns. Every DP problem reduces to one:

```
DP (Aditya Verma)
|
|-- 1. 0/1 Knapsack (Pattern 15)
|   |-- Subset Sum
|   |-- Equal Sum Partition
|   |-- Count of Subset Sum
|   |-- Minimum Subset Sum Difference
|   |-- Target Sum
|   |-- Number of Subsets with Given Difference
|
|-- 2. Unbounded Knapsack (Pattern 16)
|   |-- Rod Cutting
|   |-- Coin Change (min coins)
|   |-- Coin Change II (count ways)
|   |-- Maximum Ribbon Cut
|
|-- 3. LCS - Longest Common Subsequence (Pattern 17)
|   |-- LCS
|   |-- Longest Common Substring
|   |-- Print LCS
|   |-- Shortest Common Supersequence
|   |-- Print SCS
|   |-- Minimum Insertions/Deletions to Transform
|   |-- Longest Palindromic Subsequence
|   |-- Minimum Deletions to Make Palindrome
|   |-- Longest Repeating Subsequence
|   |-- Sequence Pattern Matching (Is Subsequence)
|
|-- 4. MCM - Matrix Chain Multiplication (Pattern 19)
|   |-- MCM
|   |-- Palindrome Partitioning
|   |-- Boolean Parenthesization
|   |-- Scramble String
|   |-- Egg Drop Problem
|
|-- 5. DP on Trees (Pattern 22)
|   |-- Diameter of Binary Tree
|   |-- Maximum Path Sum (Node to Node)
|   |-- Maximum Path Sum (Leaf to Leaf)
|
|-- 6. LIS - Longest Increasing Subsequence (Pattern 18)
    |-- LIS
    |-- Number of LIS
```

---

## NEETCODE ROADMAP PATTERN MAP (18 Categories)

```
NeetCode Roadmap
|
|-- Arrays & Hashing (Pattern 5: Prefix Sum, Pattern 11: Kadane's)
|-- Two Pointers (Pattern 1)
|-- Sliding Window (Pattern 2)
|-- Stack (Pattern 6: Monotonic Stack)
|-- Binary Search (Pattern 3)
|-- Linked List (Pattern 4: Fast/Slow, Pattern 13: LL Manipulation)
|-- Trees (Pattern 7: BFS, Pattern 14: Tree Traversals, Pattern 22: DP on Trees)
|-- Tries (Pattern 28)
|-- Heap / Priority Queue (Pattern 29)
|-- Backtracking (Pattern 8)
|-- Graphs (Pattern 7: BFS, Pattern 9: Topo Sort, Pattern 10: Union Find)
|-- Advanced Graphs (Pattern 30: Shortest Path)
|-- 1-D DP (Pattern 23: Fibonacci, Pattern 18: LIS, Pattern 11: Kadane's)
|-- 2-D DP (Pattern 15-17: Knapsack/LCS, Pattern 20: Grid DP)
|-- Greedy (Pattern 25)
|-- Intervals (Pattern 12)
|-- Math & Geometry
|-- Bit Manipulation (Pattern 27)
```

---

## FAHIM UL HAQ "14 PATTERNS" MAP

From the famous "14 Patterns to Ace Any Coding Interview" (Educative.io):

```
14 Patterns (Fahim ul Haq)           -> This Taxonomy
|
|-- 1. Sliding Window                -> Pattern 2
|-- 2. Two Pointers                  -> Pattern 1
|-- 3. Fast & Slow Pointers          -> Pattern 4
|-- 4. Merge Intervals               -> Pattern 12
|-- 5. Cyclic Sort                   -> (unique -- find missing/duplicate in [1..n] range)
|-- 6. In-place Reversal of LL       -> Pattern 13
|-- 7. Tree BFS                      -> Pattern 7
|-- 8. Tree DFS                      -> Pattern 8 / Pattern 14
|-- 9. Two Heaps                     -> Pattern 29 (Two-heap sub-variant)
|-- 10. Subsets                      -> Pattern 8 (Backtracking)
|-- 11. Modified Binary Search       -> Pattern 3
|-- 12. Topological Sort             -> Pattern 9
|-- 13. Top K Elements               -> Pattern 29
|-- 14. K-way Merge                  -> Pattern 29 (K-way merge sub-variant)
```

**Note:** Fahim's Pattern 5 (Cyclic Sort) is a niche pattern for problems where values are
in a known range [1, n]. Key problems: Find Missing Number (LC 268), Find All Duplicates (LC 442),
Find All Missing Numbers (LC 448), First Missing Positive (LC 41). We did not dedicate a
separate section to it because most of these problems also have XOR or HashSet solutions.

---

## SEAN PRASHAD'S PATTERN CATEGORIES MAP

```
Sean Prashad LeetCode Patterns       -> This Taxonomy
|
|-- Arrays                           -> Patterns 1, 2, 5, 11
|-- Backtracking                     -> Pattern 8
|-- Binary Search                    -> Pattern 3
|-- Bit Manipulation                 -> Pattern 27
|-- Bucket Sort                      -> (technique, not pattern)
|-- Design                           -> Pattern 13 (LRU Cache), Pattern 28 (Trie)
|-- Dynamic Programming              -> Patterns 15-24
|-- Fast & Slow Pointers             -> Pattern 4
|-- Graph                            -> Patterns 7, 8, 9, 10, 30
|-- Greedy                           -> Pattern 25
|-- Heap                             -> Pattern 29
|-- In-place Reversal of LL          -> Pattern 13
|-- Intervals                        -> Pattern 12
|-- Linked List                      -> Patterns 4, 13
|-- Math                             -> (not pattern-based)
|-- Matrix                           -> Patterns 3, 7, 20
|-- Merge Intervals                  -> Pattern 12
|-- Modified Binary Search           -> Pattern 3
|-- Monotonic Stack                  -> Pattern 6
|-- Sliding Window                   -> Pattern 2
|-- Stack                            -> Pattern 6
|-- Topological Sort                 -> Pattern 9
|-- Tree -- BFS                      -> Pattern 7
|-- Tree -- DFS                      -> Patterns 8, 14
|-- Trie                             -> Pattern 28
|-- Two Pointers                     -> Pattern 1
|-- Union Find                       -> Pattern 10
```

---

## STRIVER A2Z SHEET MAPPING

```
Striver A2Z DSA Sheet                -> This Taxonomy
|
|-- Step 1: Learn the basics         -> (fundamentals, not pattern)
|-- Step 2: Sorting                  -> Pattern 26 (D&C for merge/quick sort)
|-- Step 3: Arrays (Easy/Med/Hard)   -> Patterns 1, 5, 11
|-- Step 4: Binary Search            -> Pattern 3
|-- Step 5: Strings                  -> Patterns 17, 28
|-- Step 6: Linked List              -> Patterns 4, 13
|-- Step 7: Recursion & Backtracking -> Pattern 8
|-- Step 8: Bit Manipulation         -> Pattern 27
|-- Step 9: Stack & Queue            -> Pattern 6
|-- Step 10: Sliding Window & Two Pointer -> Patterns 1, 2
|-- Step 11: Heaps                   -> Pattern 29
|-- Step 12: Greedy                  -> Pattern 25
|-- Step 13: Binary Trees & BST      -> Patterns 7, 14, 22
|-- Step 14: Dynamic Programming     -> Patterns 15-24
|   |-- DP on Subsequences           -> Patterns 15, 16 (Knapsack)
|   |-- DP on Strings                -> Pattern 17 (LCS)
|   |-- DP on LIS                    -> Pattern 18
|   |-- DP on Partition/MCM          -> Patterns 19, 21
|   |-- DP on Stocks                 -> (state machine DP -- buy/sell)
|   |-- DP on Grids                  -> Pattern 20
|-- Step 15: Graphs                  -> Patterns 7, 8, 9, 10, 30
|   |-- BFS / DFS                    -> Patterns 7, 8
|   |-- Topo Sort                    -> Pattern 9
|   |-- Shortest Path                -> Pattern 30
|   |-- MST (Prim's, Kruskal's)     -> (uses Pattern 10: Union Find)
|   |-- Disjoint Set                 -> Pattern 10
```

---

## BONUS PATTERN: DP ON STOCKS (Striver's Addition)

Not in the original 30 but important enough to mention. Striver dedicates a separate section.

### Sub-variants
- **Buy and sell once** (LC 121 -- simple, not even DP)
- **Buy and sell unlimited times** (LC 122)
- **Buy and sell with at most 2 transactions** (LC 123)
- **Buy and sell with at most K transactions** (LC 188)
- **Buy and sell with cooldown** (LC 309)
- **Buy and sell with transaction fee** (LC 714)

### Core Idea
State machine DP: at each day you are in one of the states (holding, not holding, cooldown).
Transitions define what you can do next (buy, sell, hold, cooldown).

### Recognition Trigger
"Buy and sell stock" -- literally. These are their own family.

---

## FINAL NOTES

1. **Many problems belong to MULTIPLE patterns.** Trapping Rain Water (LC 42) is Two Pointers OR
   Monotonic Stack. Word Search II (LC 212) is Trie + Backtracking. This is expected -- patterns
   overlap, and recognizing that a problem can be solved multiple ways is a strength.

2. **The order to learn patterns** (recommended):
   - Foundation: Two Pointers -> Sliding Window -> Binary Search -> Prefix Sum
   - Intermediate: DFS/BFS -> Backtracking -> Monotonic Stack -> Kadane's -> Merge Intervals
   - Advanced: DP families (Fibonacci -> Knapsack -> LCS -> LIS -> MCM -> Trees -> Bitmask)
   - Expert: Topological Sort -> Union Find -> Trie -> Shortest Path -> Divide and Conquer

3. **Aditya Verma's hierarchy is the gold standard for DP.** If you can identify which of his
   6 parent patterns a problem falls into, you have the recursion template. The rest is adaptation.

4. **The "trigger" is the most valuable thing to memorize.** In an interview, you have 3-5 minutes
   to identify the pattern. The trigger phrases in each section above are your weapon.
