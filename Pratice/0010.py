import json

f = open ('./Pratice/0010.json', 'r', encoding='utf-8')

data = json.loads(f.read())

flights = data['flights']

def sumAll(s: str, e: str):
    count = 0
    for f in flights:
        if s <= f['year'] <= e:
            count += f['passengers']

    return 'Invalid' if count == 0 else count

allTest = []
for _ in range(int(input())):
    allTest.append( tuple(map(str, input().strip().split(" "))) )

for t in allTest:
    print(sumAll(t[0], t[1]))

    
    