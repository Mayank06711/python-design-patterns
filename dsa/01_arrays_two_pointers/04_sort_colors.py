"""
PROBLEM: Sort Colors (Dutch National Flag)
LeetCode #75: https://leetcode.com/problems/sort-colors/
Striver SDE Sheet: Arrays

Given an array nums with n objects colored red, white, or blue,
sort them IN-PLACE so that objects of the same color are adjacent,
with the colors in the order red (0), white (1), and blue (2).

You must solve this problem WITHOUT using the library's sort function.

CONSTRAINTS:
- Must be done IN-PLACE (modify the array, return nothing)
- Only values 0, 1, 2 in the array
- 1 <= len(nums) <= 300

FOLLOW-UP: Could you come up with a one-pass algorithm using only constant extra space?
(This is the real interview question — one pass, O(1) space)

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 12:33 AM (March 19, 2026)
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================
# so the brute force solution that clicks in my mind is like:
# I will create three empty arrays Our I should say and name them as zeros ones and twos Then he started rioting over the main givenery If I found the zero I will put it inside 0 array if I found one I will put it in once array if I found it 2 I will put it that in two array of 2
# now what I will do I will run three loops starting with looping over the zeros and keep it like keep it rating out the zeros array and putting it is from the first place like the zeroth index of the given array replacing it with the zeros once all zeros are filled we will do the same with one`s array and 2s array 
# I am finally return the mutated list because now it is sorted with zero one and two
# T.c for this is O(n) + O(n) (bcz we iterated twice ) =>  O(n)
# SC -> O(n) bcz we have taken an array of same size

# 2nd approach with O(1)
# in this we extra arrays we will take three variables namely zero1 and 2 We loop over the The first time we count the frequency of zero1 and 2 Then on second time we like then we will have 3 loops for 140142 and one one and we will fill with zeros equals to number of zeros we count then one equals to number of ones we count then two equals to number of two we count For example let us assume an array arrays like 11022 so in if we sort this the answer should be 01122 So according to this approach first loop will give us the values of the variable where 0 will be 11 will be 2 and 2 will be 2 Then we will we make three loops while with a global pointer I equals to zero to put the variables in like the value in the array and it will first start at I less than zero We will fill the zero increase die then we go and I less than one we fill the one increase the I then we go and fill the 2

# 3rd one
# we take three pointers low , separator and high
# rules wil be like everythin after high is 2, everything below including low is 0 and in between them its 1
# we start a loop wit condition separator <= high 
# check if separator is zero it needs to go to left side and move on if its 1 just move if its two swap with high (when high val is not eqaual to 2)

# T.c -> O(n) -> 1 pass and S.C -> O(1) only pointer variables nothing else.


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def sort_colors(nums):
    low = 0
    separator = 0
    high = len(nums) - 1
    while(separator <= high):
        if nums[separator] == 0:
            nums[low], nums[separator] = nums[separator], nums[low]
            low += 1
            separator +=1
        elif nums[separator] == 1:
            separator += 1
        else:
            nums[separator], nums[high] = nums[high], nums[separator]
            high -= 1


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (input, expected)
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2, 2, 2, 0, 0, 0], [0, 0, 0, 2, 2, 2]),
        ([1, 0], [0, 1]),
        ([0, 0, 0], [0, 0, 0]),
        ([2, 1, 0, 2, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        ([1, 2, 0, 1, 2, 0], [0, 0, 1, 1, 2, 2]),
        ([0, 2, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 2, 2]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            nums_copy = nums[:]
            sort_colors(nums_copy)
            if nums_copy == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: sort_colors({nums}) = {nums_copy}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
