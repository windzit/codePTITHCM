#TỔNG CHỮ SỐ THUẬN NGHỊCH
for _ in range(int(input())):
    N = str(sum(map(int, input()))) 
    print("YES" if len(N) > 1 and N == N[::-1] else "NO")
    
