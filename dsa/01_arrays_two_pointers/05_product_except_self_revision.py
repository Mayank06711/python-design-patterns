"""
PROBLEM: Product of Array Except Self (REVISION)
LeetCode #238: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and WITHOUT using the division operation.

CONSTRAINTS:
- 2 <= len(nums) <= 10^5
- -30 <= nums[i] <= 30
- Product of any prefix/suffix fits in 32-bit integer
- O(n) time required
- NO division allowed

FOLLOW-UP: Can you solve it in O(1) extra space? (The output array does not count as extra space.)

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 1:08 AM, Mar 25, 2026
COMPLETED: 12:55 PM, Mar 25, 2026
ATTEMPT: REVISION (original: 5/10, Mar 22, 2026) → CLEARED 10/10
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: Question ask me to return the product All elements except itself that mean if I am at place so the I value should be the product of every other element except this I value in the real list
# 2. HOW: I will have to calculate left product array and right product then any element I the product of left and right of any element I will be from left into product from
# 3. EDGE CASES: no
# 4. COMPLEXITY: tc=O(n) + Sc(1)

# algo 1 brute force O(n^2)
# algo 2
# two arrays left and right product then cal produ except self from them
#algo 3
# cal left product in ans array nowin other loop cal running r prod from end side and mult with corr left produ val and save it to ans itself 

# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def product_except_self(nums):
    n = len(nums)
    ans = []
    r_prod = 1
    for i in range(n):
        if i == 0:
            ans.append(1)
        else:
            ans.append(ans[i-1]*nums[i-1])
    for i in range(n-1, -1, -1):
        if i == n-1:
            r_prod = 1
        else:
            r_prod = r_prod * nums[i+1]
        ans[i] = ans[i] * r_prod
    return ans


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (input, expected)
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([0, 0], [0, 0]),
        ([1, 0, 3, 4], [0, 12, 0, 0]),
        ([5, -1, 2, -3], [6, -30, 15, -10]),
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([-1, -1, -1, -1], [-1, -1, -1, -1]),
        ([10, 0, 0, 5], [0, 0, 0, 0]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            result = product_except_self(nums[:])
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: product_except_self({nums}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
