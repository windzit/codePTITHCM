#VỊ TRÍ NGUYÊN TỐ


for _ in range(int(input())):
    N = input()    
    size = len(N)
    primes = [True] * size
    primes[0] = primes[1] = False
    for i in range(2, int(size**0.5) + 1):
        if primes[i]:
            for j in range(i*i, size, i):
                primes[j] = False

    basicPrime = {2, 3, 5, 7}
    i = 0
    while i<size:
        num = int(N[i])
        if (not primes[i] or not num in basicPrime) and (primes[i] or num in basicPrime):
            break
        i += 1

    print("YES" if i == size else "NO")