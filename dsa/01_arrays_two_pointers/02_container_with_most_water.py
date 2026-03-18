"""
PROBLEM: Container With Most Water
LeetCode #11: https://leetcode.com/problems/container-with-most-water/
Striver SDE Sheet: Arrays

You are given an integer array `height` of length n. There are n vertical
lines drawn such that the two endpoints of the i-th line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container, such that
the container holds the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

Water stored = min(height[left], height[right]) * (right - left)

Constraints:
- n == len(height)
- 2 <= n <= 100000
- 0 <= height[i] <= 10000

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 2026-03-17 16:28 IST
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================
# So there can be two approaches for this one is uh Big O of N Square where what we do is since we need to calculate the maximum area we can iterate on over from my equus to zero to I equals to N minus 1 and inside that there is another loop from I equals to IJ equals to our key goes to 0 sorry J equals to I plus one tell J less than N - 1 NJ here each time we keep calculating the the formula of areas length into breadth and length we can get fry OK the G minus I we get the length For example I was zero the J will be one and the length is of one unit and height we can calculate OK the height from the now the main why we need minimum height is because let us assume at index height was three unit at at and at index one the height was five unit So we can never store water above the three unit because the water will go out spill out after the 3 3rd unit because there is no left side spouting wall to store the water But this will be a big O of N square with a space complexity big O of one so to reduce this the final answer will be to use 2 pointer approach or maximum area of histogram something I heard of this I don't remember so I will write the below steps
 #so I will write the below steps so I will write the below steps
#step -1
# intiliase two pointers -> i  = 0, and j = len of arr -1 and one var for storing area 
# iterate over array while i < j
# len of rectangl/shape which will store water  = j(right) - i(left)
# height (actual height till where we can store the water) = min(height at i , at j)
# Now question is which side of pointer will move so always the pointer where height is less will move towards higher height here we can't predict the next fight will definitely be because it can be less than let us say at zero the unit was three but at one it's two and at 4 the at the end of the vector the unit was already 5 so you know what I mean by logic you are definite that you will decrease in this case
# maxi = maximum of calculated area , prev_area (that we intialise as 0) 
#return maxi 
# T>C -> O(n) and S.C O(1)
# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def max_area(height):
    left, right = 0, len(height)-1
    maxi = 0
    while left < right:
        min_height = min(height[left], height[right])
        area = min_height*(right - left)
        maxi = max(maxi, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxi



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (height, expected_max_water)
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 8, 6, 2, 5, 4, 8, 25, 7], 49),
        ([1, 2, 4, 3], 4),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([10, 1, 1, 1, 1, 1, 1, 10], 70),
        ([1, 1, 1, 1, 1000, 1000, 1, 1], 1000),
        ([5, 2, 12, 1, 5, 3, 4, 11, 1, 9], 63),
    ]

    passed = 0
    total = len(tests)

    for i, (height, expected) in enumerate(tests, 1):
        try:
            result = max_area(height)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: max_area({height}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
