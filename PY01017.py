#MÃ HÓA 1
for _ in range(int(input())):
    X = input()
    count = 0
    char = X[0]
    Encodes = list()
    for c in X:
        if char != c:
            Encodes.append(str(count) + char)
            count = 1
            char = c
        else:
            count += 1
    Encodes.append(str(count) + char)
    print(''.join(Encodes))