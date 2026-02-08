#TÍNH ĐIỂM TRUNG BÌNH
T = int(input()) #Tà đạo
N = list(map(float, input().split()))

Max = max(N)
Min = min(N)

N = [x for x in N if x != Max and x != Min]

avg = sum(N) / len(N)

print(f"{avg:.2f}")