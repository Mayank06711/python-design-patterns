"""
================================================================================
EXERCISE 08 — Factory Pattern
================================================================================
Build a Shape factory that creates shapes by name.

YOUR TASK:
1. Create Shape ABC with abstract method `area()` and abstract method `describe()`
2. Create Circle(Shape) — takes radius. area = 3.14159 * r^2. describe = "Circle with radius {r}"
3. Create Rectangle(Shape) — takes width, height. area = w*h. describe = "Rectangle {w}x{h}"
4. Create Triangle(Shape) — takes base, height. area = 0.5*b*h. describe = "Triangle base={b} height={h}"
5. Create ShapeFactory class with:
   - A dict mapping string names to classes
   - A `create(shape_type: str, **kwargs)` method that:
     - Looks up the class in the dict
     - Creates and returns the object using **kwargs
     - Raises ValueError if shape_type is unknown
   - A `register(name: str, cls)` method to add new shapes WITHOUT modifying existing code

Run this file to test:  python 08_factory_pattern.py
================================================================================
"""
from abc import ABC, abstractmethod

# ── YOUR CODE BELOW ──────────────────────────────────────────────────────────
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def describe(self):
        pass 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def describe(self):
        return f"Circle with radius {self.radius}"

    def area(self):
        return 3.14159*self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height 

    def describe(self):
        return f"Rectangle {self.width}x{self.height}"
    
    def area(self):
        return self.width*self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base, self.height = base, height   
    
    def describe(self):
        return f"Triangle base={self.base} height={self.height}"
    
    def area(self):
        return 0.5*self.base*self.height

class ShapeFactory:
    _dict = {'circle': Circle, 'rectangle': Rectangle, 'triangle': Triangle}
    def create(self, shape: str, **kwargs):
        shape_cls = ShapeFactory._dict.get(shape, None)
        if shape_cls is None:
            raise ValueError
        obj = shape_cls(**kwargs)
        return obj
    
    def register(self, name: str, cls):
        ShapeFactory._dict[name] = cls 




# ── YOUR CODE ABOVE ──────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    factory = ShapeFactory()

    # Test 1: Create circle
    try:
        c = factory.create("circle", radius=5)
        assert abs(c.area() - 78.53975) < 0.01, f"Expected ~78.54 but got {c.area()}"
        print("  [PASS] Test 1: Circle area correct")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1: Circle — {e}")
        failed += 1

    # Test 2: Create rectangle
    try:
        r = factory.create("rectangle", width=4, height=6)
        assert r.area() == 24, f"Expected 24 but got {r.area()}"
        print("  [PASS] Test 2: Rectangle area correct")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2: Rectangle — {e}")
        failed += 1

    # Test 3: Create triangle
    try:
        t = factory.create("triangle", base=10, height=5)
        assert t.area() == 25.0, f"Expected 25.0 but got {t.area()}"
        print("  [PASS] Test 3: Triangle area correct")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3: Triangle — {e}")
        failed += 1

    # Test 4: Describe works
    try:
        c = factory.create("circle", radius=3)
        assert c.describe() == "Circle with radius 3"
        r = factory.create("rectangle", width=2, height=5)
        assert r.describe() == "Rectangle 2x5"
        t = factory.create("triangle", base=6, height=4)
        assert t.describe() == "Triangle base=6 height=4"
        print("  [PASS] Test 4: All describe() methods correct")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4: describe — {e}")
        failed += 1

    # Test 5: Unknown shape raises ValueError
    try:
        factory.create("hexagon", sides=6)
        print("  [FAIL] Test 5: Should have raised ValueError")
        failed += 1
    except ValueError:
        print("  [PASS] Test 5: ValueError for unknown shape")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5: Wrong exception — {e}")
        failed += 1

    # Test 6: Register new shape dynamically
    try:
        class Pentagon(Shape):
            def __init__(self, side):
                self._side = side
            def area(self):
                return 1.72 * self._side ** 2
            def describe(self):
                return f"Pentagon with side {self._side}"

        factory.register("pentagon", Pentagon)
        p = factory.create("pentagon", side=4)
        assert abs(p.area() - 27.52) < 0.01
        assert p.describe() == "Pentagon with side 4"
        print("  [PASS] Test 6: Dynamically registered Pentagon works")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 6: Dynamic registration — {e}")
        failed += 1

    # Test 7: All created objects are Shape instances
    try:
        c = factory.create("circle", radius=1)
        r = factory.create("rectangle", width=1, height=1)
        t = factory.create("triangle", base=1, height=1)
        assert isinstance(c, Shape), "Circle should be a Shape"
        assert isinstance(r, Shape), "Rectangle should be a Shape"
        assert isinstance(t, Shape), "Triangle should be a Shape"
        print("  [PASS] Test 7: All shapes are Shape instances")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 7: isinstance — {e}")
        failed += 1

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{passed+failed} tests passed")
    if failed == 0:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
