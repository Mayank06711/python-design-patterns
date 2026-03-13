# Closures, Higher-Order Functions & Decorators -- Interview Questions
## (Mid to Advanced | Google, Amazon & Top Tech Companies)

---

## SECTION 1: CLOSURES -- Output Prediction & Conceptual

---

### Q1. [JavaScript | Output Prediction | Asked at Google & Amazon]
**What is the output of the following code? Explain why.**

```javascript
for (var i = 0; i < 5; i++) {
  setTimeout(function () {
    console.log(i);
  }, i * 1000);
}
```

**Follow-up:** How would you fix it to print 0, 1, 2, 3, 4? Provide at least three different solutions (let, IIFE, third argument to setTimeout).

---

### Q2. [Python | Output Prediction | Toptal / FAANG Classic]
**What does the following code print? Why?**

```python
def multipliers():
    return [lambda x: i * x for i in range(4)]

print([m(2) for m in multipliers()])
```

**Follow-up:** Fix it using (a) default argument binding, (b) functools.partial, and (c) a generator expression.

---

### Q3. [JavaScript | Output Prediction | Mid-Level]
**What is the output?**

```javascript
function createFunctions() {
  var result = [];
  for (var i = 0; i < 3; i++) {
    result.push(function () {
      return i;
    });
  }
  return result;
}

var funcs = createFunctions();
console.log(funcs[0]());
console.log(funcs[1]());
console.log(funcs[2]());
```

**Follow-up:** Rewrite using `let`. Then rewrite using an IIFE to achieve the same fix while keeping `var`.

---

### Q4. [Python | Output Prediction | Advanced]
**What is the output? Explain the role of late binding.**

```python
def make_adders():
    adders = []
    for i in range(5):
        def adder(x):
            return x + i
        adders.append(adder)
    return adders

adders = make_adders()
print(adders[0](10))
print(adders[2](10))
print(adders[4](10))
```

**Follow-up:** How does Python's late binding of closures differ from JavaScript's behavior with `let` vs `var`?

---

### Q5. [JavaScript | Conceptual + Coding | Google-style]
**Explain lexical scoping and how closures leverage it. Then write a function `createCounter()` that returns an object with `increment()`, `decrement()`, and `getValue()` methods, all sharing private state via closure.**

```javascript
// Expected usage:
const counter = createCounter(10); // starts at 10
counter.increment();
counter.increment();
counter.decrement();
console.log(counter.getValue()); // 11
```

---

### Q6. [Python | Coding | Amazon-style]
**Write a function `make_accumulator(n)` that returns a function. Each time the returned function is called with a value, it adds that value to a running total (starting from `n`) and returns the new total.**

```python
acc = make_accumulator(5)
print(acc(10))  # 15
print(acc(20))  # 35
print(acc(3))   # 38
```

**Follow-up:** Explain why you need `nonlocal` in Python 3 for this to work. What would happen in Python 2?

---

### Q7. [JavaScript | Output Prediction | Advanced Pitfall]
**What is the output? Explain the difference between closure over variable vs. closure over value.**

```javascript
let a = 1;
function outer() {
  let b = 2;
  function inner() {
    let c = 3;
    console.log(a, b, c);
  }
  a = 10;
  b = 20;
  return inner;
}

const fn = outer();
fn();
```

---

## SECTION 2: HIGHER-ORDER FUNCTIONS (map, filter, reduce, function factories, currying, partial application)

---

### Q8. [Python | Coding | Mid-Level]
**Without using any built-in, implement your own `my_map`, `my_filter`, and `my_reduce` functions from scratch.** They should behave identically to Python's `map()`, `filter()`, and `functools.reduce()`.

```python
# Example usage:
print(list(my_map(lambda x: x ** 2, [1, 2, 3, 4])))    # [1, 4, 9, 16]
print(list(my_filter(lambda x: x > 2, [1, 2, 3, 4])))   # [3, 4]
print(my_reduce(lambda a, b: a + b, [1, 2, 3, 4], 0))   # 10
```

---

### Q9. [JavaScript | Coding | Google-style]
**Implement a `curry` function that converts any multi-argument function into a curried version.**

```javascript
function curry(fn) {
  // Your implementation
}

function add(a, b, c) {
  return a + b + c;
}

const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3));   // 6
console.log(curriedAdd(1, 2)(3));   // 6
console.log(curriedAdd(1)(2, 3));   // 6
console.log(curriedAdd(1, 2, 3));   // 6
```

---

### Q10. [Python | Coding | Advanced]
**Implement `partial` from scratch (without using `functools.partial`).** It should fix some arguments of a function and return a new function that takes the remaining arguments.

```python
def my_partial(func, *fixed_args, **fixed_kwargs):
    # Your implementation
    pass

def power(base, exponent):
    return base ** exponent

square = my_partial(power, exponent=2)
cube = my_partial(power, exponent=3)

print(square(5))  # 25
print(cube(3))    # 27
```

---

### Q11. [JavaScript | Coding | Amazon-style]
**Write a function `compose` that takes multiple functions and returns a new function that is the right-to-left composition of those functions. Also write `pipe` (left-to-right).**

```javascript
const compose = (...fns) => { /* your code */ };
const pipe = (...fns) => { /* your code */ };

const add1 = x => x + 1;
const double = x => x * 2;
const square = x => x * x;

const composed = compose(square, double, add1);
console.log(composed(3));  // square(double(add1(3))) = square(double(4)) = square(8) = 64

const piped = pipe(add1, double, square);
console.log(piped(3));     // square(double(add1(3))) = 64
```

---

### Q12. [Python | Conceptual + Coding | Mid-Level]
**Explain the difference between `map` + `lambda` vs list comprehension in Python. When would you prefer one over the other? Then, using only higher-order functions (no loops, no comprehensions), transform a list of strings into a list of their lengths, keeping only those with length > 3.**

```python
words = ["hi", "hello", "hey", "wonderful", "ok", "python"]
# Expected: [5, 9, 6]
```

---

### Q13. [JavaScript | Output Prediction + Conceptual | Advanced]
**What is the output? Explain how `reduce` works step-by-step.**

```javascript
const result = [1, 2, 3, 4, 5].reduce((acc, curr, idx) => {
  console.log(`Step ${idx}: acc=${acc}, curr=${curr}`);
  return acc + curr;
});
console.log("Result:", result);
```

**Follow-up:** What happens if the array is empty and no initial value is provided?

---

### Q14. [Python | Coding | Advanced | Function Factory]
**Create a function factory `make_validator(min_val, max_val)` that returns a validator function. The validator should return True if a value is within the range, False otherwise. Then use it with `filter()` to filter a list.**

```python
in_range = make_validator(10, 50)
data = [5, 12, 48, 3, 55, 30, 100, 25]
print(list(filter(in_range, data)))  # [12, 48, 30, 25]
```

**Follow-up:** Extend it to `make_validator(min_val, max_val, inclusive=True)` and handle edge cases.

---

## SECTION 3: PYTHON DECORATORS (function decorators, class decorators, decorators with arguments, functools.wraps)

---

### Q15. [Python | Coding | Google / Amazon Classic]
**Implement a `@timer` decorator that measures and prints the execution time of any function. Make sure to use `functools.wraps` properly. Explain what happens if you omit `functools.wraps` and why it matters.**

```python
import time
import functools

def timer(func):
    # Your implementation
    pass

@timer
def slow_function(n):
    """Simulates a slow computation."""
    time.sleep(n)
    return f"Done after {n}s"

result = slow_function(2)
# Should print: slow_function executed in 2.00xx seconds
# result should be "Done after 2s"
print(slow_function.__name__)  # Should print: slow_function (not 'wrapper')
print(slow_function.__doc__)   # Should print: Simulates a slow computation.
```

---

### Q16. [Python | Coding | Advanced | Decorator with Arguments]
**Write a `@retry(max_attempts=3, delay=1, backoff=2)` decorator that retries a function if it raises an exception, with exponential backoff.**

```python
import time
import functools

def retry(max_attempts=3, delay=1, backoff=2):
    # Your implementation
    pass

@retry(max_attempts=4, delay=0.5, backoff=2)
def unstable_api_call():
    """Simulates an unreliable API."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("API failed")
    return {"status": "success"}

# Should retry up to 4 times with delays: 0.5s, 1s, 2s, 4s
```

---

### Q17. [Python | Coding | Advanced | Memoization Decorator]
**Implement a `@memoize` decorator that caches results of function calls. It should handle unhashable arguments gracefully. Compare your implementation with `functools.lru_cache`.**

```python
def memoize(func):
    # Your implementation
    pass

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # Should compute instantly due to caching
```

**Follow-up:** How would you add a cache size limit (LRU eviction)? How does `functools.lru_cache` handle this internally?

---

### Q18. [Python | Coding | Advanced | Class-Based Decorator]
**Implement a class-based decorator `@count_calls` that tracks how many times a decorated function has been called. It should preserve the original function's metadata.**

```python
import functools

class count_calls:
    # Your implementation
    pass

@count_calls
def say_hello(name):
    """Greets a person."""
    print(f"Hello, {name}!")

say_hello("Alice")
say_hello("Bob")
say_hello("Charlie")
print(say_hello.call_count)  # 3
print(say_hello.__name__)    # say_hello
print(say_hello.__doc__)     # Greets a person.
```

**Follow-up:** What is the difference between using `functools.wraps` (for function decorators) and `functools.update_wrapper` (for class-based decorators)?

---

### Q19. [Python | Coding | Advanced | Stacking Decorators]
**What is the output of the following code? Explain the order of decorator execution.**

```python
def decorator_a(func):
    def wrapper(*args, **kwargs):
        print("Entering A")
        result = func(*args, **kwargs)
        print("Exiting A")
        return result
    return wrapper

def decorator_b(func):
    def wrapper(*args, **kwargs):
        print("Entering B")
        result = func(*args, **kwargs)
        print("Exiting B")
        return result
    return wrapper

@decorator_a
@decorator_b
def greet(name):
    print(f"Hello, {name}!")

greet("World")
```

**Follow-up:** If you swap the order to `@decorator_b` then `@decorator_a`, what changes? Explain the "decorator wrapping order vs execution order" distinction.

---

### Q20. [Python | Coding | Advanced | Decorator with Optional Arguments]
**Write a decorator that can be used BOTH with and without arguments:**

```python
# Both of these should work:
@debug
def add(a, b):
    return a + b

@debug(prefix="[TRACE]")
def multiply(a, b):
    return a * b

add(2, 3)       # Prints: calling add(2, 3) -> 5
multiply(4, 5)  # Prints: [TRACE] calling multiply(4, 5) -> 20
```

*Hint: You need to detect whether the decorator received a function or arguments.*

---

### Q21. [Python | Coding | Google-style | Rate Limiter]
**Implement a `@rate_limit(max_calls, period)` decorator that limits how many times a function can be called within a given time period (in seconds). If the limit is exceeded, raise a `RateLimitExceeded` exception.**

```python
import time

class RateLimitExceeded(Exception):
    pass

def rate_limit(max_calls, period):
    # Your implementation
    pass

@rate_limit(max_calls=3, period=10)
def api_request(endpoint):
    return f"Response from {endpoint}"

# Should allow first 3 calls, raise RateLimitExceeded on 4th within 10 seconds
```

---

### Q22. [Python | Conceptual + Coding | Advanced]
**Explain the relationship between closures and decorators. Then demonstrate that every decorator is essentially a higher-order function that leverages closures by writing a decorator step-by-step WITHOUT using the `@` syntax.**

```python
# Show that this:
@my_decorator
def foo():
    pass

# Is exactly equivalent to:
# foo = my_decorator(foo)

# Then show a decorator with arguments:
@my_decorator_with_args(arg1, arg2)
def bar():
    pass

# Is exactly equivalent to:
# bar = my_decorator_with_args(arg1, arg2)(bar)
```

---

## SECTION 4: MIXED / PRACTICAL CODING CHALLENGES

---

### Q23. [Python + JS | Conceptual | Advanced]
**Compare closures in Python vs JavaScript across these dimensions:**
1. How does variable binding work (late vs early)?
2. How does Python's `nonlocal` compare to JS's natural closure-over-variable behavior?
3. What are the scoping differences (`var`/`let`/`const` in JS vs Python's LEGB rule)?
4. Why does Python require `nonlocal` for reassignment but not for mutation (e.g., appending to a list)?

---

### Q24. [JavaScript | Coding | Advanced | Module Pattern]
**Using closures, implement a mini "module" that manages a user list. Expose only `addUser`, `removeUser`, `getUsers`, and `findUser` -- the internal array must be completely private and inaccessible from outside.**

```javascript
const UserModule = (function () {
  // Your implementation using closures for privacy
})();

UserModule.addUser({ id: 1, name: "Alice" });
UserModule.addUser({ id: 2, name: "Bob" });
console.log(UserModule.getUsers());        // [{id:1, name:"Alice"}, {id:2, name:"Bob"}]
console.log(UserModule.findUser(1));        // {id:1, name:"Alice"}
UserModule.removeUser(1);
console.log(UserModule.getUsers());         // [{id:2, name:"Bob"}]
// UserModule.users --> undefined (private!)
```

---

### Q25. [Python | Coding | Amazon-style | Real-World Decorator]
**Implement a `@validate_types` decorator that checks the types of arguments passed to a function at runtime using type hints. Raise `TypeError` with a descriptive message if any argument has the wrong type.**

```python
import functools
import inspect

def validate_types(func):
    # Your implementation using inspect.signature and func.__annotations__
    pass

@validate_types
def process_data(name: str, age: int, scores: list) -> str:
    return f"{name} (age {age}) has scores: {scores}"

print(process_data("Alice", 25, [90, 85, 92]))  # Works fine
print(process_data("Alice", "25", [90, 85, 92])) # Raises TypeError:
# Expected argument 'age' to be <class 'int'>, got <class 'str'>
```

---

### Q26. [JavaScript | Output Prediction | Tricky | Advanced]
**What is the output? Explain step by step.**

```javascript
function createMultiplier(multiplier) {
  return function (value) {
    return value * multiplier;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

const operations = [double, triple, createMultiplier(4)];
const results = operations.map((fn, idx) => fn(idx + 1));
console.log(results);
```

---

### Q27. [Python | Output Prediction | Tricky Decorator + Closure]
**What is the output of the following code? Trace through the execution carefully.**

```python
def logged(func):
    def wrapper(*args):
        print(f"Calling {func.__name__}")
        result = func(*args)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logged
def add(a, b):
    return a + b

@logged
def double(x):
    return add(x, x)

print(double(5))
```

*Hint: Think about what `add` refers to after decoration.*

---

### Q28. [Python | Coding | Advanced | Decorator that modifies return value]
**Write a `@jsonify` decorator that converts the return value of any function into a JSON string. Handle cases where the return value is not JSON-serializable by returning an error JSON.**

```python
import json
import functools

def jsonify(func):
    # Your implementation
    pass

@jsonify
def get_user():
    return {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

@jsonify
def get_time():
    from datetime import datetime
    return {"time": datetime.now()}  # datetime is not JSON serializable

print(get_user())   # '{"name": "Alice", "age": 30, "scores": [95, 87, 92]}'
print(get_time())   # '{"error": "Object of type datetime is not JSON serializable"}'
```

---

## BONUS RAPID-FIRE QUESTIONS (Conceptual -- often asked in phone screens)

---

### Q29. What is the difference between a closure and a lambda? Can you have a closure without a lambda? Can you have a lambda without a closure?

### Q30. In JavaScript, why does `typeof` a variable inside a closure return `undefined` before assignment (temporal dead zone with `let`/`const`) but not with `var`?

### Q31. What is the purpose of `functools.wraps`? What specific attributes does it copy? What breaks in production if you omit it (think: logging, documentation generators, serialization)?

### Q32. Explain the difference between currying and partial application with a concrete example. Is JavaScript's `Function.prototype.bind` an example of currying or partial application?

### Q33. Can a decorator change the number of arguments a function accepts? Give an example. What are the risks?

---

## ANSWER KEY HINTS

| Q# | Key Concept | Quick Answer Hint |
|----|-------------|-------------------|
| 1  | var + closure + setTimeout | Prints 5 five times (var is function-scoped) |
| 2  | Python late binding | [6, 6, 6, 6] -- i is 3 when lambdas execute |
| 3  | var + closure in loop | 3, 3, 3 |
| 4  | Python late binding | 14, 14, 14 -- i is 4 when adders execute |
| 7  | Closure over variable | 10 20 3 -- a and b were reassigned before inner() called |
| 13 | reduce without initial | First acc is element[0], iteration starts at index 1 |
| 19 | Stacked decorators | Entering A, Entering B, Hello World!, Exiting B, Exiting A |
| 26 | map with closures | [2, 6, 12] -- double(1)=2, triple(2)=6, quad(3)=12 |
| 27 | Decorated add inside double | "Calling double", "Calling add", "add returned 10", "double returned 10", 10 |

---

*Sources: Questions compiled and adapted from interview patterns reported at Google, Amazon, Meta, and other top tech companies via GeeksforGeeks, Toptal, InterviewBit, Frontend Interview Handbook, Coderbyte, and Dmitri Pavlutin's blog.*
