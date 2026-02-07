#GIẢI MÃ
for _ in range(int(input())):
    X = input()
    text = ""
    for i in range(0, len(X), 2):
        text += X[i] * int(X[i+1])
    print(text)