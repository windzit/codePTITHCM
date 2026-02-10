#BẢNG XẾP HẠNG
def cmpAccount(l, r):
    if l[1] > r[1]: return True
    elif l[1] < r[1]: return False
    
    elif l[2] < r[2]: return True
    elif l[2] > r[2]: return False
    
    return l[0] < r[0]

def quickSort(arr, s, e):
    if s >= e: return
    
    p = arr[(s+e) // 2]
    
    l, r = s, e
    while l <= r:
        while cmpAccount(arr[l], p): l+=1
        while cmpAccount(p ,arr[r]): r-=1
        
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            
            l += 1
            r -= 1
    
    quickSort(arr, s, r)
    quickSort(arr, l, e)
            
accs = list() 
for _ in range(int(input())):
    acc = []
    acc.append(input().strip())
    acc += list(map(int, input().split()))
    
    accs.append(acc)

#You can test ver1 or ver2 :)))
def ver1(arr):
    quickSort(arr, 0, len(arr) - 1)
    for acc in arr: print(*acc)

def ver2(arr):
    arr = sorted(arr, key=lambda x: (-x[1], x[2], x[0]))
    for acc in arr: print(*acc)

ver2(accs)