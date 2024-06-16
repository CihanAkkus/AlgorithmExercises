def div(num):
    list = []
    for i in range(1,(num+1)):
        if(num % i == 0):
            list.append(i)
    return list

while True:
    num = input("Please enter a number, if you wanna quit press q = ")
    if(num == "q"):
        print("The system is shutting down...")
        break
    else:
        num = int(num)
        print("sub-multiples =",div(num))