
# INPUT
allTest = list()
for _ in range(int(input())):
    allTest.append([input(), input()])

for t in allTest:
    s1, s2 = t

    s1 = set(s1.lower().split())
    s2 = s2.split()

    print(*[i for i in s2 if i.lower() in s1])
