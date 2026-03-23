"""
PROBLEM: Subarray Sum Equals K
LeetCode #560: https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number
of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

CONSTRAINTS:
- 1 <= len(nums) <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
- Elements can be NEGATIVE (this is crucial — sliding window won't work!)

DIFFICULTY: Medium
TIME LIMIT: 15 minutes
STARTED: 7:02 PM (March 22, 2026)
COMPLETED: 1:54 AM (March 24, 2026)
ATTEMPT: 2
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================
# Algo  1
# generate all subaray using two loops 
# inside inner loop keep calcualting sum
# if sum ===k increase a global counter by +1
# return that counter
# t.c- > O(n^2) and S>C-> O(1)

# Algo 2 
# an empty pref sum array and a hashmap for storing sum with 0 -> 1 already in hashmap
# loop over given sum array
# check if (current sum - k) is in hashmap
# add current sum to hashmap
# if yes then add the value of (current sum - k) to the global counter
# return that counter
# t.c- > O(n) and S>C-> O(n)

# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def subarray_sum(nums, k):
    count = 0
    pref_sum = 0
    hashmap = {0:1}
    for i in nums:
        pref_sum += i
        if pref_sum - k in hashmap:
            count += hashmap[pref_sum -k]
        hashmap[pref_sum] = hashmap.get(pref_sum,0) + 1
    return count


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (nums, k, expected_count)
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 1, 1),
        ([1], 0, 0),
        ([0, 0, 0, 0], 0, 10),
        ([-1, -1, 1], 0, 1),
        ([1, -1, 1, -1], 0, 4),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
        ([1, 2, 3, -3, 1, 1, 1], 3, 6),
        ([28, 54, 7, -70, 22, 28, -30, 14], 28, 2),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, k, expected) in enumerate(tests, 1):
        try:
            result = subarray_sum(nums[:], k)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: subarray_sum({nums}, {k}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
