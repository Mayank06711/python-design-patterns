"""
PROBLEM: Next Greater Element I
LeetCode #496: https://leetcode.com/problems/next-greater-element-i/

The next greater element of some element x in an array is the first greater
element that is to the right of x in the same array.

You are given two DISTINCT 0-indexed integer arrays nums1 and nums2, where
nums1 is a SUBSET of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
and determine the next greater element of nums2[j] in nums2. If there is no
next greater element, the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next
greater element as described above.

Example 1:
  Input:  nums1 = [4,1,2], nums2 = [1,3,4,2]
  Output: [-1, 3, -1]
  Explanation:
    - For nums1[0]=4, next greater in nums2 after index 2 is none -> -1
    - For nums1[1]=1, next greater in nums2 after index 0 is 3 -> 3
    - For nums1[2]=2, next greater in nums2 after index 3 is none -> -1

Example 2:
  Input:  nums1 = [2,4], nums2 = [1,2,3,4]
  Output: [3, -1]

CONSTRAINTS:
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are UNIQUE
- All integers in nums1 also appear in nums2

PATTERN: Monotonic Stack (child of Daily Temperatures #739)
DIFFICULTY: Easy
TIME LIMIT: 5 minutes
STARTED:   2026-04-12 12:57:53
COMPLETED: 2026-04-12 16:16:09
ATTEMPT:   1
SCORE:     7/10 (Correctness 4 + Time 1 + Hints 1 + Quality 1)
"""


# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: <Restate problem in one line, your own words> question wants me to return next greater ele of each ele in nums1 whihc is subset of nums2
# 2. HOW: <Numbered algorithm steps — specific, not vague> algo 1, we do O(n2) loop inefficiet, algo2, : we have a stack and we iterate over nums2 (bcz nums1 is subset of nums2) in each iteration we check if the top ele in stack is greater than current ele then its next greater if not then it doesn`t have greater 
# 3. EDGE CASES: <What could go wrong?> array is increasing or decreasing or same ele 
# 4. COMPLEXITY: Time O(?), Space O(?) O(n), s.c O(n) for stack


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    st = []
    lookup_table =  {}
    ans = [-1]*len(nums1)
    for i in range(len(nums2)):
        while(st and nums2[i] > st[-1]):
            lookup_table[st[-1]] =  nums2[i]
            st.pop()
        st.append(nums2[i])
    for i, v in enumerate(nums1):
        ans[i] = lookup_table.get(v,-1)
    return ans
    



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================
def run_tests():
    passed = 0
    total = 10

    # Test 1: classic example from problem
    result = next_greater_element([4, 1, 2], [1, 3, 4, 2])
    if result == [-1, 3, -1]:
        print("  [PASS] Test 1: [4,1,2],[1,3,4,2] -> [-1,3,-1]")
        passed += 1
    else:
        print(f"  [FAIL] Test 1: got {result}, expected [-1,3,-1]")

    # Test 2: second example from problem
    result = next_greater_element([2, 4], [1, 2, 3, 4])
    if result == [3, -1]:
        print("  [PASS] Test 2: [2,4],[1,2,3,4] -> [3,-1]")
        passed += 1
    else:
        print(f"  [FAIL] Test 2: got {result}, expected [3,-1]")

    # Test 3: single element, no greater
    result = next_greater_element([1], [1])
    if result == [-1]:
        print("  [PASS] Test 3: single element -> [-1]")
        passed += 1
    else:
        print(f"  [FAIL] Test 3: got {result}, expected [-1]")

    # Test 4: all strictly decreasing, no answer exists
    result = next_greater_element([4, 3, 2, 1], [4, 3, 2, 1])
    if result == [-1, -1, -1, -1]:
        print("  [PASS] Test 4: strictly decreasing -> [-1]*4")
        passed += 1
    else:
        print(f"  [FAIL] Test 4: got {result}, expected [-1,-1,-1,-1]")

    # Test 5: all strictly increasing
    result = next_greater_element([1, 2, 3], [1, 2, 3, 4])
    if result == [2, 3, 4]:
        print("  [PASS] Test 5: strictly increasing")
        passed += 1
    else:
        print(f"  [FAIL] Test 5: got {result}, expected [2,3,4]")

    # Test 6: nums1 in reversed order from nums2
    result = next_greater_element([3, 2, 1], [1, 2, 3, 4])
    if result == [4, 3, 2]:
        print("  [PASS] Test 6: nums1 reversed from nums2")
        passed += 1
    else:
        print(f"  [FAIL] Test 6: got {result}, expected [4,3,2]")

    # Test 7: last element never has a greater
    result = next_greater_element([4], [1, 2, 3, 4])
    if result == [-1]:
        print("  [PASS] Test 7: last element in nums2 -> -1")
        passed += 1
    else:
        print(f"  [FAIL] Test 7: got {result}, expected [-1]")

    # Test 8: query same element by two different positions
    result = next_greater_element([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7])
    if result == [7, 7, 7, 7, 7]:
        print("  [PASS] Test 8: everything maps to 7")
        passed += 1
    else:
        print(f"  [FAIL] Test 8: got {result}, expected [7,7,7,7,7]")

    # Test 9: zigzag pattern
    result = next_greater_element([5, 1, 3], [1, 5, 2, 3, 4])
    if result == [-1, 5, 4]:
        print("  [PASS] Test 9: zigzag -> [-1,5,4]")
        passed += 1
    else:
        print(f"  [FAIL] Test 9: got {result}, expected [-1,5,4]")

    # Test 10: nums1 is a single element in the middle
    result = next_greater_element([13], [1, 2, 13, 11, 12, 15])
    if result == [15]:
        print("  [PASS] Test 10: [13] -> [15]")
        passed += 1
    else:
        print(f"  [FAIL] Test 10: got {result}, expected [15]")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")


if __name__ == "__main__":
    run_tests()
