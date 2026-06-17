#include <iostream>
#include <stack>
#include <vector>
using namespace std;

const int MAX = 100;
int adj[MAX][MAX];
int n;


vector<int> EulerCycle (int start) 
{
    stack <int> s;
    vector <int> CE;

    s.push(start);

    while (!s.empty())
    {
        int u = s.top();
        
        int v;
        
        for(v = 0; v < n; v++)
        {
            if (adj[u][v] == 1) 
            {
                s.push(v);

                adj[u][v] = 0;
                adj[v][u] = 0;

                break;
            }
        }

        if (v == n)
        {
            CE.push_back(u);

            s.pop();
        }
    }

    reverse(CE.begin(), CE.end());
    return CE;
}