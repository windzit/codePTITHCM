#TÌM SỐ LỚN NHẤT
import re

loop = int(input())

for _ in range(loop):
    context = input()
    maxNumber = max( list(map(int, re.findall(r"\d+", context))) )
    print(maxNumber)