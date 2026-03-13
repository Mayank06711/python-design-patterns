/*
 * Course Schedule
 * LeetCode: #207 | Difficulty: Medium
 * Can finish all courses? Cycle detection
 * Pattern: Topological sort / Kahns algo
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) { return false; }
};

int main() {
    Solution sol;
    vector<vector<int>> p1={{1,0}}; cout<<"Test1: "<<sol.canFinish(2,p1)<<" (expected 1)"<<endl;
    vector<vector<int>> p2={{1,0},{0,1}}; cout<<"Test2: "<<sol.canFinish(2,p2)<<" (expected 0)"<<endl;
    return 0;
}
