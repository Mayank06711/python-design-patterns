"""
Set Matrix Zeroes
LeetCode #73: https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix, if an element is 0, set its entire row and
column to 0's. You must do it IN PLACE.

Examples:
  [[1,1,1],        [[1,0,1],
   [1,0,1],   ->    [0,0,0],
   [1,1,1]]         [1,0,1]]

  [[0,1,2,0],      [[0,0,0,0],
   [3,4,5,2],  ->   [0,4,5,0],
   [1,3,1,5]]       [0,3,1,0]]

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

Follow-up:
- O(mn) space is trivial (copy matrix). Can you do O(m+n)?
- Can you do O(1) space? (use first row/col as markers)

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?)
# 2. HOW: (step-by-step algorithm)
# 3. EDGE CASES: (what could go wrong?)
# 4. COMPLEXITY: (time and space)
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================

def set_zeroes(matrix):
    pass


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        ),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ),
        (
            [[0]],
            [[0]]
        ),
        (
            [[1, 0]],
            [[0, 0]]
        ),
        (
            [[1], [0]],
            [[0], [0]]
        ),
        (
            [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 3], [0, 0, 0, 0]]
        ),
        (
            [[1, 2], [3, 4]],
            [[1, 2], [3, 4]]
        ),
        (
            [[-1, 0, -3], [0, -2, 0]],
            [[0, 0, 0], [0, 0, 0]]
        ),
        (
            [[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12]],
            [[0, 0, 0, 0], [5, 0, 0, 8], [0, 0, 0, 0]]
        ),
    ]

    passed = 0
    total = len(tests)

    for i, (matrix, expected) in enumerate(tests, 1):
        try:
            import copy
            mat = copy.deepcopy(matrix)
            set_zeroes(mat)
            if mat == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}:")
                print(f"    Input:    {matrix}")
                print(f"    Got:      {mat}")
                print(f"    Expected: {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
