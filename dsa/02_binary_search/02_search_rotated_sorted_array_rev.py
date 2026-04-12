"""
REVISION: Search in Rotated Sorted Array
==========================================

LeetCode #33
Original: Session 15 (Apr 3) — scored 4/10, 3 bugs, heavy hints.
This is your clean-slate redo.

STARTED:   2026-04-11 17:40:36
COMPLETED: 2026-04-11 17:54:58
ATTEMPT:   REVISION — 1st run 12/12 (latent boundary bug on right branch)
SCORE:     8/10 (Correctness 3 + Time 3 + Hints 1 + Quality 1)
TIME:      ~7 min / 8 min (Medium) — under budget

PROBLEM:
--------
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is:
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 to become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

CONSTRAINTS:
  - 1 <= nums.length <= 5000
  - -10^4 <= nums[i] <= 10^4
  - All values of nums are unique
  - nums is an ascending array that is possibly rotated
  - O(log n) runtime required. No linear scan.
  - No peeking at the original file.
"""


# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT:
# 2. HOW:
# 3. EDGE CASES:
# 4. COMPLEXITY: Time O(?), Space O(?)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def search(nums, target):
    left, right = 0, len(nums)-1
    while(left <= right):
        middle = left + (right - left)//2
        if target == nums[middle]:
            return middle
        if nums[left] <= nums[middle]:# left sorted     
            if target <= nums[middle] and target >= nums[left]:
                right = middle - 1
            else:
                left = middle + 1 # means it isn right hal
        else:
            if target <= nums[right] and target >= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1 
    return -1

# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================
def run_tests():
    passed = 0
    total = 12

    # Test 1: basic rotated, target in right portion
    result = search([4, 5, 6, 7, 0, 1, 2], 0)
    if result == 4:
        print("  [PASS] Test 1: [4,5,6,7,0,1,2] target=0 → 4")
        passed += 1
    else:
        print(f"  [FAIL] Test 1: got {result}, expected 4")

    # Test 2: basic rotated, target in left portion
    result = search([4, 5, 6, 7, 0, 1, 2], 5)
    if result == 1:
        print("  [PASS] Test 2: [4,5,6,7,0,1,2] target=5 → 1")
        passed += 1
    else:
        print(f"  [FAIL] Test 2: got {result}, expected 1")

    # Test 3: target not found
    result = search([4, 5, 6, 7, 0, 1, 2], 3)
    if result == -1:
        print("  [PASS] Test 3: target=3 not in array → -1")
        passed += 1
    else:
        print(f"  [FAIL] Test 3: got {result}, expected -1")

    # Test 4: single element found
    result = search([1], 1)
    if result == 0:
        print("  [PASS] Test 4: single element found")
        passed += 1
    else:
        print(f"  [FAIL] Test 4: got {result}, expected 0")

    # Test 5: single element not found
    result = search([1], 0)
    if result == -1:
        print("  [PASS] Test 5: single element not found")
        passed += 1
    else:
        print(f"  [FAIL] Test 5: got {result}, expected -1")

    # Test 6: not rotated (already sorted)
    result = search([1, 2, 3, 4, 5], 3)
    if result == 2:
        print("  [PASS] Test 6: not rotated, target=3 → 2")
        passed += 1
    else:
        print(f"  [FAIL] Test 6: got {result}, expected 2")

    # Test 7: rotated, target is first element
    result = search([4, 5, 6, 7, 0, 1, 2], 4)
    if result == 0:
        print("  [PASS] Test 7: target is first element → 0")
        passed += 1
    else:
        print(f"  [FAIL] Test 7: got {result}, expected 0")

    # Test 8: rotated, target is last element
    result = search([4, 5, 6, 7, 0, 1, 2], 2)
    if result == 6:
        print("  [PASS] Test 8: target is last element → 6")
        passed += 1
    else:
        print(f"  [FAIL] Test 8: got {result}, expected 6")

    # Test 9: two elements rotated
    result = search([2, 1], 1)
    if result == 1:
        print("  [PASS] Test 9: [2,1] target=1 → 1")
        passed += 1
    else:
        print(f"  [FAIL] Test 9: got {result}, expected 1")

    # Test 10: pivot at end (rotated by 1)
    result = search([2, 3, 4, 5, 1], 1)
    if result == 4:
        print("  [PASS] Test 10: rotated by 1, target=1 → 4")
        passed += 1
    else:
        print(f"  [FAIL] Test 10: got {result}, expected 4")

    # Test 11: larger array
    result = search([6, 7, 8, 1, 2, 3, 4, 5], 8)
    if result == 2:
        print("  [PASS] Test 11: [6,7,8,1,2,3,4,5] target=8 → 2")
        passed += 1
    else:
        print(f"  [FAIL] Test 11: got {result}, expected 2")

    # Test 12: target just outside range
    result = search([3, 4, 5, 1, 2], 6)
    if result == -1:
        print("  [PASS] Test 12: target=6 not in array → -1")
        passed += 1
    else:
        print(f"  [FAIL] Test 12: got {result}, expected -1")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
