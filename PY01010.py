#ĐẦU CUỐI
for _ in range(int(input())):
    N = str(input())
    size = len (N)
    print(
        "YES" if N[0:2] == N[size - 2: size]  else "NO"
    )