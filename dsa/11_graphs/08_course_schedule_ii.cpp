/*
 * Course Schedule II
 * LeetCode: #210 | Difficulty: Medium
 * Return valid course ordering
 * Pattern: Topological sort (full ordering)
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) { return {}; }
};

int main() {
    Solution sol;
    vector<vector<int>> p={{1,0},{2,0},{3,1},{3,2}};
    auto r=sol.findOrder(4,p);
    cout<<"Test: "<<r.size()<<" courses (expected 4)"<<endl;
    return 0;
}
