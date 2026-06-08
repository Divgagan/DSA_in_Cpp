#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> bfs(int n, vector<vector<int>>& graph, int source) {
        vector<int> dist(n, -1);
        queue<int> q;
        dist[source] = 0;
        q.push(source);
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (int next : graph[node]) {
                if (dist[next] == -1) {
                    dist[next] = dist[node] + 1;
                    q.push(next);
                }
            }
        }
        return dist;
    }
};
