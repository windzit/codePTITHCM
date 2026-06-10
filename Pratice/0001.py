
def kientra(s):
    s = s.lower()
    if len(s) % 2 == 0:
        return False
    
    for c in s:
        if c.isdigit():
            return False
    
    return s == s[::-1]

def main():
    N = int(input())
    
    allTest = list()
    for i in range(N):
        allTest.append(input())

    for t in allTest:
        print('YES' if kientra(t) else 'NO')


if __name__ == "__main__":
    main()