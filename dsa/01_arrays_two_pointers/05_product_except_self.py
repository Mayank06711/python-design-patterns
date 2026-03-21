"""
PROBLEM: Product of Array Except Self
LeetCode #238: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and WITHOUT using the division operation.

CONSTRAINTS:
- 2 <= len(nums) <= 10^5
- -30 <= nums[i] <= 30
- Product of any prefix/suffix fits in 32-bit integer
- O(n) time required
- NO division allowed

FOLLOW-UP: Can you solve it in O(1) extra space? (The output array does not count as extra space.)

DIFFICULTY: Medium
TIME LIMIT: 10 minutes
STARTED: 1:18 AM (March 20, 2026)
COMPLETED: 1:42 AM (March 22, 2026)
ATTEMPT: 4+
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# - What pattern will you use? Why?
# - Step-by-step algorithm
# - Time complexity? Space complexity?
# ============================================================
#approch 1:
# what I can do in the first thing In the first pass I will calculate the overall product of the array excluding the giro like if an element is zero we want to multiply with that zero but we I have a pointer like a variable which will track is there any zero in the array
# in the second what I will do is I will it first I will cheque like OK so if there was an zero every place where there is a non zero the output will be I will PL zero and everywhere where there is a zero I will put the product overall product and if no zero was there i will deivde the product with the value at i
# this will take T>C -> O(n) and S>c-> O(1)

# approach 2
# the brute force approach is to use two loops where I the first loop is for iterating on the I start with zero and goes to Second loop also starts with zero and goes to L till but and inside the inner loop what we will do except for the array of we will multiply every other element and once this inner loop is before the next leak the outer loop moves to the next value of I We will update that particular value of I in place This will give output and if like element is not zero and I divided the product with that element but product was positive and element is negative and then I will divide it with absolute value of the index value But if product is negative value is positive same goes but product is also negative and value is also negative then in this case like
# t.c- > O(n2) and s.c O(1) then in this case like then in this case like

# approach 3
# can come up with like I don't know how but if I do take two arrays one is left product like the product of everything left side of the element and one is right product product of everything right side of array what I will do I will create like I will do for the same array First form I equals to zero to and what we will do is deep multiplying like a tie goes to the left product array will have three like the value of I then at high cost one the product will be III zero into I of one Then I goes to two the product will be I one because I one already contains I 0 and I 1 into I 2 and place at I 2 same and other loop will start with I equals to N minus 1 and go till zero And we will do the same kind of multiplication but from the backwards
# 

# ============================================================
# STEP 2: WRITE YOUR SOLUTION BELOW
# ============================================================
def product_except_self(nums):
    n = len(nums)
    ans = []
    r_prod = 1
    for i in range(n):
        if i == 0:
            ans.append(1)
        else:
            ans.append(ans[i-1]*nums[i-1])
    for i in range(n-1, -1, -1):
        if i == n-1:
            r_prod = 1
        else:
            r_prod = r_prod * nums[i+1]
        ans[i] = ans[i] * r_prod
    return ans

        
        



# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (input, expected)
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([0, 0], [0, 0]),
        ([1, 0, 3, 4], [0, 12, 0, 0]),
        ([5, -1, 2, -3], [6, -30, 15, -10]),
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([-1, -1, -1, -1], [-1, -1, -1, -1]),
        ([10, 0, 0, 5], [0, 0, 0, 0]),
    ]

    passed = 0
    total = len(tests)

    for i, (nums, expected) in enumerate(tests, 1):
        try:
            result = product_except_self(nums[:])
            if result == expected:
                print(f"  [PASS] Test {i}")
                passed += 1
            else:
                print(f"  [FAIL] Test {i}: product_except_self({nums}) = {result}, expected {expected}")
        except Exception as e:
            print(f"  [FAIL] Test {i}: {type(e).__name__} — {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
