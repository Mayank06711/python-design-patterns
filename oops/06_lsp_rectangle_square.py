"""
================================================================================
EXERCISE 06 — LSP: Rectangle-Square Problem
================================================================================
The classic interview question. Fix the broken inheritance.

YOUR TASK:
1. Create an ABC called `Shape` with an abstract method `area()`
2. Create `Rectangle(Shape)` with width, height, and setters for both
3. Create `Square(Shape)` with side and a setter for side
4. Rectangle and Square are SIBLINGS — no inheritance between them
5. Create a function `print_area(shape: Shape)` that calls shape.area()

RULES:
- Square must NOT inherit from Rectangle
- Both must inherit from Shape
- Rectangle: setting width should NOT affect height (and vice versa)
- Square: setting side changes the one dimension

Run this file to test:  python 06_lsp_rectangle_square.py
================================================================================
"""
from abc import ABC, abstractmethod
# ── YOUR CODE BELOW ──────────────────────────────────────────────────────────
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height
    def area(self):
        return self.width*self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side*self.side

def print_area(shape: Shape):
    return shape.area()



# ── YOUR CODE ABOVE ──────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    # Test 1: Rectangle area
    try:
        r = Rectangle(5, 4)
        assert r.area() == 20, f"Expected 20 but got {r.area()}"
        print("  [PASS] Test 1: Rectangle area = 20")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1: Rectangle area — {e}")
        failed += 1

    # Test 2: Square area
    try:
        s = Square(5)
        assert s.area() == 25, f"Expected 25 but got {s.area()}"
        print("  [PASS] Test 2: Square area = 25")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2: Square area — {e}")
        failed += 1

    # Test 3: Rectangle width/height are independent
    try:
        r = Rectangle(5, 4)
        r.width = 10
        assert r.height == 4, f"Changing width should not affect height! Got height={r.height}"
        assert r.area() == 40, f"Expected 40 but got {r.area()}"
        print("  [PASS] Test 3: Rectangle width/height independent")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3: Rectangle independence — {e}")
        failed += 1

    # Test 4: Square side setter
    try:
        s = Square(5)
        s.side = 7
        assert s.area() == 49, f"Expected 49 but got {s.area()}"
        print("  [PASS] Test 4: Square side setter works")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4: Square side setter — {e}")
        failed += 1

    # Test 5: Both are Shape instances (isinstance check)
    try:
        r = Rectangle(3, 4)
        s = Square(5)
        assert isinstance(r, Shape), "Rectangle should be a Shape"
        assert isinstance(s, Shape), "Square should be a Shape"
        print("  [PASS] Test 5: Both are Shape instances")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5: isinstance check — {e}")
        failed += 1

    # Test 6: Square is NOT a Rectangle
    try:
        s = Square(5)
        assert not isinstance(s, Rectangle), "Square must NOT inherit from Rectangle!"
        print("  [PASS] Test 6: Square is NOT a Rectangle (LSP safe)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 6: LSP check — {e}")
        failed += 1

    # Test 7: print_area works with both (polymorphism via Shape)
    try:
        r = Rectangle(6, 3)
        s = Square(4)
        assert print_area(r) == 18, f"Expected 18 but got {print_area(r)}"
        assert print_area(s) == 16, f"Expected 16 but got {print_area(s)}"
        print("  [PASS] Test 7: print_area works with both shapes")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 7: print_area polymorphism — {e}")
        failed += 1

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{passed+failed} tests passed")
    if failed == 0:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
