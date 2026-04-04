"""
EXERCISE: Build a @cache decorator with proper metadata preservation

Create a decorator that caches function results based on arguments.
The decorator MUST preserve the original function's metadata.

Requirements:
1. Cache results in a dictionary (args tuple as key)
2. Return cached result if arguments seen before
3. Use functools.wraps to preserve metadata
4. Works with any function signature (*args, **kwargs)

Example:
    @cache
    def expensive_calculation(n):
        '''Calculates fibonacci number'''
        # expensive computation
        return result

    expensive_calculation.__name__  # Should be "expensive_calculation"
    expensive_calculation.__doc__   # Should be "Calculates fibonacci number"

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
HINT: You get ONE free hint if stuck (this is new pattern)
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the decorator need to do?) it need to cache the result and return result if same key found
# 2. HOW: (step-by-step - how will you build this?) i will first create a cache decorator with wraps functool as nternal wrapper then inside i will check if arg is already in the hashmap i will return that else i will cache it 
# 3. EDGE CASES: (what could go wrong?) if key is unique each time, or cache takes cinsumes to much memory or someone thinder attacl
# 4. COMPLEXITY: (time and space for cache hit vs miss) are u fool how can we cal its time compelxity
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================

# TODO: Import what you need here
from functools import wraps

def cache(func):
    cache_mem = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if cache_mem.get(key, None):
            return cache_mem.get(key)
        result = func(*args, **kwargs)
        cache_mem[key] = result
        return result
    return wrapper
            



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    # Track call counts
    call_counts = {}

    @cache
    def add(a, b):
        """Adds two numbers"""
        call_counts['add'] = call_counts.get('add', 0) + 1
        return a + b

    @cache
    def fibonacci(n):
        """Calculate fibonacci number"""
        call_counts['fib'] = call_counts.get('fib', 0) + 1
        if n <= 1:
            return n
        # Without cache, this would be exponential calls
        return fibonacci(n-1) + fibonacci(n-2)

    @cache
    def greet(name, greeting="Hello"):
        """Greet someone"""
        call_counts['greet'] = call_counts.get('greet', 0) + 1
        return f"{greeting}, {name}!"

    tests = []
    passed = 0

    # Test 1: Basic caching works
    tests.append(("Caching works",
                  add(2, 3) == 5 and add(2, 3) == 5 and call_counts['add'] == 1))

    # Test 2: Different args = new call
    tests.append(("Different args call function",
                  add(3, 4) == 7 and call_counts['add'] == 2))

    # Test 3: Metadata preserved - __name__
    tests.append(("Function name preserved",
                  add.__name__ == "add"))

    # Test 4: Metadata preserved - __doc__
    tests.append(("Docstring preserved",
                  add.__doc__ == "Adds two numbers"))

    # Test 5: Works with recursion + caching
    call_counts['fib'] = 0
    result = fibonacci(10)
    tests.append(("Fibonacci caching (should be ~11 calls, not 177)",
                  result == 55 and call_counts['fib'] <= 15))

    # Test 6: __name__ preserved for fibonacci
    tests.append(("Fibonacci name preserved",
                  fibonacci.__name__ == "fibonacci"))

    # Test 7: Works with kwargs
    tests.append(("Works with kwargs",
                  greet("Alice") == "Hello, Alice!"))

    # Test 8: Kwargs cached correctly
    call_counts['greet'] = 0
    greet("Bob", greeting="Hi")
    greet("Bob", greeting="Hi")
    tests.append(("Kwargs cached",
                  call_counts['greet'] == 1))

    # Test 9: Different kwargs = new call
    greet("Bob", greeting="Hey")
    tests.append(("Different kwargs call function",
                  call_counts['greet'] == 2))

    # Test 10: __wrapped__ attribute exists
    tests.append(("__wrapped__ exists",
                  hasattr(add, '__wrapped__')))

    for i, (desc, result) in enumerate(tests, 1):
        if result:
            print(f"  [PASS] Test {i}: {desc}")
            passed += 1
        else:
            print(f"  [FAIL] Test {i}: {desc}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{len(tests)} tests passed")
    if passed == len(tests):
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
