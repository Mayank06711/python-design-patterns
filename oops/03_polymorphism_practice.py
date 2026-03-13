"""
Practice 3: Runtime Polymorphism

Build a payment system for Swiggy:
1. Payment (base class)
   - process(amount) — abstract, children must implement
   - receipt(amount) — returns "Receipt: ₹{amount} via {type}" (shared by all)

2. UPI(Payment)
   - __init__(self, vpa): store VPA (e.g., "mayank@upi")
   - process(amount): return "₹{amount} sent via UPI ({vpa})"

3. CreditCard(Payment)
   - __init__(self, last_four): store last 4 digits
   - process(amount): return "₹{amount} charged to card ending {last_four}"

4. COD(Payment)
   - process(amount): return "₹{amount} to be collected on delivery"

5. Write a standalone function (NOT inside any class):
   checkout(payment: Payment, amount: int) -> str
   - It should call payment.process(amount) and return the result
   - This function should work with ANY payment type without knowing which one it is
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    # def process(self, amount): thsi is not abstract method mssing abstarctmethod decorator
    #     pass
    @abstractmethod
    def process(self, amount):
        pass

    #type(self)          → <class 'UPI'>
    #type(self).__name__ → "UPI"
    def receipt(self, amount): 
        return f"Receipt: ₹{amount} via {type(self).__name__}"
    


class UPI(Payment):
    def  __init__(self, vpa: str):
        self._vpa = vpa
    
    def process(self, amount):
       return f"₹{amount} sent via UPI ({self._vpa})"


class CreditCard(Payment):
    def __init__(self, last_four):
        self._last_four = last_four
    def process(self, amount):
        return f"₹{amount} charged to card ending {self._last_four}"


class COD(Payment):
    def __init__(self):
        pass 
    def process(self,amount):
        return f"₹{amount} to be collected on delivery"


def checkout(payment: Payment, amount: int) -> str:
    return payment.process(amount) # whateer obj we pass in arg it will call process of that

    


# ============ TEST CASES (DO NOT MODIFY) ============

if __name__ == "__main__":
    # Test 1: UPI
    upi = UPI("mayank@upi")
    result = checkout(upi, 500)
    assert result == "₹500 sent via UPI (mayank@upi)", f"Got: {result}"
    print("Test 1 PASS: UPI checkout works")

    # Test 2: CreditCard
    card = CreditCard("4242")
    result = checkout(card, 1200)
    assert result == "₹1200 charged to card ending 4242", f"Got: {result}"
    print("Test 2 PASS: CreditCard checkout works")

    # Test 3: COD
    cod = COD()
    result = checkout(cod, 350)
    assert result == "₹350 to be collected on delivery", f"Got: {result}"
    print("Test 3 PASS: COD checkout works")

    # Test 4: receipt() inherited by all (not overridden)
    assert upi.receipt(500) == "Receipt: ₹500 via UPI"
    assert card.receipt(1200) == "Receipt: ₹1200 via CreditCard"
    assert cod.receipt(350) == "Receipt: ₹350 via COD"
    print("Test 4 PASS: receipt() works via inheritance for all types")

    # Test 5: Cannot instantiate abstract Payment directly
    try:
        p = Payment()
        print("Test 5 FAIL: should not be able to create Payment()")
    except TypeError:
        print("Test 5 PASS: Payment is abstract, cannot instantiate")

    # Test 6: Polymorphism — same function handles all types
    payments = [UPI("test@upi"), CreditCard("1111"), COD()]
    amounts = [100, 200, 300]
    results = [checkout(p, a) for p, a in zip(payments, amounts)]
    assert len(results) == 3
    print("Test 6 PASS: checkout() handles all payment types polymorphically")

    print(f"\nAll tests passed!")
