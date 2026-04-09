"""
PROBLEM: Retry Decorator with Exponential Backoff
Closures/HOF/Decorators Q16

Build a @retry(max_attempts, delay, backoff) decorator that:
- Retries a function up to max_attempts times if it raises an exception
- Waits with exponential backoff: delay, delay*backoff, delay*backoff^2, ...
- If all attempts fail, re-raises the LAST exception
- Preserves function metadata (functools.wraps)
- Prints attempt info for visibility

DIFFICULTY: Advanced
TIME LIMIT: 12 minutes
STARTED: 5:03 PM, Apr 6, 2026
COMPLETED: 5:21 PM, Apr 6, 2026
ATTEMPT: 4
"""

from functools import wraps
# ============================================================
# YOUR SOLUTION BELOW
# ============================================================
def retry(max_attempts, delay, backoff):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **Kwargs):
            attempt = 1
            nonlocal delay 
            while(attempt <= max_attempts):
                try:
                    result = func(*args, **Kwargs)
                    return result
                except Exception as e:
                    if attempt == max_attempts:
                        raise # re-raise the same exception
                    else:
                        time.sleep(delay)
                        delay = delay*backoff
                        attempt += 1
        return wrapper
    return decorator




# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================
import time

# --- Test 1: Succeeds on first try (no retries needed) ---
call_log = []

@retry(max_attempts=3, delay=0.1, backoff=2)
def always_works():
    """A reliable function."""
    call_log.append("called")
    return "success"

result = always_works()
assert result == "success", f"Expected 'success', got {result}"
assert len(call_log) == 1, f"Should be called once, was called {len(call_log)} times"
print("Test 1 PASSED: Succeeds on first try")

# --- Test 2: Fails then succeeds (retries work) ---
attempt_counter = {"count": 0}

@retry(max_attempts=4, delay=0.1, backoff=2)
def fails_twice_then_works():
    attempt_counter["count"] += 1
    if attempt_counter["count"] <= 2:
        raise ConnectionError(f"Fail #{attempt_counter['count']}")
    return "recovered"

result = fails_twice_then_works()
assert result == "recovered", f"Expected 'recovered', got {result}"
assert attempt_counter["count"] == 3, f"Should take 3 attempts, took {attempt_counter['count']}"
print("Test 2 PASSED: Fails twice then succeeds on 3rd attempt")

# --- Test 3: All attempts fail — exception re-raised ---
fail_count = {"count": 0}

@retry(max_attempts=3, delay=0.05, backoff=2)
def always_fails():
    fail_count["count"] += 1
    raise ValueError(f"Permanent failure #{fail_count['count']}")

try:
    always_fails()
    assert False, "Should have raised ValueError"
except ValueError as e:
    assert "Permanent failure #3" in str(e), f"Should re-raise LAST exception, got: {e}"
    assert fail_count["count"] == 3, f"Should try 3 times, tried {fail_count['count']}"
print("Test 3 PASSED: Re-raises last exception after all attempts fail")

# --- Test 4: Exponential backoff timing ---
@retry(max_attempts=4, delay=0.1, backoff=2)
def timed_failure():
    raise RuntimeError("fail")

start = time.time()
try:
    timed_failure()
except RuntimeError:
    elapsed = time.time() - start

# Expected delays: 0.1 + 0.2 + 0.4 = 0.7 seconds (3 sleeps before 4th attempt fails)
# Allow some tolerance
assert 0.5 < elapsed < 1.2, f"Backoff timing off: {elapsed:.2f}s (expected ~0.7s)"
print(f"Test 4 PASSED: Exponential backoff timing correct ({elapsed:.2f}s)")

# --- Test 5: functools.wraps preserves metadata ---
assert always_works.__name__ == "always_works", f"Name not preserved: {always_works.__name__}"
assert always_works.__doc__ == "A reliable function.", f"Doc not preserved: {always_works.__doc__}"
print("Test 5 PASSED: functools.wraps preserves metadata")

# --- Test 6: Function arguments forwarded correctly ---
@retry(max_attempts=2, delay=0.05, backoff=2)
def add(a, b, extra=0):
    return a + b + extra

assert add(3, 4) == 7, "Positional args not forwarded"
assert add(3, 4, extra=10) == 17, "Keyword args not forwarded"
print("Test 6 PASSED: Arguments forwarded correctly")

# --- Test 7: Different exception types caught ---
toggle = {"val": True}

@retry(max_attempts=2, delay=0.05, backoff=2)
def mixed_exceptions():
    if toggle["val"]:
        toggle["val"] = False
        raise TypeError("type error")
    return "ok"

assert mixed_exceptions() == "ok"
print("Test 7 PASSED: Different exception types handled")

# --- Test 8: max_attempts=1 means no retries ---
single_count = {"count": 0}

@retry(max_attempts=1, delay=0.1, backoff=2)
def one_shot():
    single_count["count"] += 1
    raise RuntimeError("one and done")

try:
    one_shot()
except RuntimeError:
    assert single_count["count"] == 1, f"max_attempts=1 should call once, called {single_count['count']}"
print("Test 8 PASSED: max_attempts=1 means single attempt, no retries")

print("\n=== ALL 8 TESTS PASSED ===")
