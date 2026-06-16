import math
x = []
y = []

n = int(input())
for _ in range(n):
    x.append(list(map(int, input().strip().split())))
    y.append(list(map(int, input().strip().split())))

for i in range(n):
    L = len(x[i])
    if L != len(y[i]):
        print("INVALID")
        continue
    
    d = 0
    xy = 0
    for j in range (L):
        d += (y[i][j] - x[i][j]) ** 2
        xy += y[i][j] * x[i][j]

    d = math.sqrt(d)
    print(f'{round(d, 2):.2f} {xy}')