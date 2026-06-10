base5 = {'0', '1', '2', '3', '4'}

def check (t):
    count = 0

    for c in t:
        if c.isdigit() and c in base5:
            count += int(c)
            continue
        return False

    return count == 5

allTest = list()
for _ in range(int(input())):
    allTest.append(input())

for t in allTest:
    print('YES' if check(t) else 'NO')
    