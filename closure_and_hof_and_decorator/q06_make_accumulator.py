"""
PROBLEM: Make Accumulator (Closure + nonlocal)
Source: Amazon-style interview question (Q6 from question bank)

Write a function `make_accumulator(n)` that returns a function.
Each time the returned function is called with a value, it adds
that value to a running total (starting from `n`) and returns
the new total.

Example:
    acc = make_accumulator(5)
    print(acc(10))  # 15
    print(acc(20))  # 35
    print(acc(3))   # 38

CONSTRAINTS:
- Must use closure (no classes, no global variables)
- The inner function takes exactly one argument
- Starting value comes from the outer function parameter

DIFFICULTY: Easy-Medium
TIME LIMIT: 5 minutes
STARTED: 12:50 AM, Mar 25, 2026
COMPLETED: 1:00 AM, Mar 25, 2026
ATTEMPT: 1
"""

# ============================================================
# STEP 1: CLOSURE DESIGN (fill before coding)
# ============================================================
# 1. WHAT: Question marks like I feel like question wants me to create a closure function which returns another function what it does it will calculate total Number of times the function is being called
# 2. CLOSURE DESIGN: (outer function / inner function / persistent state) I will create a outer function and name it same as in the test like make accumulator inside that that function will take a parameter I will call it initial value like value to be added and then slice like outer function variable and name it as total and it will be assigned with Whatever value we pass in make accumulator
# 3. CAPTURED VARS: (which vars captured? nonlocal needed where? why?) Now the inner function will be named as accumulator It will do only one thing It will first make sure that the total is assigned as non local so Python check for the enclosed and global variables and then it will do one thing it will be taking a parameter named as X it will do one thing it will assign total as total equal to total plus X then return the total 
# 4. ISOLATION: (two instances — shared state or independent? why?) Now if the make accommodator is called called toys it will create two different totals like in different like at different places in heap memory But if it is called once and then inner function is gets called multiple times it will keep updating the same value because that was defined as non local so it will not give undefined error


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def make_accumulator(x):
    running_total = x
    def acc(val):
        nonlocal running_total
        running_total += val
        return  running_total
    return acc



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 50)
    print("RUNNING TESTS")
    print("=" * 50)
    passed = 0
    failed = 0

    # Test 1: Basic accumulation
    acc = make_accumulator(5)
    result = acc(10)
    if result == 15:
        print("Test 1 PASSED: make_accumulator(5), acc(10) = 15")
        passed += 1
    else:
        print(f"Test 1 FAILED: expected 15, got {result}")
        failed += 1

    # Test 2: Continued accumulation
    result = acc(20)
    if result == 35:
        print("Test 2 PASSED: acc(20) = 35")
        passed += 1
    else:
        print(f"Test 2 FAILED: expected 35, got {result}")
        failed += 1

    # Test 3: Another call
    result = acc(3)
    if result == 38:
        print("Test 3 PASSED: acc(3) = 38")
        passed += 1
    else:
        print(f"Test 3 FAILED: expected 38, got {result}")
        failed += 1

    # Test 4: Start from zero
    acc2 = make_accumulator(0)
    result = acc2(100)
    if result == 100:
        print("Test 4 PASSED: make_accumulator(0), acc2(100) = 100")
        passed += 1
    else:
        print(f"Test 4 FAILED: expected 100, got {result}")
        failed += 1

    # Test 5: Negative starting value
    acc3 = make_accumulator(-10)
    result = acc3(5)
    if result == -5:
        print("Test 5 PASSED: make_accumulator(-10), acc3(5) = -5")
        passed += 1
    else:
        print(f"Test 5 FAILED: expected -5, got {result}")
        failed += 1

    # Test 6: Adding negative numbers
    result = acc3(-3)
    if result == -8:
        print("Test 6 PASSED: acc3(-3) = -8")
        passed += 1
    else:
        print(f"Test 6 FAILED: expected -8, got {result}")
        failed += 1

    # Test 7: Two independent accumulators don't interfere
    a = make_accumulator(10)
    b = make_accumulator(100)
    a(5)   # a: 15
    b(50)  # b: 150
    result_a = a(5)   # a: 20
    result_b = b(50)  # b: 200
    if result_a == 20 and result_b == 200:
        print("Test 7 PASSED: independent accumulators don't share state")
        passed += 1
    else:
        print(f"Test 7 FAILED: expected a=20, b=200, got a={result_a}, b={result_b}")
        failed += 1

    # Test 8: Adding zero
    acc4 = make_accumulator(42)
    result = acc4(0)
    if result == 42:
        print("Test 8 PASSED: acc(0) doesn't change total")
        passed += 1
    else:
        print(f"Test 8 FAILED: expected 42, got {result}")
        failed += 1

    # Test 9: Float values
    acc5 = make_accumulator(1.5)
    result = acc5(2.5)
    if result == 4.0:
        print("Test 9 PASSED: works with floats")
        passed += 1
    else:
        print(f"Test 9 FAILED: expected 4.0, got {result}")
        failed += 1

    # Test 10: Many calls
    acc6 = make_accumulator(0)
    for i in range(1, 11):
        result = acc6(i)
    if result == 55:  # 1+2+...+10 = 55
        print("Test 10 PASSED: 10 consecutive calls sum to 55")
        passed += 1
    else:
        print(f"Test 10 FAILED: expected 55, got {result}")
        failed += 1

    print("=" * 50)
    print(f"RESULTS: {passed}/{passed + failed} passed")
    print("=" * 50)

run_tests()
