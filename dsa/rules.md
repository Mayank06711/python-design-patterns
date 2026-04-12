# DSA-Specific Rules (extends ../rules.md)

> Master rules live in `../rules.md`. This file adds DSA-specific conventions.

---

## Per-Session Problem Count (EFFECTIVE SESSION 18 — user directive Apr 12, 2026)

**Every DSA session = 8 problems from the SAME pattern.** No cross-pattern mixing.

### Distribution
- **3 Easy** (build confidence, warm up the pattern)
- **3 Medium** (apply the pattern to real problems)
- **2 Hard** (push the pattern to its limit)

### Rules
1. **Single-pattern focus.** If we're on Mono Stack, all 8 are Mono Stack. If we're on Linked List, all 8 are Linked List. Never mix.
2. **If a pattern has fewer than 3 strict "Easy" LC problems** (e.g., Mono Stack, DP, Graphs), take the easiest 3 available regardless of LC tag. Don't force the tag.
3. **Hards can spill into the next session** as "previous pattern hards" if time runs out. They still count toward that pattern's bank.
4. **Slot 1 (concept) and Slot 3 (graph micro) stay untouched** — the user said "can't leave those other things". Only Slot 2 volume changed.
5. **Tracker must be updated after every problem.** Visibility = motivation.

### Why this exists
Before this rule, sessions had 2-3 cross-pattern problems, which felt slow and prevented pattern solidification. User said: "I don't feel like I didn't practice too much... I was not able to solve the easy problem". 8 same-pattern problems per session = enough reps to feel the pattern before moving on.

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
3. User writes their **approach in STEP 1 section** using the 4-part format:
   - **WHAT:** Restate the problem in one line (own words)
   - **HOW:** Numbered algorithm steps (specific, not vague)
   - **EDGE CASES:** What could go wrong?
   - **COMPLEXITY:** Time O(?), Space O(?)
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

## Algorithm Fundamentals (NEW — effective Session 15)

> **Rule:** Before solving problems in a new topic, TEACH the core algorithms first.
> Research shows: theory FIRST within each pattern unit, then immediately apply via problems.

### When a new topic starts in Track A, the FIRST session includes:

| Topic | Must Implement From Scratch | Must Understand (concept + complexity) |
|-------|---------------------------|---------------------------------------|
| **Sorting** | Merge Sort, Quick Sort, Heap Sort | Counting Sort, Bucket Sort, Radix Sort |
| **Trees** | Recursive inorder/preorder/postorder, Iterative inorder, BFS level-order | Morris traversal, iterative postorder |
| **Graphs** | BFS, DFS, Dijkstra's, Topological Sort (Kahn's), Union-Find | Bellman-Ford, Kruskal's, Prim's |
| **DP** | Recursion → Memoization → Tabulation pipeline on parent problem | Space optimization (rolling array) |

**Flow:** Teach algorithm (10-15 min) → User implements it as a standalone exercise → THEN solve problems using it.

### Already Covered (retroactive):
- Binary Search: basic algorithm taught in Session 14
- Two Pointers: taught organically via 3Sum, Sort Colors, Trapping Rain Water
- Floyd's Fast/Slow: taught via Cycle Detection
- Kadane's: taught via Maximum Subarray
- Prefix Sum: taught via Subarray Sum K, Product Except Self

## Pattern Learning Cycle (NEW — effective Session 15)

> **Rule:** Every new pattern follows a 3-step cycle. Just solving 2-3 problems is NOT enough.
> Research-backed: 5-7 problems per pattern for solidification.

### Step 1: TEACH the pattern (when first encountered)
- **Recognition triggers:** "When you see X in the problem statement, think pattern Y"
- **Counter-example:** "This LOOKS like Y but ISN'T because..."
- **Parent problem:** Solve together (from `PATTERN_REFERENCE.md`)

### Step 2: APPLY (3-5 problems across sessions)
- Start with obvious applications → progress to disguised variants
- Cross-DS: same pattern on different data structures (e.g., two pointers on arrays AND linked lists)
- Track problem count per pattern in `PATTERN_REFERENCE.md`

### Step 3: VERIFY (after 5+ problems in a pattern)
- Give an UNLABELED problem — user must identify the pattern in 2 min before coding
- If user can't identify → pattern is NOT learned yet, do 2 more problems
- Once identified correctly → pattern is solidified

### Pattern Coverage Tracking
- Maintained at the bottom of `PATTERN_REFERENCE.md`
- Format: Pattern | Problems Solved | Target (5-7) | Status
- Teacher checks this when selecting problems — prioritize under-covered patterns

## Pattern Recognition Drills (NEW — effective Session 18)

> **Rule:** Every 4th session, Slot 2 becomes a mixed drill.
> This builds the interview skill of identifying patterns under pressure.

### How Drills Work
1. Slot 2 gets 3 unlabeled problems from patterns already covered
2. For each problem, user has **2 minutes** to:
   - Name the pattern
   - Explain WHY (what triggered the recognition)
3. THEN code the solution (scored normally)
4. Problems deliberately mix patterns from different topics

### Drill Schedule
- First drill: Session 18 (by then ~6 patterns covered)
- Then every 4th session: 22, 26, 30, 34, ...
- Slot 1 (concept) and Slot 3 (graph) stay unchanged during drills

### Scoring Drills
- Same /10 scoring per problem
- BONUS: +1 if pattern identified correctly in under 2 min (no hints)
- This rewards pattern recognition, not just coding ability

## Exercise File Template (MUST follow for every new problem)

Every exercise file MUST use this exact structure:

```python
"""
PROBLEM: <Problem Name>
LeetCode #<number>: https://leetcode.com/problems/<slug>/

<Problem description>

CONSTRAINTS:
- <constraint 1>
- <constraint 2>

DIFFICULTY: Easy/Medium/Hard
TIME LIMIT: 5/8/12 minutes (Easy/Medium/Hard)
STARTED:
COMPLETED:
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: <Restate problem in one line, your own words>
# 2. HOW: <Numbered algorithm steps — specific, not vague>
# 3. EDGE CASES: <What could go wrong?>
# 4. COMPLEXITY: Time O(?), Space O(?)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================
```

**Rules:**
- No skeleton code, no class hints — user designs everything from scratch
- User fills STEP 1 (approach comments) FIRST → teacher evaluates → THEN user codes STEP 2
- STARTED/COMPLETED timestamps filled by teacher when user begins/finishes
- Hints available but cost marks per scoring system

## Daily Graph Exposure (CRITICAL — starts immediately)
- Even while working on Arrays/Two Pointers/etc., solve **1 easy graph problem per day**
- Before graph coding starts, teach graph THEORY first:
  - What is a graph? Nodes, edges, directed vs undirected
  - Representations: adjacency list vs adjacency matrix
  - BFS vs DFS — when to use which and WHY
  - Connected components, cycles, topological sort (conceptual)
- Oral questions to build graph intuition alongside daily problems
- This ensures graph familiarity is built gradually, not crammed later

## Problem Sources
- **Primary:** Striver's SDE Sheet (Take U Forward) — 79 core problems covering all patterns
  - Link: https://takeuforward.com/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/
  - Cross-reference Striver problem # in tracker when applicable
- **Secondary:** LeetCode top interview questions, Blind 75
- Every problem includes LeetCode link for profile building

## Specialized Teacher Roles
See `../rules.md` Rule 3 for the full DSA teacher table. Each folder = different persona.
