def countBits(n):
    list = []
    for i in range(0,n+1):
        count = 0
        while (True):
            remainder = i % 2
            i = i // 2
            if (remainder == 1):
                count += 1
            if (i == 0):
                break
        list.append(count)
    return list
print(countBits(5))