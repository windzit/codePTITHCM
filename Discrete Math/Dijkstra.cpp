const int INF = 1e9;

int dist[MAX];
bool visited[MAX];
int parent[MAX];

void Dijkstra(int a[][MAX], int s)
{
    for (int i = 0; i < n; i++)
    {
        dist[i] = INF;
        visited[i] = false;
        parent[i] = -1;
    }

    dist[s] = 0;

    for (int i = 0; i < n; i++)
    {
        int u = -1;
        int Min = INF;

        // Chọn đỉnh chưa thăm có dist nhỏ nhất
        for (int j = 0; j < n; j++)
        {
            if (!visited[j] && dist[j] < Min)
            {
                Min = dist[j];
                u = j;
            }
        }

        if (u == -1)
            break;

        visited[u] = true;

        // Relax
        for (int v = 0; v < n; v++)
        {
            if (a[u][v] != 0 &&
                !visited[v] &&
                dist[u] + a[u][v] < dist[v])
            {
                dist[v] = dist[u] + a[u][v];
                parent[v] = u;
            }
        }
    }
}