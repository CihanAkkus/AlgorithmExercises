num = int(input("Please, enter a number : "))

i = 1
sum = 0

while (i < num):
    if (num % i == 0):
        sum += i
    i += 1

if (sum == num):
    print("The number you entered is perfect number")
else:
    print("The number you entered is not perfect number")
