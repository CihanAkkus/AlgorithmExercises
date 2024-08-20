def fibonacci(a,b,n,c = 0):

    sum = a + b
    print(sum)
    if (c >= n):
        return
    if (c % 2 == 0):
        fibonacci(a,sum,n,c+1)
    else:
        fibonacci(sum,b,n,c+1)

a,b = 1,1

print(a)
print(b)

fibonacci(a,b,10)