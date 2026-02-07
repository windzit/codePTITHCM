# SỐ MAY MẮN
import re
N = str(input())
sumOf7and4 = len(re.findall(r"[7]", N)) + len(re.findall(r"[4]", N))
print("YES" if (sumOf7and4 == 4 or sumOf7and4 == 7) else "NO")