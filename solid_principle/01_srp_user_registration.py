"""
================================================================================
EXERCISE 01 — SRP: User Registration Refactor
================================================================================
SCENARIO:
You're a senior dev reviewing a PR. The intern wrote a single method that does
EVERYTHING for user registration. Your job: split it into clean, single-
responsibility classes.

YOUR TASK:
Read the tests below. They tell you EXACTLY what classes and methods are needed.
Figure out the design yourself. No skeleton code this time.

HINTS (read only if stuck):
- The tests import specific class names — read them carefully
- Each class has one clear job
- One class orchestrates the others (but doesn't DO their work)

SCORING:
- Correctness: /4  |  Attempts: /3  |  Hints: /2  |  Code quality: /1
- Time limit: 8 minutes (tracked, not scored — for your own progress reference)

STARTED: 2026-03-13 18:58 IST (reset after meeting break)
ATTEMPT: 1

Run:  python 01_srp_user_registration.py
================================================================================
"""
from typing import List
# ── YOUR CODE BELOW ──────────────────────────────────────────────────────────
class UserValidator:
    def validate(self, name:str, email:str)->bool:
        if name and email and "@" in email:  
            return True
        return False

class UserRepository:
    def __init__(self):
        self.users = []
    
    def save(self, name:str, email:str):
        self.users.append({"name":name, "email":email})

    def get_all(self)->List:
        return self.users

class EmailService:
    def send_welcome(self, email:str, name:str)->str:
        return f"Email sent to {email}: Welcome, {name}!"

class EventLogger:
    def __init__(self):
        self.logs = []
    
    def log(self, msg:str):
        self.logs.append(msg)

    def get_logs(self):
        return self.logs
    
class RegistrationService:
    def __init__(self, validate: UserValidator, repo: UserRepository, email_svc: EmailService, logger: EventLogger):
        self.validator = validate
        self.repo = repo
        self.email_svc = email_svc
        self.logger = logger

    def register(self, name: str, email: str)->bool:
        is_validated = self.validator.validate(name, email)
        if is_validated:
            self.repo.save(name, email)
            result = self.email_svc.send_welcome(email, name)
            self.logger.log(f"User created: {name}")
            self.logger.log(result)
            return True        
        return is_validated


# ── YOUR CODE ABOVE ──────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    # Test 1: UserValidator validates correctly
    try:
        validator = UserValidator()
        assert validator.validate("Alice", "alice@test.com") == True
        print("  [PASS] Test 1: Valid user passes validation")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1: Valid user — {e}")
        failed += 1

    # Test 2: UserValidator rejects empty name
    try:
        validator = UserValidator()
        assert validator.validate("", "alice@test.com") == False
        print("  [PASS] Test 2: Empty name rejected")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2: Empty name — {e}")
        failed += 1

    # Test 3: UserValidator rejects invalid email (no @)
    try:
        validator = UserValidator()
        assert validator.validate("Alice", "alicetest.com") == False
        print("  [PASS] Test 3: Invalid email rejected (no @)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3: Invalid email — {e}")
        failed += 1

    # Test 4: UserRepository saves and retrieves user
    try:
        repo = UserRepository()
        repo.save("Alice", "alice@test.com")
        users = repo.get_all()
        assert len(users) == 1
        assert users[0] == {"name": "Alice", "email": "alice@test.com"}
        print("  [PASS] Test 4: User saved and retrieved")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4: Save/retrieve — {e}")
        failed += 1

    # Test 5: UserRepository stores multiple users
    try:
        repo = UserRepository()
        repo.save("Alice", "alice@test.com")
        repo.save("Bob", "bob@test.com")
        assert len(repo.get_all()) == 2
        print("  [PASS] Test 5: Multiple users stored")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5: Multiple users — {e}")
        failed += 1

    # Test 6: EmailService sends welcome email
    try:
        email_svc = EmailService()
        result = email_svc.send_welcome("alice@test.com", "Alice")
        assert result == "Email sent to alice@test.com: Welcome, Alice!"
        print("  [PASS] Test 6: Welcome email sent")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 6: Welcome email — {e}")
        failed += 1

    # Test 7: EventLogger logs events
    try:
        logger = EventLogger()
        logger.log("User created: Alice")
        logger.log("Email sent to alice@test.com")
        logs = logger.get_logs()
        assert len(logs) == 2
        assert "User created: Alice" in logs[0]
        assert "Email sent" in logs[1]
        print("  [PASS] Test 7: Events logged correctly")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 7: Event logging — {e}")
        failed += 1

    # Test 8: RegistrationService orchestrates everything (happy path)
    try:
        validator = UserValidator()
        repo = UserRepository()
        email_svc = EmailService()
        logger = EventLogger()
        service = RegistrationService(validator, repo, email_svc, logger)
        result = service.register("Alice", "alice@test.com")
        assert result == True
        assert len(repo.get_all()) == 1
        assert len(logger.get_logs()) >= 1
        print("  [PASS] Test 8: Full registration succeeds")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 8: Full registration — {e}")
        failed += 1

    # Test 9: RegistrationService rejects invalid input
    try:
        validator = UserValidator()
        repo = UserRepository()
        email_svc = EmailService()
        logger = EventLogger()
        service = RegistrationService(validator, repo, email_svc, logger)
        result = service.register("", "bad-email")
        assert result == False
        assert len(repo.get_all()) == 0  # nothing saved
        print("  [PASS] Test 9: Invalid registration rejected, nothing saved")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 9: Invalid registration — {e}")
        failed += 1

    # Test 10: RegistrationService uses injected dependencies (DI check)
    try:
        validator = UserValidator()
        repo = UserRepository()
        email_svc = EmailService()
        logger = EventLogger()
        service = RegistrationService(validator, repo, email_svc, logger)
        service.register("Bob", "bob@test.com")
        # The SAME repo object should have the user
        assert repo.get_all()[0]["name"] == "Bob"
        print("  [PASS] Test 10: Service uses injected repo (not internal copy)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 10: DI check — {e}")
        failed += 1

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{passed+failed} tests passed")
    if failed == 0:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
