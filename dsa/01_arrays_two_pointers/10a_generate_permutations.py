"""
WARM-UP: Generate All Permutations
LeetCode #46: https://leetcode.com/problems/permutations/

Given an array of DISTINCT integers, return all possible permutations.
You can return the answer in ANY ORDER.

Examples:
  [1, 2, 3] → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
  [1] → [[1]]
  [0, 1] → [[0,1],[1,0]]

Constraints:
- 1 <= len(nums) <= 6
- All integers are unique

DIFFICULTY: Medium (but classic backtracking pattern)
TIME LIMIT: 8 minutes
STARTED: 2:44 PM, Mar 30, 2026
COMPLETED: 3:20 PM, Mar 30, 2026
ATTEMPT: 2 (backtracking pattern learned)
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# 1. WHAT: (what does the question want?) question wants me to findout all permutaions of given array
# 2. HOW: (step-by-step algorithm)  
# 3. EDGE CASES: (what could go wrong?) 
# 4. COMPLEXITY: (time and space) O(n!*n), S>C(n)
# ============================================================


# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def sol(visited, nums, curr, res):
    if len(curr) == len(nums):
        res.append(curr[:])
        return 
    for i in range(len(nums)):
        if nums[i] in visited:
            continue
        visited.append(nums[i])
        curr.append(nums[i])
        sol(visited, nums, curr, res)
        curr.pop()
        visited.pop()



def permute(nums):
    visited = []
    res = []
    curr = []
    sol(visited, nums, curr, res)
    return res

   
    
    


# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        ([1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([1], [[1]]),
        ([0, 1], [[0,1],[1,0]]),
        ([1, 2], [[1,2],[2,1]]),
        ([1, 2, 3, 4], 24),  # just check count = 4! = 24
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            result = permute(nums[:])
            if isinstance(expected, int):
                # just check count
                if len(result) == expected and all(sorted(p) == sorted(nums) for p in result):
                    print(f"  [PASS] Test {i}")
                    passed += 1
                else:
                    print(f"  [FAIL] Test {i}: got {len(result)} permutations, expected {expected}")
            else:
                result_sorted = sorted([sorted(p) for p in result])
                expected_sorted = sorted([sorted(p) for p in expected])
                result_set = set(tuple(p) for p in result)
                expected_set = set(tuple(p) for p in expected)
                if result_set == expected_set and len(result) == len(expected):
                    print(f"  [PASS] Test {i}")
                    passed += 1
                else:
                    print(f"  [FAIL] Test {i}: got {result}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
