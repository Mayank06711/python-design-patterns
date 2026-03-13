"""
================================================================================
SOLID PRINCIPLES - INTERVIEW QUESTIONS (Mid to Advanced Level)
================================================================================
Curated from questions asked at Google, Amazon, Meta, Microsoft, and other
top tech companies. Covers all 5 SOLID principles with conceptual, coding,
and refactoring problems.

Sources:
- https://www.adaface.com/blog/solid-principles-interview-questions/
- https://www.wecreateproblems.com/interview-questions/solid-principles-interview-questions
- https://climbtheladder.com/solid-design-principles-interview-questions/
- https://www.geeksforgeeks.org/system-design/solid-principle-in-programming-understand-with-real-life-examples/
- https://www.designgurus.io/blog/essential-software-design-principles-you-should-know-before-the-interview
- https://javatechonline.com/solid-principles-interview-questions-and-answers/
- https://www.baeldung.com/java-liskov-substitution-principle
- https://reflectoring.io/interface-segregation-principle-unused-methods/
- https://www.pluralsight.com/guides/solid-design-microservices
================================================================================
"""

# =============================================================================
# QUESTION 1 [SRP - Mid Level] (Conceptual + Coding)
# =============================================================================
# The following class handles user registration, email notification, and
# logging all in one place. Identify every SRP violation and refactor it
# into a clean design. Explain why each extracted class has exactly one
# reason to change.
# Asked at: Amazon, Microsoft
# -----------------------------------------------------------------------------

class UserService_BEFORE:
    """VIOLATES SRP - has multiple reasons to change."""

    def register_user(self, username, email, password):
        # 1. Validate input
        if not username or not email or not password:
            raise ValueError("All fields required")
        if "@" not in email:
            raise ValueError("Invalid email")

        # 2. Save to database
        user = {"username": username, "email": email, "password": password}
        # db.save(user)
        print(f"User {username} saved to database")

        # 3. Send welcome email
        print(f"Sending welcome email to {email}")
        # smtp.send(email, "Welcome!", "Thanks for joining.")

        # 4. Log the event
        print(f"[LOG] User registered: {username}")
        # logger.info(f"User registered: {username}")

        return user


# REFACTORED ANSWER:

class UserValidator:
    """Single reason to change: validation rules change."""

    def validate(self, username: str, email: str, password: str) -> None:
        if not username or not email or not password:
            raise ValueError("All fields required")
        if "@" not in email:
            raise ValueError("Invalid email")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")


class UserRepository:
    """Single reason to change: data persistence mechanism changes."""

    def save(self, user: dict) -> dict:
        # db.save(user)
        print(f"User {user['username']} saved to database")
        return user


class EmailService:
    """Single reason to change: email delivery mechanism changes."""

    def send_welcome_email(self, email: str) -> None:
        print(f"Sending welcome email to {email}")


class EventLogger:
    """Single reason to change: logging strategy changes."""

    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class UserRegistrationService:
    """Orchestrates registration; single reason to change: registration workflow changes."""

    def __init__(self, validator: UserValidator, repo: UserRepository,
                 email_svc: EmailService, logger: EventLogger):
        self._validator = validator
        self._repo = repo
        self._email_svc = email_svc
        self._logger = logger

    def register(self, username: str, email: str, password: str) -> dict:
        self._validator.validate(username, email, password)
        user = self._repo.save({"username": username, "email": email, "password": password})
        self._email_svc.send_welcome_email(email)
        self._logger.log(f"User registered: {username}")
        return user


# =============================================================================
# QUESTION 2 [OCP - Mid Level] (Coding / Refactoring)
# =============================================================================
# The following discount calculator uses if/elif chains. Every time a new
# customer type is added, you must modify this class. Refactor it so new
# discount types can be added WITHOUT modifying existing code.
# Asked at: Google, Amazon
# -----------------------------------------------------------------------------

class DiscountCalculator_BEFORE:
    """VIOLATES OCP - must be modified for every new customer type."""

    def calculate(self, customer_type: str, amount: float) -> float:
        if customer_type == "regular":
            return amount * 0.05
        elif customer_type == "premium":
            return amount * 0.10
        elif customer_type == "vip":
            return amount * 0.20
        else:
            return 0.0


# REFACTORED ANSWER:

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Open for extension (new strategies), closed for modification."""

    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass


class RegularDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.05


class PremiumDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.10


class VIPDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.20


# Adding a new type requires ZERO changes to existing code:
class EmployeeDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.30


class DiscountCalculator:
    """Never needs modification -- new discounts just implement the interface."""

    def __init__(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def calculate(self, amount: float) -> float:
        return self._strategy.calculate(amount)


# =============================================================================
# QUESTION 3 [LSP - Advanced] (Classic Rectangle-Square Problem)
# =============================================================================
# A Square class inherits from Rectangle. Demonstrate precisely how this
# violates LSP. Show a function that works correctly with Rectangle but
# breaks when passed a Square. Then show the correct design.
# Asked at: Google, Meta
# -----------------------------------------------------------------------------

class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    def area(self) -> float:
        return self._width * self._height


class Square_VIOLATES_LSP(Rectangle):
    """VIOLATES LSP - setting width also changes height and vice versa."""

    def __init__(self, side: float):
        super().__init__(side, side)

    @Rectangle.width.setter
    def width(self, value: float):
        self._width = value
        self._height = value  # Side-effect that breaks LSP

    @Rectangle.height.setter
    def height(self, value: float):
        self._width = value  # Side-effect that breaks LSP
        self._height = value


def compute_area_expecting_rectangle(rect: Rectangle) -> float:
    """This function ASSUMES independent width/height -- breaks with Square."""
    rect.width = 5
    rect.height = 4
    assert rect.area() == 20, f"Expected 20 but got {rect.area()}"
    return rect.area()


# CORRECT DESIGN: Use composition or a common Shape interface

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class CorrectRectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height


class CorrectSquare(Shape):
    """Not a subclass of Rectangle -- no LSP violation possible."""

    def __init__(self, side: float):
        self._side = side

    def area(self) -> float:
        return self._side ** 2


# =============================================================================
# QUESTION 4 [ISP - Mid Level] (Coding / Refactoring)
# =============================================================================
# The following IWorker interface forces Robot to implement eat(), which
# makes no sense. Identify the ISP violation and refactor.
# Asked at: Amazon, Apple
# -----------------------------------------------------------------------------

class IWorker_BEFORE(ABC):
    """FAT INTERFACE - forces all implementers to have all methods."""

    @abstractmethod
    def work(self): pass

    @abstractmethod
    def eat(self): pass

    @abstractmethod
    def sleep(self): pass


class HumanWorker_BEFORE(IWorker_BEFORE):
    def work(self): print("Human working")
    def eat(self): print("Human eating")
    def sleep(self): print("Human sleeping")


class RobotWorker_BEFORE(IWorker_BEFORE):
    def work(self): print("Robot working")
    def eat(self): raise NotImplementedError("Robots don't eat!")  # ISP violation!
    def sleep(self): raise NotImplementedError("Robots don't sleep!")  # ISP violation!


# REFACTORED ANSWER:

class Workable(ABC):
    @abstractmethod
    def work(self): pass


class Eatable(ABC):
    @abstractmethod
    def eat(self): pass


class Sleepable(ABC):
    @abstractmethod
    def sleep(self): pass


class HumanWorker(Workable, Eatable, Sleepable):
    def work(self): print("Human working")
    def eat(self): print("Human eating")
    def sleep(self): print("Human sleeping")


class RobotWorker(Workable):
    """Only implements what it actually needs -- no dummy methods."""
    def work(self): print("Robot working")


# =============================================================================
# QUESTION 5 [DIP - Mid Level] (Coding / Refactoring)
# =============================================================================
# The following OrderService directly instantiates MySQLDatabase. How does
# this violate DIP? Refactor it so the high-level module depends on an
# abstraction, not a concrete implementation.
# Asked at: Google, Amazon
# -----------------------------------------------------------------------------

class MySQLDatabase:
    def save(self, data: dict): print(f"Saving {data} to MySQL")
    def fetch(self, id: int): return {"id": id, "item": "widget"}


class OrderService_BEFORE:
    """VIOLATES DIP - high-level module depends directly on low-level concrete class."""

    def __init__(self):
        self.db = MySQLDatabase()  # Tight coupling!

    def place_order(self, order: dict):
        self.db.save(order)


# REFACTORED ANSWER:

class DatabaseInterface(ABC):
    """Abstraction that both high-level and low-level modules depend on."""

    @abstractmethod
    def save(self, data: dict) -> None: pass

    @abstractmethod
    def fetch(self, id: int) -> dict: pass


class MySQLDB(DatabaseInterface):
    def save(self, data: dict): print(f"Saving {data} to MySQL")
    def fetch(self, id: int): return {"id": id, "item": "widget"}


class PostgresDB(DatabaseInterface):
    def save(self, data: dict): print(f"Saving {data} to Postgres")
    def fetch(self, id: int): return {"id": id, "item": "widget"}


class OrderService:
    """Depends on abstraction (DatabaseInterface), not concretion."""

    def __init__(self, db: DatabaseInterface):
        self._db = db  # Injected -- can swap MySQL, Postgres, or a mock

    def place_order(self, order: dict):
        self._db.save(order)


# =============================================================================
# QUESTION 6 [SRP + OCP - Advanced] (God Class Refactoring)
# =============================================================================
# You are given an InvoiceManager "God class" that does everything: creates
# invoices, calculates tax, applies discounts, generates PDFs, and sends
# emails. It has 2000 lines and every change risks breaking something.
#
# (a) List every SRP violation.
# (b) Draw out the refactored class hierarchy.
# (c) How does your refactoring also satisfy OCP?
# Asked at: Google, Microsoft
# -----------------------------------------------------------------------------

class InvoiceManager_GOD_CLASS:
    """GOD CLASS -- violates SRP, OCP, and makes testing nearly impossible."""

    def create_invoice(self, customer, items):
        # ... 200 lines of invoice creation logic ...
        pass

    def calculate_tax(self, invoice, region):
        # ... tax logic for 50 different regions (if/elif chains) ...
        if region == "US":
            return invoice["total"] * 0.08
        elif region == "EU":
            return invoice["total"] * 0.20
        elif region == "UK":
            return invoice["total"] * 0.17
        # ... more regions ...

    def apply_discount(self, invoice, discount_code):
        # ... discount logic with switch cases ...
        pass

    def generate_pdf(self, invoice):
        # ... PDF generation logic ...
        pass

    def send_email(self, invoice, recipient):
        # ... Email sending logic ...
        pass


# ANSWER SKETCH:
# SRP violations: 5 distinct responsibilities crammed into one class.
#
# Refactored design:
#   - InvoiceFactory         (creates invoices)
#   - TaxCalculator (ABC)    (with RegionTax subclasses -- OCP compliant)
#   - DiscountApplier (ABC)  (with strategy per discount type -- OCP compliant)
#   - PDFGenerator           (generates PDFs)
#   - InvoiceEmailer         (sends emails)
#   - InvoiceService         (orchestrator that composes the above)
#
# OCP is satisfied because adding a new tax region = new TaxCalculator subclass
# and adding a new discount = new DiscountApplier subclass, with ZERO changes
# to existing code.


# =============================================================================
# QUESTION 7 [LSP - Advanced] (Conceptual + Tricky)
# =============================================================================
# You have a ReadOnlyCollection interface with methods: get(index), size(),
# and contains(item). You also have a MutableCollection that adds: add(item),
# remove(item). A colleague suggests MutableCollection should extend
# ReadOnlyCollection. Does this violate LSP? Why or why not?
#
# Follow-up: If a function accepts ReadOnlyCollection and you pass a
# MutableCollection, is the contract preserved? What about the other way
# around?
# Asked at: Google, Meta
# -----------------------------------------------------------------------------

# ANSWER:
# MutableCollection extending ReadOnlyCollection does NOT violate LSP, because
# a MutableCollection can do everything a ReadOnlyCollection can (get, size,
# contains) and MORE. Passing a MutableCollection where ReadOnlyCollection is
# expected preserves the contract -- the function only calls read methods.
#
# HOWEVER: ReadOnlyCollection extending MutableCollection WOULD violate LSP
# because client code expects add()/remove() to work, and ReadOnlyCollection
# would have to throw exceptions or silently fail for those methods.
#
# Key insight: LSP is about behavioral compatibility, not just structural.


# =============================================================================
# QUESTION 8 [OCP - Advanced] (Real-World Design Problem)
# =============================================================================
# Design a notification system for an e-commerce platform. Currently it
# supports Email and SMS. Tomorrow it might need Push, Slack, and Webhook.
# Show a design that is fully OCP-compliant -- adding new channels requires
# zero changes to existing code.
# Asked at: Amazon, Uber
# -----------------------------------------------------------------------------

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass


class EmailNotification(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        print(f"Email to {recipient}: {message}")
        return True


class SMSNotification(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        print(f"SMS to {recipient}: {message}")
        return True


# Adding Slack tomorrow -- ZERO changes to existing classes:
class SlackNotification(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        print(f"Slack to {recipient}: {message}")
        return True


class NotificationService:
    """Orchestrates notifications -- never modified, only extended via new channels."""

    def __init__(self, channels: list[NotificationChannel]):
        self._channels = channels

    def notify_all(self, recipient: str, message: str) -> None:
        for channel in self._channels:
            channel.send(recipient, message)


# Usage:
# svc = NotificationService([EmailNotification(), SMSNotification(), SlackNotification()])
# svc.notify_all("user@example.com", "Your order has shipped!")


# =============================================================================
# QUESTION 9 [ISP - Advanced] (Fat Interface in Real Code)
# =============================================================================
# A third-party library gives you this interface for data sources:
#
#   class DataSource(ABC):
#       def read(self) -> bytes: ...
#       def write(self, data: bytes) -> None: ...
#       def seek(self, position: int) -> None: ...
#       def close(self) -> None: ...
#       def get_metadata(self) -> dict: ...
#
# You need to implement a ReadOnlyFileSource that only reads files and a
# NetworkStreamSource that can read/write but cannot seek. How do you split
# this fat interface to satisfy ISP?
# Asked at: Google, Netflix
# -----------------------------------------------------------------------------

class Readable(ABC):
    @abstractmethod
    def read(self) -> bytes: pass


class Writable(ABC):
    @abstractmethod
    def write(self, data: bytes) -> None: pass


class Seekable(ABC):
    @abstractmethod
    def seek(self, position: int) -> None: pass


class Closable(ABC):
    @abstractmethod
    def close(self) -> None: pass


class MetadataProvider(ABC):
    @abstractmethod
    def get_metadata(self) -> dict: pass


class ReadOnlyFileSource(Readable, Seekable, Closable, MetadataProvider):
    def read(self) -> bytes: return b"file data"
    def seek(self, position: int): pass
    def close(self): pass
    def get_metadata(self) -> dict: return {"type": "file"}


class NetworkStreamSource(Readable, Writable, Closable):
    """Cannot seek -- and ISP means it does not have to pretend it can."""
    def read(self) -> bytes: return b"stream data"
    def write(self, data: bytes): pass
    def close(self): pass


# =============================================================================
# QUESTION 10 [DIP - Advanced] (Real-World Dependency Inversion)
# =============================================================================
# You are building an analytics module. Currently it logs events to a file.
# Product wants it to also support logging to Kafka, Datadog, and a custom
# HTTP endpoint. Refactor to apply DIP so the analytics module never knows
# about specific backends.
#
# Follow-up: How does DIP make this module unit-testable without actually
# connecting to Kafka or Datadog?
# Asked at: Amazon, Stripe
# -----------------------------------------------------------------------------

class AnalyticsBackend(ABC):
    @abstractmethod
    def track_event(self, event_name: str, properties: dict) -> None: pass


class FileBackend(AnalyticsBackend):
    def track_event(self, event_name: str, properties: dict):
        print(f"[File] {event_name}: {properties}")


class KafkaBackend(AnalyticsBackend):
    def track_event(self, event_name: str, properties: dict):
        print(f"[Kafka] {event_name}: {properties}")


class DatadogBackend(AnalyticsBackend):
    def track_event(self, event_name: str, properties: dict):
        print(f"[Datadog] {event_name}: {properties}")


class MockBackend(AnalyticsBackend):
    """For unit tests -- no real I/O. This is possible BECAUSE of DIP."""

    def __init__(self):
        self.events = []

    def track_event(self, event_name: str, properties: dict):
        self.events.append((event_name, properties))


class AnalyticsService:
    """High-level module depends on AnalyticsBackend abstraction, not any concretion."""

    def __init__(self, backends: list[AnalyticsBackend]):
        self._backends = backends

    def track(self, event_name: str, **properties):
        for backend in self._backends:
            backend.track_event(event_name, properties)


# =============================================================================
# QUESTION 11 [SRP - Advanced] (Microservices Context)
# =============================================================================
# You have a monolithic OrderProcessor class in a microservice that:
#   (a) Validates the order
#   (b) Checks inventory
#   (c) Processes payment
#   (d) Sends confirmation email
#   (e) Updates analytics dashboard
#
# Explain how SRP applies at the SERVICE level in a microservices
# architecture -- not just the class level. How would you decompose this
# into separate services? What communication patterns would you use?
# Asked at: Amazon, Google
# -----------------------------------------------------------------------------

# ANSWER:
# SRP at the microservice level means each service has ONE bounded context:
#
#   OrderService        -> validates and creates orders
#   InventoryService    -> checks and reserves stock
#   PaymentService      -> processes payments
#   NotificationService -> sends emails/SMS/push
#   AnalyticsService    -> tracks events and metrics
#
# Communication patterns:
#   - Synchronous (REST/gRPC) for critical path: Order -> Inventory -> Payment
#   - Asynchronous (events via Kafka/RabbitMQ) for side effects:
#     Order publishes "OrderCreated" event, NotificationService and
#     AnalyticsService subscribe. This is also OCP at the architecture level:
#     adding a new consumer requires zero changes to OrderService.


# =============================================================================
# QUESTION 12 [LSP - Advanced] (Behavioral Subtyping)
# =============================================================================
# Consider a base class `Cache` with methods get(key) and put(key, value).
# get() is documented to return None if the key doesn't exist.
#
# A subclass `StrictCache` overrides get() to throw a KeyError if the key
# doesn't exist. Does this violate LSP? Explain using the concept of
# "strengthening preconditions" vs "weakening postconditions".
# Asked at: Google, Meta
# -----------------------------------------------------------------------------

# ANSWER:
# Yes, this VIOLATES LSP.
#
# LSP rules:
#   - Preconditions cannot be STRENGTHENED in a subclass
#   - Postconditions cannot be WEAKENED in a subclass
#
# The base class Cache.get() has a postcondition: "returns None for missing keys"
# StrictCache.get() changes this to "raises KeyError for missing keys"
#
# This is a STRONGER postcondition (more restrictive -- callers expecting None
# will crash). Any code written against the Cache interface that handles None
# returns will break when given a StrictCache.
#
# Correct approach: StrictCache should be a separate type, not a subclass of
# Cache, OR Cache's contract should be defined to allow either behavior
# (but that weakens the usefulness of the contract).


# =============================================================================
# QUESTION 13 [OCP + DIP - Advanced] (Plugin Architecture)
# =============================================================================
# Design a file processing system that can handle CSV, JSON, XML, and
# Parquet files. New formats will be added over time. Show how OCP and DIP
# together enable a plugin architecture where new parsers can be added
# without modifying any existing code -- even at runtime.
# Asked at: Google, Netflix
# -----------------------------------------------------------------------------

from typing import Any


class FileParser(ABC):
    """Abstraction for DIP; extension point for OCP."""

    @abstractmethod
    def can_parse(self, filename: str) -> bool:
        pass

    @abstractmethod
    def parse(self, content: str) -> Any:
        pass


class CSVParser(FileParser):
    def can_parse(self, filename: str) -> bool:
        return filename.endswith(".csv")

    def parse(self, content: str) -> list:
        return [line.split(",") for line in content.strip().split("\n")]


class JSONParser(FileParser):
    def can_parse(self, filename: str) -> bool:
        return filename.endswith(".json")

    def parse(self, content: str) -> dict:
        import json
        return json.loads(content)


class ParserRegistry:
    """Plugin registry -- new parsers registered without touching existing code."""

    def __init__(self):
        self._parsers: list[FileParser] = []

    def register(self, parser: FileParser) -> None:
        self._parsers.append(parser)

    def get_parser(self, filename: str) -> FileParser:
        for parser in self._parsers:
            if parser.can_parse(filename):
                return parser
        raise ValueError(f"No parser found for {filename}")


class FileProcessingService:
    """Depends on abstractions (DIP). Never modified for new formats (OCP)."""

    def __init__(self, registry: ParserRegistry):
        self._registry = registry

    def process(self, filename: str, content: str) -> Any:
        parser = self._registry.get_parser(filename)
        return parser.parse(content)


# =============================================================================
# QUESTION 14 [ISP - Advanced] (API Design)
# =============================================================================
# You're designing an internal API client SDK. Some consumers only need
# read access (GET endpoints), others need write access (POST/PUT/DELETE),
# and some need admin operations (user management, config changes).
#
# A single APIClient class with all methods forces read-only consumers to
# depend on write and admin methods they never use. How do you apply ISP?
# What are the tradeoffs of having too many granular interfaces?
# Asked at: Amazon, Stripe
# -----------------------------------------------------------------------------

class ReadableAPI(ABC):
    @abstractmethod
    def get_resource(self, resource_id: str) -> dict: pass

    @abstractmethod
    def list_resources(self, filters: dict) -> list: pass


class WritableAPI(ABC):
    @abstractmethod
    def create_resource(self, data: dict) -> dict: pass

    @abstractmethod
    def update_resource(self, resource_id: str, data: dict) -> dict: pass

    @abstractmethod
    def delete_resource(self, resource_id: str) -> bool: pass


class AdminAPI(ABC):
    @abstractmethod
    def manage_users(self, action: str, user_id: str) -> dict: pass

    @abstractmethod
    def update_config(self, config: dict) -> None: pass


class FullAPIClient(ReadableAPI, WritableAPI, AdminAPI):
    """Implements everything -- only given to consumers that need everything."""
    def get_resource(self, resource_id): return {}
    def list_resources(self, filters): return []
    def create_resource(self, data): return {}
    def update_resource(self, resource_id, data): return {}
    def delete_resource(self, resource_id): return True
    def manage_users(self, action, user_id): return {}
    def update_config(self, config): pass


class ReadOnlyClient(ReadableAPI):
    """Consumer that only needs read access -- no unnecessary dependencies."""
    def get_resource(self, resource_id): return {}
    def list_resources(self, filters): return []


# TRADEOFF DISCUSSION:
# Too many micro-interfaces (e.g., one per method) leads to "interface explosion",
# making the codebase harder to navigate. The sweet spot is grouping by
# cohesive capability (read, write, admin) rather than individual operations.


# =============================================================================
# QUESTION 15 [ALL PRINCIPLES - Advanced] (Full Refactoring Challenge)
# =============================================================================
# The following class violates ALL 5 SOLID principles. Identify each
# violation and provide a complete refactored design.
# Asked at: Google (System Design Round), Amazon (LLD Round)
# -----------------------------------------------------------------------------

class ECommerceSystem_BEFORE:
    """
    VIOLATES:
    - SRP: Does ordering, payment, shipping, and notifications
    - OCP: if/elif chains for payment and shipping methods
    - LSP: (see discussion below)
    - ISP: Everything in one class forces dependents to know about all methods
    - DIP: Directly instantiates concrete dependencies
    """

    def place_order(self, items, customer):
        total = sum(item["price"] * item["qty"] for item in items)
        print(f"Order placed for {customer['name']}, total: {total}")
        return {"items": items, "customer": customer, "total": total}

    def process_payment(self, order, method):
        if method == "credit_card":
            print(f"Charging credit card for ${order['total']}")
        elif method == "paypal":
            print(f"Charging PayPal for ${order['total']}")
        elif method == "crypto":
            print(f"Charging crypto wallet for ${order['total']}")
        # Every new payment method = modify this class

    def calculate_shipping(self, order, method):
        if method == "standard":
            return 5.99
        elif method == "express":
            return 15.99
        elif method == "overnight":
            return 29.99
        # Every new shipping option = modify this class

    def send_notification(self, customer, message):
        # Hardcoded to email
        print(f"Emailing {customer['email']}: {message}")


# REFACTORED ANSWER KEY (class skeleton -- full implementation follows patterns above):
#
# 1. SRP: Split into OrderService, PaymentProcessor, ShippingCalculator,
#          NotificationService
# 2. OCP: PaymentProcessor(ABC) with subclasses per method;
#          ShippingStrategy(ABC) with subclasses per method
# 3. LSP: All subclasses of PaymentProcessor fully honor the base contract
#          (process() returns receipt or raises PaymentError, no surprises)
# 4. ISP: Separate interfaces: Orderable, Payable, Shippable, Notifiable
# 5. DIP: ECommerceService orchestrator accepts all dependencies via
#          constructor injection (abstractions, not concretions)


# =============================================================================
# QUESTION 16 [DIP - Advanced] (Testing & Mocking)
# =============================================================================
# Explain how Dependency Inversion makes unit testing possible. Given:
#
#   class ReportGenerator:
#       def __init__(self):
#           self.db = ProductionDatabase()
#           self.formatter = PDFFormatter()
#           self.sender = SMTPEmailSender()
#
# Why is this class impossible to unit test properly? Refactor it and write
# a test using mock objects.
# Asked at: Microsoft, Amazon
# -----------------------------------------------------------------------------

class ReportGenerator_UNTESTABLE:
    """VIOLATES DIP - impossible to unit test without hitting real DB/SMTP."""
    def __init__(self):
        # These are real production dependencies -- can't substitute mocks
        # self.db = ProductionDatabase()
        # self.formatter = PDFFormatter()
        # self.sender = SMTPEmailSender()
        pass

    def generate_and_send(self, report_id: int, recipient: str):
        # data = self.db.fetch(report_id)
        # pdf = self.formatter.format(data)
        # self.sender.send(recipient, pdf)
        pass


# REFACTORED:

class DataFetcher(ABC):
    @abstractmethod
    def fetch(self, report_id: int) -> dict: pass


class ReportFormatter(ABC):
    @abstractmethod
    def format(self, data: dict) -> bytes: pass


class ReportSender(ABC):
    @abstractmethod
    def send(self, recipient: str, content: bytes) -> None: pass


class ReportGenerator:
    """DIP-compliant: all dependencies are injected abstractions."""

    def __init__(self, fetcher: DataFetcher, formatter: ReportFormatter,
                 sender: ReportSender):
        self._fetcher = fetcher
        self._formatter = formatter
        self._sender = sender

    def generate_and_send(self, report_id: int, recipient: str):
        data = self._fetcher.fetch(report_id)
        content = self._formatter.format(data)
        self._sender.send(recipient, content)


# Test example:
class MockFetcher(DataFetcher):
    def fetch(self, report_id): return {"id": report_id, "data": "test"}

class MockFormatter(ReportFormatter):
    def format(self, data): return b"formatted"

class MockSender(ReportSender):
    def __init__(self):
        self.sent = []
    def send(self, recipient, content):
        self.sent.append((recipient, content))


def test_report_generator():
    sender = MockSender()
    gen = ReportGenerator(MockFetcher(), MockFormatter(), sender)
    gen.generate_and_send(42, "test@example.com")
    assert len(sender.sent) == 1
    assert sender.sent[0] == ("test@example.com", b"formatted")


# =============================================================================
# QUESTION 17 [LSP - Advanced] (Exception Contracts)
# =============================================================================
# A base class PaymentGateway has a method charge(amount) that is documented
# to raise `InsufficientFundsError` if the account balance is too low.
#
# A subclass StripeGateway overrides charge() and raises a generic
# `ConnectionError` when Stripe's API is unreachable.
#
# Does this violate LSP? Discuss the concept of "exception specification"
# in the context of LSP.
# Asked at: Stripe, Google
# -----------------------------------------------------------------------------

# ANSWER:
# It DEPENDS on how the base contract defines exceptions.
#
# If PaymentGateway documents that charge() ONLY raises InsufficientFundsError,
# then StripeGateway raising ConnectionError VIOLATES LSP because client code
# is only prepared to catch InsufficientFundsError.
#
# If PaymentGateway documents that charge() may raise PaymentError (a broader
# base exception), and both InsufficientFundsError and ConnectionError are
# subclasses of PaymentError, then it does NOT violate LSP.
#
# Key principle: A subclass should not raise exceptions that the base class
# contract does not allow. This is analogous to "postconditions cannot be
# weakened" -- unexpected exceptions are a form of weakened postcondition.
#
# Best practice: Define a clear exception hierarchy in the base class contract.


# =============================================================================
# QUESTION 18 [SRP + OCP - Advanced] (Logging System Design)
# =============================================================================
# Design a logging framework from scratch that:
#   - Supports multiple output targets (console, file, remote server)
#   - Supports multiple formats (plain text, JSON, XML)
#   - Supports log levels (DEBUG, INFO, WARN, ERROR)
#   - Is extensible for new targets and formats without modification
#
# Show the class hierarchy and how SRP and OCP guide your design.
# Asked at: Google, Amazon
# -----------------------------------------------------------------------------

from enum import Enum


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3


class LogFormatter(ABC):
    """SRP: Only responsible for formatting. OCP: new formats = new subclass."""

    @abstractmethod
    def format(self, level: LogLevel, message: str, timestamp: str) -> str:
        pass


class PlainTextFormatter(LogFormatter):
    def format(self, level, message, timestamp):
        return f"[{timestamp}] {level.name}: {message}"


class JSONFormatter(LogFormatter):
    def format(self, level, message, timestamp):
        import json
        return json.dumps({"timestamp": timestamp, "level": level.name, "message": message})


class LogTarget(ABC):
    """SRP: Only responsible for output destination. OCP: new targets = new subclass."""

    @abstractmethod
    def write(self, formatted_message: str) -> None:
        pass


class ConsoleTarget(LogTarget):
    def write(self, formatted_message: str):
        print(formatted_message)


class FileTarget(LogTarget):
    def __init__(self, filepath: str):
        self._filepath = filepath

    def write(self, formatted_message: str):
        with open(self._filepath, "a") as f:
            f.write(formatted_message + "\n")


class Logger:
    """Composes formatter and targets. DIP: depends on abstractions."""

    def __init__(self, formatter: LogFormatter, targets: list[LogTarget],
                 min_level: LogLevel = LogLevel.DEBUG):
        self._formatter = formatter
        self._targets = targets
        self._min_level = min_level

    def log(self, level: LogLevel, message: str):
        if level.value >= self._min_level.value:
            from datetime import datetime
            formatted = self._formatter.format(level, message, datetime.now().isoformat())
            for target in self._targets:
                target.write(formatted)

    def debug(self, msg): self.log(LogLevel.DEBUG, msg)
    def info(self, msg): self.log(LogLevel.INFO, msg)
    def warn(self, msg): self.log(LogLevel.WARN, msg)
    def error(self, msg): self.log(LogLevel.ERROR, msg)


# =============================================================================
# QUESTION 19 [LSP + ISP - Advanced] (Collections Framework)
# =============================================================================
# Java's List interface includes an add() method. Collections.unmodifiableList()
# returns a List that throws UnsupportedOperationException on add().
#
# (a) Explain why this violates LSP.
# (b) Explain why it also violates ISP.
# (c) How would you redesign this to satisfy both LSP and ISP?
# (d) Why do you think Java chose this design despite the violation?
# Asked at: Google, Amazon
# -----------------------------------------------------------------------------

# ANSWER:
#
# (a) LSP Violation: Client code written against List expects add() to work.
#     unmodifiableList() breaks this expectation by throwing an exception.
#     A subtype is NOT substitutable for the base type.
#
# (b) ISP Violation: The List interface forces all implementations to expose
#     add(), remove(), set() even if the implementation is read-only. Clients
#     that only read are forced to depend on mutation methods they don't use.
#
# (c) Correct design:
#     - ReadableList (get, size, contains, iterator)
#     - MutableList extends ReadableList (add, remove, set)
#     - UnmodifiableList implements ReadableList only
#     Now UnmodifiableList never needs to throw UnsupportedOperationException.
#
# (d) Java chose this for backwards compatibility. The Collections framework
#     was designed before generics and before SOLID was widely understood.
#     Splitting the interface would break millions of lines of existing code.
#     This is a pragmatic tradeoff: LSP purity vs. ecosystem stability.


# =============================================================================
# QUESTION 20 [ALL PRINCIPLES - Advanced] (Ride-Sharing System)
# =============================================================================
# Design a simplified ride-sharing system (like Uber/Lyft) applying all
# SOLID principles. The system must:
#   - Support different vehicle types (car, bike, auto-rickshaw)
#   - Support different pricing strategies (surge, flat, distance-based)
#   - Support different payment methods (card, wallet, cash)
#   - Send ride status notifications
#
# Show the key classes/interfaces and explain which SOLID principle each
# design decision satisfies.
# Asked at: Uber, Google, Amazon (LLD round)
# -----------------------------------------------------------------------------

# --- SRP: Each class has one responsibility ---

class Ride:
    """Data model for a ride."""
    def __init__(self, rider, driver, vehicle, origin, destination):
        self.rider = rider
        self.driver = driver
        self.vehicle = vehicle
        self.origin = origin
        self.destination = destination
        self.distance = 0.0
        self.status = "requested"


# --- OCP: New vehicle/pricing/payment types = new subclass, no modification ---

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, ride: Ride) -> float: pass


class DistanceBasedPricing(PricingStrategy):
    def __init__(self, rate_per_km: float):
        self._rate = rate_per_km
    def calculate_fare(self, ride: Ride) -> float:
        return ride.distance * self._rate


class SurgePricing(PricingStrategy):
    def __init__(self, base_strategy: PricingStrategy, multiplier: float):
        self._base = base_strategy
        self._multiplier = multiplier
    def calculate_fare(self, ride: Ride) -> float:
        return self._base.calculate_fare(ride) * self._multiplier


# --- LSP: All PaymentMethod subclasses honor the contract ---

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool: pass


class CardPayment(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"Charged ${amount} to card")
        return True


class WalletPayment(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"Deducted ${amount} from wallet")
        return True


class CashPayment(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"Collect ${amount} in cash")
        return True


# --- ISP: Separate interfaces for different capabilities ---

class RideRequestable(ABC):
    @abstractmethod
    def request_ride(self, rider, origin, destination) -> Ride: pass


class RideTrackable(ABC):
    @abstractmethod
    def track_ride(self, ride_id: str) -> dict: pass


class RideCompletable(ABC):
    @abstractmethod
    def complete_ride(self, ride_id: str) -> float: pass


# --- DIP: High-level RideService depends on abstractions ---

class RideService(RideRequestable, RideTrackable, RideCompletable):
    def __init__(self, pricing: PricingStrategy, payment: PaymentMethod,
                 notifier: NotificationChannel):
        self._pricing = pricing
        self._payment = payment
        self._notifier = notifier

    def request_ride(self, rider, origin, destination) -> Ride:
        ride = Ride(rider, driver=None, vehicle=None,
                    origin=origin, destination=destination)
        self._notifier.send(rider, "Ride requested! Finding a driver...")
        return ride

    def track_ride(self, ride_id: str) -> dict:
        return {"ride_id": ride_id, "status": "in_progress"}

    def complete_ride(self, ride_id: str) -> float:
        ride = Ride("rider", "driver", "car", "A", "B")
        ride.distance = 10.0
        fare = self._pricing.calculate_fare(ride)
        self._payment.pay(fare)
        self._notifier.send("rider", f"Ride complete! Fare: ${fare}")
        return fare


# =============================================================================
# QUESTION 21 [OCP + Strategy Pattern - Advanced]
# =============================================================================
# You have a data validation pipeline for user input. Currently it checks:
# email format, password strength, and age range. Show how to design this
# so new validation rules (e.g., phone number format, address verification)
# can be added without modifying the pipeline.
# Asked at: Google, Microsoft
# -----------------------------------------------------------------------------

class ValidationRule(ABC):
    @abstractmethod
    def validate(self, data: dict) -> list[str]:
        """Returns list of error messages. Empty list = valid."""
        pass


class EmailFormatRule(ValidationRule):
    def validate(self, data: dict) -> list[str]:
        email = data.get("email", "")
        if "@" not in email or "." not in email:
            return ["Invalid email format"]
        return []


class PasswordStrengthRule(ValidationRule):
    def validate(self, data: dict) -> list[str]:
        password = data.get("password", "")
        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")
        if not any(c.isupper() for c in password):
            errors.append("Password must contain an uppercase letter")
        if not any(c.isdigit() for c in password):
            errors.append("Password must contain a digit")
        return errors


class AgeRangeRule(ValidationRule):
    def validate(self, data: dict) -> list[str]:
        age = data.get("age", 0)
        if age < 18 or age > 120:
            return [f"Age {age} is out of valid range (18-120)"]
        return []


class ValidationPipeline:
    """OCP: add new rules without touching this class."""

    def __init__(self, rules: list[ValidationRule]):
        self._rules = rules

    def add_rule(self, rule: ValidationRule):
        self._rules.append(rule)

    def validate(self, data: dict) -> list[str]:
        errors = []
        for rule in self._rules:
            errors.extend(rule.validate(data))
        return errors


# =============================================================================
# QUESTION 22 [SRP - Advanced] (When NOT to Split)
# =============================================================================
# A colleague argues that a UserProfile class with methods getName(),
# getEmail(), getAddress(), and getPhone() violates SRP because it manages
# multiple pieces of data. Do you agree? When does splitting go too far?
# What is the correct way to identify "reasons to change"?
# Asked at: Google, Meta
# -----------------------------------------------------------------------------

# ANSWER:
# The colleague is WRONG. A UserProfile class that manages a user's personal
# data has ONE reason to change: the structure of user profile data changes.
#
# SRP does NOT mean "a class should do only one thing." It means "a class
# should have only one REASON TO CHANGE" -- i.e., one actor or stakeholder
# whose requirements drive modifications.
#
# getName(), getEmail(), etc. are all cohesive -- they all relate to the same
# concept (user profile data) and would change for the same reason (e.g.,
# "we need to add a middle name field").
#
# Splitting too far leads to:
#   - Class explosion (hundreds of tiny classes)
#   - Increased complexity in understanding the codebase
#   - More indirection for no real benefit
#
# The correct test: "If requirement X changes, does the class need to change?
# If requirement Y changes, does the SAME class need to change? If X and Y
# come from DIFFERENT stakeholders/actors, the class has too many responsibilities."


# =============================================================================
# QUESTION 23 [OCP - Advanced] (Decorator Pattern)
# =============================================================================
# Show how the Decorator pattern enables OCP compliance in a coffee shop
# ordering system. A coffee can have milk, sugar, whipped cream, and any
# combination. Adding new toppings should never require modifying existing
# classes. Compare this to an if/elif approach.
# Asked at: Amazon, Microsoft
# -----------------------------------------------------------------------------

class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float: pass

    @abstractmethod
    def description(self) -> str: pass


class Coffee(Beverage):
    def cost(self) -> float: return 2.00
    def description(self) -> str: return "Coffee"


class Tea(Beverage):
    def cost(self) -> float: return 1.50
    def description(self) -> str: return "Tea"


class BeverageDecorator(Beverage):
    """Base decorator -- subclasses add behavior without modifying originals."""

    def __init__(self, beverage: Beverage):
        self._beverage = beverage


class MilkDecorator(BeverageDecorator):
    def cost(self) -> float: return self._beverage.cost() + 0.50
    def description(self) -> str: return self._beverage.description() + " + Milk"


class SugarDecorator(BeverageDecorator):
    def cost(self) -> float: return self._beverage.cost() + 0.25
    def description(self) -> str: return self._beverage.description() + " + Sugar"


class WhipDecorator(BeverageDecorator):
    def cost(self) -> float: return self._beverage.cost() + 0.75
    def description(self) -> str: return self._beverage.description() + " + Whip"


# Usage -- composable, OCP-compliant:
# order = WhipDecorator(MilkDecorator(Coffee()))
# print(order.description())  # "Coffee + Milk + Whip"
# print(order.cost())         # 3.25

# Adding caramel topping = new class, ZERO changes to existing code:
class CaramelDecorator(BeverageDecorator):
    def cost(self) -> float: return self._beverage.cost() + 0.60
    def description(self) -> str: return self._beverage.description() + " + Caramel"


# =============================================================================
# QUESTION 24 [DIP - Advanced] (Framework vs Library)
# =============================================================================
# Explain the relationship between Dependency Inversion Principle and the
# "Hollywood Principle" ("Don't call us, we'll call you"). How does DIP
# manifest in:
#   (a) A web framework like Django/Flask (framework calls your code)
#   (b) Dependency Injection containers (Spring, Guice, etc.)
#   (c) Event-driven architectures (pub/sub, observer pattern)
#
# Give a concrete Python example showing how a framework inverts control.
# Asked at: Google, Netflix
# -----------------------------------------------------------------------------

# ANSWER:
#
# DIP and the Hollywood Principle are closely related:
# - DIP says: depend on abstractions, not concretions
# - Hollywood Principle says: the framework calls your code, not the other way
#
# (a) Django/Flask: You define view functions/classes conforming to the
#     framework's interface. The framework calls YOUR code when a request
#     arrives. You never call the framework's HTTP handling directly.
#
# (b) DI Containers: Instead of your class creating its dependencies (new),
#     the container injects them. Your class declares WHAT it needs
#     (abstractions), not HOW to create them.
#
# (c) Event-driven: Publishers don't know about subscribers. Both depend on
#     the event bus abstraction. Adding a new subscriber requires zero
#     changes to the publisher.

class EventBus:
    """Concrete example of DIP in event-driven architecture."""

    def __init__(self):
        self._subscribers: dict[str, list] = {}

    def subscribe(self, event_type: str, handler):
        self._subscribers.setdefault(event_type, []).append(handler)

    def publish(self, event_type: str, data: dict):
        for handler in self._subscribers.get(event_type, []):
            handler(data)  # Framework calls YOUR code (Hollywood Principle)


# Publisher knows nothing about subscribers:
# bus = EventBus()
# bus.subscribe("order_placed", lambda data: print(f"Email: {data}"))
# bus.subscribe("order_placed", lambda data: print(f"Analytics: {data}"))
# bus.publish("order_placed", {"order_id": 123})


# =============================================================================
# QUESTION 25 [ALL PRINCIPLES - Advanced] (Code Review Scenario)
# =============================================================================
# You're reviewing a PR that adds a new feature to an existing payment
# processing system. The developer added this class. Identify ALL SOLID
# violations and write review comments for each.
# Asked at: Google, Amazon, Meta (Code Review rounds)
# -----------------------------------------------------------------------------

class PaymentProcessor_REVIEW:
    """
    PR Code to Review -- find ALL violations.
    """

    def __init__(self):
        # DIP VIOLATION: hardcoded concrete dependencies
        # self.stripe = StripeAPI()
        # self.logger = FileLogger("/var/log/payments.log")
        # self.emailer = SMTPClient("smtp.company.com")
        pass

    def process(self, order: dict, payment_type: str):
        # OCP VIOLATION: if/elif chain -- must modify for new payment types
        if payment_type == "stripe":
            self._charge_stripe(order)
        elif payment_type == "paypal":
            self._charge_paypal(order)

        # SRP VIOLATION: payment processing + logging + emailing in one class
        # self.logger.log(f"Processed {payment_type} for order {order['id']}")
        # self.emailer.send(order["customer_email"], "Payment received!")

    def _charge_stripe(self, order):
        # ISP VIOLATION: method uses only charge() from Stripe but class
        # depends on entire Stripe API with refund(), subscription(), etc.
        pass

    def _charge_paypal(self, order):
        pass

    def generate_report(self, start_date, end_date):
        # SRP VIOLATION: reporting has nothing to do with payment processing
        pass


# REVIEW COMMENTS:
#
# 1. [DIP] __init__ creates concrete dependencies. Inject abstractions instead.
# 2. [OCP] process() uses if/elif -- use strategy pattern for payment types.
# 3. [SRP] This class processes payments, logs, emails, AND generates reports.
#    Split into PaymentProcessor, PaymentLogger, PaymentNotifier, ReportGenerator.
# 4. [ISP] Depending on full StripeAPI when only charge() is needed. Define a
#    Chargeable interface with just charge().
# 5. [LSP] Not directly violated here, but the if/elif pattern prevents
#    polymorphic substitution which would guarantee LSP compliance.


# =============================================================================
# QUESTION 26 [SRP + DIP - Advanced] (Event Sourcing & CQRS Context)
# =============================================================================
# In an event-sourced system, commands (writes) and queries (reads) are
# separated. Explain how this architecture naturally enforces SRP and DIP.
# Why is this separation more robust than a single service handling both
# reads and writes?
# Asked at: Amazon, Google
# -----------------------------------------------------------------------------

# ANSWER:
#
# CQRS (Command Query Responsibility Segregation) is SRP at the architectural level:
#
# - Command Side (writes): Has ONE reason to change -- business logic for
#   state mutations. Classes: CommandHandler, EventStore, Aggregate.
#
# - Query Side (reads): Has ONE reason to change -- how data is read and
#   projected for consumers. Classes: QueryHandler, ReadModel, Projections.
#
# DIP is enforced because:
# - CommandHandlers depend on abstract Repository/EventStore interfaces
# - QueryHandlers depend on abstract ReadModel interfaces
# - Neither side depends on concrete database implementations
#
# Benefits over a single service:
# - Read and write models can be optimized independently
# - Scaling: reads (typically 90%+ of traffic) scale separately from writes
# - Testing: command handlers tested without read infrastructure and vice versa
# - A change in how reports are displayed (query side) cannot accidentally
#   break order processing (command side)


# =============================================================================
# SUMMARY: ALL 26 QUESTIONS AT A GLANCE
# =============================================================================
"""
 #  | Principle(s)     | Level    | Type            | Key Topic
----|------------------|----------|-----------------|----------------------------------
 1  | SRP              | Mid      | Code Refactor   | User registration God method
 2  | OCP              | Mid      | Code Refactor   | Discount calculator if/elif
 3  | LSP              | Advanced | Classic Problem  | Rectangle-Square
 4  | ISP              | Mid      | Code Refactor   | Worker interface (human vs robot)
 5  | DIP              | Mid      | Code Refactor   | Database coupling
 6  | SRP + OCP        | Advanced | God Class        | InvoiceManager decomposition
 7  | LSP              | Advanced | Conceptual       | ReadOnly vs Mutable collections
 8  | OCP              | Advanced | System Design    | Notification system
 9  | ISP              | Advanced | Interface Design  | Data source fat interface
10  | DIP              | Advanced | System Design    | Analytics multi-backend
11  | SRP              | Advanced | Architecture     | Microservices decomposition
12  | LSP              | Advanced | Conceptual       | Cache behavioral subtyping
13  | OCP + DIP        | Advanced | System Design    | Plugin file parser architecture
14  | ISP              | Advanced | API Design       | SDK client interface segregation
15  | ALL              | Advanced | Full Refactor    | E-commerce system rewrite
16  | DIP              | Advanced | Testing          | Mock objects and testability
17  | LSP              | Advanced | Conceptual       | Exception contracts
18  | SRP + OCP        | Advanced | System Design    | Logging framework
19  | LSP + ISP        | Advanced | Conceptual       | Java Collections design flaw
20  | ALL              | Advanced | System Design    | Ride-sharing (Uber) LLD
21  | OCP              | Advanced | Design Pattern   | Validation pipeline
22  | SRP              | Advanced | Conceptual       | When NOT to split (over-engineering)
23  | OCP              | Advanced | Design Pattern   | Decorator pattern (coffee shop)
24  | DIP              | Advanced | Conceptual       | Hollywood Principle & frameworks
25  | ALL              | Advanced | Code Review      | PR review scenario
26  | SRP + DIP        | Advanced | Architecture     | CQRS / Event Sourcing
"""
