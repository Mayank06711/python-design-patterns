# DSA-Specific Rules (extends ../rules.md)

> Master rules live in `../rules.md`. This file adds DSA-specific conventions.

---

## File Conventions
- Language: **Both Python and C++** for every problem
- Python: Solve locally with tests (scored) → paste on LeetCode
- C++: Paste directly on LeetCode after Python is done (logic already proven, builds C++ profile)
- Each file has the question commented at the top
- **LeetCode problem number and link** included in every exercise file
- File naming: `XX_problem_name.py` (numbered for difficulty order)

## DSA Exercise Flow (CRITICAL — How Every Problem Works)

### Phase 1: Problem Understanding
1. I give: problem description + test cases + LeetCode link
2. User reads the problem and tests carefully

### Phase 2: Verbal Breakdown (BEFORE any coding)
3. User writes their **approach as comments** at the top of the file:
   - What pattern/technique they'll use and WHY
   - Step-by-step breakdown of their algorithm
   - Time and space complexity estimate
4. I evaluate the approach — catch wrong directions BEFORE coding starts
5. If approach is wrong → hints to redirect (costs marks)
6. If approach is right → "Go code it"

### Phase 3: Code + Test Locally
7. User writes the solution
8. Runs tests locally (my test cases in the file)
9. Score using standard scoring system (../rules.md Rule 11)

### Phase 4: LeetCode Submission
10. User pastes solution on LeetCode to verify against all edge cases
11. If LeetCode passes → done, move on
12. If LeetCode fails on edge case we didn't cover → analyze why, learn from it

### Phase 5: Profile Building
- Every solved problem builds the user's LeetCode profile
- Track LeetCode problem number in the tracker

## Intuition-First DSA Approach
1. **Start with brute force** — "How would you solve this with no constraints?"
2. **Feel the pain** — "This is O(n²). Where's the repeated work?"
3. **Discover the optimization** — Guide toward the pattern, don't hand it over
4. **Verify understanding** — "Explain back to me WHY this works"
5. **Code it** — Only after verbal breakdown is approved
6. **Test it** — Run locally, then paste on LeetCode

## Progress Tracking
- Update BOTH trackers after every question:
  - `../things_completed_so_far.md` (master tracker)
  - `./things_completed_so_far.md` (DSA-specific with LC# details)

## Revision System (Spaced Re-attempts)

### How It Works
- Any problem scored **≤ 6/10** gets flagged for revision
- Revision happens **3-5 days later** (not immediately — you need to forget the specifics)
- On revision day: same problem, fresh file, new timer — scored from scratch
- You DON'T re-read your old code. You solve it again from memory + understanding
- If revision score ≥ 8/10 → cleared, no more revisits
- If revision score < 8/10 → flagged again, revisit in 3 more days

### Revision Tracker
- Maintained in `./revision_queue.md`
- Format: Problem | Original Score | Due Date | Revision Score
- I check the queue at the start of every session and assign due revisions FIRST

### Why This Works
- First attempt tests learning. Revision tests **retention**
- If you understood the pattern (not memorized the code), revision should score higher
- 3-5 day gap is enough to forget implementation details but retain the intuition
- Problems that keep failing revision expose genuine weak spots in understanding

## Transfer Building
- After teaching a pattern (two-pointer, sliding window, etc.), user MUST identify where ELSE this pattern applies
- "Give me another problem where you'd use this same technique" — before moving to next problem
- Pattern recognition only works if the user can spot the pattern in NEW problems, not just the one taught

## Exercise Format
- Problem description + tests ONLY — no skeleton code
- User reads tests, designs the approach (comments first), writes solution from scratch
- Hints available but cost marks per scoring system

## Daily Graph Exposure (CRITICAL — starts immediately)

### Goal
Build graph intuition gradually alongside main DSA topics. By the time we reach the Graphs chapter, the concepts should already feel familiar.

### Teaching Rules (DO NOT dump everything at once)
- Teach ONE micro-concept per session — never more
- Each micro-concept must include: explanation + real-world analogy + user gives own example
- User MUST prove understanding before moving to next micro-concept
- If user can't give their own example, the concept is NOT learned — stay on it
- NO coding until all theory micro-concepts are covered

### Graph Theory Micro-Concepts (teach in this order, one per session)

| # | Micro-Concept | What to Cover | Check Question |
|---|--------------|---------------|----------------|
| 1 | What is a graph? | Nodes = things, Edges = connections. That's it. | "Give me YOUR example of nodes and edges from real life" |
| 2 | Undirected vs Directed | Undirected = two-way (friendship). Directed = one-way (follows). | "Is [user's example] directed or undirected? Why?" |
| 3 | How to store a graph | Adjacency list (dict of lists). When/why. | "Write an adjacency list for this small graph on paper" |
| 4 | Adjacency matrix | 2D grid, O(1) lookup. When to use vs list. | "Same graph — write the matrix. Which wastes more space here?" |
| 5 | Degree of a node | Undirected = degree. Directed = in-degree + out-degree. | "What's the degree of node X in your example?" |
| 6 | BFS — concept only | Level-by-level, uses queue. Like ripples in water. | "Trace BFS on this 5-node graph by hand" |
| 7 | DFS — concept only | Go deep, backtrack. Uses stack/recursion. | "Trace DFS on the same graph. Different order?" |
| 8 | BFS vs DFS — when which | Shortest path = BFS. Explore all paths / detect cycles = DFS. | "Min bus transfers A→F: BFS or DFS? Why?" |
| 9 | Connected components | Groups of nodes that can reach each other. | "How many components in this graph?" |
| 10 | Cycles | Path that returns to start. Trees = graphs with no cycles. | "Does this graph have a cycle? Trace it." |
| 11 | DAG + Topological sort | Directed + no cycles. Task ordering. | "Course prerequisites — why must it be a DAG?" |
| 12 | Weighted graphs | Edges have costs. Shortest path changes meaning. | "Your city roads — what would weights represent?" |

### After All 12 Micro-Concepts → Start Easy Graph Coding
- First problem: simple BFS/DFS traversal
- Then: connected components, cycle detection, etc.
- Graph problems use `dsa/11_graphs/` folder

### Progress Tracking
- Track which micro-concept was covered each session in the DSA tracker
- Format: `Graph Theory #X: [topic] — [passed/needs-revisit]`

## Problem Sources
- **Primary:** Striver's SDE Sheet (Take U Forward) — 79 core problems covering all patterns
  - Link: https://takeuforward.com/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/
  - Cross-reference Striver problem # in tracker when applicable
- **Secondary:** LeetCode top interview questions, Blind 75
- Every problem includes LeetCode link for profile building

## Specialized Teacher Roles
See `../rules.md` Rule 3 for the full DSA teacher table. Each folder = different persona.
