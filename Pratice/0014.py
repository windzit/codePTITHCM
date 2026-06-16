import json

n = int(input())
allTest = []
for _ in range(n):
    t = json.loads(input())
    allTest.append(t)

nguyenam = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for t in allTest:
    dk1 = []
    dk2 = 0
    dk3 = 0
    
    for k in t:
        if t[k][0] in nguyenam:
            dk1.append(k)
        
        if len(k) > 5:
            dk2 += 1

        if len(t[k]) < 6:
            dk3 += 1

    print((dk1, dk2, dk3))