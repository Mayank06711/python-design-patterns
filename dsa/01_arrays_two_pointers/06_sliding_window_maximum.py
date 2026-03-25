"""
PROBLEM: Sliding Window Maximum
LeetCode #239: https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums and an integer k (the window size).
There is a sliding window of size k which moves from the very left of the
array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves one position to the right.

Return a list of the maximum value in each window position.

Example:
    nums = [1,3,-1,-3,5,3,6,7], k = 3

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7      3
     1 [3  -1  -3] 5  3  6  7      3
     1  3 [-1  -3  5] 3  6  7      5
     1  3  -1 [-3  5  3] 6  7      5
     1  3  -1  -3 [5  3  6] 7      6
     1  3  -1  -3  5 [3  6  7]     7

    Output: [3, 3, 5, 5, 6, 7]

CONSTRAINTS:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

DIFFICULTY: Hard
TIME LIMIT: 12 minutes
STARTED: 4:25 PM, Mar 25, 2026
COMPLETED:
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: Question is asking that when there is a array and given an integer K which is actually the size of the window so at a time the window moves like there will be a fixed window which will move on the array from left to extreme right read and inside each window I need to find out the maximum value within that window 
# 2. HOW: 
# 3. EDGE CASES:
# 4. COMPLEXITY:


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (nums, k, expected)
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
        ([9, 11], 2, [11]),
        ([4, 3, 2, 1], 2, [4, 3, 2]),
        ([1, 2, 3, 4], 2, [2, 3, 4]),
        ([1, 1, 1, 1, 1], 3, [1, 1, 1]),
        ([7, 2, 4], 2, [7, 4]),
        ([-7, -8, 7, 5, 7, 1, 6, 0], 4, [7, 7, 7, 7, 7]),
        ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, k, expected) in enumerate(tests, 1):
        try:
            result = max_sliding_window(nums[:], k)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: max_sliding_window({nums}, {k}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
