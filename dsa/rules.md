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
