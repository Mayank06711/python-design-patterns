"""
Binary Search
LeetCode #704: https://leetcode.com/problems/binary-search/

Given a SORTED array of integers nums and an integer target, return the
index of target if it exists, otherwise return -1.

You must write an algorithm with O(log n) runtime complexity.

Examples:
  nums = [-1,0,3,5,9,12], target = 9  ->  4
  nums = [-1,0,3,5,9,12], target = 2  ->  -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All integers in nums are unique
- nums is sorted in ascending order

DIFFICULTY: Easy
TIME LIMIT: 5 minutes
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?)   question wants me to return the index of ele which is equal to target 
# 2. HOW: (step-by-step algorithm) algo 1 we iterate over complete array matching every array ele with target if found we return index algo 2:we take two pointer one at index 0 and other at n-1 and cal middle now loop over array until left<= right and in each iteration keep comp middle and target id middle is < target move left to middle + 1 as its sorted and its guarnteed tjhat if lesss than middlewa it can`t be on left of middle ` same for right then if we found middle == target we return middle index
# 3. EDGE CASES: (what could go wrong?) array does not have ele repeating ele 
# 4. COMPLEXITY: (time and space)  O(n) 2: O(logn) s.c ()
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================

def binary_search(nums, target):
    left, right = 0, len(nums)-1
    while(left <= right):
        middle = left + (right - left)//2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            right = middle-1
        elif  target > nums[middle]:
            left = middle + 1
    return -1



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([2, 5], 5, 1),
        ([2, 5], 2, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 9),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 5),
        ([-10, -5, 0, 3, 7], -5, 1),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, target, expected) in enumerate(tests, 1):
        try:
            result = binary_search(nums[:], target)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: binary_search({nums}, {target}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
