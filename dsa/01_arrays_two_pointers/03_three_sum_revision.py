"""
REVISION: 3Sum
LeetCode #15: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

CONSTRAINTS:
- 3 <= len(nums) <= 3000
- -10^5 <= nums[i] <= 10^5
- No duplicate triplets in output

DIFFICULTY: Medium
TIME LIMIT: 12 minutes
STARTED: 6:50 PM (March 22, 2026)
COMPLETED: 7:00 PM (March 22, 2026)
ATTEMPT: 1
REVISION OF: Day 5 — Mar 18 (scored 5/10)
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================
# algo-1
# i will have an ans empty list to store triplets
# i will sort the array
# loop over given array (with ind i = 0) so this value remains fixed 
# skip if prev and curr value is same (index must be iterable that is i>0 <n)
# intialise left = i + 1 and right = len(nums) - 1
# loop till left  < right -> prob becomes 2 pointer with target = nums[i] giving combiend sum 0
# if total sum is 0 we can store the triplet and we don`t need to sort bcz its already sorted and increase left and right-
# now we can skip duplcaited by looping till left less than right and val of nums[left] and its left-1 is same 
# similar loop for right side skip
# now if total sum < 0 -> we move left + to increase sum
# if total sum > 0 we decrease right to descrease sum
# return ans
# t.c-> O(n)*O(n)
# s.c-> O(1)



# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def three_sum(nums):
    nums.sort()
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right]  + nums[i] == 0:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif nums[left] + nums[right]  + nums[i] < 0:
                left += 1
            else:
                right -= 1
    return ans


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([1, -1, -1, 0], [[-1, 0, 1]]),
        ([-1, 0, 1, 0], [[-1, 0, 1]]),
        ([-4, -2, -1, 0, 1, 2, 3, 4], [[-4, 0, 4], [-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-1, -1, -1, 2], [[-1, -1, 2]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            result = three_sum(nums[:])
            # Sort inner lists and outer list for comparison
            result_sorted = sorted([sorted(t) for t in result])
            expected_sorted = sorted([sorted(t) for t in expected])
            if result_sorted == expected_sorted:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: three_sum({nums}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
