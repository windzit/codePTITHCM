'''
3
1 2 3
2 1 4
3 4 1
'''


adj = []
n = int(input())
for _ in range(n):
    adj.append(list(map(int, input().strip().split())))

def check (adj : list):
    for i in adj:
        if n != len(i):
            return False
    
    for i in range(n):
        for j in range(n):
            if adj[i][j] != adj[j][i]:
                return False
    
    return True

print("YES" if check(adj) else "NO")