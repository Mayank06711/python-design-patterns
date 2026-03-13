/*
 * Minimum Platforms
 * LeetCode: GFG | Difficulty: Medium
 * Min platforms for trains. arr/dep arrays
 * Pattern: Sort arrivals+departures, sweep line
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findPlatform(vector<int>& arr, vector<int>& dep) { return 0; }
};

int main() {
    Solution sol;
    vector<int> a={900,940,950,1100,1500,1800},d={910,1200,1120,1130,1900,2000};
    cout<<"Test: "<<sol.findPlatform(a,d)<<" platforms (expected 3)"<<endl;
    return 0;
}
