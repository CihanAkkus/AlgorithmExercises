def isHappy(n):
    sum = 0
    while (True):
        copy_num = str(n)
        for i in range(0, len(str(n))):
            sum += int(copy_num[i]) ** 2
        n = sum
        if (sum == 1):
            return True
        sum = 0
print(isHappy(19))