#EMIRP NUMBER

MAXN = 10**6 + 1
is_prime = [True] * MAXN
is_prime[0] = is_prime[1] = False


for i in range(2, MAXN): #create list prime 2->10^6
    if is_prime[i]:
        for j in range(i*2, MAXN, i):
            is_prime[j] = False

for _ in range(int(input())):
    N = int(input())
    
    check = set()
    result = []
    
    for i in range(2, N+1):
        if not is_prime[i] or i in check:
            continue
        
        reverse = int(str(i)[::-1])
        
        if reverse == i or reverse > N:
            continue
        
        if is_prime[reverse]:
            check.update([i, reverse])
            result.extend([i, reverse])
            
    print(*result)
        