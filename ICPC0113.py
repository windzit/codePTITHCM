#EMIRP NUMBER
for _ in range(int(input())):
    N = int(input())
    MAXN = N + 1
    is_prime = [True] * MAXN
    is_prime[0] = is_prime[1] = False


    for i in range(2, MAXN):
        if is_prime[i]:
            for j in range(i*2, MAXN, i):
                is_prime[j] = False
    
    check = set()
    
    for i in range(2, N+1):
        if not is_prime[i] or i in check:
            continue
        
        reverse = int(str(i)[::-1])
        
        if reverse == i or reverse > N:
            continue
        
        if is_prime[reverse]:
            check.update([i, reverse])
            print(i, reverse, end=" ")
    print()
        