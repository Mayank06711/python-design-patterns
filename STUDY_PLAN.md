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
| **Slot 1: Core Concept** | 45-60 min | Current concept topic (see Phase below) | Always comes FIRST. Teach concept → exercise → user gives own example. |
| **Slot 2: DSA** | 60-90 min | 2-3 problems from current DSA chapter | Check `dsa/revision_queue.md` first — due revisions replace one new problem. |
| **Slot 3: Graph Micro** | 10-15 min | One micro-concept from `dsa/rules.md` graph table | Last thing in session. ONE concept only. User gives own example to pass. |

**Session start checklist:**
1. Pull latest branch
2. Check revision queue — do due revisions in Slot 2 before new problems
3. Check which **Phase + Session** we're in (see below)
4. Follow the 3-slot structure

---

## Phase 1: Closures + Arrays/Binary Search (Sessions 8-15)

> **Concept Track:** Closures / HOF / Decorators (33 questions)
> **DSA Track:** Finish Arrays (8 left) → Start Binary Search (10)
> **Graph Track:** Micro-concepts #1 through #6

**We are currently HERE. Session 8 is next.**

| Session | Slot 1: Closures/HOF/Decorators | Slot 2: DSA | Slot 3: Graph |
|---------|--------------------------------|-------------|---------------|
| **8** | What is a closure? Scope chain. Variable lookup. (3-4 Qs) | Arrays: 2-3 remaining problems | #1: What is a graph? Nodes + edges |
| **9** | Closure practical: `nonlocal`, closures in loops, factory functions (3-4 Qs) | Arrays: finish remaining + revision if due | #2: Directed vs Undirected |
| **10** | Higher-Order Functions: map, filter, reduce from scratch (3-4 Qs) | Binary Search: concept teach + first 2 problems | #3: Adjacency list |
| **11** | Writing your own HOFs, callbacks, function composition (3-4 Qs) | Binary Search: 2-3 problems | #4: Adjacency matrix |
| **12** | Decorators basics: @syntax, wrapping, functools.wraps (3-4 Qs) | Binary Search: 2-3 problems | #5: Degree of a node |
| **13** | Decorators advanced: with args, stacking, class decorators (3-4 Qs) | Binary Search: finish remaining | #6: BFS concept |
| **14** | Closures + HOF + Decorators capstone exercise (full application) | Linked List: concept teach + first 2 problems | — (capstone takes more time) |
| **15** | Quiz: 30-40 MCQ + written on Closures/HOF/Decorators | Linked List: 2-3 problems | — |

---

## Phase 2: SQL + Linked List/Stacks/Sorting (Sessions 16-23)

> **Concept Track:** SQL & Indexing (35 questions)
> **DSA Track:** Linked List (12) → Stacks/Queues (10) → Sorting (8)
> **Graph Track:** Micro-concepts #7 through #12

| Session | Slot 1: SQL & Indexing | Slot 2: DSA | Slot 3: Graph |
|---------|----------------------|-------------|---------------|
| **16** | SQL basics: SELECT, WHERE, JOINs, NULL handling (4-5 Qs) | Linked List: continue | #7: DFS concept |
| **17** | JOINs deep dive: LEFT/RIGHT/FULL/CROSS/SELF + practice (4-5 Qs) | Linked List: continue | #8: BFS vs DFS — when which |
| **18** | Aggregation: GROUP BY, HAVING, subqueries (4-5 Qs) | Linked List: finish | #9: Connected components |
| **19** | Window functions: ROW_NUMBER, RANK, LAG, LEAD, running totals (4-5 Qs) | Stacks/Queues: concept + first problems | #10: Cycles |
| **20** | CTEs, recursive CTEs, temp tables (4-5 Qs) | Stacks/Queues: continue | #11: DAG + Topological sort |
| **21** | Indexing: B-tree internals, EXPLAIN plans, query optimization (4-5 Qs) | Stacks/Queues: finish | #12: Weighted graphs |
| **22** | Composite indexes, covering indexes, index pitfalls (3-4 Qs) | Sorting: concept + problems | — |
| **23** | SQL capstone + quiz | Sorting: finish | — |

---

## Phase 3: Rate Limiting + Trees/Heaps (Sessions 24-30)

> **Concept Track:** Rate Limiting (27 questions)
> **DSA Track:** Trees/BST (15) → Heaps (8)
> **Graph Track:** Start easy graph CODING problems (theory done)

| Session | Slot 1: Rate Limiting | Slot 2: DSA | Slot 3: Extra |
|---------|----------------------|-------------|---------------|
| **24** | Rate limiting concepts: why, where, types of limits (3-4 Qs) | Trees: concept teach + traversals | Graph: first easy coding problem |
| **25** | Token Bucket + Leaky Bucket algorithms (4-5 Qs) | Trees: BST problems | Graph: easy problem |
| **26** | Fixed Window + Sliding Window algorithms (4-5 Qs) | Trees: continue | Graph: easy problem |
| **27** | Sliding Window Log + comparison of all 5 algorithms (4-5 Qs) | Trees: finish | Graph: easy problem |
| **28** | Distributed rate limiting, Redis-based, race conditions (4-5 Qs) | Heaps: concept + problems | Graph: easy problem |
| **29** | Rate limiting capstone: implement 2-3 algorithms (3-4 Qs) | Heaps: finish | — |
| **30** | Rate limiting quiz | Recursion/Backtracking: concept + start | — |

---

## Phase 4: System Design + Recursion/Greedy/DP (Sessions 31-42)

> **Concept Track:** System Design (27 questions)
> **DSA Track:** Recursion/Backtracking (12) → Greedy (8) → DP start (30)

| Session | Slot 1: System Design | Slot 2: DSA |
|---------|----------------------|-------------|
| **31** | SD fundamentals: CAP theorem, scaling, load balancing | Recursion/Backtracking: continue |
| **32** | SD: URL Shortener (full design) | Recursion/Backtracking: finish |
| **33** | SD: Chat/Messaging System | Greedy: concept + problems |
| **34** | SD: Rate Limiter (connects to Phase 3!) | Greedy: finish |
| **35** | SD: Notification System | DP: 1D basics (Climbing Stairs, House Robber) |
| **36** | SD: News Feed / Timeline | DP: 2D grid (Unique Paths, Min Path Sum) |
| **37** | SD: Distributed Cache | DP: Knapsack family |
| **38** | SD: Search Autocomplete | DP: String DP (LCS, Edit Distance) |
| **39** | SD: Payment System | DP: LIS family |
| **40** | SD: Video Streaming | DP: Interval DP |
| **41** | SD capstone: mock design interview | DP: Tree DP + finish |
| **42** | SD quiz | DP: revision of weak patterns |

---

## Phase 5: Graph Coding + Final Polish (Sessions 43-50)

> **DSA Track:** Graphs coding (20) → Bits/Tries (5)
> **Concept Track:** Deferred topics (OOP remaining 5, SOLID remaining 18)

| Session | Focus |
|---------|-------|
| **43-44** | Graph: BFS problems (3-4) |
| **45-46** | Graph: DFS problems (3-4) |
| **47** | Graph: Topological Sort problems |
| **48** | Graph: Shortest path (Dijkstra/Bellman-Ford) |
| **49** | Graph: Union-Find + advanced |
| **50** | Bits/Tries (5 problems) |
| **51** | OOP deferred: Observer, Decorator, __slots__, Metaclasses, MI pitfalls |
| **52** | SOLID remaining: quick-fire 18 questions |
| **53-55** | Mock interviews: DSA + System Design + Behavioral |

---

## Key Rules (for any AI reading this)

1. **3 slots per session. No exceptions.** If DSA takes longer, cut it — don't skip Slot 1.
2. **Slot 1 (concept) always comes first.** The user's weakness is concepts, not just DSA.
3. **~4 questions per concept session** is realistic. Not 33 in one day.
4. **Graph micro-concepts are 10 minutes.** Don't dump all 12 at once.
5. **Check revision queue** at start. Due revisions happen in Slot 2.
6. **Track the session number.** Update "Current Status" below after every session.
7. **If user solved independently** (personal laptop), update trackers but still follow slot structure.
8. **Teaching style:** See `rules.md` for scoring, intuition-first approach, transfer building.
9. **DSA rules:** See `dsa/rules.md` for exercise flow, revision system, problem sources.

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
- Example: "Session 8: Slot 1 DONE, Slot 2 pending, Slot 3 pending"
- The next AI picks up from the first incomplete slot

### Conflict Resolution:
- If two laptops somehow work on the same session, the one that pushes LAST wins
- Always pull before starting to minimize this risk

---

## Current Status

**Phase: 1 — Closures + Arrays/Binary Search**
**Next Session: 8**
**Session 8 Progress: Not started**
**Last completed: Session 7 (Day 7, Mar 22, 2026)**

### What's Done So Far
- Sessions 1-2: OOP foundations (20/25 done, 5 deferred to Phase 5)
- Session 3: SOLID principles (8/26 done, remaining deferred to Phase 5)
- Sessions 4-7: DSA Arrays/Two Pointers ONLY — no concept slot (this was the mistake)
- Graph micro-concepts #1 and #2: PASSED (WhatsApp example — nodes=contacts, edges=who can message, undirected)

### Active Revision Queue
- Product of Array Except Self (LC #238) — 5/10 — due Mar 25, 2026
