#DÃY SỐ HAMMING
import bisect
hammings = [1]
i2 = i3 = i5 = 0
MAXN = 10**18
while hammings[-1] <= MAXN :
    nextNumber = min(hammings[i2]*2, hammings[i3]*3, hammings[i5]*5)
    hammings.append(nextNumber)
    
    if nextNumber == hammings[i2]*2: i2 += 1
    if nextNumber == hammings[i3]*3: i3 += 1
    if nextNumber == hammings[i5]*5: i5 += 1
    
for i in range(int(input())):
    N = int(input())
    
    pos = bisect.bisect_left(hammings, N)
    print(pos + 1 if hammings[pos] == N else "Not in sequence")
    
    
