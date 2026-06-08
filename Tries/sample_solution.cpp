#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    array<TrieNode*, 26> child{};
    bool terminal = false;
};

class Trie {
public:
    TrieNode root;
};
