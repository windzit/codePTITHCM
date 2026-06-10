import math

def khoangcach (X, y):
    r = 0
    for i in range(len(X)):
        r += abs(X[i] - y[i]) ** 2
    
    return r**0.5

def tichvohuong (X, y):
    r = 0
    for i in range(len(X)):
        r += X[i] * y[i]
                 
    return r


def main():
    allTest = []
    for _ in range(int(input())):
        X = list(map(int, input().split()))
        y = list(map(int, input().split()))

        allTest.append([X, y])
    
    for t in allTest:
        print(f'{khoangcach(t[0], t[1]):.2f}', tichvohuong(t[0], t[1]))

if __name__ == "__main__":
    main()