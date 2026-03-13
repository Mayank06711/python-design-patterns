# DSA Interview Questions - Master List (155 Questions)

> **Language:** C++ | **Target:** Google/Amazon/Meta | **Source:** 2024-2025 interview data
> **Your profile:** Strong arrays/trees/sorting | Weak: DP intuition, Recursion | Never done: Graphs
>
> Detailed breakdowns available in:
> - [dp_interview_questions_2024_2025.md](dp_interview_questions_2024_2025.md) (30 DP questions with intuition tips)
> - [graph_interview_questions.md](graph_interview_questions.md) (20 graph questions from scratch)
> - [DSA_QUESTION_LIST.md](DSA_QUESTION_LIST.md) (Trees, Heaps, Backtracking, Greedy, Tries)

---

## Progress Tracker

| # | Category | Questions | Your Focus | Status |
|---|----------|-----------|------------|--------|
| 1 | Arrays, Two Pointers, Sliding Window | 15 | Speed drill (you're strong) | [ ] |
| 2 | Binary Search | 10 | Tricky applications | [ ] |
| 3 | Linked List | 12 | Classic patterns | [ ] |
| 4 | Stacks, Queues, Monotonic Stack | 10 | Pattern building | [ ] |
| 5 | Sorting Algorithms | 8 | Application problems | [ ] |
| 6 | Trees & BST | 15 | Push to hard | [ ] |
| 7 | Heaps / Priority Queue | 8 | Top-K mastery | [ ] |
| 8 | Recursion & Backtracking | 12 | **INTUITION BUILDING** | [ ] |
| 9 | Greedy | 8 | Proof-based thinking | [ ] |
| 10 | Dynamic Programming | 30 | **HEAVY FOCUS** | [ ] |
| 11 | Graphs | 20 | **LEARN FROM SCRATCH** | [ ] |
| 12 | Bit Manipulation + Tries | 5 | Must-knows only | [ ] |
| | **TOTAL** | **153** | | |

---

## 1. Arrays, Two Pointers & Sliding Window (15 Questions)

> You're strong here. Treat these as speed drills -- solve under time pressure.

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 1 | Two Sum | 1 | E | Hash map complement lookup | Amazon, Google, Meta |
| 2 | Move Zeroes | 283 | E | Read/write two pointers | Meta, Amazon |
| 3 | Squares of a Sorted Array | 977 | E | Two pointers from both ends | Amazon, Google |
| 4 | Two Sum II (Sorted) | 167 | M | Converging two pointers | Amazon, Google |
| 5 | 3Sum | 15 | M | Sort + two pointers + skip dupes | Meta, Google, Amazon |
| 6 | Container With Most Water | 11 | M | Greedy two-pointer shrink shorter side | Amazon, Google, Meta |
| 7 | Product of Array Except Self | 238 | M | Prefix/suffix without division | Meta, Amazon, Google |
| 8 | Maximum Subarray (Kadane's) | 53 | M | Local vs global max DP | Amazon, Google, Meta |
| 9 | Subarray Sum Equals K | 560 | M | Prefix sum + hash map | Meta, Google, Amazon |
| 10 | Merge Intervals | 56 | M | Sort by start + greedy merge | Google, Meta, Amazon |
| 11 | Maximum Product Subarray | 152 | M | Track min AND max (negatives flip) | Amazon, Google |
| 12 | Next Permutation | 31 | M | Lexicographic ordering algorithm | Google, Meta |
| 13 | Rotate Array | 189 | M | Three-reverse trick | Amazon, Meta |
| 14 | Trapping Rain Water | 42 | H | Two-pointer left-max/right-max OR monotonic stack | Amazon, Google, Meta |
| 15 | Sliding Window Maximum | 239 | H | Monotonic decreasing deque | Amazon, Google, Meta |

---

## 2. Binary Search (10 Questions)

> Beyond basic search -- these test tricky applications that interviewers love.

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 16 | Binary Search | 704 | E | Vanilla binary search (warm-up) | Amazon, Google |
| 17 | Search Insert Position | 35 | E | Lower bound / bisect_left | Amazon, Google |
| 18 | Find First and Last Position | 34 | M | Two binary searches (left + right bound) | Meta, Amazon, Google |
| 19 | Search in Rotated Sorted Array | 33 | M | Identify sorted half, then decide | Amazon, Google, Meta |
| 20 | Find Minimum in Rotated Sorted Array | 153 | M | Binary search on rotated array | Amazon, Google |
| 21 | Search a 2D Matrix | 74 | M | Treat 2D as 1D sorted array | Amazon, Google |
| 22 | Koko Eating Bananas | 875 | M | Binary search on answer space | Google, Amazon |
| 23 | Find Peak Element | 162 | M | Binary search with gradient | Meta, Google |
| 24 | Median of Two Sorted Arrays | 4 | H | Binary search on partition | Amazon, Google, Meta |
| 25 | Split Array Largest Sum | 410 | H | Binary search + greedy validation | Google, Amazon |

---

## 3. Linked List (12 Questions)

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 26 | Reverse Linked List | 206 | E | 3-pointer swap (prev/curr/next) | Amazon, Google, Meta |
| 27 | Merge Two Sorted Lists | 21 | E | Dummy head + compare-and-advance | Amazon, Meta, Google |
| 28 | Linked List Cycle | 141 | E | Floyd's slow/fast (tortoise & hare) | Amazon, Google |
| 29 | Intersection of Two Linked Lists | 160 | E | Switch-to-other-head trick | Amazon, Meta |
| 30 | Palindrome Linked List | 234 | E | Find mid + reverse half + compare | Amazon, Meta, Google |
| 31 | Linked List Cycle II | 142 | M | Floyd's extended -- find cycle start | Amazon, Google, Meta |
| 32 | Remove Nth Node From End | 19 | M | Two pointers with N-gap | Amazon, Meta, Google |
| 33 | Add Two Numbers | 2 | M | Digit-by-digit with carry | Amazon, Google, Meta |
| 34 | Copy List with Random Pointer | 138 | M | Hash map clone OR interleaving trick | Amazon, Meta, Google |
| 35 | Reorder List | 143 | M | Find mid + reverse + interleave | Meta, Amazon, Google |
| 36 | LRU Cache | 146 | M | Doubly linked list + hash map | Amazon, Google, Meta |
| 37 | Reverse Nodes in k-Group | 25 | H | Reverse sublists with careful pointers | Amazon, Google, Meta |

---

## 4. Stacks, Queues & Monotonic Stack (10 Questions)

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 38 | Valid Parentheses | 20 | E | Stack for matching pairs | Amazon, Google, Meta |
| 39 | Min Stack | 155 | M | Auxiliary stack for running min | Amazon, Google, Meta |
| 40 | Next Greater Element I | 496 | E | Monotonic decreasing stack + hash | Amazon, Google |
| 41 | Daily Temperatures | 739 | M | Monotonic stack storing indices | Amazon, Meta, Google |
| 42 | Online Stock Span | 901 | M | Streaming monotonic stack | Amazon, Google |
| 43 | Next Greater Element II | 503 | M | Monotonic stack on circular array (2N) | Amazon, Google |
| 44 | Evaluate Reverse Polish Notation | 150 | M | Stack-based expression evaluation | Amazon, Google, Meta |
| 45 | Largest Rectangle in Histogram | 84 | H | Monotonic increasing stack | Amazon, Google, Meta |
| 46 | Maximal Rectangle | 85 | H | Histogram per row + LC 84 | Google, Amazon, Meta |
| 47 | Trapping Rain Water (Stack) | 42 | H | Monotonic decreasing stack approach | Amazon, Google, Meta |

---

## 5. Sorting Algorithm Problems (8 Questions)

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 48 | Merge Sorted Array | 88 | E | Three-pointer merge from end | Amazon, Meta |
| 49 | Sort Colors (Dutch National Flag) | 75 | M | Three-way partition in one pass | Amazon, Meta, Google |
| 50 | Kth Largest Element | 215 | M | Quickselect O(n) avg | Amazon, Google, Meta |
| 51 | Top K Frequent Elements | 347 | M | Bucket sort / heap | Amazon, Google, Meta |
| 52 | Sort List | 148 | M | Merge sort on linked list | Amazon, Google |
| 53 | Merge K Sorted Lists | 23 | H | Min-heap of K / divide-and-conquer | Amazon, Google, Meta |
| 54 | Kth Largest in a Stream | 703 | E | Min-heap of size K (online) | Amazon, Google |
| 55 | Merge Intervals | 56 | M | Sort + sweep (also in arrays) | Google, Meta, Amazon |

---

## 6. Trees & BST (15 Questions)

> You're comfortable -- push to hard patterns.

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 56 | Diameter of Binary Tree | 543 | E | Post-order DFS + global max | Amazon, Meta, Google |
| 57 | Binary Tree Level Order Traversal | 102 | M | BFS with queue | Amazon, Meta, Google |
| 58 | Binary Tree Right Side View | 199 | M | BFS last node per level | Meta, Amazon |
| 59 | Lowest Common Ancestor (BT) | 236 | M | Recursive DFS simultaneous search | Meta, Amazon, Google |
| 60 | Lowest Common Ancestor (BST) | 235 | M | BST split-point logic | Meta, Amazon |
| 61 | Validate BST | 98 | M | In-order with bounds / range propagation | Amazon, Meta, Google |
| 62 | Kth Smallest in BST | 230 | M | In-order traversal + early stop | Amazon, Meta, Google |
| 63 | Construct from Preorder & Inorder | 105 | M | Divide-and-conquer + index map | Amazon, Google, Meta |
| 64 | Flatten Binary Tree to Linked List | 114 | M | Reverse post-order / Morris traversal | Amazon, Meta |
| 65 | Count Good Nodes | 1448 | M | Pre-order DFS with running max | Amazon, Google |
| 66 | Vertical Order Traversal | 314 | M | BFS + column indexing + HashMap | Meta, Amazon |
| 67 | Serialize and Deserialize BT | 297 | H | Pre-order encoding + queue reconstruction | Meta, Amazon, Google |
| 68 | Binary Tree Max Path Sum | 124 | H | Post-order, local vs global optimum | Google, Amazon, Meta |
| 69 | Vertical Order (Hard variant) | 987 | H | DFS/BFS + sort by (col, row, val) | Google, Amazon, Meta |
| 70 | Binary Tree Cameras | 968 | H | Greedy post-order, 3-state system | Amazon, Google |

---

## 7. Heaps / Priority Queue (8 Questions)

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 71 | Kth Largest in a Stream | 703 | E | Min-heap of size K | Amazon, Google |
| 72 | Kth Largest Element | 215 | M | Min-heap / Quickselect | Amazon, Meta, Google |
| 73 | Top K Frequent Elements | 347 | M | Min-heap of K + frequency count | Amazon, Meta, Google |
| 74 | K Closest Points to Origin | 973 | M | Max-heap of K, no sqrt needed | Amazon, Meta, Google |
| 75 | Reorganize String | 767 | M | Max-heap greedy placement | Amazon, Google |
| 76 | Task Scheduler | 621 | M | Max-heap + cooldown queue | Amazon, Meta, Google |
| 77 | Find Median from Data Stream | 295 | H | Two-heap (max-heap + min-heap) | Amazon, Google, Meta |
| 78 | Merge K Sorted Lists | 23 | H | Min-heap with K pointers | Amazon, Google, Meta |

---

## 8. Recursion & Backtracking (12 Questions)

> **YOU GET STUCK HERE.** Follow this exact order. Draw decision trees on paper.

### Phase 1: Build the muscle
| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 79 | Subsets | 78 | M | Include/exclude at each index | Amazon, Meta, Google |
| 80 | Subsets II (with dupes) | 90 | M | Sort + skip dupes at same level | Amazon, Google |
| 81 | Permutations | 46 | M | Swap-based or used-array | Amazon, Meta, Google |
| 82 | Combination Sum | 39 | M | Unbounded choice, start-index | Amazon, Meta, Google |

### Phase 2: Apply to strings/grids
| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 83 | Generate Parentheses | 22 | M | Constraint branching (open < n, close < open) | Amazon, Meta, Google |
| 84 | Letter Combinations of Phone | 17 | M | Multi-way branching per digit | Amazon, Meta, Google |
| 85 | Palindrome Partitioning | 131 | M | Partition + palindrome check | Amazon, Google, Meta |
| 86 | Word Search | 79 | M | Grid DFS + visited + backtrack | Amazon, Meta, Google |

### Phase 3: Boss levels
| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 87 | N-Queens | 51 | H | Column + diagonal constraint tracking | Amazon, Google, Meta |
| 88 | N-Queens II | 52 | H | Count-only, bit manipulation optim | Google, Amazon |
| 89 | Sudoku Solver | 37 | H | Cell-by-cell, 3-constraint validation | Amazon, Google |
| 90 | Word Search II | 212 | H | Trie + grid backtracking | Amazon, Google, Meta |

**Backtracking Template (memorize this):**
```cpp
void backtrack(vector<int>& path, vector<int>& choices, int start) {
    if (goal_reached(path)) {
        result.push_back(path);
        return;
    }
    for (int i = start; i < choices.size(); i++) {
        if (!is_valid(i)) continue;    // prune
        path.push_back(choices[i]);    // choose
        backtrack(path, choices, i+1); // recurse (i+1 or i for reuse)
        path.pop_back();               // un-choose (BACKTRACK)
    }
}
```

---

## 9. Greedy (8 Questions)

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 91 | Jump Game | 55 | M | Track farthest reachable index | Amazon, Google, Meta |
| 92 | Jump Game II | 45 | M | BFS-style greedy (min jumps) | Amazon, Google |
| 93 | Gas Station | 134 | M | Circular reset when tank < 0 | Amazon, Google |
| 94 | Non-overlapping Intervals | 435 | M | Sort by end, count overlaps to remove | Amazon, Google, Meta |
| 95 | Meeting Rooms II | 253 | M | Min-heap / sweep line | Amazon, Meta, Google |
| 96 | Merge Intervals | 56 | M | Sort by start, extend or create | Amazon, Meta, Google |
| 97 | Minimum Platforms (GFG) | -- | M | Arrival/departure sort + sweep | Amazon, Google |
| 98 | Activity Selection | -- | M | Sort by end, greedily pick | Google, Amazon |

---

## 10. Dynamic Programming (30 Questions)

> **HEAVY FOCUS. See [dp_interview_questions_2024_2025.md](dp_interview_questions_2024_2025.md) for full explanations.**
> **Rule:** Always start with recursion + memo. Then convert to bottom-up.

### 1D DP
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 99 | Climbing Stairs | 70 | E | Fibonacci template |
| 100 | Min Cost Climbing Stairs | 746 | E | Optimization DP (min) |
| 101 | House Robber | 198 | M | Take or skip |
| 102 | House Robber II | 213 | M | Circular → two linear |
| 103 | Decode Ways | 91 | M | Conditional transitions |

### 2D Grid DP
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 104 | Unique Paths | 62 | M | Grid counting |
| 105 | Unique Paths II | 63 | M | Grid with obstacles |
| 106 | Minimum Path Sum | 64 | M | Grid optimization (min) |
| 107 | Triangle | 120 | M | Bottom-up grid |
| 108 | Dungeon Game | 174 | H | **Reverse DP direction** |

### Knapsack Family
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 109 | Partition Equal Subset Sum | 416 | M | 0/1 knapsack in disguise |
| 110 | Target Sum | 494 | M | Transform to subset sum |
| 111 | Coin Change | 322 | M | Unbounded knapsack (min) |
| 112 | Coin Change II | 518 | M | Unbounded knapsack (count) |
| 113 | Last Stone Weight II | 1049 | M | Min difference partition |

### String DP
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 114 | Longest Common Subsequence | 1143 | M | Two-string comparison |
| 115 | Edit Distance | 72 | M | Insert/delete/replace |
| 116 | Longest Palindromic Subsequence | 516 | M | LCS(s, reverse(s)) |
| 117 | Longest Palindromic Substring | 5 | M | Expand around center / interval DP |
| 118 | Word Break | 139 | M | String partition DP |

### LIS Family
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 119 | Longest Increasing Subsequence | 300 | M | O(n^2) DP, O(nlogn) BS |
| 120 | Number of LIS | 673 | M | Track count[] alongside length[] |
| 121 | Russian Doll Envelopes | 354 | H | Sort + LIS on one dimension |

### Interval / Partition DP
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 122 | Palindrome Partitioning II | 132 | H | Min cuts + palindrome DP |
| 123 | Burst Balloons | 312 | H | **Think LAST, not first** |
| 124 | Min Cost to Cut a Stick | 1547 | H | Modern matrix chain multiplication |
| 125 | Strange Printer | 664 | H | Interval DP with endpoint merge |

### DP on Trees
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 126 | Unique BSTs | 96 | M | Catalan numbers via DP |
| 127 | House Robber III | 337 | M | Tree DP (rob/not-rob pair) |
| 128 | Binary Tree Max Path Sum | 124 | H | Local vs global optimum |

---

## 11. Graphs (20 Questions)

> **NEVER DONE GRAPHS. See [graph_interview_questions.md](graph_interview_questions.md) for full explanations.**
> Follow this exact order -- each section builds on the previous.

### BFS Basics
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 129 | Binary Tree Level Order | 102 | M | Queue-based BFS |
| 130 | Rotting Oranges | 994 | M | Multi-source BFS |
| 131 | Shortest Path in Binary Matrix | 1091 | M | BFS shortest path (8-dir) |

### DFS Basics
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 132 | Number of Islands | 200 | M | DFS/BFS connected components |
| 133 | Flood Fill | 733 | E | Recursive DFS on grid |
| 134 | Surrounded Regions | 130 | M | Boundary DFS (invert problem) |

### Topological Sort
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 135 | Course Schedule | 207 | M | Cycle detection (Kahn's) |
| 136 | Course Schedule II | 210 | M | Full topological ordering |
| 137 | Alien Dictionary | 269 | H | Graph construction + topo sort |

### Shortest Path (Weighted)
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 138 | Network Delay Time | 743 | M | Classic Dijkstra |
| 139 | Cheapest Flights K Stops | 787 | M | Modified Bellman-Ford |
| 140 | Path with Max Probability | 1514 | M | Modified Dijkstra (max-heap) |

### Union-Find
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 141 | Number of Provinces | 547 | M | Classic Union-Find |
| 142 | Redundant Connection | 684 | M | Union-Find cycle detection |
| 143 | Accounts Merge | 721 | M | Union-Find on non-numeric data |

### Advanced Graph
| # | Problem | LC | Diff | Pattern |
|---|---------|-----|------|---------|
| 144 | Min Cost to Connect All Points | 1584 | M | MST (Prim's / Kruskal's) |
| 145 | Word Ladder | 127 | H | BFS on implicit graph |
| 146 | Is Graph Bipartite? | 785 | M | Graph 2-coloring |
| 147 | Clone Graph | 133 | M | DFS/BFS + hash map deep copy |
| 148 | Graph Valid Tree | 261 | M | Union-Find + tree properties |

---

## 12. Bit Manipulation + Tries (5 Questions)

| # | Problem | LC | Diff | Pattern | Company |
|---|---------|-----|------|---------|---------|
| 149 | Single Number | 136 | E | XOR cancellation (a^a=0) | Amazon, Google, Meta |
| 150 | Counting Bits | 338 | E | dp[i] = dp[i>>1] + (i&1) | Amazon, Google |
| 151 | Implement Trie | 208 | M | Trie node insert/search/prefix | Amazon, Google, Meta |
| 152 | Maximum XOR of Two Numbers | 421 | M | Bitwise trie, greedy opposite bits | Google, Amazon |
| 153 | Word Search II | 212 | H | Trie + grid DFS backtracking | Amazon, Google, Meta |

---

## Difficulty Distribution

| Difficulty | Count | Percentage |
|-----------|-------|------------|
| Easy | 20 | 13% |
| Medium | 107 | 70% |
| Hard | 26 | 17% |
| **Total** | **153** | **100%** |

---

## Recommended Daily Practice Schedule (Alongside 7-day concept plan)

| Week | Focus | Questions/Day | Topics |
|------|-------|--------------|--------|
| Week 1 | Warm-up + Strong topics | 5-6 | Arrays, Binary Search, Linked List, Stacks |
| Week 2 | Medium grind | 4-5 | Sorting, Trees, Heaps, Greedy |
| Week 3 | Weak areas | 3-4 (harder) | Backtracking, DP (1D, Grid, Knapsack) |
| Week 4 | DP deep dive | 3-4 | DP (String, LIS, Interval, Tree) |
| Week 5 | Graphs from scratch | 3-4 | BFS, DFS, Topo Sort, Dijkstra |
| Week 6 | Advanced + Review | 3-4 | Union-Find, Advanced Graph, Bits/Tries |
| Week 7+ | Mock interviews | 2-3 timed | Random mix, focus on weak spots |

---

## Key C++ Templates to Memorize

### Binary Search Template
```cpp
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (check(mid)) hi = mid - 1;
    else lo = mid + 1;
}
return lo; // first position where check() is true
```

### BFS Template
```cpp
queue<pair<int,int>> q;
q.push({start_r, start_c});
visited[start_r][start_c] = true;
while (!q.empty()) {
    auto [r, c] = q.front(); q.pop();
    for (auto [dr, dc] : dirs) {
        int nr = r+dr, nc = c+dc;
        if (nr>=0 && nr<m && nc>=0 && nc<n && !visited[nr][nc]) {
            visited[nr][nc] = true;
            q.push({nr, nc});
        }
    }
}
```

### Union-Find Template
```cpp
class UnionFind {
    vector<int> parent, rank_;
public:
    UnionFind(int n) : parent(n), rank_(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // path compression
        return parent[x];
    }
    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank_[px] < rank_[py]) swap(px, py);
        parent[py] = px;
        if (rank_[px] == rank_[py]) rank_[px]++;
        return true;
    }
};
```

### Dijkstra Template
```cpp
vector<int> dist(n, INT_MAX);
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
dist[src] = 0;
pq.push({0, src});
while (!pq.empty()) {
    auto [d, u] = pq.top(); pq.pop();
    if (d > dist[u]) continue;
    for (auto [v, w] : adj[u]) {
        if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            pq.push({dist[v], v});
        }
    }
}
```
