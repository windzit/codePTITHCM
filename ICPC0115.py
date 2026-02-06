#SỐ KRISH
import math

Fac = [0] * 10
for i in range(10):
    Fac[i] = math.factorial(i)
    

def isKrish(number):
    if number < 1:
        return False
    
    result = 0
    for i in str(number):
        result += Fac[int(i)]
    return number == result

for i in range( int(input()) ):
    N = int(input())
    print("Yes" if isKrish(N) else "No")
