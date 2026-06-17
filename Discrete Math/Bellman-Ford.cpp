struct Edge {
    int u, v, w;
};

Edge E[MAX];
int m;      // số cạnh
int n;      // số đỉnh

const int INF = 1e9;

int dist[MAX];
int parent[MAX];

void BellmanFord(int s)
{
    // Khởi tạo
    for (int i = 0; i < n; i++)
    {
        dist[i] = INF;
        parent[i] = -1;
    }

    dist[s] = 0;

    // Relax n-1 lần
    for (int i = 1; i <= n - 1; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int u = E[j].u;
            int v = E[j].v;
            int w = E[j].w;

            if (dist[u] != INF &&
                dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w;
                parent[v] = u;
            }
        }
    }
}