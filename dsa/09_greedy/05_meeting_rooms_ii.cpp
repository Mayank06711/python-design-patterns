/*
 * Meeting Rooms II
 * LeetCode: #253 | Difficulty: Medium
 * Min rooms needed. [[0,30],[5,10],[15,20]]->2
 * Pattern: Min-heap or sweep line
 * Company: Amazon, Meta, Google
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) { return 0; }
};

int main() {
    Solution sol;
    vector<vector<int>> a={{0,30},{5,10},{15,20}}; cout<<"Test1: "<<sol.minMeetingRooms(a)<<" (expected 2)"<<endl;
    vector<vector<int>> b={{7,10},{2,4}}; cout<<"Test2: "<<sol.minMeetingRooms(b)<<" (expected 1)"<<endl;
    return 0;
}
