# SOLID Principles Interview Questions (26 Questions - Mid to Advanced)

> Curated from Google, Amazon, Meta, Microsoft interviews
> Full code examples available in `solid_principles_interview_questions.py`

---

## Quick Reference

| # | Principle(s) | Level | Type | Topic |
|---|-------------|-------|------|-------|
| 1 | SRP | Mid | Code Refactor | User registration God method |
| 2 | OCP | Mid | Code Refactor | Discount calculator if/elif |
| 3 | LSP | Advanced | Classic Problem | Rectangle-Square |
| 4 | ISP | Mid | Code Refactor | Worker interface (human vs robot) |
| 5 | DIP | Mid | Code Refactor | Database coupling |
| 6 | SRP + OCP | Advanced | God Class | InvoiceManager decomposition |
| 7 | LSP | Advanced | Conceptual | ReadOnly vs Mutable collections |
| 8 | OCP | Advanced | System Design | Notification system |
| 9 | ISP | Advanced | Interface Design | Data source fat interface |
| 10 | DIP | Advanced | System Design | Analytics multi-backend |
| 11 | SRP | Advanced | Architecture | Microservices decomposition |
| 12 | LSP | Advanced | Conceptual | Cache behavioral subtyping |
| 13 | OCP + DIP | Advanced | System Design | Plugin file parser architecture |
| 14 | ISP | Advanced | API Design | SDK client interface segregation |
| 15 | ALL | Advanced | Full Refactor | E-commerce system rewrite |
| 16 | DIP | Advanced | Testing | Mock objects and testability |
| 17 | LSP | Advanced | Conceptual | Exception contracts |
| 18 | SRP + OCP | Advanced | System Design | Logging framework |
| 19 | LSP + ISP | Advanced | Conceptual | Java Collections design flaw |
| 20 | ALL | Advanced | System Design | Ride-sharing (Uber) LLD |
| 21 | OCP | Advanced | Design Pattern | Validation pipeline |
| 22 | SRP | Advanced | Conceptual | When NOT to split (over-engineering) |
| 23 | OCP | Advanced | Design Pattern | Decorator pattern (coffee shop) |
| 24 | DIP | Advanced | Conceptual | Hollywood Principle & frameworks |
| 25 | ALL | Advanced | Code Review | PR review scenario |
| 26 | SRP + DIP | Advanced | Architecture | CQRS / Event Sourcing |

---

## Q1. [SRP - Mid] User Registration God Method
**The following class handles registration, email, and logging all in one place. Identify every SRP violation and refactor.**

Violation: 4 reasons to change (validation rules, DB schema, email provider, logging format).
Fix: Split into `UserValidator`, `UserRepository`, `EmailService`, `EventLogger`, `UserRegistrationService`.

---

## Q2. [OCP - Mid] Discount Calculator
**This uses if/elif chains. Every new customer type = modify the class. Refactor for OCP.**

Fix: `DiscountStrategy` ABC with subclasses (`RegularDiscount`, `PremiumDiscount`, `VIPDiscount`). Adding `EmployeeDiscount` = new class, zero changes to existing code.

---

## Q3. [LSP - Advanced] Rectangle-Square
**Demonstrate how Square extending Rectangle violates LSP. Show breaking test. Fix it.**

Key: `setWidth()` on Square also changes height (side-effect). Fix: Both implement `Shape` ABC, no inheritance between them.

---

## Q4. [ISP - Mid] Worker Interface
**`IWorker` has `work()`, `eat()`, `sleep()`. Robot must implement `eat()` = ISP violation.**

Fix: Split into `Workable`, `Eatable`, `Sleepable`. Robot only implements `Workable`.

---

## Q5. [DIP - Mid] Database Coupling
**OrderService directly creates MySQLDatabase. Refactor for DIP.**

Fix: `DatabaseInterface` ABC. OrderService accepts it via constructor. Can swap MySQL, Postgres, or MockDB.

---

## Q6. [SRP + OCP - Advanced] InvoiceManager God Class
**2000-line class: creates invoices, calculates tax, applies discounts, generates PDFs, sends emails.**

Fix: `InvoiceFactory`, `TaxCalculator(ABC)`, `DiscountApplier(ABC)`, `PDFGenerator`, `InvoiceEmailer`, `InvoiceService` (orchestrator).

---

## Q7. [LSP - Advanced] ReadOnly vs Mutable Collections
**MutableCollection extends ReadOnlyCollection. Does this violate LSP?**

Answer: NO. Mutable can do everything ReadOnly can + more. But ReadOnly extending Mutable WOULD violate LSP.

---

## Q8. [OCP - Advanced] Notification System
**Design Email + SMS + Push notifications. Adding Slack tomorrow should require zero existing code changes.**

Fix: `NotificationChannel` ABC → concrete channels. `NotificationService` takes a list of channels.

---

## Q9. [ISP - Advanced] Fat DataSource Interface
**DataSource has read/write/seek/close/getMetadata. ReadOnlyFile can't seek, NetworkStream can't seek.**

Fix: Split into `Readable`, `Writable`, `Seekable`, `Closable`, `MetadataProvider`. Each class picks what it needs.

---

## Q10. [DIP - Advanced] Analytics Multi-Backend
**Analytics logs to file. Now add Kafka, Datadog, HTTP. Refactor so analytics never knows about backends.**

Fix: `AnalyticsBackend` ABC. `AnalyticsService` takes a list of backends. MockBackend for testing.

---

## Q11. [SRP - Advanced] Microservices Decomposition
**Monolithic OrderProcessor: validates, checks inventory, processes payment, emails, analytics. How does SRP apply at SERVICE level?**

Fix: OrderService, InventoryService, PaymentService, NotificationService, AnalyticsService. Sync for critical path, async events for side effects.

---

## Q12. [LSP - Advanced] Cache Behavioral Subtyping
**Base `Cache.get()` returns None for missing keys. `StrictCache.get()` raises KeyError. LSP violation?**

YES. Postcondition changed (None → exception). Code expecting None will crash.

---

## Q13. [OCP + DIP - Advanced] Plugin File Parser
**CSV/JSON/XML/Parquet parser. New formats added at runtime.**

Fix: `FileParser` ABC with `can_parse()` + `parse()`. `ParserRegistry` stores parsers. `FileProcessingService` asks registry.

---

## Q14. [ISP - Advanced] SDK Client Interfaces
**Single APIClient forces read-only consumers to depend on write/admin methods.**

Fix: `ReadableAPI`, `WritableAPI`, `AdminAPI`. `FullAPIClient` implements all. `ReadOnlyClient` implements only `ReadableAPI`.

---

## Q15. [ALL - Advanced] E-Commerce Full Refactor
**Class violates ALL 5 SOLID principles. Identify each and provide complete refactored design.**

S: Does ordering + payment + shipping + notifications.
O: if/elif for payment and shipping.
L: Prevented by polymorphic design.
I: Everything in one class.
D: Hardcoded dependencies.

---

## Q16. [DIP - Advanced] Testing & Mocking
**ReportGenerator creates ProductionDatabase, PDFFormatter, SMTPEmailSender internally. Why untestable?**

Fix: Inject `DataFetcher`, `ReportFormatter`, `ReportSender` abstractions. Test with mocks.

---

## Q17. [LSP - Advanced] Exception Contracts
**PaymentGateway.charge() raises InsufficientFundsError. StripeGateway raises ConnectionError. LSP violation?**

Depends on base contract. If only InsufficientFundsError allowed → YES. If PaymentError base exception → NO.

---

## Q18. [SRP + OCP - Advanced] Logging Framework
**Multiple targets (console, file, remote) + multiple formats (text, JSON). Extensible.**

Fix: `LogFormatter(ABC)`, `LogTarget(ABC)`, `Logger` (composes formatter + targets).

---

## Q19. [LSP + ISP - Advanced] Java Collections Design Flaw
**`Collections.unmodifiableList()` returns List that throws on `add()`. Why is this LSP + ISP violation?**

LSP: Client expects add() to work. ISP: ReadOnly forced to expose mutation methods. Fix: Separate ReadableList and MutableList interfaces.

---

## Q20. [ALL - Advanced] Ride-Sharing System (Uber LLD)
**Vehicle types, pricing strategies, payment methods, notifications. Apply all 5 principles.**

SRP: Separate classes per concern. OCP: Strategy for pricing/payment. LSP: All payment methods honor contract. ISP: RideRequestable, RideTrackable, RideCompletable. DIP: RideService accepts abstractions.

---

## Q21. [OCP - Advanced] Validation Pipeline
**Email, password, age validation. Add phone/address without modifying pipeline.**

Fix: `ValidationRule` ABC. `ValidationPipeline` takes list of rules. New rule = new class.

---

## Q22. [SRP - Advanced] When NOT to Split
**UserProfile with getName/getEmail/getAddress violates SRP?**

NO. All relate to same concern (profile data). SRP = one REASON TO CHANGE, not "one thing."

---

## Q23. [OCP - Advanced] Decorator Pattern (Coffee Shop)
**Toppings (milk, sugar, whip) as decorators. Stackable, no modification needed.**

`BeverageDecorator` wraps `Beverage`. Each topping = new decorator class.

---

## Q24. [DIP - Advanced] Hollywood Principle
**"Don't call us, we'll call you." How DIP manifests in frameworks, DI containers, event systems.**

Framework calls YOUR code (not the reverse). EventBus: publishers don't know subscribers.

---

## Q25. [ALL - Advanced] Code Review Scenario
**Find ALL SOLID violations in a PaymentProcessor PR.**

DIP: hardcoded deps. OCP: if/elif payment types. SRP: processing + logging + reporting. ISP: depends on full Stripe API.

---

## Q26. [SRP + DIP - Advanced] CQRS / Event Sourcing
**How CQRS naturally enforces SRP (separate read/write) and DIP (abstract repositories).**

Command side: business logic. Query side: read projections. Scale independently, test independently.
