# OOP Interview Questions (25 Questions - Mid to Advanced)

> Curated from Google, Amazon, Meta, Microsoft interviews
> Languages: Python + Java/JS where relevant

---

## Section A: Core Concepts (Q1-Q10)

### Q1. Four Pillars with a Unified Analogy [Mid]
**Explain all four OOP pillars using a single real-world system (e.g., Vehicle system) that ties them together.**

- Encapsulation: engine internals hidden behind an interface
- Abstraction: driver uses steering wheel, not pistons
- Inheritance: `ElectricCar` extends `Vehicle`
- Polymorphism: `start()` behaves differently for `ElectricCar` vs `GasCar`

*Interviewers want to see you CONNECT them, not define them in isolation.*

---

### Q2. Abstraction vs Encapsulation [Mid]
**Many candidates confuse these. How are they fundamentally different?**

- Abstraction = design-level concept (hides complexity via interfaces, e.g., a `Map` interface)
- Encapsulation = implementation-level mechanism (bundles data + methods, restricts access via private fields)
- Abstraction answers "WHAT does it do?", Encapsulation answers "HOW is it protected?"

---

### Q3. Compile-time vs Runtime Polymorphism [Mid]
**Explain with examples. Why can't constructors be polymorphic? Why don't static methods participate in runtime polymorphism?**

- Compile-time = method overloading (resolved by compiler based on signature)
- Runtime = method overriding (resolved via vtable/dynamic dispatch based on actual object type)
- Constructors: not polymorphic because they don't participate in dynamic dispatch
- Static methods: use method hiding, not overriding -- resolved by reference type, not object type

---

### Q4. Diamond Problem & MRO [Advanced]
**What is the Diamond Problem? How does Python solve it vs Java vs C++?**

```python
class A:
    def greet(self): print("A")
class B(A):
    def greet(self): print("B")
class C(A):
    def greet(self): print("C")
class D(B, C):
    pass

D().greet()        # What prints?
print(D.__mro__)   # What is the MRO?
```

**Answer:** Prints "B". MRO: `D -> B -> C -> A -> object` (C3 linearization).
- Python: C3 linearization (MRO)
- C++: virtual inheritance
- Java: no multiple class inheritance; interface default method conflict resolution since Java 8

---

### Q5. Method Resolution Order Deep Dive [Advanced]
**Given a complex hierarchy, predict the MRO and trace method calls:**

```python
class A:
    def process(self): return "A"

class B(A):
    def process(self): return "B" + super().process()

class C(A):
    def process(self): return "C" + super().process()

class D(B, C):
    def process(self): return "D" + super().process()

print(D().process())  # What's the output?
```

**Answer:** `"DBCA"` -- super() follows MRO: D -> B -> C -> A

---

### Q6. Abstract Class vs Interface [Mid]
**When would you choose one over the other? How have modern languages blurred the line?**

| Feature | Abstract Class | Interface |
|---------|---------------|-----------|
| State (fields) | Yes | No (traditionally) |
| Constructors | Yes | No |
| Partial implementation | Yes | Only default methods (Java 8+) |
| Multiple inheritance | No (most languages) | Yes |
| Use when | "is-a" with shared behavior | "can-do" capability contract |

---

### Q7. Composition over Inheritance [Advanced]
**Give a concrete example where inheritance is WRONG and composition is correct.**

BAD:
```python
class Stack(list):  # Stack IS-A list? No! Users can call insert(), pop(0), etc.
    pass
```

GOOD:
```python
class Stack:
    def __init__(self):
        self._items = []  # Stack HAS-A list (composition)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]
```

*Inheritance exposes the full list API. Composition restricts to only push/pop/peek.*

---

### Q8. LSP - Rectangle/Square Problem [Advanced]
**Show code that works with Rectangle but breaks with Square. Then fix it.**

```python
class Rectangle:
    def __init__(self, w, h):
        self._w, self._h = w, h

    @property
    def width(self): return self._w
    @width.setter
    def width(self, v): self._w = v

    @property
    def height(self): return self._h
    @height.setter
    def height(self, v): self._h = v

    def area(self): return self._w * self._h

class Square(Rectangle):  # VIOLATES LSP
    def __init__(self, side):
        super().__init__(side, side)
    @Rectangle.width.setter
    def width(self, v): self._w = self._h = v  # side-effect!
    @Rectangle.height.setter
    def height(self, v): self._w = self._h = v  # side-effect!

def test(rect: Rectangle):
    rect.width = 5
    rect.height = 4
    assert rect.area() == 20  # FAILS for Square (gets 16)
```

**Fix:** Don't make Square extend Rectangle. Both implement a `Shape` ABC.

---

### Q9. Encapsulation Violation - Mutable State Leak [Advanced]
**What's wrong with this code? How do you fix it?**

```python
class Team:
    def __init__(self):
        self._members = ["Alice", "Bob"]

    def get_members(self):
        return self._members  # DANGER: returns reference to internal list

team = Team()
members = team.get_members()
members.append("Hacker")  # Mutates internal state!
print(team.get_members())  # ['Alice', 'Bob', 'Hacker'] -- encapsulation broken
```

**Fix:** Return a defensive copy: `return self._members.copy()` or `return tuple(self._members)`

---

### Q10. Tricky Output - Fields vs Methods in Polymorphism [Advanced]

```python
# Java-style question (but demonstrable concept)
class Animal:
    name = "Animal"
    def speak(self): return "..."

class Dog(Animal):
    name = "Dog"
    def speak(self): return "Woof"

a = Dog()
print(a.name)     # "Dog" (Python resolves from instance -> class -> parent)
print(a.speak())  # "Woof"

# BUT in Java:
# Animal a = new Dog();
# a.name   -> "Animal" (fields NOT polymorphic, resolved by reference type)
# a.speak() -> "Woof"  (methods ARE polymorphic, resolved by object type)
```

---

## Section B: Design Patterns (Q11-Q15)

### Q11. Singleton - Thread Safe [Advanced]
**Implement Singleton. Make it thread-safe. What are its pitfalls?**

```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
        return cls._instance
```

**Pitfalls:** Global state, hard to test/mock, hidden dependencies, violates SRP.
**When to avoid:** When you need testability or the "single instance" assumption may change.

---

### Q12. Factory Pattern [Mid]
**Implement a ShapeFactory that creates different shapes based on input.**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class ShapeFactory:
    @staticmethod
    def create(shape_type: str, **kwargs) -> Shape:
        factories = {
            "circle": lambda: Circle(kwargs["radius"]),
            "rectangle": lambda: Rectangle(kwargs["w"], kwargs["h"]),
        }
        if shape_type not in factories:
            raise ValueError(f"Unknown shape: {shape_type}")
        return factories[shape_type]()
```

---

### Q13. Strategy Pattern + OCP [Advanced]
**Implement a payment system where strategy can be swapped at runtime.**

```python
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str: pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount): return f"Paid ${amount} via Credit Card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount): return f"Paid ${amount} via PayPal"

class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def checkout(self, amount: float):
        return self._strategy.pay(amount)

# Usage: cart = ShoppingCart(PayPalPayment())
# Adding Bitcoin = new class, zero changes to existing code
```

---

### Q14. Observer Pattern [Advanced]
**Implement a notification system where multiple listeners react to events.**

```python
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event: str, callback):
        self._listeners.setdefault(event, []).append(callback)

    def off(self, event: str, callback):
        self._listeners.get(event, []).remove(callback)

    def emit(self, event: str, data=None):
        for cb in self._listeners.get(event, []):
            cb(data)

# Usage:
# emitter = EventEmitter()
# emitter.on("order_placed", lambda d: print(f"Email: {d}"))
# emitter.on("order_placed", lambda d: print(f"SMS: {d}"))
# emitter.emit("order_placed", {"order_id": 123})
```

---

### Q15. Decorator Pattern (OOP, not Python @decorator) [Advanced]
**Build a coffee ordering system where toppings are decorators.**

```python
class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float: pass
    @abstractmethod
    def description(self) -> str: pass

class Coffee(Beverage):
    def cost(self): return 2.00
    def description(self): return "Coffee"

class MilkDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    def cost(self): return self._beverage.cost() + 0.50
    def description(self): return self._beverage.description() + " + Milk"

class SugarDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    def cost(self): return self._beverage.cost() + 0.25
    def description(self): return self._beverage.description() + " + Sugar"

# order = SugarDecorator(MilkDecorator(Coffee()))
# order.description() -> "Coffee + Milk + Sugar"
# order.cost() -> 2.75
```

---

## Section C: OOP Design Problems (Q16-Q21)

### Q16. Design a Parking Lot [Advanced - Classic LLD]
**Define class hierarchy, relationships, and key methods.**

Key classes:
- `ParkingLot` (has many `ParkingFloor`)
- `ParkingFloor` (has many `ParkingSpot`)
- `ParkingSpot` (subtypes: `CompactSpot`, `LargeSpot`, `HandicappedSpot`)
- `Vehicle` (subtypes: `Car`, `Truck`, `Motorcycle`)
- `Ticket` (vehicle, spot, entry_time)
- `Payment` (ticket, amount, exit_time)

Key methods: `parkVehicle()`, `unparkVehicle()`, `calculateFee()`, `findAvailableSpot(vehicleType)`

---

### Q17. Design a Library Management System [Mid]
**Model books, users, borrowing, and returns with proper OOP.**

Key classes:
- `Book` (title, author, ISBN, copies_available)
- `Member` (name, member_id, borrowed_books[])
- `Library` (catalog: dict[ISBN, Book], members: dict[id, Member])
- `BorrowRecord` (book, member, borrow_date, due_date, return_date)

Key methods: `search_by_title()`, `borrow_book()`, `return_book()`, `check_overdue()`

---

### Q18. Design a Deck of Cards for Multiple Games [Advanced]
**How do you make it extensible for Poker, Blackjack, etc.?**

```python
from enum import Enum
import random

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Card:
    def __init__(self, suit: Suit, rank: int):
        self.suit = suit
        self.rank = rank  # 1=Ace, 11=J, 12=Q, 13=K

class Deck:
    def __init__(self):
        self._cards = [Card(s, r) for s in Suit for r in range(1, 14)]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, count=1):
        return [self._cards.pop() for _ in range(count)]

class Game(ABC):
    @abstractmethod
    def evaluate_hand(self, cards: list[Card]) -> int: pass

    @abstractmethod
    def play_round(self): pass

class BlackjackGame(Game):
    def evaluate_hand(self, cards):
        return sum(min(c.rank, 10) for c in cards)

    def play_round(self): pass  # implement game logic
```

---

### Q19. Design a File System (Composite Pattern) [Advanced]
**Files, directories, and recursive size calculation.**

```python
class FileSystemEntity(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_size(self) -> int: pass

class File(FileSystemEntity):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    def get_size(self) -> int:
        return self._size

class Directory(FileSystemEntity):
    def __init__(self, name: str):
        super().__init__(name)
        self._children: list[FileSystemEntity] = []

    def add(self, entity: FileSystemEntity):
        self._children.append(entity)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)
```

*Tests: Composite pattern + recursion + polymorphism*

---

### Q20. Design an Elevator System [Advanced]
**Model request dispatching, movement, and state management.**

Key classes:
- `Elevator` (current_floor, direction, state, request_queue)
- `ElevatorController` (dispatches requests to optimal elevator)
- `Request` (floor, direction: UP/DOWN)
- `Building` (floors, list of elevators)

Patterns used:
- **State Pattern** for elevator states: IDLE, MOVING_UP, MOVING_DOWN, MAINTENANCE
- **Strategy Pattern** for dispatch algorithm: nearest elevator, zone-based
- **Observer Pattern** for notifying controller of state changes

---

### Q21. Design a Notification System (OCP-compliant) [Advanced]
**Email, SMS, Push -- new types addable without modifying existing code.**

```python
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool: pass

class EmailNotification(NotificationChannel):
    def send(self, recipient, message):
        print(f"Email -> {recipient}: {message}")
        return True

class SMSNotification(NotificationChannel):
    def send(self, recipient, message):
        print(f"SMS -> {recipient}: {message}")
        return True

class NotificationService:
    def __init__(self, channels: list[NotificationChannel]):
        self._channels = channels

    def notify(self, recipient: str, message: str):
        for channel in self._channels:
            channel.send(recipient, message)
```

---

## Section D: Advanced / Tricky (Q22-Q25)

### Q22. Dependency Injection without a Framework [Advanced]
**Implement DI manually. Why does it matter for testing?**

```python
class Database(ABC):
    @abstractmethod
    def query(self, sql: str) -> list: pass

class MySQL(Database):
    def query(self, sql): return ["real data"]

class MockDB(Database):
    def query(self, sql): return ["mock data"]

class UserService:
    def __init__(self, db: Database):  # Injected, not created
        self._db = db

    def get_users(self):
        return self._db.query("SELECT * FROM users")

# Production: UserService(MySQL())
# Testing:    UserService(MockDB())  -- no real DB needed!
```

---

### Q23. Multiple Inheritance Pitfalls [Advanced]
**What's the output? Explain the `super()` chain.**

```python
class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()

D()
```

**Output:**
```
D init
B init
C init
A init
```
MRO: D -> B -> C -> A -> object. `super()` follows the MRO, NOT the direct parent.

---

### Q24. `__slots__` and Memory Optimization [Advanced]
**What are `__slots__`? When would you use them?**

```python
class PointRegular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointOptimized:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

# PointOptimized uses ~40% less memory
# Cannot add dynamic attributes: PointOptimized().z = 3  -> AttributeError
# Use when: millions of instances, fixed attributes, performance-critical
```

---

### Q25. Metaclasses - How Classes Are Created [Advanced]
**What is a metaclass? When would you use one?**

```python
class ValidatedMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Enforce that all subclasses must implement 'validate' method
        if bases:  # skip for the base class itself
            if 'validate' not in namespace:
                raise TypeError(f"{name} must implement validate()")
        return super().__new__(mcs, name, bases, namespace)

class BaseModel(metaclass=ValidatedMeta):
    def validate(self): pass

class UserModel(BaseModel):
    def validate(self):
        print("Validating user...")

# class BadModel(BaseModel):  # TypeError: BadModel must implement validate()
#     pass
```

*Use when: framework code, ORM field registration, enforcing contracts at class creation time.*
*In practice, 99% of the time you don't need metaclasses -- use ABCs or decorators instead.*

---

## Quick Reference: What Interviewers Really Test

| Concept | What They Want to See |
|---------|----------------------|
| 4 Pillars | Connected explanation, not textbook definitions |
| Inheritance | When NOT to use it (composition over inheritance) |
| Polymorphism | Runtime dispatch understanding, tricky output Qs |
| Design Patterns | Apply to real problems, not just recite names |
| LLD Problems | Clean class hierarchies, proper relationships |
| SOLID connection | How OOP principles connect to SOLID |
