"""
PROBLEM: Two Sum II - Input Array Is Sorted
LeetCode #167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers `numbers` that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number.

Return the indices of the two numbers (1-indexed) as a list [index1, index2]
where 1 <= index1 < index2 <= len(numbers).

There is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space (no hashmap!).

Constraints:
- 2 <= len(numbers) <= 30000
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- Exactly one solution exists

DIFFICULTY: Easy
TIME LIMIT: 5 minutes
STARTED: 2026-03-17 14:12 IST
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================
#step 1
# i will intialise two pointer with one as i = 1 , and j = len, bxz list indexed from 1
# start itertating over list till i<j, 
# on each iteration i will keep adding ele at i and j and check if their sum is = to target
# if target sum found return i and j as list else keep iterating tilll cond is met
# return empty list if no found but since there will always be a solution this will never hit
# time complexity -> O(n) bcz i + j = n so overall iteration is n 


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def two_sum(arr, tg):
    i , j = 0, len(arr)-1
    while i < j:
        temp_sum = arr[i] + arr[j]
        if temp_sum == tg:
            return [i+1, j+1]
        if temp_sum < tg:
            i += 1
        else:
            j -= 1



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (numbers, target, expected_output)
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19, [9, 10]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [1, 2]),
        ([-5, -3, 0, 2, 4, 6, 8], 3, [1, 7]),
        ([1, 1, 1, 1, 2, 3], 4, [1, 6]),  # duplicate values
        ([5, 25, 75], 100, [2, 3]),
        ([-1000, -1, 0, 1, 1000], 0, [1, 5]),
        ([1, 3], 4, [1, 2]),
    ]

    passed = 0
    total = len(tests)

    for i, (numbers, target, expected) in enumerate(tests, 1):
        try:
            result = two_sum(numbers, target)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: two_sum({numbers}, {target}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
