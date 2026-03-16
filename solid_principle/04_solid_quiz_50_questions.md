# SOLID Principles Quiz — 50 Questions
## Based on YOUR Payment Processing System + All SOLID Concepts

> **Format:** 40 MCQ (4 options each) + 10 Written/Short Answer
> **Rules:** Answer ALL. No going back. Track your score at the end.
> **Difficulty:** Mixed (Easy / Medium / Tricky)
> **Time:** No limit — but be honest with yourself.
> **IMPORTANT:** Principle tags are HIDDEN. You must identify which principle applies.

---

## SECTION A: Multiple Choice (40 Questions)

---

### Q1.
In your PaymentService, which class is responsible for deciding if a payment is valid?

- A) PaymentProcessor
- B) PaymentService
- C) PaymentValidator
- D) TransactionLogger

---

### Q2.
A developer adds a `send_receipt_email()` method to `CreditCardProcessor`. Which SOLID principle is violated?

- A) OCP
- B) LSP
- C) SRP
- D) DIP

---

### Q3.
Your PaymentService works with CreditCard, PayPal, Crypto, and UPI without any code changes to PaymentService. Which principle does this demonstrate?

- A) SRP
- B) OCP
- C) ISP
- D) LSP

---

### Q4.
A developer changes the tax rate from 18% to 20% inside TaxCalculator. Is this an OCP violation?

- A) Yes — any modification to existing code violates OCP
- B) No — changing a configuration value is not adding new behavior
- C) Yes — they should create a new TaxCalculator20 class
- D) No — OCP only applies to abstract classes

---

### Q5.
Test 14 checks that all processors are `isinstance(p, PaymentProcessor)` and return the same dict structure. Which principle does this verify?

- A) OCP
- B) DIP
- C) LSP
- D) ISP

---

### Q6.
A developer creates `FreeTrialProcessor(PaymentProcessor)` where `process()` always returns `{"status": "free", "amount": 0}` (missing "method" and "user" keys). Which principle is violated?

- A) SRP — it's doing too much
- B) LSP — it doesn't honor the parent's contract
- C) OCP — it modifies existing behavior
- D) ISP — it implements methods it doesn't need

---

### Q7.
In `PaymentService.__init__`, the constructor takes `processor: PaymentProcessor` (an ABC), not `processor: CreditCardProcessor`. Why?

- A) It's faster at runtime
- B) High-level modules should depend on abstractions, not concrete classes
- C) Python requires it for type checking
- D) It's a Python convention with no real benefit

---

### Q8.
Which principle is violated here?

```python
class PaymentService:
    def __init__(self):
        self.processor = CreditCardProcessor()  # created inside
```

- A) SRP
- B) OCP
- C) DIP
- D) Both B and C

---

### Q9.
Your PaymentProcessor ABC has only ONE abstract method: `process()`. If it also forced `validate()` and `log()`, which principle would that violate?

- A) SRP
- B) OCP
- C) ISP
- D) DIP

---

### Q10.
A fat interface `PaymentHandler` has: `process()`, `validate()`, `log()`, `send_receipt()`. CryptoProcessor only needs `process()`. What's the best fix?

- A) CryptoProcessor implements all methods with `pass`
- B) CryptoProcessor raises `NotImplementedError` for unused methods
- C) Split into separate focused interfaces: Processable, Validatable, Loggable, Receiptable
- D) Make CryptoProcessor not inherit from PaymentHandler

---

### Q11.
Your `PaymentService.pay()` method calls validator, processor, and logger. Is PaymentService violating SRP?

- A) Yes — it's doing 3 things (validate, process, log)
- B) No — its single responsibility is orchestrating the payment workflow
- C) Yes — it should only call the processor
- D) No — SRP only applies to data classes

---

### Q12.
Which line of code would be a SOLID violation if added to PaymentService?

- A) `self.logger.log(result)`
- B) `if processor_type == "crypto": self.processor = CryptoProcessor()`
- C) `return self.processor.process(user, amount)`
- D) `self.validator.validate(user, amount)`

---

### Q13.
In your system, PaymentService depends on PaymentProcessor (ABC). CreditCardProcessor implements PaymentProcessor. What's the dependency structure?

- A) PaymentService → CreditCardProcessor (direct dependency)
- B) PaymentService → PaymentProcessor ← CreditCardProcessor (both depend on abstraction)
- C) CreditCardProcessor → PaymentService
- D) PaymentProcessor → PaymentService

---

### Q14.
If TransactionLogger also had `validate_amount()` and `format_receipt()`, how many responsibilities would it have?

- A) 1
- B) 2
- C) 3
- D) Still 1 — they're all related to transactions

---

### Q15.
Your PM says: "Add BankTransfer payment method." With your current design, what do you do?

- A) Add an `elif` in PaymentService for bank transfer
- B) Create `BankTransferProcessor(PaymentProcessor)` with `process()` — done
- C) Modify PaymentProcessor ABC to add a `transfer()` method
- D) Create a completely new PaymentService for bank transfers

---

### Q16.
Which of these `process()` implementations is problematic for substitutability?

- A) Returns `{"status": "success", "method": "upi", "amount": 100, "user": "alice"}`
- B) Returns `{"status": "success", "method": "crypto", "amount": 100, "user": "bob"}`
- C) Returns `{"error": "not supported"}` (different structure entirely)
- D) Returns `{"status": "success", "method": "bnpl", "amount": 100, "user": "charlie"}`

---

### Q17.
"High-level modules should not depend on low-level modules." In your system, which is the high-level module?

- A) CreditCardProcessor
- B) PaymentProcessor (ABC)
- C) PaymentService
- D) TransactionLogger

---

### Q18.
Test 13 checks that `CreditCardProcessor` does NOT have `validate` or `log` methods. Which principle(s) does this enforce?

- A) SRP only
- B) ISP only
- C) Both SRP and ISP
- D) OCP

---

### Q19.
A developer adds a `retry()` abstract method to the PaymentProcessor ABC. All existing processors (CreditCard, PayPal, Crypto) now must implement `retry()`. Is this a SOLID violation?

- A) No — ABCs are meant to be extended with new methods
- B) Yes — modifying the ABC forces changes to ALL existing implementations
- C) No — adding methods is always fine
- D) Yes — but only if retry() is abstract

---

### Q20.
Which of these class names suggests a SOLID violation?

- A) `UserAuthenticator`
- B) `InvoiceGeneratorAndEmailer`
- C) `PaymentValidator`
- D) `TransactionLogger`

---

### Q21.
Why does `Square(Rectangle)` violate a SOLID principle?

- A) Square can't have width and height
- B) Setting width on a Square changes height too, breaking Rectangle's contract that width and height are independent
- C) Square is not a shape
- D) Rectangle should inherit from Square

---

### Q22.
Your PaymentService receives its dependencies through `__init__`. What type of dependency injection is this?

- A) Setter injection
- B) Interface injection
- C) Constructor injection
- D) Field injection

---

### Q23.
Why doesn't PaymentValidator inherit from any ABC in your system?

- A) It should — this is a design flaw
- B) There's only one validation strategy needed — no polymorphism required, so no ABC needed
- C) Python doesn't support ABCs for validators
- D) ISP forbids validators from having ABCs

---

### Q24.
Your system currently hardcodes the failure reason: `"invalid amount"`. A developer changes it to `"invalid payment details"`. Is this a SOLID violation?

- A) Yes — any string change is a modification that violates SOLID
- B) No — changing a message string is not adding new behavior variants
- C) Yes — they should create a new PaymentService class
- D) No — SOLID doesn't apply to string literals at all

---

### Q25.
Test 13 checks that no class has methods belonging to another class (e.g., processor doesn't have `validate`). Why is this test important?

- A) It verifies that no existing code was modified
- B) It verifies each class has exactly one responsibility
- C) It verifies classes depend on abstractions
- D) It verifies all subclasses honor the contract

---

### Q26.
All your processors return a dict with keys: status, method, amount, user. This consistent return structure is called a:

- A) Precondition
- B) Postcondition / contract
- C) Invariant
- D) Side effect

---

### Q27.
If Python didn't have ABC, could you still follow DIP?

- A) No — DIP requires abstract classes in all languages
- B) Yes — duck typing means you depend on the interface implicitly
- C) No — DIP only works with compiled languages like Java
- D) Yes — but only with typing.Protocol, nothing else works

---

### Q28.
PaymentService is called an "orchestrator." Which statement about orchestrators is TRUE?

- A) An orchestrator should contain all business logic directly
- B) An orchestrator delegates work to other classes but doesn't DO the work itself
- C) An orchestrator must inherit from ABC
- D) An orchestrator always violates SRP because it calls multiple classes

---

### Q29.
Which code pattern is a classic SOLID violation, and which follows SOLID?

```python
# Pattern X
if method == "credit_card":
    process_credit_card()
elif method == "paypal":
    process_paypal()
elif method == "crypto":
    process_crypto()

# Pattern Y
processor.process(user, amount)
```

- A) X violates SOLID; Y follows SOLID
- B) Y violates SOLID; X follows SOLID
- C) Both violate SOLID
- D) Neither violates SOLID

---

### Q30.
Your PaymentProcessor ABC has only `process()`. A developer wants to add `refund()` support. Some processors don't support refunds. Best approach?

- A) Add `refund()` to PaymentProcessor ABC — processors that can't refund raise NotImplementedError
- B) Create a separate `RefundableProcessor(ABC)` with `refund()` — only refund-supporting processors inherit it
- C) Add `refund()` as a non-abstract method with a default `pass`
- D) Add refund logic inside `process()` with an if-check

---

### Q31.
How many "reasons to change" does your PaymentValidator have?

- A) 1 — if validation rules change
- B) 2 — if validation rules change OR if payment methods change
- C) 3 — validation, logging, and processing
- D) 0 — validators never need to change

---

### Q32.
Test 10 creates `UPIProcessor` (not in your original code) and passes it to PaymentService. This works because:

- A) Python is dynamically typed so anything works
- B) UPIProcessor inherits PaymentProcessor and honors its contract
- C) PaymentService doesn't actually check the processor type
- D) UPI is just a string in the method field

---

### Q33.
In traditional code: `PaymentService → CreditCardProcessor` (direct). With DIP: `PaymentService → PaymentProcessor ← CreditCardProcessor`. What changed?

- A) The dependency was completely removed
- B) The dependency direction was INVERTED — low-level now depends on the abstraction too
- C) Nothing changed, it's just a naming convention
- D) CreditCardProcessor now depends on PaymentService

---

### Q34.
Match each test to the principle it primarily verifies:
- Test 1 (ABC prevents instantiation without process())
- Test 10 (UPI works without modifying existing code)
- Test 13 (no class has methods from another class)
- Test 14 (all processors are proper subtypes with same return structure)

- A) OCP, SRP, LSP, ISP
- B) OCP, OCP, SRP, LSP
- C) ISP, OCP, SRP, LSP
- D) LSP, OCP, SRP, ISP

---

### Q35.
A developer argues: "PaymentService has 3 dependencies, so it has 3 responsibilities." Is this correct?

- A) Yes — one dependency = one responsibility
- B) No — PaymentService's ONE responsibility is orchestrating; it DELEGATES the 3 tasks
- C) Yes — it should be split into 3 services
- D) No — but only because Python handles it differently than Java

---

### Q36.
Why is PaymentProcessor an ABC and not a concrete class?

- A) ABCs are faster in Python
- B) It defines a contract that all processors must follow, enabling extension without modifying existing code
- C) Concrete classes can't have subclasses in Python
- D) It's a Python convention with no design benefit

---

### Q37.
Which of these is a code smell that suggests a SOLID violation?

- A) `def process(self): return {"status": "success"}`
- B) `def refund(self): pass  # not supported`
- C) `def validate(self, user, amount): return bool(user)`
- D) `def log(self, data): self.logs.append(data)`

---

### Q38.
Because PaymentService depends on PaymentProcessor (ABC) instead of CreditCardProcessor directly, you can easily:

- A) Skip writing tests entirely
- B) Inject a MockProcessor for unit testing without hitting real payment APIs
- C) Remove the ABC and use strings instead
- D) Make PaymentService a singleton

---

### Q39.
Original God class: `PaymentManager` does validation, processing, logging, and emailing. You split it into 4 focused classes + orchestrator. Which principles did this refactoring apply?

- A) Only SRP
- B) SRP + DIP
- C) SRP + DIP + ISP
- D) All 5 SOLID principles potentially

---

### Q40.
OCP says "extend via new classes." LSP says "new subclasses must honor the parent's contract." What happens if you follow OCP but violate LSP?

- A) Nothing — they're completely independent
- B) The new class extends the system but BREAKS existing behavior — worst of both worlds
- C) LSP automatically fixes itself if OCP is followed
- D) You can't violate LSP if you follow OCP

---

## SECTION B: Written / Short Answer (10 Questions)

---

### Q41.
In one sentence, explain SRP using your payment system as the example.

> Your answer: ___

---

### Q42.
Your PM says: "Add AfterPay (buy now, pay later) support." List the exact steps you'd take. How many existing files do you modify?

> Your answer: ___

---

### Q43.
```python
class CashProcessor(PaymentProcessor):
    def process(self, user_id, amount):
        if amount > 500:
            raise ValueError("Cash payments over 500 not allowed")
        return {"status": "success", "method": "cash", "amount": amount, "user": user_id}
```
Does this violate any SOLID principle? Which one and why?

> Your answer: ___

---

### Q44.
Draw (or describe in words) the dependency arrows for: PaymentService, PaymentProcessor (ABC), CreditCardProcessor, PayPalProcessor. Which direction do arrows point?

> Your answer: ___

---

### Q45.
A colleague wrote this ABC:
```python
class PaymentHandler(ABC):
    @abstractmethod
    def process(self): pass
    @abstractmethod
    def refund(self): pass
    @abstractmethod
    def generate_receipt(self): pass
    @abstractmethod
    def send_notification(self): pass
```
CryptoProcessor only needs `process()`. Redesign this following SOLID principles.

> Your answer: ___

---

### Q46.
List all the "reasons to change" for your PaymentService class. Is it truly just one? Defend your answer.

> Your answer: ___

---

### Q47.
For each scenario, name the SOLID principle being violated:
1. `PaymentService` creates `CreditCardProcessor()` inside its constructor
2. `CreditCardProcessor.process()` also sends an email receipt
3. Adding PayPal requires adding `elif "paypal"` inside PaymentService
4. `FreeProcessor.process()` returns `None` instead of a dict

> Your answer: ___

---

### Q48.
Your payment system uses inheritance (PaymentProcessor ABC) for OCP. Could you achieve the same using the Strategy pattern with composition instead? Describe how.

> Your answer: ___

---

### Q49.
An interviewer asks: "Walk me through how your payment system follows SOLID. Give me one specific example for each letter." Write your answer as if speaking in an interview.

> Your answer: ___

---

### Q50.
Apply the SAME architecture from your payment system to a completely different domain: a **notification system** (email, SMS, push, Slack). Name the classes you'd create and which SOLID principle each one demonstrates.

> Your answer: ___

---

## ANSWER KEY

> **DO NOT READ until you've answered ALL questions.**
> When ready, tell Claude "grade me" and I'll score your responses.

---

## Scoring
- MCQ (Q1-Q40): 1 point each = /40
- Written (Q41-Q50): 2 points each = /20
- **Total: /60**

| Score | Verdict |
|-------|---------|
| 50-60 | SOLID master — ready for interviews |
| 40-49 | Strong understanding — minor gaps |
| 30-39 | Decent — needs review on weak areas |
| 20-29 | Shaky — revisit conceptual foundations |
| <20 | Re-study all 5 principles before proceeding |
