#MÃ HÓA 2
P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
def findP(char):
    if char == '_': return 26
    if char == ".": return 27
    return ord(char) - ord("A")

while True:
    cell = input().split(" ")
    if cell[0] == "0": break
    
    content = list()
    for c in cell[1]:
        content.append(P[(int(cell[0]) + findP(c)) % 28])

    print(''.join(content[::-1]))