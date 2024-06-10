a,b = 1,1

num = int(input("Please enter how many steps you will proceed : "))

print(a)
print(b)


for i in range(0,num):
    sum = a + b
    print(sum)

    if (i % 2 == 0):
        b = sum
    else:
        a = sum