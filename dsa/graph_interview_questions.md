# Graph Interview Questions: Complete Beginner-to-Advanced Roadmap
## 20 Questions Frequently Asked at Google, Amazon, and Meta (2024-2025)

> **How to use this list:** Work through these questions in order. Each section builds on the previous one. By the end, you will have covered every major graph pattern tested in FAANG interviews.

---

## Section 1: BFS Basics (Questions 1-3)

> **Why start here:** BFS (Breadth-First Search) explores nodes level by level using a queue. It is the foundation for shortest-path problems in unweighted graphs and grids. Master BFS first because it is the most intuitive graph traversal.

### 1. Binary Tree Level Order Traversal
- **LeetCode:** #102
- **Difficulty:** Medium
- **Concept/Pattern:** Core BFS with a queue. Teaches you how to process nodes level by level, which is the fundamental BFS mechanic. This is the gentlest introduction to BFS because trees have no cycles.
- **Frequently Asked At:** Amazon, Meta, Google, Microsoft, Apple

### 2. Rotting Oranges
- **LeetCode:** #994
- **Difficulty:** Medium
- **Concept/Pattern:** Multi-source BFS. Instead of starting from one node, you start from ALL rotten oranges simultaneously. Teaches how BFS naturally models "spreading" over time in a grid. Each BFS layer = one time step.
- **Frequently Asked At:** Amazon, Google, Meta, Microsoft

### 3. Shortest Path in Binary Matrix
- **LeetCode:** #1091
- **Difficulty:** Medium
- **Concept/Pattern:** BFS for shortest path in an unweighted grid. Teaches 8-directional movement (vs. the typical 4-directional) and why BFS guarantees shortest path when all edge weights are equal.
- **Frequently Asked At:** Meta, Amazon, Google

---

## Section 2: DFS Basics (Questions 4-6)

> **Why this next:** DFS (Depth-First Search) explores as deep as possible before backtracking. It is ideal for "explore all connected components" problems. Together with BFS, DFS forms the backbone of all graph algorithms.

### 4. Number of Islands
- **LeetCode:** #200
- **Difficulty:** Medium
- **Concept/Pattern:** DFS/BFS on a grid to count connected components. This is THE classic graph problem. Teaches how to treat a 2D grid as an implicit graph, use visited marking, and count distinct connected components.
- **Frequently Asked At:** Amazon, Google, Meta, Microsoft, Bloomberg

### 5. Flood Fill
- **LeetCode:** #733
- **Difficulty:** Easy
- **Concept/Pattern:** Basic DFS on a grid (like Microsoft Paint's bucket fill). Teaches recursive DFS traversal with boundary conditions. A simpler version of Number of Islands that reinforces the same pattern.
- **Frequently Asked At:** Amazon, Google, Meta

### 6. Surrounded Regions
- **LeetCode:** #130
- **Difficulty:** Medium
- **Concept/Pattern:** DFS from the boundary inward (reverse thinking). Instead of finding surrounded regions directly, you find all 'O' cells connected to the border (which are NOT surrounded), then flip the rest. Teaches the powerful technique of inverting the problem.
- **Frequently Asked At:** Amazon, Google, Meta

---

## Section 3: Topological Sort (Questions 7-9)

> **Why this next:** Topological sort orders nodes in a directed acyclic graph (DAG) so that for every edge u -> v, u comes before v. It is essential for dependency resolution problems. Uses DFS or Kahn's Algorithm (BFS with in-degree tracking).

### 7. Course Schedule
- **LeetCode:** #207
- **Difficulty:** Medium
- **Concept/Pattern:** Cycle detection in a directed graph using topological sort. Given course prerequisites, determine if it is possible to finish all courses. Teaches Kahn's Algorithm (BFS-based topological sort) and how to detect cycles.
- **Frequently Asked At:** Amazon, Meta, Google, Microsoft

### 8. Course Schedule II
- **LeetCode:** #210
- **Difficulty:** Medium
- **Concept/Pattern:** Full topological sort to produce a valid ordering. Builds directly on Course Schedule #207 by actually returning the ordering, not just checking if one exists. Teaches the complete topological sort implementation.
- **Frequently Asked At:** Amazon, Meta, Google, DoorDash

### 9. Alien Dictionary
- **LeetCode:** #269 (Premium)
- **Difficulty:** Hard
- **Concept/Pattern:** Build a graph from implicit ordering rules, then topological sort. You must first construct the directed graph by comparing adjacent words, then find the topological order. Teaches graph construction from non-obvious input.
- **Frequently Asked At:** Google, Meta, Amazon, Airbnb

---

## Section 4: Shortest Path - Weighted Graphs (Questions 10-12)

> **Why this next:** Real-world graphs have weighted edges. BFS only works for unweighted graphs. Dijkstra handles non-negative weights; Bellman-Ford handles negative weights and constraints like "at most K stops."

### 10. Network Delay Time
- **LeetCode:** #743
- **Difficulty:** Medium
- **Concept/Pattern:** Classic Dijkstra's Algorithm. Given a network of nodes with weighted edges, find the time it takes for a signal to reach all nodes. This is the purest "implement Dijkstra" problem and the best starting point for weighted shortest paths.
- **Frequently Asked At:** Google, Amazon, Meta

### 11. Cheapest Flights Within K Stops
- **LeetCode:** #787
- **Difficulty:** Medium
- **Concept/Pattern:** Modified Bellman-Ford Algorithm (or BFS with pruning). Find the cheapest flight path with at most K stops. Teaches how to adapt shortest-path algorithms when there are additional constraints (max number of edges).
- **Frequently Asked At:** Amazon, Google, Meta

### 12. Path with Maximum Probability
- **LeetCode:** #1514
- **Difficulty:** Medium
- **Concept/Pattern:** Modified Dijkstra (max-probability instead of min-distance). Teaches how to adapt Dijkstra for different optimization objectives. Uses a max-heap instead of min-heap and multiplies probabilities instead of adding distances.
- **Frequently Asked At:** Google, Amazon

---

## Section 5: Union-Find / Disjoint Set (Questions 13-15)

> **Why this next:** Union-Find is an alternative to DFS/BFS for connected component problems. It excels when edges are added dynamically or when you need to efficiently merge and query groups. Two key optimizations: path compression and union by rank.

### 13. Number of Provinces
- **LeetCode:** #547
- **Difficulty:** Medium
- **Concept/Pattern:** Classic Union-Find to count connected components. Given a city adjacency matrix, group connected cities into provinces. This is the best introduction to Union-Find because it is a direct "count components" problem.
- **Frequently Asked At:** Amazon, Google, Meta

### 14. Redundant Connection
- **LeetCode:** #684
- **Difficulty:** Medium
- **Concept/Pattern:** Union-Find to detect cycles. Given edges of a graph that was originally a tree, find the one extra edge that creates a cycle. Teaches how Union-Find detects cycles: if two nodes are already connected when you try to union them, you found a cycle.
- **Frequently Asked At:** Amazon, Google, Meta

### 15. Accounts Merge
- **LeetCode:** #721
- **Difficulty:** Medium
- **Concept/Pattern:** Union-Find for grouping by shared attributes. Merge accounts that share at least one email. Teaches how to use Union-Find on non-numeric data by mapping emails to account indices. A practical, real-world application of Union-Find.
- **Frequently Asked At:** Meta, Amazon, Google

---

## Section 6: Advanced Graph (Questions 16-20)

> **Why this last:** These problems combine multiple techniques or introduce new algorithms (MST, BFS on transformed graphs, graph coloring). Tackle these once you are comfortable with all the patterns above.

### 16. Min Cost to Connect All Points
- **LeetCode:** #1584
- **Difficulty:** Medium
- **Concept/Pattern:** Minimum Spanning Tree (Prim's or Kruskal's Algorithm). Connect all points with minimum total Manhattan distance. Teaches MST construction -- Kruskal's uses Union-Find (connecting earlier patterns), while Prim's uses a priority queue.
- **Frequently Asked At:** Amazon, Google

### 17. Word Ladder
- **LeetCode:** #127
- **Difficulty:** Hard
- **Concept/Pattern:** BFS on an implicit graph where each word is a node and edges connect words differing by one letter. Teaches how to recognize a graph problem when no explicit graph is given, and how to construct adjacency relationships from problem constraints.
- **Frequently Asked At:** Amazon, Meta, Google, Microsoft

### 18. Is Graph Bipartite?
- **LeetCode:** #785
- **Difficulty:** Medium
- **Concept/Pattern:** Graph coloring / 2-coloring using BFS or DFS. Determine if a graph can be divided into two sets where no two nodes in the same set are adjacent. Teaches the graph coloring technique and how bipartiteness relates to cycle detection (odd cycles = not bipartite).
- **Frequently Asked At:** Amazon, Google, Meta

### 19. Clone Graph
- **LeetCode:** #133
- **Difficulty:** Medium
- **Concept/Pattern:** Deep copy of a graph using DFS/BFS with a hash map. Teaches how to traverse a graph while maintaining a mapping between original and cloned nodes. Tests understanding of reference vs. value and graph structure preservation.
- **Frequently Asked At:** Meta, Amazon, Google, Microsoft

### 20. Graph Valid Tree
- **LeetCode:** #261 (Premium)
- **Difficulty:** Medium
- **Concept/Pattern:** Combines Union-Find and graph properties. A valid tree must have exactly n-1 edges and be fully connected (no cycles). Teaches the mathematical properties of trees as a special case of graphs, and ties together cycle detection with connectivity checking.
- **Frequently Asked At:** Google, Amazon, Meta

---

## Study Order Summary

| Phase | Questions | Core Skill Unlocked |
|-------|-----------|-------------------|
| **Week 1** | #1-3 (BFS) | Queue-based traversal, multi-source BFS, grid shortest path |
| **Week 1** | #4-6 (DFS) | Recursive traversal, connected components, boundary DFS |
| **Week 2** | #7-9 (Topo Sort) | Dependency ordering, cycle detection in directed graphs |
| **Week 2** | #10-12 (Shortest Path) | Dijkstra, Bellman-Ford, weighted graph traversal |
| **Week 3** | #13-15 (Union-Find) | Disjoint sets, dynamic connectivity, cycle detection |
| **Week 3** | #16-20 (Advanced) | MST, implicit graphs, graph coloring, deep copy |

---

## Key Patterns Cheat Sheet

| Pattern | When to Use | Key Data Structure |
|---------|------------|-------------------|
| **BFS** | Shortest path (unweighted), level-by-level processing | Queue |
| **DFS** | Explore all paths, connected components, backtracking | Stack / Recursion |
| **Topological Sort** | Dependency ordering, course scheduling | In-degree array + Queue (Kahn's) |
| **Dijkstra** | Shortest path (non-negative weights) | Min-Heap / Priority Queue |
| **Bellman-Ford** | Shortest path (with negative weights or edge constraints) | Relaxation array |
| **Union-Find** | Dynamic connectivity, cycle detection, component counting | Parent array + Rank array |
| **Kruskal's MST** | Minimum spanning tree | Sorted edges + Union-Find |
| **Graph Coloring** | Bipartite check, scheduling conflicts | Color array + BFS/DFS |
