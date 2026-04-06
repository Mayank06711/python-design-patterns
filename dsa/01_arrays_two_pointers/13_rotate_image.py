"""
Rotate Image
LeetCode #48: https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees CLOCKWISE. You must do it IN PLACE.

Examples:
  [[1,2,3],        [[7,4,1],
   [4,5,6],   ->    [8,5,2],
   [7,8,9]]         [9,6,3]]

  [[5,1,9,11],      [[15,13,2,5],
   [2,4,8,10],  ->   [14,3,4,1],
   [13,3,6,7],       [12,6,8,9],
   [15,14,12,16]]    [16,7,10,11]]

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

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

def rotate(matrix):
    pass


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        ),
        (
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        ),
        (
            [[1]],
            [[1]]
        ),
        (
            [[1, 2], [3, 4]],
            [[3, 1], [4, 2]]
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        ),
        (
            [[2, 29, 20, 26, 16, 28],
             [12, 27, 9, 25, 13, 21],
             [32, 33, 32, 2, 28, 14],
             [13, 14, 32, 27, 22, 29],
             [31, 27, 9, 2, 15, 17],
             [22, 7, 31, 3, 29, 10]],
            [[22, 31, 13, 32, 12, 2],
             [7, 27, 14, 33, 27, 29],
             [31, 9, 32, 32, 9, 20],
             [3, 2, 27, 2, 25, 26],
             [29, 15, 22, 28, 13, 16],
             [10, 17, 29, 14, 21, 28]]
        ),
        (
            [[-1, -2], [-3, -4]],
            [[-3, -1], [-4, -2]]
        ),
        (
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        ),
    ]

    passed = 0
    total = len(tests)

    for i, (matrix, expected) in enumerate(tests, 1):
        try:
            import copy
            mat = copy.deepcopy(matrix)
            rotate(mat)
            if mat == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}:")
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
