/*
 * Subsets
 * LeetCode: #78 | Difficulty: Medium
 * Return all possible subsets (power set). nums=[1,2,3]
 * Pattern: Include/exclude at each index
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        // TODO: implement
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> n1 = {1, 2, 3};
    auto r1 = sol.subsets(n1);
    cout << "Test 1: {1,2,3} -> " << r1.size() << " subsets (expected 8) " << (r1.size()==8?"PASS":"FAIL") << endl;

    vector<int> n2 = {0};
    auto r2 = sol.subsets(n2);
    cout << "Test 2: {0} -> " << r2.size() << " subsets (expected 2) " << (r2.size()==2?"PASS":"FAIL") << endl;
    return 0;
}
