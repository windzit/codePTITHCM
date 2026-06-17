#include <iostream>
#include <stack>
#include <vector>
using namespace std;

struct Egde {
    int u, v, w;
}

const int MAX = 100;

Egde E[MAX];
Egde T[MAX];

int parent[MAX];
int n, m;

int Find(int u)
{
    while (u != parent[u])
        u = parent[u];

    return u;
}

void Union (int u, int v)
{
    parent[Find(u)] = Find(v);
}

void Kruskal ()
{
    for (int i = 0; i < n; i++)
    {
        parent[i] = i;
    }

    int cnt = 0;

    // Giả sử E đã được sort tăng dần theo trọng số
    for (int i = 0; i<m; i++)
    {
        int u = E[i].u;
        int v = E[i].v;

        if (Find(u) != Find(v))
        {
            T[cnt++] = E[i];

            Union(u, v);

            if (cnt == n - 1)
                break;
        }
    }
}