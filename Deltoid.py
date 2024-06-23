num = int(input("Please enter the size of the deltoid = "))

i = num
j = 1

while(i >= 0):
    print(" "*i, end="")
    i -= 1
    while(j <= num):
        print("*"*(2*j-1))
        j += 1
        break

k = num-1
m = 1
while (k > 0):
    print(" "* (m),"*" * (2*k-1))
    k -= 1
    m +=1