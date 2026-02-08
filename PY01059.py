#TỔNG CHỮ SỐ - TÍCH CHỮ SỐ
for _ in range(int(input())):
    N = input()
    
    tong = sum(map(int, N[::2]))
    
    tich = 0
    i = 1
    size = len (N)
    while i < size:
        num = int(N [i])
        if num != 0:
            tich = num if tich == 0 else (tich * num)
        i+=2
        
    print(tong, tich)