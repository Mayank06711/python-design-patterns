"""
================================================================================
EXERCISE 03 — SOLID CAPSTONE: Payment Processing System
================================================================================
SCENARIO:
You're building a payment processing system for an e-commerce platform.
It must support multiple payment methods, apply validation rules, log
transactions, and be easily extensible for new payment types.

This is NOT an isolated principle exercise. You need ALL of SOLID:
- SRP: Each class does ONE thing
- OCP: Adding a new payment method = new class, ZERO changes to existing code
- LSP: All payment processors honor the same contract
- ISP: Clean, focused interfaces (no forced methods)
- DIP: The service depends on abstractions, not concrete classes

YOUR TASK:
Read the tests below. Design the ENTIRE system from scratch.
There are ABCs, concrete classes, and an orchestrator.
The tests tell you exactly what's needed — but the DESIGN is yours.

DIFFICULTY: Advanced (combines all SOLID principles)

SCORING:
- Correctness: /4  |  Attempts: /3  |  Hints: /2  |  Code quality: /1
- Time limit: 12 minutes (tracked, not scored — this is harder)

STARTED: 2026-03-16 17:37 IST
SUBMITTED: 2026-03-16 18:12 IST (2 runs)
ATTEMPT: 2

Run:  python 03_solid_capstone_payment_system.py
================================================================================
"""
from abc import ABC, abstractmethod
from typing import List

# ── YOUR CODE BELOW ──────────────────────────────────────────────────────────
class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, user:str, amount:float)->List:
        pass

class CreditCardProcessor(PaymentProcessor):
    def __init__(self):
        pass 
    
    def process(self, user: str, amount: float)->List:
        return {"status": "success", "method": "credit_card", "amount": amount, "user": user}

class PayPalProcessor(PaymentProcessor):
    def __init__(self):
        pass 
    
    def process(self, user: str, amount)->List:
        return {"status": "success", "method": "paypal", "amount": amount, "user": user} 


class CryptoProcessor(PaymentProcessor):
    def __init__(self):
        pass 
    
    def process(self, user: str, amount: float)->List:
        return {"status": "success", "method": "crypto", "amount": amount, "user": user}

class PaymentValidator:
    def __init__(self):
        pass 
    
    def validate(self, user: str, amount: float)->bool:
        return bool(user) and amount > 0
    
class TransactionLogger:
    def __init__(self):
        self.logs = [] 
    
    def log(self, msg: dict)->str:
        self.logs.append(msg)

    def get_logs(self):
        return self.logs

class PaymentService:
    def __init__(self, processor: PaymentProcessor, validator: PaymentValidator, logger: TransactionLogger):
        self.processor, self.validator, self.logger = processor, validator, logger
    
    def pay(self, user:str, amount: float):
        is_validated = self.validator.validate(user, amount)
        if is_validated:
            pay_result = self.processor.process(user, amount)
            self.logger.log(pay_result)
            return pay_result
        self.logger.log({"status": "failed", "reason": "invalid amount"})
        return {"status": "failed", "reason": "invalid amount"}


# ── YOUR CODE ABOVE ──────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    # ── Test 1: PaymentProcessor ABC enforces contract ──
    try:
        class BrokenProcessor(PaymentProcessor):
            pass
        bp = BrokenProcessor()
        print("  [FAIL] Test 1: ABC should prevent instantiation without process()")
        failed += 1
    except TypeError:
        print("  [PASS] Test 1: PaymentProcessor ABC enforces process() contract")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1: ABC — {e}")
        failed += 1

    # ── Test 2: CreditCardProcessor processes payment ──
    try:
        cc = CreditCardProcessor()
        result = cc.process("user1", 100.0)
        assert result == {"status": "success", "method": "credit_card", "amount": 100.0, "user": "user1"}
        print("  [PASS] Test 2: CreditCard processes payment")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2: CreditCard — {e}")
        failed += 1

    # ── Test 3: PayPalProcessor processes payment ──
    try:
        pp = PayPalProcessor()
        result = pp.process("user2", 250.0)
        assert result == {"status": "success", "method": "paypal", "amount": 250.0, "user": "user2"}
        print("  [PASS] Test 3: PayPal processes payment")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3: PayPal — {e}")
        failed += 1

    # ── Test 4: CryptoProcessor processes payment ──
    try:
        crypto = CryptoProcessor()
        result = crypto.process("user3", 500.0)
        assert result == {"status": "success", "method": "crypto", "amount": 500.0, "user": "user3"}
        print("  [PASS] Test 4: Crypto processes payment")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4: Crypto — {e}")
        failed += 1

    # ── Test 5: PaymentValidator validates correctly ──
    try:
        validator = PaymentValidator()
        assert validator.validate("user1", 100.0) == True
        assert validator.validate("", 100.0) == False      # empty user
        assert validator.validate("user1", 0) == False      # zero amount
        assert validator.validate("user1", -50) == False     # negative amount
        print("  [PASS] Test 5: Validator accepts/rejects correctly")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5: Validation — {e}")
        failed += 1

    # ── Test 6: TransactionLogger logs and retrieves ──
    try:
        logger = TransactionLogger()
        logger.log({"status": "success", "method": "credit_card", "amount": 100.0, "user": "user1"})
        logger.log({"status": "failed", "reason": "invalid amount"})
        logs = logger.get_logs()
        assert len(logs) == 2
        assert logs[0]["method"] == "credit_card"
        assert logs[1]["status"] == "failed"
        print("  [PASS] Test 6: Logger stores and retrieves transactions")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 6: Logger — {e}")
        failed += 1

    # ── Test 7: PaymentService orchestrates happy path ──
    try:
        cc = CreditCardProcessor()
        validator = PaymentValidator()
        logger = TransactionLogger()
        service = PaymentService(cc, validator, logger)
        result = service.pay("user1", 100.0)
        assert result["status"] == "success"
        assert result["method"] == "credit_card"
        assert len(logger.get_logs()) == 1
        print("  [PASS] Test 7: PaymentService happy path (credit card)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 7: Happy path — {e}")
        failed += 1

    # ── Test 8: PaymentService rejects invalid payment ──
    try:
        pp = PayPalProcessor()
        validator = PaymentValidator()
        logger = TransactionLogger()
        service = PaymentService(pp, validator, logger)
        result = service.pay("", 100.0)   # empty user
        assert result["status"] == "failed"
        assert "invalid" in result["reason"].lower()
        assert len(logger.get_logs()) == 1  # failure is also logged
        print("  [PASS] Test 8: Invalid payment rejected and logged")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 8: Rejection — {e}")
        failed += 1

    # ── Test 9: PaymentService works with ANY processor (DIP) ──
    try:
        crypto = CryptoProcessor()
        validator = PaymentValidator()
        logger = TransactionLogger()
        service = PaymentService(crypto, validator, logger)
        result = service.pay("user3", 999.0)
        assert result["method"] == "crypto"
        assert result["amount"] == 999.0
        print("  [PASS] Test 9: Service works with Crypto (DIP verified)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 9: DIP — {e}")
        failed += 1

    # ── Test 10: OCP — Adding new processor needs ZERO changes ──
    try:
        # Simulating a NEW payment method added by another developer
        class UPIProcessor(PaymentProcessor):
            def process(self, user_id: str, amount: float) -> dict:
                return {"status": "success", "method": "upi", "amount": amount, "user": user_id}

        upi = UPIProcessor()
        validator = PaymentValidator()
        logger = TransactionLogger()
        service = PaymentService(upi, validator, logger)
        result = service.pay("user4", 75.0)
        assert result["method"] == "upi"
        assert result["status"] == "success"
        print("  [PASS] Test 10: New UPI processor works without ANY code changes (OCP)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 10: OCP — {e}")
        failed += 1

    # ── Test 11: PaymentService uses injected dependencies (not internal) ──
    try:
        cc = CreditCardProcessor()
        validator = PaymentValidator()
        logger = TransactionLogger()
        service = PaymentService(cc, validator, logger)
        service.pay("user5", 200.0)
        # The SAME logger object should have the log
        assert len(logger.get_logs()) == 1
        assert logger.get_logs()[0]["user"] == "user5"
        print("  [PASS] Test 11: Service uses injected logger (not internal copy)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 11: DI check — {e}")
        failed += 1

    # ── Test 12: Multiple payments through same service ──
    try:
        cc = CreditCardProcessor()
        validator = PaymentValidator()
        logger = TransactionLogger()
        service = PaymentService(cc, validator, logger)

        service.pay("alice", 100.0)
        service.pay("bob", 200.0)
        service.pay("", -5.0)    # invalid — should fail but still log

        logs = logger.get_logs()
        assert len(logs) == 3
        assert logs[0]["status"] == "success"
        assert logs[1]["status"] == "success"
        assert logs[2]["status"] == "failed"
        print("  [PASS] Test 12: Multiple payments, all logged (success + failure)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 12: Multiple payments — {e}")
        failed += 1

    # ── Test 13: Each class has single responsibility (SRP check) ──
    try:
        cc = CreditCardProcessor()
        v = PaymentValidator()
        l = TransactionLogger()
        # Processor should NOT have validate/log
        assert not hasattr(cc, 'validate'), "Processor should not validate"
        assert not hasattr(cc, 'log'), "Processor should not log"
        # Validator should NOT have process/log
        assert not hasattr(v, 'process'), "Validator should not process"
        assert not hasattr(v, 'log'), "Validator should not log"
        # Logger should NOT have process/validate
        assert not hasattr(l, 'process'), "Logger should not process"
        assert not hasattr(l, 'validate'), "Logger should not validate"
        print("  [PASS] Test 13: Each class has single responsibility (SRP)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 13: SRP check — {e}")
        failed += 1

    # ── Test 14: PaymentProcessor subclasses are proper subtypes (LSP) ──
    try:
        processors = [CreditCardProcessor(), PayPalProcessor(), CryptoProcessor()]
        for p in processors:
            assert isinstance(p, PaymentProcessor), f"{type(p).__name__} is not a PaymentProcessor"
            result = p.process("test_user", 1.0)
            assert "status" in result, f"{type(p).__name__} missing 'status' in result"
            assert "method" in result, f"{type(p).__name__} missing 'method' in result"
            assert "amount" in result, f"{type(p).__name__} missing 'amount' in result"
            assert "user" in result, f"{type(p).__name__} missing 'user' in result"
        print("  [PASS] Test 14: All processors are proper PaymentProcessor subtypes (LSP)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 14: LSP — {e}")
        failed += 1

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{passed+failed} tests passed")
    if failed == 0:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
