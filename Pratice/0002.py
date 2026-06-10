def check(N):
    count = 0
    for n in N:
        if count > 5:
            return False
        if n == '3' or n == '5':
            count += 1

    return count == 3 or count == 5

def main():
    number = input()
    print('YES' if check (number) else 'NO')

if __name__ == "__main__":
    main()