# DSA-Specific Rules (extends ../rules.md)

> Master rules live in `../rules.md`. This file adds DSA-specific conventions.

---

## File Conventions
- Language: **C++** with `#include <bits/stdc++.h>`
- Each file has the question commented at the top
- User writes solution ONLY inside the `Solution` class
- Test cases in `main()` are PRE-WRITTEN — user does NOT touch them
- File naming: `XX_problem_name.cpp` (numbered for difficulty order)

## Intuition-First DSA Approach
1. **Start with brute force** — "How would you solve this with no constraints?"
2. **Feel the pain** — "This is O(n^2). Where's the repeated work?"
3. **Discover the optimization** — Guide toward the pattern, don't hand it over
4. **Verify understanding** — "Explain back to me WHY this works"
5. **Code it** — Only now write in the Solution class
6. **Test it** — Compile, run, check test output

## Progress Tracking
- Update BOTH trackers after every question:
  - `../things_completed_so_far.md` (master tracker)
  - `./things_completed_so_far.md` (DSA-specific with LC# details)

## Transfer Building
- After teaching a pattern (two-pointer, sliding window, etc.), user MUST identify where ELSE this pattern applies
- "Give me another problem where you'd use this same technique" — before moving to next problem
- Pattern recognition only works if the user can spot the pattern in NEW problems, not just the one taught

## Exercise Format
- Problem description + tests ONLY — no skeleton code beyond the Solution class shell
- User reads tests, designs the approach, writes solution from scratch
- Hints available but cost marks per scoring system

## Specialized Teacher Roles
See `../rules.md` Rule 3 for the full DSA teacher table. Each folder = different persona.
