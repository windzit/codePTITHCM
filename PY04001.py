#LỚP POINT
for _ in range(int(input())):
    N = list(map(float, input().split()))

    p1 = N[0:2]
    p2 = N[2:]

    result = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) **0.5

    print(f"{result:.4f}")