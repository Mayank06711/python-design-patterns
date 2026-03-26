# Interview Prep: Master Progress Tracker

> Updated after every question/topic completed. This is your single source of truth.

---

## Overall Progress

| Topic | Total Qs | Done | Remaining | Status |
|-------|----------|------|-----------|--------|
| OOP | 25 | 20 | 5 | In progress |
| SOLID Principles | 26 | 8 | 18 | In progress |
| Closures/HOF/Decorators | 33 | 7 | 26 | In progress |
| SQL & Indexing | 35 | 0 | 35 | Not started |
| Rate Limiting | 27 | 0 | 27 | Not started |
| System Design | 27 | 0 | 27 | Not started |
| DSA — Arrays/Two Pointers | 15 | 10 | 5 | In progress |
| DSA — Binary Search | 10 | 0 | 10 | Not started |
| DSA — Linked List | 12 | 0 | 12 | Not started |
| DSA — Stacks/Queues | 10 | 0 | 10 | Not started |
| DSA — Sorting | 8 | 0 | 8 | Not started |
| DSA — Trees & BST | 15 | 0 | 15 | Not started |
| DSA — Heaps | 8 | 0 | 8 | Not started |
| DSA — Recursion/Backtracking | 12 | 0 | 12 | Not started |
| DSA — Greedy | 8 | 0 | 8 | Not started |
| DSA — Dynamic Programming | 30 | 0 | 30 | Not started |
| DSA — Graphs | 20 | 0 | 20 | Not started |
| DSA — Bits/Tries | 5 | 0 | 5 | Not started |
| **TOTAL** | **326** | **43** | **283** | |

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
