"""
PROBLEM: Memoize Decorator
Closures/HOF/Decorators Q17

Build a @memoize decorator that caches function results.
- Must handle falsy cached values correctly (0, False, [], '')
- Cache key = function arguments (positional)
- Preserve function metadata with functools.wraps
- Bonus: expose cache for inspection via func.cache attribute

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 5:24 PM, Apr 6, 2026
COMPLETED: 5:33 PM, Apr 6, 2026
ATTEMPT: 2
"""
from functools import wraps
# ============================================================
# YOUR SOLUTION BELOW
# ============================================================
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key in cache:
            wrapper.cache = cache
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            wrapper.cache = cache # bcz in python funtion are also obje first class obj
            return result
    return wrapper



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

# --- Test 1: Basic caching works ---
call_count = {"fib": 0}

@memoize
def fibonacci(n):
    """Computes nth Fibonacci number."""
    call_count["fib"] += 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

assert fibonacci(10) == 55
print(f"Test 1 PASSED: fibonacci(10) = 55 (called {call_count['fib']} times)")

# --- Test 2: Cache actually prevents recomputation ---
assert call_count["fib"] == 11, f"Should call fib 11 times (0-10), called {call_count['fib']}"
# Call again — should NOT increase count
fibonacci(10)
fibonacci(5)
assert call_count["fib"] == 11, f"Cached calls should not recompute, count is {call_count['fib']}"
print("Test 2 PASSED: Cached results prevent recomputation")

# --- Test 3: Falsy values cached correctly (the bug from Session 13!) ---
zero_calls = {"count": 0}

@memoize
def returns_zero(x):
    zero_calls["count"] += 1
    return 0

assert returns_zero(5) == 0
assert returns_zero(5) == 0  # should use cache, NOT recompute
assert zero_calls["count"] == 1, f"Should call once, called {zero_calls['count']}"
print("Test 3 PASSED: Falsy value (0) cached correctly")

# --- Test 4: False cached correctly ---
false_calls = {"count": 0}

@memoize
def returns_false(x):
    false_calls["count"] += 1
    return False

assert returns_false(1) == False
assert returns_false(1) == False
assert false_calls["count"] == 1, f"Should call once, called {false_calls['count']}"
print("Test 4 PASSED: Falsy value (False) cached correctly")

# --- Test 5: Empty string cached correctly ---
empty_calls = {"count": 0}

@memoize
def returns_empty(x):
    empty_calls["count"] += 1
    return ""

assert returns_empty(1) == ""
assert returns_empty(1) == ""
assert empty_calls["count"] == 1, f"Should call once, called {empty_calls['count']}"
print("Test 5 PASSED: Falsy value ('') cached correctly")

# --- Test 6: Multiple arguments as cache key ---
multi_calls = {"count": 0}

@memoize
def add(a, b):
    multi_calls["count"] += 1
    return a + b

assert add(2, 3) == 5
assert add(2, 3) == 5  # cached
assert add(3, 2) == 5  # different key! should recompute
assert multi_calls["count"] == 2, f"Different arg order = different key, count: {multi_calls['count']}"
print("Test 6 PASSED: Multiple arguments form correct cache key")

# --- Test 7: functools.wraps preserves metadata ---
assert fibonacci.__name__ == "fibonacci", f"Name not preserved: {fibonacci.__name__}"
assert fibonacci.__doc__ == "Computes nth Fibonacci number.", f"Doc not preserved"
print("Test 7 PASSED: Metadata preserved")

# --- Test 8: Cache accessible via .cache attribute ---
@memoize
def square(x):
    return x * x

square(4)
square(5)
assert hasattr(square, 'cache'), "Decorated function should have .cache attribute"
assert square.cache[(4,)] == 16, f"Cache should contain (4,) -> 16"
assert square.cache[(5,)] == 25, f"Cache should contain (5,) -> 25"
print("Test 8 PASSED: Cache exposed via .cache attribute")

print("\n=== ALL 8 TESTS PASSED ===")
