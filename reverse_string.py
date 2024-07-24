def reverseString(s):
    s = list(s)
    for i in range(1,len(s)):
        for j in range(0, len(s) - i ):
            s[j], s[j + 1] = s[j + 1], s[j]
    return s


