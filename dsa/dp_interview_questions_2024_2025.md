# Dynamic Programming Interview Questions (2024-2025)
## Progressive Intuition Builder: 30 Questions by Pattern

> Organized to build DP intuition step-by-step. Each pattern section starts with the
> foundational problem and escalates. Master each section before moving to the next.

---

## PATTERN 1: 1D DP (Linear Sequence)
**Core intuition:** dp[i] depends on one or more previous states in a single dimension.
**State template:** `dp[i] = f(dp[i-1], dp[i-2], ...)`

---

### 1. Climbing Stairs
- **LeetCode:** #70
- **Difficulty:** Easy
- **Company:** Amazon, Google, Microsoft
- **Why it matters:** The absolute foundation of DP. Teaches you that dp[i] = dp[i-1] + dp[i-2] is just Fibonacci in disguise. If you cannot see the overlapping subproblems here, nothing else will click. This is the problem that bridges recursion to DP.

### 2. Min Cost Climbing Stairs
- **LeetCode:** #746
- **Difficulty:** Easy
- **Company:** Amazon, Microsoft
- **Why it matters:** Extends Climbing Stairs by adding a cost to each step. Teaches you to pick the OPTIMAL previous state (min instead of sum). This is your first encounter with optimization DP vs. counting DP -- a critical distinction.

### 3. House Robber
- **LeetCode:** #198
- **Difficulty:** Medium
- **Company:** Amazon, Google, Cisco, Adobe
- **Why it matters:** Introduces the "take or skip" decision: dp[i] = max(dp[i-1], dp[i-2] + nums[i]). This is the most common 1D DP pattern in interviews -- you either include the current element or you do not. Nearly every 1D DP problem reduces to a variant of this choice.

### 4. House Robber II
- **LeetCode:** #213
- **Difficulty:** Medium
- **Company:** Google, Amazon, Microsoft
- **Why it matters:** Identical to House Robber, but the array is circular. Teaches you a powerful trick: reduce a circular problem to two linear subproblems (rob houses 0..n-2 OR 1..n-1). This "decompose circular into linear" technique shows up repeatedly.

### 5. Decode Ways
- **LeetCode:** #91
- **Difficulty:** Medium
- **Company:** Google, Amazon, Meta, Microsoft
- **Why it matters:** A counting problem where dp[i] depends on whether the current digit and the two-digit combination form valid characters. Teaches conditional state transitions -- not all previous states are always valid. This is a massive jump in complexity from Climbing Stairs despite looking similar.

---

## PATTERN 2: 2D DP / Grid Traversal
**Core intuition:** dp[i][j] represents optimal value or count at cell (i, j).
**State template:** `dp[i][j] = f(dp[i-1][j], dp[i][j-1], ...)`

---

### 6. Unique Paths
- **LeetCode:** #62
- **Difficulty:** Medium
- **Company:** Google, Amazon, Microsoft, Bloomberg
- **Why it matters:** The "Hello World" of 2D DP. A robot moves only right or down on a grid. dp[i][j] = dp[i-1][j] + dp[i][j-1]. Teaches you to visualize DP as filling a table cell by cell. Once you see this, every grid DP problem becomes a table-filling exercise.

### 7. Unique Paths II
- **LeetCode:** #63
- **Difficulty:** Medium
- **Company:** Amazon, Google, Bloomberg
- **Why it matters:** Adds obstacles to Unique Paths. Teaches you how to handle constraints/blocked states in DP -- simply set dp[i][j] = 0 for obstacle cells. Real interview problems always have constraints; this is where you learn to adapt the base pattern.

### 8. Minimum Path Sum
- **LeetCode:** #64
- **Difficulty:** Medium
- **Company:** Amazon, Google, Goldman Sachs
- **Why it matters:** Switches from counting paths to minimizing cost. dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]). Teaches you that the same grid framework supports both counting and optimization -- the only thing that changes is the aggregation function (sum vs. min).

### 9. Triangle
- **LeetCode:** #120
- **Difficulty:** Medium
- **Company:** Amazon, Apple, Microsoft
- **Why it matters:** A non-rectangular grid DP. Forces you to think bottom-up (starting from the last row) which is often more natural than top-down for path problems. Teaches that DP direction matters -- sometimes working backwards simplifies the logic dramatically.

### 10. Dungeon Game
- **LeetCode:** #174
- **Difficulty:** Hard
- **Company:** Google, Amazon, Microsoft
- **Why it matters:** You MUST traverse the grid backwards (from bottom-right to top-left) because the knight needs minimum health at each point. Teaches that when the optimal choice at (i,j) depends on the FUTURE (not the past), you reverse the DP direction. This single insight solves an entire class of "minimum resource to survive" problems.

---

## PATTERN 3: Knapsack Family
**Core intuition:** Given items with weight/value, select a subset under constraints.
**State template:** `dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i]] + value[i])`

---

### 11. Partition Equal Subset Sum
- **LeetCode:** #416
- **Difficulty:** Medium
- **Company:** Amazon, Google, Apple, Meta
- **Why it matters:** The gateway to Knapsack DP. Asks: can you split an array into two subsets with equal sum? This is 0/1 Knapsack in disguise (target = totalSum/2, each number is an item). Once you see this reduction, you unlock an entire family of problems.

### 12. Target Sum
- **LeetCode:** #494
- **Difficulty:** Medium
- **Company:** Amazon, Google, Meta
- **Why it matters:** Assign + or - to each number to reach a target. Looks different from Knapsack but reduces to: find a subset with sum = (target + total) / 2. Teaches the critical skill of transforming a problem into a known pattern. This transformation step is what separates good from great DP solvers.

### 13. Coin Change
- **LeetCode:** #322
- **Difficulty:** Medium
- **Company:** Amazon, Google, Apple, Bloomberg, Microsoft
- **Why it matters:** The most-asked DP problem in interviews, period. Unbounded Knapsack variant where you minimize the number of coins. dp[amount] = min(dp[amount], dp[amount - coin] + 1). Teaches unbounded knapsack (items reusable) vs. 0/1 knapsack (items used once).

### 14. Coin Change II
- **LeetCode:** #518
- **Difficulty:** Medium
- **Company:** Amazon, Google, Bloomberg
- **Why it matters:** Same setup as Coin Change but counts the NUMBER of ways instead of minimum coins. The critical lesson: iterating coins in the outer loop vs. amounts in the outer loop determines whether you count combinations or permutations. This subtlety trips up most candidates.

### 15. Last Stone Weight II
- **LeetCode:** #1049
- **Difficulty:** Medium
- **Company:** Google, Amazon
- **Why it matters:** Disguised as a simulation problem but reduces to: partition stones into two groups and minimize the absolute difference of their sums. This is the "minimum difference partition" variant of knapsack. Teaches you to recognize Knapsack hiding behind problem descriptions that look nothing like Knapsack.

---

## PATTERN 4: String DP
**Core intuition:** dp[i][j] compares/aligns prefixes of two strings (or substrings of one).
**State template:** `dp[i][j] = f(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])`

---

### 16. Longest Common Subsequence (LCS)
- **LeetCode:** #1143
- **Difficulty:** Medium
- **Company:** Amazon, Google, Microsoft, Karat
- **Why it matters:** The foundational string DP problem. If s1[i] == s2[j], extend the subsequence; otherwise take the best of skipping either character. This "match or skip" framework is the backbone of edit distance, diff algorithms, and DNA sequence alignment. Master this and the rest follow.

### 17. Edit Distance
- **LeetCode:** #72
- **Difficulty:** Medium
- **Company:** Google, Amazon, Microsoft, Bloomberg
- **Why it matters:** Extends LCS with three operations: insert, delete, replace. dp[i][j] = min of three choices. This is one of the most frequently asked Hard-tier DP problems (classified Medium but plays Hard). It directly models real-world problems like spell-checkers and version control diffs.

### 18. Longest Palindromic Subsequence
- **LeetCode:** #516
- **Difficulty:** Medium
- **Company:** Amazon, Google, LinkedIn
- **Why it matters:** The key insight is that the longest palindromic subsequence of string s equals the LCS of s and reverse(s). Teaches you to reduce unfamiliar problems to problems you have already solved. This reductive thinking is pure interview gold.

### 19. Longest Palindromic Substring
- **LeetCode:** #5
- **Difficulty:** Medium
- **Company:** Amazon, Google, Microsoft, Meta, Apple
- **Why it matters:** Unlike subsequence problems, substrings must be contiguous. dp[i][j] = true if s[i..j] is a palindrome. Teaches the "expand around center" technique and interval-based DP on a single string. One of the most frequently asked DP problems across all companies.

### 20. Word Break
- **LeetCode:** #139
- **Difficulty:** Medium
- **Company:** Amazon, Google, Meta, Apple, Bloomberg
- **Why it matters:** dp[i] = true if s[0..i-1] can be segmented into dictionary words. Combines string matching with 1D DP. Teaches you to think about string partitioning as a DP problem -- each position is a potential "cut point." Extremely popular in interviews because it tests multiple skills simultaneously.

---

## PATTERN 5: Longest Increasing Subsequence (LIS) Family
**Core intuition:** For each element, find the best ending at or before it.
**State template:** `dp[i] = max(dp[j] + 1) for all j < i where arr[j] < arr[i]`

---

### 21. Longest Increasing Subsequence
- **LeetCode:** #300
- **Difficulty:** Medium
- **Company:** Google, Amazon, Microsoft, Apple
- **Why it matters:** The template problem for the LIS pattern. O(n^2) DP solution teaches the "for each element, check all previous elements" framework. The O(n log n) binary search optimization (patience sorting) is a must-know for senior roles. Google has asked this directly in 2024.

### 22. Number of Longest Increasing Subsequence
- **LeetCode:** #673
- **Difficulty:** Medium
- **Company:** Amazon, Google, Meta
- **Why it matters:** Not just the length, but COUNT all LIS. Requires maintaining two arrays: length[] and count[]. Teaches you to track auxiliary information alongside the main DP state -- a technique that generalizes to many "count optimal solutions" variants.

### 23. Russian Doll Envelopes
- **LeetCode:** #354
- **Difficulty:** Hard
- **Company:** Google, Amazon, Microsoft
- **Why it matters:** 2D extension of LIS. Sort by width ascending, then by height DESCENDING for same width, then find LIS on heights. Teaches dimensional reduction: convert a multi-dimensional problem to a known 1D pattern via clever sorting. This sort-then-LIS trick is reusable across many problems.

---

## PATTERN 6: Interval / Partition DP
**Core intuition:** Solve for all subranges [i, j] by trying every possible split point k.
**State template:** `dp[i][j] = optimize over k in [i, j] of: dp[i][k] + dp[k][j] + cost`

---

### 24. Palindrome Partitioning II
- **LeetCode:** #132
- **Difficulty:** Hard
- **Company:** Google, Amazon, Bloomberg
- **Why it matters:** Find the minimum cuts to partition a string so every piece is a palindrome. A classic "minimum partitioning" DP. Teaches you to combine palindrome checking (which itself is DP) with partition DP. Two DP tables working together is an advanced but critical concept.

### 25. Burst Balloons
- **LeetCode:** #312
- **Difficulty:** Hard
- **Company:** Google, Amazon, Microsoft
- **Why it matters:** THE canonical interval DP problem. The key counter-intuitive insight: instead of thinking about which balloon to burst FIRST, think about which balloon to burst LAST in the interval [i, j]. This "reverse the order of operations" insight is one of the deepest in DP and unlocks matrix chain multiplication and similar problems.

### 26. Minimum Cost to Cut a Stick
- **LeetCode:** #1547
- **Difficulty:** Hard
- **Company:** Google, Amazon
- **Why it matters:** Modern variant of matrix chain multiplication. Given cut positions, find the minimum total cost of cuts (cost = length of the stick being cut). Cleaner than matrix chain multiplication but tests the exact same interval DP framework. Appeared frequently in 2024 Google interviews.

### 27. Strange Printer
- **LeetCode:** #664
- **Difficulty:** Hard
- **Company:** Google
- **Why it matters:** A printer can print a sequence of same characters at a time. Find the minimum turns to print a string. This is interval DP with a twist: if s[i] == s[j], you can merge the subproblems. Teaches that interval DP is not just about splitting -- sometimes endpoints interact. This is the hardest pattern to recognize in the wild.

---

## PATTERN 7: DP on Trees / Graphs
**Core intuition:** Run DFS/BFS; at each node, combine results from children.
**State template:** `dp[node] = f(dp[child1], dp[child2], ...)`

---

### 28. Unique Binary Search Trees
- **LeetCode:** #96
- **Difficulty:** Medium
- **Company:** Amazon, Google, Microsoft
- **Why it matters:** Count structurally unique BSTs with n nodes. G(n) = sum of G(i-1) * G(n-i) for each root i. This is Catalan numbers via DP. Teaches tree-structured subproblem decomposition: choosing a root splits the problem into independent left and right subtrees.

### 29. House Robber III
- **LeetCode:** #337
- **Difficulty:** Medium
- **Company:** Amazon, Google, Uber
- **Why it matters:** House Robber on a binary tree. Each node returns a pair: (max if robbed, max if not robbed). Teaches the "DP state at each node" technique using post-order DFS. This is the bridge from linear DP to tree DP -- the same "take or skip" logic from House Robber I now runs on a tree structure.

### 30. Binary Tree Maximum Path Sum
- **LeetCode:** #124
- **Difficulty:** Hard
- **Company:** Google, Amazon, Meta, Microsoft, Bloomberg
- **Why it matters:** Find the maximum sum path between any two nodes in a binary tree. At each node, you decide: extend the path through this node or start a new path here. Teaches the "local vs. global optimum" pattern: the value you return UP to the parent differs from the global answer you update. This distinction is THE key concept in tree DP and appears in diameter-of-tree, longest-path, and similar problems.

---

## Study Order Recommendation

**Week 1 - Foundation (Problems 1-5):** 1D DP. Get comfortable converting recursion to tabulation.

**Week 2 - Grids (Problems 6-10):** 2D DP on grids. Practice visualizing the DP table.

**Week 3 - Knapsack (Problems 11-15):** Learn to recognize knapsack variants in disguise.

**Week 4 - Strings (Problems 16-20):** Master the two-string comparison framework.

**Week 5 - LIS + Interval (Problems 21-27):** Advanced patterns. Focus on the "try all split points" technique.

**Week 6 - Trees + Review (Problems 28-30):** Tree DP, then revisit any weak areas.

---

## Key Intuition-Building Tips

1. **Always start with recursion + memoization.** Write the brute-force recursive solution first. Then add a cache. THEN convert to bottom-up. Skipping straight to tabulation is why people get stuck.

2. **Define the state in English before coding.** Write down: "dp[i] represents ___." If you cannot complete that sentence, you are not ready to code.

3. **Draw the DP table on paper for small inputs.** Fill in 3-4 rows/columns by hand. The transition formula will reveal itself.

4. **Recognize the pattern category first.** Before solving, ask: Is this 1D? Grid? Knapsack? String comparison? Interval? The category tells you the state shape and transition structure.

5. **The hardest part is not coding -- it is the state definition.** If your state is wrong, no amount of clever coding will save you. Spend 60% of your time on state definition, 40% on implementation.
