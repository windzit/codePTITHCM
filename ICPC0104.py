#TÌM SỐ NHỎ NHẤT
import re

loop = int(input())

for _ in range(loop):
    context = input()
    minNumber = min( list(map(int, re.findall(r"\d+", context))) )
    print(minNumber)