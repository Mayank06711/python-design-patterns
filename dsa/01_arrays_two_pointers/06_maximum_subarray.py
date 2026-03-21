"""
PROBLEM: Maximum Subarray (Kadane's Algorithm)
LeetCode #53: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum,
and return its sum.

A subarray is a contiguous non-empty sequence of elements within an array.

CONSTRAINTS:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- Must run in O(n) time

FOLLOW-UP: Can you also return the start and end indices of the max subarray?

DIFFICULTY: Medium
TIME LIMIT: 10 minutes
STARTED: 2:09 AM (March 22, 2026)
COMPLETED: 2:51 AM (March 22, 2026)
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================
# approach 1
# take var named as maxi sum = 0
# two loop with outer i = 0 and inner j = 0 j<i
# in outer loop we declare a var named as sub_sum = 0now in inner loop we add sum of all elem till cond not met
# here we compare with maxi and sub_sum and update maxi is sub_sum > maxi
# return maxi
# t.c ->O(n2) and S.c ->O(1)

# approach 2
# DECLARE A GOABL VAR NAMED AS MAXI = int_min and another as sum
# NOW LOOP OVER GIVEN ARRAY FROM I = 0 TO < N
# for each iwill have  i willl do :
# sum = sum  + nums[i]
# if sum will be greater than maxi update maxi
# if sum is less than 0 i will make the sum as 0
# repeat it 
# t.c -> O(n) and S.c -> O(1)
# this algo work as say in [-1,2,1,-3] -> sub arrays will be [-1],[-1,2],[-1,2,1],[-1,2,1,-3],[2],[2,1],[2,1,-3],[1],[1,-3],[-3]
# now sums will be -1,1,2,-1,2,3,0,1,-2,-3
# but form here onward it doesn`t hit my mind why ?`  


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def max_subarray(nums):
    maxi = float('-inf')
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum > maxi:
            maxi = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return maxi


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (input, expected)
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
        ([-2, -1], -1),
        ([1, 2, 3, 4, 5], 15),
        ([-1, -2, -3, -4], -1),
        ([3, -2, 5, -1, 6], 11),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4, 10], 15),
        ([0, 0, 0, 0], 0),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            result = max_subarray(nums[:])
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: max_subarray({nums}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
