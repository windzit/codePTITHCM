#ĐỊA CHỈ IP
def checkIP(ip):
    nums = ip.split(".")
    if len(nums) != 4:
        return False

    for x in nums:
        if not x.isdigit() or not (0 <= int(x) <= 255):
            return False

    return True


for _ in range(int(input())):
    print(
        "YES" if checkIP(input())
        else "NO"
    )
