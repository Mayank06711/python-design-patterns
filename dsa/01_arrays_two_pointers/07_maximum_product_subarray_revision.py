"""
REVISION: Maximum Product Subarray
LeetCode #152: https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous subarray that has
the largest PRODUCT, and return the product.

Examples:
  [2,3,-2,4] → 6 (subarray [2,3])
  [-2,0,-1] → 0
  [-2,3,-4] → 24 (subarray [-2,3,-4])

Constraints:
- 1 <= len(nums) <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix is guaranteed to fit in 32-bit int

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
REVISION OF: Session 11 (scored 5/10)
DUE DATE: Mar 31, 2026
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?) question ask for returning maximum product of subarray from a given array
# 2. HOW: (step-by-step algorithm) # 1 generate all subarray then cal product of each then find maxi and return, # take three pointers maxi, wors_Case and ebst_Case and now we find each of these in each iteration as when there is a negative ele (arr[i]) it can make biggest product to lowest and lowest to biggest so we have to track all three ele itself and these tow product to cal maxi out of these three candidates
# 3. EDGE CASES: (what could go wrong?) # it has all 0 we iterate but answer is always 0,
# 4. COMPLEXITY: (time and space)# 1st algo takes O(n^2) + O(n) , s.c O(n)
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def max_product(nums):
    if len(nums)==1:
        return nums[0]
    prev_maxi, prev_min = nums[0], nums[0]
    maxi = nums[0]
    for i in range(1, len(nums), 1):
        prev_max_temp = prev_maxi
        prev_maxi = max(nums[i], max(prev_min*nums[i], nums[i]*prev_maxi))
        prev_min = min(nums[i], min(prev_max_temp*nums[i], prev_min*nums[i]))
        maxi = max(maxi, max(prev_maxi, prev_min))
    return maxi
        





# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2], -2),
        ([2, -5, -2, -4, 3], 24),
        ([0, 2], 2),
        ([3, -1, 4], 4),
        ([-2, 3, -4], 24),
        ([2, 3, -2, 4, -1], 48),
        ([-1, -2, -3, -4], 24),
        ([0, -1, 4, -2, 3], 24),
        ([-4, -3, -2], 12),
        ([1, 0, -1, 2, 3, -5, -2], 60),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            result = max_product(nums[:])
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: max_product({nums}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  REVISION CLEARED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
