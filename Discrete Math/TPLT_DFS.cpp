#include <iostream>
using namespace std;

const int MAX = 100;
int adj [MAX][MAX];
bool visited[MAX];
int n;

void DFS(int u) {
    visited[u] = true;

    for (int i = 0; i < n; i++){
        if (adj[u][i] == 1 && !visited[i]) {
            DFS (i);
        }
    }
}

int TPLT_DFS (int a[][MAX]) {
    for (int i = 0; i < n; i++){
        visited[i] = false;

        for (int j = 0; j < n; j++){
            adj[i][j] = a[i][j];
        }
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            count++;
            DFS(i);
        }
    }

    return count;
}