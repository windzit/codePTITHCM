n = int(input())

allTest = []
for _ in range(n):
    name = input()
    sn = input().strip()
    mon1 = float(input())
    mon2 = float(input())
    mon3 = float(input())

    name = ' '.join(name.strip().split()).title()
    dtb = sum([mon1, mon2, mon3, min([mon1, mon2, mon3])]) / 4

    allTest.append((f'{name} {sn}', dtb))


allTest= sorted(allTest, key = lambda x : -x[1])

for t in allTest:
    print(f'{t[0]} {round(t[1], 1):.1f}')