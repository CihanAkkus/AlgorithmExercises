def isHappy(n):
    seen = set()
    while True:
        sum = 0
        copy_num = str(n)
        for i in range(0, len(copy_num)):
            sum += int(copy_num[i]) ** 2
        n = sum
        if n == 1:
            return True
        if n in seen:
            return False
        seen.add(n)