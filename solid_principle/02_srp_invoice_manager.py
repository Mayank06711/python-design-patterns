"""
================================================================================
EXERCISE 02 — SRP: Invoice Manager God Class
================================================================================
SCENARIO:
A 2000-line InvoiceManager class does EVERYTHING: creates invoices, calculates
tax, applies discounts, generates invoice text, and sends emails.

Your PM just reported 3 bugs filed by 3 different teams — all touching the
same file. Refactor this monster.

YOUR TASK:
Read the tests below. Design all classes from scratch. This time there are
MORE classes and the orchestrator has to coordinate a multi-step workflow.

SCORING:
- Correctness: /4  |  Attempts: /3  |  Hints: /2  |  Code quality: /1
- Time limit: 8 minutes (tracked, not scored)

STARTED: 2026-03-16 15:05 IST (reset after toilet break)
ATTEMPT: 1

Run:  python 02_srp_invoice_manager.py
================================================================================
"""

# ── YOUR CODE BELOW ──────────────────────────────────────────────────────────
class TaxCalculator:
    def __init__(self, tax_rate:float):
        self.tax_rate = tax_rate
    
    def calculate(self, amount:float)->float:
        return amount*self.tax_rate

class DiscountApplier: 
    def __init__(self, discount_percent:float):
        self.discount_percent = discount_percent
    
    def apply(self, amount: float)->float:
        return amount - amount*self.discount_percent/100 #// is floor division — gives an integer. Use / instead to get a float
    
class InvoiceGenerator:
    def __init__(self):
        pass
    
    def generate(self, name:str, amount:float, discount: float, tax: float)->str:
        total = amount - discount + tax 
        return f"Invoice for {name}: subtotal={amount}, discount={discount}, tax={tax}, total={total}"

class EmailSender:
    def __init__(self):
        pass 
    
    def send(self, email: str, invoice:str)->str:
        return f"Email sent to {email} with invoice"

class InvoiceService:
    def __init__(self, tax_calc: TaxCalculator, discount: DiscountApplier, generator: InvoiceGenerator, sender: EmailSender):
        self.tax_calc, self.discount, self.generator, self.sender = tax_calc, discount, generator, sender
    
    def process(self, name: str, email:str, subtotal:float)->dict:
        result = {}
        discounted_price =  self.discount.apply(subtotal)
        tax = self.tax_calc.calculate(discounted_price)
        total = discounted_price + tax
        invoice = self.generator.generate(name, subtotal, subtotal - discounted_price, tax)
        result["subtotal"] = subtotal
        result["discount"] = subtotal - discounted_price
        result["tax"] = tax
        result["total"] = total
        result["email_status"] = self.sender.send(email, invoice)
        result["invoice_text"] = invoice
        return result

    

# ── YOUR CODE ABOVE ──────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    # Test 1: TaxCalculator computes tax
    try:
        tax_calc = TaxCalculator(tax_rate=0.18)
        assert tax_calc.calculate(1000) == 180.0
        print("  [PASS] Test 1: Tax on 1000 at 18% = 180")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1: Tax calculation — {e}")
        failed += 1

    # Test 2: TaxCalculator with different rate
    try:
        tax_calc = TaxCalculator(tax_rate=0.05)
        assert tax_calc.calculate(500) == 25.0
        print("  [PASS] Test 2: Tax on 500 at 5% = 25")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2: Tax rate flexibility — {e}")
        failed += 1

    # Test 3: DiscountApplier applies percentage discount
    try:
        discount = DiscountApplier(discount_percent=10)
        assert discount.apply(1000) == 900.0
        print("  [PASS] Test 3: 10% discount on 1000 = 900")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3: Discount — {e}")
        failed += 1

    # Test 4: DiscountApplier with 0% (no discount)
    try:
        discount = DiscountApplier(discount_percent=0)
        assert discount.apply(500) == 500.0
        print("  [PASS] Test 4: 0% discount = no change")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4: Zero discount — {e}")
        failed += 1

    # Test 5: InvoiceGenerator creates invoice text
    try:
        gen = InvoiceGenerator()
        text = gen.generate("Alice", 1000, 100, 180)
        assert "Alice" in text
        assert "1000" in text
        assert "100" in text   # discount
        assert "180" in text   # tax
        assert "1080" in text  # final = 1000 - 100 + 180
        print("  [PASS] Test 5: Invoice text contains all fields")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5: Invoice generation — {e}")
        failed += 1

    # Test 6: InvoiceGenerator format check
    try:
        gen = InvoiceGenerator()
        text = gen.generate("Bob", 500, 50, 81)
        expected = "Invoice for Bob: subtotal=500, discount=50, tax=81, total=531"
        assert text == expected, f"Got: {text}"
        print("  [PASS] Test 6: Invoice format matches exactly")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 6: Invoice format — {e}")
        failed += 1

    # Test 7: EmailSender sends invoice email
    try:
        sender = EmailSender()
        result = sender.send("alice@test.com", "Invoice for Alice: subtotal=1000, discount=100, tax=180, total=1080")
        assert result == "Email sent to alice@test.com with invoice"
        print("  [PASS] Test 7: Email sent confirmation")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 7: Email sending — {e}")
        failed += 1

    # Test 8: InvoiceService orchestrates full workflow
    try:
        tax_calc = TaxCalculator(tax_rate=0.18)
        discount = DiscountApplier(discount_percent=10)
        generator = InvoiceGenerator()
        sender = EmailSender()
        service = InvoiceService(tax_calc, discount, generator, sender)

        result = service.process("Alice", "alice@test.com", 1000)
        assert result["subtotal"] == 1000
        assert result["discount"] == 100.0
        assert result["tax"] == 162.0     # tax on (1000 - 100) = 900 * 0.18
        assert result["total"] == 1062.0  # 900 + 162
        assert result["email_status"] == "Email sent to alice@test.com with invoice"
        print("  [PASS] Test 8: Full invoice workflow (discount THEN tax)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 8: Full workflow — {e}")
        failed += 1

    # Test 9: InvoiceService with zero discount
    try:
        tax_calc = TaxCalculator(tax_rate=0.10)
        discount = DiscountApplier(discount_percent=0)
        generator = InvoiceGenerator()
        sender = EmailSender()
        service = InvoiceService(tax_calc, discount, generator, sender)

        result = service.process("Bob", "bob@test.com", 500)
        assert result["subtotal"] == 500
        assert result["discount"] == 0.0
        assert result["tax"] == 50.0
        assert result["total"] == 550.0
        print("  [PASS] Test 9: No discount, tax only")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 9: Zero discount workflow — {e}")
        failed += 1

    # Test 10: InvoiceService uses injected dependencies
    try:
        tax_calc = TaxCalculator(tax_rate=0.18)
        discount = DiscountApplier(discount_percent=20)
        generator = InvoiceGenerator()
        sender = EmailSender()
        service = InvoiceService(tax_calc, discount, generator, sender)

        result = service.process("Charlie", "charlie@test.com", 2000)
        # 2000 - 20% = 1600, tax = 1600 * 0.18 = 288, total = 1888
        assert result["total"] == 1888.0
        assert "charlie@test.com" in result["email_status"]
        print("  [PASS] Test 10: Different rates, DI verified")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 10: DI check — {e}")
        failed += 1

    # Test 11: Invoice text in result matches generator output
    try:
        tax_calc = TaxCalculator(tax_rate=0.10)
        discount = DiscountApplier(discount_percent=10)
        generator = InvoiceGenerator()
        sender = EmailSender()
        service = InvoiceService(tax_calc, discount, generator, sender)

        result = service.process("Dave", "dave@test.com", 1000)
        expected_text = "Invoice for Dave: subtotal=1000, discount=100.0, tax=90.0, total=990.0"
        assert result["invoice_text"] == expected_text, f"Got: {result['invoice_text']}"
        print("  [PASS] Test 11: Invoice text stored in result")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 11: Invoice text in result — {e}")
        failed += 1

    # Test 12: Each class has exactly one job (no cross-contamination)
    try:
        # TaxCalculator should NOT have discount/email/generate methods
        tc = TaxCalculator(tax_rate=0.1)
        assert not hasattr(tc, 'apply'), "TaxCalculator should not have apply()"
        assert not hasattr(tc, 'send'), "TaxCalculator should not have send()"
        assert not hasattr(tc, 'generate'), "TaxCalculator should not have generate()"
        # DiscountApplier should NOT have tax/email/generate methods
        da = DiscountApplier(discount_percent=10)
        assert not hasattr(da, 'calculate'), "DiscountApplier should not have calculate()"
        assert not hasattr(da, 'send'), "DiscountApplier should not have send()"
        print("  [PASS] Test 12: No class leaks responsibilities to another")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 12: SRP enforcement — {e}")
        failed += 1

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{passed+failed} tests passed")
    if failed == 0:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
