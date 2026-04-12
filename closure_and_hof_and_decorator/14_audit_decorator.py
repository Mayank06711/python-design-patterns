"""
Exercise 14: @audit Decorator — Integration Capstone
=====================================================

STARTED:   2026-04-09 13:19:59
COMPLETED: 2026-04-09 13:34:14
ATTEMPT:   2
SCORE:     8/10 (Correctness 4 + Attempts 2 + Hints 1 + Quality 1)
TIME:      14 min 15 sec

This exercise is based on YOUR OWN Q5 answer from the Session 17 capstone quiz.
You said: "for important DB operations, use a 3-tier decorator that takes an
event name and emits success/failure events so other services can consume."

Now build it.

---

PROBLEM:
--------
Write a decorator `@audit(event_name)` that logs what happened to a function call.
Think of it as the foundation of an observability / analytics pipeline.

Requirements:
  1. Takes ONE argument: `event_name` (a string)
  2. BEFORE the function runs: append "START:<event_name>" to the audit log
  3. If function returns normally:
       - Append "SUCCESS:<event_name>" to the audit log
       - Return the function's actual return value (don't eat it)
  4. If function raises an exception:
       - Append "FAILURE:<event_name>:<exception message>" to the audit log
       - Re-raise the SAME exception (don't swallow it)
  5. Must use `functools.wraps` to preserve function metadata
  6. Must accept any combination of *args and **kwargs

The audit log is a module-level list called `audit_log`. The decorator appends
to this list. Tests inspect this list to verify correct ordering.

NO hints on structure. Design it yourself. Remember: 3 levels, try/except in the
innermost wrapper, and functools.wraps on the wrapper.

---
"""

import functools

# Module-level audit log — the decorator appends to this.
audit_log: list[str] = []


def audit(event_name: str):
    # YOUR CODE HERE
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                audit_log.append(f"START:{event_name}")
                result = func(*args, **kwargs)
                audit_log.append(f"SUCCESS:{event_name}")
                return result
            except Exception as e:
                audit_log.append(f"FAILURE:{event_name}:{e}")
                raise
        return wrapper
    return deco




# ============================================================================
# TESTS — do not modify below this line
# ============================================================================

def _reset():
    audit_log.clear()


def test_success_returns_value():
    _reset()

    @audit("create_user")
    def create_user(name: str) -> dict:
        return {"id": 1, "name": name}

    result = create_user("alice")
    assert result == {"id": 1, "name": "alice"}, f"return value lost: {result}"
    print("PASS: success returns correct value")


def test_success_logs_start_and_success_in_order():
    _reset()

    @audit("delete_user")
    def delete_user(user_id: int) -> bool:
        return True

    delete_user(42)
    assert audit_log == ["START:delete_user", "SUCCESS:delete_user"], \
        f"wrong log order: {audit_log}"
    print("PASS: success logs START then SUCCESS in order")


def test_failure_logs_start_and_failure():
    _reset()

    @audit("charge_card")
    def charge_card(amount: int):
        raise ValueError("insufficient funds")

    try:
        charge_card(100)
        assert False, "expected ValueError to propagate"
    except ValueError as e:
        assert str(e) == "insufficient funds"

    assert audit_log[0] == "START:charge_card", f"missing START: {audit_log}"
    assert audit_log[1] == "FAILURE:charge_card:insufficient funds", \
        f"wrong failure log: {audit_log}"
    print("PASS: failure logs START then FAILURE with exception message")


def test_failure_reraises_same_exception_type():
    _reset()

    @audit("divide")
    def divide(a, b):
        return a / b

    try:
        divide(10, 0)
        assert False, "expected ZeroDivisionError"
    except ZeroDivisionError:
        pass
    except Exception as e:
        assert False, f"wrong exception type: {type(e).__name__}"
    print("PASS: re-raises original exception type (ZeroDivisionError)")


def test_accepts_args_and_kwargs():
    _reset()

    @audit("update_profile")
    def update_profile(user_id, *, email=None, age=None):
        return f"{user_id}:{email}:{age}"

    result = update_profile(7, email="a@b.c", age=30)
    assert result == "7:a@b.c:30", f"args/kwargs broken: {result}"
    print("PASS: accepts positional and keyword args")


def test_preserves_function_metadata():
    _reset()

    @audit("compute")
    def compute(x: int) -> int:
        """Compute the double of x."""
        return x * 2

    assert compute.__name__ == "compute", f"__name__ not preserved: {compute.__name__}"
    assert compute.__doc__ == "Compute the double of x.", \
        f"__doc__ not preserved: {compute.__doc__}"
    print("PASS: functools.wraps preserves __name__ and __doc__")


def test_multiple_functions_share_same_log():
    _reset()

    @audit("op_a")
    def op_a():
        return "a"

    @audit("op_b")
    def op_b():
        raise RuntimeError("boom")

    op_a()
    try:
        op_b()
    except RuntimeError:
        pass
    op_a()

    assert audit_log == [
        "START:op_a", "SUCCESS:op_a",
        "START:op_b", "FAILURE:op_b:boom",
        "START:op_a", "SUCCESS:op_a",
    ], f"wrong multi-call log: {audit_log}"
    print("PASS: multiple functions share one audit log with correct interleaving")


def test_different_event_names_on_same_function_type():
    _reset()

    @audit("order_create")
    def create():
        return "created"

    @audit("order_cancel")
    def cancel():
        return "cancelled"

    create()
    cancel()
    assert audit_log == [
        "START:order_create", "SUCCESS:order_create",
        "START:order_cancel", "SUCCESS:order_cancel",
    ], f"event names not captured per-decoration: {audit_log}"
    print("PASS: event_name is captured per decoration (closure works)")


if __name__ == "__main__":
    test_success_returns_value()
    test_success_logs_start_and_success_in_order()
    test_failure_logs_start_and_failure()
    test_failure_reraises_same_exception_type()
    test_accepts_args_and_kwargs()
    test_preserves_function_metadata()
    test_multiple_functions_share_same_log()
    test_different_event_names_on_same_function_type()
    print("\nAll 8 tests passed ✅")
