"""
Decorator Stacking + Class Decorators Exercise

PART A: Decorator Stacking
Build two decorators:
  1. @bold - wraps the return value in <b>...</b>
  2. @italic - wraps the return value in <i>...</i>

Then stack them on functions to produce correct HTML output.
Remember: wrapping order (bottom-up) vs calling order (top-down).

PART B: Class Decorator
Build a class-based decorator called `CallTracker` that:
  - Tracks how many times the function has been called (.call_count)
  - Tracks the last arguments it was called with (.last_args, .last_kwargs)
  - Still returns the correct result of the original function
  - Preserves the original function's __name__ and __doc__

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
"""
from functools import wraps
# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# for ppaert A, i will create two decorators one named as bold and other as italic and inside that  i will make wrapper and wrapper will take args and kwrgs and then wrap them inside b and i tag as per decorator

# ============================================================
# PART A: Build @bold and @italic decorators
# ============================================================
def bold(func):
    @wraps(func) 
    def bold_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return bold_wrapper

def italic(func):
    @wraps(func)
    def italic_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return italic_wrapper


# ============================================================
# PART B: Build CallTracker class decorator
# ============================================================
class CallTracker:
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__
        self.call_count = 0
        self.last_args = None
        self.last_kwargs = None
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        self.call_count += 1
        self.last_args = args
        self.last_kwargs = kwargs
        return result
    



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    passed = 0
    total = 16

    # --- PART A: Stacking tests ---

    # Test 1: bold only
    @bold
    def greet1():
        return "hello"
    result = greet1()
    if result == "<b>hello</b>":
        print("  [PASS] Test 1: @bold alone")
        passed += 1
    else:
        print(f"  [FAIL] Test 1: got {result!r}, expected '<b>hello</b>'")

    # Test 2: italic only
    @italic
    def greet2():
        return "hello"
    result = greet2()
    if result == "<i>hello</i>":
        print("  [PASS] Test 2: @italic alone")
        passed += 1
    else:
        print(f"  [FAIL] Test 2: got {result!r}, expected '<i>hello</i>'")

    # Test 3: bold on top of italic
    @bold
    @italic
    def greet3():
        return "hello"
    result = greet3()
    if result == "<b><i>hello</i></b>":
        print("  [PASS] Test 3: @bold(@italic) = <b><i>hello</i></b>")
        passed += 1
    else:
        print(f"  [FAIL] Test 3: got {result!r}, expected '<b><i>hello</i></b>'")

    # Test 4: italic on top of bold (reversed order)
    @italic
    @bold
    def greet4():
        return "hello"
    result = greet4()
    if result == "<i><b>hello</b></i>":
        print("  [PASS] Test 4: @italic(@bold) = <i><b>hello</b></i>")
        passed += 1
    else:
        print(f"  [FAIL] Test 4: got {result!r}, expected '<i><b>hello</b></i>'")

    # Test 5: with arguments
    @bold
    @italic
    def greet5(name):
        return f"hi {name}"
    result = greet5("Mayank")
    if result == "<b><i>hi Mayank</i></b>":
        print("  [PASS] Test 5: stacked with args")
        passed += 1
    else:
        print(f"  [FAIL] Test 5: got {result!r}, expected '<b><i>hi Mayank</i></b>'")

    # Test 6: triple stack
    @bold
    @italic
    @bold
    def greet6():
        return "wow"
    result = greet6()
    if result == "<b><i><b>wow</b></i></b>":
        print("  [PASS] Test 6: triple stack @bold(@italic(@bold))")
        passed += 1
    else:
        print(f"  [FAIL] Test 6: got {result!r}, expected '<b><i><b>wow</b></i></b>'")

    # --- PART B: CallTracker tests ---

    # Test 7: basic call counting
    @CallTracker
    def add(a, b):
        """Adds two numbers."""
        return a + b

    add(1, 2)
    if add.call_count == 1:
        print("  [PASS] Test 7: call_count = 1 after one call")
        passed += 1
    else:
        print(f"  [FAIL] Test 7: call_count = {add.call_count}, expected 1")

    # Test 8: return value preserved
    result = add(3, 4)
    if result == 7:
        print("  [PASS] Test 8: return value correct (7)")
        passed += 1
    else:
        print(f"  [FAIL] Test 8: got {result}, expected 7")

    # Test 9: call_count increments
    if add.call_count == 2:
        print("  [PASS] Test 9: call_count = 2 after two calls")
        passed += 1
    else:
        print(f"  [FAIL] Test 9: call_count = {add.call_count}, expected 2")

    # Test 10: last_args tracked
    add(10, 20)
    if add.last_args == (10, 20):
        print("  [PASS] Test 10: last_args = (10, 20)")
        passed += 1
    else:
        print(f"  [FAIL] Test 10: last_args = {add.last_args}, expected (10, 20)")

    # Test 11: last_kwargs tracked
    add(a=5, b=6)
    if add.last_kwargs == {"a": 5, "b": 6}:
        print("  [PASS] Test 11: last_kwargs tracked")
        passed += 1
    else:
        print(f"  [FAIL] Test 11: last_kwargs = {add.last_kwargs}, expected {{'a': 5, 'b': 6}}")

    # Test 12: call_count after 4 calls
    if add.call_count == 4:
        print("  [PASS] Test 12: call_count = 4 after four calls")
        passed += 1
    else:
        print(f"  [FAIL] Test 12: call_count = {add.call_count}, expected 4")

    # Test 13: __name__ preserved
    if add.__name__ == "add":
        print("  [PASS] Test 13: __name__ preserved")
        passed += 1
    else:
        print(f"  [FAIL] Test 13: __name__ = {add.__name__!r}, expected 'add'")

    # Test 14: __doc__ preserved
    if add.__doc__ == "Adds two numbers.":
        print("  [PASS] Test 14: __doc__ preserved")
        passed += 1
    else:
        print(f"  [FAIL] Test 14: __doc__ = {add.__doc__!r}")

    # Test 15: separate instances don't share state
    @CallTracker
    def multiply(a, b):
        return a * b

    multiply(2, 3)
    multiply(4, 5)
    if multiply.call_count == 2 and add.call_count == 4:
        print("  [PASS] Test 15: separate instances, independent counts")
        passed += 1
    else:
        print(f"  [FAIL] Test 15: multiply.count={multiply.call_count}, add.count={add.call_count}")

    # Test 16: works with no-arg functions
    @CallTracker
    def say_hi():
        return "hi"

    result = say_hi()
    if result == "hi" and say_hi.call_count == 1 and say_hi.last_args == ():
        print("  [PASS] Test 16: no-arg function works")
        passed += 1
    else:
        print(f"  [FAIL] Test 16: result={result!r}, count={say_hi.call_count}, args={say_hi.last_args}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
