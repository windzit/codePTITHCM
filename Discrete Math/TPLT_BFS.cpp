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

int TPLT_BFS (int a[][MAX]) {
    for (int i = 0; i < n; i++) {
        visited[i] = false;

        for (int j = 0; j < n; j++) {
            adj[i][j] = a[i][j];
        }
    }

    int count = 0;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            BFS(i);
            count++;
        }
    }

    return count;
}