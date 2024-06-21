num = int(input("Please enter the height of the triangle = "))

i = num-1
j = 1

while(i >= 0):
    print(" "*i, end="")
    i -= 1
    while(j <= num):
        print("*"*(2*j-1))
        j += 1
        break
