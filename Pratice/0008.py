allTest = []

for _ in range(int(input())):
    allTest.append(input())

for t in allTest:
    if t[0:2] == t[::-1][0:2]:
        print('YES')
        continue
    print('NO')
