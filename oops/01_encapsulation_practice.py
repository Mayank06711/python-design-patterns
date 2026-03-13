"""
Practice 1: Encapsulation
Build a BankAccount class with proper encapsulation.

Requirements:
- Private fields: _balance, _owner, _transaction_history (list)
- deposit(amount): adds to balance, logs to history, rejects negative amounts
- withdraw(amount): subtracts from balance, rejects if insufficient funds, logs to history
- get_balance(): returns balance (read-only access)
- get_statement(): returns a copy of transaction_history (NOT the original — defensive copy!)

Test cases verify your implementation. Just write the class.
"""

from typing import List
import copy
class BankAccount:
    # YOUR CODE HERE
    def __init__(self, owner: str, balance: int = 0):
        self._balance = balance
        self._owner = owner
        self._transaction_history: List = []
    def get_balance(self):
        return self._balance

    def deposit(self, balance):
        if balance < 0:
            print(f"deposted amount can not be negative, {balance}")
            raise ValueError
        
        self._balance += balance
        self._transaction_history.append(f"{self._owner}, balance is {self._balance}") 

    def withdraw(self, amount):
        if amount > self._balance:
            print("Amount can not be withdrawn, insufficient balance")
            raise ValueError
        self._balance -= amount
        self._transaction_history.append(f"{self._owner}, new balance is {self._balance}") 

    def get_statement(self):
        temp_statement = copy.copy(self._transaction_history) # so nothing is shared
        return temp_statement


# ============ TEST CASES (DO NOT MODIFY) ============

if __name__ == "__main__":
    # Test 1: Basic deposit and withdraw
    acc = BankAccount("Mayank", 1000)
    acc.deposit(500)
    assert acc.get_balance() == 1500, f"Expected 1500, got {acc.get_balance()}"
    print("Test 1 PASS: deposit works")

    acc.withdraw(200)
    assert acc.get_balance() == 1300, f"Expected 1300, got {acc.get_balance()}"
    print("Test 2 PASS: withdraw works")

    # Test 3: Reject negative deposit
    try:
        acc.deposit(-100)
        print("Test 3 FAIL: should have raised ValueError")
    except ValueError:
        print("Test 3 PASS: negative deposit rejected")

    # Test 4: Reject overdraft
    try:
        acc.withdraw(99999)
        print("Test 4 FAIL: should have raised ValueError")
    except ValueError:
        print("Test 4 PASS: overdraft rejected")

    # Test 5: Transaction history logged
    history = acc.get_statement()
    assert len(history) >= 2, f"Expected at least 2 transactions, got {len(history)}"
    print(f"Test 5 PASS: {len(history)} transactions logged")

    # Test 6: Defensive copy — mutating returned list should NOT affect internal state
    history.append("HACKED ENTRY")
    real_history = acc.get_statement()
    assert "HACKED ENTRY" not in real_history, "Test 6 FAIL: encapsulation broken! Internal list was mutated"
    print("Test 6 PASS: defensive copy works, encapsulation intact")

    # Test 7: Cannot access private fields directly (convention in Python)
    print(f"\nAll tests passed!")
    print(f"Final balance: {acc.get_balance()}")
    print(f"Statement: {acc.get_statement()}")
