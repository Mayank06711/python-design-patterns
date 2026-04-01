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

| Priority | Topic | Problems | Prereqs | Est. Sessions |
|----------|-------|----------|---------|---------------|
| 1 | Arrays/Two Pointers (finish) | 5 remaining | — | 2-3 |
| 2 | Binary Search | 10 | Arrays comfort | 4-5 |
| 3 | Sorting | 8 | Arrays | 3-4 |
| 4 | DP | 30 | Recursion from Track B | 12-15 |
| 5 | Graphs (coding) | 20 | BFS/DFS from micro-concepts | 8-10 |
| 6 | Bits/Tries | 5 | — | 2 |

### Track B — Refresh (rotate every 2-3 sessions)

| Rotation | Topic | Problems | User's C++ Level | Python Focus |
|----------|-------|----------|-------------------|-------------|
| B1 | Linked List | 12 | Practiced | Pointer-free approach, Python idioms |
| B2 | Stacks/Queues | 10 | Practiced | collections.deque, monotonic patterns |
| B3 | Trees/BST | 15 | Practiced | Recursive + iterative traversals |
| B4 | Recursion/Backtracking | 12 | Practiced | Generator patterns, memoization |
| B5 | Heaps | 8 | Practiced | heapq module, top-K patterns |
| B6 | Greedy | 8 | Some exposure | Proof of correctness |

**Rotation rule:** Spend 2-3 sessions on each Track B topic (4-6 problems), then rotate to next.
When Sliding Window Max revision comes due (after B2 deque), do it immediately.

### Concrete Session Plan

| Session | Slot 1: Concept | Track A | Track B | Graph Micro |
|---------|----------------|---------|---------|-------------|
| **11** | HOF Q7 done + Q9 curry (oral) | Arrays: 1 problem | Linked List: 2 problems (start B1) | #6: BFS concept |
| **12** | Decorators basics: @syntax, wrapping | Arrays: 1 problem | Linked List: 2 problems | #7: DFS concept |
| **13** | Decorators: functools.wraps, metadata | Arrays: 1 problem (finish!) | Linked List: 2 problems | #8: BFS vs DFS |
| **14** | Decorators: with arguments | Binary Search: 1 problem (start) | Linked List: 2 problems (finish B1 rotation) | #9: Connected components |
| **15** | Decorators: stacking, class decorators | Binary Search: 1 problem | Stacks/Queues: 2 problems (start B2) | #10: Cycles |
| **16** | Decorators: advanced + capstone | Binary Search: 1 problem | Stacks/Queues: 2 problems | #11: DAG + Topo sort |
| **17** | Closures/HOF/Deco quiz | Binary Search: 1 problem | Stacks/Queues: 2 problems (finish B2) | #12: Weighted graphs |
| **18** | SQL: SELECT, WHERE, JOINs | Binary Search: 1 problem | Trees: 2 problems (start B3) | Graph coding #1 |
| **19** | SQL: JOINs deep dive | Binary Search: finish | Trees: 2 problems | Graph coding #2 |
| **20** | SQL: GROUP BY, HAVING, subqueries | Sorting: 1 problem (start) | Trees: 2 problems | Graph coding #3 |
| ... | ... continues ... | ... | ... | ... |

> Sessions 20+ follow the same pattern: rotate Track B every 2-3 sessions, advance Track A linearly.
> By Session ~17, Stacks/Queues Track B unlocks Sliding Window Max revision (monotonic deque).

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
**Next Session: 13**
**Last completed: Session 12 FULL (Day 12, Apr 1, 2026)**

### What's Done So Far
- Sessions 1-2: OOP foundations (20/25 done, 5 deferred to Phase 5)
- Session 3: SOLID principles (8/26 done, remaining deferred to Phase 5)
- Sessions 4-7: DSA Arrays/Two Pointers ONLY — no concept slot (this was the mistake)
- Session 8: Closures (Q1-Q3: scope chain, late binding, loop trap) + DSA (Buy/Sell Stock 10/10, Merge Intervals 8/10) + Graph #3 (adjacency list)
- Session 9: Closures (Q4-Q6: nonlocal, factory functions, make_accumulator 10/10) + DSA (Product Except Self REVISION CLEARED 10/10) + Graph #4 (adjacency matrix)
- Session 10: HOF (Q7 closure-over-variable PASSED, Q8 map/filter/reduce 7/10) + DSA (Sliding Window Max 7/10 brute, optimal blocked on deque) + Graph #5 (degree of a node, in/out-degree)
- Session 11: Q7 closure-over-variable PASSED + Track A: Max Product Subarray 5/10 (revision due Mar 31) + Track B: Reverse Linked List 8/10, Linked List Cycle 9/10 + Graph #6 BFS PASSED
- Session 12 (complete): Decorators basics PASSED + Track A: Next Permutation 8/10 (+ permutation generation warm-up) + Track B: Cycle II 9/10, Middle of LL 10/10 + Graph #7 DFS PASSED
- Graph micro-concepts #1-#7: PASSED

### DSA Track Status
- **Track A:** Arrays 12/15 done (3 remaining) → then Binary Search
- **Track B:** Linked List 4/12 (B1 rotation in progress)

### Active Revision Queue
- Sliding Window Maximum OPTIMAL — blocked until Stacks/Queues (B2) covers deque (~Session 15-17)
- Maximum Product Subarray — due Mar 31, 2026
