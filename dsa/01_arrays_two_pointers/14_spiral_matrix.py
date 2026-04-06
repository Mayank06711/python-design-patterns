"""
Spiral Matrix
LeetCode #54: https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in SPIRAL ORDER.

Spiral order: right along top row, down along right column,
              left along bottom row, up along left column, then repeat inward.

Examples:
  [[1,2,3],
   [4,5,6],       ->  [1, 2, 3, 6, 9, 8, 7, 4, 5]
   [7,8,9]]

  [[1,2,3,4],
   [5,6,7,8],     ->  [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
   [9,10,11,12]]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

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

def spiral_order(matrix):
    pass


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([[1]], [1]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
         [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2, 4, 6, 5, 3]),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], [1, 2, 4, 6, 8, 7, 5, 3]),
        ([[6, 9, 7]], [6, 9, 7]),
    ]

    passed = 0
    total = len(tests)

    for i, (matrix, expected) in enumerate(tests, 1):
        try:
            import copy
            mat = copy.deepcopy(matrix)
            result = spiral_order(mat)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: spiral_order({matrix}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
