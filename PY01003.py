#LÀM TRÒN SỐ

def lamTron(num):
    digits = list(map(int, str(num)))
    i = len(digits) - 2
    while (i > -1):
        if digits[i + 1] >= 5:
            digits[i] += 1
        digits[i + 1] = 0
        i -= 1
    return ''.join(map(str, digits))


for _ in range(int(input())):
    print(lamTron(int(input())))