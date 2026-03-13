/*
 * Strange Printer
 * LeetCode: #664 | Difficulty: Hard
 * Min turns. aaabbb->2
 * Pattern: Interval DP, endpoint merge
 * Company: Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int strangePrinter(string s) { return 0; }
};

int main() {
    Solution sol;
    cout<<"Test1: "<<sol.strangePrinter("aaabbb")<<" (expected 2)"<<endl;
    cout<<"Test2: "<<sol.strangePrinter("aba")<<" (expected 2)"<<endl;
    return 0;
}
