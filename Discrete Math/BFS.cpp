#include <iostream>
#include <queue>
using namespace std;

const int MAX = 100;
queue <int> q;
bool visited[MAX];
int adj[MAX][MAX];
int n;

void BFS (int u) {
    q.push(u);
    visited[u] = true;

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        
        // handle 
        
        for (int i = 0; i < n; i++) {
            if (adj[node][i] == 1 && !visited[i]) {
                q.push(i);
                visited[i] = true;
            }
        }
    }
}