def isPalindrome(num):
    if (num / 10 < 1 and num / 10 > 0):
        return True
    backup = num
    backup2 = num
    digit = 1
    while(True):
        if (backup // 10 != 0):
            digit += 1
            backup = backup // 10
        elif (backup // 10 == 0):
            break
    reverse_num = 0
    while (digit > 0):
        step = backup2 % 10
        reverse_num = reverse_num + (step * (10 ** (digit-1)))
        digit -= 1
        backup2 = backup2 // 10
    if (num == reverse_num):
        return True
    else:
        return False

print(isPalindrome(11))
