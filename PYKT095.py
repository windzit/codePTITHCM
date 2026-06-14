# TÍNH TIỀN ĐIỆN
loai = {
    'A': 100,
    'B': 500,
    'C': 200
}

users = []

for i in range(int(input())):
    name = ' '.join(input().title().split())
    datas = input().strip().split()

    f = datas[0]
    bef = int(datas[1])
    af = int(datas[2])
    Elec = af - bef

    if Elec > loai[f]:
        MoneyIn = loai[f] * 450
        MoneyOut = (Elec - loai[f]) * 1000
        ThueVAT = MoneyOut // 20
    else:
        MoneyIn = Elec * 450
        MoneyOut = 0
        ThueVAT = 0

    Total = MoneyIn + MoneyOut + ThueVAT

    users.append((f"KH{i + 1:02d} {name} {MoneyIn} {MoneyOut} {ThueVAT}", Total))

for u in sorted(users, key = lambda x : -x[1]):
    print(f'{u[0]} {u[1]}')