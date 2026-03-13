/*
 * Gas Station
 * LeetCode: #134 | Difficulty: Medium
 * Circular route start index. gas=[1,2,3,4,5] cost=[3,4,5,1,2]->3
 * Pattern: Reset start when tank<0
 * Company: Amazon, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) { return 0; }
};

int main() {
    Solution sol;
    vector<int> g={1,2,3,4,5},c={3,4,5,1,2}; cout<<"Test1: "<<sol.canCompleteCircuit(g,c)<<" (expected 3)"<<endl;
    vector<int> g2={2,3,4},c2={3,4,3}; cout<<"Test2: "<<sol.canCompleteCircuit(g2,c2)<<" (expected -1)"<<endl;
    return 0;
}
