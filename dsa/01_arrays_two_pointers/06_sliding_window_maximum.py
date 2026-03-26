"""
PROBLEM: Sliding Window Maximum
LeetCode #239: https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums and an integer k (the window size).
There is a sliding window of size k which moves from the very left of the
array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves one position to the right.

Return a list of the maximum value in each window position.

Example:
    nums = [1,3,-1,-3,5,3,6,7], k = 3

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7      3
     1 [3  -1  -3] 5  3  6  7      3
     1  3 [-1  -3  5] 3  6  7      5
     1  3  -1 [-3  5  3] 6  7      5
     1  3  -1  -3 [5  3  6] 7      6
     1  3  -1  -3  5 [3  6  7]     7

    Output: [3, 3, 5, 5, 6, 7]

CONSTRAINTS:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

DIFFICULTY: Hard
TIME LIMIT: 12 minutes
STARTED: 4:25 PM, Mar 25, 2026
COMPLETED: 2:11 PM, Mar 26, 2026
ATTEMPT: 2 (1st: 2/10 — loop bounds bugs; 2nd: 10/10)
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: Question is asking that when there is a array and given an integer K which is actually the size of the window so at a time the window moves like there will be a fixed window which will move on the array from left to extreme right read and inside each window I need to find out the maximum value within that window 
# 2. HOW: So there are two possible ways that I could come up one is brute force where we run one loop to traverse till II mean till I is less than N minus K plus one where K is the size of that window and inside that loop we take I and like every time we calculate maximum of each each window and keep updating it That will be big of N into K because inside there will be K loops, Another I can come up with is an K log K
# 3. EDGE CASES: couldn`t find edge case for my algo
# 4. COMPLEXITY: 
# algo 1
# two one outer loop to move window
# innner loop find max of each window and save it to ans
# t.c O(n*k) S.c O(n-k+1) as

# algo 2
# In this loop what we will be doing We know that let us assume the case three right So when I move by one place K will move like window will move by one leg it discard one element from the window and add one the next one So if we already know the maximum of a window and the next element is coming and the outgoing element is not the maximum of this window then we are we only need compare between the incoming element and the maximum of previous window, Now if the element which is left behind the window he's gone now we have to find a new maximum again in the new window So this is how we will find the maximum of each window 

# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def max_sliding_window(nums, k):
    if k == 1:
        return nums
    ans = []
    for i in range(len(nums)-k+1):
        j , maxi = nums[0] , 0
        while j < i + k-1:
            new_maxi = max(nums[j],  nums[j+1])
            maxi = max(new_maxi, maxi)
            j += 1
        ans.append(maxi)
    return ans



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (nums, k, expected)
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
        ([9, 11], 2, [11]),
        ([4, 3, 2, 1], 2, [4, 3, 2]),
        ([1, 2, 3, 4], 2, [2, 3, 4]),
        ([1, 1, 1, 1, 1], 3, [1, 1, 1]),
        ([7, 2, 4], 2, [7, 4]),
        ([-7, -8, 7, 5, 7, 1, 6, 0], 4, [7, 7, 7, 7, 7]),
        ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, k, expected) in enumerate(tests, 1):
        try:
            result = max_sliding_window(nums[:], k)
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: max_sliding_window({nums}, {k}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
