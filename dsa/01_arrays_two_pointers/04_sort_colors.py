"""
PROBLEM: Sort Colors (Dutch National Flag)
LeetCode #75: https://leetcode.com/problems/sort-colors/
Striver SDE Sheet: Arrays

Given an array nums with n objects colored red, white, or blue,
sort them IN-PLACE so that objects of the same color are adjacent,
with the colors in the order red (0), white (1), and blue (2).

You must solve this problem WITHOUT using the library's sort function.

CONSTRAINTS:
- Must be done IN-PLACE (modify the array, return nothing)
- Only values 0, 1, 2 in the array
- 1 <= len(nums) <= 300

FOLLOW-UP: Could you come up with a one-pass algorithm using only constant extra space?
(This is the real interview question — one pass, O(1) space)

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: ___
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def sort_colors(nums):
    pass


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (input, expected)
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2, 2, 2, 0, 0, 0], [0, 0, 0, 2, 2, 2]),
        ([1, 0], [0, 1]),
        ([0, 0, 0], [0, 0, 0]),
        ([2, 1, 0, 2, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        ([1, 2, 0, 1, 2, 0], [0, 0, 1, 1, 2, 2]),
        ([0, 2, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 2, 2]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            nums_copy = nums[:]
            sort_colors(nums_copy)
            if nums_copy == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: sort_colors({nums}) = {nums_copy}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
