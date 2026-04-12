"""
PROBLEM: Next Greater Element II
LeetCode #503: https://leetcode.com/problems/next-greater-element-ii/

Given a CIRCULAR integer array nums (i.e., the next element of nums[nums.length - 1]
is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its
traversing-order next in the array, which means you could search circularly
to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
  Input:  nums = [1, 2, 1]
  Output: [2, -1, 2]
  Explanation:
    - nums[0]=1: next greater is 2 (at index 1)
    - nums[1]=2: no greater element exists anywhere -> -1
    - nums[2]=1: wrap around to index 0 (value 1), then index 1 (value 2) -> 2

Example 2:
  Input:  nums = [1, 2, 3, 4, 3]
  Output: [2, 3, 4, -1, 4]

CONSTRAINTS:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- Values are NOT unique (unlike NGE I)

PATTERN: Monotonic Stack (child of Daily Temperatures / NGE I)
         The twist: CIRCULAR traversal.

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED:   2026-04-12 16:48:25 (paused for circular/rotation detour)
COMPLETED: 2026-04-12 17:02:40
ATTEMPT:   1
SCORE:     9/10 (Correctness 4 + Time 3 + Hints 1 + Quality 1)
"""


# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: <Restate problem in one line, your own words> question want to find next greater ele for ele at i in a cyclid array
# 2. HOW: <Numbered algorithm steps — specific, not vague># we start our loop from i = 0 till n-1 this is first pass and keep checking at each iteration as:
# st and curr > st.top is yes then store it in ans and pop else append in both case
# 2nd pass again 0 to n-1 this time we only compare and pop not appen 
# 3. EDGE CASES: <What could go wrong?> decreasing array, no ele in array 
# 4. COMPLEXITY: Time O(?), Space O(?) (n) , s.c (N) (stack)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def next_greater_elements(nums: list[int]) -> list[int]:
    st = []
    n = len(nums)
    ans = [-1]*n
    for ind in range(2*n):
        i = ind%n
        while(st and nums[i] > nums[st[-1]]):
            ans[st[-1]] = nums[i]
            st.pop()
        if ind < n:
            st.append(i)

    return ans
# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================
def run_tests():
    passed = 0
    total = 10

    # Test 1: LC example 1
    result = next_greater_elements([1, 2, 1])
    if result == [2, -1, 2]:
        print("  [PASS] Test 1: [1,2,1] -> [2,-1,2]")
        passed += 1
    else:
        print(f"  [FAIL] Test 1: got {result}, expected [2,-1,2]")

    # Test 2: LC example 2
    result = next_greater_elements([1, 2, 3, 4, 3])
    if result == [2, 3, 4, -1, 4]:
        print("  [PASS] Test 2: [1,2,3,4,3] -> [2,3,4,-1,4]")
        passed += 1
    else:
        print(f"  [FAIL] Test 2: got {result}, expected [2,3,4,-1,4]")

    # Test 3: all same elements
    result = next_greater_elements([5, 5, 5, 5])
    if result == [-1, -1, -1, -1]:
        print("  [PASS] Test 3: all equal -> all -1")
        passed += 1
    else:
        print(f"  [FAIL] Test 3: got {result}, expected [-1,-1,-1,-1]")

    # Test 4: single element
    result = next_greater_elements([1])
    if result == [-1]:
        print("  [PASS] Test 4: single element -> [-1]")
        passed += 1
    else:
        print(f"  [FAIL] Test 4: got {result}, expected [-1]")

    # Test 5: two elements
    result = next_greater_elements([1, 2])
    if result == [2, -1]:
        print("  [PASS] Test 5: [1,2] -> [2,-1]")
        passed += 1
    else:
        print(f"  [FAIL] Test 5: got {result}, expected [2,-1]")

    # Test 6: circular wrap-around required
    result = next_greater_elements([3, 1, 2])
    if result == [-1, 2, 3]:
        print("  [PASS] Test 6: [3,1,2] -> [-1,2,3]  (wrap required)")
        passed += 1
    else:
        print(f"  [FAIL] Test 6: got {result}, expected [-1,2,3]")

    # Test 7: strictly decreasing (circular gives some answers)
    result = next_greater_elements([5, 4, 3, 2, 1])
    if result == [-1, 5, 5, 5, 5]:
        print("  [PASS] Test 7: [5,4,3,2,1] -> [-1,5,5,5,5]")
        passed += 1
    else:
        print(f"  [FAIL] Test 7: got {result}, expected [-1,5,5,5,5]")

    # Test 8: strictly increasing (last element wraps to -1)
    result = next_greater_elements([1, 2, 3, 4, 5])
    if result == [2, 3, 4, 5, -1]:
        print("  [PASS] Test 8: [1,2,3,4,5] -> [2,3,4,5,-1]")
        passed += 1
    else:
        print(f"  [FAIL] Test 8: got {result}, expected [2,3,4,5,-1]")

    # Test 9: duplicates with circular need
    result = next_greater_elements([2, 1, 2, 1])
    if result == [-1, 2, -1, 2]:
        print("  [PASS] Test 9: [2,1,2,1] -> [-1,2,-1,2]")
        passed += 1
    else:
        print(f"  [FAIL] Test 9: got {result}, expected [-1,2,-1,2]")

    # Test 10: negatives
    result = next_greater_elements([-1, -2, -3, 0])
    if result == [0, 0, 0, -1]:
        print("  [PASS] Test 10: negatives -> wrap to 0 where possible")
        passed += 1
    else:
        print(f"  [FAIL] Test 10: got {result}, expected [0,0,0,-1]")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
