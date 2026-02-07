#SỐ ĐẢO NGUYÊN TỐ CÙNG NHAU
import math

for _ in range(int(input())):
    N = input("")
    reverse = int(N[::-1])
    N = int(N)

    print("YES" if math.gcd (N, reverse) == 1 else "NO")