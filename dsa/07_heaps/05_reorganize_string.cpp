/*
 * Problem: Reorganize String (LC #767) - Medium
 *
 * Rearrange characters of s so that no two adjacent characters
 * are the same. Return "" if not possible.
 * "aab" -> "aba"
 *
 * Approach: Max-heap greedy. Always place the most frequent char.
 * After placing, hold it aside, place next most frequent, then
 * push held char back.
 *
 * Time:  O(N log 26) = O(N)
 * Space: O(26) = O(1)
 */

#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <cassert>

using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        // TODO: Frequency count + max-heap greedy placement
        return "";
    }
};

bool isValid(const string& s) {
    for (int i = 1; i < (int)s.size(); i++) {
        if (s[i] == s[i - 1]) return false;
    }
    return true;
}

int main() {
    cout << "=== Reorganize String (LC #767) ===" << endl;
    Solution sol;

    string r1 = sol.reorganizeString("aab");
    cout << "Test 1: \"aab\" -> \"" << r1 << "\"" << endl;
    assert(r1.size() == 3 && isValid(r1));

    string r2 = sol.reorganizeString("aaab");
    cout << "Test 2: \"aaab\" -> \"" << r2 << "\" (expected empty)" << endl;
    assert(r2 == "");

    string r3 = sol.reorganizeString("aabbcc");
    cout << "Test 3: \"aabbcc\" -> \"" << r3 << "\"" << endl;
    assert(r3.size() == 6 && isValid(r3));

    string r4 = sol.reorganizeString("a");
    cout << "Test 4: \"a\" -> \"" << r4 << "\"" << endl;
    assert(r4 == "a");

    string r5 = sol.reorganizeString("aa");
    cout << "Test 5: \"aa\" -> \"" << r5 << "\" (expected empty)" << endl;
    assert(r5 == "");

    cout << "\nAll tests passed!" << endl;
    return 0;
}
