"""
PROBLEM: Daily Temperatures
LeetCode #739: https://leetcode.com/problems/daily-temperatures/

Given an array of integers `temperatures` representing daily temperatures,
return an array `answer` such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature.

If there is no future day with a warmer temperature, set answer[i] = 0.

CONSTRAINTS:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 5:51 PM, Apr 6, 2026
COMPLETED: 6:42 PM, Apr 6, 2026
ATTEMPT: 2
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT:  Needs to know like question is I need to answer the day which is warmer than today it can be tomorrow day after tomorrow Day after tomorrow's tomorrow 
# 2. HOW:  1# two loops inside start from i+1 to find next warmer day 2: we take a stack and answer array with size n and prefilled values = 0, and then iterate on given array and in eacjh iteration we keep checking if stack is not empty and stackk top ele is less than current ele if yes then keep poping till curr ele is greater tha top ele and on each pop we store answer by current i - (stored ele index) and store in answer 
# 3. EDGE CASES: no days exist answer 0, decreasing array no answer , one elemenet
# 4. COMPLEXITY: Time O(?), Space O(?):1: O(n^2), O(1) 2: O(n), O(n)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def daily_temperatures(nums):
    n = len(nums)
    stack = []
    answer = [0]*n
    for i in range(n):
        while(stack and nums[i] > nums[stack[-1]]):
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return answer
                


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (temperatures, expected)
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
        ([30,40,50,60], [1,1,1,0]),
        ([60,50,40,30], [0,0,0,0]),
        ([50,50,50,50], [0,0,0,0]),
        ([72], [0]),
        ([71, 73], [1, 0]),
        ([73, 71], [0, 0]),
        ([30, 30, 30, 30, 100], [4, 3, 2, 1, 0]),
        ([80, 70, 60, 70, 80, 90], [5, 3, 1, 1, 1, 0]),
        ([70, 80, 70, 80, 70], [1, 0, 1, 0, 0]),
    ]

    passed = 0
    total = len(tests)

    for i, (temps, expected) in enumerate(tests, 1):
        try:
            result = daily_temperatures(temps[:])
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: daily_temperatures({temps}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
