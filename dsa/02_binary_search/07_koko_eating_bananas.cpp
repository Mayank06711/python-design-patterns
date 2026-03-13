/*
 * Problem: Koko Eating Bananas
 * LeetCode: #875 | Difficulty: Medium
 *
 * Koko loves to eat bananas. There are n piles of bananas, the i-th pile
 * has piles[i] bananas. The guards have gone and will come back in h hours.
 * Koko can decide her bananas-per-hour eating speed of k. Each hour, she
 * picks a pile and eats k bananas from it. If the pile has fewer than k
 * bananas, she eats all of them and does not eat any more during that hour.
 * Return the minimum integer k such that she can eat all bananas within h hours.
 * Hint: Binary search on the answer space [1, max(piles)].
 *
 * Example: piles = [3,6,7,11], h = 8 -> Output: 4
 * Example: piles = [30,11,23,4,20], h = 5 -> Output: 30
 *
 * Pattern: Binary Search on Answer Space
 * Company: Google, Facebook, Amazon, Airbnb, DoorDash
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // TODO: Binary search on speed k in [1, max(piles)]
        // For each k, compute total hours needed and check if <= h
        return 0;
    }
};

int main() {
    Solution sol;

    // Test 1: basic case
    vector<int> piles1 = {3, 6, 7, 11};
    int res1 = sol.minEatingSpeed(piles1, 8);
    cout << "Test 1: piles=[3,6,7,11], h=8 -> " << res1;
    cout << (res1 == 4 ? " [PASS]" : " [FAIL]") << endl;

    // Test 2: tight hours (must eat fastest)
    vector<int> piles2 = {30, 11, 23, 4, 20};
    int res2 = sol.minEatingSpeed(piles2, 5);
    cout << "Test 2: piles=[30,11,23,4,20], h=5 -> " << res2;
    cout << (res2 == 30 ? " [PASS]" : " [FAIL]") << endl;

    // Test 3: generous hours
    vector<int> piles3 = {30, 11, 23, 4, 20};
    int res3 = sol.minEatingSpeed(piles3, 6);
    cout << "Test 3: piles=[30,11,23,4,20], h=6 -> " << res3;
    cout << (res3 == 23 ? " [PASS]" : " [FAIL]") << endl;

    // Test 4: single pile
    vector<int> piles4 = {1000000000};
    int res4 = sol.minEatingSpeed(piles4, 2);
    cout << "Test 4: piles=[1000000000], h=2 -> " << res4;
    cout << (res4 == 500000000 ? " [PASS]" : " [FAIL]") << endl;

    // Test 5: all piles size 1
    vector<int> piles5 = {1, 1, 1, 1};
    int res5 = sol.minEatingSpeed(piles5, 4);
    cout << "Test 5: piles=[1,1,1,1], h=4 -> " << res5;
    cout << (res5 == 1 ? " [PASS]" : " [FAIL]") << endl;

    // Test 6: more hours than piles
    vector<int> piles6 = {3, 6, 7, 11};
    int res6 = sol.minEatingSpeed(piles6, 100);
    cout << "Test 6: piles=[3,6,7,11], h=100 -> " << res6;
    cout << (res6 == 1 ? " [PASS]" : " [FAIL]") << endl;

    return 0;
}
