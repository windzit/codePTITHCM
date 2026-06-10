import json

f = open('./Pratice/0009.json', 'r', encoding='utf-8')

data = json.loads(f.read())

f.close()

flights = {}

for d in data['flights']:
    key = (d['year'], d['month'])
    flights[key] = flights.get(key, 0) + d['passengers']

for _ in range(int(input())):
    date = input()
    k = tuple(map(str, date.split()))
    
    print(flights.get(k, 'Invalid'))
