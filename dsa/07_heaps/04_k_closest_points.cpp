/*
 * Problem: K Closest Points to Origin (LC #973) - Medium
 *
 * Given an array of points and integer k, return the k closest
 * points to the origin (0,0). No need for sqrt.
 * points=[[1,3],[-2,2]] K=1 -> [[-2,2]]
 *
 * Approach: Max-heap of size K using squared distances.
 * If heap exceeds K, pop the farthest point.
 *
 * Time:  O(N log K)
 * Space: O(K)
 */

#include <iostream>
#include <vector>
#include <queue>
#include <cassert>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // TODO: Max-heap of size K with squared distances
        return {};
    }
};

void printPoints(const vector<vector<int>>& pts) {
    cout << "[";
    for (int i = 0; i < (int)pts.size(); i++) {
        cout << "[" << pts[i][0] << "," << pts[i][1] << "]";
        if (i < (int)pts.size() - 1) cout << ",";
    }
    cout << "]";
}

bool samePoints(vector<vector<int>> a, vector<vector<int>> b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    return a == b;
}

int main() {
    cout << "=== K Closest Points to Origin (LC #973) ===" << endl;
    Solution sol;

    vector<vector<int>> pts1 = {{1, 3}, {-2, 2}};
    vector<vector<int>> r1 = sol.kClosest(pts1, 1);
    cout << "Test 1: [[1,3],[-2,2]] K=1 -> ";
    printPoints(r1);
    cout << " (expected [[-2,2]])" << endl;
    assert(samePoints(r1, {{-2, 2}}));

    vector<vector<int>> pts2 = {{3, 3}, {5, -1}, {-2, 4}};
    vector<vector<int>> r2 = sol.kClosest(pts2, 2);
    cout << "Test 2: [[3,3],[5,-1],[-2,4]] K=2 -> ";
    printPoints(r2);
    cout << " (expected [[3,3],[-2,4]])" << endl;
    assert(samePoints(r2, {{3, 3}, {-2, 4}}));

    vector<vector<int>> pts3 = {{0, 0}, {1, 1}};
    vector<vector<int>> r3 = sol.kClosest(pts3, 1);
    cout << "Test 3: [[0,0],[1,1]] K=1 -> ";
    printPoints(r3);
    cout << " (expected [[0,0]])" << endl;
    assert(samePoints(r3, {{0, 0}}));

    cout << "\nAll tests passed!" << endl;
    return 0;
}
