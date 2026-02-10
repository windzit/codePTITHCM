#SẮP XẾP THEO TÍCH CHỮ SỐ
def mul(a):
    result = 1
    for i in a: result *= i
    return result

def cmpMUL(a, b):
    A = mul(map(int, str(a)))
    B = mul(map(int, str(b)))
    if A == B:
        return a < b
    return A < B

def quickSort(nums, start, end):
    if start >= end: return
    pivot = nums[(start + end) // 2]
    
    s, e = start, end
    while s <= e:
        
        while cmpMUL(nums[s], pivot): s+=1
        while cmpMUL(pivot, nums[e]): e-=1
        
        if s <= e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        
    quickSort(nums, start, e)
    quickSort(nums, s, end)

for _ in range(int(input())):
    T = int(input())
    N = list(map(int, input().split()))
    quickSort(N, 0, T - 1)
    print(*N)