#include <iostream>
using namespace std;

const int MAX = 100;
const int INF = 1e9;

int parent[MAX];
int key[MAX];
bool visited[MAX];
int n;

void Prim (int a[][MAX])
{
    for (int i=0; i<n; i++)
    {
        visited[i] = false;
        key[i] = INF;
        parent[i] = -1;
    }

    key[0] = 0;

    for (int i = 0; i < n; i++)
    {
        int u = -1;
        int MIN = INF;

        for (int j=0; j<n; j++)
        {
            if (!visited[j] && key[j] < MIN)
            {
                MIN = key[j];
                u = j;
            }
        }

        visited[u] = true;

        for (int v = 0; v < n; v++)
        {
            if(a[u][v] != 0 && !visited[v] && a[u][v] < key[v])
            {
                key[v] = a[u][v];
                parent[v] = u;
            }
        }
    }
}