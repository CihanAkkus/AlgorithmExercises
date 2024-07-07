def firstUnique(s):
    count = 0
    for i in s:
        for j in s:
            if (i != j):
                count += 1
                
                