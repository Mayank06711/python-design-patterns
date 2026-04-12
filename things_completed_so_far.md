# Interview Prep: Master Progress Tracker

> Updated after every question/topic completed. This is your single source of truth.

---

## Overall Progress

| Topic | Total Qs | Done | Remaining | Status |
|-------|----------|------|-----------|--------|
| OOP | 25 | 20 | 5 | In progress |
| SOLID Principles | 26 | 8 | 18 | In progress |
| Closures/HOF/Decorators | 33 | 12 | 21 | In progress |
| SQL & Indexing | 35 | 0 | 35 | Not started |
| Rate Limiting | 27 | 0 | 27 | Not started |
| System Design | 27 | 0 | 27 | Not started |
| DSA — Arrays/Two Pointers | 19 | 12 | 7 | In progress (+3 matrix created, +4 added from C++ cross-check) |
| DSA — Binary Search | 16 | 3 | 13 | In progress (+6 BS-on-answer added from Striver/NeetCode) |
| DSA — Linked List | 15 | 7 | 8 | In progress (+3 added: Reverse II, Sort List, Merge k) |
| DSA — Stacks/Queues | 15 | 1 | 14 | In progress (+5 added: Asteroid, Decode String, Car Fleet, LRU, Max Freq Stack) |
| DSA — Sorting | 8 | 0 | 8 | Not started |
| DSA — Trees & BST | 15 | 0 | 15 | Not started |
| DSA — Heaps | 8 | 0 | 8 | Not started |
| DSA — Recursion/Backtracking | 12 | 0 | 12 | Not started |
| DSA — Greedy | 8 | 0 | 8 | Not started |
| DSA — Dynamic Programming | 30 | 0 | 30 | Not started |
| DSA — Graphs | 20 | 0 | 20 | Not started |
| DSA — Bits/Tries | 5 | 0 | 5 | Not started |
| **TOTAL** | **346** | **62** | **284** | |

---

## Day-wise Log

### Day 1 — Feb 26, 2026

**OOP Foundations Blitz:**
- [x] Q1: Four Pillars (unified analogy) | OOP | Mid | Solved | Used banking + food delivery examples | **Def:** Encapsulation (hide data), Abstraction (hide complexity), Inheritance (reuse via parent-child), Polymorphism (same interface, different behavior).
- [x] Q2: Abstraction vs Encapsulation | OOP | Mid | Solved | "Encapsulation = mechanism, Abstraction = goal" | **Def:** Encapsulation is HOW you hide (private fields + methods); Abstraction is WHY you hide (expose only what matters to the caller).
- [x] Q3: Compile-time vs Runtime Polymorphism | OOP | Mid | Solved | Overloading vs overriding, Python has no true overloading (dynamic typing) | **Def:** Compile-time = method overloading (resolved at compile); Runtime = method overriding (resolved via vtable at runtime). Python only has runtime polymorphism.
- [x] Q4: Diamond Problem & MRO | OOP | Advanced | Solved | Python C3 linearization, C++ vtable + virtual inheritance | **Def:** When a class inherits from two parents sharing a grandparent, creating ambiguity. Python uses C3 linearization (MRO) to resolve; C++ uses virtual inheritance.
- [x] Q5: Inheritance types + is-a vs has-a | OOP | Mid | Solved | 5 types, is-a = inherit, has-a = composition. Minor slip on Q10 (Car/Engine) | **Def:** is-a = inheritance (Dog IS-A Animal); has-a = composition (Car HAS-A Engine). Prefer composition over inheritance when the relationship isn't truly hierarchical.
- **Notes:** Strong on encapsulation vs abstraction distinction. Understands vtable internals. Needs to watch out for "when to use composition" — got tripped on Car(Engine).

**OOP Coding Practice:**
- [x] 01_encapsulation_practice.py | OOP | Mid | Solved | Minor bugs: f-string typo, deepcopy vs copy. Defensive copy understood. | **Def:** Encapsulation = bundle data + methods together, control access via private fields + public getters/setters. Use defensive copies to prevent external mutation.
- [x] 02_inheritance_diamond.py | OOP | Advanced | Solved | Learned super() only follows MRO, need explicit Class.method(self) for both parents. | **Def:** super() calls the NEXT class in MRO, not the parent. For diamond inheritance, MRO is linearized via C3 algorithm.
- [x] 03_polymorphism_practice.py | OOP | Mid | Solved | Bugs: bare `type`, forgot @abstractmethod. | **Def:** Polymorphism = one interface, many implementations. ABC + @abstractmethod enforces the contract; subclasses provide their own behavior.
- [x] 04_composition_vs_inheritance.py | OOP | Mid | Solved | Minor bug: called `eng()` on already-instantiated object. Clean delegation pattern. | **Def:** Composition = object OWNS another object and delegates work to it. More flexible than inheritance — can swap components at runtime.
- [x] 05_all_pillars_combined.py | OOP | Advanced | Solved | Bugs: `*` vs `★`, `valueError`. Dict loop→O(1) lookup. | **Def:** All 4 pillars working together: ABC (abstraction), private fields (encapsulation), subclasses (inheritance), overridden methods (polymorphism).

**OOP Quick-fire (Python-specific):**
- [x] Q6: @property | OOP | Mid | Taught | Pythonic getter/setter, read-only via skipping setter | **Def:** @property makes a method behave like an attribute. Use it for validation, computed values, or read-only fields. Pythonic replacement for getX()/setX().
- [x] Q7: @staticmethod vs @classmethod | OOP | Mid | Taught | static=no args (utility), classmethod=cls (alternative constructors) | **Def:** @staticmethod = no self/cls, utility function namespaced to class. @classmethod = receives cls, used for alternative constructors (e.g., from_json).
- [x] Q8: __str__ vs __repr__ | OOP | Mid | Taught | str=users, repr=devs | **Def:** __repr__ = unambiguous dev representation (always implement first). __str__ = user-friendly display. str() falls back to __repr__ if __str__ missing.

**OOP Advanced Theory:**
- [x] Q9: MRO Deep Dive (super chain) | OOP | Advanced | Solved | Traced DBCA, 6-class diamond (FDBECA). | **Def:** MRO (Method Resolution Order) = the order Python searches for methods. super() = next in MRO of the ACTUAL object's class, not the parent. C3 linearization guarantees: child before parent, left before right.
- [x] Q10: Fields vs Methods in Polymorphism | OOP | Advanced | Solved | Python: both from actual object. Java: fields=reference type. | **Def:** In Python, both field and method lookup use the actual object. In Java, fields resolve at compile-time (reference type) but methods resolve at runtime (actual object via vtable).
- [x] Q11: LSP Rectangle-Square (exercise 06) | OOP | Advanced | Solved | **8/10** — Shape ABC, siblings not parent-child. 1 hint. | **Def:** Liskov Substitution = subclass must be usable wherever parent is expected without breaking behavior. Square inheriting Rectangle violates this — make them siblings under a Shape ABC.
- [x] Q12: Singleton Pattern (exercise 07) | OOP | Advanced | Solved | **8/10** — __new__ + Lock + hasattr guard. | **Def:** Singleton = exactly one instance of a class, globally accessible. Use __new__ + threading.Lock for thread safety. Guard __init__ with hasattr to prevent re-initialization.
- [x] Q13: Factory Pattern (exercise 08) | OOP | Mid | Solved | **9/10** — Dict-based registry, register() for extensibility. | **Def:** Factory = centralized object creation via a registry. Caller says WHAT to create (string key), factory knows HOW. Adding new types requires zero changes to factory code.
- [x] Q14: Strategy Pattern (exercise 09) | OOP | Advanced | Solved | **7/10** — Swappable discount strategies, runtime swap. 3 bugs. | **Def:** Strategy = family of interchangeable algorithms injected into a context class. Context delegates work to the strategy. Swap behavior at runtime without changing the context.
- [x] Q15: Dependency Injection (exercise 10) | OOP | Mid | Solved | **8/10** — Notification system with injected channels. 1 hint. | **Def:** DI = pass dependencies IN from outside instead of creating them inside. The class depends on abstractions (ABC), not concrete implementations. Enables testing, flexibility, and swappability.

### Day 2 — Mar 13, 2026

**SOLID Principles — SRP:**
- [x] Q1: SRP User Registration (exercise 01) | SOLID | Mid | Solved | **8/10** — 5 classes: UserValidator, UserRepository, EmailService, EventLogger, RegistrationService (orchestrator). 3 attempts. Bugs: named attribute `validate` shadowing method, called object as function instead of calling method on object (`self.validate()` vs `self.validator.validate()`), same bug with logger. Own example: Bicycle class handling brakes + chain + wheels = 3 reasons to change. | **Def:** SRP = a class should have only one reason to change. If you can't describe its job without "and", it has too many responsibilities.
- [x] Q2: SRP Invoice Manager (exercise 02) | SOLID | Advanced | Solved | **7/10** — 5 classes: TaxCalculator, DiscountApplier, InvoiceGenerator, EmailSender, InvoiceService (orchestrator). 3 attempts. Bugs: missing return statement (recurring), confused discounted price with discount value, tax on original instead of discounted amount, missing dict key, `//` floor division instead of `/`. 1 hint. Fixed: no more "calling object as function" bug. | **Def:** SRP in practice = split a God class into focused classes, connect them via an orchestrator that delegates but doesn't DO the work.

### Day 3 — Mar 16, 2026

**SOLID Principles — OCP, LSP, ISP, DIP (conceptual):**
- [x] Q3: OCP Conceptual | SOLID | Mid | Taught | Understood: OCP = open for extension (new classes), closed for modification (no touching if/elif). Config changes (rate 18%→20%) are NOT violations. Adding new VARIANTS is where OCP matters. Solved via inheritance, strategy/composition, or registry. OCP + LSP work together. Own example: AI model — chat → image → file attachments = new classes extending base, not modifying. | **Def:** OCP = add new behavior via new classes/strategies, never modify existing working code. if/elif chains for types = violation; polymorphism/strategy = fix.
- [x] Q4: LSP (already covered in OOP Q11) | SOLID | Advanced | Cross-ref | Rectangle-Square exercise. Subclass must honor parent's contract. Already scored 8/10. | **Def:** LSP = any subclass must be substitutable for its parent without breaking behavior. If it can't, make them siblings, not parent-child.
- [x] Q5: ISP Conceptual | SOLID | Mid | Taught | Understood: ISP = don't force clients to implement methods they don't use. If you write `pass` or `raise NotImplementedError`, it's ISP violation. Fix: split fat interfaces into focused ones. Self-corrected from SRP to ISP during example. Own example: Feedback ABC forcing OrderFeedback to implement rate_delivery_partner() — split into ProductRatable, OrderReviewable, DeliveryRatable. | **Def:** ISP = split fat interfaces into small, focused ones. No client should depend on methods it doesn't use. `pass` in abstract method = ISP smell.
- [x] Q6: DIP (already covered in OOP Q15) | SOLID | Mid | Cross-ref | DI exercise with NotificationService. Already scored 8/10. DI = technique (how), DIP = principle (why: depend on abstractions, not concretions). | **Def:** DIP = high-level modules should not depend on low-level modules; both should depend on abstractions. DI is the technique that implements DIP.

**SOLID Capstone — Full Application:**
- [x] Q7: SOLID Capstone — Payment Processing System (exercise 03) | SOLID | Advanced | Solved | **9/10** — 7 classes: PaymentProcessor ABC, CreditCardProcessor, PayPalProcessor, CryptoProcessor, PaymentValidator, TransactionLogger, PaymentService (orchestrator). 2 attempts. Bug: `>= 0` instead of `> 0` in validator (boundary condition). 0 hints. All 5 SOLID principles applied: SRP (each class = one job), OCP (UPIProcessor works with zero changes), LSP (all processors are proper subtypes), ISP (focused interfaces — PaymentProcessor only has process()), DIP (PaymentService depends on abstractions). | **Def:** SOLID in practice = ABC defines the contract, concrete classes extend it, orchestrator depends on abstractions and delegates to focused single-responsibility classes. New behavior = new class, zero modifications.

**SOLID Quiz — 50 Questions (Conceptual Verification):**
- [x] Q8: SOLID Quiz — 50 MCQ + Written | SOLID | Advanced | Scored **48.5/60** (34/40 MCQ + 14.5/20 written). Weak spots identified: (1) OCP vs ISP confusion — OCP = extending system with new types, ISP = interface bloat; (2) DIP mechanics shallow — can't draw dependency arrows correctly, doesn't understand duck typing as DIP; (3) LSP exceptions — raising ValueError breaks parent contract even if return type is correct when no exception. Strengths: SRP rock-solid, OCP+LSP combo understood, orchestrator pattern clear, transfer to new domains (notification system) excellent. | **Def:** Knowing SOLID definitions is not enough — you must identify which principle applies in ambiguous scenarios and explain dependency direction.

### Day 5 — Mar 18, 2026

**DSA — Arrays & Two Pointers:**
- [x] 3Sum (LC #15) | Two Pointers | Medium | **5/10** | Solved in Python | Fix i, two-pointer j/k on sorted subarray. 4 attempts, multiple Python-level bugs (hashable types, dict KeyError, abs() trap, if/elif fall-through). Approach correct from start. | **Def:** 3Sum = fix one element + 2Sum on remainder. Sort first, compare total against 0 directly.

### Day 6 — Mar 19, 2026

**DSA — Arrays & Two Pointers (continued):**
- [x] Sort Colors / Dutch National Flag (LC #75) | Three Pointers | Medium | **9/10** | Solved in Python | 1st run all 10 tests passed. 3 approaches discussed: (1) bucket sort O(n)/O(n), (2) counting sort O(n)/O(1) two-pass, (3) Dutch National Flag one-pass O(n)/O(1). Used low/separator/high pointers — zones: before low=0s, after high=2s, between=1s. Key trap: don't advance separator after swapping with high (unseen value lands there). 1 hint. Clean variable naming. | **Def:** Dutch National Flag = 3-way partition using low/mid/high pointers. Swap 0s left, swap 2s right, 1s stay in middle. One pass, O(1) space.

### Day 7 — Mar 22, 2026

**DSA — Arrays & Two Pointers (continued):**
- [x] Product of Array Except Self (LC #238) | Prefix/Suffix Product | Medium | **5/10** | Solved in Python | 4+ attempts. Approaches: (1) total product + division — disqualified (no division allowed), (2) brute force O(n²), (3) prefix-suffix product O(n)/O(n), (4) **optimized O(1) space** — use output array for left products + single running variable for right product. Key bugs: building right_prod with append in left-to-right loop, computing answer before arrays fully built, infinite loop from i++ inside else. Lesson: build data structures completely before using them. | **Def:** Product Except Self = for each index, answer = (product of all elements left of i) × (product of all elements right of i). Optimal: store left in output array, compute right with a running variable in reverse pass.
- [x] Maximum Subarray / Kadane's (LC #53) | Kadane's Algorithm | Medium | **9/10** | Solved in Python | 1st run all 10 tests passed. 2 approaches: (1) brute force O(n²), (2) Kadane's O(n)/O(1). Running sum + reset to 0 when negative. 1 hint (explained WHY Kadane's works with traced walkthrough). Minor: used `sum` shadowing built-in. Solve time: ~42 min (including intuition discussion). | **Def:** Kadane's = running sum, reset when negative. A negative prefix can never help a future subarray. Track global max as you go. O(n) time, O(1) space.
- [x] **REVISION** 3Sum (LC #15) | Two Pointers | Medium | **10/10** (was 5/10) | Revision CLEARED | 1st run, 0 hints. Sort + fix i + two-pointer + skip dupes. Perfect execution from understanding, not memory.
- [x] Subarray Sum Equals K (LC #560) | Prefix Sum + HashMap | Medium | **7/10** | Solved in Python | 2 runs (1st failed on bad test case — my error). New pattern learned: prefix sum property (subarray sum = prefix[j] - prefix[i-1]). Multiple hints needed (prefix sum concept taught, ordering, {0:1} init). Clean use of `.get()`. | **Def:** Prefix sum + hashmap. Store running prefix sums and their frequencies. At each step, check if (prefix_sum - k) exists in map — that count = number of subarrays ending here with sum k. Init map with {0:1}.

### Day 8 — Mar 24, 2026

**Closures (Session 8, Slot 1):**
- [x] Q1: What is a closure? Scope chain, LEGB | Closures | Mid | Taught | Understood: closure = function + captured variables from enclosing scope. Holds REFERENCE via cell objects on heap, not copy. LEGB = Local → Enclosing → Global → Built-in. Enclosing = where DEFINED, not where CALLED. Own example: API util function with `.then()` chain where callbacks capture `userId`, `method`, `path` from outer scope. | **Def:** A closure is a function that remembers variables from the scope where it was defined, even after that scope has finished executing.
- [x] Q2: Late binding — closure sees latest value | Closures | Mid | Taught | Correctly predicted `print(20)` when `x` changed from 10 to 20 after inner function was created but before it was called. Reason: closure holds reference to cell, not snapshot of value. | **Def:** Late binding = closure reads the variable's value at CALL time, not at definition time, because it holds a reference.
- [x] Q3: Closure-in-loop trap + default arg fix | Closures | Advanced | Taught | Predicted `make_adders()` output wrong initially (thought each gets own `i`), then self-corrected after testing that `for i` reuses one variable. Final answer: all print 14 (i=4 after loop). Struggled with fix (tried local var `j=i` — understood it runs at call time). Got default arg fix `def adder(x, ind=i)` with 1 hint (free — new topic). | **Def:** Closures in loops share ONE variable — all see the final value. Fix: default argument `ind=i` freezes value at definition time because defaults are evaluated when `def` executes.

**DSA — Arrays (Session 8, Slot 2):**
- [x] Best Time to Buy and Sell Stock (LC #121) | Single Pass / Greedy | Easy | **10/10** | Solved in Python | 1st run all 10 tests passed. 0 hints. Approach: track min_price seen so far + compute profit at each step. Initially proposed "find global min then max after it" — caught flaw with [2,7,1,3] counterexample, self-corrected to single-pass greedy. Clean code, minor: function name shadows variable name. Same pattern family as Kadane's (scan + track running state). | **Def:** Track min buy price so far, compute profit at each step, keep running max. One pass O(n), O(1) space. Same greedy scan pattern as Kadane's.
- [x] Merge Intervals (LC #56) | Sort + Merge | Medium | **8/10** | Solved in Python | 1st run all 10 tests passed. 2 hints (missing sort step, end should use max not just take from i). Rewrote from scratch for deeper understanding — passed again. Sort by start, compare each against last in answer list: if overlap (end >= start) extend with max, else push new. Learned: sort eliminates O(n^2) pair comparisons → O(n log n). Python sort: `arr.sort()` in-place, `sorted()` returns new list. | **Def:** Sort intervals by start. Scan left-to-right: if current overlaps last merged (end >= start), extend end with max. Otherwise push new interval. O(n log n). Pattern: sort + single-pass replaces brute-force all-pairs.

**Graph Micro-concept #3:**
- [x] Adjacency List | Graph Theory | Taught | Dict where key = node, value = list of neighbors. For undirected graph, every edge appears TWICE (in both nodes' lists). For directed, only once. WhatsApp = undirected (both see each other), Instagram follow = directed (one-way). Connected graph = reach everyone from any node. Disconnected = isolated groups.

### Day 9 — Mar 25, 2026

**Closures (Session 9, Slot 1):**
- [x] Q4: nonlocal keyword — UnboundLocalError trap | Closures | Mid | PASSED | Understood: Python decides local vs enclosing at compile time based on assignment. `count += 1` inside inner function → Python treats `count` as local → UnboundLocalError. Fix: `nonlocal count` tells Python to look in enclosing scope. nonlocal = skip L, start from E. global = skip L and E, go to G. Own example: notification timer adjusting delay based on severity. | **Def:** `nonlocal` tells Python a variable belongs to the enclosing scope, not local. Required when REASSIGNING a closure variable. Reading without assignment doesn't need it.
- [x] Q5: Factory functions — multiplier pattern | Closures | Mid | PASSED | Each call to factory creates a separate closure with its own captured value on heap. `double = multiplier(2)` and `triple = multiplier(3)` have independent `factor` values. Factories beat two-param functions when one param is fixed early and the other comes later at call time. Own example: discount factory — `diwali_sale = discount(30)`, configure once, use many times.
- [x] Q6: make_accumulator (coding exercise) | Closures | Easy-Medium | **10/10** | 1st run, 0 hints. Factory + nonlocal combined. Clean code: outer sets `running_total`, inner uses `nonlocal` to reassign. Transfer: middleware request timing. | **Def:** Closure factory with mutable state — outer function sets up initial state, inner function modifies it via `nonlocal` and returns updated value. Each factory call = independent closure.

**DSA — Arrays (Session 9, Slot 2):**
- [x] **REVISION** Product of Array Except Self (LC #238) | Prefix/Suffix | Medium | **10/10** (was 5/10) | ✅ CLEARED | 1st run, 0 hints. Wrote optimal O(n)/O(1) from memory. Listed all 3 approaches (brute → two arrays → single array + running r_prod). Pattern retained. | **Def:** For each index, answer = left product × right product. Build left products forward in ans, compute right products backward with running variable. O(n) time, O(1) extra space.

**Graph Micro-concept #4:**
- [x] Adjacency Matrix | Graph Theory | PASSED | 2D grid where matrix[i][j] = 1 if edge exists. Undirected → symmetric matrix (if [i][j]=1 then [j][i]=1). Diagonal = 0. Matrix: O(1) edge lookup, O(n) get-all-neighbors, O(n²) space. List: O(degree) edge lookup, O(degree) get-neighbors, O(V+E) space. Matrix = dense graphs, List = sparse graphs.

**HOF (Session 10, Slot 1):**
- [x] Q8: my_map, my_filter, my_reduce (coding exercise) | HOF | Medium | **7/10** | 21/21 tests passed. map and filter correct from start. Struggled with reduce: initially called func with 1 arg instead of 2 (map thinking), then double-processed first element, then used truthiness instead of None-check for empty list. 3 hints. | **Def:** HOF = function that takes a function as argument OR returns a function. map = transform every item, filter = keep items passing a test, reduce = fold list into single value by combining accumulator + current item with a two-arg function.

**DSA — Arrays (Session 10, Slot 2):**
- [x] Sliding Window Maximum (LC #239) | Sliding Window | Hard | **7/10** | 10/10 brute force O(n*k). 2nd attempt (1st had loop bounds bugs). Identified heap O(n log k) and monotonic deque O(n) approaches conceptually but not comfortable with deque. Added to revision queue (HIGH priority, blocked on deque). | **Def:** Sliding window = fixed-size subarray moving left to right. Brute: scan each window for max. Optimal: monotonic deque maintains candidates in decreasing order, front = current max.

**Graph Micro-concept #5:**
- [x] Degree of a Node | Graph Theory | PASSED | Degree = number of edges connected to a node. Adjacency list: `len(graph[node])` → O(1). Adjacency matrix: `sum(row)` → O(n). Directed graphs: out-degree = edges going out (row sum / list length), in-degree = edges coming in (column sum / scan all lists O(V+E)).

### Day 11 — Mar 28, 2026

**Closures/HOF (Session 11, Slot 1):**
- [x] Q7: Closure over variable vs value (oral) | Closures | Mid | PASSED | Output: `10 20 3`. Closures capture variables, not values. `a` reassigned to 10 (global), `b` reassigned to 20 (enclosing) before `inner()` called. `c=3` is local.

**DSA — Arrays (Session 11, Track A):**
- [x] Maximum Product Subarray (LC #152) | Kadane's variant | Medium | **5/10** | 12/12 on 4th+ attempt. Many hints. Key: negatives flip min↔max, track both prev_max AND prev_min. 3 candidates per step. Global maxi never decreases. Added to revision (due Mar 31).

**DSA — Linked List (Session 11, Track B1 start):**
- [x] Reverse Linked List (LC #206) | 3-pointer | Easy | **8/10** | 7/7. Free hint (first LL in Python) + 1 hint (loop condition, null check). Python: `.next` not `->`, return `prev`.
- [x] Linked List Cycle (LC #141) | Floyd's Tortoise & Hare | Easy | **9/10** | 8/8. Hash map brute first (O(n) space), then Floyd's O(1) space. 1 bug: `or` instead of `and` in while condition (short-circuit logic). 0 hints. | **Def:** Floyd's = slow (1 step) + fast (2 steps). If cycle exists, they MUST meet (gap shrinks by 1 each step). Use `and` for short-circuit safety.

**Graph Micro-concept #6:**
- [x] BFS (Breadth-First Search) | Graph Theory | PASSED | BFS = explore all neighbors (level by level) before going deeper. Uses QUEUE (FIFO) + visited set. Guarantees shortest path in unweighted graphs. Own example: department notification — CEO tells all VPs (level 1), then VPs tell all Directors (level 2), ripples down level by level.

### Day 12 — Apr 1, 2026

**Decorators (Session 12, Slot 1):**
- [x] Decorators Basics | Decorators | Mid | PASSED | Decorator = HOF + closure + `@` syntax. `@decorator` is sugar for `func = decorator(func)`. Universal pattern: `def wrapper(*args, **kwargs)` forwards all args. Own example: `@timer` for request timing, `@sanitize` for input validation.

**DSA — Backtracking (Session 12, warm-up for Track A):**
- [x] Generate Permutations (LC #46) | Backtracking | Medium | PASSED (5/5) | Backtracking template: base case → loop choices → pick → recurse → unpick. Visited list tracks picked elements. O(n! * n) to generate all permutations.

**DSA — Arrays (Session 12, Track A):**
- [x] Next Permutation (LC #31) | Greedy / Lexicographic | Medium | **8/10** | Find break point from right (first ascending), swap with smallest bigger, reverse tail. Lexicographic = number odometer. | **Def:** Next permutation = increment rightmost digit possible, reset everything after to smallest.

**DSA — Linked List (Session 12, Track B continued):**
- [x] Linked List Cycle II (LC #142) | Floyd's Phase 2 | Medium | **9/10** | After Floyd's detects cycle, reset one pointer to head, move both at speed 1 → meet at cycle start. Math: L = nC - x. | **Def:** Floyd's Cycle II = detect meeting → reset one to head → move both speed 1 → meet at cycle entry.
- [x] Middle of Linked List (LC #876) | Fast/Slow Pointers | Easy | **10/10** | Fast moves 2x, slow moves 1x. When fast reaches end, slow at middle. 1-pass O(n).

**Graph Micro-concept #7:**
- [x] DFS (Depth-First Search) | Graph Theory | PASSED | DFS = go deep first then backtrack. Uses STACK (LIFO) or recursion. Recursion IS DFS — call stack handles it naturally. Use cases: detect cycles, topological sort, find all paths, maze solving. Own example: Finding all connections between two people in social network. | **Def:** DFS explores as far as possible along each branch before backtracking. Stack-based or recursive. Does NOT guarantee shortest path (unlike BFS).

### Session 13 — Apr 1, 2026

**Decorators (Session 13, Slot 1):**
- [x] Q10: functools.wraps (coding exercise) | Decorators | Medium | **6/10** | 10/10 tests. Build @cache decorator with metadata preservation. Bug: line 49 uses `.get(key, None)` which checks truthiness, not existence — fails for falsy cached values (0, False, [], ''). Should use `if key in cache_mem:` or `if key not in cache_mem:`. | **Def:** functools.wraps copies metadata (__name__, __doc__, __module__, __annotations__) from original function to wrapper, preserving identity for debugging/logging.

**DSA — Arrays REVISION (Session 13, Slot 2):**
- [x] **REVISION** Maximum Product Subarray (LC #152) | Kadane's variant | Medium | **10/10** (was 5/10) | ✅ CLEARED | 1st run, 0 hints. Track prev_max AND prev_min (negatives flip). 3 candidates: nums[i], prev_max*nums[i], prev_min*nums[i]. Caught test case error (24 vs 6). | **Def:** Track prev_max and prev_min at each step. New_max = max(nums[i], prev_max*nums[i], prev_min*nums[i]). New_min = min(nums[i], prev_max*nums[i], prev_min*nums[i]). Global max = max across all positions.

**DSA — Arrays (Session 13, Track A):**
- [x] Trapping Rain Water (LC #42) | Prefix Max Arrays | Hard | **6/10** | 10/10 both brute O(n^2) and optimized O(n). Core formula: water[i] = min(left_max, right_max) - height[i]. Brute: scan left+right for each index. Optimized: precompute left_max[] and right_max[] arrays in 2 passes. Bugs: typo htg/hgt, range step -1 instead of +1, overcomplicated running max initially. Added to revision (due Apr 4, must do O(1) space two-pointer). | **Def:** Water at each position = min(tallest bar to left, tallest bar to right) - bar height. Precompute both max arrays in O(n) to avoid O(n^2) repeated scans.

**DSA — Linked List (Session 13, Track B):**
- [x] Remove Nth Node From End (LC #19) | Two-pass length | Medium | **9/10** | 10/10 1st run. Two-pass: count length, traverse to (length-n-1), rewire. Edge case: n==length → return head.next. 1 hint (head removal simplification). Follow-up: one-pass with two pointers (gap of n). | **Def:** Find length first, compute position from start = length-n, stop one before to rewire .next. Edge case: removing head when n==length.

**Graph Micro-concept #8:**
- [x] BFS vs DFS Comparison | Graph Theory | PASSED | BFS = queue, level-by-level, guarantees shortest path (unweighted), O(width) space. DFS = stack/recursion, branch-by-branch, no shortest guarantee, O(depth) space. BFS for: shortest path, level-order, ripple problems. DFS for: cycles, topological sort, all paths, maze/backtracking. Own examples: navigation/maps = BFS (shortest route), LinkedIn connection chains = DFS (deep exploration). Key: both traverse any graph; BFS guarantees shortest, DFS guarantees complete exploration with less memory.

### Session 14 — Apr 5, 2026

**Decorators (Session 14, Slot 1):**
- [x] Decorators with Arguments (oral) | Decorators | Advanced | PASSED | 3-level nesting: outer function takes decorator args → returns actual decorator → which returns wrapper. `@repeat(3)` = `repeat(3)` returns decorator, then `@decorator` wraps the function. Own explanation confirmed understanding of why 3 levels needed.

**DSA — Arrays REVISION (Session 14, Slot 2):**
- [x] **REVISION** Trapping Rain Water O(1) space (LC #42) | Two Pointers | Hard | **8/10** (was 6/10) | ✅ CLEARED | Two-pointer O(1) space: if height[left] <= height[right], process left side (right_max >= height[right] >= height[left], so left is bottleneck). Track left_max/right_max, move shorter side inward. | **Def:** Two-pointer O(1): the shorter side is the bottleneck. If height[left] <= height[right], then right_max >= height[left], so water = left_max - height[left]. Process shorter side, move inward.

**DSA — Binary Search (Session 14, Track A start):**
- [x] Binary Search (LC #704) | Binary Search | Easy | **9/10** | 10/10. 1 bug: wrote `middle = (right - left)//2` instead of `left + (right - left)//2` — offset concept (distance from left, must add to left). Overflow-safe formula: avoids int overflow in C++/Java. `<=` because both endpoints must be checked. | **Def:** Binary search = halve search space each step. middle = left + (right-left)//2. If target < mid → right = mid-1, if target > mid → left = mid+1. O(log n).

**DSA — Linked List (Session 14, Track B continued):**
- [x] Add Two Numbers (LC #2) | Dummy Head + Carry | Medium | **7/10** | 10/10. Multiple attempts. Learned dummy head technique (new concept, free hint): create fake node at front, build list after it, return dummy.next. Bugs: (1) initially overwrote result.val without linking nodes, (2) advanced to result.next which was None, (3) missing carry check after loops. | **Def:** Dummy head = create fake node, attach real nodes after it, return dummy.next. For digit addition: process carry at every step, check carry>0 after all loops for extra digit.

**Graph Micro-concept #9:**
- [x] Connected Components | Graph Theory | PASSED | A connected component = group of nodes where every node is reachable from every other within the group. Find all: loop through all nodes, start BFS/DFS from each unvisited node — each fresh traversal = one component. Count of fresh BFS/DFS starts = number of components. Own example: Family tree — members within a family are connected, different families are separate components; marriage merges two components (union). | **Def:** Connected component = maximal set of mutually reachable nodes. Find them by starting BFS/DFS from each unvisited node.

### Session 15 — Apr 3, 2026

**Decorators (Session 15, Slot 1):**
- [x] Decorator Stacking + Class Decorators (exercise 11) | Decorators | Advanced | **8.5/10** | 16/16 tests. Stacking: decorators apply bottom-up (`@A @B def f` = `A(B(f))`), execute top-down. Class decorators: function that takes a class, modifies/wraps it, returns it. `@singleton` class decorator using `__new__` override. 0 hints. | **Def:** Stacking = chain of wrappers, apply bottom-up, execute top-down. Class decorator = function(cls) → modified cls. Common uses: singleton, auto-repr, registry, validation.

**DSA — Binary Search (Session 15, Track A):**
- [x] Search in Rotated Sorted Array (LC #33) | Binary Search | Medium | **4/10** | 12/12 on 3rd+ attempt. 3 bugs: (1) `while(left < right)` → `<=` (missed single-element), (2) strict `<`/`>` → `<=`/`>=` (missed boundary elements), (3) missing `else` in right-sorted branch (infinite loop). Didn't build intuition for WHY one half is always sorted. Added to revision (due Apr 7). | **Def:** Rotated array has exactly 1 break point. `nums[left] <= nums[mid]` → left half sorted. Check if target in sorted range → search there, else search other half. Single pass O(log n).

**DSA — Linked List (Session 15, Track B):**
- [x] Merge Two Sorted Lists (LC #21) | Dummy Head + Compare-and-Pick | Easy | **9/10** | 8/8 1st run. Dummy head pattern (create fake node, build merged list by comparing and picking smaller node, return dummy.next). O(n+m) time, O(1) space — rewiring existing nodes, NOT creating new ones. 0 hints. Transfer: Merge Sort's merge step, Merge K Sorted Lists. | **Def:** Dummy head + compare-and-pick: create fake node, at each step pick smaller of two list heads, advance that pointer. After one exhausted, attach remainder. Return dummy.next.

**Graph Micro-concept #10:**
- [x] Cycle Detection | Graph Theory | PASSED | Undirected: DFS + parent tracking — visiting a non-parent visited node = cycle (back to parent via same edge is NOT a cycle). Directed: 3-state coloring — white (unvisited), gray (in current DFS path), black (fully explored). Gray→gray = back edge = cycle. BFS can detect cycles in undirected graphs but NOT reliably in directed graphs (can't distinguish back edges from cross edges). Kahn's Algorithm (BFS topological sort) can detect cycle existence but not location. Own example: Instagram follow graph (directed cycles possible: A→B→C→A). | **Def:** Undirected = DFS + parent (non-parent visited = cycle). Directed = 3-state DFS (gray→gray = cycle). BFS works for undirected only; Kahn's detects directed cycle existence.

### Session 16 — Apr 6, 2026

**Decorators Advanced (Session 16, Slot 1):**
- [x] Q16: @retry with Exponential Backoff (exercise 12) | Decorators | Advanced | **7/10** | 8/8 tests. 4 attempts. Bugs: (1) UnboundLocalError on `delay` — needed `nonlocal delay` (recognized from Session 9 Q4), (2) off-by-one: `attempt=0` with `<=` gave max_attempts+1 iterations — fixed to `attempt=1`, (3) wrong backoff formula `delay += delay*backoff` instead of `delay = delay*backoff`. 3-level nesting: outer takes config → returns decorator → returns wrapper. Transfer: DB connection retries for transient failures. Known issue: `nonlocal delay` mutates shared state across calls; should use local copy. | **Def:** @retry = 3-level nested decorator. Exponential backoff: delay *= backoff each failure. Re-raise last exception after all attempts exhausted.
- [x] Q17: @memoize Decorator (exercise 13) | Decorators | Medium | **8/10** | 8/8 tests. 2 attempts. Bug: `if cache[key]` tries to ACCESS key (KeyError if missing) instead of checking existence — fixed to `if key in cache:`. Handles falsy values (0, False, '', []) correctly now. Cache exposed via `wrapper.cache = cache`. kwargs handled via `tuple(sorted(kwargs.items()))`. | **Def:** Memoize = cache function results by argument key. Use `key in cache` (not `cache[key]`) to handle falsy cached values. Expose cache via function attribute (functions are first-class objects).

**DSA — Stacks/Queues (Session 16, Slot 2):**
- [x] Monotonic Stack Pattern (algo fundamental) | Stacks | Taught | PASSED | Recognition triggers: "next greater/smaller element", "previous greater/smaller", "how many days until X". Stack = elements waiting for their answer. Pop when current element resolves them. Each element pushed/popped at most once → O(n). Python stack: list with append/pop/[-1], all O(1). | **Def:** Monotonic stack maintains elements in sorted order. When new element comes, pop everything it "beats". Popped elements get their answer (the current element). O(n) total — each element enters and exits stack exactly once.
- [x] Daily Temperatures (LC #739) | Monotonic Stack | Medium | **8/10** | 10/10. 2 attempts. Monotonic stack parent problem. Stack stores indices (not values) — when popping, answer = current_index - popped_index. Initial bugs: duplicate push of index 0, complex if/else structure with break. Simplified to clean 3-line inner structure. Also discussed reverse-skip alternative (no stack, uses answer array as skip list). | **Def:** Stack stores indices of days waiting for warmer temperature. When current temp > stack top's temp, pop and compute days = i - popped_index. Push current index. O(n) time, O(n) space.

**Graph Micro-concept #11 (Session 16, Slot 3 — STARTED, NOT COMPLETED):**
- [ ] DAG + Topological Sort | Graph Theory | STARTED | User requested visual/diagram approach — text-only explanations not memorable enough. Course prerequisites example introduced but not completed. To be finished next session with diagrams.

### Session 17 — Apr 9 + Apr 11-12, 2026 (split across 3 days due to meetings)

**DSA — Stacks/Queues (Session 17, Track B):**
- [x] MyDeque from Scratch | DLL | Advanced | **7/10** | 10/10. 4 attempts. Dummy head/tail doubly linked list pattern. Key learnings: standard insert-between-A-and-B beats shift-dummy trick; dummies never hold values; __iter__ off-by-one trap; __bool__ inversion. | **Def:** Doubly linked list with dummy head + tail sentinels. append/pop/peek both ends O(1) via direct pointers. Used as foundation for Sliding Window Max optimal.
- [x] Sliding Window Maximum OPTIMAL REVISION (LC #239) | Monotonic Deque | Hard | **7/10** | ✅ CLEARED. 12/12 tests using own MyDeque. 4-step loop: evict dominated (back) → append → evict window (front) → record. Multiple approach bugs caught pre-coding. | **Def:** Monotonic deque holds candidate indices. Back = dominance eviction (nums[peek_right()] ≤ nums[i]). Front = window eviction (peek_left() ≤ i-k) + answer (nums[peek_left()] when i≥k-1). O(n) amortized.
- [x] Next Greater Element I (LC #496) | Monotonic Stack | Easy | **7/10** | 10/10 tests. Mono stack on nums2 + value→next_greater dict + O(1) lookup for nums1. Hints needed for bridge concept. | **Def:** Decreasing mono stack: pop when nums2[i] > stack top, record nums2[i] as answer. Build value→answer dict. Query nums1 via dict lookup. O(n+m).
- [x] Next Greater Element II (LC #503) | Monotonic Stack + Circular | Medium | **9/10** | 10/10 1st run. Best score this session. Circular twist: 2n loop, real=i%n, push only during first pass (i<n). Free hint on circular indexing (brand-new concept). | **Def:** Extend mono stack to circular array by iterating 2*n times. Real index = i%n. Push only during first pass; pop during both. O(n) time/space.

**DSA — Binary Search (Session 17, Track A):**
- [x] Search in Rotated Sorted Array REVISION (LC #33) | Binary Search | Medium | **8/10** (was 4/10) | ✅ CLEARED. 12/12 first run, ~7 min (under 8-min budget). Fresh file approach — no peeking at original. Latent bug: strict `<` in right-branch boundary check (should be `<=`). | **Def:** Rotated array has exactly 1 pivot; one half is always sorted. Left-sorted check: nums[left]<=nums[mid]. If target in sorted range, binary search there; else search other half. O(log n).

**Graph Micro-concept #12:**
- [x] Weighted Graphs | Graph Theory | PASSED | Weighted edge = edge carrying a number (cost/distance/time/price). Stored as adjacency list of (neighbor, weight) tuples. BFS insufficient for shortest path (fewer-hops ≠ shorter); needs Dijkstra (positive weights) or Bellman-Ford (with negatives). Own example: Music — nodes=notes, edges=transitions, weight=frequency change in Hz (G=196Hz, D=293Hz → edge weight 97). Valid unit + meaning. | **Def:** Weighted graph = edges carry numeric weight with unit/meaning. Adjacency list of (neighbor, weight) tuples. Dijkstra for positive weights, Bellman-Ford for negatives.
