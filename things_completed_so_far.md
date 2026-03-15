# Interview Prep: Master Progress Tracker

> Updated after every question/topic completed. This is your single source of truth.

---

## Overall Progress

| Topic | Total Qs | Done | Remaining | Status |
|-------|----------|------|-----------|--------|
| OOP | 25 | 20 | 5 | In progress |
| SOLID Principles | 26 | 1 | 25 | In progress |
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
| **TOTAL** | **326** | **21** | **305** | |

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

