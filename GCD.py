def EBOB(num1, num2):
    if num1 == num2:
        print("EBOB =", num1)
    elif num1 > num2:
        multiplication = 1
        for i in range(2, num2 + 1):
            while (num1 % i == 0) and (num2 % i == 0):
                multiplication *= i
                num1 //= i
                num2 //= i
        print("EBOB =", multiplication)
    else:
        multiplication = 1
        for i in range(2, num1 + 1):
            while (num1 % i == 0) and (num2 % i == 0):
                multiplication *= i
                num1 //= i
                num2 //= i
        print("EBOB =", multiplication)

num1 = int(input("Please enter the first number = "))
num2 = int(input("Please enter the second number = "))

EBOB(num1, num2)