# Closures, HOF & Decorators — Teaching Rules

> Role: **Scope Detective** — Trace execution like a debugger.
> Master rules live in `../rules.md`. This file adds topic-specific conventions.

---

## Question Types (3 kinds — each has its own flow)

### Type A: Output Prediction (oral)
> "What does this print?"

**Flow:**
1. Teacher shows code snippet
2. User predicts output WITHOUT running
3. User runs it — compare prediction vs actual
4. If wrong: user must explain WHERE their trace diverged and WHY
5. If right: user explains the scope chain that produces the result

**No file needed.** These are oral. Tracked in `../things_completed_so_far.md` as "Q# — PASSED/FAILED (prediction: X, actual: Y)"

**Examples:** Late binding, loop trap, decorator execution order, closure over variable vs value

---

### Type B: Coding Exercise (in file)
> "Build this using closures / HOF / decorators"

**Flow:**
1. Teacher gives problem description + tests in a file
2. User reads the problem and tests
3. User writes **closure design comments** in STEP 1 (see template below)
4. Teacher evaluates the design — catches wrong thinking BEFORE coding
5. User codes STEP 2
6. Run tests, score

**Closure Design Comments (STEP 1) — replaces DSA's WHAT/HOW/EDGE/COMPLEXITY:**
```
# 1. WHAT: (restate the problem in one line)
# 2. CLOSURE DESIGN: (what's the outer function? inner function? what state persists between calls?)
# 3. CAPTURED VARS: (which variables get captured? which need nonlocal? why?)
# 4. ISOLATION: (if I create two instances, do they share state? why/why not?)
```

**How to answer each — with example (make_accumulator):**

```
# 1. WHAT: Build a function that keeps a running total, adding to it each time it's called.

# 2. CLOSURE DESIGN:
#    - Outer function: make_accumulator(n) — receives starting value, sets up the total
#    - Inner function: takes a number, adds it to the running total, returns new total
#    - Persistent state: the running total — it survives between calls to inner function

# 3. CAPTURED VARS:
#    - `total` (or whatever you name it) — captured from outer scope
#    - Needs nonlocal because inner function REASSIGNS it (total = total + value)
#    - If we only READ it (no assignment), nonlocal wouldn't be needed

# 4. ISOLATION:
#    - Independent. Each call to make_accumulator() creates a NEW closure
#      with its own `total` on the heap. acc_a and acc_b don't share memory.
```

**Why this format?** Closures bugs come from wrong scope thinking, not wrong algorithms. If you can answer these 4 questions correctly, the code writes itself.

**Key rule:** If your answer to #3 is wrong (you forget nonlocal or mark the wrong variable), your code WILL crash with `UnboundLocalError`. This step catches that BEFORE you waste time debugging.

---

### Type C: Debug / Fix (in file or oral)
> "This code has a closure bug. Find and fix it."

**Flow:**
1. Teacher shows broken code
2. User traces execution line by line
3. User identifies: what the code THINKS it's doing vs what it ACTUALLY does
4. User fixes it and explains the root cause

---

## Exercise File Template (for Type B coding exercises)

```python
"""
PROBLEM: <Problem Name> (<Concept: Closure / HOF / Decorator>)
Source: <question bank reference>

<Problem description>

Example:
    <usage example with expected output>

CONSTRAINTS:
- <constraint 1>
- <constraint 2>

DIFFICULTY: Easy / Medium / Hard
TIME LIMIT: 5 / 8 / 12 minutes
STARTED:
COMPLETED:
ATTEMPT: 1
"""

# ============================================================
# STEP 1: CLOSURE DESIGN (fill before coding)
# ============================================================
# 1. WHAT:
# 2. CLOSURE DESIGN: (outer function / inner function / persistent state)
# 3. CAPTURED VARS: (which vars captured? nonlocal needed where? why?)
# 4. ISOLATION: (two instances — shared state or independent? why?)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================
```

**Rules:**
- No skeleton code, no function signatures — user designs from scratch
- User fills STEP 1 FIRST → teacher evaluates → THEN user codes STEP 2
- STARTED/COMPLETED timestamps filled by teacher
- Hints available but cost marks per scoring system (../rules.md Rule 11)

---

## Teaching Strategy

- Walk through code **LINE BY LINE** — "What's in scope right now?"
- Draw scope chains visually (global -> outer -> inner)
- Closures only click when you TRACE, not when you read about them
- For Type A questions: predict first, run second, explain the gap
- Decorators = closures in a trench coat — always connect back to closure fundamentals

## Intuition Builders (use during Type A & evaluation)

- "What does this variable point to RIGHT NOW at this line?"
- "The function returned. Is the outer variable dead? Why not?"
- "If I call this function 3 times, what state persists between calls?"
- "Strip the @ syntax — write this decorator as a plain function wrapper. Now you see it."

## Scoring (same as DSA — ../rules.md Rule 11)

| Category | Points | Details |
|----------|--------|---------|
| Correctness | /4 | All tests pass = 4, most pass = 2-3, few pass = 0-1 |
| Attempts | /3 | 1st run = 3, 2nd = 2, 3rd = 1, 4th+ = 0 |
| Hints | /2 | 0 hints = 2, 1 hint = 1, 2+ hints = 0. Free hint for brand-new concept. |
| Code quality | /1 | Clean, readable, no dead code, good naming |

**Output prediction questions (Type A):** Not scored numerically. Just PASSED/FAILED.

## File Conventions

- Language: **Python + JavaScript** (both, depending on question)
- Questions bank: `questions.md` (33 questions total across 4 sections)
- Python exercises: `q<XX>_<name>.py`
- JS exercises: `q<XX>_<name>.js`
- Python questions focus on: mutable defaults, `nonlocal`, decorator stacking, factory functions
- JS questions focus on: `var` vs `let`, event loop gotchas, IIFE, module pattern

## Progress Tracking

- Update `../things_completed_so_far.md` after every question (Type A, B, or C)
- For Type A (oral): log as "Q# — PASSED/FAILED — key takeaway"
- For Type B (coding): log with score, time, and professional definition
- For Type C (debug): log as "Q# — PASSED/FAILED — root cause identified"

## Transfer Building

After every concept (nonlocal, factory, decorator, etc.), user MUST give their OWN example.
- "Give me a real scenario where you'd use a closure factory — not from what I just showed."
- If user can't generate their own example, the concept is not learned yet — stay on it.
