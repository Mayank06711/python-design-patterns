"""
PROBLEM: Implement my_map, my_filter, my_reduce (Higher-Order Functions)
Source: Q8 — Section 2: Higher-Order Functions

Without using any built-in map/filter/reduce or list comprehensions,
implement your own versions from scratch.

- my_map(func, iterable) → list of func(item) for each item
- my_filter(func, iterable) → list of items where func(item) is True
- my_reduce(func, iterable, initial) → single value by repeatedly
  applying func(accumulator, current_item)

Example:
    my_map(lambda x: x ** 2, [1, 2, 3])        → [1, 4, 9]
    my_filter(lambda x: x > 2, [1, 2, 3, 4])   → [3, 4]
    my_reduce(lambda a, b: a + b, [1, 2, 3], 0) → 6

CONSTRAINTS:
- No built-in map(), filter(), functools.reduce()
- No list comprehensions or generator expressions
- Use only loops and basic operations
- my_reduce must support an optional initial value
  (if not given, use first element as initial and start from second)

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 3:47 PM, Mar 25, 2026
COMPLETED: 4:10 PM, Mar 25, 2026
ATTEMPT: 1 (multiple iterations on reduce)
"""

# ============================================================
# STEP 1: HOF DESIGN (fill before coding)
# ============================================================
# 1. WHAT: So the question want me to implement this map filter reduce of my own for better understanding of higher order function 
# 2. HOF PATTERN: (each function takes a ___ as argument — what does that function do at each step?) The X fun AA function is the first input and the list auditable item at second and applies that function on each item of that table and return and new list , Filters do the same but it like filter out the based on the output of a function like the past function if it is true that that particular input will be inside return returned a renewary , Reduce do one thing it's it applies the given function on all of the items and then returns a single value Can it can be Curvilator it can be a product something like
# 3. ALGORITHM: (step by step for each of the 3 functions)
# 4. EDGE CASES: (what if the list is empty? what if no initial value for reduce?)
# for map
# And I will create my map function which will take any function What I will do is I will iterate on the given list and call that function for each item in the list and save it inside another list and return it one slope comple 
# for filetr I will do as same as map but here I will check the output of the function If it is true I will put that value in the returning list otherwise I exclude that
# fir reduce  i will run funtion for each ele and keeping taking result in one var and then return it

def my_map(func, items):
    if len(items)==0:
        return items
    ans = []
    for item in items:
        ans.append(func(item))
    return ans

def my_filter(func, items):
    if len(items) == 0:
        return items
    ans = []
    for item in items:
        is_passed = func(item)
        if is_passed:
            ans.append(item)
    return ans


def my_reduce(func, items, initial = None):
    if len(items) ==0:
        if initial is not None:
            return initial
        else:
            return 0
    for item in items:
        if initial is None:
            initial = items[0]
            continue
        val = func(initial, item)
        initial = val
    return initial
    
        
        


    

# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests_passed = 0
    tests_total = 0

    def check(label, result, expected):
        nonlocal tests_passed, tests_total
        tests_total += 1
        if result == expected:
            print(f"  [PASS] {label}")
            tests_passed += 1
        else:
            print(f"  [FAIL] {label}: got {result}, expected {expected}")

    # ---- my_map tests ----
    print("\n--- my_map ---")
    check("square numbers", my_map(lambda x: x ** 2, [1, 2, 3, 4]), [1, 4, 9, 16])
    check("double strings", my_map(lambda s: s * 2, ["a", "b", "c"]), ["aa", "bb", "cc"])
    check("empty list", my_map(lambda x: x + 1, []), [])
    check("single element", my_map(lambda x: x * 10, [7]), [70])
    check("bool conversion", my_map(lambda x: x > 0, [-1, 0, 1, 2]), [False, False, True, True])
    check("string lengths", my_map(len, ["hi", "hello", "hey"]), [2, 5, 3])

    # ---- my_filter tests ----
    print("\n--- my_filter ---")
    check("keep positives", my_filter(lambda x: x > 0, [-2, -1, 0, 1, 2]), [1, 2])
    check("even numbers", my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]), [2, 4, 6])
    check("empty list", my_filter(lambda x: x > 0, []), [])
    check("none pass", my_filter(lambda x: x > 100, [1, 2, 3]), [])
    check("all pass", my_filter(lambda x: x > 0, [1, 2, 3]), [1, 2, 3])
    check("filter strings", my_filter(lambda s: len(s) > 3, ["hi", "hello", "hey", "world"]), ["hello", "world"])

    # ---- my_reduce tests ----
    print("\n--- my_reduce ---")
    check("sum with initial", my_reduce(lambda a, b: a + b, [1, 2, 3, 4], 0), 10)
    check("sum without initial", my_reduce(lambda a, b: a + b, [1, 2, 3, 4]), 10)
    check("product with initial", my_reduce(lambda a, b: a * b, [1, 2, 3, 4], 1), 24)
    check("product without initial", my_reduce(lambda a, b: a * b, [1, 2, 3, 4]), 24)
    check("max value", my_reduce(lambda a, b: a if a > b else b, [3, 1, 4, 1, 5, 9]), 9)
    check("string concat", my_reduce(lambda a, b: a + b, ["h", "e", "l", "l", "o"]), "hello")
    check("single element no initial", my_reduce(lambda a, b: a + b, [42]), 42)
    check("initial with empty list", my_reduce(lambda a, b: a + b, [], 0), 0)
    check("build dict", my_reduce(lambda d, kv: {**d, kv[0]: kv[1]}, [("a", 1), ("b", 2)], {}), {"a": 1, "b": 2})

    print(f"\n{'='*50}")
    print(f"  Results: {tests_passed}/{tests_total} tests passed")
    if tests_passed == tests_total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
