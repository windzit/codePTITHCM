#SỐ TĂNG GIẢM
def check(num):
    size = len(num)
    if size < 3: return False
    i = 1
    stats = False
    while i < size:
        if  num[i-1] >= num[i]:
            stats = True
            break
        i+=1

    while i < size:
        if  num[i-1] <= num[i]:
            return False
        i+=1
    
    return stats

for _ in range(int(input())):
    print("YES" if check(input()) else "NO")