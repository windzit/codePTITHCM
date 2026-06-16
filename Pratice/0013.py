import json

n = int(input())
allTest = []
for _ in range(n):
    t = json.loads(input())
    allTest.append(t)

for t in allTest:
    sc = 0
    ss = 0
    ds = []
    
    for k in t:
        T = type(t[k])
        if T == str:
            ss += 1
        elif T == int:
            sc += t[k]
            if t[k] % 2 == 0:
                ds.append(k)


    print((ds, sc, ss))