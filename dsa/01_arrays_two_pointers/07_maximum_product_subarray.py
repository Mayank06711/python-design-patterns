"""
PROBLEM: Maximum Product Subarray
LeetCode #152: https://leetcode.com/problems/maximum-product-subarray/
TRACK: A (Primary — Arrays)

Given an integer array nums, find a subarray that has the largest product,
and return the product.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [2, 3, -2, 4]
    Output: 6
    Explanation: [2, 3] has the largest product 6.

Example 2:
    Input: nums = [-2, 0, -1]
    Output: 0
    Explanation: The result cannot be 2, because [-2, -1] is not a subarray.

CONSTRAINTS:
- 1 <= len(nums) <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray fits in a 32-bit integer

HINT: You already solved Maximum Subarray (Kadane's). This is similar but
multiplication has a twist — think about what happens with negative numbers.

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 4:08 PM, Mar 26, 2026
COMPLETED: 1:45 AM, Mar 28, 2026
ATTEMPT: 4+ (4/12 → 3/12 → 8/12 → 12/12)
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: Question is very straight forward it says that out of every summaries of given we need to return the maximum product of the I mean which pro which subway gives the maximum product
# 2. HOW: There are two possible ways one when you use both brute force and calculate my exam regular product of each, Another is where you use 3 variables one as global maxi another as previous min and previous Max and you run a loop where you calculate three things previous which will be equals to minimum of the current element into minimum of element the elemented index, product of element and the previous minimum Same goes for maximum and then for calculating the global maximum You will do what you will calculate the maximum of all these three That will be the maximum Where maxima previous Max and previous along with global maximum start with 0
# 3. EDGE CASES: I don't think there's any age case to my solution
# 4. COMPLEXITY: 1sr O(n^2) and 2nd have O(n)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def max_product_subarray(nums):
    maxi, prev_min, prev_max = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        worst_Case = prev_min
        best_case = prev_max
        prev_max = max(max(nums[i], best_case*nums[i]), worst_Case*nums[i])
        prev_min = min(min(nums[i], worst_Case*nums[i]), best_case*nums[i])
        if maxi < max(nums[i], max(prev_max, prev_min)):
            maxi =  max(nums[i], max(prev_max, prev_min))
    return maxi




# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2, 3, -4], 24),
        ([0, 2], 2),
        ([-2], -2),
        ([2, -5, -2, -4, 3], 24),
        ([-1, -2, -3, 0], 6),
        ([1, 2, 3, 4], 24),
        ([0, 0, 0], 0),
        ([-2, -3, 7], 42),
        ([2, -1, 1, 1], 2),
        ([-4, -3, -2], 12),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            result = max_product_subarray(nums[:])
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: max_product_subarray({nums}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
