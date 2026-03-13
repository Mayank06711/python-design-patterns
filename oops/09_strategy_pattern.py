"""
================================================================================
EXERCISE 09 — Strategy Pattern (Discount System)
================================================================================
Build a shopping cart with swappable discount strategies.

YOUR TASK:
1. Create DiscountStrategy ABC with abstract method `apply(total: float) -> float`
   - apply() returns the FINAL price after discount (not the discount amount)
2. Create PercentageDiscount(DiscountStrategy) — takes `percent` (e.g., 10 means 10% off)
3. Create FlatDiscount(DiscountStrategy) — takes `amount` (e.g., 500 means ₹500 off)
4. Create NoDiscount(DiscountStrategy) — returns total unchanged
5. Create ShoppingCart class:
   - __init__(self, discount: DiscountStrategy)
   - add_item(name: str, price: float)
   - set_discount(discount: DiscountStrategy) — swap strategy at runtime
   - total() -> float — returns sum of item prices
   - checkout() -> float — returns total AFTER applying discount

RULES:
- Discount can never make price negative (minimum is 0)
- PercentageDiscount: percent is 0-100 range
- Adding a new discount type should require ZERO changes to ShoppingCart

Run this file to test:  python 09_strategy_pattern.py
================================================================================
"""
from abc import ABC, abstractmethod

# ── YOUR CODE BELOW ──────────────────────────────────────────────────────────
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
        
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        if 0 <= percent <= 100:
            self.percent = percent
        else:
            raise ValueError("Percent must be between 0 and 100")

    def apply(self, total:float)->float:
        final_amt  = total - total*self.percent/100 
        if final_amt < 0:
            final_amt = 0
        return final_amt

class FlatDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount
    
    def apply(self, total: float) -> float:
        if total > self.amount:
            return total - self.amount
        return 0 

class NoDiscount(DiscountStrategy):
    def apply(self, total:float)->float:
        return total

class ShoppingCart:
    def __init__(self, discount: DiscountStrategy):
        self.discount = discount
        self.item_name = []
        self.item_price = []
    
    def add_item(self, name:str, price: float):
        self.item_name.append(name)
        self.item_price.append(price)
            
    def set_discount(self, discount: DiscountStrategy):
        self.discount = discount
    
    def total(self)->float:
        return sum(self.item_price)

    def checkout(self):
        return self.discount.apply(self.total())

# ── YOUR CODE ABOVE ──────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    # Test 1: No discount
    try:
        cart = ShoppingCart(NoDiscount())
        cart.add_item("Laptop", 50000)
        cart.add_item("Mouse", 500)
        assert cart.checkout() == 50500, f"Expected 50500 but got {cart.checkout()}"
        print("  [PASS] Test 1: No discount — full price")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1: No discount — {e}")
        failed += 1

    # Test 2: Percentage discount
    try:
        cart = ShoppingCart(PercentageDiscount(10))
        cart.add_item("Laptop", 50000)
        cart.add_item("Mouse", 500)
        assert cart.checkout() == 45450.0, f"Expected 45450.0 but got {cart.checkout()}"
        print("  [PASS] Test 2: 10% off ₹50500 = ₹45450")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2: Percentage discount — {e}")
        failed += 1

    # Test 3: Flat discount
    try:
        cart = ShoppingCart(FlatDiscount(5000))
        cart.add_item("Laptop", 50000)
        cart.add_item("Mouse", 500)
        assert cart.checkout() == 45500, f"Expected 45500 but got {cart.checkout()}"
        print("  [PASS] Test 3: ₹5000 flat off ₹50500 = ₹45500")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3: Flat discount — {e}")
        failed += 1

    # Test 4: Swap discount at runtime
    try:
        cart = ShoppingCart(NoDiscount())
        cart.add_item("Phone", 30000)
        assert cart.checkout() == 30000

        cart.set_discount(PercentageDiscount(20))
        assert cart.checkout() == 24000.0, f"Expected 24000.0 but got {cart.checkout()}"

        cart.set_discount(FlatDiscount(3000))
        assert cart.checkout() == 27000, f"Expected 27000 but got {cart.checkout()}"
        print("  [PASS] Test 4: Discount swapped at runtime")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4: Runtime swap — {e}")
        failed += 1

    # Test 5: Discount can't make price negative
    try:
        cart = ShoppingCart(FlatDiscount(100000))
        cart.add_item("Pen", 50)
        assert cart.checkout() == 0, f"Expected 0 but got {cart.checkout()}"
        print("  [PASS] Test 5: Flat discount capped at 0 (no negative)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5: Negative price guard — {e}")
        failed += 1

    # Test 6: total() vs checkout()
    try:
        cart = ShoppingCart(PercentageDiscount(50))
        cart.add_item("A", 1000)
        cart.add_item("B", 2000)
        assert cart.total() == 3000, f"total() should be raw sum, got {cart.total()}"
        assert cart.checkout() == 1500.0, f"checkout() should apply discount, got {cart.checkout()}"
        print("  [PASS] Test 6: total() = raw sum, checkout() = after discount")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 6: total vs checkout — {e}")
        failed += 1

    # Test 7: New strategy without changing ShoppingCart
    try:
        class Buy2Get1Free(DiscountStrategy):
            def apply(self, total: float) -> float:
                return total * (2/3)

        cart = ShoppingCart(Buy2Get1Free())
        cart.add_item("Shirt", 1000)
        cart.add_item("Shirt", 1000)
        cart.add_item("Shirt", 1000)
        result = cart.checkout()
        assert abs(result - 2000.0) < 0.01, f"Expected ~2000 but got {result}"
        print("  [PASS] Test 7: New Buy2Get1Free strategy works (no ShoppingCart changes)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 7: New strategy — {e}")
        failed += 1

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{passed+failed} tests passed")
    if failed == 0:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
