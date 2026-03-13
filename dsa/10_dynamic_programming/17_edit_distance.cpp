/*
 * Edit Distance
 * LeetCode: #72 | Difficulty: Medium
 * Min ops word1->word2. horse->ros->3
 * Pattern: Insert/delete/replace DP
 * Company: Google, Amazon
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDistance(string w1, string w2) { return 0; }
};

int main() {
    Solution sol;
    cout<<"Test1: "<<sol.minDistance("horse","ros")<<" (expected 3)"<<endl;
    cout<<"Test2: "<<sol.minDistance("intention","execution")<<" (expected 5)"<<endl;
    return 0;
}
