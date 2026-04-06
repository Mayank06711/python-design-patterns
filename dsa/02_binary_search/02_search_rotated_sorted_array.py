"""
PROBLEM: Search in Rotated Sorted Array
LeetCode #33: https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is:
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 to become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

CONSTRAINTS:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED:
COMPLETED:
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: question want me to return the index of ele which is equal to target 
# 2. HOW: there are two algo: 1: iterate on array and find target return index else -1 , 2: since array is rortated and sorted it means now there are two arrays within one array both soreted and now when we cal the middle we have to check : First we have calculated the middle right now we will check with the middle whether the target is less than or greater than the value at the middle if target is less than middle OK now what should be actually happening we should bring to middle but since the array can be rotated so we know there will be a pivot so we we are not going to find here what I will check we will checked whether the middle is greater than its left value and lesser than its right value If that holds it means till now we are in the position where a race sorted So I will simply left pointer to right because the target was less than valued metal and we need to go right and if but the left value is less than and the right value is also less than middle it means this is the pivot and here there can be two case either we bring left to middle plus one or we bring right to middle minus one so we will in there will be two pass solutions so in first pass we will always make sure that left goes to middle one and in the second pass we will always make sure right goes to middle middle one in this case where middle is the pivot point so there will be 2 pass and we will be able to find the solution
# 3. EDGE CASES: What can be age each case I don't think my problem cannot handle any edge case but edge case is like arrays already it is not rotated and it can be like when it was rotated but same as the number of elements in the array so this will be the same array
# 4. COMPLEXITY: Time O(?), Space O(?) 1: O(n) , s.c O(1), 2: 2*log(n) s.c O(1)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def search(nums, target):
    left, right = 0, len(nums) -1
    while(left<= right):
        middle = left + (right - left)//2
        if nums[middle] == target:
            return middle
        if nums[left] <= nums[middle]: # left is sorted
            if target >= nums[left] and target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else: # right sorted
            if target <= nums[right] and target > nums[middle]: 
                left = middle + 1
            else:
                right = middle -1
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
