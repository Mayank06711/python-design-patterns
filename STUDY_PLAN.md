# Interview Prep: Structured Study Plan

> **READ THIS FIRST** — Every AI on every laptop reads this file at session start.
> Target: Google-level interview readiness
> Languages: Python (concepts + DSA local), C++ (DSA on LeetCode)
> Total: 326 questions (173 concept + 153 DSA)

---

## How Every Session Works (2-3 hours)

**3 slots. Never skip a slot. Never let one topic eat the whole session.**

| Slot | Duration | What | Rule |
|------|----------|------|------|
| **Slot 1: Core Concept** | 30-40 min | Current concept topic (closures/HOF/decorators, then SQL, etc.) | Always comes FIRST. Teach concept → exercise → user gives own example. |
| **Slot 2: DSA (Mixed)** | 60-75 min | 3 problems from TWO tracks (see below) | Check `dsa/revision_queue.md` first — due revisions replace one problem. |
| **Slot 3: Graph Micro** | 10-15 min | One micro-concept from graph table | Last thing in session. ONE concept only. User gives own example to pass. |

**Session start checklist:**
1. Pull latest branch
2. Check revision queue — do due revisions in Slot 2 before new problems
3. Check which **Phase + Session** we're in (see below)
4. Follow the 3-slot structure

---

## DSA Mixed-Topic System (NEW — effective Session 11)

> **Why:** User already practiced arrays, linked lists, trees, stacks, recursion, DP in C++.
> Interleaved practice builds stronger retention than grinding one topic.
> Known topics go fast (Python translation), freeing time for harder new patterns.

### Two Parallel Tracks

| Track | Purpose | Difficulty | Speed |
|-------|---------|-----------|-------|
| **Track A (Primary)** | New/challenging patterns done in order | Medium-Hard | ~15-20 min/problem |
| **Track B (Refresh)** | Topics user knows from C++ — Python translation | Medium (start), ramp up | ~8-12 min/problem |

**Each session Slot 2:** 1 Track A + 2 Track B = 3 DSA problems
(If time is tight or a problem is Hard: 1 Track A + 1 Track B = 2 problems)

### Track A — Primary (go in order)

| Priority | Topic | Problems | Algo Fundamentals (first session) | Est. Sessions |
|----------|-------|----------|----------------------------------|---------------|
| 1 | Arrays/Two Pointers (finish) | 3 remaining (matrix) | — (already covered) | 1-2 |
| 2 | Binary Search | 10 | Basic BS taught S14. Variants: rotated, answer-space | 4-5 |
| 3 | Sorting | 8 | **Implement: Merge Sort, Quick Sort, Heap Sort.** Concept: Counting/Bucket Sort | 4-5 |
| 4 | DP | 30 | **Recursion → Memo → Tabulation pipeline on 0/1 Knapsack parent** | 12-15 |
| 5 | Graphs (coding) | 20 | **Implement: BFS, DFS, Dijkstra, Topo Sort, Union-Find.** Concept: Bellman-Ford, Kruskal's, Prim's | 10-12 |
| 6 | Bits/Tries | 5 | XOR properties, Trie implementation | 2 |

### Track B — Refresh (rotate every 2-3 sessions)

| Rotation | Topic | Problems | Algo Fundamentals (first session) | Python Focus |
|----------|-------|----------|----------------------------------|-------------|
| B1 | Linked List | 12 | Dummy head technique (taught S14) | Pointer-free approach, Python idioms |
| B2 | Stacks/Queues | 10 | **Monotonic stack/deque pattern.** collections.deque | Monotonic patterns, sliding window max |
| B3 | Trees/BST | 15 | **Implement: recursive + iterative traversals, BFS level-order** | BST properties, validate BST |
| B4 | Recursion/Backtracking | 12 | **Backtracking template: base→loop→pick→recurse→unpick** | Generator patterns, memoization |
| B5 | Heaps | 8 | **heapq module, heapify, Top-K template** | Two-heap technique |
| B6 | Greedy | 8 | Exchange argument proof technique | Proof of correctness |

**Rotation rule:** Spend 2-3 sessions on each Track B topic (4-6 problems), then rotate to next.
When Sliding Window Max revision comes due (after B2 deque), do it immediately.

### Pattern Learning Cycle (applied to every new pattern)

```
1. TEACH: recognition triggers + counter-example + parent problem (10 min)
2. APPLY: 3-5 problems across sessions, including cross-DS variants
3. VERIFY: unlabeled problem — user identifies pattern in 2 min
   → If can't identify → 2 more problems before moving on
   → Target: 5-7 problems per pattern for solidification
```

### Concrete Session Plan

| Session | Slot 1: Concept | Track A | Track B | Graph Micro | Notes |
|---------|----------------|---------|---------|-------------|-------|
| **11** | HOF Q7 + Q9 curry | Arrays: 1 | LL: 2 (start B1) | #6: BFS | |
| **12** | Decorators basics | Arrays: 1 | LL: 2 | #7: DFS | |
| **13** | Deco: functools.wraps | Arrays: 1 (finish!) | LL: 2 | #8: BFS vs DFS | |
| **14** | Deco: with arguments | BS: 1 (start) | LL: 1 (finish B1) | #9: Connected comp | ✅ DONE |
| **15** | Deco: stacking, class deco | BS: 1 + matrix problem | LL: 1 (last B1) + Stack: 1 (start B2) | #10: Cycles | Algo: monotonic stack intro |
| **16** | Deco: advanced + capstone | BS: 1 | Stack: 2 | #11: DAG + Topo sort | |
| **17** | Closures/HOF/Deco quiz | BS: 1 | Stack: 2 (finish B2, Sliding Window Max revision!) | #12: Weighted graphs | |
| **18** | SQL: SELECT, WHERE, JOINs | BS: 1 | Trees: algo fundamentals (implement traversals) | Graph coding #1 | **DRILL SESSION** — Slot 2 = 3 unlabeled mixed problems |
| **19** | SQL: JOINs deep dive | BS: finish | Trees: 2 | Graph coding #2 | |
| **20** | SQL: GROUP BY, HAVING | **Sorting: algo fundamentals** (implement Merge/Quick/Heap sort) | Trees: 2 | Graph coding #3 | First sorting session = implement algos |
| **21** | SQL: subqueries, CTEs | Sorting: 2 problems | Trees: 2 (finish B3) | Graph coding #4 | |
| **22** | SQL: indexing, EXPLAIN | Sorting: 2 problems | Recursion/BT: 2 (start B4) | Graph coding #5 | **DRILL SESSION** |
| ... | ... continues ... | ... | ... | ... | Drill every 4th: 26, 30, 34... |

> **Key changes from old plan:**
> - Algo fundamentals block when each new topic starts (bold in table)
> - Drill sessions every 4th session starting at Session 18
> - Pattern coverage tracked in `PATTERN_REFERENCE.md`
> - Target: 5-7 problems per pattern before moving on
> - Cross-DS pattern application built into problem selection

---

## Phase 1 (Current): Closures/HOF/Decorators + Mixed DSA (Sessions 8-17)

> **Concept Track:** Closures / HOF / Decorators (33 questions)
> **DSA Track A:** Finish Arrays (5 left) → Binary Search (10)
> **DSA Track B:** Linked List (B1) → Stacks/Queues (B2)
> **Graph Track:** Micro-concepts #1 through #12

---

## Phase 2: SQL + Mixed DSA (Sessions 18-25)

> **Concept Track:** SQL & Indexing (35 questions)
> **DSA Track A:** Finish Binary Search → Sorting (8)
> **DSA Track B:** Trees (B3) → Recursion/Backtracking (B4)
> **Graph Track:** Start graph CODING problems

---

## Phase 3: Rate Limiting + Mixed DSA (Sessions 26-32)

> **Concept Track:** Rate Limiting (27 questions)
> **DSA Track A:** DP start (30 problems — longest track)
> **DSA Track B:** Heaps (B5) → Greedy (B6)

---

## Phase 4: System Design + DP Focus (Sessions 33-45)

> **Concept Track:** System Design (27 questions)
> **DSA Track A:** DP continue (most of the 30 problems here)
> **DSA Track B:** Rotate back to weak topics for revision

---

## Phase 5: Graphs Coding + Final Polish (Sessions 46-55)

> **DSA Track A:** Graphs coding (20) → Bits/Tries (5)
> **Concept Track:** Deferred topics (OOP remaining 5, SOLID remaining 18)
> Mock interviews: DSA + System Design + Behavioral

---

## Key Rules (for any AI reading this)

1. **3 slots per session. No exceptions.** If DSA takes longer, cut it — don't skip Slot 1.
2. **Slot 1 (concept) always comes first.** The user's weakness is concepts, not just DSA.
3. **~3-4 questions per concept session** is realistic.
4. **Graph micro-concepts are 10 minutes.** Don't dump all 12 at once.
5. **Check revision queue** at start. Due revisions happen in Slot 2.
6. **Track the session number.** Update "Current Status" below after every session.
7. **If user solved independently** (personal laptop), update trackers but still follow slot structure.
8. **Teaching style:** See `rules.md` for scoring, intuition-first approach, transfer building.
9. **DSA rules:** See `dsa/rules.md` for exercise flow, revision system, problem sources.
10. **Mixed DSA:** Every Slot 2 MUST pull from BOTH Track A and Track B. Never do 3 from one track.

---

## Cross-Laptop Sync Protocol

This user works on **multiple laptops**. Each laptop may have a different AI. Here's how to stay in sync:

### At Session START (every laptop, every time):
1. `git pull` the latest branch
2. Read this "Current Status" section — it's the SINGLE SOURCE OF TRUTH
3. Continue from wherever the status says

### At Session END (every laptop, every time):
1. Update "Current Status" below (increment session, update slots completed)
2. `git add` + `git commit` + `git push`
3. The next laptop that pulls will see the updated state

### Split Sessions (user does Slot 1 on laptop A, Slot 2 on laptop B):
- If a session is partially done, "Current Status" shows which slots are completed
- Example: "Session 11: Slot 1 DONE, Slot 2 pending, Slot 3 pending"
- The next AI picks up from the first incomplete slot

### Conflict Resolution:
- If two laptops somehow work on the same session, the one that pushes LAST wins
- Always pull before starting to minimize this risk

---

## Current Status

**Phase: 1 — Closures/HOF/Decorators + Mixed DSA**
**Next Session: 15**
**Last completed: Session 14 (Apr 5, 2026)**

### What's Done So Far
- Sessions 1-2: OOP foundations (20/25 done, 5 deferred to Phase 5)
- Session 3: SOLID principles (8/26 done, remaining deferred to Phase 5)
- Sessions 4-7: DSA Arrays/Two Pointers ONLY — no concept slot (this was the mistake)
- Session 8: Closures (Q1-Q3: scope chain, late binding, loop trap) + DSA (Buy/Sell Stock 10/10, Merge Intervals 8/10) + Graph #3 (adjacency list)
- Session 9: Closures (Q4-Q6: nonlocal, factory functions, make_accumulator 10/10) + DSA (Product Except Self REVISION CLEARED 10/10) + Graph #4 (adjacency matrix)
- Session 10: HOF (Q7 closure-over-variable PASSED, Q8 map/filter/reduce 7/10) + DSA (Sliding Window Max 7/10 brute, optimal blocked on deque) + Graph #5 (degree of a node, in/out-degree)
- Session 11: Q7 closure-over-variable PASSED + Track A: Max Product Subarray 5/10 (revision due Mar 31) + Track B: Reverse Linked List 8/10, Linked List Cycle 9/10 + Graph #6 BFS PASSED
- Session 12 (complete): Decorators basics PASSED + Track A: Next Permutation 8/10 (+ permutation generation warm-up) + Track B: Cycle II 9/10, Middle of LL 10/10 + Graph #7 DFS PASSED
- Session 13: functools.wraps 6/10 + Max Product REVISION CLEARED 10/10 + Trapping Rain Water 6/10 (brute+optimized) + Remove Nth LL 9/10 (both two-pass and one-pass) + Graph #8 BFS vs DFS PASSED
- Session 14: Decorators with arguments PASSED (oral) + Trapping Rain Water REVISION CLEARED 8/10 + Binary Search 9/10 (Track A start) + Add Two Numbers 7/10 (Track B) + Graph #9 Connected Components PASSED
- Graph micro-concepts #1-#9: PASSED

### DSA Track Status
- **Track A:** Arrays done → Binary Search 1/10 started
- **Track B:** Linked List 6/12 (B1 rotation in progress)

### Active Revision Queue
- Sliding Window Maximum OPTIMAL — blocked until Stacks/Queues (B2) covers deque (~Session 15-17)

### Also Created This Session
- Matrix problem files: Set Matrix Zeroes (LC #73), Rotate Image (LC #48), Spiral Matrix (LC #54) — to be mixed into future sessions
- `dsa/PATTERN_REFERENCE.md` — comprehensive 32-pattern, ~200-problem reference with cross-DS branching, LeetCode/GFG links, difficulty tags, parent problems marked
