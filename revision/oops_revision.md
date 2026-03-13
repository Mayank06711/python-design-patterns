# OOP Revision — Day 1

> Session Date: Feb 26, 2026
> Topics: All 4 pillars, inheritance types, diamond problem, polymorphism types

---

## The 4 Pillars — How They Connect

```
ENCAPSULATION  →  protect internals (data AND methods)
      ↓
ABSTRACTION    →  expose simple interface, hide complexity
      ↓
INHERITANCE    →  child reuses parent's protected + abstracted code
      ↓
POLYMORPHISM   →  same call, different behavior based on actual object
```

Each pillar NEEDS the one above it. They're layers, not separate topics.

---

## Encapsulation vs Abstraction (Your Biggest Takeaway)

> "Encapsulation is the MECHANISM. Abstraction is the GOAL."

| | Encapsulation | Abstraction |
|---|---|---|
| **What** | Protection | Simplification |
| **Problem it solves** | "Someone messed with my data" | "This is too complex" |
| **How** | Private fields + private methods | Simple public interface hiding internal steps |
| **Phone analogy** | Battery, motherboard sealed inside case | Tap call button → 15 steps happen invisibly |
| **Without it** | Data corruption, invalid states | Overwhelming complexity |

**Key insight:** Encapsulation protects BOTH data AND methods (not just fields).
```python
class Restaurant:
    self._inventory = {}          # private DATA — encapsulated
    self._kitchen_status = "open" # private DATA — encapsulated

    def _check_availability(self): ...  # private METHOD — also encapsulated!
    def _assign_chef(self): ...         # private METHOD — also encapsulated!

    def prepare_order(self, item):      # public — ABSTRACTION (simple interface)
        self._check_availability(item)  # hides all the complexity
        self._assign_chef(item)
        self._cook(item)
```

**Abstraction is ENABLED by encapsulation.** If internals aren't protected, someone bypasses your clean interface and the abstraction breaks.

---

## Inheritance

### is-a vs has-a (Say it out loud!)

- **is-a → Inheritance:** "VegRestaurant **is a** Restaurant" → sounds natural → inherit ✓
- **has-a → Composition:** "Car **has a** Engine" → car contains an engine → compose ✓
- **Your mistake:** `class Car(Engine)` — Car is NOT an engine. Should be composition.

```python
# WRONG
class Car(Engine): pass

# RIGHT
class Car:
    def __init__(self):
        self._engine = Engine()  # has-a
```

### 5 Types (They describe SHAPE, not a choice you make)

| Type | Shape | When it happens |
|------|-------|-----------------|
| Single | A → B | One parent, one child |
| Multilevel | A → B → C | Chain of generations |
| Hierarchical | A → B, A → C, A → D | One parent, many children |
| Multiple | A + B → C | One child, two parents |
| Hybrid | Mix of above | Usually creates the diamond |

**Interview insight:** You don't "choose" a type. You design classes based on relationships. The shape that forms gets a name. The names exist to talk about PROBLEMS (especially the diamond problem).

---

## Diamond Problem

### The Problem
Two paths to the same ancestor → which method gets called?

```
      Restaurant
       /      \
VegRestaurant  NonVegRestaurant
       \      /
    FusionRestaurant    ← calls accept_order()... which path?
```

### Python's Solution: MRO (C3 Linearization)
Flatten the diamond into a single list. Left-to-right in class definition.

```python
class FusionRestaurant(VegRestaurant, NonVegRestaurant):
#                      ↑ FIRST         ↑ SECOND

# MRO: Fusion → Veg → NonVeg → Restaurant → object
# First match wins. Restaurant appears ONCE at the end.
```

### C++ Solution: Virtual Inheritance
Without `virtual`: two COPIES of grandparent in memory → ambiguity.
With `virtual`: both parents share ONE copy via vptr (virtual pointer).

```cpp
class VegRestaurant : virtual public Restaurant {};     // virtual!
class NonVegRestaurant : virtual public Restaurant {};  // virtual!
// Now FusionRestaurant has ONE Restaurant copy, not two.
```

---

## Polymorphism

### Two Types

| | Compile-time (Overloading) | Runtime (Overriding) |
|---|---|---|
| **When decided** | Before program runs | While program runs |
| **How** | Same method name, different parameters | Child replaces parent's method |
| **Python support** | NO (dynamically typed) | YES |
| **C++/Java** | YES | YES |

### Why Python has no true overloading
Python is dynamically typed — doesn't know types at compile time. Two methods with same name → second replaces first (variable reassignment).

```python
class Calc:
    def add(self, a, b): return a + b
    def add(self, a, b, c): return a + b + c  # replaces the one above!
```

### Why constructors can't do runtime polymorphism
Constructor CREATES the object. Object doesn't exist yet → no vptr → no vtable lookup. The constructor is what BUILDS the vptr. Chicken-and-egg.

### Why static methods can't be overridden
Static methods belong to the CLASS, not an object. No object → no vptr → no vtable → no runtime dispatch.

### Parent-Child direction matters

```python
def checkout(payment: Payment):    # expects parent
    payment.process()

checkout(UPI())       # ✓ child into parent slot (UPI is-a Payment)
checkout(Payment())   # ✓ exact match

def upi_only(payment: UPI):       # expects child
    payment.check_vpa()

upi_only(Payment())  # ✗ BREAKS — parent into child slot (Payment lacks check_vpa)
```

> Child → parent slot: ALWAYS safe (upcasting)
> Parent → child slot: BREAKS (downcasting, missing abilities)

---

## How `self` Actually Works

### ONE object, not many
When you create `FusionRestaurant("Test")`, Python creates **ONE object**. Not four objects (one per class). The `__init__` chain adds fields to that same single object layer by layer.

```
┌─────────────────────────────────────┐
│         ONE OBJECT (fusion)          │
│                                      │
│  _name = "Fusion Bites"  ← Restaurant.__init__ set this │
│  _specialty = "Paneer"   ← VegRestaurant.__init__ set this │
│                                      │
└─────────────────────────────────────┘
```

### Method lookup = MRO search
When you call `fusion.accept_order()`, Python searches UP the MRO automatically:
```
FusionRestaurant → has accept_order()? NO
VegRestaurant    → has accept_order()? NO
NonVegRestaurant → has accept_order()? NO
Restaurant       → has accept_order()? YES → call it, STOP
```

### `object.method()` is sugar for `Class.method(object)`
```python
veg.prepare("Biryani")                   # Python auto-passes veg as self
VegRestaurant.prepare(veg, "Biryani")    # You manually pass veg as self
# Both are IDENTICAL
```

This is why `VegRestaurant.prepare(self, item)` works inside FusionRestaurant — you're manually choosing WHICH class's method to run, while passing the fusion object as self.

### Calling both parents in multiple inheritance
`super()` only follows ONE path (next in MRO). To call BOTH parents:
```python
class FusionRestaurant(VegRestaurant, NonVegRestaurant):
    def prepare(self, item):
        veg_res = VegRestaurant.prepare(self, item)        # explicit
        non_veg_res = NonVegRestaurant.prepare(self, item)  # explicit
        return veg_res + " & " + non_veg_res
```
But if you need this, consider **composition** instead — it's usually a cleaner design.

### Parent accessing child properties
- **Can it?** Technically yes, because `self` is the actual object.
- **Should it?** NO. Parent should never depend on child-specific fields — breaks when used with a different child.

| Direction | Can? | Should? |
|-----------|------|---------|
| Child → parent's stuff | Yes | Yes (that's inheritance) |
| Parent → its own stuff | Yes | Yes (normal) |
| Parent → child's stuff | Yes (via self) | NO (breaks with other children) |

---

## Composition (has-a)
Composition = storing another object as a field. **NOT a new concept — just has-a in code.**

```python
# Inheritance (is-a):
class VegRestaurant(Restaurant): pass    # VegRestaurant IS-A Restaurant

# Composition (has-a):
class Car:
    def __init__(self):
        self._engine = Engine()           # Car HAS-A Engine
```

When to use: say it out loud. "Car is-a Engine?" No → composition. "Car has-a Engine?" Yes → composition.

---

## Mistakes I Made & Lessons

1. **Initially mixed up encapsulation and abstraction** — used the word "abstracting" to explain encapsulation. Fix: Encapsulation = protection, Abstraction = simplification.

2. **Car(Engine) confusion** — Said "Engine should inherit from Car" instead of recognizing it's a composition (has-a) problem. Neither direction of inheritance works. Fix: Say the "is-a" sentence out loud.

3. **Diamond problem — "we don't know which one"** — Actually Python DOES know. MRO is deterministic (left-to-right). Not random.

4. **super() calls both parents** — No it doesn't. `super()` only goes to NEXT in MRO. To call both parents explicitly use `ParentClass.method(self, args)`.

5. **Confused about how self has everything** — There's only ONE object. `__init__` chain adds fields to the same object. Methods are found by searching UP the MRO.

---

## One-Liners for Interview

- "Encapsulation is the mechanism, abstraction is the goal"
- "If is-a doesn't sound natural in English, use composition"
- "Python resolves the diamond with MRO using C3 linearization — left to right, shared ancestor last"
- "Constructors can't be runtime-polymorphic because the object doesn't exist yet to do vtable lookup"
- "Python has no true overloading because types aren't known at compile time"
- "object.method() is just syntactic sugar for Class.method(object)"
- "Inheritance creates ONE object — __init__ chain just keeps adding fields to it"
- "super() follows MRO, not 'all parents' — to call both parents, use ClassName.method(self) explicitly"
- "When needing both parents' behavior, prefer composition over multiple inheritance"
- "An interface is a pure contract. An abstract class is a partial blueprint — shares code AND forces contracts"
- "`type(self).__name__` gives the actual class name of the current object as a string"
- "@property = encapsulation + abstraction: validates like a method, accessed like a field"
- "@staticmethod needs nothing, @classmethod needs the class (cls), regular method needs the object (self)"
- "Always implement __repr__ first — __str__ falls back to it, not the other way around"

---

## Interface vs Abstract Class vs Class vs Object

| | Interface | Abstract Class | Class | Object |
|---|---|---|---|---|
| **What** | Pure contract | Partial blueprint | Full blueprint | Actual instance |
| **Code inside?** | NO methods have bodies | SOME do, some don't | ALL do | N/A — it's data |
| **Create objects?** | NO | NO | YES | IS the object |
| **Why exists** | Force rules | Share code + force rules | Define everything | Do actual work |
| **Python** | ABC, all `@abstractmethod` | ABC, mix of abstract + concrete | Normal `class` | `obj = Class()` |

**Key:** Python has no separate `interface` keyword — an ABC with ALL methods abstract acts as an interface.

```python
# Abstract class (partial blueprint):
class Payment(ABC):
    @abstractmethod
    def process(self, amount): pass     # child MUST implement
    def receipt(self, amount):          # child gets for FREE
        return f"Receipt: ₹{amount} via {type(self).__name__}"

# Interface (pure contract — ALL abstract):
class Printable(ABC):
    @abstractmethod
    def to_pdf(self): pass
    @abstractmethod
    def to_html(self): pass
    # zero implementation — just rules
```
