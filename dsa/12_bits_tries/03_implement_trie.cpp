/*
 * Implement Trie (Prefix Tree)
 * LeetCode: #208 | Difficulty: Medium
 * Build trie with insert, search, startsWith
 * Pattern: Trie node structure
 * Company: Amazon, Google, Meta
 */
#include <bits/stdc++.h>
using namespace std;

class Trie {
public:
    Trie() { /* TODO */ }
    void insert(string word) { /* TODO */ }
    bool search(string word) { return false; }
    bool startsWith(string prefix) { return false; }
};

int main() {
    Trie trie;
    trie.insert("apple");
    cout << "search apple: " << trie.search("apple") << " (expected 1)" << endl;
    cout << "search app: " << trie.search("app") << " (expected 0)" << endl;
    cout << "startsWith app: " << trie.startsWith("app") << " (expected 1)" << endl;
    trie.insert("app");
    cout << "search app: " << trie.search("app") << " (expected 1)" << endl;
    return 0;
}
