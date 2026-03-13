"""
Practice 5: All 4 Pillars Combined — Food Delivery System

Build a mini food delivery system that uses ALL 4 OOP pillars:

1. Restaurant (abstract base class):
   - __init__(self, name, rating): store name (public), _rating (private), _menu (private dict)
   - add_item(name, price): adds to _menu
   - get_menu(): returns a COPY of _menu (defensive copy — encapsulation!)
   - prepare(item) — abstract, children must implement
   - __str__(): return "{name} ({rating}★)"

2. VegRestaurant(Restaurant):
   - prepare(item): return "🥗 Preparing veg {item} at {name}"

3. NonVegRestaurant(Restaurant):
   - prepare(item): return "🍗 Preparing non-veg {item} at {name}"

4. Order class:
   - __init__(self, restaurant: Restaurant, item: str, quantity: int)
   - total(): looks up item price from restaurant's menu, returns price * quantity
   - summary(): return "{quantity}x {item} from {restaurant} = ₹{total}"

Pillars used:
- ENCAPSULATION: _rating, _menu are private, get_menu() returns defensive copy
- ABSTRACTION: prepare() hides cooking complexity, Order.summary() hides calculation
- INHERITANCE: VegRestaurant and NonVegRestaurant extend Restaurant
- POLYMORPHISM: prepare() behaves differently per restaurant type
"""

from abc import ABC, abstractmethod
import copy

class Restaurant(ABC):
    def __init__(self, name:str, rating:float):
        self.name = name
        self._rating = rating
        self._menu = {}
    
    def add_item(self, name:str, price:int):
        if price < 0 or len(name)==0:
            raise ValueError
        self._menu[name] = price
    
    def get_menu(self):
        return copy.copy(self._menu)
    
    def __str__(self):
        return f"{self.name} ({self._rating}★)"

    @abstractmethod
    def prepare(self, item):
        pass

class VegRestaurant(Restaurant):
    def __init__(self, name:str, rating:float):
        super().__init__(name, rating)
    
    def prepare(self, item):
        return f"🥗 Preparing veg {item} at {self.name}"

class NonVegRestaurant(Restaurant):
    def __init__(self, name:str, rating: float):
        super().__init__(name, rating)
    
    def prepare(self, item):
        return f"🍗 Preparing non-veg {item} at {self.name}"


class Order:
    def __init__(self, restaurant: Restaurant, item: str, quantity:int):
        self.res = restaurant
        self._item = item
        self._quantity = quantity
    
    def total(self):
        item_price = self.res.get_menu()[self._item]
        return item_price*self._quantity
    
    def summary(self):
        total = self.total()
        name = self.res.name
        return f"{self._quantity}x {self._item} from {name} = ₹{total}"




# ============ TEST CASES (DO NOT MODIFY) ============

if __name__ == "__main__":
    # Setup
    veg = VegRestaurant("Green Kitchen", 4.5)
    veg.add_item("Paneer Tikka", 250)
    veg.add_item("Dal Makhani", 200)

    nonveg = NonVegRestaurant("Tandoori Hub", 4.2)
    nonveg.add_item("Chicken Biryani", 300)
    nonveg.add_item("Butter Chicken", 350)

    # Test 1: Encapsulation — get_menu returns copy
    menu = veg.get_menu()
    menu["HACKED"] = 9999
    assert "HACKED" not in veg.get_menu(), "Encapsulation broken!"
    print("Test 1 PASS: get_menu() returns defensive copy")

    # Test 2: Inheritance — both have add_item from parent
    assert "Paneer Tikka" in veg.get_menu()
    assert "Chicken Biryani" in nonveg.get_menu()
    print("Test 2 PASS: add_item() inherited by both")

    # Test 3: Polymorphism — same method, different behavior
    veg_result = veg.prepare("Paneer Tikka")
    nonveg_result = nonveg.prepare("Chicken Biryani")
    assert "veg" in veg_result.lower()
    assert "non-veg" in nonveg_result.lower()
    print(f"Test 3 PASS: Polymorphism — veg: '{veg_result}', nonveg: '{nonveg_result}'")

    # Test 4: Abstraction — Order.summary() hides calculation
    order1 = Order(veg, "Paneer Tikka", 2)
    assert order1.total() == 500, f"Expected 500, got {order1.total()}"
    print(f"Test 4 PASS: order.total() = {order1.total()}")

    # Test 5: Order summary
    summary = order1.summary()
    assert "2x" in summary and "Paneer Tikka" in summary and "500" in summary
    print(f"Test 5 PASS: {summary}")

    # Test 6: Polymorphic order processing
    orders = [
        Order(veg, "Dal Makhani", 1),
        Order(nonveg, "Butter Chicken", 3),
    ]
    for o in orders:
        print(f"  → {o.summary()}")
    print("Test 6 PASS: orders work with both restaurant types")

    # Test 7: __str__
    assert str(veg) == "Green Kitchen (4.5★)"
    print(f"Test 7 PASS: str(veg) = {veg}")

    # Test 8: Cannot instantiate abstract Restaurant
    try:
        r = Restaurant("Test", 5.0)
        print("Test 8 FAIL: should not instantiate abstract class")
    except TypeError:
        print("Test 8 PASS: Restaurant is abstract")

    print(f"\nAll tests passed!")
