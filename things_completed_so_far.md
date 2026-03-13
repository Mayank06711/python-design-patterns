# Interview Prep: Master Progress Tracker

> Updated after every question/topic completed. This is your single source of truth.

---

## Overall Progress

| Topic | Total Qs | Done | Remaining | Status |
|-------|----------|------|-----------|--------|
| OOP | 25 | 20 | 5 | In progress |
| SOLID Principles | 26 | 0 | 26 | Not started |
| Closures/HOF/Decorators | 33 | 0 | 33 | Not started |
| SQL & Indexing | 35 | 0 | 35 | Not started |
| Rate Limiting | 27 | 0 | 27 | Not started |
| System Design | 27 | 0 | 27 | Not started |
| DSA — Arrays/Two Pointers | 15 | 0 | 15 | Not started |
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
| **TOTAL** | **326** | **20** | **306** | |

---

## Day-wise Log

### Day 1 — Feb 26, 2026

**OOP Foundations Blitz:**
- [x] Q1: Four Pillars (unified analogy) | OOP | Mid | Solved | Used banking + food delivery examples
- [x] Q2: Abstraction vs Encapsulation | OOP | Mid | Solved | "Encapsulation = mechanism, Abstraction = goal"
- [x] Q3: Compile-time vs Runtime Polymorphism | OOP | Mid | Solved | Overloading vs overriding, Python has no true overloading (dynamic typing)
- [x] Q4: Diamond Problem & MRO | OOP | Advanced | Solved | Python C3 linearization, C++ vtable + virtual inheritance
- [x] Q5: Inheritance types + is-a vs has-a | OOP | Mid | Solved | 5 types, is-a = inherit, has-a = composition. Minor slip on Q10 (Car/Engine)
- **Notes:** Strong on encapsulation vs abstraction distinction. Understands vtable internals. Needs to watch out for "when to use composition" — got tripped on Car(Engine).

**OOP Coding Practice:**
- [x] 01_encapsulation_practice.py | OOP | Mid | Solved | Minor bugs: f-string typo, deepcopy vs copy. Defensive copy understood.
- [x] 02_inheritance_diamond.py | OOP | Advanced | Solved | Learned super() only follows MRO, need explicit Class.method(self) for both parents. Good comments in code.
- [x] 03_polymorphism_practice.py | OOP | Mid | Solved | Bugs: used bare `type` instead of `type(self).__name__`, forgot @abstractmethod decorator. Learned interface vs abstract class vs class distinction.
- [x] 04_composition_vs_inheritance.py | OOP | Mid | Solved | Minor bug: called `eng()` on already-instantiated object. Self-fixed. Clean delegation pattern.
- [x] 05_all_pillars_combined.py | OOP | Advanced | Solved | Bugs: `*` instead of `★`, `valueError` (lowercase v). Used dict loop instead of direct lookup — fixed to O(1). All 4 pillars demonstrated in one system.

**OOP Quick-fire (Python-specific):**
- [x] Q6: @property | OOP | Mid | Taught | Pythonic getter/setter, read-only via skipping setter, use when need validation/computation
- [x] Q7: @staticmethod vs @classmethod | OOP | Mid | Taught | static=no args (utility), classmethod=cls (alternative constructors), regular=self (object data)
- [x] Q8: __str__ vs __repr__ | OOP | Mid | Taught | str=users (pretty), repr=devs (unambiguous). Always implement __repr__ first — __str__ falls back to it.

**OOP Advanced Theory:**
- [x] Q9: MRO Deep Dive (super chain) | OOP | Advanced | Solved | Traced DBCA, handled missing methods (skip in MRO), 6-class diamond (FDBECA). Key: super() = next in MRO of actual object, not parent class.
- [x] Q10: Fields vs Methods in Polymorphism | OOP | Advanced | Solved | Python: both from actual object. Java: fields=reference type (compile), methods=actual object (runtime). Fields don't go through vtable.
- [x] Q11: LSP Rectangle-Square (exercise 06) | OOP | Advanced | Solved | **8/10** — Shape ABC as common contract, siblings not parent-child. Dead __init__ in Shape (no need for constructor in pure interface). 1 hint (print_area standalone vs method).
- [x] Q12: Singleton Pattern (exercise 07) | OOP | Advanced | Solved | **8/10** — __new__ vs __init__, threading.Lock for thread safety, hasattr guard for re-init. Learned: threads, GIL, race conditions, why frameworks create threads. Dead code after return.
- [x] Q13: Factory Pattern (exercise 08) | OOP | Mid | Solved | **9/10** — Dict-based registry, **kwargs forwarding, register() for extensibility. Bugs: pi typo, param name mismatch, bare vars. No hints needed.
- [x] Q14: Strategy Pattern (exercise 09) | OOP | Advanced | Solved | **7/10** — Swappable discount strategies, runtime swap via setter. Bugs: checkout() missing arg, total()-apply() double subtraction, dict overwriting duplicate keys→two lists. No hints needed but 3 bugs.
- [x] Q15: Dependency Injection (exercise 10) | OOP | Mid | Solved | **8/10** — Notification system with injected channels. Bugs: enumerate missing, filter logic (append outside if), isinstance vs __name__, syntax error. 1 hint. Missing @abstractmethod on ABC.

