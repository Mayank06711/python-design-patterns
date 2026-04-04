"""
Trapping Rain Water
LeetCode #42: https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

The elevation map is represented by array height where height[i] is the
height of the bar at position i.

Examples:
  [0,1,0,2,1,0,1,3,2,1,2,1] → 6
  Explanation: bars at [0,1,0,2,1,0,1,3,2,1,2,1]
               water trapped: at index 2 (1 unit), index 4 (1), index 5 (2),
                             index 7 (1), index 9 (1) = total 6 units

  [4,2,0,3,2,5] → 9
  [3,0,2,0,4] → 7

Constraints:
- n == len(height)
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

DIFFICULTY: Hard
TIME LIMIT: 12 minutes
STARTED: Apr 1, 2026 17:30
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?) question want me to return total water trapped on each index not the area
# 2. HOW: (step-by-step algorithm) # i will loop through all index using a for loop and insde we have to calculate left_max and right_max for each element and then compare it with current if ele is <= curr[i] there won`t be any water on this index, if greater then water on this index will be min(left and right) -curr[i] and then we will add it to global water_trapped var.. but problem is do we track the right and left maximum with some data structure like hashmap with index so we don1t have to loop again and again or not?
# 3. EDGE CASES: (what could go wrong?) # array is sorted answer always 0 or only one element
# 4. COMPLEXITY: (time and space) T.c O(n for loop) + if used hashmap then O(nlogn ) s.c O(n)
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def left_maxi(ele, start, hgt):
    maxi = ele
    for j in range(start, -1, -1):
        if hgt[j] > ele:
            maxi = max(maxi, hgt[j])
    return maxi
def right_maxi(ele, start, hgt):
    maxi = ele
    for i in range(start,len(hgt),1):
        if hgt[i] > ele:
            maxi = max(maxi, hgt[i])
    return maxi

def trap(height):
    n = len(height)
    if n <=1 :
        return 0
    water_trapped = 0
    left_max = []
    left_max.append(height[0])
    right_max = []
    right_max.append(height[n-1])
    for i in range(1, n, 1):
        left_max.append(max(left_max[i-1], height[i]))
    for i in range(1,n):
        right_max.append(max(right_max[i-1], height[n-i-1]))

    for i in range(1,n):
        mini_of_left_and_right  = min(right_max[n-i-1], left_max[i])
        if mini_of_left_and_right <= height[i]:
            continue
        water_trapped += mini_of_left_and_right - height[i]
    return water_trapped
        




# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([3, 0, 2, 0, 4], 7),
        ([2, 0, 2], 2),
        ([3, 0, 0, 2, 0, 4], 10),
        ([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2], 8),
        ([5, 4, 1, 2], 1),
        ([5, 2, 1, 2, 1, 5], 14),
        ([1, 0, 1], 1),
        ([4, 2, 3], 1),
    ]

    passed = 0
    total = len(tests)

    for i, (height, expected) in enumerate(tests, 1):
        try:
            result = trap(height[:])
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: trap({height}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
