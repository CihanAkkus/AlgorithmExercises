def prime_number(num):
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

while True:
    num = input("Please enter a number, if you wanna quit press q = ")
    if(num == "q"):
        print("System is shutting down...")
        break
    else:
        num = int(num)
        if(prime_number(num)):
            print("The number you entered is a prime number")
        else:
            print("The number you entered is not a prime number")