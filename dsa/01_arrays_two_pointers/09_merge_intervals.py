"""
PROBLEM: Merge Intervals
LeetCode #56: https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.

CONSTRAINTS:
- 1 <= len(intervals) <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

DIFFICULTY: Medium
TIME LIMIT: 8 minutes
STARTED: 5:33 PM (March 24, 2026)
COMPLETED: 7:08 PM (March 24, 2026)
ATTEMPT: 1 (8/10) — rewriting for deeper understanding
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT: OK so problem says that there is an list of lists right and inside each list there are two only 2 elements start of the interval end of the interval and there can be overlapping interval means let's say the my interview interval was two hours and I had to interview but the second interview was also scheduled before my this interview gets over I mean within the interval of my first interview the 2 hours the second interview comes in That's an overlap 
# 2. HOW: 
# 3. EDGE CASES:
# 4. COMPLEXITY:
# algo -1
# I will have a loop running from index 0 Length of array -1
# I will compare each list like now at index 0 there is a list of two element and at index one there is an element of 2 there is a list of two element so the list at index I minus 1 the second element at least off list at index I 1 must be less than index the first index element at indexed I and we take minimum an maximum of them of ans
# What if when we store the interval in answer list that interval collides with some other interval so for that we will now have one more check
# We will check before storing it  That from the interval array like from the last side from where we appended the N - 1 TH element if its second element is less than or equal I mean greater than or equal the loops one like from the loop that at index I That means it is a it needs the new will not come inside and it will be updated the second element will be updated of the answer as per the  i
# If conditions satisfied we will store Inside an answer list with a where is start interval will be from the left index I - 1 and end interval will be at of index I remember here can be an edge case
# t.c => nlog(n) + O(n), S>C-> O(n) to store ans

# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def merge(arr):
    arr.sort() #  [[4,7],[1,4]] => [[1,4],[4,7]] 
    n = len(arr)
    ans = [arr[0]] # [[1,4]] => 1sr ele always sorted 
    for i in range(1,n):
        if ans[len(ans)-1][1] >= arr[i][0]: # means [1,4] compared with [4,7] here i am already in int 1-4 but nextt start within this block
            ans[-1][1] = max(ans[-1][1], arr[i][1])
        else:
            ans.append(arr[i])
    return ans






# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (input, expected)
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[0,4]], [[0,4]]),
        ([[1,4],[2,3]], [[1,4]]),               # one inside another
        ([[1,4],[0,0]], [[0,0],[1,4]]),           # no overlap
        ([[1,4]], [[1,4]]),                       # single interval
        ([[1,4],[0,2],[3,5]], [[0,5]]),           # chain merge
        ([[2,3],[4,5],[6,7],[8,9],[1,10]], [[1,10]]),  # one big interval absorbs all
        ([[1,3],[2,6],[8,10],[9,12],[15,18]], [[1,6],[8,12],[15,18]]),
        ([[0,0],[1,1],[2,2]], [[0,0],[1,1],[2,2]]),  # no overlaps at all
    ]

    passed = 0
    total = len(tests)

    for i, (intervals, expected) in enumerate(tests, 1):
        try:
            result = merge(intervals)
            status = "PASS" if result == expected else "FAIL"
            if status == "PASS":
                passed += 1
            print(f"  Test {i}: {status} | Input: {intervals} | Expected: {expected} | Got: {result}")
        except Exception as e:
            print(f"  Test {i}: ERROR | Input: {intervals} | {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
