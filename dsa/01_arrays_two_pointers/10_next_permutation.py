"""
PROBLEM: Next Permutation
LeetCode #31: https://leetcode.com/problems/next-permutation/

A permutation of an array of integers is an arrangement of its members
into a sequence or linear order.

The next permutation of an array of integers is the next lexicographically
greater permutation. If the array is the last permutation (fully descending),
return the first permutation (fully ascending).

The replacement must be IN PLACE and use only constant extra memory.

Examples:
  [1, 2, 3] → [1, 3, 2]     (next after 123 is 132)
  [3, 2, 1] → [1, 2, 3]     (last permutation wraps to first)
  [1, 1, 5] → [1, 5, 1]
  [1, 3, 2] → [2, 1, 3]     (next after 132 is 213)

Constraints:
- 1 <= len(nums) <= 100
- 0 <= nums[i] <= 100
- Modify nums IN PLACE. Return nothing.

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 4:11 PM, Mar 30, 2026
COMPLETED: 1:29 PM, Apr 1, 2026
ATTEMPT: 2 (fixed swap logic)
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?) The question says it needs a number which is like bigger than the given number I mean given list what numbers come just after it
# 2. HOW: (step-by-step algorithm) Algorithm one we can calculate all possible permutation and save it in a result array Then it rate on that result array and match which array Like which element like which number in that resultatory is same as the given number and since we will already be we will be sorting that result before doing this We know that after this the permutation the next element just after this is the permutation, Second algorithm is what we do is since we need lexicographical order or next next means what comes just after this just after this is the mean word So just after this means what comes after one it's two what comes after 10 it's 11 just after it's not 12 it's not 9 How did we know that Eleven will come we know 10 if we increase by the minimum amount that is unity it will be going to be one how do we know this if we start from the right because this is how we write things right left to down 1 tense 100,000 so if one is at Max 0 there is nothing that we can have at zero place Got it we we go to one OK so one is there any smaller event beyond this yes one so one plus 10-> 11
# 3. EDGE CASES: (what could go wrong?) If if there are duplicates we have to handle that case And if the array is already sorted we will not find anything Any break point then we have to reverse it
# 4. COMPLEXITY: (time and space) Big O of N for finding breakpoint then we go off N for fixing it
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def next_permutation(nums):
    if len(nums) <= 1:
        return nums
    break_point = -1
    n = len(nums)
    for i in range(n-1, 0, -1):
        if nums[i-1] < nums[i]:
            break_point = i - 1
            break
    if break_point < 0:
        nums.reverse()
        return nums
    for i in range(n-1, break_point, -1):
        if nums[i] > nums[break_point]: # smallet ele greater than pur breakpoint
            nums[i], nums[break_point] = nums[break_point], nums[i]
            break
    nums[break_point+1:] = nums[break_point+1:][::-1]
    return nums    



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (input, expected_after_mutation)
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 3, 2], [2, 1, 3]),
        ([1], [1]),
        ([2, 3, 1], [3, 1, 2]),
        ([1, 5, 8, 4, 7, 6, 5, 3, 1], [1, 5, 8, 5, 1, 3, 4, 6, 7]),
        ([5, 4, 7, 5, 3, 2], [5, 5, 2, 3, 4, 7]),
        ([1, 2, 3, 4], [1, 2, 4, 3]),
        ([2, 2, 2], [2, 2, 2]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            original = nums[:]
            next_permutation(nums)
            if nums == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: {original} → {nums}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
