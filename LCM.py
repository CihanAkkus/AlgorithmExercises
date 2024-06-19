def EKOK(num1,num2):
    multiplication = 1
    if(num1 < num2):
        for i in range(2,(num1+1)):
            if((num1 % i == 0) and (num2 % i == 0)):
                multiplication *= i
                num1 /= i
                num2 /= i
            if((num1 % i != 0) and (num2 % i == 0)):
                multiplication *= i
                num2 /= i
            if((num2 % i != 0) and (num1 % i == 0)):
                multiplication *= i
                num1 /= i
    if (num1 > num2):
        for i in range(2, (num2 + 1)):
            if ((num1 % i == 0) and (num2 % i == 0)):
                multiplication *= i
                num1 /= i
                num2 /= i
            if ((num1 % i != 0) and (num2 % i == 0)):
                multiplication *= i
                num2 /= i
            if ((num2 % i != 0) and (num1 % i == 0)):
                multiplication *= i
                num1 /= i


    print("EKOK =",multiplication)

num1 = int(input("Please enter the first number = "))
num2 = int(input("Please enter the second number = "))

EKOK(num1,num2)
