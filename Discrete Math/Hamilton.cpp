#include <iostream>
#include <stack>
#include <vector>
using namespace std;

const int MAX = 100;

int adj[MAX][MAX];
bool visited[MAX];
int HC[MAX + 1];
int n;

bool Hamilton(int k) {

    for (int v = 0; v < n; v++) {

        if (adj[HC[k - 1]][v] == 1 && !visited[v]) {

            HC[k] = v;
            visited[v] = true;

            // Đã đi qua n đỉnh
            if (k == n - 1) {

                // Có cạnh quay về đỉnh đầu
                if (adj[HC[k]][HC[0]] == 1) {

                    HC[n] = HC[0];

                    return true;
                }
            }
            else {

                if (Hamilton(k + 1))
                    return true;
            }

            visited[v] = false;
        }
    }

    return false;
}

/* Khởi tạo
int start;
HC[0] = start;
visited[start] = true;

Hamilton(1);
*/