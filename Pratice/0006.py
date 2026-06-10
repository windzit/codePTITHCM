def check(s):
    if len(s) != 8:
        return False
    
    end = len(s) - 1
    i = 0
    while i < end:
        if s[i] <= s[i + 1]:
            break
        i+=1
    
    if i == end - 1: 
        return False

    while i < end:
        if s[i] >= s[i + 1]:
            return False
        i+=1
    
    return True


allTest = []
for _ in range(int(input())):
    allTest.append(input())

for t in allTest:
    print('YES' if check(t) else 'NO')