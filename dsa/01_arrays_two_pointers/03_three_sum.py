"""
PROBLEM: 3Sum
LeetCode #15: https://leetcode.com/problems/3sum/
Striver SDE Sheet: Arrays

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

The ORDER of the triplets in the output doesn't matter, but each triplet
must be sorted in non-decreasing order.

Constraints:
- 3 <= len(nums) <= 3000
- -100000 <= nums[i] <= 100000

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 2026-03-18 13:30 IST
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================
# OK so there can the one off approach I can think is I am unable to think of brute force that I should have been because in interview that makes sense like you go from the worst time complexity to increase in time complexity like 10 square to N to log in you know but solution I can think of is we have two The outer loop is for I the inner loop is with J and K where J = to I plus one and game is equals length of the array minus one that is at the extreme right of the So here J and K plays left and right pointers of the remaining arr after like remaining remains the array after the I pointer like starting with I one and since the condition is like IJ and K should never be equal
# So the Eye loop will be for loop while the J and K loop will be a while loop which will run inside for loop with condition S J is less than K and we will submit the pointer here ith will be fixed JK will move towards each
# Now some their sums would be equals to zero and eye is fixed Show their song can only be equals to when the J and K they are same as ith value What I mean is if X + Y + Z = to 0 then Y + Z = to - X that they should be same the their model that means the magnitude should be same So here the value is X and the problem will become to 2 finding value of I sorry J and K which should be equals to i
# So how the looping wheel work is like from that for loop of for value of I we go to the inner lobe while J is less than K and find out the sum of J and K Check if it is equals to the magnitude of i
# If the sum is Less than the value of I But to move the pointers I mean J and K since this array is not sorted the remaining array we cannot definitely say that Uh if the sum is less than I we will move J two towards or if sum is greater than at I we will move K towards J so to solve this I believe the first step should be to sort the rain increasing order I mean non decreasing order
#  Before restoring the triplets we will take have to take a hass off the triplets which will take the triplet as key and value one so that there is no triplet kept in final list
# Now to store the triplets we will have to take a list List of list actually Where that triplets will be a smaller list which will be inside the main list We will always sort the triplets before St in non decreasing order
# At the end we will return the output
# t.c -> O(n*log(n) -> for  sorting + o(n^2) for triplets sorting worst case we find multiple triplets, S.c-> o(n) + O(n) for hashmap


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def three_sum(nums):
    ans = [] 
    nums.sort()
    for ind, val in enumerate(nums):
        j = ind + 1
        k = len(nums) - 1
        if ind > 0 and nums[ind] == nums[ind-1]:
            continue
        while j < k: 
            total = nums[j] + nums[k] + val
            if total < 0:
                j +=  1
            elif total > 0:
                k -= 1
            else:
                ans.append([val, nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]: 
                    j += 1  # skip duplicate j
                while j < k and nums[k] == nums[k-1]: 
                    k -= 1  # skip duplicate k 
                j += 1
                k -= 1
    return ans
            



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (nums, expected_triplets)
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-1, 0, 1, 0], [[-1, 0, 1]]),
        ([1, 2, -2, -1], []),
        ([-4, -1, -1, 0, 1, 2], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([-1, -1, -1, 2], [[-1, -1, 2]]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            result = three_sum(nums)
            # Sort both for comparison (order of triplets doesn't matter)
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
