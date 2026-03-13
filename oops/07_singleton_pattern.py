"""
================================================================================
EXERCISE 07 — Singleton Pattern
================================================================================
Implement a thread-safe Singleton.

YOUR TASK:
1. Create a class `DatabaseConnection` that is a Singleton
2. Override `__new__` to ensure only ONE instance ever exists
3. It should have an `__init__` that takes `connection_string` (str)
4. Method `query(sql: str)` -> returns f"[{connection_string}] Executing: {sql}"
5. Make it thread-safe using threading.Lock

IMPORTANT:
- Multiple calls to DatabaseConnection("...") must return the SAME object
- __init__ should only set connection_string ONCE (first time)
- Two threads creating instances simultaneously must still get the same object

Run this file to test:  python 07_singleton_pattern.py
================================================================================
"""
import threading

# ── YOUR CODE BELOW ──────────────────────────────────────────────────────────
class DatabaseConnection:
    _instance  = None
    _lock = threading.Lock()
    def __new__(cls, *args, **kwrgs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
    
    def __init__(self, connection_string:str):
        if not hasattr(self, 'connection_string'):
            self.connection_string = connection_string    
    def query(self, sql: str):
        return f"[{self.connection_string}] Executing: {sql}"



# ── YOUR CODE ABOVE ──────────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════════════════════════════
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════════════

def run_tests():
    passed = 0
    failed = 0

    # Reset singleton between test runs (for re-running)
    DatabaseConnection._instance = None

    # Test 1: Basic creation
    try:
        db1 = DatabaseConnection("postgres://localhost:5432")
        assert db1 is not None
        print("  [PASS] Test 1: Singleton created successfully")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 1: Creation — {e}")
        failed += 1

    # Test 2: Same instance
    try:
        db1 = DatabaseConnection("postgres://localhost:5432")
        db2 = DatabaseConnection("mysql://localhost:3306")
        assert db1 is db2, f"db1 and db2 should be the SAME object! id(db1)={id(db1)}, id(db2)={id(db2)}"
        print("  [PASS] Test 2: Same instance returned (db1 is db2)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 2: Same instance — {e}")
        failed += 1

    # Test 3: First connection string wins
    try:
        db1 = DatabaseConnection("postgres://localhost:5432")
        db2 = DatabaseConnection("mysql://localhost:3306")
        assert db1.connection_string == "postgres://localhost:5432", \
            f"Expected postgres but got {db1.connection_string}"
        print("  [PASS] Test 3: First connection string preserved")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 3: Connection string — {e}")
        failed += 1

    # Test 4: Query works
    try:
        db = DatabaseConnection("postgres://localhost:5432")
        result = db.query("SELECT * FROM users")
        expected = "[postgres://localhost:5432] Executing: SELECT * FROM users"
        assert result == expected, f"Expected '{expected}' but got '{result}'"
        print("  [PASS] Test 4: Query returns correct format")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 4: Query — {e}")
        failed += 1

    # Test 5: Has a lock (thread-safety check)
    try:
        assert hasattr(DatabaseConnection, '_lock'), "Must have a _lock class attribute"
        assert isinstance(DatabaseConnection._lock, type(threading.Lock())), \
            "_lock must be a threading.Lock"
        print("  [PASS] Test 5: Thread-safe lock exists")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 5: Thread safety — {e}")
        failed += 1

    # Test 6: Thread-safety — multiple threads get same instance
    try:
        DatabaseConnection._instance = None  # reset
        results = []

        def create_instance(conn_str):
            inst = DatabaseConnection(conn_str)
            results.append(id(inst))

        threads = [
            threading.Thread(target=create_instance, args=(f"db_{i}",))
            for i in range(10)
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert len(set(results)) == 1, \
            f"All threads should get same instance! Got {len(set(results))} different instances"
        print("  [PASS] Test 6: 10 threads all got the same instance")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 6: Thread safety — {e}")
        failed += 1

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{passed+failed} tests passed")
    if failed == 0:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
