#include <iostream>
using namespace std;
/*
Có hai cách để làm DFS 
Cách 1: Dùng stack và while
Đặc điểm:
- Dễ đọc
- Dễ hình dung, dễ hiểu
Nhược điểm:
- Quá dài trong thi cử sai một li đi 1 dặm

Cách 2: Dùng đệ quy
Đặc điểm:
- Siêu ngắn gọn
Nhược điểm:
- Khó hiểu hơn 1 tý nhưng hiểu rồi thì học rất lẹ
*/

const int MAX = 100;
int adj [MAX][MAX];
bool visited[MAX];
int n;

void DFS(int u) {
    visited[u] = true;

    // handle -> mọi xử lý hay việc muốn làm phải làm trước khi vào for

    for (int i = 0; i < n; i++){
        if (adj[u][i] == 1 && !visited[i]) {
            DFS (i);
        }
    }
}