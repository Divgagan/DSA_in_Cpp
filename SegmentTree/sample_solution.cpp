#include <bits/stdc++.h>
using namespace std;

class SegmentTree {
    vector<long long> tree;

public:
    explicit SegmentTree(int n) : tree(4 * max(1, n), 0) {}
};
