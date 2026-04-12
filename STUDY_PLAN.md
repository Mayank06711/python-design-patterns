# Interview Prep: Structured Study Plan

> **READ THIS FIRST** — Every AI on every laptop reads this file at session start.
> Target: Google-level interview readiness
> Languages: Python (concepts + DSA local), C++ (DSA on LeetCode)
> Total: 346 questions (173 concept + 173 DSA) — expanded with Striver/NeetCode/Blind75 children

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

**Each session Slot 2:** Target **4-5 problems** using parent+child grouping:
- 1-2 Track A (new pattern OR child of recently learned pattern)
- 2-3 Track B (problems user knows from C++ — but SOLVE fresh in Python, not just translate)
- Revision if due (replaces 1 problem, ~10 min)
- When a new pattern is taught: next 1-2 sessions MUST include 2-3 children of that pattern
- Minimum 3 problems per session. Never fewer.

### Track A — Primary (go in order)

| Priority | Topic | Problems | Algo Fundamentals (first session) | Est. Sessions |
|----------|-------|----------|----------------------------------|---------------|
| 1 | Arrays/Two Pointers (finish) | 3 remaining (matrix) | — (already covered) | 1-2 |
| 2 | Binary Search | 10 + 6 BS-on-answer = 16 | Basic BS taught S14. Variants: rotated, answer-space, 2D | 5-6 |
| 3 | Sorting | 8 | **Implement: Merge Sort, Quick Sort, Heap Sort.** Concept: Counting/Bucket Sort | 4-5 |
| 4 | DP | 30 | **Recursion → Memo → Tabulation pipeline on 0/1 Knapsack parent** | 12-15 |
| 5 | Graphs (coding) | 20 | **Implement: BFS, DFS, Dijkstra, Topo Sort, Union-Find.** Concept: Bellman-Ford, Kruskal's, Prim's | 10-12 |
| 6 | Bits/Tries | 5 | XOR properties, Trie implementation | 2 |

### Track B — Refresh (rotate every 2-3 sessions)

| Rotation | Topic | Problems | Algo Fundamentals (first session) | Python Focus |
|----------|-------|----------|----------------------------------|-------------|
| B1 | Linked List | 12 + 3 new = 15 | Dummy head technique (taught S14) | Pointer-free approach, Python idioms |
| B2 | Stacks/Queues | 10 + 5 new = 15 | **Monotonic stack/deque pattern.** collections.deque | Monotonic patterns, sliding window, stack simulation |
| B3 | Trees/BST | 15 | **Implement: recursive + iterative traversals, BFS level-order** | BST properties, validate BST |
| B4 | Recursion/Backtracking | 12 | **Backtracking template: base→loop→pick→recurse→unpick** | Generator patterns, memoization |
| B5 | Heaps | 8 | **heapq module, heapify, Top-K template** | Two-heap technique |
| B6 | Greedy | 8 | Exchange argument proof technique | Proof of correctness |

**Rotation rule:** Spend 3-4 sessions on each Track B topic (6-8 problems), then rotate to next.
When Sliding Window Max revision comes due (after B2 deque), do it immediately.

### Pattern Learning Cycle — Parent + Child Format (applied to every new pattern)

```
Session N:
  1. TEACH: recognition triggers + counter-example (10 min)
  2. PARENT: solve the canonical problem for this pattern (15-20 min)
  3. CHILD 1: same pattern, simpler or same difficulty (10-12 min, same session if time)

Session N+1 or N+2:
  4. CHILD 2-3: same pattern, new twist (circular, 2D, reverse direction)
  5. VERIFY: unlabeled problem — user identifies pattern in 2 min
     → If can't identify → 2 more children before moving on

Target: 4-6 problems per pattern before moving to next pattern
Children should be FAST — pattern is known, only the twist is new
```

### Concrete Session Plan

**Sessions 11-16: DONE** (see "What's Done So Far" below)

| Session | Slot 1: Concept | Slot 2: DSA (target 4-5 problems) | Graph | Notes |
|---------|----------------|-----------------------------------|-------|-------|
| **17** | Deco quiz (capstone) | **Algo: deque** + Rotated Array REVISION + NGE I (496, stack child) + NGE II (503, stack child) + Sliding Window Max REVISION | #12: Weighted | Deque unlocks SWM revision |
| **18** | SQL: SELECT, WHERE | BS: First & Last Position (34) + BS: Find Peak Element (162) + Stack: Stock Span (901) + LL: Intersection (160) | Graph code #1 | |
| **19** | SQL: JOINs basics | BS: Search 2D Matrix (74) + BS: Find Min Rotated (153) + Stack: Asteroid Collision (735) + LL: Palindrome (234) | Graph code #2 | |
| **20** | SQL: JOINs deep | BS-on-answer parent: Koko Bananas (875) + BS-on-answer child: Ship Packages (1011) + Stack: Valid Parentheses (20) + LL: Reorder List (143) | Graph code #3 | |
| **21** | SQL: GROUP BY, HAVING | BS-on-answer child: Min Days Bouquets (1482) + Stack: Largest Rectangle (84, HARD) + LL: Copy Random Ptr (138) + Stack: Min Stack (155) | Graph code #4 | **DRILL: 1 unlabeled** |
| **22** | SQL: subqueries, CTEs | BS Hard: Split Array (410) or Median Two Arrays (4) + Stack: Decode String (394) + LL: Reverse k-Group (25, HARD) + LL: Sort List (148) | Graph code #5 | |
| **23** | SQL: indexing, EXPLAIN | **Sorting: algo fundamentals** (Merge Sort, Quick Sort) + Stack: Eval RPN (150) + LL: Merge k Sorted (23, HARD) | Graph code #6 | **DRILL: 1 unlabeled** |
| **24** | SQL: window functions | Sorting: 2 problems + Stack: LRU Cache (146) + Trees start: algo fundamentals (traversals) | Graph code #7 | |
| **25** | SQL: optimization, query plans | Sorting: 2 problems + Trees: Diameter (543) + Trees: Level Order (102) | Graph code #8 | **DRILL: 1 unlabeled** |
| **26** | SQL quiz (capstone) | Sorting: 2 finish + Trees: Validate BST (98) + Trees: LCA (236) | Graph code #9 | |
| **27+** | Rate Limiting start | DP begins + Trees continue + Recursion/BT start (B4) | Graph code #10+ | See Phase 3 |

> **Key changes from old plan (effective Session 17):**
> - **4-5 problems per Slot 2** instead of 2-3
> - **Parent + Child grouping** — when a pattern is taught, next 1-2 sessions include its children
> - **Problems sourced from:** Striver SDE Sheet, NeetCode 150, Blind 75, LeetCode FAANG tags
> - Drill sessions every 4th session (21, 25, 29...)
> - Pattern coverage tracked in `PATTERN_REFERENCE.md`
> - Problems that appear in 3+ curated lists are highest priority

---

## Pattern Status Map — All 32 Patterns

> **Source of truth for ALL patterns + problems:** [`dsa/PATTERN_REFERENCE.md`](dsa/PATTERN_REFERENCE.md) (32 patterns, ~200 problems with parent + variants + cross-DS branching).
> This file (STUDY_PLAN.md) only tracks **what's active right now**. Don't duplicate the catalog.
>
> Status legend: ✅ taught & active | 🟢 active (in next 8 sessions) | ⚪ upcoming | 🔒 deferred to later phase

| # | Pattern | Status | Where it lives in STUDY_PLAN | PATTERN_REFERENCE section |
|---|---------|--------|------------------------------|---------------------------|
| 1 | Two Pointers | ✅ | Phase 1 done | §1 |
| 2 | Sliding Window | ✅ | Phase 1 done (SWM optimal blocked on deque) | §2 |
| 3 | Binary Search (classical) | ✅ | Sessions 17-22 (children active) | §3 |
| 4 | Binary Search on Answer | 🟢 | Sessions 20-22 | §3 (extension) |
| 5 | Prefix Sum / Product | ✅ | Phase 1 done | §4 |
| 6 | Monotonic Stack/Queue | ✅ | Sessions 17-21 (children active) | §5 |
| 7 | Merge Intervals | ✅ | Phase 1 partial | §6 |
| 8 | Cyclic Sort | ⚪ | Phase 2 | §7 |
| 9 | LL Reversal (in-place) | ✅ | Sessions 18-22 (children active) | §8 |
| 10 | BFS | ✅ | Graph track + sessions 24-26 | §9 |
| 11 | DFS | ✅ | Graph track + sessions 24-26 | §10 |
| 12 | Backtracking (subsets/perms/combos) | 🔒 | Phase 3 (Track B5) | §11 |
| 13 | Topological Sort | 🟢 | Graph #11 (Session 16-17), then problems S24+ | §12 |
| 14 | Union Find | ⚪ | Phase 3 (graph coding) | §13 |
| 15 | Two Heaps | 🔒 | Phase 3 (Track B5) | §14 |
| 16 | Top-K / Heap | 🔒 | Phase 3 (Track B5) | §15 |
| 17 | K-Way Merge | 🔒 | Sessions 23 (Merge k Lists) | §16 |
| 18 | Kadane's / Subarray | ✅ | Phase 1 done | §17 |
| 19 | Greedy | 🔒 | Phase 3 (Track B6) | §18 |
| 20 | Matrix Traversal | 🟢 | Sessions 17-19 (matrix files exist) | §19 |
| 21 | Divide and Conquer | 🟢 | Session 23 (Merge Sort, Quick Sort) | §20 |
| 22 | Bit Manipulation | 🔒 | Phase 5 | §21 |
| 23 | Trie | 🔒 | Phase 5 | §22 |
| 24 | Graph: Shortest Path | 🔒 | Phase 5 (Dijkstra/Bellman-Ford) | §23 |
| 25 | DP: 0/1 Knapsack | 🔒 | Phase 3 start (S27+) | §24 |
| 26 | DP: Unbounded Knapsack | 🔒 | Phase 3 | §25 |
| 27 | DP: LCS family | 🔒 | Phase 3 | §26 |
| 28 | DP: LIS | 🔒 | Phase 3 | §27 |
| 29 | DP: MCM / Partition | 🔒 | Phase 4 | §28 |
| 30 | DP: Grid / Path | 🔒 | Phase 3 | §29 |
| 31 | DP: Fibonacci / Linear | 🔒 | Phase 3 | §30 |
| 32 | DP: Trees / Bitmask | 🔒 | Phase 4 | §31-32 |

**Active count:** 4 ✅ in maintenance + 6 🟢 actively progressing = 10 patterns being worked on.
The remaining 22 are queued for later phases.

---

## Active Pattern Banks (Sessions 17-27 only)

> **These are the 6 patterns receiving NEW problems in the next 8 sessions.** All other patterns: see PATTERN_REFERENCE.md.
> Every pattern has a parent (teaches the template) and children (apply + twist).
> Sources: Striver SDE/A2Z, NeetCode 150, Blind 75, LeetCode FAANG frequency tags.
> ✅ = done, ⏳ = revision pending, 🔒 = blocked on prerequisite

### Monotonic Stack (taught Session 16)

| Role | LC# | Problem | Diff | Sources | FAANG | Status |
|------|-----|---------|------|---------|-------|--------|
| Parent | 739 | Daily Temperatures | Med | NeetCode, Blind 75 | Google, Amazon | ✅ 8/10 |
| Child | 496 | Next Greater Element I | Easy | Striver, NeetCode | Amazon | S17 |
| Child | 503 | Next Greater Element II (circular) | Med | Striver | Amazon | S17 |
| Child | 901 | Online Stock Span | Med | Striver | Amazon | S18 |
| Child | 735 | Asteroid Collision | Med | NeetCode 150 | Google, Amazon | S19 |
| Child | 402 | Remove K Digits | Med | Striver | Google, Microsoft | optional |
| Child | 907 | Sum of Subarray Minimums | Med | Striver A2Z | Amazon | optional |
| Boss | 84 | Largest Rectangle in Histogram | Hard | NeetCode, Striver | Amazon, Google, Meta | S21 |
| Boss | 85 | Maximal Rectangle | Hard | Striver | Amazon, Google | after 84 |

### Binary Search — Classical (started Session 14)

| Role | LC# | Problem | Diff | Sources | FAANG | Status |
|------|-----|---------|------|---------|-------|--------|
| Parent | 704 | Binary Search | Easy | NeetCode 150 | — | ✅ 9/10 |
| Child | 35 | Search Insert Position | Easy | NeetCode 150 | Google | S18 |
| Problem | 33 | Search in Rotated Sorted Array | Med | NeetCode, Blind 75, Striver | Amazon, Google | ✅ 4/10 ⏳ |
| Child | 34 | Find First and Last Position | Med | NeetCode, Striver | Meta, Amazon, Google | S18 |
| Child | 153 | Find Min in Rotated Sorted Array | Med | NeetCode, Blind 75 | Microsoft, Amazon | S19 |
| Child | 162 | Find Peak Element | Med | NeetCode 150 | Meta, Amazon, Google | S18 |
| Child | 74 | Search a 2D Matrix | Med | NeetCode, Striver | Google, Amazon | S19 |
| Boss | 4 | Median of Two Sorted Arrays | Hard | NeetCode, Blind 75 | Google, Amazon | S22 |

### Binary Search — On Answer (starts Session 20)

| Role | LC# | Problem | Diff | Sources | FAANG | Status |
|------|-----|---------|------|---------|-------|--------|
| Parent | 875 | Koko Eating Bananas | Med | NeetCode, Striver | Google, Amazon | S20 |
| Child | 1011 | Capacity to Ship Packages | Med | Striver A2Z | Amazon, Google | S20 |
| Child | 1482 | Min Days to Make Bouquets | Med | Striver A2Z | Google | S21 |
| Child | 1283 | Smallest Divisor Given Threshold | Med | Striver A2Z | Amazon | optional |
| Child | 1552 | Magnetic Force Between Balls | Med | Striver A2Z | Google | optional |
| Boss | 410 | Split Array Largest Sum | Hard | Striver | Google, Amazon | S22 |

### Stacks & Queues — General (B2, starts Session 17)

| Role | LC# | Problem | Diff | Sources | FAANG | Status |
|------|-----|---------|------|---------|-------|--------|
| Fundamental | 20 | Valid Parentheses | Easy | NeetCode, Blind 75, Striver | Amazon, Google, Meta | S20 |
| Fundamental | 155 | Min Stack | Med | NeetCode, Striver | Amazon, Google | S21 |
| Problem | 150 | Evaluate Reverse Polish Notation | Med | NeetCode 150 | Google, Meta | S23 |
| Problem | 394 | Decode String | Med | Striver | Amazon, Google, Meta | S22 |
| Problem | 232 | Implement Queue using Stacks | Easy | Striver | Amazon | optional |
| Problem | 853 | Car Fleet | Med | NeetCode 150 | Amazon | optional |
| Design | 146 | LRU Cache | Med | NeetCode, Blind 75 | Amazon, Google, Meta | S24 |
| Boss | 239 | Sliding Window Maximum | Hard | NeetCode, Striver | Amazon, Google | ⏳ after deque |
| Boss | 895 | Maximum Frequency Stack | Hard | Striver | Amazon | late |

### Linked List — Remaining (B1, 7/15 done)

| Role | LC# | Problem | Diff | Sources | FAANG | Status |
|------|-----|---------|------|---------|-------|--------|
| Child | 160 | Intersection of Two Lists | Easy | Striver, NeetCode | Amazon, Microsoft | S18 |
| Child | 234 | Palindrome Linked List | Easy | NeetCode, Blind 75 | Google, Amazon | S19 |
| Child | 143 | Reorder List | Med | NeetCode, Blind 75 | Amazon, Google, Meta | S20 |
| Child | 138 | Copy List with Random Pointer | Med | NeetCode, Striver | Amazon, Google, Meta | S21 |
| Child | 92 | Reverse Linked List II (subrange) | Med | NeetCode 150 | Amazon, Google | S22 |
| Child | 148 | Sort List | Med | Striver | Amazon, Google | S22 |
| Boss | 25 | Reverse Nodes in k-Group | Hard | NeetCode, Striver | Google, Microsoft | S22 |
| Boss | 23 | Merge k Sorted Lists | Hard | NeetCode, Blind 75, Striver | Amazon, Microsoft, Meta | S23 |

### Trees & BST (B3, starts ~Session 24)

| Role | LC# | Problem | Diff | Sources | FAANG | Status |
|------|-----|---------|------|---------|-------|--------|
| Fundamental | 102 | Binary Tree Level Order Traversal | Med | NeetCode, Striver | Amazon, Meta | |
| Parent | 543 | Diameter of Binary Tree | Easy | NeetCode, Striver | Amazon, Meta, Google | |
| Parent | 98 | Validate Binary Search Tree | Med | NeetCode, Blind 75, Striver | Amazon, Meta, Google | |
| Parent | 236 | Lowest Common Ancestor | Med | NeetCode, Blind 75 | Meta, Amazon, Google | |
| Child | 235 | LCA of BST | Med | Striver | Meta, Amazon | |
| Child | 199 | Binary Tree Right Side View | Med | NeetCode 150 | Meta, Amazon | |
| Child | 230 | Kth Smallest in BST | Med | NeetCode, Blind 75 | Amazon, Meta | |
| Child | 105 | Construct from Preorder + Inorder | Med | NeetCode, Striver | Amazon, Google | |
| Child | 114 | Flatten Binary Tree to Linked List | Med | Striver | Amazon, Meta | |
| Child | 1448 | Count Good Nodes | Med | NeetCode 150 | Amazon, Google | |
| Boss | 124 | Binary Tree Maximum Path Sum | Hard | NeetCode, Blind 75 | Google, Amazon, Meta | |
| Boss | 297 | Serialize and Deserialize | Hard | NeetCode, Striver | Meta, Amazon, Google | |
| Boss | 968 | Binary Tree Cameras | Hard | Striver | Amazon, Google | optional |

> **For all 32 patterns + ~200 problems with cross-DS variants, recognition triggers, and the parent-problem map → see [`dsa/PATTERN_REFERENCE.md`](dsa/PATTERN_REFERENCE.md).**
> When a new pattern enters the next 8-session window (e.g., Topo Sort moving from 🟢 to 🟢 active), promote its problem bank into this section and update the status map above.

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
**Next Session: 18**
**Last completed: Session 17 complete (Apr 9 + Apr 11-12, 2026) — split across 3 days due to meetings**

### NEW RULE (effective Session 18, per user directive Apr 12)
**DSA Slot 2 = 8 problems from the SAME pattern only.** 3 Easy + 3 Medium + 2 Hard. Never mix patterns. See [dsa/rules.md](dsa/rules.md).

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
- Session 15: Deco stacking + class deco 8.5/10 + Search Rotated Array 4/10 (revision due Apr 7) + Merge Two Sorted Lists 9/10 + Graph #10 Cycles PASSED
- Session 16 (partial): @retry 7/10 + @memoize 8/10 + Monotonic Stack taught + Daily Temperatures 8/10 + Graph #11 DAG/Topo Sort STARTED (needs visual approach)
- Session 17 (split Apr 9 + Apr 11-12): MyDeque 7/10 + SWM optimal revision 7/10 CLEARED + Rotated Array revision 8/10 CLEARED + NGE I 7/10 + NGE II 9/10 + Graph #12 Weighted Graphs PASSED (guitar/Hz example)
- Graph micro-concepts #1-#10, #12: PASSED, #11 still in progress

### DSA Track Status
- **Track A:** Arrays done → Binary Search 2/10 (basic BS + rotated array) — Track A problem skipped this session due to time
- **Track B:** Linked List 7/12 (B1 nearing end), Stacks/Queues 1/10 (B2 started — Daily Temperatures done, monotonic stack taught)

### Active Revision Queue
- Sliding Window Maximum OPTIMAL — blocked until Stacks/Queues (B2) covers deque (~Session 16-17)
- Search in Rotated Sorted Array (4/10) — due Apr 7, 2026

### Session 16 Remaining
- Complete Graph micro #11 (DAG + Topological Sort) — user wants visual/diagram approach
- Build intuition for reverse-skip approach to Daily Temperatures
- Rotated Array revision due tomorrow (Apr 7)

### Also Created
- Matrix problem files: Set Matrix Zeroes (LC #73), Rotate Image (LC #48), Spiral Matrix (LC #54) — to be mixed into future sessions
- `dsa/PATTERN_REFERENCE.md` — comprehensive 32-pattern, ~200-problem reference with cross-DS branching, LeetCode/GFG links, difficulty tags, parent problems marked
