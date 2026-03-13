/*
 * Problem: Task Scheduler (LC #621) - Medium
 *
 * Given tasks array and cooldown interval n, return the least
 * number of time units the CPU will take to finish all tasks.
 * tasks=["A","A","A","B","B","B"] n=2 -> 8
 *
 * Approach: Max-heap to always pick most frequent task.
 * After executing, place in cooldown queue with available time.
 * Move tasks back to heap when cooldown expires.
 *
 * Time:  O(N * 26)
 * Space: O(26) = O(1)
 */

#include <iostream>
#include <vector>
#include <queue>
#include <cassert>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // TODO: Frequency count + max-heap + cooldown queue
        return -1;
    }
};

int main() {
    cout << "=== Task Scheduler (LC #621) ===" << endl;
    Solution sol;

    vector<char> t1 = {'A', 'A', 'A', 'B', 'B', 'B'};
    int r1 = sol.leastInterval(t1, 2);
    cout << "Test 1: [A,A,A,B,B,B] n=2 -> " << r1 << " (expected 8)" << endl;
    assert(r1 == 8);

    vector<char> t2 = {'A', 'A', 'A', 'B', 'B', 'B'};
    int r2 = sol.leastInterval(t2, 0);
    cout << "Test 2: [A,A,A,B,B,B] n=0 -> " << r2 << " (expected 6)" << endl;
    assert(r2 == 6);

    vector<char> t3 = {'A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    int r3 = sol.leastInterval(t3, 2);
    cout << "Test 3: [A*6,B,C,D,E,F,G] n=2 -> " << r3 << " (expected 16)" << endl;
    assert(r3 == 16);

    vector<char> t4 = {'A'};
    int r4 = sol.leastInterval(t4, 5);
    cout << "Test 4: [A] n=5 -> " << r4 << " (expected 1)" << endl;
    assert(r4 == 1);

    cout << "\nAll tests passed!" << endl;
    return 0;
}
