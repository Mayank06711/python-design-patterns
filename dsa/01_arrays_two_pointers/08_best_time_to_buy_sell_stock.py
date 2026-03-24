"""
PROBLEM: Best Time to Buy and Sell Stock
LeetCode #121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array `prices` where prices[i] is the price of a given
stock on the i-th day.

You want to maximize your profit by choosing a SINGLE day to buy and a
SINGLE DIFFERENT day in the future to sell.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

CONSTRAINTS:
- 1 <= len(prices) <= 10^5
- 0 <= prices[i] <= 10^4

DIFFICULTY: Easy
TIME LIMIT: 5 minutes
STARTED: 5:05 PM (March 24, 2026)
COMPLETED: 5:20 PM (March 24, 2026)
ATTEMPT: 1
"""

# ============================================================
# STEP 1: WRITE YOUR APPROACH HERE AS COMMENTS BEFORE CODING
# ============================================================
# 1. WHAT:
# 2. HOW:
# 3. EDGE CASES:
# 4. COMPLEXITY:

# So what I understand from the question is question is asking that give the maximum profit to the user by buying up stock on the day when it is less like bike and selling it on the maximum profit day and you cannot buy I mean sell before buying So this creates a natural constraint that we have to be in limit only one if it is A and on day two it is 99 if it is decreasing it can never
 #never can itreasing Dec is it ifety is it two day on and a is it if one only limit in be to have we thatraint const natural aes creat this so buying before sell mean Ibuy  cannot you andximum profit dayMax the on it selling andike B like less is it when day the on stock up buying byer US the to profitimum Max thegive  that asking ision quest ision que if it is decreasing it can never
# algo 1 brute force
# two loop outer tells when to buy and inner find when to sell by cal max profict from sell - buy
# t.c O(n^2)  and s.c O(1)
# algo 2
# take two pointer as buy_price and max_profit = 0  and intilise buy_price as arr[0]
# run a loop i = 1 to len of arr 
# inside it cal profit = arr[i] - buy_price
# if profit is > 0 that means sell price is greater than buy no need to change buy price
# if proft is < 0 -> here selling price is less than buy we update buy_price and
# if zero just move as buy and sell both same
# max_profit = maxi of profit and max_profit 
# return max_profit
# t.c -> O(N) and S>C=> O(1)


# ============================================================
# STEP 2: CODE YOUR SOLUTION
# ============================================================
def max_profit(prices:list):
    best_profit = 0
    buy_price = prices[0]
    i = 1
    while i < len(prices):
        profit = prices[i] - buy_price
        if profit < 0:
            buy_price = prices[i]
        best_profit = max(best_profit , profit)
        i += 1
    return best_profit




# ============================================================
# TESTS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    tests = [
        # (input, expected)
        ([7, 1, 5, 3, 6, 4], 5),       # buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),           # decreasing — no profit
        ([1, 2], 1),                     # simple profit
        ([2, 1], 0),                     # buy > sell — no profit
        ([2, 4, 1], 2),                  # best is early pair, not global min
        ([3, 3, 3, 3], 0),              # all same — no profit
        ([1], 0),                        # single element
        ([2, 7, 1, 3], 5),              # global min (1) comes after best sell (7)
        ([1, 2, 3, 4, 5], 4),           # ascending — buy first, sell last
        ([10, 1, 10, 1, 10], 9),        # repeated peaks
    ]

    passed = 0
    total = len(tests)

    for i, (prices, expected) in enumerate(tests, 1):
        try:
            result = max_profit(prices)
            status = "PASS" if result == expected else "FAIL"
            if status == "PASS":
                passed += 1
            print(f"  Test {i}: {status} | Input: {prices} | Expected: {expected} | Got: {result}")
        except Exception as e:
            print(f"  Test {i}: ERROR | Input: {prices} | {e}")

    print(f"\n{'='*50}")
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ALL TESTS PASSED!")
    print(f"{'='*50}")

if __name__ == "__main__":
    run_tests()
