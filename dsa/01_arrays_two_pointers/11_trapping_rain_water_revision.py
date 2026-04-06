"""
Trapping Rain Water — REVISION
LeetCode #42: https://leetcode.com/problems/trapping-rain-water/

REVISION REQUIREMENT: Solve using TWO-POINTER approach — O(n) time, O(1) space.
NO prefix arrays allowed. Only constant extra space.

Original score: 6/10 (Apr 1, 2026)
Due date: Apr 4, 2026 (OVERDUE)
Must score >= 8/10 to clear.

Quick refresher (DO NOT read your old solution):
- water[i] = min(left_max, right_max) - height[i]
- You already know the prefix-array O(n) space version
- Challenge: how can you compute the same thing WITHOUT storing left_max[] and right_max[]?

Hint (use only if stuck after 5 min):
  Think about what information you ACTUALLY need at each position.
  If left_max < right_max, does the exact value of right_max matter?

DIFFICULTY: Hard
TIME LIMIT: 10 minutes
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?)
# 2. HOW: (step-by-step — two pointers, O(1) space)
# 3. WHY does two-pointer work? (key insight)
# 4. COMPLEXITY: (time and space)
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================

def trap(height):
    left_max = 0
    right_max = 0
    left, right = 0, len(height)-1
    total_water = 0
    while(left < right):
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            total_water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total_water +=  right_max - height[right]
            right -= 1
    return total_water



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
